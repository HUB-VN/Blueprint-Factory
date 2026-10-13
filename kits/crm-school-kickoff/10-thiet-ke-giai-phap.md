# 10 · Thiết kế giải pháp CRM (Solution Design)

**Giai đoạn:** Sprint 0 · **Chủ trì:** Solution consultant · **Ký duyệt (`KG-1`):** Project Owner + Trưởng Marketing + PM
**Đầu vào:** doc 02 (hành trình), Decision log D-01..D-08 (doc 08), doc 05 (dữ liệu)
**Ranh giới FlowX (BP-01 `philosophy.md`):** quy tắc gate và ngưỡng nằm trong **rule engine / cấu hình**, không nằm cứng trong workflow; workflow không chứa con số.

---

## 1. Ánh xạ khái niệm sang nền tảng

| Khái niệm kit | BP-01 | HubSpot | Salesforce (Education Cloud / Sales Cloud) | Zoho CRM | Bitrix24 |
|---|---|---|---|---|---|
| Hộ gia đình | `SVC-ACCOUNT` | Company (đổi nhãn) hoặc custom object | Household Account | Account | Company |
| Phụ huynh / Học sinh | `SVC-CONTACT` | Contact + association label | Contact + Relationship | Contact | Contact |
| Lead chưa đủ điều kiện | `SVC-LEAD` | Contact lifecycle = Lead/MQL | Lead | Lead | Lead |
| Hồ sơ tuyển sinh | `SVC-OPP` | Deal (pipeline `LN-DH`) | Opportunity / Application | Deal | Deal |
| Đăng ký khoá ngắn hạn | `SVC-OPP` / `SVC-ORDER` | Deal (pipeline `LN-NH`) | Opportunity hoặc Order | Deal | Deal / Smart Process |
| Chương trình / Khoá | `SVC-PRODUCT` | Product | Product / Program | Product | Product |
| Đợt tuyển sinh, chiến dịch, sự kiện | `SVC-CAMPAIGN` | Campaign + Marketing Event | Campaign (cha–con) + Campaign Member | Campaign | Marketing / custom |
| Cuộc gọi, ghi chú, tin nhắn | `SVC-ACTIVITY` | Activity | Activity / Task | Activity | Activity |
| Nhắc việc, follow-up | `SVC-TASK` | Task + Sequence | Task / Cadence | Task / Cadence | Task / Robot |
| Học bổng / giá | `SVC-PRICING` | Line item discount + approval | Price book + Approval process | Price book + Approval | Discount + workflow |
| Báo cáo | `SVC-ANALYTICS` | Reports/Dashboards | Reports/Dashboards | Analytics | Reports |

> Bảng chỉ là điểm xuất phát — consultant kiểm tra tính năng theo gói license thực tế và ghi lệch chuẩn (deviation) vào §9.

## 2. Mô hình dữ liệu

```
 Trường THCS nguồn (Account: Đối tác/Feeder) ◄───── đang học ────┐
                                                                  │
 Hộ gia đình (Account: Household) 1───* Contact ──────────────────┤
        │                                ├─ Phụ huynh (vai trò Parent, consent)
        │                                └─ Học sinh  (vai trò Student, năm sinh, lớp)
        │
        1───* Hồ sơ tuyển sinh (Opportunity LN-DH)  *───1 Chương trình (Product)
        │          └─ Học sinh, năm học, stage, TVV, nguồn đầu/cuối, học bổng, lý do thua
        │
        1───* Đăng ký khoá ngắn hạn (Opportunity LN-NH) *───1 Lớp/Khoá (Product + sĩ số)
        │
        └── Contact *───* Campaign Member *───1 Sự kiện / Chiến dịch (Campaign LN-SK)
                                                  └─ cha: Đợt tuyển sinh năm học N+1
```

**Trường tuỳ chỉnh then chốt** (bổ sung doc 05 §2):

| Đối tượng | Trường | Kiểu | Ghi chú |
|---|---|---|---|
| Opportunity | Dòng sản phẩm | Picklist `LN-DH` / `LN-NH` | Quyết định pipeline |
| Opportunity | Năm học | Picklist `2027–2028`… | Một học sinh có thể có hồ sơ nhiều năm |
| Opportunity | Đợt tuyển sinh | Lookup Campaign | Sớm / Chính thức / Bổ sung |
| Opportunity | Nguồn đầu tiên / Nguồn chốt | Picklist (taxonomy doc 12 §2) | Không cho sửa tay sau khi tạo (chỉ admin) |
| Opportunity | Đang chờ kết quả thi công lập | Checkbox + ngày dự kiến | Kích hoạt chuỗi "sau khi có điểm" |
| Opportunity | Học bổng đề xuất (%, VNĐ) | Số | Gắn quy trình `P-08` |
| Opportunity | Lý do thua | Picklist bắt buộc khi DH-X | Học phí / Chọn công lập / Chọn trường tư khác / Khoảng cách / Học lực không đạt / Không liên lạc được / Khác (bắt buộc ghi chú) |
| Opportunity | Đối thủ | Lookup danh mục | Khi lý do = chọn trường khác |
| Contact | Điểm lead | Số (tính tự động) | Xem §4 |
| Product | Sĩ số tối đa / đã đăng ký / còn trống | Số / rollup | `LN-NH` |

## 3. Pipeline & quy tắc stage

**`LN-DH`:** stage DH-1..DH-7, DH-X đúng như doc 02 §3.1 sau D-03. Cấu hình:
- **Trường bắt buộc khi vào stage** (validation — `P-02`): DH-3 cần "Ngày trải nghiệm"; DH-4 cần "Lịch kiểm tra"; DH-5 cần "Kết quả" + "Học bổng đề xuất"; DH-6 chỉ được chuyển khi **Kế toán xác nhận** (hoặc tích hợp báo đã thu); DH-X cần "Lý do thua".
- **Không cho nhảy lùi** quá 1 stage nếu không có ghi chú.
- **Cảnh báo kẹt stage** (tinh thần `HF-2` của BP-01 runbook): hồ sơ ở một stage quá [ĐIỀN] ngày → task cho TVV, quá [ĐIỀN] ngày → báo Trưởng TS.

**`LN-NH`:** stage NH-1..NH-4, NH-W, NH-X (doc 02 §3.2). Khi "còn trống" = 0 → đăng ký mới tự vào NH-W.

**Tái ghi danh (nếu D-04 đưa vào phạm vi):** pipeline riêng `LN-DH / Tái ghi danh` với 4 stage: Đã khảo sát ý định → Xác nhận học tiếp → Đã nộp phí giữ chỗ → Rủi ro rời trường (chuyển `G-5`).

## 4. Quy tắc tự động hoá (`CC-A`) — danh mục

| ID | Kích hoạt | Điều kiện | Hành động | Tham chiếu |
|---|---|---|---|---|
| AU-01 | Lead mới từ bất kỳ kênh | — | Chuẩn hoá SĐT, khử trùng lặp theo doc 05 §3.2, gắn nguồn + UTM | `PH1-S1`, `BR-01` |
| AU-02 | Lead mới / cập nhật | Tính điểm | Điểm = Fit + Hành vi (bảng dưới) | `PH1-S3` |
| AU-03 | Điểm ≥ ngưỡng **và** tiêu chí D-02 | Gate `G-1` | Chuyển thành đủ điều kiện → gán TVV theo D-05 → tạo task "Gọi lần đầu" hạn = SLA D-08 | `G-1`, `PH2-S1` |
| AU-04 | Lead không đạt `G-1` | — | Vào chuỗi nurture phù hợp (doc 12 §4); chấm lại mỗi khi có hành vi mới | `BR-02` |
| AU-05 | Task "Gọi lần đầu" quá hạn SLA | — | Cảnh báo TVV → sau [ĐIỀN] phút báo Trưởng TS → sau [ĐIỀN] phút **chuyển lead cho TVV khác** | D-08 |
| AU-06 | Đăng ký sự kiện | — | Tin xác nhận + nhắc T-3 ngày, T-1 ngày, T-2 giờ (kênh theo consent) | doc 12 §3 |
| AU-07 | Check-in sự kiện | Contact có hồ sơ `LN-DH` mở | Chuyển hồ sơ lên DH-3 (nếu đang thấp hơn); task follow-up ≤ 24h | `G-2` |
| AU-08 | Vắng mặt sự kiện | — | Chuỗi "bỏ lỡ sự kiện" + mời sự kiện kế tiếp | |
| AU-09 | Hoàn thành khoá `LN-NH` | HS ngoài trường, lớp 8–9 | Tạo/cập nhật lead `LN-DH` năm phù hợp, gán TVV, đính kèm nhận xét (nếu có consent) | doc 02 §3.2 |
| AU-10 | Học bổng đề xuất vượt ngưỡng | Theo D-06 | Gửi duyệt đúng cấp; khoá chỉnh sửa đến khi có kết quả | `P-08`, `CC-C`, `E-3` |
| AU-11 | Lý do thua = Chọn công lập | — | Đặt ngày kích hoạt lại = ngày công bố điểm thi vào 10 [ĐIỀN] | doc 02 §1 |
| AU-12 | Rút consent marketing | — | Gỡ khỏi mọi chuỗi, chặn gửi, ghi audit | `P-05`, `P-06` |
| AU-13 | Hồ sơ DH-6 (Won) | — | Thông báo Kế toán & học vụ; task hoàn thiện hồ sơ; chuỗi chào mừng | `PH-4` |
| AU-14 | Hằng ngày 7:00 | — | Email/Zalo nội bộ cho mỗi TVV: việc hôm nay, việc quá hạn | `T-8` |

**Mô hình chấm điểm lead (khung — trọng số [ĐIỀN] sau khi có dữ liệu, ban đầu dùng quy tắc đơn giản):**

| Nhóm | Tín hiệu | Điểm |
|---|---|---|
| Fit | Học sinh đúng khối mục tiêu (lớp 9 cho `LN-DH`) | [ĐIỀN] |
| Fit | Khu vực trong bán kính phục vụ / có tuyến xe | [ĐIỀN] |
| Fit | Đến từ trường THCS nằm trong top feeder | [ĐIỀN] |
| Hành vi | Đăng ký / tham dự sự kiện | [ĐIỀN] / [ĐIỀN] |
| Hành vi | Xem trang học phí, tải brochure | [ĐIỀN] |
| Hành vi | Học khoá ngắn hạn của trường | [ĐIỀN] |
| Hành vi | Chủ động gọi hotline / nhắn OA | [ĐIỀN] |
| Âm | Không nghe máy ≥ 3 lần, số không tồn tại | [ĐIỀN] |

## 5. Phê duyệt học bổng / ưu đãi (`P-08`, `BR-04`)

- Ngưỡng là **tham số cấu hình** (`P-08.discount_threshold_pct`, `P-08.contract_value_threshold`) — lấy từ D-06, không viết cứng.
- Mỗi đề xuất lưu: người đề xuất, lý do (học lực / hoàn cảnh / anh chị em / đăng ký sớm / khác), phiên bản (`P-06` audit).
- Ưu đãi niêm yết (đăng ký sớm, anh chị em) áp tự động theo điều kiện, **không** cần duyệt.
- Kết quả duyệt thông báo cho TVV qua CRM + kênh nội bộ; SLA duyệt [ĐIỀN] giờ làm việc, quá hạn nhắc người duyệt.

## 6. Tích hợp

| ID | Hệ thống | Chiều | Dữ liệu | Phương thức giai đoạn 1 | Tần suất |
|---|---|---|---|---|---|
| IN-01 | Form website | → CRM | Lead, UTM, consent | Form nhúng của CRM / webhook | Thời gian thực |
| IN-02 | Meta Lead Ads | → CRM | Lead form | Connector chính thức / middleware | Thời gian thực |
| IN-03 | Zalo OA / ZNS | ↔ | Người quan tâm, tin nhắn, ZNS giao dịch | API Zalo OA qua connector / middleware | Thời gian thực |
| IN-04 | Tổng đài / hotline | → CRM | Cuộc gọi, ghi âm (theo `P-07`), click-to-call | Connector tổng đài [ĐIỀN] | Thời gian thực |
| IN-05 | SMS brandname | CRM → | Nhắc lịch, xác nhận | API nhà cung cấp | Theo sự kiện |
| IN-06 | Email | CRM → | Xác nhận, nurture | Dịch vụ email của CRM, tên miền đã cấu hình (DP-04) | Theo sự kiện |
| IN-07 | Kế toán | Kế toán → CRM | Trạng thái giữ chỗ / học phí | File định kỳ hoặc thao tác xác nhận thủ công | Hằng ngày |
| IN-08 | SIS | CRM → SIS | Học sinh đã nhập học | Xuất file theo mẫu SIS | Theo đợt |
| IN-09 | Check-in sự kiện | → CRM | Check-in QR | Ứng dụng di động của CRM / form check-in | Thời gian thực |

Mọi tích hợp có **nhật ký lỗi + hàng đợi thử lại** và người nhận cảnh báo (tinh thần `HF-3`, `R-3` của BP-01).

## 7. Báo cáo & dashboard

| Dashboard | Người xem | Chỉ số chính |
|---|---|---|
| Ban giám hiệu | Sponsor | Phễu `LN-DH` theo đợt vs. chỉ tiêu; dự báo nhập học; chi phí/nhập học theo kênh; doanh thu `LN-NH` |
| Tuyển sinh | Trưởng TS | Speed-to-lead theo TVV; hồ sơ kẹt stage; tỷ lệ chuyển đổi từng stage; lý do thua; tải theo TVV |
| Cá nhân TVV | Tư vấn viên | Việc hôm nay, quá hạn, hồ sơ của tôi theo stage, tiến độ chỉ tiêu cá nhân |
| Marketing | Trưởng Marketing | Lead theo nguồn/chiến dịch; % đủ điều kiện; chi phí/lead, chi phí/nhập học; feeder top 20 |
| Sự kiện | Marketing | Đăng ký → tham dự → follow-up đúng SLA → chuyển stage → nhập học, theo từng sự kiện |
| Khoá ngắn hạn | Phụ trách NH | Lấp đầy lớp, danh sách chờ, chuyển đổi sang `LN-DH` |

Định nghĩa công thức chi tiết ở doc 14 §4.

## 8. Phân quyền

Theo doc 05 §4.3. Bổ sung: hồ sơ của TVV nghỉ việc được Trưởng TS chuyển hàng loạt; không xoá Contact (chỉ ẩn danh hoá theo `P-07`).

## 9. Lệch chuẩn so với BP-01 (Deviation log)

| ID | Điểm lệch | Lý do | Ảnh hưởng |
|---|---|---|---|
| DV-01 | `G-4` "In stock?" được hiểu là "còn chỗ trong lớp" cho `LN-NH`; với `LN-DH` hiểu là "hồ sơ đủ & học phí đã thu" | Ngành giáo dục không có tồn kho vật lý | Không |
| DV-02 | `SVC-INVENTORY`, `SVC-ORDER` không triển khai ở giai đoạn 1; sĩ số dùng trường rollup trên Product | Giảm phạm vi | Xem lại nếu bán đồng phục/sách qua CRM |
| DV-03 | [ĐIỀN theo nền tảng] | | |

## 10. Ký duyệt `KG-1`

| Vai trò | Họ tên | Đồng ý | Ghi chú/điều kiện | Ngày |
|---|---|---|---|---|
| Project Owner | | ☐ | | |
| Trưởng Marketing | | ☐ | | |
| PM | | ☐ | | |
