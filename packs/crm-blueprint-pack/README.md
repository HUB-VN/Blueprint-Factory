# FlowX CRM Blueprint Pack

**Agent Pack** — ấn bản máy-đọc-được của bộ blueprint FlowX CRM, dành cho AI agent (coding / business / product). Ấn bản cho người đọc: xem `manifest.json → publisher.edition_human`.

## Dùng thế nào (30 giây)

**Với Claude Code / Cursor:** thả cả thư mục này vào repo của bạn (hoặc `--add-dir`), rồi ra lệnh:
> "Đọc CLAUDE.md trong crm-blueprint-pack và bắt đầu Milestone 0 theo coding-agent guide."

**Với agent phân tích/PM:** đính kèm thư mục vào cuộc hội thoại, trỏ agent tới `agent-guides/business-agent.md` hoặc `product-agent.md`.

## Bên trong

- `CLAUDE.md` — file mồi: thứ tự đọc, tham số phải hỏi, ranh giới, quy tắc trích ID
- `blueprint/` — nguồn sự thật: journey, requirements, services, policies, architecture, runbook (YAML có ID chuẩn)
- `agent-guides/` — hướng dẫn theo vai trò agent
- `schemas/` — JSON Schema để validate manifest

## Versioning

SemVer, đồng bộ với Human Edition. Xem `manifest.json`. Phát hành theo chuẩn **Dual Edition Publishing Standard v1.0** của hệ sinh thái AI Business Architect.

## License

CC BY-NC 4.0 — dùng tự do cho mục đích phi thương mại, ghi nguồn. Dùng thương mại: liên hệ publisher.
