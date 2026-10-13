# Blueprint Factory

**Bản thiết kế hệ thống doanh nghiệp — máy đọc được, người dùng được.**

Mỗi blueprint phát hành hai ấn bản đồng bộ từ một nguồn sự thật duy nhất:

- **Human Edition** — bộ tài liệu HTML chuẩn xuất bản (whitepaper, BRD, kiến trúc giải pháp, capability spec, ma trận policy, runbook) để đọc và ra quyết định.
- **Agent Pack** — cùng blueprint đó ở dạng YAML/JSON có ID chuẩn hóa, decision table máy theo được, tham số cố ý để trống. Thả vào Claude Code / Cursor là agent bắt đầu xây.

**Phép thử của mỗi bản phát hành:** nạp Agent Pack vào một coding agent sạch và yêu cầu scaffold hệ thống — đạt chuẩn khi agent không phải hỏi lại bất kỳ điều gì blueprint đã trả lời.

## Thư viện

| ID | Blueprint | Trạng thái |
|---|---|---|
| BP-01 | **FlowX CRM** — CRM đa kênh trọn vòng đời khách hàng: 9 trigger, journey 5 giai đoạn với gate quyết định, 15 service, 8 policy, runbook vận hành | ✅ v1.0.0 |
| BP-02 | FlowX ERP Lite | 🔜 Q4/2026 |
| BP-03 | FlowX Helpdesk | 🔜 Q4/2026 |
| BP-04 | FlowX HRM | 🗓 2027 |
| BP-05 | FlowX E-commerce | 🗓 2027 |
| BP-06 | FlowX Booking | 🗓 2027 |

## Implementation Kits

Kit áp một blueprint vào một ngành và một giai đoạn dự án cụ thể — tài liệu thực chiến cho đội triển khai, trích dẫn ID của blueprint.

| ID | Kit | Áp dụng | Trạng thái |
|---|---|---|---|
| KIT-01 | **Bộ tài liệu Kickoff triển khai CRM — Trường tư thục THCS & THPT**: 14 tài liệu trước/sau kickoff cho CRM Sales & Marketing: tuyển sinh mọi khối 6–12 (đầu cấp, chuyển trường, lên cấp, tái ghi danh), khoá ngắn hạn, sự kiện & chương trình đào tạo là sản phẩm; kênh, nguồn lead, chiến dịch ở dạng khám phá | BP-01 | ✅ v1.1.0 · [`kits/crm-school-kickoff/`](kits/crm-school-kickoff/) |

## Dùng trong 30 giây

```bash
git clone https://github.com/HUB-VN/Blueprint-Factory.git
```

Rồi trong Claude Code / Cursor:

> "Đọc `Blueprint-Factory/packs/crm-blueprint-pack/CLAUDE.md` và bắt đầu Milestone 0 theo coding-agent guide."

Agent sẽ đọc blueprint, **hỏi bạn** các tham số nghiệp vụ cố ý để trống (ngưỡng duyệt chiết khấu, retention, rate limit — không bao giờ tự bịa), và xây theo từng milestone, trích dẫn ID blueprint (`BR-03`, `SVC-LEAD`, `P-08`…) trong mọi sản phẩm sinh ra.

Không chỉ cho coding agent: `agent-guides/business-agent.md` (gap analysis, scorecard build-vs-buy) và `agent-guides/product-agent.md` (PRD, epic map, roadmap).

## Phương pháp luận FlowX

Năm tầng, mỗi tầng trả lời đúng một câu hỏi: **Trigger** (điều gì khởi phát?) → **Flow** (quy trình diễn ra thế nào?) → **Capability** (khối năng lực nào thực thi?) → **Policy** (luật chơi nào ràng buộc?) → **Runtime** (nền tảng nào thực thi?). Chiều mũi tên cũng là chiều tốc độ thay đổi — tách tầng đúng nghĩa là cô lập nhịp thay đổi. Spec đầy đủ: [`standard/DUAL-EDITION-STANDARD.md`](standard/DUAL-EDITION-STANDARD.md).

## Human Edition

Mở `site/index.html` để duyệt toàn bộ tài liệu HTML (hoặc qua GitHub Pages khi bật).

## Cấu trúc repo

```
standard/     Chuẩn Dual Edition Publishing (spec mọi pack tuân theo)
packs/        Agent Packs — mỗi blueprint một thư mục, bắt đầu từ CLAUDE.md
kits/         Implementation Kits — áp blueprint vào ngành/giai đoạn dự án cụ thể
site/         Human Edition — site tĩnh kèm toàn bộ tài liệu HTML
tools/        Validator (parse YAML, cross-ref ID, checksum manifest)
```

## License

Kép: **nội dung blueprint** (packs, site, standard) theo [CC BY-NC 4.0](LICENSE-CONTENT.md) — miễn phí phi thương mại kèm ghi nguồn, dùng thương mại liên hệ; **tooling và schema** (`tools/`, `schemas/`) theo [MIT](LICENSE).

Một phần của hệ sinh thái **AI Business Architect**.
