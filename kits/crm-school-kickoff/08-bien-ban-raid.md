# 08 · Biên bản Kickoff · Decision Log · RAID Log · Change Log

**Giai đoạn:** Sau kickoff, dùng xuyên suốt dự án · **Chủ trì:** PM
**Quy ước:** quyết định chỉ có hiệu lực khi được ghi vào Decision log. RAID log là tài liệu **sống** — cập nhật mỗi họp tuần, rà mục Cao ở mỗi SteerCo.

---

## 1. Mẫu biên bản Kickoff (gửi ≤ 24h)

```
BIÊN BẢN KICKOFF — Dự án CRM Tuyển sinh & Marketing — [Tên trường]
Ngày: [ĐIỀN]   Địa điểm: [ĐIỀN]   Người ghi: [ĐIỀN]
Thành phần: [danh sách]   Vắng: [danh sách]

1. Thông điệp của Sponsor (tóm tắt 2–3 câu)
2. Phạm vi đã xác nhận: In scope … / Out of scope … / Giai đoạn 2 …
3. Lịch: Go-live mục tiêu … · Vùng cấm go-live từ … đến …
4. Quyết định đã chốt: D-0x … (chi tiết ở Decision log)
5. Quyết định còn mở: D-0x — người chịu trách nhiệm … — hạn …
6. Rủi ro mới ghi nhận: RK-xx …
7. Việc 2 tuần tới: (Việc · Người · Hạn)
8. Lịch họp tiếp theo: SteerCo … · Họp tuần …

Đề nghị các thành viên phản hồi trong [ĐIỀN] ngày làm việc; quá hạn biên bản được coi là thống nhất.
```

## 2. Decision log

| ID | Ngày | Quyết định | Phương án đã cân nhắc | Lý do chọn | Người quyết | Ảnh hưởng (doc/cấu hình) | Ngày xem lại |
|---|---|---|---|---|---|---|---|
| D-01 | | Go-live mục tiêu …; vùng cấm … | | | Sponsor | doc 03 §6, doc 09 | — |
| D-02 | | Lead đủ điều kiện = … | | | | doc 10 §4 (rule `G-1`) | Go-live + 30 ngày |
| D-03 | | Stage `LN-DH` = … | | | | doc 10 §3 | |
| D-04 | | Phạm vi giai đoạn 1 … | | | | doc 03 §4 | |
| D-05 | | Quy tắc gán lead … | | | | doc 10 §4 | |
| D-06 | | Ngưỡng phê duyệt học bổng … | | | | doc 10 §5 (`P-08`) | |
| D-07 | | Kênh liên lạc chính thức … | | | | doc 11 §5 | |
| D-08 | | SLA … | | | | doc 10 §4, doc 11 §2 | |
| D-09+ | | *(quyết định phát sinh trong dự án)* | | | | | |

**Quy tắc:** quyết định thay đổi → **không sửa dòng cũ**; thêm dòng mới "D-xx thay thế D-yy" (giống quy tắc ID không tái sử dụng của BP-01).

## 3. RAID log

### 3.1 Rủi ro (Risks) — điền sẵn các rủi ro điển hình của ngành, xoá dòng không áp dụng

Thang: Khả năng (K) và Tác động (T) 1–3; Mức = K × T (≥ 6 = Cao).

| ID | Rủi ro | K | T | Mức | Giảm thiểu | Người theo dõi | Trạng thái |
|---|---|---|---|---|---|---|---|
| RK-01 | Go-live trượt vào mùa cao điểm tuyển sinh → tư vấn viên không có thời gian học, quay về Excel | 2 | 3 | 6 | Vùng cấm cứng (D-01); phương án MVP; quyết định trượt tại `KG-3` theo luật ở README §2 | PM | |
| RK-02 | Tư vấn viên không nhập liệu vì lo mất "khách của mình" / bị giám sát | 3 | 3 | 9 | Chính sách ghi nhận công công bố trước go-live (doc 11 §6); key user là tư vấn viên; dashboard cá nhân cho TVV | Project Owner | |
| RK-03 | Không có admin CRM phía trường → phụ thuộc đơn vị triển khai sau hypercare | 2 | 3 | 6 | Chỉ định trước `KG-0`; admin tham gia cấu hình từ Sprint 1; checklist năng lực ở doc 14 §5 | Sponsor | |
| RK-04 | Dữ liệu cũ chất lượng thấp, trùng lặp nhiều | 3 | 2 | 6 | Ngưỡng chất lượng (doc 05 §3.3); không chuyển dữ liệu quá [ĐIỀN] năm | Data lead | |
| RK-05 | Marketing & Tuyển sinh không thống nhất định nghĩa lead | 2 | 2 | 4 | D-02 + xem lại sau 30 ngày bằng dữ liệu | PM | |
| RK-06 | Không tuân thủ quy định dữ liệu trẻ em / consent | 2 | 3 | 6 | doc 05 §4; pháp chế duyệt trước `KG-2` | Đầu mối pháp chế | |
| RK-07 | Zalo OA chưa xác thực / mẫu ZNS chưa được duyệt kịp | 2 | 2 | 4 | Nộp hồ sơ OA & mẫu ZNS ngay Sprint 1; phương án dự phòng SMS/email | Marketing | |
| RK-08 | Tích hợp với SIS / kế toán không có API | 2 | 2 | 4 | Phương án nhập/xuất file định kỳ ở giai đoạn 1 | IT trường | |
| RK-09 | Key user không có thời gian (đang mùa sự kiện) | 2 | 2 | 4 | Lịch key user cố định trong tuần, Project Owner bảo vệ thời gian | Project Owner | |
| RK-10 | Yêu cầu phình to (scope creep) từ nhiều bộ phận | 3 | 2 | 6 | Quy trình CR (doc 03 §9); danh sách giai đoạn 2 công khai | PM | |
| RK-11 | Nhân sự tư vấn biến động (thời vụ, cộng tác viên mùa cao điểm) | 2 | 2 | 4 | Tài liệu đào tạo tự học + license cho nhân sự thời vụ (D-xx) | Project Owner | |

### 3.2 Giả định (Assumptions)
| ID | Giả định | Nếu sai thì | Người xác nhận | Hạn xác nhận |
|---|---|---|---|---|
| AS-01 | Trường bàn giao dữ liệu nguồn đúng hạn | Trượt lịch chuyển đổi | Project Owner | |
| AS-02 | Nền tảng CRM hỗ trợ quan hệ Household–nhiều Contact | Cần tuỳ biến / workaround | Consultant | |
| AS-03 | … | | | |

### 3.3 Vấn đề (Issues) — rủi ro đã xảy ra
| ID | Vấn đề | Ngày phát hiện | Tác động | Hành động | Người xử lý | Hạn | Trạng thái |
|---|---|---|---|---|---|---|---|
| IS-01 | | | | | | | |

### 3.4 Phụ thuộc (Dependencies)
| ID | Phụ thuộc | Bên cung cấp | Cần trước | Trạng thái |
|---|---|---|---|---|
| DP-01 | Zalo OA đã xác thực + mẫu ZNS được duyệt | Marketing / Zalo | Sprint 3 | |
| DP-02 | SMS brandname đăng ký | Marketing / nhà mạng | Sprint 3 | |
| DP-03 | Quyền truy cập Meta Business Manager | Marketing / agency | Sprint 2 | |
| DP-04 | SPF/DKIM/DMARC cho tên miền gửi email | IT trường | Sprint 2 | |
| DP-05 | API / file xuất từ SIS và phần mềm kế toán | IT trường / nhà cung cấp | Sprint 2 | |
| DP-06 | Văn bản privacy notice + mẫu consent được duyệt | Pháp chế | Trước UAT | |

## 4. Change log (Change Request)

| CR | Ngày | Người đề xuất | Mô tả | Lý do | Ước tính (ngày công) | Ảnh hưởng mốc | Cấp duyệt | Quyết định | Ngày quyết |
|---|---|---|---|---|---|---|---|---|---|
| CR-01 | | | | | | Có/Không | PO / SteerCo | Duyệt / Từ chối / Giai đoạn 2 | |
