# 05 · Data Readiness & Tuân thủ dữ liệu

**Giai đoạn:** Trước kickoff (bắt đầu T-4 tuần), tiếp tục đến UAT · **Chủ trì:** Data lead (phía triển khai) + đầu mối pháp chế/IT trường
**Áp dụng BP-01:** `BR-07` (privacy mặc định), `P-05` Data Privacy, `P-06` Audit, `P-07` Retention, enforcement point `E-4` (data layer)

> ⚠️ **Lưu ý pháp lý.** Phần §4 tóm tắt các yêu cầu thường gặp để đội dự án đặt đúng câu hỏi; **không** phải tư vấn pháp lý. Trường cần pháp chế/luật sư xác nhận áp dụng Nghị định 13/2023/NĐ-CP, Luật Bảo vệ dữ liệu cá nhân (Luật số 91/2025/QH15, hiệu lực từ 01/01/2026) và văn bản hướng dẫn mới nhất tại thời điểm triển khai.

---

## 1. Kiểm kê nguồn dữ liệu

Điền trong buổi S7 (doc 01) và cập nhật đến T-1 tuần.

| ID | Nguồn | Định dạng / hệ thống | Chủ sở hữu | Số bản ghi (ước/đếm) | Khoảng thời gian | Chất lượng (1–5) | Chuyển đổi? |
|---|---|---|---|---|---|---|---|
| SRC-01 | File Excel tuyển sinh tổng | .xlsx (Drive) | Phòng TS | | | | Có |
| SRC-02 | Excel riêng từng tư vấn viên | .xlsx cá nhân | Từng TVV | | | | Gộp vào SRC-01 trước |
| SRC-03 | Meta Lead Ads (form) | Export CSV / Ads Manager | Marketing | | | | 12 tháng gần nhất |
| SRC-04 | Form website | DB website / email | Marketing | | | | |
| SRC-05 | Đăng ký sự kiện | Google Forms / Sheets | Marketing | | | | Có (lịch sử tham dự) |
| SRC-06 | Zalo OA (người quan tâm) | Zalo OA Manager | Marketing | | | | Chỉ liên kết ID, xem §3.4 |
| SRC-07 | Danh sách khoá ngắn hạn | Excel / LMS | Phụ trách NH | | | | Có |
| SRC-08 | Học sinh đang học | SIS | Học vụ | | | | Chỉ trường tối thiểu (tái ghi danh) |
| SRC-09 | Thanh toán giữ chỗ/học phí | Phần mềm kế toán | Kế toán | | | | Chỉ trạng thái |
| SRC-10 | Danh bạ trường THCS nguồn | Excel | Phòng TS | | | | Có (dữ liệu tham chiếu) |
| SRC-11 | Zalo cá nhân / điện thoại TVV | Không có cấu trúc | Từng TVV | Không xác định | | 1 | **Không** chuyển tự động — xem §5 |

## 2. Bộ trường dữ liệu tối thiểu (Minimum Viable Data)

Nguyên tắc **dữ liệu tối thiểu** (`BR-07`): chỉ thu thập trường có mục đích sử dụng rõ ràng. Mỗi trường dưới đây phải trả lời được "dùng để làm gì".

### 2.1 Phụ huynh (Contact — vai trò Parent)
| Trường | Bắt buộc | Mục đích | Ghi chú |
|---|---|---|---|
| Họ tên | ✔ | Xưng hô, tư vấn | |
| Số điện thoại chính | ✔ | Liên hệ, **khoá khử trùng lặp** | Chuẩn hoá về dạng `+84…` / `0…` thống nhất |
| Email | | Gửi tài liệu, xác nhận | |
| Quan hệ với học sinh | ✔ | Bố / Mẹ / Người giám hộ / Khác | Cần cho consent trẻ em |
| Zalo ID (qua Zalo OA) | | Gửi tin OA/ZNS | Chỉ khi người dùng đã tương tác/quan tâm OA |
| Kênh ưu tiên & khung giờ | | Tôn trọng trải nghiệm | |
| Quận/huyện | | Phân vùng, xe đưa đón | Không cần địa chỉ chi tiết ở giai đoạn lead |
| Trạng thái đồng ý (consent) | ✔ | Hợp pháp hoá xử lý | Xem §4 |

### 2.2 Học sinh (Contact — vai trò Student)
| Trường | Bắt buộc | Mục đích | Ghi chú |
|---|---|---|---|
| Họ tên | ✔ | Hồ sơ tuyển sinh | |
| Năm sinh | ✔ | Xác định lớp/năm học; xác định quy tắc consent trẻ em | Ngày sinh đầy đủ chỉ cần ở stage DH-4 trở đi |
| Lớp hiện tại | ✔ | Xác định dòng sản phẩm phù hợp | |
| Trường đang học (THCS nguồn) | ✔ | Phân tích feeder, sự kiện tại trường | Chọn từ danh mục SRC-10, không nhập tự do |
| Năm học dự kiến nhập học | ✔ (LN-DH) | Pipeline đúng đợt | |
| SĐT / email riêng của học sinh | ✗ | — | **Không thu thập mặc định.** Chỉ khi có lý do cụ thể + đồng ý của phụ huynh |
| Kết quả kiểm tra đầu vào, học bạ | Từ DH-4 | Xét tuyển, học bổng | Dữ liệu nhạy cảm hơn — phân quyền hạn chế (§4.3) |
| Thông tin sức khoẻ, hoàn cảnh gia đình | ✗ trong CRM | — | Thuộc SIS sau nhập học, không lưu ở CRM tuyển sinh |

### 2.3 Thực thể khác
- **Household:** tên hộ (tự sinh), danh sách thành viên, tổng số hồ sơ, giá trị trọn đời.
- **Hồ sơ tuyển sinh (Opportunity):** chương trình, năm học, stage, tư vấn viên, nguồn đầu tiên, nguồn chốt, đề xuất học bổng, trạng thái phê duyệt, lý do thua.
- **Chương trình/Khoá (Product):** mã, tên, dòng (`LN-DH`/`LN-NH`), học phí niêm yết, sĩ số tối đa, ngày khai giảng.
- **Sự kiện (Campaign):** xem doc 12 §3.

## 3. Quy tắc làm sạch & khử trùng lặp

### 3.1 Chuẩn hoá
- SĐT: bỏ khoảng trắng/dấu chấm; đổi đầu số cũ 11 số sang 10 số; loại số không đủ độ dài → hàng đợi "cần xác minh".
- Họ tên: Title Case tiếng Việt, giữ dấu; tách họ/tên nếu nền tảng yêu cầu.
- Trường THCS: ánh xạ biến thể ("THCS Ng. Du", "Nguyễn Du Q1") về một mã trong danh mục.
- Ngày tháng: `YYYY-MM-DD`.

### 3.2 Khoá trùng lặp (theo thứ tự)
1. Cùng SĐT phụ huynh (đã chuẩn hoá) → **cùng Household**.
2. Cùng email phụ huynh → ứng viên trùng, cần người xác nhận.
3. Cùng họ tên học sinh + năm sinh + trường THCS → ứng viên trùng học sinh.

Khi gộp: giữ **nguồn đầu tiên** (first touch) và **toàn bộ lịch sử tương tác**; tư vấn viên giữ hồ sơ là người có tương tác gần nhất trừ khi Trưởng TS chỉ định khác (D-05).

### 3.3 Ngưỡng chấp nhận chất lượng (đề xuất, chốt tại kickoff)
| Chỉ số | Ngưỡng |
|---|---|
| % bản ghi có SĐT hợp lệ | ≥ [ĐIỀN]% |
| % trùng lặp còn lại sau làm sạch | ≤ [ĐIỀN]% |
| % lead có nguồn (source) | ≥ [ĐIỀN]% (dữ liệu cũ thiếu nguồn → gán "Không rõ – dữ liệu cũ", không đoán) |
| % hồ sơ có trường THCS từ danh mục | ≥ [ĐIỀN]% |

### 3.4 Lưu ý theo kênh Việt Nam
- **Zalo:** CRM chỉ nhắn được qua Zalo OA/ZNS theo chính sách của Zalo; hội thoại trên Zalo cá nhân **không** đồng bộ được hợp lệ. ZNS là tin giao dịch/chăm sóc theo mẫu được duyệt — không dùng cho quảng cáo.
- **SMS brandname:** tách brandname CSKH và quảng cáo; tin quảng cáo tuân thủ khung giờ và quy định chống tin rác hiện hành.
- **Meta Lead Ads:** form phải có liên kết chính sách quyền riêng tư của trường và câu hỏi/mô tả đồng ý.

## 4. Tuân thủ dữ liệu cá nhân (áp `P-05`, `BR-07`)

### 4.1 Dữ liệu trẻ em — điểm đặc thù của trường THPT
Học sinh lớp 9–12 phần lớn **dưới 18 tuổi**; theo NĐ 13/2023 (Điều 20), xử lý dữ liệu cá nhân của trẻ em cần sự đồng ý của cha mẹ/người giám hộ, và với trẻ từ đủ 7 tuổi cần cả sự đồng ý của trẻ. Đội dự án **phải** để pháp chế xác nhận cách áp dụng theo Luật BVDLCN 2025 và văn bản hướng dẫn. Hàm ý thiết kế:

- Mặc định: phụ huynh là chủ thể liên lạc; **không** gửi marketing trực tiếp đến học sinh.
- Form do học sinh tự điền (ví dụ đăng ký thi thử): yêu cầu thông tin phụ huynh + cơ chế xác nhận của phụ huynh trước khi đưa vào chuỗi nurture.
- Ảnh/video học sinh tại sự kiện: consent riêng, không gộp vào consent nhận tin.

### 4.2 Mô hình consent tối thiểu
| Trường consent | Giá trị | Ghi nhận |
|---|---|---|
| Đồng ý xử lý để tư vấn tuyển sinh | Có / Không / Rút lại | Thời điểm, kênh, phiên bản văn bản thông báo |
| Đồng ý nhận tin marketing | Theo kênh: Zalo / SMS / Email / Gọi điện | Như trên |
| Đồng ý của phụ huynh cho dữ liệu học sinh | Có / Chưa | Người đồng ý, thời điểm |
| Đồng ý dùng hình ảnh | Có / Không | Theo sự kiện |

Quy tắc: **rút lại** phải dừng mọi automation marketing trong ≤ [ĐIỀN: `P-05.erasure_sla_days` / SLA dừng gửi] và được ghi audit (`P-06`).

### 4.3 Phân quyền (áp `P-01`)
| Vai trò | Xem | Sửa | Xuất dữ liệu |
|---|---|---|---|
| Tư vấn viên | Hồ sơ được gán + hồ sơ chưa gán trong đội ([ĐIỀN: `P-01.ownership_scope`]) | Hồ sơ được gán | ✗ |
| Trưởng TS | Toàn bộ `LN-DH` | Toàn bộ | Có, ghi log |
| Marketing | Lead, campaign, sự kiện; **không** xem kết quả kiểm tra đầu vào | Campaign, sự kiện | Có, ghi log |
| Phụ trách NH | `LN-NH` | `LN-NH` | Danh sách lớp |
| Kế toán | Trạng thái thanh toán, đề xuất học bổng đã duyệt | Trạng thái thanh toán | ✗ |
| Ban giám hiệu | Dashboard + toàn bộ | Phê duyệt | Có, ghi log |

### 4.4 Lưu trữ (áp `P-07` — tham số phải hỏi, không tự đặt)
| Loại dữ liệu | Thời hạn | Hành động khi hết hạn |
|---|---|---|
| Lead không chuyển đổi | [ĐIỀN: `P-07.cold_lead_months`] tháng kể từ tương tác cuối | Ẩn danh hoá hoặc xoá |
| Ghi âm cuộc gọi | [ĐIỀN: `P-07.call_recording_months`] tháng | Xoá |
| Hồ sơ đã nhập học | Chuyển sang SIS; CRM giữ [ĐIỀN] | Theo chính sách hồ sơ học sinh |
| Kết quả kiểm tra của người không nhập học | [ĐIỀN] | Xoá |

### 4.5 Việc cần làm trước go-live
- [ ] Văn bản thông báo xử lý dữ liệu cá nhân (privacy notice) cập nhật, đăng trên website, link trong mọi form
- [ ] Mẫu câu consent cho form web, Lead Ads, form sự kiện, kịch bản gọi điện (doc 11)
- [ ] Đánh giá tác động xử lý dữ liệu cá nhân (hồ sơ DPIA theo quy định) — pháp chế xác nhận nghĩa vụ và thời điểm nộp
- [ ] Nếu CRM lưu trữ ngoài Việt Nam: pháp chế xác nhận nghĩa vụ liên quan chuyển dữ liệu ra nước ngoài
- [ ] Quy trình xử lý yêu cầu của chủ thể dữ liệu (xem, sửa, xoá, rút đồng ý) — ai nhận, SLA
- [ ] Quy trình thông báo khi có sự cố lộ lọt dữ liệu

## 5. Xử lý "dữ liệu tối" trên Zalo cá nhân (SRC-11)

Không thể và không nên "chuyển đổi" hội thoại cá nhân. Kế hoạch đề xuất:
1. **Trước go-live:** mỗi tư vấn viên tự nhập danh sách phụ huynh đang theo dõi tích cực (mẫu Excel rút gọn: SĐT, tên, học sinh, stage, ghi chú gần nhất) — có buổi hướng dẫn và hạn chót.
2. **Từ go-live:** mọi trao đổi mới ghi vào CRM; chuyển dần phụ huynh sang Zalo OA của trường (mời quan tâm OA trong cuộc gọi).
3. **Sau 60 ngày:** đo OBJ-4 (doc 03).
4. Chính sách ghi nhận công (doc 11 §6) phải công bố **trước bước 1** — nếu không, tư vấn viên sẽ không nhập.

## 6. Kế hoạch chuyển đổi dữ liệu

| Bước | Việc | Người làm | Thời điểm |
|---|---|---|---|
| 1 | Kiểm kê nguồn (§1) | Data lead + IT trường | T-4 → T-1 tuần |
| 2 | Nhận file mẫu (extract) từ mỗi nguồn | Chủ sở hữu nguồn | T-2 tuần |
| 3 | Mapping trường nguồn → trường đích | BA + Data lead | Sau `KG-1` |
| 4 | Làm sạch & khử trùng lặp vòng 1 | Data lead; key user xác nhận ứng viên trùng | Sprint build |
| 5 | Nạp thử vào môi trường test, key user kiểm tra mẫu ngẫu nhiên [ĐIỀN] bản ghi | Admin + key users | Trước UAT |
| 6 | Nạp chính thức (delta từ lần nạp thử) | Admin | Cutover (doc 14) |
| 7 | Đối soát: số bản ghi nguồn vs. đích, tổng theo stage | Data lead + Project Owner | Ngay sau bước 6 |
