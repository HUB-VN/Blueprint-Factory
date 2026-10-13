# Changelog

## [1.2.0] — 2026-10-13

### Added
- **KIT-01 v1.2.0 · doc 15 Fit-Gap & Nâng cấp sản phẩm CRM** cho trường hợp đơn vị triển khai là chủ sản phẩm: nguyên tắc "một sản phẩm, không fork"; ba vị trí của gap (L1 sản phẩm lõi, L2 gói ngành giáo dục, L3 mở rộng riêng của khách hàng); cây quyết định xử lý gap; quy trình FG-1..FG-12 từ fit-gap sơ bộ đến cải tiến sau go-live; mẫu Gap register và đặc tả tính năng; Product Council; luồng phát triển song song với feature flag; gate `KG-D` Dev-complete.
- Nối doc 15 vào các tài liệu khác: fit-gap sơ bộ trong discovery và checklist `KG-0`; mục gap & nguyên tắc chi phí trong charter (DL-8, mốc M2b); quyết định D-10; rủi ro RK-14..RK-16; luồng sản phẩm trong kế hoạch triển khai; kịch bản UAT cho gap, workaround và hồi quy; nhịp release sau go-live.

## [1.1.0] — 2026-10-13

### Added
- **KIT-01 · CRM Kickoff Kit — Trường tư thục THCS & THPT** (`kits/crm-school-kickoff/`, v1.1.0): bộ 14 tài liệu trước và sau kickoff cho triển khai CRM Sales & Marketing ngành giáo dục phổ thông, áp dụng BP-01.
  - Tuyển sinh **mọi khối 6–12** với 4 loại tuyển sinh (đầu cấp, chuyển trường, lên cấp nội bộ, tái ghi danh) trên một pipeline `LN-DH`, kèm bảng Sức chứa theo năm học × khối × lớp (gate `G-4`).
  - **Sự kiện & chương trình đào tạo là sản phẩm** (`LN-SK`): sức chứa, loại vé (0đ hoặc có phí), thanh toán, check-in, hoàn thành; báo cáo hai mặt (doanh thu và tạo lead).
  - **Marketing ở dạng khám phá:** quy trình khám phá K1–K7, bảng kiểm kê điểm vào, taxonomy nguồn 3 cấp và cấu trúc chiến dịch 3 cấp (cố định cấu trúc, giá trị do trường cung cấp, chốt ở D-09), 4 mẫu tích hợp điểm vào A–D, thẻ thiết kế chuỗi nurture.
  - Các tài liệu: discovery, lịch mùa vụ & hành trình, charter, RACI, data readiness & dữ liệu trẻ em, checklist `KG-0`, agenda kickoff (D-01..D-09), biên bản/RAID/change log, kế hoạch sprint theo mùa vụ, solution design, playbook Sales, playbook Marketing & Sự kiện, UAT & đào tạo, go-live/hypercare/KPI.

## [1.0.0] — 2026-08-04

### Added
- **Dual Edition Publishing Standard v1.0** (`standard/`) — pack structure, ID conventions, per-file schemas, CLAUDE.md format, release checklist.
- **BP-01 · FlowX CRM Blueprint** (`packs/crm-blueprint-pack/`, v1.0.0) — first Agent Pack: journey (5 phases, gates G-1..G-5, 9 triggers), requirements BR-01..07, 15 services, 8 policies with 4 enforcement points, architecture decisions AD-01..05, runtime & ops runbook, guides for coding/business/product agents, validated manifest with checksums.
- **Human Edition site** (`site/`) — homepage with Dual Edition positioning, FlowX CRM blueprint page, 7-document HTML suite, `llms.txt`, markdown mirrors.
- **Pack validator** (`tools/validate_pack.py`) + CI workflow.
