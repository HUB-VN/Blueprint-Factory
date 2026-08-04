#!/usr/bin/env python3
"""Blueprint Factory pack validator.

Checks a Dual Edition Agent Pack for:
  1. YAML parseability of every blueprint/*.yaml
  2. Null-key corruption (unquoted commas in flow mappings)
  3. ID cross-references — every referenced ID is declared somewhere in the pack
  4. Required files present per manifest, with matching sha256 checksums
  5. manifest.json validity against schemas/pack.schema.json

Usage:  python tools/validate_pack.py packs/crm-blueprint-pack
Exit 0 = pack valid, exit 1 = errors (printed to stdout).
"""
import hashlib
import json
import os
import re
import sys

try:
    import yaml
    import jsonschema
except ImportError:
    print("Missing deps — run: pip install pyyaml jsonschema")
    sys.exit(2)

ID_PATTERN = re.compile(
    r"\b(BR|AD|SVC|PH\d?|G|T|R|O|SC|E|CC|CL|HF|INF|FLOW|P)-[A-Z0-9]+\b"
)
# IDs allowed to appear without declaration (illustrative examples in guides)
ALLOWLIST = {"BR-08"}


def validate(pack_dir: str) -> list[str]:
    errors: list[str] = []
    bp_dir = os.path.join(pack_dir, "blueprint")

    # 1–2: parse YAML + null-key check
    docs = {}
    for fname in sorted(os.listdir(bp_dir)) if os.path.isdir(bp_dir) else []:
        if not fname.endswith(".yaml"):
            continue
        path = os.path.join(bp_dir, fname)
        try:
            docs[fname] = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{fname}: PARSE ERROR {exc}")

    def check_nulls(node, path, fname):
        if isinstance(node, dict):
            for key, val in node.items():
                if val is None and key != "value":
                    errors.append(
                        f"{fname}: null at {path}/{key} (unquoted comma?)"
                    )
                check_nulls(val, f"{path}/{key}", fname)
        elif isinstance(node, list):
            for i, val in enumerate(node):
                check_nulls(val, f"{path}[{i}]", fname)

    for fname, doc in docs.items():
        check_nulls(doc, "", fname)

    # 3: ID cross-references
    declared = set()

    def collect(node):
        if isinstance(node, dict):
            for key in ("id", "component"):
                if isinstance(node.get(key), str):
                    declared.add(node[key])
            for val in node.values():
                collect(val)
        elif isinstance(node, list):
            for val in node:
                collect(val)

    for doc in docs.values():
        collect(doc)

    referenced = set()
    for root, _, files in os.walk(pack_dir):
        for fname in files:
            if fname.endswith((".yaml", ".md")):
                text = open(os.path.join(root, fname), encoding="utf-8").read()
                referenced |= {m.group(0) for m in ID_PATTERN.finditer(text)}

    unresolved = sorted(referenced - declared - ALLOWLIST)
    if unresolved:
        errors.append("Unresolved ID refs: " + ", ".join(unresolved))

    # 4–5: manifest + schema + checksums
    manifest_path = os.path.join(pack_dir, "manifest.json")
    schema_path = os.path.join(pack_dir, "schemas", "pack.schema.json")
    if not os.path.exists(manifest_path):
        errors.append("MISSING manifest.json")
        return errors
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    if os.path.exists(schema_path):
        try:
            jsonschema.validate(manifest, json.load(open(schema_path)))
        except jsonschema.ValidationError as exc:
            errors.append(f"manifest.json schema error: {exc.message}")
    for entry in manifest.get("files", []):
        fpath = os.path.join(pack_dir, entry["path"])
        if not os.path.exists(fpath):
            errors.append(f"manifest lists missing file: {entry['path']}")
            continue
        digest = hashlib.sha256(open(fpath, "rb").read()).hexdigest()[:16]
        if entry.get("sha256") and entry["sha256"] != digest:
            errors.append(
                f"checksum mismatch: {entry['path']} "
                f"(manifest {entry['sha256']}, actual {digest})"
            )
    return errors


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    failed = False
    for pack_dir in sys.argv[1:]:
        errs = validate(pack_dir)
        label = os.path.basename(os.path.normpath(pack_dir))
        if errs:
            failed = True
            print(f"✗ {label}: {len(errs)} error(s)")
            for err in errs:
                print(f"  - {err}")
        else:
            print(f"✓ {label}: valid")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
