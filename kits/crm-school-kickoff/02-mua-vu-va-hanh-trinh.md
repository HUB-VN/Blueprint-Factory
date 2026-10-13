# 02 · Mùa vụ tuyển sinh & Hành trình khách hàng

**Giai đoạn:** Trước kickoff · **Chủ trì:** BA + Trưởng Tuyển sinh · **Duyệt:** Ban giám hiệu
**Vì sao tài liệu này đi trước charter:** trong giáo dục, **lịch mùa vụ quyết định lịch dự án**. Go-live sai thời điểm (giữa đỉnh tuyển sinh) gần như chắc chắn thất bại về adoption, dù hệ thống tốt.
**Phạm vi:** trường tư thục THCS, THPT hoặc liên cấp. Trường tuyển ở **mọi khối lớp**, không chỉ đầu cấp.

---

## 1. Bốn loại tuyển sinh và khối lớp

Trường tư không chỉ tuyển ở đầu cấp: còn chỗ ở khối nào thì tuyển khối đó. CRM phải mô hình hoá được mọi trường hợp bằng **hai trường**: *Khối nhập học* (6–12) và *Loại tuyển sinh*.

| Loại tuyển sinh | Khối áp dụng | Thời điểm | Đặc điểm | Hỏi trong discovery |
|---|---|---|---|---|
| **Đầu cấp** | Lớp 6 (THCS), lớp 10 (THPT) | Theo mùa (§2) | Số lượng lớn nhất; cạnh tranh với kỳ tuyển sinh của trường công lập / chất lượng cao; có kiểm tra đầu vào | Chỉ tiêu từng khối đầu cấp |
| **Chuyển trường** | **Bất kỳ khối 6–12** | Quanh năm, thường đông vào hè và sau học kỳ 1 | Ra quyết định nhanh (vài ngày đến vài tuần); phụ thuộc **số chỗ còn trống của từng khối/lớp**; cần hồ sơ học bạ, giấy chuyển trường | Chính sách nhận chuyển trường từng khối, có khối nào đóng không |
| **Lên cấp nội bộ** | Lớp 9 → 10 (trường liên cấp) | Học kỳ 2 lớp 9 | Học sinh đã là "khách hàng" — rủi ro mất vào trường THPT khác; cần chăm sóc như tuyển sinh mới | Tỷ lệ học sinh lớp 9 ở lại lên lớp 10 |
| **Tái ghi danh** | Mọi khối đang học | Mỗi năm học (thường học kỳ 2) | Giữ chân; phát hiện sớm ý định rời trường | Tỷ lệ rời trường hằng năm theo khối |

**Hệ quả thiết kế:**
- Một pipeline `LN-DH` dùng chung, kèm trường *Khối nhập học* và *Loại tuyển sinh*. Một số bước có thể bỏ qua tuỳ loại (§3.1).
- Cần quản lý **sức chứa theo khối/lớp** cho năm học hiện tại và năm học tới: số chỗ còn trống của từng khối quyết định có nhận chuyển trường hay không (giống gate `G-4` "còn hàng?" của BP-01).
- Chỉ tiêu, báo cáo và dự báo đều **cắt theo khối** và **theo loại tuyển sinh**.

## 2. Lịch mùa vụ (khung — trường xác nhận từng dòng)

Lịch dưới là khung điển hình cho năm học N+1 bắt đầu tháng 8–9. Mốc của các kỳ tuyển sinh công lập / chất lượng cao **khác nhau theo tỉnh/thành và theo năm**. Ô `[ĐIỀN]` là mốc riêng của trường hoặc của địa phương, phải xác nhận trong discovery.

| Tháng | `LN-DH` Đầu cấp (lớp 6 & lớp 10) | `LN-DH` Chuyển trường & nội bộ | `LN-NH` Khoá ngắn hạn | `LN-SK` Sự kiện & chương trình đào tạo | Mức tải CRM |
|---|---|---|---|---|---|
| T9–T10 | Xây danh sách học sinh lớp 5 và lớp 9 tiềm năng | Chuyển trường đầu năm; khảo sát ý định tái ghi danh | CLB, khoá học kỳ 1 | Hội thảo phụ huynh đầu năm; workshop có phí | Thấp–TB |
| T11–T12 | **Mở tuyển sinh sớm** cả hai cấp | Lớp 9 nội bộ: tư vấn lên lớp 10 | Luyện thi chuyển cấp | Open Day, sự kiện tại trường nguồn | Trung bình |
| T1–T2 (Tết) | Nuôi dưỡng; kiểm tra đầu vào đợt sớm | **Chuyển trường sau học kỳ 1** | — | Ít sự kiện | Thấp–TB — **cửa sổ go-live tốt** |
| T3–T5 | **Đợt chính**; kiểm tra đầu vào; xét học bổng | Chốt tái ghi danh, lên cấp nội bộ | Mở đăng ký hè | Open Day, thi thử chuyển cấp, chương trình trải nghiệm | **Cao** |
| T5–T7 | Kỳ tuyển sinh công lập / chất lượng cao lớp 6 và lớp 10 [ĐIỀN ngày theo địa phương] → nhóm "chờ kết quả" tạm dừng, sau đó **đỉnh thứ hai** khi có kết quả | Chuyển trường hè bắt đầu | Trại hè, khoá hè | Trại hè, chương trình hè có phí | **Rất cao** |
| T7–T8 | Hoàn tất hồ sơ, nhập học, đợt bổ sung | **Đỉnh chuyển trường hè** (theo chỗ trống từng khối) | Kết thúc hè | Định hướng tân học sinh | Cao |
| Mốc riêng | [ĐIỀN: Open Day, hạn đợt sớm, ngày kiểm tra đầu vào từng cấp, ngày công bố kết quả tuyển sinh công lập tại địa phương] | [ĐIỀN] | [ĐIỀN] | [ĐIỀN] | |

**Hệ quả cho dự án (đưa vào doc 03 và doc 09):**
- **Vùng cấm go-live:** từ 2 tuần trước Open Day lớn nhất đến hết đỉnh thứ hai T5–T7. [ĐIỀN ngày cụ thể]
- **Cửa sổ go-live khuyến nghị:** T12–T2 (trước đợt chính) hoặc T9–T10 (sau mùa, chuẩn bị cho năm sau).
- Vì chuyển trường diễn ra quanh năm, **không có thời điểm nào "không có lead"**. Kể cả go-live trong cửa sổ tốt vẫn phải bảo đảm kênh thu lead liên tục (doc 14 §1).
- Nếu kickoff rơi vào T3–T7: go-live **MVP thu lead + sự kiện** trước, phần pipeline đầy đủ làm sau mùa.

## 3. Người tham gia quyết định (Decision-Making Unit)

| Vai | Ai | Vai trò trong quyết định | Hàm ý CRM |
|---|---|---|---|
| Người trả tiền | Bố/mẹ (thường 1 người chủ đạo) | Quyết định cuối, nhạy cảm học phí | Contact chính của Household; kênh liên lạc ưu tiên |
| Người dùng | Học sinh **10–17 tuổi** | Lớp 6: phụ huynh quyết định gần như toàn bộ. Lớp 10 và chuyển trường cấp 3: học sinh có tiếng nói lớn (môi trường, bạn bè, CLB) | Contact phụ; **dữ liệu trẻ em** — hạn chế liên lạc trực tiếp (doc 05) |
| Người ảnh hưởng | Ông bà, giáo viên chủ nhiệm, phụ huynh khác | Uy tín, truyền miệng | Trường "Người giới thiệu" trên Opportunity |
| Người gác cổng | Trường nguồn (tiểu học, THCS) | Cho phép tổ chức sự kiện, phát tài liệu | Account loại "Đối tác"; quan hệ ngoài pipeline |

**Hệ quả:** mô hình hoá **Household** với ≥ 1 phụ huynh và ≥ 1 học sinh. Một Household có thể đồng thời có: hồ sơ lớp 6 cho em, tái ghi danh lớp 11 cho anh, và vé workshop cho cả hai. Xem doc 10 §2.

## 4. Hành trình theo dòng sản phẩm, ánh xạ vào BP-01

BP-01 định nghĩa 5 phase: `PH-1` Lead Management → `PH-2` Engagement → `PH-3` Opportunity → `PH-4` Delivery → `PH-5` Loyalty, với gate `G-1`..`G-5`. Kit **giữ nguyên cấu trúc phase-gate**, chỉ đổi tên bước cho ngành giáo dục.

### 4.1 `LN-DH` — Chương trình dài hạn (mọi khối, mọi loại tuyển sinh)

```
 Nguồn: mọi kênh trường đang có (khám phá ở doc 12 §1) · SỰ KIỆN (LN-SK) · KHOÁ NGẮN HẠN (LN-NH) · học sinh nội bộ
   │
   ▼
 PH-1  Lead mới ──► Làm giàu (khối hiện tại, trường đang học, khu vực) ──► Xác định Khối nhập học + Loại tuyển sinh ──► Chấm điểm
   │
   │   G-1  Đủ điều kiện? (khối nhập học trường có tuyển, có SĐT phụ huynh hợp lệ, có nhu cầu trong năm học xác định, có consent)
   │        không ──► nurture (BR-02: không bỏ lead; lead "còn sớm", ví dụ học sinh lớp 4, chờ đến đúng mùa)
   ▼ có
 PH-2  Gán tư vấn viên ──► Tư vấn lần đầu ──► KIỂM TRA CHỖ TRỐNG khối/lớp (bắt buộc với chuyển trường)
       ──► Mời tham quan / sự kiện ──► Ghi mọi tương tác (BR-03)
   │
   │   G-2  Quan tâm thật? (đã tham quan HOẶC dự sự kiện HOẶC đăng ký kiểm tra/phỏng vấn)
   │        không ──► nurture, mời sự kiện kế tiếp
   ▼ có
 PH-3  Mở hồ sơ ──► Kiểm tra đầu vào / xét học bạ / phỏng vấn ──► Đề xuất (học phí + học bổng: P-08) ──► Giữ chỗ
   │
   │   G-3  Đã nộp giữ chỗ?
   │        không ──► Lost + LÝ DO bắt buộc
   │                  └─► "Chờ kết quả trường khác" = nurture có ngày kích hoạt lại
   ▼ có
 PH-4  Hoàn thiện hồ sơ (học bạ, giấy chuyển trường) ──► Nộp học phí ──► Xếp lớp ──► Bàn giao sang học vụ/SIS
   │   G-4  Hồ sơ đủ, học phí đã thu, còn chỗ trong lớp?  không ──► nhắc + hỗ trợ / danh sách chờ (không im lặng, tinh thần BR-05)
   ▼
 PH-5  Đang học ──► Khảo sát hài lòng ──► Tái ghi danh / lên cấp nội bộ ──► Bán chéo LN-NH, LN-SK ──► Giới thiệu anh/chị/em
       G-5  Có vấn đề (khiếu nại, ý định rời trường)?  có ──► xử lý trước, KHÔNG upsell (BR-06)
```

**Trạng thái hồ sơ dùng chung** (tên stage chốt ở D-03):

| Stage | Tên | Tiêu chí vào | Đầu cấp | Chuyển trường | Lên cấp nội bộ / Tái ghi danh |
|---|---|---|---|---|---|
| DH-1 | Mới tiếp nhận | SĐT phụ huynh hợp lệ + khối nhập học + năm học | ✔ | ✔ | ✔ (tạo tự động từ danh sách học sinh) |
| DH-2 | Đã tư vấn | Cuộc gọi/gặp ≥ 3 phút được ghi; với chuyển trường: **đã xác nhận còn chỗ** | ✔ | ✔ | ✔ (khảo sát ý định) |
| DH-3 | Đã trải nghiệm | Tham quan HOẶC dự sự kiện (check-in thật) | ✔ | Tuỳ chọn | Bỏ qua |
| DH-4 | Đăng ký kiểm tra / xét hồ sơ | Có lịch kiểm tra/phỏng vấn hoặc đã nộp học bạ | ✔ | ✔ | Bỏ qua (hoặc xét điều kiện lên cấp) |
| DH-5 | Đã có kết quả & đề xuất | Kết quả + đề xuất học phí/học bổng đã gửi | ✔ | ✔ | ✔ (chính sách ưu đãi nội bộ) |
| DH-6 | Giữ chỗ (Won) | Kế toán xác nhận đã nhận tiền giữ chỗ | ✔ | ✔ | ✔ |
| DH-7 | Nhập học | Hồ sơ đủ + học phí kỳ 1 + đã xếp lớp trong SIS | ✔ | ✔ | ✔ |
| DH-X | Không thành công | Lý do từ danh sách chuẩn | ✔ | ✔ | ✔ (= rời trường; nuôi KPI giữ chân) |

Xác suất thắng mỗi stage để `[ĐIỀN]` có chủ ý, và nên khác nhau theo loại tuyển sinh (chuyển trường chốt nhanh hơn, tỷ lệ cao hơn). Chỉ đặt sau khi có dữ liệu ít nhất một mùa.

### 4.2 `LN-NH` — Khoá ngắn hạn

| Stage | Tên | Ghi chú |
|---|---|---|
| NH-1 | Quan tâm | Từ form, quảng cáo, giới thiệu, bán chéo |
| NH-2 | Đã đăng ký khoá | Chọn lớp cụ thể; kiểm tra sĩ số (`G-4`) |
| NH-3 | Đã thanh toán (Won) | Online hoặc kế toán xác nhận |
| NH-4 | Đang học → Hoàn thành | Điểm danh / hoàn thành |
| NH-W | Danh sách chờ | Lớp đầy, mời khi có chỗ hoặc mở lớp mới |
| NH-X | Huỷ / không thanh toán | Lý do chuẩn |

### 4.3 `LN-SK` — Sự kiện & chương trình đào tạo (là **sản phẩm**)

Mỗi sự kiện được mô hình hoá bằng **hai đối tượng**:
- **Sản phẩm sự kiện** (Product): tên, loại, ngày giờ, địa điểm, **sức chứa**, **loại vé và giá** (có thể 0đ), đối tượng (khối lớp, phụ huynh hay học sinh, học sinh trong hay ngoài trường), điều kiện hoàn/huỷ, có cấp chứng nhận không.
- **Chiến dịch của sự kiện** (Campaign): hoạt động marketing để bán vé hoặc kéo người đến; chi phí; nguồn đăng ký.

Mỗi người tham dự có một **Đăng ký sự kiện** (Opportunity của pipeline `LN-SK`), nên doanh thu sự kiện được đo giống hệt các sản phẩm khác.

**Phân loại sự kiện (khung — danh sách thực tế lấy từ discovery doc 01 §6):**

| Nhóm | Mục tiêu chính | Có thu phí | Ví dụ (để gợi ý khi hỏi) |
|---|---|---|---|
| SK-A · Chương trình đào tạo / trải nghiệm | **Doanh thu** + tạo lead | Thường có | Workshop kỹ năng, trại 1–3 ngày, khoá trải nghiệm cuối tuần, hội thảo chuyên đề cho học sinh |
| SK-B · Sự kiện tuyển sinh | **Tạo lead & chuyển đổi** `LN-DH` | Thường miễn phí | Open Day, ngày hội tuyển sinh, "Một ngày làm học sinh", thi thử chuyển cấp |
| SK-C · Sự kiện cộng đồng / phụ huynh | Uy tín, giữ chân, giới thiệu | Tuỳ | Hội thảo nuôi dạy con, ngày hội gia đình |
| SK-D · Sự kiện cho học sinh đang học | Doanh thu + giữ chân | Tuỳ | Dã ngoại, trại, cuộc thi, chương trình quốc tế ngắn ngày |

**Pipeline `LN-SK`:**

| Stage | Tên | Vé 0đ | Vé có phí | Hành động tự động |
|---|---|---|---|---|
| SK-1 | Quan tâm / được mời | ✔ | ✔ | — |
| SK-2 | Đã đăng ký | ✔ | ✔ | Xác nhận + lịch; với vé có phí: link thanh toán, hạn thanh toán |
| SK-3 | Đã thanh toán (Won) | Bỏ qua | ✔ | Biên nhận; trừ sức chứa |
| SK-4 | Đã xác nhận tham dự | ✔ | ✔ | Nhắc lịch theo nhịp doc 12 §4.2 |
| SK-5 | Đã tham dự | ✔ | ✔ | Check-in thật; task follow-up cho tư vấn viên nếu có nhu cầu `LN-DH` |
| SK-6 | Hoàn thành | Tuỳ | ✔ (chương trình nhiều buổi) | Chứng nhận; khảo sát; gợi ý sản phẩm tiếp theo |
| SK-W | Danh sách chờ | ✔ | ✔ | Mời khi có chỗ |
| SK-N | Vắng mặt | ✔ | ✔ | Chuỗi "bỏ lỡ"; với vé có phí: áp chính sách hoàn/chuyển [ĐIỀN] |
| SK-X | Huỷ | ✔ | ✔ | Hoàn tiền theo chính sách; trả lại sức chứa |

**Hai thước đo cho mỗi sự kiện**, luôn báo cáo cùng nhau: (1) **hiệu quả sản phẩm**: doanh thu, tỷ lệ lấp đầy, hài lòng; (2) **hiệu quả tạo lead**: lead mới, hồ sơ `LN-DH` tiến stage, số nhập học có điểm chạm từ sự kiện.

## 5. Dòng chảy giữa 3 dòng sản phẩm

```
           ┌──────────────────────┐   tham dự / hoàn thành   ┌────────────────────────┐
 Kênh ────►│ LN-SK Sự kiện &      │─────────────────────────►│ LN-DH Dài hạn           │◄── Kênh trực tiếp
 Trường ──►│ chương trình đào tạo │                          │ mọi khối 6–12           │    (khám phá doc 12)
 nguồn     │ (sản phẩm có doanh   │◄──── bán chéo ───────────│ đầu cấp · chuyển trường │
           │  thu)                │                          │ lên cấp · tái ghi danh  │
           └─────────┬────────────┘                          └─────▲─────────┬────────┘
                     │ đăng ký khoá                                │         │ đang học
                     ▼                                             │         ▼
           ┌──────────────────────┐  HS ngoài trường ở khối        │  ┌──────────────────┐
           │ LN-NH Ngắn hạn       │──trước khối tuyển (vd lớp 5, 9)┘  │ PH-5 Giữ chân     │
           │                      │◄──────────────────────────────────│ bán chéo NH & SK │
           └──────────────────────┘                                   └──────────────────┘
```

**Quy tắc bán chéo sang tuyển sinh (tổng quát):** học sinh **ngoài trường** tham dự `LN-SK` hoặc hoàn thành `LN-NH` ⇒ tạo/cập nhật lead `LN-DH` với *Khối nhập học* = khối kế tiếp mà trường có tuyển (lớp 6 nếu đang học tiểu học, lớp 10 nếu đang học THCS, hoặc khối hiện tại + 1 nếu là chuyển trường). Lead chỉ được gán tư vấn viên khi còn trong cửa sổ tuyển sinh của khối đó; nếu chưa đến mùa thì vào nurture dài hạn.

**Báo cáo bắt buộc phải trả lời được:** "Bao nhiêu học sinh nhập học năm nay, **theo từng khối**, đã từng tham dự ≥ 1 sự kiện hoặc học ≥ 1 khoá ngắn hạn trước đó?" Xem doc 14 §4.

## 6. Câu hỏi mở cần chốt ở kickoff

| # | Câu hỏi | Chuyển thành quyết định |
|---|---|---|
| 1 | Ngày cụ thể của vùng cấm go-live? | D-01 (doc 07) |
| 2 | Định nghĩa "Lead đủ điều kiện" (`G-1`) thống nhất giữa Marketing và Tuyển sinh? | D-02 |
| 3 | Stage DH-1..DH-7 và các bước bỏ qua theo loại tuyển sinh có phù hợp không? | D-03 |
| 4 | Giai đoạn 1 gồm những khối và loại tuyển sinh nào? Có gồm tái ghi danh, `LN-NH`, `LN-SK` có phí không? | D-04 |
| 5 | Kênh, nguồn lead, cấu trúc chiến dịch: ai cung cấp danh sách, khi nào workshop? | D-09 |
