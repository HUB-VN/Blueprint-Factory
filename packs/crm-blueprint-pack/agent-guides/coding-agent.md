# Coding Agent Guide — Scaffold hệ thống từ pack

Bạn là coding agent (Claude Code, Cursor…) được yêu cầu xây CRM theo blueprint này. Đọc `CLAUDE.md` trước. Sau khi hỏi đủ tham số (mục 3 của CLAUDE.md), build theo milestone:

## Milestone 0 — Nền móng (trước mọi feature)
1. Monorepo hoặc polyrepo theo lựa chọn người dùng; template service chuẩn có sẵn: structured logging + correlation_id, health endpoint, tracing hook (AD-05)
2. Event schema thống nhất: `{source, type, payload, timestamp, correlation_id}` (AD-01)
3. Event bus (R-3) + một consumer mẫu idempotent
4. Middleware chung: authorization (P-01) + validation (P-02) — thư viện, không copy-paste

## Milestone 1 — MVP dọc: PH-1 Lead Management
- Services: SVC-CONTACT (trước — mọi thứ phụ thuộc nó), SVC-LEAD, SVC-EMAIL, SVC-CAMPAIGN (tối thiểu)
- Trigger đầu tiên: T-1 (web form) qua API gateway có P-03, P-04
- Gate G-1 chạy trên rule engine (R-2) — rule là config, không if/else trong code
- Nurture loop của G-1 on_no chạy được end-to-end
- Definition of done: BR-01, BR-02 acceptance criteria pass

## Milestone 2 — PH-2 + PH-3: Engagement → Opportunity
- SVC-ACCOUNT, SVC-ACTIVITY (BR-03: track tự động), SVC-OPP, SVC-PRICING, SVC-PRODUCT, SVC-DOC
- Workflow engine (R-1) điều phối phase transition thay vì code tự chuyển
- Approval gate (E-3, P-08) cho Proposal/Quote — ngưỡng đọc từ config
- Closed Lost bắt buộc lost_reason
- Definition of done: BR-04 pass; một deal đi từ lead → won không thao tác DB tay

## Milestone 3 — PH-4 + PH-5: Delivery → Loyalty
- SVC-ORDER, SVC-INVENTORY, SVC-PAYMENT, SVC-TASK; tích hợp O-ERP (mock trước, adapter thật sau)
- G-4 + nhánh procurement + notification BR-05
- G-5 + chặn upsell khi có ticket mở (BR-06)

## Milestone 4 — Cứng hóa
- P-05/P-06/P-07 ở data layer (E-4): consent, audit log bất biến, retention job trên R-4
- Observability dashboards theo `runbook.yaml → health_flows`
- Test policy độc lập (policies.yaml → testing_principle)

## Quy tắc xuyên suốt
- Mỗi PR/commit lớn ghi ID liên quan: `feat(lead): scoring via R-2 [BR-02, SVC-LEAD]`
- Không đọc chéo database service khác (AD-03) — cần dữ liệu thì API/event
- Sinh OpenAPI cho mỗi service TỪ services.yaml trước khi code endpoint
- Khi thấy mâu thuẫn trong pack → dừng, báo người dùng, không tự quyết
