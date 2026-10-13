# 15 · Fit-Gap & Nâng cấp sản phẩm CRM

**Giai đoạn:** xuyên suốt dự án. Fit-gap sơ bộ trước kickoff → fit-gap chi tiết ở Sprint 0 → phát triển song song → phát hành → cải tiến sau go-live.
**Chủ trì:** BA (fit-gap) + **Product Manager của sản phẩm CRM** (quyết định đưa gap vào sản phẩm) + PM dự án (lịch, chi phí)
**Bối cảnh:** đơn vị triển khai **là chủ sản phẩm CRM**. Gap của trường có thể trở thành tính năng của sản phẩm. Đây vừa là lợi thế (khách hàng đầu tiên kéo sản phẩm vào ngành giáo dục), vừa là rủi ro: dự án bị kéo theo nhịp roadmap, hoặc sản phẩm bị "fork" thành nhiều phiên bản riêng cho từng khách hàng.

---

## 1. Nguyên tắc

1. **Một sản phẩm, không fork.** Không tạo nhánh mã nguồn riêng cho một trường. Mọi khác biệt giữa các khách hàng được thực hiện bằng **cấu hình**, **feature flag**, hoặc **extension point** (điểm mở rộng) của sản phẩm.
2. **Rẻ và ít rủi ro trước.** Thứ tự xem xét: điều chỉnh quy trình → cấu hình → tính năng sẵn có hoặc trên roadmap → mở rộng qua extension point → phát triển mới (§3).
3. **Mỗi gap có một vị trí trong sản phẩm** (§2): lõi, gói ngành giáo dục, hoặc mở rộng riêng của khách hàng. Vị trí này quyết định ai trả tiền, ai bảo trì và khi nào phát hành.
4. **Lịch mùa vụ thắng lịch roadmap.** Tính năng chưa kịp thì go-live bằng workaround, rồi phát hành sau ngoài vùng cấm (doc 02 §2). Không dời go-live vào mùa cao điểm để chờ tính năng.
5. **Không hứa ngoài sổ.** Một gap chỉ trở thành cam kết khi có trong Gap register với quyết định đã ký. Hứa miệng trong buổi demo không phải cam kết.

## 2. Ba vị trí của một gap trong sản phẩm

| Vị trí | Định nghĩa | Ví dụ trong dự án trường học | Ai trả chi phí | Ai bảo trì | Phát hành |
|---|---|---|---|---|---|
| **L1 · Sản phẩm lõi** | Nhu cầu chung của nhiều ngành, mọi khách hàng dùng được | Danh sách chờ chung cho mọi loại sức chứa; hồ sơ Household nhiều contact; xác nhận thanh toán | Chủ sản phẩm (đầu tư roadmap) [ĐIỀN chính sách] | Đội sản phẩm | Theo release train của sản phẩm |
| **L2 · Gói ngành giáo dục** | Nhu cầu chung của các trường học, dùng lại cho khách hàng giáo dục tiếp theo | Khối nhập học & loại tuyển sinh; bảng sức chứa năm học × khối × lớp; tự tăng khối mỗi năm; pipeline sự kiện có vé | Chia sẻ: chủ sản phẩm đầu tư, khách hàng đầu tiên có thể đồng tài trợ hoặc được ưu đãi [ĐIỀN] | Đội sản phẩm (nhánh ngành) | Theo release của gói ngành, bật bằng feature flag |
| **L3 · Mở rộng riêng của khách hàng** | Chỉ trường này cần; không có giá trị dùng lại rõ ràng | Mẫu xuất file sang đúng phần mềm SIS của trường; quy tắc học bổng đặc thù | Khách hàng (Change Request, doc 03 §9) | Theo hợp đồng bảo trì [ĐIỀN] | Theo lịch dự án, qua extension point |

**Câu hỏi phân loại (Product Manager trả lời):**
1. Có ít nhất [ĐIỀN, ví dụ 2] khách hàng hoặc khách hàng tiềm năng khác cần điều này không? Có → ứng viên L1/L2.
2. Nhu cầu có đặc thù ngành giáo dục không? Có → L2. Không → L1.
3. Làm được bằng cấu hình hoặc extension point mà không đổi lõi không? Được → ưu tiên L3 hoặc cấu hình.
4. Nếu đưa vào sản phẩm, có làm phức tạp sản phẩm cho các khách hàng khác không? Có → L3 hoặc thiết kế lại thành tuỳ chọn.

## 3. Cây quyết định xử lý gap

```
 Yêu cầu không khớp sản phẩm chuẩn
   │
   ├─► Trường có thể đổi quy trình mà không mất giá trị nghiệp vụ?        ── có ──► XỬ LÝ = ĐỔI QUY TRÌNH (ghi vào playbook doc 11/12)
   │
   ├─► Cấu hình sẵn có (trường, pipeline, rule, quyền, báo cáo) đáp ứng?  ── có ──► XỬ LÝ = CẤU HÌNH (đưa vào doc 10)
   │
   ├─► Tính năng đã có trên roadmap, phát hành trước mốc cần dùng?          ── có ──► XỬ LÝ = CHỜ ROADMAP + workaround đến khi có
   │
   ├─► Extension point / low-code / tích hợp đáp ứng?                        ── có ──► XỬ LÝ = MỞ RỘNG (thường L3)
   │
   └─► Còn lại                                                               ──────► XỬ LÝ = PHÁT TRIỂN MỚI (phân L1/L2/L3 theo §2)
                                                                                      │
                                                    kịp trước go-live? ── không ──► workaround + phát hành sau vùng cấm
```

## 4. Quy trình theo giai đoạn dự án

| Bước | Giai đoạn | Việc | Ai | Đầu ra | Liên kết |
|---|---|---|---|---|---|
| FG-1 | Trước kickoff (sau discovery) | **Fit-gap sơ bộ:** demo 8–10 kịch bản then chốt trên sản phẩm chuẩn. Đánh dấu gap lớn | BA + Consultant + Product Manager | Danh sách gap sơ bộ, ước tính thô (S/M/L) | doc 01 §11 |
| FG-2 | Trước kickoff | Đưa gap lớn vào charter/SOW: trong phạm vi hay phát sinh, phân L1/L2/L3 tạm, cam kết thời gian | PM + Product Manager + Sponsor | Charter §4.3 | doc 03 |
| FG-3 | Kickoff | Chốt **nguyên tắc** xử lý gap (D-10) | Sponsor + Product Manager | Decision log | doc 07 |
| FG-4 | Sprint 0 | **Fit-gap chi tiết bằng CRP** (Conference Room Pilot): key user chạy hành trình thật trên sandbox; mỗi bước được đánh dấu Fit / Fit sau cấu hình / Gap | BA + key users | Gap register đầy đủ (§5) | doc 02, doc 10 |
| FG-5 | Sprint 0 | **Họp phân loại gap** với Product Council (§7): áp cây quyết định §3, phân vị trí §2, chốt quyết định | Product Council | Mỗi gap có quyết định + D-xx | — |
| FG-6 | Sprint 0 → `KG-1` | Gap phải phát triển: viết **đặc tả** (§6), ước tính, xếp vào release | Product Manager + BA + Tech lead | Đặc tả + release target | — |
| FG-7 | `KG-1` | Gap register được ký cùng Solution Design | Project Owner + PM + Product Manager | Gap register ký duyệt | doc 10 §10 |
| FG-8 | Sprint 1–4 | **Luồng phát triển** song song với luồng cấu hình (§8) | Đội sản phẩm | Bản build trên staging | doc 09 |
| FG-9 | Trước UAT | **Gate `KG-D` Dev-complete** (§9) | Product Manager + PM | Quyết định: vào UAT / workaround | doc 09, doc 13 |
| FG-10 | UAT | Test kịch bản gap + **hồi quy** phần chuẩn | Key users + QA sản phẩm | Kết quả UAT | doc 13 |
| FG-11 | Go-live | Bật feature flag cho trường; release note; kế hoạch quay lui | Đội sản phẩm + Admin | Bản phát hành chạy production | doc 14 |
| FG-12 | Sau go-live | Tiếp nhận yêu cầu mới, backlog cải tiến, chu kỳ phát hành (§10) | Product Manager + Admin CRM trường | Roadmap cập nhật | doc 14 |

## 5. Gap register (sổ đăng ký gap)

Mỗi gap một dòng, mã `GAP-xx`, **không tái sử dụng mã** (như quy ước ID của BP-01).

| Trường | Nội dung |
|---|---|
| Mã | GAP-xx |
| Yêu cầu | Mô tả theo ngôn ngữ nghiệp vụ, kèm kịch bản CRP phát hiện ra gap |
| Dòng sản phẩm / hành trình | `LN-DH` / `LN-NH` / `LN-SK`; stage hoặc AU liên quan |
| Lý do nghiệp vụ | Điều gì xảy ra nếu không làm |
| Tần suất & quy mô | Bao nhiêu lần/tháng, bao nhiêu người dùng |
| Thời điểm cần | Ngày cụ thể, đối chiếu lịch mùa vụ (doc 02 §2) |
| Mức ưu tiên | Bắt buộc go-live / Cần trong mùa / Có thì tốt (MoSCoW) |
| Cách xử lý | Đổi quy trình / Cấu hình / Chờ roadmap / Mở rộng / Phát triển mới (§3) |
| Vị trí sản phẩm | L1 / L2 / L3 (§2) |
| Ước tính | Ngày công (dev + QA + tài liệu) |
| Workaround | Cách làm tạm nếu tính năng chưa kịp; ai chịu thao tác tay |
| Release target | Phiên bản / ngày |
| Thương mại | Trong phạm vi / Phát sinh (CR-xx) / Đầu tư sản phẩm / Đồng tài trợ |
| Rủi ro | Ảnh hưởng tới khách hàng khác, nợ kỹ thuật, bảo trì |
| Quyết định & người quyết | Làm / Workaround / Giai đoạn 2 / Không làm, kèm D-xx |
| Trạng thái | Mở → Đã quyết → Đặc tả → Đang phát triển → Dev-complete → UAT đạt → Đã phát hành → Đóng |

**Báo cáo hằng tuần** (gửi kèm báo cáo tình trạng doc 04 §4): số gap theo trạng thái; gap "Bắt buộc go-live" chưa Dev-complete; gap trễ release target.

## 6. Đặc tả cho gap phải phát triển (mẫu rút gọn)

```
GAP-xx · [Tên tính năng]                         Vị trí: L1 / L2 / L3     Release target: vX.Y / [ngày]

1. Vấn đề & bối cảnh nghiệp vụ        (từ Gap register, kèm kịch bản CRP)
2. Người dùng & tình huống             (vai trò; câu chuyện "Là … tôi muốn … để …")
3. Phạm vi                             trong / ngoài
4. Tiêu chí nghiệm thu                 Given / When / Then, đánh số AC-1, AC-2…
5. Cấu hình hoá                        Phần nào là tham số (không viết cứng): ngưỡng, danh sách, nhãn
                                       Feature flag: tên flag, mặc định TẮT với khách hàng khác
6. Dữ liệu                             Đối tượng/trường mới; migration; ảnh hưởng báo cáo
7. Quyền & tuân thủ                    Phân quyền; dữ liệu trẻ em (doc 05 §4); audit (P-06)
8. Tương thích                         Ảnh hưởng tới khách hàng hiện có; tương thích ngược API
9. Phi chức năng                       Hiệu năng (ví dụ check-in sự kiện đông người), khả dụng
10. Kế hoạch test                      Unit, tích hợp, hồi quy, kịch bản UAT tương ứng (doc 13)
11. Tài liệu                           Release note, hướng dẫn người dùng, tài liệu admin
12. Ký duyệt                           Product Manager · Tech lead · Project Owner (trường)
```

Khi viết đặc tả, áp ranh giới FlowX của BP-01: ngưỡng và quy tắc nằm trong cấu hình hoặc rule engine, không viết cứng trong workflow. Tính năng không được nhét logic gate vào service.

## 7. Product Council (cơ chế quyết định)

| Thành phần | Vai trò |
|---|---|
| Product Manager CRM (chủ trì) | Quyết định vị trí L1/L2/L3, slot roadmap |
| Tech lead sản phẩm | Ước tính, đánh giá kiến trúc, extension point |
| PM dự án | Ảnh hưởng lịch và chi phí dự án |
| BA / Consultant dự án | Trình bày gap và kịch bản |
| Đại diện Sales/Customer Success của sản phẩm | Giá trị dùng lại cho khách hàng khác |
| Project Owner phía trường (khi cần) | Xác nhận mức ưu tiên và workaround chấp nhận được |

- **Nhịp họp:** hằng tuần trong Sprint 0; 2 tuần/lần trong giai đoạn build.
- **SLA quyết định:** một gap mới phải có quyết định trong ≤ [ĐIỀN] ngày làm việc. Quá hạn thì escalate lên SteerCo, vì gap chưa quyết định sẽ chặn thiết kế.
- **Xung đột lợi ích:** khi lợi ích dự án (kịp go-live) và lợi ích sản phẩm (thiết kế tổng quát, chậm hơn) xung đột, SteerCo quyết định, có mặt người đại diện sản phẩm. Phương án mặc định: **làm phiên bản tối thiểu đúng hướng tổng quát** (thiết kế cho L2, phát hành phạm vi vừa đủ cho trường này).

## 8. Luồng phát triển song song

```
Luồng cấu hình (đội dự án)   S0 thiết kế ─ S1 nền tảng ─ S2 thu lead ─ S3 sự kiện ─ S4 báo cáo ─┐
                                                                                                  ├─ KG-D ─ UAT ─ KG-2 ─ Go-live
Luồng sản phẩm (đội sản phẩm) S0 đặc tả ─ build ─ code review ─ QA ─ staging ─ build cho UAT ───┘
                                            └── demo cuối mỗi sprint trên sandbox của trường
```

- Tính năng mới được triển khai lên **sandbox của trường dưới feature flag** sớm nhất có thể, để key user xem trong sprint review (doc 04 §4), không chờ đến UAT.
- **Feature freeze:** [ĐIỀN, khuyến nghị ≥ 10 ngày làm việc trước UAT]. Sau mốc này chỉ sửa lỗi.
- QA sản phẩm chạy **hồi quy đa khách hàng**: tính năng mới bật cho trường này không được làm thay đổi hành vi của khách hàng khác.

## 9. Gate `KG-D` · Dev-complete (trước UAT)

| Tiêu chí | Đạt? |
|---|---|
| Mọi gap "Bắt buộc go-live" ở trạng thái Dev-complete trên staging | ☐ |
| Tiêu chí nghiệm thu AC-x của từng gap đã được QA sản phẩm xác nhận | ☐ |
| Hồi quy sản phẩm đạt; không có lỗi Blocker/Critical mở | ☐ |
| Release note + hướng dẫn người dùng/admin của tính năng mới đã có | ☐ |
| Feature flag cấu hình đúng cho trường | ☐ |

| Không đạt → | Hành động |
|---|---|
| Gap chưa xong nhưng có workaround chấp nhận được | UAT bằng workaround; gap phát hành sau go-live, ngoài vùng cấm; ghi RAID |
| Gap chưa xong và không có workaround, mà gap là điều kiện go-live | SteerCo quyết định: rút phạm vi go-live, hoặc dời go-live **chỉ khi không chạm vùng cấm** (doc 02 §2) |

## 10. Sau go-live: cải tiến liên tục

| Hoạt động | Nhịp | Ai |
|---|---|---|
| Tiếp nhận yêu cầu từ trường qua kênh chính thức (không qua chat cá nhân); phân loại: Lỗi / Hướng dẫn / Cải tiến / Gap mới | Liên tục | Admin CRM trường → Customer Success sản phẩm |
| Lỗi: xử lý theo SLA hỗ trợ [ĐIỀN] | Liên tục | Đội sản phẩm |
| Cải tiến / gap mới: vào Gap register, đi lại §3 và §7 | Product Council | Product Manager |
| Thông báo roadmap cho trường (những gì sắp có, khi nào) | Hằng quý | Product Manager |
| Release note mỗi phiên bản; đào tạo lại nếu thay đổi thao tác | Mỗi release | Đội sản phẩm + Admin trường |
| **Lịch phát hành tránh mùa vụ**: không phát hành thay đổi lớn trong vùng cấm của trường (khách hàng giáo dục nên có lịch release riêng hoặc trì hoãn bật flag) | Mỗi release | Product Manager |
| Đưa bài học về **gói ngành giáo dục** và cập nhật kit/blueprint này (Deviation log doc 10 §9 → yêu cầu sản phẩm) | Sau mỗi dự án | Product Manager + BA |

## 11. Rủi ro đặc thù khi chủ sản phẩm triển khai

| Rủi ro | Dấu hiệu | Giảm thiểu |
|---|---|---|
| Dự án biến thành "dự án phát triển sản phẩm", trễ go-live | Gap register phình, nhiều gap L1/L2 "Bắt buộc go-live" | Giới hạn số gap phát triển trong giai đoạn 1 [ĐIỀN]; quy tắc §1.4 |
| Hứa tính năng ngoài sổ để chốt hợp đồng | Trường nhắc lại "đã được hứa" ở UAT | Fit-gap sơ bộ trước charter (FG-1, FG-2); §1.5 |
| Tuỳ biến riêng làm phân mảnh sản phẩm | Yêu cầu đổi lõi chỉ cho một khách hàng | §1.1; mặc định L3 qua extension point |
| Roadmap sản phẩm đổi ưu tiên, gap của trường bị đẩy lùi | Release target dời nhiều lần | Gap "Bắt buộc go-live" được khoá slot roadmap tại `KG-1`; đổi slot phải qua SteerCo |
| Phát hành phiên bản mới giữa mùa tuyển sinh làm gián đoạn | Lỗi xuất hiện sau release, đúng lúc đông lead | Lịch release tránh vùng cấm; feature flag; quay lui được |
