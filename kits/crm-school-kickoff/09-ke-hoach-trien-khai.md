# 09 · Kế hoạch triển khai (theo mùa tuyển sinh)

**Giai đoạn:** Sau kickoff · **Chủ trì:** PM · **Duyệt:** Steering Committee
**Nguyên tắc lập lịch:** đếm **ngược từ mốc mùa vụ**, không đếm xuôi từ kickoff. Ngày go-live do doc 02 §2 quyết định; phạm vi co giãn để vừa ngày đó.

---

## 1. Khung giai đoạn & sprint (mẫu 12 tuần, sprint 2 tuần)

| Sprint | Tuần | Trọng tâm | Đầu ra chính | Gate |
|---|---|---|---|---|
| Sprint 0 — Thiết kế & khám phá | 1–2 | **Workshop khám phá Marketing** (doc 12 §1, K3–K5); workshop thiết kế: mô hình dữ liệu, pipeline theo loại tuyển sinh, sức chứa, quy tắc, tích hợp, báo cáo | Taxonomy D-09 + Solution Design (doc 10) ký duyệt | `KG-1` |
| Sprint 1 — Nền tảng | 3–4 | Đối tượng Household/Contact/Opportunity/Product/Campaign; phân quyền; pipeline `LN-DH`; bảng Sức chứa theo khối/lớp; nạp danh mục (trường nguồn, chương trình, khối) | Sandbox chạy được `PH-1`→`PH-3` cơ bản; demo cuối sprint | |
| Sprint 2 — Thu lead & Marketing | 5–6 | Tích hợp các điểm vào giai đoạn 1 theo D-09 (mẫu A–D, doc 10 §6.2); taxonomy nguồn, cấu trúc Campaign, UTM; gán lead; SLA & cảnh báo | Lead từ mọi kênh vào đúng người trong ≤ [ĐIỀN] phút | |
| Sprint 3 — Sự kiện & khoá ngắn hạn | 7–8 | Pipeline `LN-NH`, sĩ số, danh sách chờ; pipeline `LN-SK` như sản phẩm: sức chứa, loại vé, thanh toán, nhắc, check-in QR, hoàn thành, follow-up; chuỗi nurture theo thẻ thiết kế | Diễn tập 1 sự kiện giả lập end-to-end | |
| Sprint 4 — Phê duyệt, báo cáo, dữ liệu | 9–10 | Duyệt học bổng (`P-08`); dashboard; chuyển đổi dữ liệu thử; tích hợp kế toán/SIS (giai đoạn 1: file) | Dữ liệu thử đã đối soát; dashboard có số | |
| UAT & Đào tạo | 11 | UAT 2 vòng (doc 13); đào tạo theo vai trò | Biên bản UAT | `KG-2` |
| Cutover & Go-live | 12 | Nạp dữ liệu chính thức, bật tích hợp, tắt nguồn cũ (doc 14) | Hệ thống chạy thật | `KG-3` |
| Hypercare | 13–16 | Hỗ trợ tại chỗ, sửa lỗi, tinh chỉnh | Báo cáo hypercare | `KG-4` |

> **Kickoff muộn (rơi vào T3–T7)?** Đảo thứ tự: Sprint 2 + phần sự kiện của Sprint 3 lên trước → go-live **MVP "không bỏ lỡ lead nào"** (thu lead + gán + nhắc việc + sự kiện) trước đỉnh mùa; pipeline đầy đủ, phê duyệt, dashboard nâng cao triển khai sau mùa. Ghi quyết định này vào Decision log.

## 2. Phân rã công việc (WBS) — rút gọn

| Mã | Gói công việc | Sprint | Người làm chính | Phụ thuộc |
|---|---|---|---|---|
| W1 | Thiết kế mô hình dữ liệu & phân quyền | 0 | Consultant | D-03, D-05 |
| W2 | Thiết kế quy tắc tự động hoá & SLA | 0 | Consultant | D-02, D-08 |
| W3 | Cấu hình đối tượng, trường, layout | 1 | Admin/Dev | W1 |
| W4 | Pipeline `LN-DH` + lý do thua | 1 | Admin/Dev | W1 |
| W0 | Workshop khám phá kênh/nguồn/chiến dịch + truy dấu lead thật | 0 | BA + Marketing | DP-02 |
| W5 | Tích hợp điểm vào lead giai đoạn 1 (danh sách từ D-09) | 2 | Integration eng. | D-09, DP-01, DP-03 |
| W6 | Quy tắc gán lead, task, cảnh báo SLA | 2 | Admin/Dev | W2 |
| W7 | Cấu hình taxonomy nguồn + Campaign 3 cấp + UTM + báo cáo kênh | 2 | Consultant + Marketing | D-09 |
| W8 | Pipeline `LN-NH` + sĩ số + danh sách chờ | 3 | Admin/Dev | W3 |
| W9 | Pipeline `LN-SK` + sức chứa + vé & thanh toán + check-in QR + nhắc lịch | 3 | Admin/Dev | DP-01, IN-10 |
| W10 | Chuỗi nurture (số lượng theo phạm vi) | 3 | Marketing + Admin | Nội dung từ Marketing |
| W11 | Quy trình phê duyệt học bổng/ưu đãi | 4 | Admin/Dev | D-06 |
| W11b | Bảng Sức chứa theo khối/lớp + đồng bộ từ SIS + danh sách chờ | 1–4 | Admin/Dev | IN-08 |
| W12 | Dashboard & báo cáo | 4 | Consultant | W4–W9 |
| W13 | Chuyển đổi dữ liệu thử + đối soát | 4 | Data lead | doc 05 |
| W14 | Tích hợp kế toán / SIS (file hoặc API) | 4 | Integration eng. | DP-05 |
| W15 | Tài liệu đào tạo & video ngắn | 3–4 | Trainer | Cấu hình ổn định |
| W16 | UAT | 5 (tuần 11) | BA + key users | W3–W14 |
| W17 | Cutover & go-live | 6 (tuần 12) | PM + Admin | `KG-2` |
| W18 | Hypercare & bàn giao | 13–16 | Admin + PM | `KG-3` |

## 3. Định nghĩa "Hoàn thành" (Definition of Done) cho mỗi hạng mục cấu hình

- [ ] Có trong Solution Design (doc 10) hoặc CR đã duyệt
- [ ] Đã cấu hình trên sandbox, có ghi chú trích ID (ví dụ "Rule gán lead — D-05, `CC-A`")
- [ ] Key user đã xem demo và đồng ý
- [ ] Có ít nhất 1 kịch bản UAT tương ứng (doc 13)
- [ ] Tài liệu hướng dẫn người dùng đã cập nhật (nếu ảnh hưởng thao tác)

## 4. Kế hoạch nguồn lực (điền)

| Vai trò | Người | % thời gian theo sprint (0 / 1 / 2 / 3 / 4 / UAT / Go-live / Hypercare) |
|---|---|---|
| PM | | |
| BA / Consultant | | |
| Admin / Developer CRM | | |
| Integration engineer | | |
| Trainer | | |
| Project Owner (trường) | | ≥ 40% suốt dự án; 80% ở UAT & go-live |
| Key users (trường) | | 4h/tuần build · 2 ngày UAT · có mặt cả tuần go-live |
| Admin CRM (trường) | | 20% build · 50% từ UAT · 100% hypercare |

## 5. Nhịp kiểm soát tiến độ

- **Burn-up theo hạng mục W1–W18**, không theo giờ công.
- **Đèn tín hiệu tuần** (doc 04 §4): Đỏ khi bất kỳ (a) mốc gate trễ > 1 tuần, (b) RAID mức Cao chưa có biện pháp, (c) phụ thuộc DP-xx trễ ảnh hưởng sprint kế tiếp.
- **Quy tắc bảo vệ ngày go-live:** khi trễ, thứ tự hy sinh là: (1) dashboard nâng cao → (2) chuỗi nurture thứ cấp → (3) `LN-NH` → (4) phê duyệt học bổng tự động (dùng phê duyệt thủ công tạm). **Không bao giờ** hy sinh: thu lead mọi kênh, gán lead, nhắc việc, consent.
