# KIT-01 · Bộ tài liệu Kickoff triển khai CRM — Trường tư thục THCS & THPT

**Phiên bản:** 1.2.0 · 10/2026 · áp dụng blueprint [BP-01 FlowX CRM](../../packs/crm-blueprint-pack/)
**Đối tượng:** đội triển khai CRM (PM, BA, solution consultant, admin CRM) và phía trường (Ban giám hiệu, Phòng Tuyển sinh, Marketing, Kế toán, IT)
**Loại trường:** trường tư thục THCS (lớp 6–9), THPT (lớp 10–12), hoặc liên cấp có cả hai
**Phạm vi nghiệp vụ:** Sales (tư vấn tuyển sinh) + Marketing cho 3 dòng sản phẩm, **cả 3 đều là sản phẩm có pipeline và có thể có doanh thu**:

| Mã | Dòng sản phẩm | Ví dụ | Đặc điểm CRM |
|---|---|---|---|
| `LN-DH` | **Chương trình dài hạn (tuyển sinh mọi khối lớp)** | Tuyển sinh đầu cấp (lớp 6, lớp 10); chuyển trường vào **bất kỳ khối nào từ lớp 6 đến lớp 12**, kể cả giữa năm học; lên cấp nội bộ (lớp 9 → 10 ở trường liên cấp); tái ghi danh học sinh đang học | Chu kỳ từ vài ngày (chuyển trường gấp) đến 9–12 tháng (đầu cấp); giá trị cao; nhiều người quyết định; có học bổng/ưu đãi cần phê duyệt |
| `LN-NH` | **Khoá ngắn hạn** | Trại hè, luyện thi chuyển cấp, ngoại ngữ, STEM, CLB kỹ năng, ôn thi tốt nghiệp | Nhiều buổi trong vài tuần đến vài tháng; giá trị thấp đến trung bình; số lượng lớn; giới hạn sĩ số |
| `LN-SK` | **Sự kiện & chương trình đào tạo** | Có phí: workshop, chương trình trải nghiệm, trại 1–3 ngày, hội thảo chuyên đề, cuộc thi, thi thử có phí. Miễn phí: Open Day, ngày hội tuyển sinh, hội thảo phụ huynh, "Một ngày làm học sinh" | **Là một sản phẩm**: có sức chứa, loại vé (có thể 0đ), đăng ký, thanh toán, điểm danh, hoàn thành. Đồng thời là **nguồn tạo lead** cho `LN-DH` và `LN-NH` |

> **Luận điểm kiến trúc cốt lõi của kit:** ba dòng sản phẩm **không phải ba CRM**. Một hộ gia đình (phụ huynh + một hoặc nhiều học sinh ở các khối khác nhau) là một bản ghi duy nhất. Mỗi lần mua (một hồ sơ tuyển sinh, một khoá, một vé sự kiện) là một giao dịch riêng gắn vào hộ đó. Sự kiện và khoá ngắn hạn vừa tạo doanh thu, vừa đưa lead vào pipeline dài hạn. Đây là áp dụng trực tiếp `BR-01` (một hành trình, mọi kênh) và `BR-03` (Customer 360 không khoảng trống) của BP-01.

> **Nguyên tắc "khám phá trước, cấu hình sau" cho Marketing.** Mỗi trường có bộ kênh, nguồn lead và kiểu chiến dịch rất khác nhau, và chúng thay đổi liên tục. Vì vậy kit **không đặt sẵn** danh mục kênh, nguồn hay chiến dịch. Kit chỉ cố định **cấu trúc** (cách phân cấp nguồn, cách phân cấp chiến dịch, các trường bắt buộc). **Giá trị** cụ thể được thu thập qua khảo sát (doc 01 §5–§6) và workshop marketing (doc 12 §1), rồi chốt tại `KG-1`. Mọi danh sách kênh xuất hiện trong kit chỉ là **gợi ý để hỏi**, không phải cấu hình mặc định.

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
 ┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
 │ 15 Fit-Gap & Nâng cấp sản phẩm CRM — chạy xuyên suốt: fit-gap sơ bộ → CRP → Gap register →        │
 │    phát triển song song → KG-D Dev-complete → phát hành → cải tiến sau go-live                    │
 └──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| # | Tài liệu | Giai đoạn | Chủ trì | Người duyệt | Đầu ra |
|---|---|---|---|---|---|
| 01 | [Bộ câu hỏi Discovery](01-discovery-questionnaire.md) | Trước | BA | PM | Ghi chép phỏng vấn, danh sách pain point |
| 02 | [Mùa vụ & hành trình](02-mua-vu-va-hanh-trinh.md) | Trước | BA + Trưởng TS | Ban giám hiệu | Lịch mùa vụ theo cấp/khối, hành trình 3 dòng sản phẩm |
| 03 | [Project Charter & SOW](03-project-charter.md) | Trước | PM | Sponsor (Hiệu trưởng/HĐQT) | Charter ký duyệt |
| 04 | [Stakeholder · RACI · Governance](04-raci-governance.md) | Trước | PM | Sponsor | Ma trận RACI, lịch họp |
| 05 | [Data readiness & tuân thủ](05-data-readiness.md) | Trước | Data lead + Pháp chế | IT trường | Kiểm kê dữ liệu, kế hoạch consent |
| 06 | [Checklist sẵn sàng kickoff](06-pre-kickoff-checklist.md) | Trước | PM | Sponsor | Quyết định Go/No-go `KG-0` |
| 07 | [Agenda & kịch bản Kickoff](07-kickoff-agenda.md) | Nối | PM | — | Buổi kickoff, các quyết định D-01..D-10 |
| 08 | [Biên bản · Decision log · RAID](08-bien-ban-raid.md) | Sau | PM | Sponsor | Biên bản trong 24h, RAID log sống |
| 09 | [Kế hoạch triển khai](09-ke-hoach-trien-khai.md) | Sau | PM | Steering Committee | Kế hoạch sprint + gate KG-1..KG-4 |
| 10 | [Thiết kế giải pháp CRM](10-thiet-ke-giai-phap.md) | Sau | Solution consultant | Trưởng TS + Marketing | Solution Design ký duyệt (`KG-1`) |
| 11 | [Playbook Sales – Tư vấn tuyển sinh](11-playbook-sales.md) | Sau | Trưởng TS | Ban giám hiệu | SOP tư vấn, script, SLA |
| 12 | [Playbook Marketing & Sự kiện](12-playbook-marketing-su-kien.md) | Sau | Trưởng Marketing | Ban giám hiệu | Workshop khám phá kênh/nguồn, taxonomy nguồn & chiến dịch của trường, vận hành sự kiện như sản phẩm |
| 13 | [UAT & Đào tạo](13-uat-dao-tao.md) | Sau | QA/BA + Trainer | Key users | Biên bản UAT (`KG-2`), học viên đạt |
| 14 | [Go-live · Hypercare · KPI](14-golive-hypercare-kpi.md) | Sau | PM + Admin CRM | Sponsor | Cutover (`KG-3`), bàn giao (`KG-4`) |
| 15 | [Fit-Gap & Nâng cấp sản phẩm](15-fit-gap-nang-cap-san-pham.md) | Xuyên suốt | BA + Product Manager CRM | Product Council / SteerCo | Gap register, đặc tả tính năng, gate `KG-D`, backlog cải tiến |

---

## 2. Các cổng quyết định của dự án (Project Gates)

Theo tinh thần FlowX: gate là **decision table**, không phải cảm tính.

| Gate | Câu hỏi | Ai quyết | Đạt → | Không đạt → |
|---|---|---|---|---|
| `KG-0` | Sẵn sàng kickoff? (doc 06) | Sponsor + PM | Tổ chức kickoff | Dời kickoff, xử lý mục đỏ |
| `KG-1` | Thiết kế giải pháp **và Gap register** được duyệt? (doc 10, doc 15) | Trưởng TS + Marketing + PM | Bắt đầu build/cấu hình | Vòng thiết kế bổ sung (tối đa 2 vòng, sau đó escalate SteerCo) |
| `KG-D` | Dev-complete? Mọi gap "bắt buộc go-live" đã xong trên staging (doc 15 §9) | Product Manager + PM | Vào UAT với tính năng mới | UAT bằng workaround, tính năng phát hành sau ngoài vùng cấm; hoặc SteerCo rút phạm vi |
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
| Hồ sơ tuyển sinh | Opportunity (`SVC-OPP`) — một học sinh × một khối lớp × một năm học |
| Loại tuyển sinh | Đầu cấp / Chuyển trường / Lên cấp nội bộ / Tái ghi danh — cùng pipeline `LN-DH`, khác bước bắt buộc (doc 02 §4.1) |
| Khối nhập học | Lớp 6–12 mà học sinh sẽ vào học |
| Đăng ký sự kiện | Opportunity của pipeline `LN-SK` — một người tham dự × một sự kiện; vé 0đ vẫn là một đăng ký |
| Đợt tuyển sinh | Campaign (`SVC-CAMPAIGN`) cấp cha, chứa các chiến dịch kênh và sự kiện con |
| Giữ chỗ / Đặt cọc | Mốc "Won" của `LN-DH` (gate `G-3`) |
| Trường nguồn (Feeder) | Trường học sinh đang học trước khi vào: tiểu học (cho lớp 6), THCS (cho lớp 10), hoặc trường cùng cấp (chuyển trường) |
| Speed-to-lead | Thời gian từ khi lead vào CRM đến lần liên hệ thực sự đầu tiên |

## 5. Cách dùng kit với AI agent

> "Đọc `kits/crm-school-kickoff/README.md`, sau đó dùng doc 01 để soạn lịch phỏng vấn discovery cho trường [tên]. Mọi `[ĐIỀN]` hãy hỏi tôi, không tự giả định."

Kit kế thừa ranh giới của BP-01 (`packs/crm-blueprint-pack/CLAUDE.md` §3–§4): agent phải hỏi các tham số `P-05`, `P-07`, `P-08` trước khi cấu hình.
