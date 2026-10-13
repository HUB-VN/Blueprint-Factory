# 12 · Playbook Marketing & Sự kiện

**Giai đoạn:** Soạn ở Sprint 2–3 · **Chủ trì:** Trưởng Marketing (BA hỗ trợ) · **Duyệt:** Ban giám hiệu
**Mục tiêu:** mọi lead có nguồn đo được; mọi sự kiện có vòng đời chuẩn và chuyển hoá thành hồ sơ tuyển sinh; nurture tôn trọng consent.

---

## 1. Cấu trúc chiến dịch trong CRM

```
Đợt tuyển sinh Năm học 2027–2028 (Campaign cha — LN-DH)
 ├── TS-SOM  Đợt tuyển sinh sớm
 │    ├── ADS-META-2026-11-LOP10-SOM
 │    ├── SK-OPENDAY-2026-12-06
 │    └── THCS-NGUYENDU-2026-11-HOITHAO
 ├── TS-CHINH  Đợt chính thức
 │    ├── SK-THITHU10-2027-03-15
 │    └── …
 └── TS-BOSUNG  Đợt bổ sung (sau điểm thi vào 10)

Hè 2027 (Campaign cha — LN-NH)
 ├── NH-TRAIHE-2027
 └── NH-LUYENTHI10-2026-2027
```

**Quy ước đặt tên:** `[LOẠI]-[KÊNH/TÊN]-[YYYY-MM(-DD)]-[ĐỐI TƯỢNG/GHI CHÚ]`, chữ in hoa không dấu, gạch nối. Loại: `ADS`, `SK` (sự kiện), `THCS` (tại trường đối tác), `NURT` (nurture), `REF` (giới thiệu), `NH` (khoá ngắn hạn).

## 2. Taxonomy nguồn lead & UTM

### 2.1 Nguồn (picklist cố định — chỉ admin thêm giá trị)

| Nhóm nguồn (Source group) | Nguồn (Source) | Ví dụ chi tiết (Source detail) |
|---|---|---|
| Quảng cáo trả phí | Meta Ads, Google Ads, TikTok Ads, Zalo Ads | Tên chiến dịch |
| Tự nhiên (organic) | Website/SEO, Fanpage, TikTok, YouTube, Zalo OA | Bài viết / video |
| Trực tiếp | Hotline, Walk-in | |
| Sự kiện | Sự kiện tại trường, Sự kiện tại THCS, Hội chợ giáo dục | Mã sự kiện |
| Quan hệ | Giới thiệu phụ huynh, Giới thiệu giáo viên/nhân viên, Đối tác THCS | Người giới thiệu (lookup Contact) |
| Nội bộ | Khoá ngắn hạn, Học sinh hiện hữu (anh/chị/em) | Mã khoá |
| Dữ liệu cũ | Không rõ – dữ liệu cũ | Chỉ cho dữ liệu chuyển đổi |

**Hai mốc ghi nhận:** *Nguồn đầu tiên* (first touch — không đổi) và *Nguồn chốt* (last touch trước DH-6). Báo cáo kênh hiển thị cả hai; Ban giám hiệu chọn mô hình ghi nhận chính tại D-xx (đề xuất: báo cáo song song cả hai trong năm đầu).

### 2.2 UTM bắt buộc cho mọi link có thể đo
| Tham số | Quy ước | Ví dụ |
|---|---|---|
| `utm_source` | nền tảng, chữ thường | `facebook`, `google`, `zalo`, `tiktok` |
| `utm_medium` | `cpc`, `social`, `email`, `zns`, `sms`, `qr`, `referral` | `cpc` |
| `utm_campaign` | = mã Campaign trong CRM, chữ thường | `ads-meta-2026-11-lop10-som` |
| `utm_content` | biến thể nội dung / mẫu quảng cáo | `video-campus-15s` |

QR in ấn (brochure, banner) luôn có `utm_medium=qr` và `utm_content` = vị trí in.

## 3. Quy trình sự kiện chuẩn (`LN-SK`)

### 3.1 Dòng thời gian

| Mốc | Việc | Người | Trong CRM |
|---|---|---|---|
| T-30 ngày | Tạo Campaign sự kiện: mục tiêu (số đăng ký, tham dự, hồ sơ DH-4), ngân sách, sức chứa, TVV phụ trách | Marketing | Campaign + mục tiêu |
| T-28 | Form đăng ký (có consent, câu hỏi: lớp, trường THCS, số người đi cùng); trang đích; QR | Marketing | Form gắn Campaign |
| T-25 → T-3 | Quảng bá: ads, OA, email nurture, TVV mời phụ huynh "nóng" (ghi "Người mời") | Marketing + TVV | Campaign Member: Đã mời / Đã đăng ký |
| Ngay khi đăng ký | Xác nhận + lịch | Tự động AU-06 | |
| T-3, T-1, T-2 giờ | Nhắc lịch; T-1: TVV gọi xác nhận nhóm ưu tiên | Tự động + TVV | Đã xác nhận |
| T-1 | In/nạp danh sách check-in; thử QR; phân công bàn đón theo TVV | Marketing | Danh sách theo TVV |
| Ngày D | Check-in QR; tạo nhanh người đi cùng/walk-in (có consent); TVV gặp trực tiếp phụ huynh của mình | Marketing + TVV | Đã tham dự; ghi chú nhanh trên mobile |
| D+0 tối | Tin cảm ơn + tài liệu; khảo sát 3 câu | Tự động | |
| D+1 | TVV gọi người tham dự (AU-07); chuỗi "bỏ lỡ" cho người vắng (AU-08) | TVV + tự động | Task follow-up |
| D+7 | Báo cáo sự kiện (§3.2) | Marketing | Dashboard Sự kiện |
| D+60 / hết mùa | Báo cáo chuyển hoá cuối (số nhập học từ sự kiện) | Marketing | |

### 3.2 Báo cáo sau sự kiện (mẫu 1 trang)

| Chỉ số | Mục tiêu | Thực tế |
|---|---|---|
| Đăng ký | | |
| Tham dự (check-in) / tỷ lệ tham dự | | |
| Lead mới (chưa có trong CRM trước sự kiện) | | |
| % người tham dự được follow-up ≤ 24h | 100% | |
| Hồ sơ lên DH-3 / DH-4 trong 14 ngày | | |
| Chi phí / người tham dự | | |
| Phản hồi khảo sát (điểm TB, 3 ý kiến nổi bật) | | |
| Bài học cho lần sau | | |

### 3.3 Sự kiện tại trường THCS đối tác
Ghi Account trường THCS là "Đối tác"; mỗi sự kiện tại trường gắn với Account đó; lead thu được tự gán Trường THCS nguồn. Duy trì lịch quan hệ (task định kỳ) với đầu mối ở trường — đây là quan hệ B2B nằm **ngoài** pipeline tuyển sinh.

## 4. Chuỗi nurture (theo consent và kênh ưu tiên)

| ID | Chuỗi | Ai vào | Thoát khi | Nhịp gợi ý | Nội dung |
|---|---|---|---|---|---|
| NURT-01 | Chào mừng lead mới | Lead mới chưa đạt `G-1` | Đạt `G-1` / rút consent | 0, 3, 7, 14 ngày | Giới thiệu trường; câu chuyện học sinh; mời sự kiện gần nhất |
| NURT-02 | Học sinh lớp 8 (dài hạn) | Lead lớp 8 | Lên lớp 9 → NURT-01 | Hằng tháng | Định hướng chọn trường, khoá ngắn hạn, trại hè |
| NURT-03 | Bỏ lỡ sự kiện | Vắng mặt (AU-08) | Đăng ký sự kiện kế tiếp | 0, 5 ngày | Video tóm tắt; mời sự kiện kế tiếp |
| NURT-04 | Chờ điểm thi công lập | Cờ chờ điểm / DH-X "chọn công lập" | Có điểm → TVV gọi | Thưa, 2–3 tuần/lần trước thi; dồn dập **không** | Thông tin hữu ích ôn thi; nhắc chính sách đợt bổ sung |
| NURT-05 | Sau giữ chỗ (DH-6 → DH-7) | DH-6 | DH-7 | Theo mốc hồ sơ | Hướng dẫn hồ sơ, học phí, ngày định hướng |
| NURT-06 | Bán chéo `LN-NH` | Phụ huynh có con đang học / HS lớp 8–9 | Đăng ký khoá / rút consent | Theo mùa (trước hè, đầu học kỳ) | Khoá hè, luyện thi, CLB |

**Quy tắc chung:** tần suất tối đa [ĐIỀN] tin marketing/tuần/phụ huynh trên mọi kênh cộng lại; không gửi 21:00–7:00; ZNS chỉ dùng cho tin giao dịch/chăm sóc theo mẫu đã duyệt; mọi tin có cách từ chối.

## 5. Bàn giao Marketing → Tuyển sinh (SLA hai chiều, theo D-02)

| Marketing cam kết | Tuyển sinh cam kết |
|---|---|
| Lead đủ điều kiện có SĐT hợp lệ, nguồn, consent | Liên hệ trong SLA D-08 |
| Không đẩy lead trùng, lead rác (lọc tự động AU-01) | Ghi kết quả liên hệ cho 100% lead được gán |
| Thông tin sự kiện/chiến dịch đến TVV trước T-7 | Gắn lý do khi đánh giá lead "không phù hợp" (để Marketing tối ưu) |

Họp chung 30 phút mỗi 2 tuần: xem dashboard Marketing + lý do loại lead.

## 6. Ngân sách & đo hiệu quả

- Nhập chi phí theo Campaign (hằng tuần từ nền tảng quảng cáo, hoặc tích hợp nếu có).
- Chỉ số ra quyết định: **chi phí / hồ sơ DH-4** (đến sớm, đủ tín hiệu) và **chi phí / nhập học** (chậm, chính xác). Chi phí/lead chỉ để tối ưu quảng cáo hằng ngày, không để so sánh kênh.
