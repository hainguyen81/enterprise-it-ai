# BẢNG CẢNH BÁO TOÀN CẦU: membership-hub

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕI

### 1.1. Phases & Day Logs

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | ./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java | Xây dựng dịch vụ đăng ký, đăng nhập, phân quyền, và cấu trúc cơ sở dữ liệu người dùng. | Coder | [ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[ARC-006],[ARC-007],[ARC-008],[ARC-009],[ARC-010],[REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-002],[EXC-004],[NFR-001],[NFR-002],[NFR-003],[NFR-004],[NFR-005],[NFR-006],[NFR-007],[NFR-008],[NFR-009] |
| 1 | 2 | ./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/user/UserServiceTest.java | Viết kiểm thử đơn vị cho dịch vụ người dùng và xác thực. | Tester | [REQ-001],[REQ-002],[REQ-003],[EXC-004],[NFR-001],[NFR-006] |
| 2 | 1 | ./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java | Xây dựng CRUD trung tâm, khóa học, và dịch vụ ghi danh. | Coder | [REQ-004],[REQ-005],[REQ-006],[REQ-007],[REQ-008],[REQ-009],[REQ-010],[REQ-011],[DAT-003],[DAT-004],[DAT-005],[NFR-001],[NFR-002],[NFR-003],[NFR-004],[NFR-005],[NFR-006],[NFR-007],[NFR-008],[NFR-009] |
| 2 | 2 | ./sources/backend/center-service/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java | Viết kiểm thử cho trung tâm, khóa học, và ghi danh. | Tester | [REQ-004],[REQ-005],[REQ-006],[REQ-007],[REQ-008],[REQ-009],[REQ-010],[REQ-011],[NFR-001],[NFR-006] |
| 3 | 1 | ./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java | Xây dựng dịch vụ điểm danh QR, thông báo, thẻ hội viên, và chatbot. | Coder | [REQ-012],[REQ-013],[REQ-014],[REQ-015],[REQ-016],[REQ-017],[REQ-018],[REQ-019],[REQ-020],[REQ-021],[REQ-022],[REQ-023],[REQ-024],[EXC-001],[EXC-002],[EXC-003],[EXC-005],[DAT-006],[DAT-007],[DAT-008],[DAT-009],[DAT-011],[NFR-001],[NFR-002],[NFR-003],[NFR-004],[NFR-005],[NFR-006],[NFR-007],[NFR-008],[NFR-009] |
| 3 | 2 | ./sources/backend/attendance-service/src/test/java/org/nlh4j/saas/membershiphub/attendance/AttendanceServiceTest.java | Viết kiểm thử cho điểm danh, thông báo, thẻ hội viên, và chatbot. | Tester | [REQ-012],[REQ-013],[REQ-014],[REQ-015],[REQ-016],[REQ-017],[REQ-018],[REQ-019],[REQ-020],[REQ-021],[REQ-022],[REQ-023],[REQ-024],[EXC-001],[EXC-002],[EXC-003],[EXC-005],[NFR-001],[NFR-006] |
| 4 | 1 | ./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java | Xây dựng báo cáo điểm danh, bảng điều khiển, và CI/CD pipeline. | Coder | [REQ-024],[REQ-025],[NFR-001],[NFR-002],[NFR-003],[NFR-004],[NFR-005],[NFR-006],[NFR-007],[NFR-008],[NFR-009] |
| 4 | 2 | ./sources/backend/report-service/src/test/java/org/nlh4j/saas/membershiphub/report/ReportServiceTest.java | Viết kiểm thử cho báo cáo, bảng điều khiển, và CI/CD. | Tester | [REQ-024],[REQ-025],[NFR-001],[NFR-006] |
| 5 | 1 | ./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java | Xây dựng chatbot, đa ngôn ngữ, SEO, và tích hợp cuối. | Coder | [REQ-019],[REQ-022],[REQ-023],[NFR-001],[NFR-002],[NFR-003],[NFR-004],[NFR-005],[NFR-006],[NFR-007],[NFR-008],[NFR-009] |
| 5 | 2 | ./sources/backend/chatbot-service/src/test/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotServiceTest.java | Viết kiểm thử cho chatbot, đa ngôn ngữ, SEO. | Tester | [REQ-019],[REQ-022],[REQ-023],[NFR-001],[NFR-006] |

## 📁 2. THỦ TỤC CÔNG NGHỆ & THƯ VĂN KHOA

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

- Java 17, Quarkus 3.0, PostgreSQL 15, Flyway 9.12, Docker 20.10, GKE 1.27, Firebase 9.0, Redis 7.0, GitHub Actions, Terraform 1.5.

## 📁 3. RÀNH GIỚI & CHẤT LƯỢNG DOANH NGHIỆP

- Đặt ranh giới làm việc: thư mục gốc dự án luôn là `.`. Tất cả đường dẫn phải bắt đầu bằng `./sources/`.
- Định dạng đường dẫn: backend logic/layer nằm trong `./sources/backend/`, frontend logic/layer trong `./sources/frontend/`, DevOps trong `./sources/infra/`, tài liệu trong `./sources/docs/`.
- Nếu dự án sử dụng Java, tất cả mã nguồn phải nằm trong gói `org.nlh4j.saas.membershiphub`.
- Đối với các bộ kiểm thử, đường dẫn phải theo định dạng `<source_component>;<test_suite_file>`. Ví dụ: `./sources/backend/user-service/src/main/java/...;./sources/backend/user-service/src/test/java/...`.
- Các thẻ đánh dấu ẩn như `<!--START_...-->` và `<!--END_...-->` phải được giữ nguyên. Các thẻ này không được dịch hoặc thay đổi.