# Blueprint Factory

Bản thiết kế hệ thống doanh nghiệp — **máy đọc được, người dùng được**.

Mỗi bộ blueprint là một bộ tài liệu kiến trúc hoàn chỉnh (whitepaper, BRD, solution architecture, capability spec, policy matrix, runbook) phát hành đồng thời hai ấn bản:

- **Human Edition** — HTML dàn trang chuẩn xuất bản, để hiểu và ra quyết định.
- **Agent Pack** — YAML/JSON có ID chuẩn, decision table, tham số chờ điền — thả vào Claude Code / Cursor / AI agent là bắt đầu thực thi.

Phép thử của mỗi bản phát hành: nạp Agent Pack vào một coding agent sạch và yêu cầu scaffold — đạt chuẩn khi agent không phải hỏi lại điều blueprint đã trả lời.

Tất cả blueprint theo phương pháp luận **FlowX**: 5 tầng Trigger → Flow → Capability → Policy → Runtime, mỗi tầng trả lời đúng một câu hỏi.

## Thư viện

| ID | Blueprint | Trạng thái | Agent Pack |
|---|---|---|---|
| BP-01 | [FlowX CRM](crm/crm.md) | Đã phát hành v1.0.0 | [crm-blueprint-pack.zip](crm/crm-blueprint-pack.zip) |
| BP-02 | FlowX ERP Lite | Q4/2026 | — |
| BP-03 | FlowX Helpdesk | Q4/2026 | — |
| BP-04 | FlowX HRM | 2027 | — |
| BP-05 | FlowX E-commerce | 2027 | — |
| BP-06 | FlowX Booking | 2027 | — |

Một phần của hệ sinh thái **AI Business Architect**. Xem thêm: [llms.txt](llms.txt)
