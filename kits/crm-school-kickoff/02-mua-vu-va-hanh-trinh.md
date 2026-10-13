# 02 · Mùa vụ tuyển sinh & Hành trình khách hàng

**Giai đoạn:** Trước kickoff · **Chủ trì:** BA + Trưởng Tuyển sinh · **Duyệt:** Ban giám hiệu
**Vì sao tài liệu này đi trước charter:** trong giáo dục, **lịch mùa vụ quyết định lịch dự án**. Go-live sai thời điểm (giữa đỉnh tuyển sinh) gần như chắc chắn thất bại về adoption, dù hệ thống tốt.

---

## 1. Lịch mùa vụ (mẫu — xác nhận lại với trường)

Lịch dưới là khung điển hình cho trường THPT tư thục tại Việt Nam, tính cho **năm học N+1 bắt đầu tháng 8–9 năm N**. Trường phải xác nhận/sửa từng dòng; ô `[ĐIỀN]` là mốc riêng của trường.

| Tháng (năm N-1 → N) | `LN-DH` Khoá dài hạn | `LN-NH` Khoá ngắn hạn | `LN-SK` Sự kiện | Mức tải CRM |
|---|---|---|---|---|
| T9–T10 | Tái ghi danh sớm (khảo sát ý định lớp 10→11, 11→12); xây danh sách học sinh lớp 9 tiềm năng | CLB, khoá kỹ năng học kỳ 1 | Hội thảo phụ huynh đầu năm | Thấp |
| T11–T12 | **Mở đợt tuyển sinh sớm** lớp 10; ưu đãi đăng ký sớm | Luyện thi vào 10 (khai giảng) | Open Day #1, sự kiện tại trường THCS đối tác | Trung bình |
| T1–T2 (Tết) | Nuôi dưỡng; kiểm tra đầu vào đợt 1 | — | Ít sự kiện (Tết) | Thấp — **cửa sổ go-live lý tưởng** |
| T3–T4 | **Đợt tuyển sinh chính**; kiểm tra đầu vào, phỏng vấn; xét học bổng | Đăng ký trại hè mở | Open Day #2, Thi thử vào 10, "Một ngày làm học sinh" | **Cao** |
| T5 | Chốt giữ chỗ đợt chính; nhắc hạn | Đăng ký trại hè cao điểm | Hội thảo định hướng chọn trường | **Cao** |
| T6 | Thi vào 10 công lập — nhóm "chờ điểm" tạm dừng | Trại hè khai giảng | — | Trung bình |
| T6–T7 (sau khi có điểm) | **Đỉnh thứ hai**: nhóm chờ điểm quay lại, quyết định rất nhanh (3–10 ngày); đợt bổ sung | Trại hè đang chạy | Tư vấn trực tiếp tại trường, campus tour dày | **Rất cao** |
| T7–T8 | Hoàn tất hồ sơ, nhập học, bàn giao sang học vụ; chuyển trường | Kết thúc hè; khảo sát | Ngày nhập học / định hướng tân học sinh | Cao |
| Mốc riêng của trường | [ĐIỀN: ngày Open Day, hạn đợt sớm, ngày thi đầu vào…] | [ĐIỀN] | [ĐIỀN] | |

**Hệ quả cho dự án (đưa vào doc 03 và 09):**

- **Vùng cấm go-live** (code freeze): từ 2 tuần trước Open Day lớn nhất đến hết đỉnh T6–T7. [ĐIỀN ngày cụ thể]
- **Cửa sổ go-live khuyến nghị:** T12–T2 (trước đợt chính) hoặc T8–T10 (sau mùa, chuẩn bị cho năm sau).
- Nếu kickoff rơi vào T3–T7: go-live **MVP thu lead + sự kiện** trước, phần pipeline đầy đủ sau mùa. Không cố go-live toàn phần giữa mùa.

## 2. Người tham gia quyết định (Decision-Making Unit)

| Vai | Ai | Vai trò trong quyết định | Hàm ý CRM |
|---|---|---|---|
| Người trả tiền | Bố/mẹ (thường 1 người chủ đạo) | Quyết định cuối, nhạy cảm học phí | Contact chính của Household; kênh liên lạc ưu tiên |
| Người dùng | Học sinh lớp 9 (14–15 tuổi) | Ảnh hưởng mạnh, đặc biệt về môi trường, bạn bè, CLB | Contact phụ; **dữ liệu trẻ em** — hạn chế liên lạc trực tiếp (doc 05) |
| Người ảnh hưởng | Ông bà, giáo viên chủ nhiệm cấp 2, phụ huynh khác | Uy tín, truyền miệng | Trường "Người giới thiệu" trên Opportunity; Contact riêng nếu là referral |
| Người gác cổng | Trường THCS nguồn | Cho phép tổ chức sự kiện, phát tài liệu | Account loại "Đối tác"; quan hệ ngoài pipeline |

**Hệ quả:** Không mô hình hoá "Lead = 1 người". Mô hình hoá **Household** với ≥ 1 phụ huynh và ≥ 1 học sinh; một Household có thể có nhiều hồ sơ tuyển sinh (anh chị em, nhiều năm). Xem doc 10 §2.

## 3. Hành trình theo dòng sản phẩm, ánh xạ vào BP-01

BP-01 định nghĩa 5 phase: `PH-1` Lead Management → `PH-2` Engagement → `PH-3` Opportunity → `PH-4` Delivery → `PH-5` Loyalty, với gate `G-1`..`G-5`. Kit **giữ nguyên cấu trúc phase-gate**, chỉ đổi tên bước cho ngành giáo dục.

### 3.1 `LN-DH` — Khoá dài hạn (tuyển sinh lớp 10 / chuyển trường)

```
 Nguồn: Ads · Web · Hotline · Zalo OA · Walk-in · Giới thiệu · SỰ KIỆN (LN-SK) · KHOÁ NGẮN HẠN (LN-NH)
   │
   ▼
 PH-1  Lead mới ──► Làm giàu (trường THCS, khu vực, lớp) ──► Chấm điểm
   │                                                          │
   │   G-1  Đủ điều kiện? (đúng độ tuổi/lớp, có SĐT hợp lệ, khu vực phục vụ, có nhu cầu năm học N+1)
   │        không ──► Nuôi dưỡng dài hạn (nurture) ──► chấm lại (BR-02: không bỏ lead)
   ▼ có
 PH-2  Gán tư vấn viên ──► Gọi tư vấn lần đầu ──► Mời tham quan / sự kiện ──► Ghi mọi tương tác (BR-03)
   │
   │   G-2  Quan tâm thật? (đã tham quan HOẶC dự sự kiện HOẶC đăng ký kiểm tra đầu vào)
   │        không ──► nurture theo đợt, mời sự kiện kế tiếp
   ▼ có
 PH-3  Mở hồ sơ tuyển sinh ──► Kiểm tra đầu vào / phỏng vấn ──► Đề xuất (học phí + học bổng: P-08)
       ──► Thương lượng / giải đáp ──► Giữ chỗ
   │
   │   G-3  Đã nộp giữ chỗ?
   │        không ──► Closed Lost + LÝ DO bắt buộc (học phí / chọn công lập / chọn trường khác / khoảng cách / học lực)
   │                  └─► "Chọn công lập" = nurture nhóm chờ điểm, kích hoạt lại sau khi có điểm thi vào 10
   ▼ có
 PH-4  Hoàn thiện hồ sơ ──► Nộp học phí ──► Bàn giao sang học vụ/SIS ──► Định hướng tân học sinh
   │   G-4  Hồ sơ đủ & học phí đã thu?  không ──► nhắc + hỗ trợ (không im lặng — tinh thần BR-05)
   ▼
 PH-5  Đang học ──► Khảo sát hài lòng ──► Tái ghi danh 11/12 ──► Bán chéo khoá ngắn hạn ──► Giới thiệu anh/chị em
       G-5  Có vấn đề (khiếu nại, ý định rời trường)?  có ──► xử lý trước, KHÔNG upsell (BR-06)
```

**Định nghĩa trạng thái hồ sơ (dùng thống nhất trong báo cáo):**

| Stage | Tên | Tiêu chí vào (exit criteria của stage trước) | Xác suất mặc định |
|---|---|---|---|
| DH-1 | Mới tiếp nhận | Có ≥ 1 SĐT hợp lệ của phụ huynh + năm học dự kiến | [ĐIỀN] |
| DH-2 | Đã tư vấn | Có cuộc gọi/gặp ≥ 3 phút được ghi nhận | [ĐIỀN] |
| DH-3 | Đã trải nghiệm | Tham quan trường HOẶC dự sự kiện (check-in thật) | [ĐIỀN] |
| DH-4 | Đăng ký kiểm tra | Có lịch kiểm tra đầu vào / phỏng vấn | [ĐIỀN] |
| DH-5 | Đã có kết quả & đề xuất | Kết quả kiểm tra + đề xuất học phí/học bổng đã gửi | [ĐIỀN] |
| DH-6 | Giữ chỗ (Won) | Kế toán xác nhận đã nhận tiền giữ chỗ | 100% |
| DH-7 | Nhập học | Hồ sơ đủ + học phí kỳ 1 đã thu + đã tạo trong SIS | — |
| DH-X | Không thành công (Lost) | Có lý do thua từ danh sách chuẩn | 0% |

> Xác suất để `[ĐIỀN]` có chủ ý: chỉ đặt sau khi có dữ liệu lịch sử (ít nhất 1 mùa), nếu không forecast sẽ sai một cách tự tin.

### 3.2 `LN-NH` — Khoá ngắn hạn

Chu kỳ ngắn, nhiều giao dịch. **Không** bắt buộc đi qua mọi stage tư vấn — phần lớn tự đăng ký.

| Stage | Tên | Ghi chú |
|---|---|---|
| NH-1 | Quan tâm / đăng ký thông tin | Từ form, ads, giới thiệu |
| NH-2 | Đã đăng ký khoá | Chọn lớp cụ thể; kiểm tra sĩ số còn chỗ (tương ứng gate `G-4` "còn hàng?" của BP-01) |
| NH-3 | Đã thanh toán (Won) | Thanh toán online hoặc kế toán xác nhận |
| NH-4 | Đang học → Hoàn thành | Điểm danh/hoàn thành từ LMS hoặc nhập tay |
| NH-W | Danh sách chờ | Lớp đầy → tự động mời khi có chỗ / mở lớp mới |
| NH-X | Huỷ / không thanh toán | Lý do chuẩn |

**Quy tắc cross-sell (then chốt):** học sinh **ngoài trường** đang học lớp 8–9 hoàn thành `LN-NH` ⇒ tự động tạo/cập nhật lead `LN-DH` cho năm học phù hợp, gán tư vấn viên, kèm nhận xét giáo viên khoá ngắn hạn (nếu phụ huynh đồng ý — doc 05).

### 3.3 `LN-SK` — Sự kiện

Sự kiện là một **Campaign con** có vòng đời riêng; người tham dự là **Campaign Member** với trạng thái.

```
 Mời / quảng bá ──► Đăng ký ──► Xác nhận (ZNS/SMS/email) ──► Nhắc T-3 ngày, T-1 ngày, T-2 giờ
   ──► Check-in (QR) ──► Đã tham dự / Vắng mặt
         │                     │
         ▼                     ▼
   Follow-up ≤ 24h       Follow-up ≤ 48h: gửi tài liệu + mời sự kiện kế tiếp
   (tư vấn viên gọi;     (tự động; KHÔNG gọi dồn dập)
    lead LN-DH lên DH-3)
```

| Trạng thái thành viên | Định nghĩa | Hành động tự động |
|---|---|---|
| Đã mời | Có trong danh sách mời | — |
| Đã đăng ký | Điền form đăng ký | Tin xác nhận + lịch (ICS) |
| Đã xác nhận | Bấm xác nhận / trả lời nhắc | — |
| Đã tham dự | Check-in thật tại sự kiện | Task follow-up cho tư vấn viên (SLA [ĐIỀN] giờ) |
| Vắng mặt | Đăng ký nhưng không check-in | Chuỗi nurture "Xin lỗi vì đã bỏ lỡ" |
| Đi cùng | Người đi kèm không đăng ký trước | Tạo contact tại chỗ (cần consent) |

## 4. Bản đồ dòng chảy giữa 3 dòng sản phẩm

```
           ┌──────────────┐      tham dự      ┌──────────────┐
  Ads ────►│   LN-SK      │──────────────────►│   LN-DH      │◄─── Hotline / Walk-in / Giới thiệu
  THCS ───►│   Sự kiện    │                   │   Dài hạn    │
           └──────┬───────┘                   └──────▲───┬───┘
                  │ đăng ký khoá                     │   │ học sinh đang học
                  ▼                                  │   ▼
           ┌──────────────┐   HS ngoài trường lớp 8–9 │  ┌──────────────┐
           │   LN-NH      │───────────────────────────┘  │ PH-5 Giữ chân │──► bán chéo LN-NH
           │   Ngắn hạn   │◄─────────────────────────────│ & tái ghi danh│
           └──────────────┘                              └──────────────┘
```

**Báo cáo bắt buộc phải trả lời được:** "Bao nhiêu học sinh nhập học lớp 10 năm nay đã từng tham dự ≥ 1 sự kiện hoặc học ≥ 1 khoá ngắn hạn trước đó?" — đây là chỉ số chứng minh giá trị của CRM hợp nhất. Xem doc 14 §4.

## 5. Câu hỏi mở cần chốt ở kickoff

| # | Câu hỏi | Chuyển thành quyết định |
|---|---|---|
| 1 | Ngày cụ thể của vùng cấm go-live? | D-01 (doc 07) |
| 2 | Định nghĩa "Lead đủ điều kiện" (`G-1`) thống nhất giữa Marketing và Tuyển sinh? | D-02 |
| 3 | Stage DH-1..DH-7 có phù hợp quy trình trường không, cần thêm/bớt? | D-03 |
| 4 | Học sinh hiện hữu (tái ghi danh) có nằm trong phạm vi giai đoạn 1 không? | D-04 |
