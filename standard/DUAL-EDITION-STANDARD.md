# Dual Edition Publishing Standard

**Phiên bản:** 1.0 · 08/2026 · AI Business Architect ecosystem
**Trạng thái:** Draft chuẩn hóa — áp dụng cho mọi bộ blueprint phát hành trên blog

---

## 1. Triết lý

Mỗi bộ tài liệu (blueprint) phát hành **hai ấn bản đồng bộ từ một nguồn duy nhất**:

| | Human Edition | Agent Pack |
|---|---|---|
| **Đối tượng** | Người đọc: founder, BA, architect, dev | AI agent: coding, business, product agent |
| **Định dạng** | HTML editorial (multi-page, đẹp, đọc được) | Thư mục file cấu trúc: YAML/JSON + Markdown sạch |
| **Mục đích** | Hiểu và ra quyết định | Nạp làm context và **thực thi** |
| **Giá trị** | Kiến thức | Thời gian (time-to-bootstrap) |
| **Đo lường** | Lượt đọc, thời gian đọc | Lượt tải pack, dự án khởi tạo từ pack |

**Nguyên tắc bất biến:** nguồn sự thật là các file cấu trúc (Agent Pack). Human Edition được *render từ* nguồn đó — không bao giờ viết tay hai lần. Sửa một chỗ, hai ấn bản cùng cập nhật.

## 2. Cấu trúc Agent Pack

```
<slug>-blueprint-pack/
├── manifest.json          # Metadata + inventory + checksum — agent đọc file này ĐẦU TIÊN
├── CLAUDE.md              # File mồi vạn năng: pack là gì, dùng thế nào, thứ tự đọc
├── README.md              # Cho người mở pack bằng mắt (1 trang)
├── blueprint/             # NGUỒN SỰ THẬT — dữ liệu cấu trúc
│   ├── philosophy.md      # Triết lý thiết kế (prose ngắn, markdown sạch)
│   ├── journey.yaml       # Flow nghiệp vụ: phases, steps, gates
│   ├── requirements.yaml  # Yêu cầu nghiệp vụ có ID + acceptance criteria
│   ├── services.yaml      # Danh mục capability/service
│   ├── policies.yaml      # Chính sách + điểm cưỡng chế + tham số
│   ├── architecture.yaml  # Quyết định kiến trúc, runtime, hạ tầng, tích hợp
│   └── runbook.yaml       # Vận hành: tín hiệu, cảnh báo, kịch bản sự cố
├── agent-guides/          # File mồi theo loại agent
│   ├── coding-agent.md    # Cho Claude Code / Cursor: thứ tự build, milestone, MVP
│   ├── business-agent.md  # Cho agent phân tích nghiệp vụ / tư vấn
│   └── product-agent.md   # Cho agent viết PRD / roadmap
└── schemas/
    └── pack.schema.json   # JSON Schema của manifest — để tool validate pack
```

## 3. Quy ước ID (bắt buộc, toàn hệ sinh thái)

Mọi thực thể có ID duy nhất trong pack, prefix theo loại. Agent tham chiếu bằng ID, không bằng tên.

| Prefix | Loại | Ví dụ |
|---|---|---|
| `BR-` | Business requirement | BR-01 |
| `AD-` | Architecture decision | AD-03 |
| `P-` | Policy | P-08 |
| `SVC-` | Service / capability | SVC-LEAD |
| `PH-` | Journey phase | PH-1 |
| `G-` | Gate / decision point | G-3 |
| `T-` | Trigger | T-9 |
| `R-` | Runtime component | R-2 |
| `O-` | Outcome / integration | O-CUSTOMER360 |
| `SC-` | Incident scenario | SC-02 |
| `E-` | Enforcement point | E-1 |

Quy tắc: ID không bao giờ tái sử dụng sau khi xóa; thay đổi phá vỡ tương thích thì tăng `schema_version` trong manifest.

## 4. Schema từng file (tóm tắt chuẩn)

### manifest.json
```json
{
  "pack": "crm-blueprint",
  "title": "...",
  "version": "1.0.0",
  "schema_version": 1,
  "language": "vi",
  "license": "CC BY-NC 4.0",
  "publisher": { "name": "...", "site": "...", "edition_human": "<url>" },
  "entry_point": "CLAUDE.md",
  "files": [ { "path": "blueprint/journey.yaml", "role": "flow", "sha256": "..." } ],
  "id_index": { "BR": 7, "P": 8, "SVC": 15 }
}
```

### journey.yaml — mỗi phase có `id, name, goal, steps[], gate`
Gate là **decision table**: `question, evaluated_by, on_yes, on_no` — nhánh trỏ tới ID khác (machine-followable).

### requirements.yaml — mỗi requirement: `id, statement, rationale, acceptance_criteria[], applies_to[]` (trỏ ID phase/service).

### services.yaml — mỗi service: `id, name, cluster, responsibility, owns_data[], serves_phases[], depends_on[]` (ID reference), `api_style`.

### policies.yaml — mỗi policy: `id, name, rule, parameters{}` (giá trị cụ thể để agent điền/hỏi), `enforced_at[]` (E-x), `applies_to_phases[]`.

### architecture.yaml — `decisions[] (id, decision, rationale, consequences)`, `runtime[]`, `infrastructure[]`, `outcomes[]`.

### runbook.yaml — `health_flows[]`, `component_ops[] (watch, alert_when, first_response)`, `incidents[] (id, detect, isolate, resolve, never_do)`.

## 5. CLAUDE.md — file mồi vạn năng

Bắt buộc có 5 mục theo thứ tự: (1) Pack này là gì — 3 câu; (2) Thứ tự đọc cho agent; (3) Điều agent PHẢI hỏi người dùng trước khi build (các `parameters` chưa có giá trị); (4) Ranh giới — pack KHÔNG chứa gì (UI design, số liệu thật…); (5) Quy tắc trích dẫn ID khi sinh code/tài liệu phái sinh.

## 6. Tín hiệu website (Human Edition side)

- `llms.txt` ở gốc site liệt kê mọi blueprint + link pack.
- Mỗi trang HTML có bản `.md` song song (`/crm/brd.html` ↔ `/crm/brd.md`).
- Nút **"⬇ Agent Pack"** đặt cạnh nút đọc trên mọi trang blueprint.
- Metadata: `<link rel="alternate" type="text/markdown">` + JSON-LD `TechArticle`.

## 7. Vòng đời & versioning

- SemVer cho pack: patch = sửa chữ, minor = thêm thực thể, major = đổi schema/ID.
- CHANGELOG.md khi có từ minor trở lên.
- Human Edition in số version của pack ở footer — hai ấn bản luôn cùng số.

## 8. Checklist phát hành một blueprint

1. Blueprint YAML viết xong, mọi ID hợp lệ, cross-reference resolve được
2. Validate bằng schema + script kiểm tra tham chiếu chéo
3. Render Human Edition từ nguồn (không viết tay)
4. CLAUDE.md + 3 agent guides
5. Test thực chiến: nạp pack vào một coding agent sạch, yêu cầu scaffold — pass khi agent không phải hỏi lại điều pack đã trả lời
6. manifest.json cập nhật checksum + version
7. Đăng: HTML + nút tải pack + cập nhật llms.txt

---
*Chuẩn này là living document của hệ sinh thái AI Business Architect.*
