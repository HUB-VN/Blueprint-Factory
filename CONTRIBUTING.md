# Contributing to Blueprint Factory

Cảm ơn bạn quan tâm! / Thanks for your interest!

## What we welcome most

1. **Field reports** — you loaded a pack into an agent (Claude Code, Cursor, custom) and something worked or broke. Open an issue with the agent, the prompt, and what happened. This is the single most valuable contribution: the release test of every pack is "the agent never asks what the blueprint already answers."
2. **Fixes to existing packs** — wrong cross-reference, unclear rule, missing acceptance criterion.
3. **Translations** — English editions of existing Vietnamese content.
4. **New blueprint proposals** — open an issue first describing the system and its journey before writing a pack.

## Ground rules for pack changes

- Every entity has a standardized ID (`BR-`, `SVC-`, `P-`, `G-`, `PH-`…). IDs are never reused after deletion. Breaking changes bump `schema_version` in `manifest.json`.
- Business parameters that depend on a real organization stay `value: null` with a `note` telling the agent to ask. Never fill them with invented defaults.
- YAML flow-mapping values containing commas, colons, or `?` must be quoted.
- The five FlowX layers stay separate: no gate logic inside services, no thresholds hard-coded in flows.
- One source of truth: change the YAML in `packs/`, then regenerate the Human Edition — never hand-edit rendered HTML content.

## Before you open a PR

Run the validator:

```bash
pip install pyyaml jsonschema
python tools/validate_pack.py packs/crm-blueprint-pack
```

It checks YAML parseability, null-key corruption, ID cross-references, and manifest checksums. CI runs the same script on every PR.

## Versioning

SemVer per pack: patch = wording fixes, minor = new entities, major = schema/ID changes. Update `manifest.json` version and note the change in `CHANGELOG.md`.
