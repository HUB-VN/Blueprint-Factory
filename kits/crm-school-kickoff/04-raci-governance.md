# 04 · Stakeholder · RACI · Governance

**Giai đoạn:** Trước kickoff · **Chủ trì:** PM · **Duyệt:** Sponsor

---

## 1. Bản đồ stakeholder

| Stakeholder | Quan tâm chính | Ảnh hưởng | Mức ủng hộ hiện tại | Chiến lược |
|---|---|---|---|---|
| Hiệu trưởng / HĐQT | Chỉ tiêu, chi phí tuyển sinh, uy tín | Cao | [ĐIỀN] | Báo cáo 2 tuần/lần bằng số, không bằng tiến độ task |
| Trưởng phòng Tuyển sinh | Đạt chỉ tiêu, quản lý đội | Cao | [ĐIỀN] | Đồng thiết kế; là Project Owner |
| Tư vấn viên tuyển sinh | Ít việc tay chân hơn, không bị "giám sát" | Trung bình (quyết định adoption) | [ĐIỀN] | Chọn 1–2 người làm key user / "đại sứ"; cho thấy lợi ích cá nhân sớm |
| Trưởng Marketing | Chứng minh ROI kênh | Cao | [ĐIỀN] | Đồng sở hữu định nghĩa lead (D-02) |
| Phụ trách khoá ngắn hạn | Lấp đầy lớp | Trung bình | [ĐIỀN] | Quick win: đăng ký & danh sách chờ |
| Kế toán | Không thêm việc nhập liệu | Trung bình | [ĐIỀN] | Chỉ yêu cầu **một** thao tác xác nhận thanh toán, hoặc tích hợp |
| IT trường | Bảo mật, không thêm gánh nặng vận hành | Trung bình | [ĐIỀN] | Tham gia sớm về SSO, tích hợp, admin |
| Giáo viên (khoá ngắn hạn, chấm đầu vào) | Không phải dùng thêm phần mềm | Thấp | — | Giao diện tối giản / nhập qua form |
| Phụ huynh & học sinh | Được tư vấn đúng lúc, không bị làm phiền | Gián tiếp | — | Đại diện qua tiêu chí UX trong doc 11 |

**Rủi ro con người điển hình (đưa vào RAID nếu đúng với trường):**
- Tư vấn viên giữ dữ liệu trên Zalo cá nhân vì sợ mất "khách của mình" → cần chính sách ghi nhận công rõ ràng (doc 11 §6) **trước** khi bắt buộc dùng CRM.
- Marketing và Tuyển sinh đổ lỗi chất lượng lead cho nhau → D-02 phải chốt tại kickoff.

## 2. Cơ cấu tổ chức dự án

```
                       Steering Committee (SteerCo)
           Sponsor · Project Owner · PM · (Giám đốc đơn vị triển khai)
                                   │
                ┌──────────────────┴──────────────────┐
         Phía trường                           Phía triển khai
   Project Owner (Trưởng TS)                       PM
   Key user Tuyển sinh (1–2)              BA / Solution consultant
   Key user Marketing (1)                 Admin/Developer CRM
   Key user Khoá ngắn hạn (1)             Integration engineer (khi cần)
                                          Product Manager CRM + Tech lead sản phẩm
                                          (Product Council, doc 15 §7)
   Đầu mối Kế toán · Đầu mối IT           Trainer
   Admin CRM tương lai (bắt buộc)
```

## 3. Ma trận RACI

R = Thực hiện · A = Chịu trách nhiệm cuối (chỉ 1) · C = Tham vấn · I = Được thông báo

| Hoạt động | Sponsor | Project Owner | PM | BA/Consultant | Admin/Dev | Key users | Kế toán | IT trường |
|---|---|---|---|---|---|---|---|---|
| Discovery (doc 01) | C | C | A | R | I | C | C | C |
| Lịch mùa vụ & hành trình (doc 02) | C | A | C | R | I | C | I | I |
| Project charter (doc 03) | A | C | R | C | I | I | I | I |
| Kiểm kê & làm sạch dữ liệu (doc 05) | I | A | C | C | R | R | C | R |
| Consent & tuân thủ dữ liệu | A | R | C | C | C | I | I | C |
| Kickoff (doc 07) | A | R | R | C | I | C | I | I |
| Thiết kế giải pháp (doc 10) | I | A | C | R | C | C | C | C |
| Cấu hình CRM | I | I | A | C | R | I | I | I |
| Tích hợp | I | I | A | C | R | I | C | R |
| Chuyển đổi dữ liệu | I | C | A | C | R | C | I | C |
| Playbook Sales (doc 11) | C | A | I | R | I | R | I | I |
| Playbook Marketing & Sự kiện (doc 12) | C | A | I | R | I | R | I | I |
| UAT (doc 13) | I | A | R | R | C | R | C | C |
| Đào tạo | I | C | A | C | C | R | I | I |
| Quyết định go-live (`KG-3`) | A | R | R | C | C | C | I | C |
| Hypercare & bàn giao (doc 14) | I | C | A | C | R | C | I | R |
| Quyết định thay đổi phạm vi lớn | A | R | R | C | C | I | I | I |
| Fit-gap & Gap register (doc 15) | I | C | C | R | C | R | I | C |
| Quyết định vị trí gap L1/L2/L3 & slot roadmap | C | C | C | C | I | I | I | I |
| Phát triển tính năng sản phẩm | I | I | C | C | C | C | I | I |

> Hai dòng cuối do **Product Manager CRM** chịu trách nhiệm (A), đội sản phẩm thực hiện (R). Cột riêng không được thêm vì Product Council là cơ chế của chủ sản phẩm, không phải vai trò trong đội dự án.

## 4. Nhịp điều hành (Governance cadence)

| Cuộc họp | Tần suất | Thời lượng | Thành phần | Đầu ra |
|---|---|---|---|---|
| Steering Committee | 2 tuần/lần + tại mỗi gate | 45 phút | SteerCo | Quyết định, escalation đã xử lý, cập nhật RAID mức Cao |
| Họp tiến độ dự án | Hằng tuần | 60 phút | PM, Project Owner, BA, Admin | Cập nhật kế hoạch, RAID, CR |
| Sprint review / demo | Cuối mỗi sprint | 60 phút | Key users + đội dự án | Phản hồi trên **hệ thống thật**, không trên slide |
| Stand-up đội triển khai | Hằng ngày | 15 phút | Đội triển khai | Vướng mắc |
| Họp key user | Hằng tuần (trong giai đoạn build) | 45 phút | BA + key users | Làm rõ yêu cầu, xem cấu hình |
| Hypercare check-in | Hằng ngày tuần 1–2, sau đó 2 lần/tuần | 15–30 phút | Admin, key users | Danh sách lỗi/yêu cầu, ưu tiên |

**Báo cáo tình trạng hằng tuần** (gửi Sponsor, ≤ 1 trang): trạng thái tổng (Xanh/Vàng/Đỏ) · 3 việc đã xong · 3 việc tuần tới · quyết định cần Sponsor · top 3 rủi ro · ngày còn lại đến mốc kế tiếp.

## 5. Ma trận escalation

| Cấp | Loại vấn đề | Người xử lý | Thời hạn phản hồi |
|---|---|---|---|
| 1 | Làm rõ yêu cầu, lỗi cấu hình | BA ↔ Key user | [ĐIỀN, ví dụ 1 ngày làm việc] |
| 2 | Xung đột yêu cầu giữa bộ phận; trễ cung cấp dữ liệu | PM ↔ Project Owner | [ĐIỀN] |
| 3 | Ảnh hưởng mốc, ngân sách, phạm vi; xung đột không giải quyết ở cấp 2 | SteerCo | Họp SteerCo kế tiếp hoặc họp khẩn trong [ĐIỀN] ngày |

## 6. Kênh liên lạc dự án

| Mục đích | Kênh | Quy ước |
|---|---|---|
| Quyết định chính thức | Email + Decision log (doc 08) | Quyết định chỉ có hiệu lực khi đã ghi vào Decision log |
| Trao đổi nhanh | [ĐIỀN: nhóm Zalo / Slack / Teams] | Không chốt yêu cầu qua chat |
| Tài liệu | [ĐIỀN: Google Drive / SharePoint] | Một thư mục, cấu trúc theo số doc của kit |
| Lỗi & yêu cầu | [ĐIỀN: Jira / sheet theo dõi] | Mỗi mục có ID, người tạo, mức độ |
