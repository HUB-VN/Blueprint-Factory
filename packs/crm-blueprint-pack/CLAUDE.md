# FlowX CRM Blueprint Pack — Hướng dẫn cho AI Agent

## 1. Pack này là gì

Đây là **Agent Pack** của bộ blueprint FlowX CRM: bản thiết kế cấp kiến trúc + nghiệp vụ cho một nền tảng CRM đa kênh, ở dạng máy đọc được. Nó là đầu vào để bạn (AI agent) phân tích, viết PRD, hoặc scaffold hệ thống — không phải tài liệu marketing. Ấn bản cho người đọc (Human Edition) ở URL trong `manifest.json`.

## 2. Thứ tự đọc

1. `manifest.json` — inventory và version
2. `blueprint/philosophy.md` — mô hình 5 tầng FlowX (2 phút, bắt buộc: nó quy định mọi ranh giới)
3. `blueprint/journey.yaml` — flow nghiệp vụ, gates G-1..G-5
4. `blueprint/requirements.yaml` — BR-01..BR-07 với acceptance criteria
5. `blueprint/services.yaml` — 15 service, dữ liệu sở hữu, phụ thuộc
6. `blueprint/policies.yaml` — luật chơi + enforcement points
7. `blueprint/architecture.yaml` — quyết định kiến trúc AD-01..05, runtime, hạ tầng
8. `blueprint/runbook.yaml` — chỉ cần khi làm phần vận hành
9. `agent-guides/<loại-của-bạn>.md` — hướng dẫn riêng theo vai trò

## 3. Điều bạn PHẢI hỏi người dùng trước khi build

Pack là blueprint tổng quát. Các tham số sau **cố ý để trống** (`value: null` trong `policies.yaml`) — hỏi trước, không tự bịa:

- Ngưỡng phê duyệt: `P-08.discount_threshold_pct`, `P-08.contract_value_threshold`
- Rate limit: `P-04.public_form_limit`, `P-04.partner_api_limit`
- Privacy: `P-05.erasure_sla_days`, `P-05.legal_basis` (thị trường VN → cân nhắc Nghị định 13/2023)
- Retention: `P-07.cold_lead_months`, `P-07.call_recording_months`
- Authorization: `P-01.ownership_scope`
- Lựa chọn công nghệ trong `architecture.yaml → runtime[].candidates` (Temporal vs Camunda, Kafka vs RabbitMQ) — đề xuất kèm trade-off rồi để người dùng chốt

Ngoài ra, hỏi về **ngành và quy trình bán thực tế** — journey trong pack là mẫu chuẩn, doanh nghiệp thật có thể cần thêm/bớt step (nhưng giữ nguyên cấu trúc phase-gate).

## 4. Ranh giới — pack KHÔNG chứa

- UI/UX design, wireframe, màn hình
- Mô hình dữ liệu chi tiết (ERD field-level) và API contract (OpenAPI) — bạn sinh ra chúng TỪ pack này
- Số liệu thật của doanh nghiệp cụ thể
- Lựa chọn vendor cuối cùng

## 5. Quy tắc khi sinh sản phẩm phái sinh

- **Luôn trích dẫn ID** (BR-03, P-08, SVC-LEAD…) trong code comment, PRD, ADR bạn viết — để truy vết ngược về blueprint
- Không vi phạm AD-01..AD-05; muốn làm khác → ghi rõ là deviation kèm lý do
- Không nhét logic gate vào service (xem `philosophy.md` anti-patterns)
- Mọi service scaffold phải có sẵn logging + tracing + health check (AD-05)
- MVP khuyến nghị: PH-1 → PH-3 (Lead → Opportunity) với SVC-LEAD, SVC-CONTACT, SVC-ACCOUNT, SVC-OPP, SVC-ACTIVITY, SVC-EMAIL + R-1, R-2, R-3 tối thiểu — chi tiết trong `agent-guides/coding-agent.md`
