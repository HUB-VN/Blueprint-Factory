# 10 · Thiết kế giải pháp CRM (Solution Design)

**Giai đoạn:** Sprint 0 · **Chủ trì:** Solution consultant · **Ký duyệt (`KG-1`):** Project Owner + Trưởng Marketing + PM
**Đầu vào:** doc 02 (hành trình), Decision log D-01..D-09 (doc 08), doc 05 (dữ liệu), kết quả khám phá Marketing (doc 12 §1–§3)
**Ranh giới FlowX (BP-01 `philosophy.md`):** quy tắc gate và ngưỡng nằm trong **rule engine / cấu hình**, không viết cứng trong workflow. Workflow không chứa con số. Danh mục kênh và nguồn là **dữ liệu cấu hình** (picklist, bảng tham chiếu), không phải logic: thêm kênh mới không được đòi sửa workflow.

---

## 1. Ánh xạ khái niệm sang nền tảng

| Khái niệm kit | BP-01 | HubSpot | Salesforce (Education Cloud / Sales Cloud) | Zoho CRM | Bitrix24 |
|---|---|---|---|---|---|
| Hộ gia đình | `SVC-ACCOUNT` | Company (đổi nhãn) hoặc custom object | Household Account | Account | Company |
| Phụ huynh / Học sinh | `SVC-CONTACT` | Contact + association label | Contact + Relationship | Contact | Contact |
| Lead chưa đủ điều kiện | `SVC-LEAD` | Contact lifecycle = Lead/MQL | Lead | Lead | Lead |
| Hồ sơ tuyển sinh (mọi khối) | `SVC-OPP` | Deal (pipeline `LN-DH`) | Opportunity / Application | Deal | Deal |
| Đăng ký khoá ngắn hạn | `SVC-OPP` / `SVC-ORDER` | Deal (pipeline `LN-NH`) | Opportunity hoặc Order | Deal | Deal / Smart Process |
| Đăng ký sự kiện / chương trình đào tạo | `SVC-OPP` / `SVC-ORDER` | Deal (pipeline `LN-SK`) + Marketing Event | Opportunity hoặc Order + Campaign Member | Deal + Campaign | Deal / Smart Process |
| Chương trình, khoá, sự kiện (sản phẩm) | `SVC-PRODUCT` | Product | Product / Program | Product | Product |
| Sức chứa theo khối/lớp, theo khoá, theo sự kiện | `SVC-INVENTORY` | Custom object / property | Custom object | Custom module | Smart Process |
| Chương trình năm, đợt, hoạt động marketing | `SVC-CAMPAIGN` | Campaign | Campaign (cha–con) | Campaign | Marketing / custom |
| Cuộc gọi, ghi chú, tin nhắn | `SVC-ACTIVITY` | Activity | Activity / Task | Activity | Activity |
| Nhắc việc, follow-up | `SVC-TASK` | Task + Sequence | Task / Cadence | Task / Cadence | Task / Robot |
| Học bổng, giá, giá vé | `SVC-PRICING` | Line item discount + approval | Price book + Approval process | Price book + Approval | Discount + workflow |
| Thanh toán vé / khoá online | `SVC-PAYMENT` | Payments / tích hợp cổng | Tích hợp cổng | Tích hợp cổng | Tích hợp cổng |
| Báo cáo | `SVC-ANALYTICS` | Reports/Dashboards | Reports/Dashboards | Analytics | Reports |

> Bảng chỉ là điểm xuất phát. Consultant kiểm tra tính năng theo gói license thực tế và ghi lệch chuẩn (deviation) vào §9.

## 2. Mô hình dữ liệu

```
 Trường nguồn (Account: Đối tác/Feeder — tiểu học, THCS, THPT) ◄── đang học ──┐
                                                                               │
 Hộ gia đình (Account: Household) 1───* Contact ───────────────────────────────┤
        │                                ├─ Phụ huynh (Parent, consent)
        │                                └─ Học sinh  (Student, năm sinh, khối hiện tại)
        │
        1───* Hồ sơ tuyển sinh (Opp LN-DH) ─── Khối nhập học (6–12) · Loại tuyển sinh · Năm học
        │          │                                   │
        │          └── *───1 Chương trình (Product)    └── kiểm tra ──► Sức chứa theo Năm học × Khối × Lớp
        │
        1───* Đăng ký khoá ngắn hạn (Opp LN-NH) *───1 Khoá/Lớp (Product + sức chứa)
        │
        1───* Đăng ký sự kiện (Opp LN-SK) *───1 Sự kiện (Product: ngày, sức chứa, loại vé, giá ≥ 0)
        │                                                 └── *───1 Campaign (marketing của sự kiện)
        │
        └── Contact *───* Campaign Member *───1 Campaign (cấp 1 › cấp 2 › cấp 3, doc 12 §3)
```

**Bảng Sức chứa** (mới, áp tinh thần `SVC-INVENTORY` + gate `G-4`): mỗi dòng = Năm học × Khối × Lớp, gồm: sĩ số tối đa, đang học, đã giữ chỗ, **còn trống** (tính tự động). Dùng để: chặn/cảnh báo khi nhận chuyển trường vào khối đã đầy, mở danh sách chờ, báo cáo Ban giám hiệu. Người cập nhật: [ĐIỀN, thường là Trưởng TS / học vụ].

**Trường tuỳ chỉnh then chốt** (bổ sung doc 05 §2):

| Đối tượng | Trường | Kiểu | Ghi chú |
|---|---|---|---|
| Opportunity | Dòng sản phẩm | Picklist `LN-DH` / `LN-NH` / `LN-SK` | Quyết định pipeline |
| Opportunity (`LN-DH`) | Khối nhập học | Picklist 6–12 (chỉ các khối trường có) | Bắt buộc từ DH-1 |
| Opportunity (`LN-DH`) | Loại tuyển sinh | Đầu cấp / Chuyển trường / Lên cấp nội bộ / Tái ghi danh | Quyết định bước bắt buộc (doc 02 §4.1) |
| Opportunity (`LN-DH`) | Năm học, Thời điểm nhập học dự kiến | Picklist / Ngày | Chuyển trường giữa năm cần ngày cụ thể |
| Opportunity | Đợt / Campaign cấp 2 | Lookup Campaign | |
| Opportunity | Nguồn đầu tiên / Nguồn chốt (3 cấp) | Theo taxonomy D-09 (doc 12 §2) | Nguồn đầu tiên không sửa được sau khi tạo (chỉ admin) |
| Opportunity (`LN-DH`) | Đang chờ kết quả trường khác | Checkbox + tên kỳ/trường + ngày công bố | Dùng cho mọi khối; kích hoạt AU-11 |
| Opportunity | Học bổng / ưu đãi đề xuất (%, VNĐ) | Số | Gắn quy trình `P-08` |
| Opportunity | Lý do thua | Picklist bắt buộc khi DH-X / NH-X / SK-X | Danh sách khởi đầu chốt ở D-03, ví dụ: học phí, chọn trường công lập, chọn trường tư khác, khoảng cách, không đạt đầu vào, **khối đã hết chỗ**, không liên lạc được, khác (bắt buộc ghi chú) |
| Opportunity (`LN-SK`) | Loại vé, giá vé, đã thanh toán, đã check-in, đã hoàn thành | Picklist / Số / Checkbox | Vé 0đ vẫn tạo Opportunity giá trị 0 |
| Product (sự kiện) | Nhóm SK-A/B/C/D, ngày giờ, địa điểm, sức chứa, đối tượng khối, chính sách hoàn/huỷ | Nhiều | doc 02 §4.3 |
| Contact (học sinh) | Khối hiện tại, Trường đang học | Picklist / Lookup trường nguồn | Tự tăng khối mỗi năm học (job `T-8`) |
| Contact | Điểm lead | Số (tính tự động) | Xem §4 |

## 3. Pipeline & quy tắc stage

**`LN-DH`:** stage DH-1..DH-7, DH-X như doc 02 §4.1 sau D-03.
- **Trường bắt buộc khi vào stage** (validation `P-02`) **phụ thuộc Loại tuyển sinh**: ví dụ DH-2 với *Chuyển trường* cần "Đã kiểm tra chỗ trống = Có"; DH-3 chỉ bắt buộc với *Đầu cấp*; DH-6 chỉ được chuyển khi **Kế toán xác nhận**; DH-X cần "Lý do thua".
- **Kiểm tra sức chứa:** khi mở hồ sơ hoặc chuyển DH-5 → DH-6, so với bảng Sức chứa. Khối đã đầy thì cảnh báo và đề xuất danh sách chờ; chỉ Trưởng TS được vượt (ghi audit `P-06`).
- **Cảnh báo kẹt stage** (tinh thần `HF-2`): ngưỡng ngày **khác nhau theo loại tuyển sinh** [ĐIỀN], vì chuyển trường gấp không thể chờ như đầu cấp.
- **Lên cấp nội bộ / Tái ghi danh:** hồ sơ được tạo hàng loạt từ danh sách học sinh đang học (job theo lịch D-04), không qua `G-1`.

**`LN-NH`:** NH-1..NH-4, NH-W, NH-X (doc 02 §4.2). Hết chỗ thì đăng ký mới tự vào NH-W.

**`LN-SK`:** SK-1..SK-6, SK-W, SK-N, SK-X (doc 02 §4.3). Vé 0đ bỏ qua SK-3. Vé có phí quá hạn thanh toán [ĐIỀN] giờ thì tự huỷ và trả chỗ.

## 4. Quy tắc tự động hoá (`CC-A`): danh mục

| ID | Kích hoạt | Điều kiện | Hành động | Tham chiếu |
|---|---|---|---|---|
| AU-01 | Lead mới từ bất kỳ điểm vào nào đã tích hợp (§6.2) | — | Chuẩn hoá SĐT, khử trùng lặp theo doc 05 §3.2, gắn nguồn 3 cấp theo bảng ánh xạ điểm vào → taxonomy, lưu UTM | `PH1-S1`, `BR-01` |
| AU-02 | Lead mới / cập nhật | Tính điểm | Điểm = Fit + Hành vi (bảng dưới) | `PH1-S3` |
| AU-03 | Điểm ≥ ngưỡng **và** tiêu chí D-02 | Gate `G-1` | Đủ điều kiện → xác định Khối nhập học + Loại tuyển sinh → gán TVV theo D-05 → task "Gọi lần đầu" với hạn = SLA D-08 | `G-1`, `PH2-S1` |
| AU-04 | Lead không đạt `G-1` | — | Vào chuỗi nurture phù hợp (thẻ thiết kế doc 12 §5); chấm lại khi có hành vi mới | `BR-02` |
| AU-05 | Task "Gọi lần đầu" quá hạn SLA | — | Cảnh báo TVV → sau [ĐIỀN] phút báo Trưởng TS → sau [ĐIỀN] phút **chuyển cho TVV khác** | D-08 |
| AU-06 | Đăng ký sự kiện (SK-2) | — | Xác nhận; vé có phí: link thanh toán + hạn; nhắc lịch theo nhịp đã chốt cho loại sự kiện | doc 12 §4.2 |
| AU-07 | Check-in sự kiện (SK-5) | Hộ có hồ sơ `LN-DH` đang mở | Đưa hồ sơ lên DH-3 nếu đang thấp hơn; task follow-up trong SLA | `G-2` |
| AU-08 | Vắng mặt (SK-N) | — | Chuỗi "bỏ lỡ"; vé có phí: áp chính sách hoàn/chuyển | |
| AU-09 | Học sinh **ngoài trường** check-in `LN-SK` hoặc hoàn thành `LN-NH` | Có khối kế tiếp mà trường tuyển | Tạo/cập nhật lead `LN-DH` với Khối nhập học = khối kế tiếp (doc 02 §5); trong cửa sổ tuyển sinh thì gán TVV, ngoài cửa sổ thì nurture dài hạn | doc 02 §5 |
| AU-10 | Học bổng/ưu đãi đề xuất vượt ngưỡng | Theo D-06 | Gửi duyệt đúng cấp; khoá chỉnh sửa đến khi có kết quả | `P-08`, `CC-C`, `E-3` |
| AU-11 | Cờ "Chờ kết quả trường khác" hoặc lý do thua = chọn trường khác có kỳ tuyển sinh | — | Đặt ngày kích hoạt lại = ngày công bố của kỳ đó (bảng tham chiếu theo khối/địa phương [ĐIỀN]); đến ngày → task ưu tiên cao | doc 02 §2 |
| AU-12 | Rút consent marketing | — | Gỡ khỏi mọi chuỗi, chặn gửi, ghi audit | `P-05`, `P-06` |
| AU-13 | Hồ sơ DH-6 (Won) | — | Trừ sức chứa; thông báo Kế toán & học vụ; task hoàn thiện hồ sơ; chuỗi chào mừng | `PH-4` |
| AU-14 | Hằng ngày [ĐIỀN giờ] | — | Bản tin cho mỗi TVV qua kênh nội bộ: việc hôm nay, việc quá hạn | `T-8` |
| AU-15 | Đầu mỗi năm học | — | Tăng "Khối hiện tại" của học sinh; tạo hồ sơ tái ghi danh / lên cấp nội bộ theo D-04 | `T-8` |
| AU-16 | Chỗ trống của một khối/lớp/khoá/sự kiện tăng lên | Có danh sách chờ | Mời người đầu danh sách chờ; hết hạn phản hồi thì mời người kế tiếp | `G-4` |
| AU-17 | Giá trị nguồn = "Khác – cần phân loại" | — | Gom vào báo cáo cho admin rà hằng tháng (bước K7) | doc 12 §1.1 |

**Mô hình chấm điểm lead** (khung; trọng số [ĐIỀN] sau khi có dữ liệu, ban đầu dùng quy tắc đơn giản). Tín hiệu hành vi theo kênh **chỉ thêm khi kênh đó có trong taxonomy D-09**:

| Nhóm | Tín hiệu | Điểm |
|---|---|---|
| Fit | Khối nhập học là khối trường đang tuyển và **còn chỗ** | [ĐIỀN] |
| Fit | Đang trong cửa sổ tuyển sinh của khối đó | [ĐIỀN] |
| Fit | Khu vực trong bán kính phục vụ | [ĐIỀN] |
| Fit | Trường đang học thuộc nhóm trường nguồn ưu tiên | [ĐIỀN] |
| Hành vi | Đăng ký / tham dự sự kiện; mua vé có phí | [ĐIỀN] / [ĐIỀN] / [ĐIỀN] |
| Hành vi | Học khoá ngắn hạn của trường | [ĐIỀN] |
| Hành vi | Chủ động liên hệ (gọi, nhắn) | [ĐIỀN] |
| Hành vi | [Tín hiệu theo kênh, từ khám phá] | [ĐIỀN] |
| Âm | Không liên lạc được ≥ 3 lần, số không tồn tại | [ĐIỀN] |

## 5. Phê duyệt học bổng / ưu đãi (`P-08`, `BR-04`)

- Ngưỡng là **tham số cấu hình** (`P-08.discount_threshold_pct`, `P-08.contract_value_threshold`) lấy từ D-06, có thể **khác nhau theo cấp / loại tuyển sinh**. Không viết cứng.
- Áp cho cả ưu đãi giá vé sự kiện và khoá ngắn hạn nếu vượt mức niêm yết.
- Mỗi đề xuất lưu: người đề xuất, lý do, phiên bản (`P-06` audit).
- Ưu đãi niêm yết (đăng ký sớm, anh chị em, học sinh trong trường) được áp tự động theo điều kiện, **không** cần duyệt.
- SLA duyệt [ĐIỀN] giờ làm việc; quá hạn thì nhắc người duyệt.

## 6. Tích hợp

### 6.1 Hệ thống lõi (cấu trúc cố định, công cụ cụ thể [ĐIỀN])

| ID | Hệ thống | Chiều | Dữ liệu | Phương thức giai đoạn 1 | Tần suất |
|---|---|---|---|---|---|
| IN-01 | Form trên website / landing page của trường | → CRM | Lead, UTM, consent, khối | Form nhúng của CRM / webhook | Thời gian thực |
| IN-04 | Tổng đài / hotline [ĐIỀN nhà cung cấp] | ↔ | Cuộc gọi, ghi âm (theo `P-07`), click-to-call | Connector | Thời gian thực |
| IN-06 | Email gửi đi | CRM → | Xác nhận, nurture | Dịch vụ email của CRM, tên miền đã cấu hình (DP-04) | Theo sự kiện |
| IN-07 | Kế toán | Kế toán → CRM | Giữ chỗ, học phí, thanh toán khoá/vé | File định kỳ hoặc xác nhận thủ công | Hằng ngày |
| IN-08 | SIS | ↔ | CRM → SIS: học sinh nhập học. SIS → CRM: danh sách đang học, sĩ số (cho Sức chứa & tái ghi danh) | File theo mẫu SIS | Theo đợt / hằng tháng |
| IN-09 | Check-in sự kiện | → CRM | Check-in QR, walk-in | App di động của CRM / form check-in | Thời gian thực |
| IN-10 | Thanh toán online cho vé/khoá [ĐIỀN cổng] | ↔ | Link thanh toán, kết quả | API cổng thanh toán | Thời gian thực |

### 6.2 Điểm vào lead và kênh gửi tin: **sinh ra từ khám phá**

Không định nghĩa trước. Mỗi dòng "Giữ" trong bảng kiểm kê doc 12 §1.2 trở thành một dòng tích hợp, mã `IN-2x` cấp khi chốt D-09:

| ID | Điểm vào / kênh (từ kiểm kê) | Chiều | Mẫu tích hợp | Dữ liệu tối thiểu | Ánh xạ sang taxonomy nguồn | Ưu tiên (giai đoạn 1/2) | Phụ thuộc (DP-xx) |
|---|---|---|---|---|---|---|---|
| IN-2x | | | A / B / C / D | | | | |

**Bốn mẫu tích hợp** (chọn mẫu cao nhất mà kênh cho phép):
- **A. API / connector chính thức:** thời gian thực, có nguồn tự động.
- **B. Webhook / form trung gian:** form của CRM đặt trên kênh, hoặc middleware chuyển tiếp.
- **C. Nhập file định kỳ:** export từ nền tảng → import có khử trùng lặp. Phải ghi rõ độ trễ chấp nhận được.
- **D. Nhập tay có cấu trúc:** form nhập nhanh trên mobile cho TVV hoặc lễ tân, nguồn chọn từ picklist. Dùng cho walk-in, giới thiệu miệng, kênh không có API.

Kênh **gửi tin** (nhắn tin, SMS, OTT…) được khám phá cùng lúc và phải thoả: là tài khoản chính thức của trường, có cơ chế consent/từ chối, có ghi lại lịch sử vào CRM (`BR-03`). Quy định riêng của từng nền tảng ghi trong doc 05 §3.4.

Mọi tích hợp có **nhật ký lỗi + hàng đợi thử lại** và người nhận cảnh báo (tinh thần `HF-3`, `R-3` của BP-01).

## 7. Báo cáo & dashboard

Mọi báo cáo `LN-DH` có bộ lọc **Cấp · Khối · Loại tuyển sinh · Năm học**.

| Dashboard | Người xem | Chỉ số chính |
|---|---|---|
| Ban giám hiệu | Sponsor | Phễu `LN-DH` theo khối × loại vs. chỉ tiêu; **chỗ trống theo khối**; dự báo nhập học; chi phí/nhập học theo nhóm nguồn; doanh thu `LN-NH` và `LN-SK` |
| Tuyển sinh | Trưởng TS | Speed-to-lead theo TVV; hồ sơ kẹt stage theo loại; chuyển đổi từng stage; lý do thua; tải theo TVV; danh sách chờ theo khối |
| Cá nhân TVV | Tư vấn viên | Việc hôm nay, quá hạn, hồ sơ của tôi theo stage, chỉ tiêu cá nhân |
| Marketing | Trưởng Marketing | Lead theo taxonomy nguồn và Campaign 3 cấp; % đủ điều kiện; chi phí/hồ sơ DH-4; chi phí/nhập học theo khối; trường nguồn top 20; số lead "Khác – cần phân loại" |
| Sự kiện & chương trình đào tạo | Marketing / phụ trách sự kiện | Hai mặt (doc 12 §4.3): doanh thu, lấp đầy, hài lòng **và** lead mới, follow-up đúng SLA, chuyển stage, nhập học |
| Khoá ngắn hạn | Phụ trách NH | Lấp đầy lớp, danh sách chờ, doanh thu, chuyển đổi sang `LN-DH` |

Định nghĩa công thức ở doc 14 §4.

## 8. Phân quyền

Theo doc 05 §4.3. Bổ sung: hồ sơ của TVV nghỉ việc được Trưởng TS chuyển hàng loạt; không xoá Contact (chỉ ẩn danh hoá theo `P-07`). Có thể phân TVV theo cấp (THCS/THPT) nếu D-05 chọn như vậy.

## 9. Lệch chuẩn so với BP-01 (Deviation log)

| ID | Điểm lệch | Lý do | Ảnh hưởng |
|---|---|---|---|
| DV-01 | `G-4` "In stock?" được hiểu là "còn chỗ": theo khối/lớp cho `LN-DH`, theo lớp cho `LN-NH`, theo sức chứa cho `LN-SK` | Sản phẩm giáo dục có giới hạn chỗ thay cho tồn kho | Bảng Sức chứa (§2) thay cho `SVC-INVENTORY` đầy đủ |
| DV-02 | `SVC-ORDER` không triển khai ở giai đoạn 1; đăng ký khoá/vé dùng Opportunity | Giảm phạm vi | Xem lại nếu bán đồng phục/sách qua CRM |
| DV-03 | [ĐIỀN theo nền tảng] | | |

## 10. Ký duyệt `KG-1`

| Vai trò | Họ tên | Đồng ý | Ghi chú/điều kiện | Ngày |
|---|---|---|---|---|
| Project Owner | | ☐ | | |
| Trưởng Marketing | | ☐ | | |
| PM | | ☐ | | |
