# Triết lý FlowX

Năm tầng, mỗi tầng trả lời đúng một câu hỏi. Thành phần trả lời hai câu hỏi là thành phần đặt sai chỗ.

| Tầng | Câu hỏi | Trong pack này |
|---|---|---|
| **Trigger** | Điều gì khởi phát công việc? | `journey.yaml → triggers` (T-1..T-9) |
| **Flow** | Quy trình diễn ra thế nào? | `journey.yaml → phases` (PH-1..PH-5, G-1..G-5) |
| **Capability** | Khối năng lực nào thực thi? | `services.yaml` (SVC-*, 15 service) |
| **Policy** | Luật chơi nào ràng buộc? | `policies.yaml` (P-01..P-08, E-1..E-4) |
| **Runtime** | Nền tảng nào thực thi? | `architecture.yaml → runtime + infrastructure` |

Chiều mũi tên Trigger → Flow → Capability → Policy → Runtime cũng là **chiều tốc độ thay đổi**: trigger và flow đổi hằng tuần theo nghiệp vụ; capability đổi hằng quý; policy đổi khi luật chơi đổi; runtime gần như bất biến. Tách tầng đúng nghĩa là cô lập nhịp thay đổi.

Ba phép thử một kiến trúc FlowX đúng:

1. **Thêm kênh mới** = thêm một trigger, không sửa flow nào.
2. **Đổi luật chơi** = đổi tham số policy, không deploy code.
3. **Chịu tải gấp mười** = runtime hấp thụ, tầng nghiệp vụ không cần biết.

Anti-pattern nghiêm cấm: nhét logic rẽ nhánh vào capability; hard-code ngưỡng phê duyệt vào flow. Cả hai đưa hệ thống về điểm xuất phát.
