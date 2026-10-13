# 14 · Go-live · Hypercare · KPI & Bàn giao

**Giai đoạn:** Tuần 12 → go-live + 90 ngày · **Chủ trì:** PM + Admin CRM · **Quyết định `KG-3`, `KG-4`:** Sponsor
**Áp dụng BP-01 runbook:** nhịp vận hành hằng ngày/tuần/tháng (`operating_rhythm`), health flows `HF-1`..`HF-4`.

---

## 1. Checklist cutover (go-live)

**T-5 ngày làm việc**
- [ ] `KG-2` đã đạt; mọi Critical đã đóng
- [ ] Thông báo cho toàn trường: ngày go-live, thay đổi gì, hỏi ai
- [ ] Đào tạo xong; tài khoản người dùng đã tạo, đăng nhập thử thành công 100%
- [ ] Các kênh gửi tin chính thức (theo D-07/D-09) và tên miền email đã hoạt động (DP-01, DP-04)
- [ ] Bảng Sức chứa theo khối/lớp đã cập nhật số thật
- [ ] Kế hoạch rollback đã viết (xem §1.1)

**T-1 ngày (đóng băng nguồn cũ)**
- [ ] Thông báo dừng nhập vào Excel tuyển sinh chung từ [giờ]; file chuyển chế độ chỉ đọc
- [ ] Xuất delta dữ liệu từ các nguồn kể từ lần nạp thử
- [ ] TVV hoàn thành mẫu "phụ huynh đang theo dõi" (doc 05 §5)

**Ngày D**
- [ ] Nạp dữ liệu chính thức (delta) → đối soát số bản ghi và tổng theo stage (Project Owner ký)
- [ ] Chuyển **từng điểm vào giai đoạn 1** (danh sách D-09) và tổng đài sang CRM production, theo danh sách kiểm có người ký từng dòng
- [ ] Gửi lead thử từ **mỗi** kênh → xác nhận vào đúng, gán đúng (smoke test)
- [ ] Bật các quy tắc tự động AU-01..AU-14 theo thứ tự: thu & gán trước, nurture sau cùng
- [ ] Đội triển khai có mặt tại phòng tuyển sinh (hoặc trực online) cả ngày

**D+1**
- [ ] Rà soát: lead qua đêm có vào đủ không, task có tạo không, tin tự động có gửi sai không
- [ ] Họp hypercare đầu tiên

### 1.1 Rollback
Điều kiện kích hoạt: thu lead từ ≥ 1 kênh chính lỗi > [ĐIỀN] giờ không khắc phục được, **hoặc** lỗi gửi tin hàng loạt sai đối tượng.
Hành động: chuyển form/kênh lỗi về đích cũ (email/Sheet) — **không rollback toàn hệ thống**; tắt automation gửi tin liên quan; ghi lại lead phát sinh để nạp bù.

## 2. Hypercare (mặc định 30 ngày)

| Tuần | Hỗ trợ | Họp | Trọng tâm |
|---|---|---|---|
| 1 | Có mặt tại chỗ [ĐIỀN] ngày + kênh hỏi đáp phản hồi ≤ 30 phút | Hằng ngày 15 phút | Lỗi, thao tác sai, dữ liệu thiếu |
| 2 | Kênh hỏi đáp ≤ 2 giờ | Hằng ngày | Adoption từng TVV; tinh chỉnh quy tắc |
| 3–4 | Kênh hỏi đáp ≤ 4 giờ | 2 lần/tuần | Báo cáo, chất lượng dữ liệu, chuyển giao cho admin trường |

**Phân loại yêu cầu trong hypercare:** Lỗi (sửa ngay theo mức độ) · Hướng dẫn (trả lời + bổ sung FAQ) · Yêu cầu mới (ghi CR — doc 08 §4, không làm "tiện tay").

**Theo dõi adoption hằng ngày** (dashboard nội bộ dự án): số người đăng nhập/ngày; số cuộc gọi được ghi/TVV; task quá hạn/TVV; % lead mới có liên hệ trong SLA; lead còn đi vào Excel/Zalo cá nhân (hỏi trực tiếp ở họp). TVV có chỉ số thấp → kèm cặp 1–1, **không** báo cáo lên Ban giám hiệu trong 2 tuần đầu.

### 2.1 Gate `KG-4` — Thoát hypercare
| Tiêu chí | Ngưỡng | Đạt? |
|---|---|---|
| Không còn lỗi Blocker/Critical mở | 0 | ☐ |
| OBJ-5 Adoption | ≥ [ĐIỀN]% TVV dùng hằng ngày 2 tuần liên tiếp | ☐ |
| % lead mới liên hệ trong SLA | ≥ [ĐIỀN]% | ☐ |
| Admin CRM trường đạt checklist §5 | 100% mục bắt buộc | ☐ |
| Tài liệu vận hành & FAQ bàn giao | Có | ☐ |
| Quyết định | ☐ Thoát ☐ Gia hạn 2 tuần | |

## 3. Nhịp vận hành sau bàn giao (phía trường)

| Nhịp | Việc | Người |
|---|---|---|
| Hằng ngày | Kiểm tra lỗi tích hợp & hàng đợi thử lại (`HF-1`, `HF-3`); lead chưa gán; task quá hạn toàn đội | Admin CRM |
| Hằng tuần | Họp đội tuyển sinh trên dashboard; họp Marketing–Tuyển sinh 2 tuần/lần (doc 12 §6); rà hồ sơ kẹt stage (`HF-2`) | Trưởng TS, Trưởng Marketing |
| Hằng tháng | Rà người dùng/phân quyền; dữ liệu trùng; consent bị rút đã xử lý; picklist nguồn mới | Admin CRM |
| Mỗi đợt tuyển sinh | Tạo Campaign theo cấu trúc 3 cấp; cập nhật học phí/ưu đãi niêm yết theo khối; cập nhật ngày công bố kết quả các kỳ tuyển sinh (AU-11); cập nhật Sức chứa | Marketing + Admin + Trưởng TS |
| Mỗi quý | Rà taxonomy nguồn: kênh mới, kênh không còn dùng (khám phá lặp lại, doc 12 §1.1 K7) | Marketing + Admin |
| Hằng năm (sau mùa) | Hiệu chỉnh xác suất stage & trọng số chấm điểm bằng dữ liệu thật; chạy chính sách lưu trữ `P-07`; review lý do thua | PO + Marketing + Admin |

## 4. Định nghĩa KPI (dùng thống nhất cho mọi dashboard)

| KPI | Công thức | Nguồn | Tần suất | Chủ sở hữu |
|---|---|---|---|---|
| Speed-to-lead (trung vị) | Trung vị (thời điểm liên hệ thực đầu tiên − thời điểm tạo lead), chỉ tính giờ làm việc | Activity | Hằng tuần | Trưởng TS |
| % lead liên hệ trong SLA | Lead liên hệ ≤ SLA / lead đủ điều kiện mới | Activity | Hằng tuần | Trưởng TS |
| Tỷ lệ đủ điều kiện | Lead đạt `G-1` / lead mới (theo nguồn) | Lead | Hằng tuần | Marketing |
| Tỷ lệ chuyển stage | Hồ sơ vào stage n+1 / hồ sơ vào stage n (theo cohort tháng tạo) | Opportunity | Hằng tháng | Trưởng TS |
| Tỷ lệ chuyển đổi tổng | Hồ sơ DH-6 / lead đủ điều kiện (theo cohort) | Opportunity | Theo đợt | Sponsor |
| Tỷ lệ tham dự sự kiện | Check-in / đăng ký | Opp `LN-SK` | Mỗi sự kiện | Marketing |
| % follow-up sự kiện ≤ 24h | Người tham dự có activity ≤ 24h / người tham dự | Activity | Mỗi sự kiện | Trưởng TS |
| Chi phí / nhập học theo kênh | Chi phí kênh / số DH-7 có nguồn [đầu tiên hoặc chốt] = kênh | Campaign + Opp | Theo đợt | Marketing |
| Tỷ lệ chuyển hoá `LN-NH`/`LN-SK` → `LN-DH` | HS ngoài trường hoàn thành `LN-NH` hoặc tham dự `LN-SK` có hồ sơ `LN-DH` DH-6 / tổng HS ngoài trường đủ điều kiện (đang ở khối trước một khối trường tuyển), **theo khối** | Opp | Hằng năm | PO |
| Doanh thu & lãi gộp `LN-SK` | Doanh thu sau hoàn/huỷ − chi phí trực tiếp − chi phí marketing, theo sự kiện và theo nhóm SK-A..D | Opp `LN-SK` + Campaign | Mỗi sự kiện / quý | Phụ trách sự kiện |
| Lấp đầy sự kiện | Đã tham dự / sức chứa | Opp `LN-SK` | Mỗi sự kiện | Phụ trách sự kiện |
| Chỗ trống theo khối | Sức chứa − đang học − đã giữ chỗ, theo năm học × khối | Bảng Sức chứa | Hằng tuần trong mùa | Trưởng TS |
| Thời gian xử lý chuyển trường | Trung vị (DH-6 − DH-1) cho loại Chuyển trường | Opp | Hằng tháng | Trưởng TS |
| Tỷ lệ giữ chân / lên cấp nội bộ | Học sinh học tiếp năm sau / học sinh đủ điều kiện, theo khối; riêng lớp 9 → 10 nếu liên cấp | Opp tái ghi danh | Hằng năm | Sponsor |
| % lead nguồn "Khác – cần phân loại" | Lead nguồn chưa phân loại / tổng lead | Lead | Hằng tháng | Admin + Marketing |
| **Tỷ lệ nhập học có điểm chạm trước** | DH-7 năm nay từng dự ≥ 1 sự kiện hoặc học ≥ 1 khoá `LN-NH` / tổng DH-7, **theo khối** | Opp + Campaign Member | Hằng năm | Sponsor |
| Lấp đầy lớp `LN-NH` | Đã thanh toán / sĩ số tối đa | Product | Mỗi khoá | Phụ trách NH |
| Adoption | TVV có ≥ 1 activity ghi nhận/ngày làm việc / tổng TVV | Activity | Hằng ngày (hypercare), hằng tuần sau đó | Admin |
| Chất lượng dữ liệu | % hồ sơ có việc tiếp theo; % DH-X có lý do; % lead có nguồn | Opp / Lead | Hằng tuần | Admin |

## 5. Checklist năng lực Admin CRM phía trường (bàn giao)

**Bắt buộc**
- [ ] Tạo/khoá người dùng, gán vai trò & phân quyền theo doc 05 §4.3
- [ ] Chuyển hàng loạt hồ sơ giữa TVV
- [ ] Thêm giá trị picklist (nguồn theo taxonomy, lý do thua, trường nguồn) theo quy trình; rà nguồn "Khác – cần phân loại" hằng tháng
- [ ] Cập nhật bảng Sức chứa theo khối/lớp; xử lý danh sách chờ
- [ ] Tạo sản phẩm sự kiện (sức chứa, loại vé, giá, chính sách hoàn/huỷ)
- [ ] Tạo Campaign mới theo cấu trúc 3 cấp và quy ước đặt tên (doc 12 §3) và form đăng ký sự kiện
- [ ] Thêm điểm vào lead mới bằng mẫu C/D (doc 10 §6.2) mà không cần đơn vị triển khai
- [ ] Đọc nhật ký lỗi tích hợp, chạy thử lại, biết khi nào gọi nhà cung cấp
- [ ] Xử lý yêu cầu chủ thể dữ liệu: xuất, sửa, xoá/ẩn danh, rút consent
- [ ] Sửa báo cáo/dashboard đơn giản (bộ lọc, khoảng thời gian)
- [ ] Biết danh sách tham số cấu hình (SLA, ngưỡng `P-08`, ngày kích hoạt AU-11) và nơi sửa

**Nên có**
- [ ] Sửa quy tắc tự động đơn giản (điều kiện, người nhận)
- [ ] Nhập dữ liệu hàng loạt có khử trùng lặp
- [ ] Cập nhật mẫu tin nhắn/email

## 6. Review sau go-live

| Mốc | Câu hỏi | Người dự | Đầu ra |
|---|---|---|---|
| D+30 | Hệ thống có được dùng không? Lỗi gì còn tồn? **Xem lại D-02** (định nghĩa lead) bằng dữ liệu | PO, Marketing, PM | Điều chỉnh quy tắc; quyết định `KG-4` |
| D+60 | OBJ-1, OBJ-3, OBJ-4 đang ở đâu? Dữ liệu còn nằm ngoài CRM không? | SteerCo | Kế hoạch cải thiện |
| D+90 / hết mùa | OBJ-1..OBJ-5 so với mục tiêu; bài học; phạm vi giai đoạn 2 (doc 03 §4.3) | SteerCo | Báo cáo kết thúc dự án + đề xuất giai đoạn 2 |

**Mẫu báo cáo kết thúc dự án (1–2 trang):** mục tiêu vs. thực tế (OBJ-1..5) · sản phẩm bàn giao DL-1..DL-7 · quyết định quan trọng & lệch chuẩn (DV-xx) · rủi ro còn mở chuyển cho vận hành · 5 bài học · đề xuất giai đoạn 2 kèm ước tính.
