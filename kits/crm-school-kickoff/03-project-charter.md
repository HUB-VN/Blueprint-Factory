# 03 · Project Charter & Phạm vi (SOW)

**Giai đoạn:** Trước kickoff · **Chủ trì:** PM · **Ký duyệt:** Sponsor (Hiệu trưởng / đại diện HĐQT) + đại diện đơn vị triển khai
**Nguyên tắc:** charter là **hợp đồng về kỳ vọng**. Mọi thay đổi phạm vi sau khi ký đi qua quy trình Change Request (§9).

---

## 1. Thông tin dự án

| Mục | Nội dung |
|---|---|
| Tên dự án | Triển khai CRM Tuyển sinh & Marketing — [ĐIỀN: tên trường] |
| Mã dự án | [ĐIỀN] |
| Sponsor | [ĐIỀN: họ tên, chức vụ] |
| PM phía triển khai | [ĐIỀN] |
| Đầu mối phía trường (Project Owner) | [ĐIỀN — thường là Trưởng phòng Tuyển sinh] |
| Nền tảng CRM | [ĐIỀN — đã chọn / đang đánh giá; nếu đang đánh giá, xem scorecard build-vs-buy ở `packs/crm-blueprint-pack/agent-guides/business-agent.md`] |
| Ngày kickoff | [ĐIỀN] |
| Ngày go-live mục tiêu | [ĐIỀN — phải nằm ngoài vùng cấm go-live ở doc 02 §1] |
| Ngày kết thúc hypercare | Go-live + [ĐIỀN, khuyến nghị 30] ngày |

## 2. Bối cảnh & vấn đề

*Viết 1 đoạn, dùng số liệu từ tổng hợp discovery (doc 01 §11). Mẫu:*

> Năm học [N], trường tiếp nhận khoảng [ĐIỀN] lead từ [ĐIỀN] kênh, quản lý trên [Excel / Zalo cá nhân / …]. Hiện không đo được speed-to-lead, không biết chi phí trên mỗi học sinh nhập học theo kênh, và [ĐIỀN]% người tham dự sự kiện không được liên hệ lại trong 48 giờ. Dữ liệu phụ huynh nằm trong tài khoản cá nhân của tư vấn viên, tạo rủi ro mất dữ liệu và rủi ro tuân thủ Nghị định 13/2023.

## 3. Mục tiêu (SMART)

| ID | Mục tiêu | Chỉ số | Baseline | Mục tiêu | Thời điểm đo |
|---|---|---|---|---|---|
| OBJ-1 | Không lead nào bị bỏ rơi | % lead có liên hệ đầu tiên trong SLA | [ĐIỀN] | [ĐIỀN, ví dụ ≥ 90%] | Go-live + 60 ngày |
| OBJ-2 | Đo được hiệu quả kênh | % học sinh nhập học có nguồn gốc rõ ràng | [ĐIỀN] | [ĐIỀN] | Hết mùa tuyển sinh |
| OBJ-3 | Sự kiện chuyển hoá thành tuyển sinh | % người tham dự được follow-up ≤ 24h | [ĐIỀN] | [ĐIỀN] | Sự kiện đầu tiên sau go-live |
| OBJ-4 | Dữ liệu thuộc về trường | % hội thoại phụ huynh trên kênh chính thức (Zalo OA, hotline, email trường) | [ĐIỀN] | [ĐIỀN] | Go-live + 90 ngày |
| OBJ-5 | Adoption | % tư vấn viên đăng nhập & cập nhật hằng ngày | — | [ĐIỀN, ví dụ ≥ 95%] | Go-live + 30 ngày |

> Chỉ số "tăng số học sinh nhập học X%" **không** nên là mục tiêu của dự án CRM — nó phụ thuộc học phí, chất lượng, đối thủ. CRM chịu trách nhiệm về **tốc độ, độ phủ, khả năng đo** — những thứ dẫn tới tuyển sinh tốt hơn.

## 4. Phạm vi

### 4.1 Trong phạm vi (In scope) — Giai đoạn 1

| Nhóm | Hạng mục | Tham chiếu |
|---|---|---|
| Dữ liệu | Mô hình Household / Phụ huynh / Học sinh / Trường THCS nguồn / Chương trình / Sự kiện | doc 10 §2 |
| Dữ liệu | Chuyển đổi dữ liệu lead & học sinh tiềm năng [ĐIỀN: số năm] gần nhất | doc 05 |
| Sales | Pipeline `LN-DH` (DH-1..DH-7), gán lead tự động, task & nhắc việc, ghi cuộc gọi/ghi chú, lý do thua | doc 10 §3, doc 11 |
| Sales | Pipeline `LN-NH` (NH-1..NH-4), sĩ số, danh sách chờ | doc 10 §3 |
| Marketing | Thu lead tự động từ [ĐIỀN: Meta Lead Ads, form web, Zalo OA…] | doc 10 §6 |
| Marketing | Quản lý sự kiện `LN-SK`: đăng ký, nhắc lịch, check-in QR, follow-up | doc 12 |
| Marketing | Quy ước nguồn lead + UTM; báo cáo hiệu quả kênh | doc 12 §2 |
| Marketing | [ĐIỀN: số] chuỗi nurture tự động | doc 12 §4 |
| Phê duyệt | Quy trình duyệt học bổng/ưu đãi theo ngưỡng (`P-08`, `BR-04`) | doc 10 §5 |
| Báo cáo | [ĐIỀN: số] dashboard: Ban giám hiệu, Tuyển sinh, Marketing, Sự kiện | doc 14 §4 |
| Tuân thủ | Consent, quyền rút đồng ý, phân quyền dữ liệu học sinh (`BR-07`, `P-05`) | doc 05 §4 |
| Con người | Đào tạo theo vai trò, tài liệu hướng dẫn, hypercare [ĐIỀN] ngày | doc 13, 14 |

### 4.2 Ngoài phạm vi (Out of scope) — ghi rõ để tránh hiểu lầm

- Quản lý học vụ: thời khoá biểu, điểm số, điểm danh hằng ngày (thuộc SIS/LMS)
- Thu học phí định kỳ và công nợ (thuộc phần mềm kế toán) — CRM chỉ nhận **trạng thái** đã nộp giữ chỗ/học phí
- Chăm sóc phụ huynh học sinh đang học về vấn đề học tập (helpdesk) — đề xuất giai đoạn 2
- Website mới / landing page mới (chỉ nhúng form và tracking)
- Sản xuất nội dung marketing (bài viết, video) — chỉ cấu hình chuỗi gửi
- [ĐIỀN: hạng mục khác trường đã hỏi nhưng loại trừ]

### 4.3 Giai đoạn 2 (đề xuất, chưa cam kết)

Tích hợp 2 chiều với SIS; cổng phụ huynh (parent portal); helpdesk phụ huynh hiện hữu (`G-5` đầy đủ); chấm điểm lead bằng AI (`T-9`); chương trình giới thiệu (referral) có thưởng.

## 5. Sản phẩm bàn giao (Deliverables)

| # | Sản phẩm | Tiêu chí chấp nhận | Gate |
|---|---|---|---|
| DL-1 | Tài liệu Thiết kế giải pháp | Ký duyệt bởi Trưởng TS + Trưởng Marketing | `KG-1` |
| DL-2 | Hệ thống CRM cấu hình theo DL-1 | Đạt UAT: 100% kịch bản mức Critical pass, không lỗi Blocker | `KG-2` |
| DL-3 | Dữ liệu đã chuyển đổi | Đối soát số bản ghi; ≤ [ĐIỀN]% trùng lặp còn lại | `KG-2` |
| DL-4 | Tích hợp [ĐIỀN] | Kịch bản tích hợp end-to-end pass | `KG-2` |
| DL-5 | Playbook Sales & Marketing (doc 11, 12 bản hoàn chỉnh) | Ban giám hiệu duyệt | `KG-3` |
| DL-6 | Đào tạo | ≥ [ĐIỀN]% người dùng đạt bài kiểm tra | `KG-3` |
| DL-7 | Báo cáo hypercare & tài liệu vận hành | Admin CRM trường tự làm được các tác vụ ở doc 14 §5 | `KG-4` |

## 6. Mốc chính (Milestones)

| Mốc | Ngày | Ràng buộc |
|---|---|---|
| M0 Kickoff | [ĐIỀN] | Đạt `KG-0` |
| M1 Duyệt thiết kế | Kickoff + [ĐIỀN] tuần | `KG-1` |
| M2 Hoàn tất cấu hình & tích hợp | [ĐIỀN] | |
| M3 UAT đạt | [ĐIỀN] | `KG-2` |
| M4 Go-live | [ĐIỀN] | `KG-3`; **ngoài vùng cấm** doc 02 |
| M5 Thoát hypercare | [ĐIỀN] | `KG-4` |

## 7. Giả định & ràng buộc

**Giả định** (nếu sai → rủi ro, ghi RAID):
- Trường cử Project Owner dành ≥ [ĐIỀN, khuyến nghị 40]% thời gian; key user mỗi bộ phận ≥ [ĐIỀN] giờ/tuần.
- Trường có/sẽ có Zalo OA đã xác thực và [ĐIỀN: SMS brandname] trước M2.
- Dữ liệu cũ được bàn giao đúng hạn ở định dạng đã thống nhất (doc 05).
- Phản hồi tài liệu trong ≤ [ĐIỀN] ngày làm việc; quá hạn coi như chấp thuận *(cần Sponsor đồng ý điều khoản này tại kickoff)*.

**Ràng buộc:** vùng cấm go-live (doc 02 §1); ngân sách [ĐIỀN]; tuân thủ NĐ 13/2023 & Luật Bảo vệ dữ liệu cá nhân (doc 05).

## 8. Tiêu chí thành công & điều kiện kết thúc dự án

Dự án kết thúc khi: `KG-4` đạt; DL-1..DL-7 được chấp nhận; OBJ-5 đạt; OBJ-1..OBJ-4 **có số đo thật** trên dashboard (đạt hay chưa đạt mục tiêu được đánh giá ở review 90 ngày, không chặn nghiệm thu).

## 9. Quản lý thay đổi phạm vi (Change Request)

1. Bất kỳ ai đề xuất → PM ghi vào Change Log (doc 08 §4) kèm ước tính công & ảnh hưởng lịch.
2. Thay đổi ≤ [ĐIỀN] ngày công và không dịch mốc: Project Owner duyệt.
3. Thay đổi lớn hơn hoặc dịch mốc: Steering Committee duyệt.
4. Không có thay đổi nào được làm "miệng" — chưa có CR được duyệt thì chưa làm.

## 10. Ký duyệt

| Vai trò | Họ tên | Chữ ký | Ngày |
|---|---|---|---|
| Sponsor | | | |
| Project Owner (trường) | | | |
| PM (đơn vị triển khai) | | | |
