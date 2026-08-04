# Blueprint Factory

**Enterprise system blueprints that both humans and AI agents can use.**

Every blueprint here ships in two synchronized editions from a single source of truth:

- **Human Edition** — publication-quality HTML documentation (whitepaper, BRD, solution architecture, capability spec, policy matrix, runbook) for reading and decision-making.
- **Agent Pack** — the same blueprint as structured YAML/JSON with standardized IDs, machine-followable decision tables, and deliberately-blank parameters. Drop it into Claude Code / Cursor and your agent starts building.

```
┌─────────────────────────────────────────────────────────┐
│                ONE SOURCE OF TRUTH (YAML)               │
│   journey · requirements · services · policies · arch   │
└────────────────┬───────────────────────┬────────────────┘
                 ▼                       ▼
        HUMAN EDITION              AGENT PACK
        HTML docs, read         CLAUDE.md + YAML,
        & decide                 load & execute
```

**The release test:** load an Agent Pack into a clean coding agent and ask it to scaffold the system. A release passes when the agent never has to ask a question the blueprint already answers.

## 📦 Blueprints

| ID | Blueprint | Status | Agent Pack |
|---|---|---|---|
| BP-01 | **FlowX CRM** — omnichannel CRM covering the full customer lifecycle: 9 triggers, 5-phase journey with decision gates, 15 services, 8 policies, ops runbook | ✅ v1.0.0 | [`packs/crm-blueprint-pack/`](packs/crm-blueprint-pack/) |
| BP-02 | FlowX ERP Lite | 🔜 Q4/2026 | — |
| BP-03 | FlowX Helpdesk | 🔜 Q4/2026 | — |
| BP-04 | FlowX HRM | 🗓 2027 | — |
| BP-05 | FlowX E-commerce | 🗓 2027 | — |
| BP-06 | FlowX Booking | 🗓 2027 | — |

## 🚀 Use with a coding agent (30 seconds)

```bash
git clone https://github.com/HUB-VN/Blueprint-Factory.git
```

Then, in Claude Code / Cursor, from your project:

> "Read `Blueprint-Factory/packs/crm-blueprint-pack/CLAUDE.md` and start Milestone 0 following the coding-agent guide."

The agent will read the blueprint, **ask you** for the deliberately-blank business parameters (discount approval threshold, data retention, rate limits — it never invents them), and build milestone by milestone, citing blueprint IDs (`BR-03`, `SVC-LEAD`, `P-08`…) in every artifact it produces.

Also works for non-coding agents: `agent-guides/business-agent.md` (gap analysis, build-vs-buy scorecards) and `agent-guides/product-agent.md` (PRD, epic maps, roadmaps).

## 🧭 The FlowX methodology

All blueprints follow one architecture philosophy — five layers, each answering exactly one question:

| Layer | Question |
|---|---|
| **Trigger** | What initiates work? |
| **Flow** | How does the business process unfold? |
| **Capability** | Which building blocks execute? |
| **Policy** | What rules constrain everything? |
| **Runtime** | What platform runs it reliably? |

The arrow direction is also the rate-of-change direction: triggers and flows change weekly, capabilities quarterly, policies when the rules change, runtime almost never. Proper layering isolates change velocity. Full spec: [`standard/DUAL-EDITION-STANDARD.md`](standard/DUAL-EDITION-STANDARD.md).

## 📖 Human Edition

Browse the rendered documentation in [`site/`](site/) (open `site/index.html` locally, or via GitHub Pages once enabled). Vietnamese-first; English editions planned.

## 🗂 Repository layout

```
standard/     Dual Edition Publishing Standard (the spec every pack follows)
packs/        Agent Packs — one folder per blueprint, start at CLAUDE.md
site/         Human Edition — static site incl. full HTML documentation
tools/        Pack validator (YAML parse, ID cross-refs, manifest checksums)
```

## 🤝 Contributing

Issues and PRs welcome — especially real-world feedback from running packs against agents. See [CONTRIBUTING.md](CONTRIBUTING.md). Every PR runs `tools/validate_pack.py` in CI.

## 📄 License

Dual-licensed: **blueprint content** (packs, site, standard) under [CC BY-NC 4.0](LICENSE-CONTENT.md) — free for non-commercial use with attribution, contact us for commercial licensing; **tooling and schemas** (`tools/`, `schemas/`) under [MIT](LICENSE).

---

## 🇻🇳 Tiếng Việt

Blueprint Factory là thư viện **bản thiết kế hệ thống doanh nghiệp** phát hành theo chuẩn Dual Edition: mỗi bộ có **Human Edition** (tài liệu HTML để đọc và ra quyết định) và **Agent Pack** (YAML/JSON máy đọc được — thả vào Claude Code / Cursor là agent bắt đầu xây). Nội dung hiện tại viết bằng tiếng Việt. Đọc đầy đủ: [README.vi.md](README.vi.md).

Một phần của hệ sinh thái **AI Business Architect**.
