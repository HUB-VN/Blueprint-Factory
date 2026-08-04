# FlowX CRM Blueprint (BP-01)

Bản thiết kế hoàn chỉnh cho nền tảng CRM đa kênh trọn vòng đời khách hàng. Phát hành theo chuẩn Dual Edition v1.0. Phiên bản: **1.0.0**.

## Nếu bạn là AI agent

Đừng scrape các trang HTML — tải [Agent Pack](crm-blueprint-pack.zip), giải nén, và bắt đầu từ `CLAUDE.md` trong pack. Pack chứa toàn bộ blueprint ở dạng YAML có ID chuẩn:

- `blueprint/journey.yaml` — 5 phase (PH-1..PH-5), 5 gate decision-table (G-1..G-5), 9 trigger (T-1..T-9)
- `blueprint/requirements.yaml` — BR-01..BR-07 kèm acceptance criteria
- `blueprint/services.yaml` — 15 service (SVC-*) với owned data + dependencies
- `blueprint/policies.yaml` — P-01..P-08, 4 enforcement point (E-1..E-4), tham số `value: null` = phải hỏi người dùng
- `blueprint/architecture.yaml` — AD-01..AD-05, runtime R-1..R-8, hạ tầng, 9 outcome
- `blueprint/runbook.yaml` — 4 health flow, kịch bản sự cố SC-01..SC-04
- `agent-guides/` — hướng dẫn riêng cho coding / business / product agent

Quy tắc quan trọng: trích dẫn ID trong mọi sản phẩm phái sinh; không tự bịa giá trị cho tham số `null`; MVP khuyến nghị = PH-1 → PH-3.

## Nếu bạn là người đọc

Human Edition gồm 7 tài liệu HTML: [Hub](docs/index.html) · [Whitepaper](docs/whitepaper.html) · [BRD](docs/brd.html) · [Architecture](docs/architecture.html) · [Capability Spec](docs/capabilities.html) · [Policy Matrix](docs/policies.html) · [Runbook](docs/runbook.html)

## Tóm tắt hệ thống

CRM nhận sự kiện từ 9 nguồn (web/API, email, phone, social, live chat, campaign, partner, scheduler, AI agent) đổ về một journey duy nhất: Lead Management → Engagement → Opportunity → Delivery → Loyalty, với 5 điểm quyết định (Qualified? Interested? Won? In Stock? Issue?) và 2 vòng nurture. 15 capability service chia 3 cụm (Customer / Commerce / Engagement), 8 policy cắt ngang cưỡng chế tại 4 điểm, chạy trên runtime 8 thành phần (workflow engine, rule engine, event bus, scheduler + observability) trên hạ tầng cloud-native. Đầu ra là 9 dòng tích hợp, trong đó AI/ML vừa là outcome vừa là trigger — vòng lặp học khép kín.

License: CC BY-NC 4.0 · [← Blueprint Factory](../index.md)
