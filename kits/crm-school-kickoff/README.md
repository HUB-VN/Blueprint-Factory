# KIT-01 · Bộ tài liệu Kickoff triển khai CRM — Trường THPT tư thục

**Phiên bản:** 1.0.0 · 10/2026 · áp dụng blueprint [BP-01 FlowX CRM](../../packs/crm-blueprint-pack/)
**Đối tượng:** đội triển khai CRM (PM, BA, solution consultant, admin CRM) và phía trường (Ban giám hiệu, Phòng Tuyển sinh, Marketing, Kế toán, IT)
**Phạm vi nghiệp vụ:** Sales (tư vấn tuyển sinh) + Marketing cho 3 dòng sản phẩm:

| Mã | Dòng sản phẩm | Ví dụ | Đặc điểm CRM |
|---|---|---|---|
| `LN-DH` | **Khoá dài hạn** | Tuyển sinh lớp 10, chuyển trường lớp 11–12, tái ghi danh học sinh hiện hữu | Chu kỳ 3–9 tháng, giá trị cao, nhiều người quyết định, có học bổng/ưu đãi cần phê duyệt |
| `LN-NH` | **Khoá ngắn hạn** | Trại hè, luyện thi vào 10, IELTS/SAT, STEM, CLB kỹ năng, ôn thi tốt nghiệp | Chu kỳ 1–4 tuần, giá trị thấp–trung bình, số lượng lớn, giới hạn sĩ số |
| `LN-SK` | **Sự kiện** | Open Day, Ngày hội tuyển sinh, hội thảo phụ huynh, thi thử vào 10, "Một ngày làm học sinh" | Không (hoặc ít) doanh thu trực tiếp — là **cỗ máy tạo lead** cho `LN-DH` và `LN-NH` |

> **Luận điểm kiến trúc cốt lõi của kit:** ba dòng sản phẩm **không phải ba CRM**. Một hộ gia đình (phụ huynh + học sinh) là một bản ghi duy nhất; sự kiện và khoá ngắn hạn là "phễu mồi" chảy vào pipeline dài hạn. Đây là áp dụng trực tiếp `BR-01` (một hành trình, mọi kênh) và `BR-03` (Customer 360 không khoảng trống) của BP-01.

---

## 1. Bản đồ tài liệu

```
            TRƯỚC KICKOFF (T-6 → T-0 tuần)                    SAU KICKOFF (T0 → go-live + 90 ngày)
 ┌──────────────────────────────────────────────┐   ┌───────────────────────────────────────────────┐
 │ 01 Bộ câu hỏi Discovery                       │   │ 08 Biên bản kickoff · Decision log · RAID     │
 │ 02 Mùa vụ tuyển sinh & hành trình khách hàng │   │ 09 Kế hoạch triển khai (theo mùa tuyển sinh)  │
 │ 03 Project Charter & phạm vi (SOW)            │   │ 10 Thiết kế giải pháp CRM                     │
 │ 04 Stakeholder · RACI · Governance            │   │ 11 Playbook Sales – Tư vấn tuyển sinh         │
 │ 05 Data readiness & tuân thủ dữ liệu         │   │ 12 Playbook Marketing & Sự kiện               │
 │ 06 Checklist sẵn sàng kickoff (Gate KG-0)     │   │ 13 UAT & Đào tạo                              │
 │ 07 Agenda & kịch bản buổi Kickoff             │   │ 14 Go-live · Hypercare · KPI                  │
 └──────────────────────────────────────────────┘   └───────────────────────────────────────────────┘
                         ▲                                              │
                         └──────────── 07 = điểm nối hai nửa ───────────┘
```

| # | Tài liệu | Giai đoạn | Chủ trì | Người duyệt | Đầu ra |
|---|---|---|---|---|---|
| 01 | [Bộ câu hỏi Discovery](01-discovery-questionnaire.md) | Trước | BA | PM | Ghi chép phỏng vấn, danh sách pain point |
| 02 | [Mùa vụ & hành trình](02-mua-vu-va-hanh-trinh.md) | Trước | BA + Trưởng TS | Ban giám hiệu | Lịch mùa vụ, hành trình 3 dòng sản phẩm |
| 03 | [Project Charter & SOW](03-project-charter.md) | Trước | PM | Sponsor (Hiệu trưởng/HĐQT) | Charter ký duyệt |
| 04 | [Stakeholder · RACI · Governance](04-raci-governance.md) | Trước | PM | Sponsor | Ma trận RACI, lịch họp |
| 05 | [Data readiness & tuân thủ](05-data-readiness.md) | Trước | Data lead + Pháp chế | IT trường | Kiểm kê dữ liệu, kế hoạch consent |
| 06 | [Checklist sẵn sàng kickoff](06-pre-kickoff-checklist.md) | Trước | PM | Sponsor | Quyết định Go/No-go `KG-0` |
| 07 | [Agenda & kịch bản Kickoff](07-kickoff-agenda.md) | Nối | PM | — | Buổi kickoff, các quyết định D-01..D-08 |
| 08 | [Biên bản · Decision log · RAID](08-bien-ban-raid.md) | Sau | PM | Sponsor | Biên bản trong 24h, RAID log sống |
| 09 | [Kế hoạch triển khai](09-ke-hoach-trien-khai.md) | Sau | PM | Steering Committee | Kế hoạch sprint + gate KG-1..KG-4 |
| 10 | [Thiết kế giải pháp CRM](10-thiet-ke-giai-phap.md) | Sau | Solution consultant | Trưởng TS + Marketing | Solution Design ký duyệt (`KG-1`) |
| 11 | [Playbook Sales – Tư vấn tuyển sinh](11-playbook-sales.md) | Sau | Trưởng TS | Ban giám hiệu | SOP tư vấn, script, SLA |
| 12 | [Playbook Marketing & Sự kiện](12-playbook-marketing-su-kien.md) | Sau | Trưởng Marketing | Ban giám hiệu | Quy ước nguồn/UTM, quy trình sự kiện |
| 13 | [UAT & Đào tạo](13-uat-dao-tao.md) | Sau | QA/BA + Trainer | Key users | Biên bản UAT (`KG-2`), học viên đạt |
| 14 | [Go-live · Hypercare · KPI](14-golive-hypercare-kpi.md) | Sau | PM + Admin CRM | Sponsor | Cutover (`KG-3`), bàn giao (`KG-4`) |

---

## 2. Các cổng quyết định của dự án (Project Gates)

Theo tinh thần FlowX: gate là **decision table**, không phải cảm tính.

| Gate | Câu hỏi | Ai quyết | Đạt → | Không đạt → |
|---|---|---|---|---|
| `KG-0` | Sẵn sàng kickoff? (doc 06) | Sponsor + PM | Tổ chức kickoff | Dời kickoff, xử lý mục đỏ |
| `KG-1` | Thiết kế giải pháp được duyệt? (doc 10) | Trưởng TS + Marketing + PM | Bắt đầu build/cấu hình | Vòng thiết kế bổ sung (tối đa 2 vòng, sau đó escalate SteerCo) |
| `KG-2` | UAT đạt? (doc 13) | Key users + PM | Chuẩn bị cutover | Sửa lỗi, UAT vòng 2 |
| `KG-3` | Go-live? (doc 14) | Sponsor | Cutover | Lùi ngày, **nhưng không lùi qua mốc mùa vụ đã chốt ở doc 02** — nếu chạm mốc, go-live phạm vi rút gọn (MVP) |
| `KG-4` | Thoát hypercare? (doc 14) | Sponsor + Admin CRM trường | Bàn giao vận hành | Gia hạn hypercare 2 tuần |

## 3. Quy ước dùng kit

- **Tham số để trống có chủ ý.** Mọi chỗ ghi `[ĐIỀN: …]` là thông tin phụ thuộc trường cụ thể (học phí, ngưỡng học bổng, SLA, chỉ tiêu…). Không điền số "mẫu" vào tài liệu phát hành cho khách — hỏi và ghi nguồn.
- **Trích dẫn ID.** Khi viết tài liệu phái sinh (BRD, cấu hình, test case), trích ID của kit (`LN-DH`, `KG-1`, `D-03`, `RK-02`…) và của BP-01 (`PH-1`, `G-1`, `SVC-LEAD`, `P-08`, `BR-07`…) để truy vết.
- **Trung lập nền tảng.** Kit dùng thuật ngữ chung (Lead, Contact, Account/Household, Opportunity, Campaign). Bảng ánh xạ sang HubSpot / Salesforce Education Cloud / Zoho / Bitrix24 / CRM nội địa ở doc 10 §1.
- **Song ngữ thuật ngữ.** Tiếng Việt là chính; thuật ngữ CRM giữ tiếng Anh khi đó là từ đội triển khai và phần mềm thực sự dùng.

## 4. Thuật ngữ nhanh

| Thuật ngữ | Nghĩa trong kit |
|---|---|
| Hộ gia đình (Household) | Đơn vị khách hàng = Account trong BP-01 (`SVC-ACCOUNT`). Gồm phụ huynh, học sinh, anh/chị/em |
| Phụ huynh (Parent) | Người ra quyết định + người trả tiền. Contact chính |
| Học sinh (Student) | Người dùng + người ảnh hưởng. Contact phụ — **dữ liệu trẻ em**, xem doc 05 |
| Hồ sơ tuyển sinh | Opportunity (`SVC-OPP`) — một học sinh × một chương trình × một năm học |
| Đợt tuyển sinh | Campaign (`SVC-CAMPAIGN`) cấp cha, chứa các chiến dịch kênh và sự kiện con |
| Giữ chỗ / Đặt cọc | Mốc "Won" của `LN-DH` (gate `G-3`) |
| Trường THCS nguồn (Feeder) | Trường cấp 2 mà học sinh đang học — chiều phân tích quan trọng nhất cho marketing |
| Speed-to-lead | Thời gian từ khi lead vào CRM đến lần liên hệ thực sự đầu tiên |

## 5. Cách dùng kit với AI agent

> "Đọc `kits/crm-school-kickoff/README.md`, sau đó dùng doc 01 để soạn lịch phỏng vấn discovery cho trường [tên]. Mọi `[ĐIỀN]` hãy hỏi tôi, không tự giả định."

Kit kế thừa ranh giới của BP-01 (`packs/crm-blueprint-pack/CLAUDE.md` §3–§4): agent phải hỏi các tham số `P-05`, `P-07`, `P-08` trước khi cấu hình.
