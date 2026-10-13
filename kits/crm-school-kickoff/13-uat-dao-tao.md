# 13 · UAT & Đào tạo

**Giai đoạn:** Tuần 11 (mẫu kế hoạch doc 09) · **Chủ trì:** BA/QA (UAT), Trainer (đào tạo) · **Ký duyệt `KG-2`:** Project Owner + key users + PM

---

## 1. Nguyên tắc UAT

- Key user **tự thao tác** theo kịch bản trên môi trường có dữ liệu thử đã chuyển đổi — đội triển khai không làm thay.
- Kịch bản viết theo **hành trình thật** (một phụ huynh đi từ quảng cáo đến giữ chỗ), không theo màn hình.
- Mức độ lỗi: **Blocker** (không làm tiếp được hành trình) · **Critical** (sai dữ liệu/sai quy tắc, có workaround khó) · **Major** (bất tiện đáng kể) · **Minor** (giao diện, chính tả).
- Tiêu chí đạt `KG-2`: 100% kịch bản Critical pass; 0 Blocker; Critical mở = 0; Major mở ≤ [ĐIỀN] và có kế hoạch sửa trước go-live hoặc trong hypercare được PO chấp nhận.

## 2. Bộ kịch bản UAT

| ID | Kịch bản (end-to-end) | Mức | Vai trò test | Tham chiếu |
|---|---|---|---|---|
| UAT-01 | **Với mỗi điểm vào giai đoạn 1** (doc 10 §6.2): tạo lead thử → vào CRM trong độ trễ đã chốt, nguồn 3 cấp + UTM đúng taxonomy, consent ghi nhận. Mỗi điểm vào là một dòng kết quả riêng | Critical | Marketing | AU-01, IN-2x |
| UAT-02 | Lead trùng SĐT với hộ đã có → gộp đúng Household, giữ nguồn đầu tiên, không tạo hồ sơ mới thừa | Critical | Key user TS | doc 05 §3.2 |
| UAT-03 | Lead đạt `G-1` ở **mỗi cấp (THCS, THPT) và mỗi loại tuyển sinh** → khối nhập học đúng, gán đúng TVV theo D-05, task hạn đúng SLA | Critical | Key user TS | AU-03 |
| UAT-04 | Task quá SLA → cảnh báo TVV → báo Trưởng TS → chuyển TVV khác đúng mốc thời gian | Critical | Trưởng TS | AU-05 |
| UAT-05 | Lead không đạt `G-1` → vào chuỗi nurture tương ứng (theo thẻ thiết kế đã duyệt); có hành vi mới → chấm lại, đạt → gán | Major | Marketing | AU-04, `BR-02` |
| UAT-06 | Hồ sơ đi DH-1 → DH-6: validation từng stage chặn khi thiếu trường bắt buộc | Critical | Key user TS | doc 10 §3 |
| UAT-07 | Đề xuất học bổng dưới ngưỡng → không cần duyệt; trên ngưỡng bậc 2 / bậc 3 → đúng người duyệt; từ chối → TVV nhận thông báo | Critical | TVV + Trưởng TS + BGH | AU-10, `P-08` |
| UAT-08 | Kế toán xác nhận giữ chỗ → DH-6, thông báo học vụ, chuỗi sau giữ chỗ bắt đầu (nếu có) | Critical | Kế toán | AU-13 |
| UAT-09 | Cờ "Chờ kết quả trường khác" cho lead lớp 6 và lead lớp 10 → ngày kích hoạt lại đúng theo từng kỳ; đến ngày → task cho TVV | Major | Key user TS | AU-11 |
| UAT-09b | Chuyển trường vào khối **còn chỗ** → đi được đến DH-6, sức chứa giảm; vào khối **đã đầy** → cảnh báo, vào danh sách chờ; có chỗ → mời (AU-16) | Critical | Key user TS | doc 10 §3, AU-16 |
| UAT-09c | Đầu năm học: khối hiện tại của học sinh tự tăng; hồ sơ tái ghi danh / lên cấp nội bộ được tạo đúng (nếu trong phạm vi D-04) | Major | Admin | AU-15 |
| UAT-10 | Sự kiện **miễn phí**: đăng ký → xác nhận → nhắc theo nhịp → check-in QR → hồ sơ lên DH-3 → task follow-up trong SLA | Critical | Marketing + TVV | AU-06, AU-07 |
| UAT-10b | Sự kiện/chương trình **có phí**: đăng ký → thanh toán online → biên nhận → sức chứa giảm; quá hạn chưa trả → tự huỷ, trả chỗ; huỷ sau thanh toán → hoàn theo chính sách; hoàn thành → chứng nhận + khảo sát | Critical | Phụ trách sự kiện + Kế toán | doc 10 §3, IN-10 |
| UAT-10c | Sự kiện đầy → SK-W; có người huỷ → mời người chờ | Major | Marketing | AU-16 |
| UAT-11 | Người vắng mặt sự kiện → chuỗi "bỏ lỡ" đã duyệt (nếu có thẻ thiết kế) | Major | Marketing | AU-08 |
| UAT-12 | Walk-in tại sự kiện → tạo nhanh trên mobile kèm consent | Major | TVV | doc 12 §4.2 |
| UAT-13 | `LN-NH`: đăng ký khi lớp còn chỗ → NH-2; lớp đầy → NH-W; có người huỷ → mời người chờ đầu tiên | Critical | Phụ trách NH | doc 10 §3 |
| UAT-14 | HS ngoài trường **lớp 5** dự chương trình hè và HS ngoài trường **lớp 9** hoàn thành khoá ngắn hạn → lead `LN-DH` khối 6 / khối 10 được tạo; trong cửa sổ tuyển sinh thì gán, ngoài cửa sổ thì nurture | Critical | Phụ trách NH + TS | AU-09 |
| UAT-15 | Phụ huynh rút consent marketing → gỡ mọi chuỗi, chặn gửi, có audit log | Critical | Admin | AU-12, `P-05`, `P-06` |
| UAT-16 | Phân quyền: TVV không xem hồ sơ ngoài phạm vi; Marketing không xem kết quả kiểm tra; Kế toán chỉ thấy trường được phép | Critical | Admin | doc 05 §4.3 |
| UAT-17 | Với mỗi kênh nhắn tin chính thức đã tích hợp (D-07): gửi từ CRM / phụ huynh nhắn đến → hội thoại ghi vào timeline | Critical | TVV | IN-2x, `BR-03` |
| UAT-17b | Lead từ điểm vào chưa phân loại → nguồn "Khác – cần phân loại" → xuất hiện trong báo cáo rà soát của admin | Major | Admin | AU-17 |
| UAT-18 | Click-to-call → cuộc gọi + ghi âm ghi vào timeline | Major | TVV | IN-04 |
| UAT-19 | Dashboard Ban giám hiệu: số trên phễu **theo khối × loại tuyển sinh**, chỗ trống, doanh thu `LN-SK`/`LN-NH` khớp với đếm tay trên dữ liệu thử | Critical | PO + BA | doc 14 §4 |
| UAT-20 | Xuất danh sách nhập học theo mẫu SIS | Major | Học vụ / IT | IN-08 |
| UAT-21 | TVV nghỉ việc → Trưởng TS chuyển hàng loạt hồ sơ, lịch sử giữ nguyên | Major | Trưởng TS | doc 10 §8 |
| UAT-22 | Đối soát dữ liệu chuyển đổi: mẫu ngẫu nhiên [ĐIỀN] bản ghi khớp nguồn | Critical | Key users | doc 05 §6 |

**Mẫu ghi kết quả:**

| UAT | Người test | Ngày | Kết quả (Pass/Fail) | Lỗi (ID, mức) | Ghi chú | Re-test |
|---|---|---|---|---|---|---|

## 3. Kế hoạch đào tạo theo vai trò

| Vai trò | Hình thức | Thời lượng | Nội dung | Bài kiểm tra đạt |
|---|---|---|---|---|
| Tư vấn viên | Thực hành trên sandbox, nhóm ≤ 8 người | 2 × 2 giờ | Một ngày làm việc (doc 11 §1); ghi cuộc gọi; stage & validation theo loại tuyển sinh; kiểm tra chỗ trống; bán vé sự kiện; sự kiện trên mobile; kênh nhắn tin chính thức; đề xuất học bổng; dashboard cá nhân | Tự hoàn thành 1 hành trình DH-1→DH-6 trong ≤ 20 phút, không trợ giúp |
| Trưởng TS | 1–1 + nhóm | 3 giờ | Như TVV + gán lại, duyệt, dashboard đội, kiểm tra chất lượng dữ liệu, xử lý tranh chấp | Đọc và giải thích dashboard Tuyển sinh |
| Marketing | Nhóm | 3 giờ | Taxonomy nguồn của trường, Campaign 3 cấp, UTM, form, sự kiện như sản phẩm (vé, sức chứa), nurture, báo cáo kênh | Tạo một sự kiện có phí hoàn chỉnh từ đầu |
| Phụ trách khoá NH | Nhóm | 1,5 giờ | `LN-NH`, sĩ số, danh sách chờ | Xử lý kịch bản UAT-13 |
| Kế toán | 1–1 | 45 phút | Xác nhận giữ chỗ/học phí; xem học bổng đã duyệt | Xác nhận 1 giao dịch |
| Ban giám hiệu | 1–1 | 30 phút | Dashboard trên điện thoại; duyệt học bổng | Duyệt 1 yêu cầu trên mobile |
| Admin CRM trường | Kèm cặp xuyên suốt + 2 buổi chuyên sâu | 2 × 3 giờ + thực hành | Quản lý người dùng, phân quyền, picklist nguồn, sửa quy tắc đơn giản, xử lý lỗi tích hợp, báo cáo | Checklist doc 14 §5 |
| Nhân sự thời vụ | Video tự học + 1 buổi | 1 giờ | Phần TVV rút gọn | Hoàn thành 1 hành trình |

**Học liệu:** video ngắn 2–3 phút cho mỗi thao tác chính; "thẻ 1 trang" in cho bàn TVV; kênh hỏi đáp [ĐIỀN] trong hypercare; tài liệu người dùng lưu trong thư mục dự án và liên kết từ trang chủ CRM.

**Thời điểm:** đào tạo **không sớm hơn 5 ngày làm việc trước go-live** (để không quên) và **không trong vùng cấm** (doc 02).

## 4. Ký duyệt `KG-2`

| Mục | Kết quả |
|---|---|
| Số kịch bản Critical pass / tổng | __ / __ |
| Blocker mở | __ |
| Critical mở | __ |
| Major mở (kèm kế hoạch) | __ |
| Pháp chế duyệt privacy notice & mẫu consent (DP-06) | ☐ |
| % người dùng đạt bài kiểm tra | __% (mục tiêu [ĐIỀN]%) |
| Quyết định | ☐ Đạt ☐ Đạt có điều kiện ☐ UAT vòng 2 |
| Ký | Project Owner ____ · Key users ____ · PM ____ |
