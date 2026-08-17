# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260817145217 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/17 14:52:17 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & CƠ CẤU KIẾN TRÚC CỐT LÕI

### ⚙️ 1.1. CƠ CẤU HỆ THỐNG CỐT LÕI & CƠ CẤU KIẾN TRÚC CỐT LÕI
- Hệ thống được xây dựng theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, khóa học, và điểm danh.
- Sử dụng mô hình Event-Driven Architecture (EDA) cho các tính năng như điểm danh và thông báo.
- Áp dụng CQRS pattern để tách biệt các thao tác đọc và ghi, tối ưu hóa hiệu suất.
- Sử dụng mô hình Reactive để xử lý các luồng dữ liệu thời gian thực như điểm danh và thông báo.
- Triển khai cơ chế idempotency cho các thao tác điểm danh để đảm bảo tính nhất quán dữ liệu.
- Sử dụng cơ chế caching để tối ưu hóa hiệu suất cho các truy vấn thường xuyên.
- Triển khai cơ chế retry cho các thao tác không thành công để đảm bảo tính đáng tin cậy của hệ thống.
- Sử dụng cơ chế queue để xử lý các tác vụ bất đồng bộ như gửi thông báo và xử lý điểm danh.
- Triển khai cơ chế logging và monitoring để theo dõi hiệu suất và phát hiện lỗi.

### 🌊 1.2. LUỒNG DỮ LIỆU DOANH NGHIỆP & CƠ SỞ HỆ THỐNG CỐT LÕI
- Hệ thống sử dụng Kafka để xử lý các sự kiện như điểm danh và thông báo.
- Sử dụng Redis để caching các truy vấn thường xuyên.
- Triển khai cơ chế retry cho các thao tác không thành công.
- Sử dụng cơ chế queue để xử lý các tác vụ bất đồng bộ.
- Triển khai cơ chế logging và monitoring để theo dõi hiệu suất và phát hiện lỗi.

## 📁 2. PHỤ THUỘC CÔNG NGHỆ & CƠ SỞ HỆ THỐNG
- **Backend Infrastructure Core Stack:** Quarkus 3.8.2, Hibernate ORM 6.4.4, PostgreSQL 16.2, Kafka 3.7.0, Redis 7.2.4, Keycloak 23.0.6
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14.1.0, React 18.2.0, Tailwind CSS 3.4.1, Firebase 10.8.0, React Native 0.73.2

## 📁 3. QUY TẮC TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
- Triển khai cơ chế RBAC để quản lý quyền truy cập của người dùng.
- Sử dụng JWT để xác thực và ủy quyền.
- Triển khai cơ chế logging và monitoring để theo dõi hiệu suất và phát hiện lỗi.
- Sử dụng cơ chế caching để tối ưu hóa hiệu suất cho các truy vấn thường xuyên.
- Triển khai cơ chế retry cho các thao tác không thành công để đảm bảo tính đáng tin cậy của hệ thống.
- Sử dụng cơ chế queue để xử lý các tác vụ bất đồng bộ như gửi thông báo và xử lý điểm danh.
- Triển khai cơ chế backup và khôi phục dữ liệu để đảm bảo tính sẵn sàng của hệ thống.
- Sử dụng cơ chế mã hóa dữ liệu để đảm bảo tính bảo mật của hệ thống.
- Triển khai cơ chế kiểm tra và xác thực đầu vào để ngăn chặn các cuộc tấn công như SQL injection và XSS.
- Sử dụng cơ chế kiểm tra và xác thực đầu vào để ngăn chặn các cuộc tấn công như SQL injection và XSS.

### 🔑 3.1. Bảo mật & Tuân thủ
- Triển khai cơ chế RBAC để quản lý quyền truy cập của người dùng.
- Sử dụng JWT để xác thực và ủy quyền.
- Triển khai cơ chế logging và monitoring để theo dõi hiệu suất và phát hiện lỗi.
- Sử dụng cơ chế caching để tối ưu hóa hiệu suất cho các truy vấn thường xuyên.
- Triển khai cơ chế retry cho các thao tác không thành công để đảm bảo tính đáng tin cậy của hệ thống.
- Sử dụng cơ chế queue để xử lý các tác vụ bất đồng bộ như gửi thông báo và xử lý điểm danh.
- Triển khai cơ chế backup và khôi phục dữ liệu để đảm bảo tính sẵn sàng của hệ thống.
- Sử dụng cơ chế mã hóa dữ liệu để đảm bảo tính bảo mật của hệ thống.
- Triển khai cơ chế kiểm tra và xác thực đầu vào để ngăn chặn các cuộc tấn công như SQL injection và XSS.

### 🌐 3.2. Infrastructure & Performance Guardrails
- Triển khai cơ chế RBAC để quản lý quyền truy cập của người dùng.
- Sử dụng JWT để xác thực và ủy quyền.
- Triển khai cơ chế logging và monitoring để theo dõi hiệu suất và phát hiện lỗi.
- Sử dụng cơ chế caching để tối ưu hóa hiệu suất cho các truy vấn thường xuyên.
- Triển khai cơ chế retry cho các thao tác không thành công để đảm bảo tính đáng tin cậy của hệ thống.
- Sử dụng cơ chế queue để xử lý các tác vụ bất đồng bộ như gửi thông báo và xử lý điểm danh.
- Triển khai cơ chế backup và khôi phục dữ liệu để đảm bảo tính sẵn sàng của hệ thống.
- Sử dụng cơ chế mã hóa dữ liệu để đảm bảo tính bảo mật của hệ thống.
- Triển khai cơ chế kiểm tra và xác thực đầu vào để ngăn chặn các cuộc tấn công như SQL injection và XSS.

### 🥞 3.3. ARCHITECTURAL STACK MATRIX
```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 🏁 4. TỔNG QUAN KIẾN TRÚC HỆ THỐNG ĐA PHASE

### 📦 4.1. LỄ TỔNG HỢP KIẾN TRÚC SẢN PHẨM

<!--START_BACKLOG_SYNOPSIS_GRID-->

### [MA TRẬN TÍNH TOÁN HỆ THỐNG]
> - **Tổng [REQ] Tags:** 25 Tags
> - **Tổng [EXC] Tags:** 5 Tags
> - **Tổng [ARC] Tags:** 9 Tags
> - **Tổng [DAT] Tags:** 10 Tags
> - **Tổng [NFR] Tags:** 9 Tags
> - ➡️ **Tổng SRS Tags:** 58 Tags

| STT | Công việc | Mục đích kỹ thuật / Tóm tắt giao hàng | Loại | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Đăng ký người dùng | Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu, tích hợp đăng nhập qua Firebase, Google, Facebook | Application Code | [REQ-001] [REQ-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 2 | Quản lý vai trò người dùng | Xây dựng chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student) | Application Code | [REQ-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 3 | Quản lý trung tâm | Xây dựng chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm | Application Code | [REQ-004] [REQ-005] [REQ-006] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 4 | Quản lý khóa học | Xây dựng chức năng xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học | Application Code | [REQ-007] [REQ-008] [REQ-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 5 | Đăng ký khóa học cho học viên | Xây dựng chức năng xem danh sách khóa học, đăng ký khóa học cho học viên | Application Code | [REQ-010] [REQ-011] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 6 | Quản lý điểm danh | Xây dựng chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh | Application Code | [REQ-012] [REQ-013] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 7 | Quản lý thẻ thành viên | Xây dựng chức năng xem thông tin thẻ thành viên, gia hạn thẻ thành viên | Application Code | [REQ-014] [REQ-015] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 8 | Quản lý thông báo | Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm | Application Code | [REQ-016] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 9 | Quản lý khuyến mãi | Xây dựng chức năng tạo, sửa, xóa khuyến mãi | Application Code | [REQ-017] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 10 | Quản lý thông báo | Xây dựng chức năng tạo, sửa, xóa thông báo | Application Code | [REQ-018] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 11 | Tích hợp chatbot AI | Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp | Application Code | [REQ-019] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 12 | Tính năng ứng dụng di động | Xây dựng giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.) | Application Code | [REQ-020] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 13 | Thông báo đẩy trên di động | Xây dựng chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động | Application Code | [REQ-021] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 14 | Đa ngôn ngữ và SEO | Xây dựng chức năng phát hiện ngôn ngữ mặc định, hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha) | Application Code | [REQ-022] [REQ-023] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 15 | Báo cáo và phân tích | Xây dựng chức năng tạo báo cáo điểm danh hàng ngày, bảng điều khiển tổng quan cho quản trị viên trung tâm | Application Code | [REQ-024] [REQ-025] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 16 | Xử lý ngoại lệ | Xây dựng chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố | Application Code | [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 17 | Cơ sở dữ liệu và xác thực mã thông báo | Xây dựng cơ sở dữ liệu và xác thực mã thông báo cho hệ thống | Application Code | [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 18 | Cơ sở hạ tầng DevOps | Xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes | DevOps Infrastructure | [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 19 | Tài liệu kiến trúc doanh nghiệp | Xây dựng tài liệu kiến trúc doanh nghiệp bao gồm các bản thiết kế hệ thống, sơ đồ cơ sở dữ liệu, tài liệu hướng dẫn hoạt động và hợp đồng API | Enterprise Documentation | [DAT-ALL (1 to 10)] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| **TÓM TẮT** | **Tổng số Tag đã bao phủ:** 58 | **Tổng số công việc:** 19 | **Trạng thái:** Đã xác minh | **Độ bao phủ:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

### 🔭 4.2. MẬT MA TRẬN PHÂN PHỐI PHASE

<!--START_PHASE_SYNOPSIS_GRID-->

### [MA TRẬN TÍNH TOÁN PHÂN PHỐI]
> - **Tổng số công việc Backlog:** 19 Tasks
> - **Tổng số Tags Backlog:** 58 Tags
> - **Tổng số công việc đã phân phối:** 19 Tasks
> - **Tổng số Tags đã phân phối:** 58 Tags

| Phase | Dải ngày | ID công việc được bao phủ | Thành phần kiến trúc / Đường dẫn module | Tóm tắt giao hàng kỹ thuật | Đặc vụ được chỉ định | Tags được nhắm mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 2 | Công việc 1, Công việc 2 | ./sources/backend/auth/, ./sources/backend/user/ | Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu, tích hợp đăng nhập qua Firebase, Google, Facebook. Xây dựng chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student) | Coder, Tester, Reviewer, Doc | [REQ-001] [REQ-002] [REQ-003] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 2 | Ngày 1 - 3 | Công việc 3, Công việc 4, Công việc 5 | ./sources/backend/center/, ./sources/backend/course/, ./sources/backend/enrollment/ | Xây dựng chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm. Xây dựng chức năng xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học. Xây dựng chức năng xem danh sách khóa học, đăng ký khóa học cho học viên | Coder, Tester, Reviewer, Doc | [REQ-004] [REQ-005] [REQ-006] [REQ-007] [REQ-008] [REQ-009] [REQ-010] [REQ-011] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 3 | Ngày 1 - 2 | Công việc 6, Công việc 7 | ./sources/backend/attendance/, ./sources/backend/studentcard/ | Xây dựng chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh. Xây dựng chức năng xem thông tin thẻ thành viên, gia hạn thẻ thành viên | Coder, Tester, Reviewer, Doc | [REQ-012] [REQ-013] [REQ-014] [REQ-015] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 4 | Ngày 1 - 2 | Công việc 8, Công việc 9, Công việc 10, Công việc 11 | ./sources/backend/notification/, ./sources/backend/promotion/, ./sources/backend/announcement/, ./sources/backend/chatbot/ | Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm. Xây dựng chức năng tạo, sửa, xóa khuyến mãi. Xây dựng chức năng tạo, sửa, xóa thông báo. Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp | Coder, Tester, Reviewer, Doc | [REQ-016] [REQ-017] [REQ-018] [REQ-019] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 5 | Ngày 1 - 2 | Công việc 12, Công việc 13, Công việc 14, Công việc 15, Công việc 16, Công việc 17, Công việc 18, Công việc 19 | ./sources/frontend/, ./sources/backend/report/, ./sources/backend/exception/, ./sources/backend/architecture/, ./sources/infra/ | Xây dựng giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.). Xây dựng chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động. Xây dựng chức năng phát hiện ngôn ngữ mặc định, hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha). Xây dựng chức năng tạo báo cáo điểm danh hàng ngày, bảng điều khiển tổng quan cho quản trị viên trung tâm. Xây dựng chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố. Xây dựng cơ sở dữ liệu và xác thực mã thông báo cho hệ thống. Xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes. Xây dựng tài liệu kiến trúc doanh nghiệp bao gồm các bản thiết kế hệ thống, sơ đồ cơ sở dữ liệu, tài liệu hướng dẫn hoạt động và hợp đồng API | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-020] [REQ-021] [REQ-022] [REQ-023] [REQ-024] [REQ-025] [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005] [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009] [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009] [DAT-ALL (1 to 10)] <!--REGISTERED_PHASE_ROW--> |
| **Kiểm tra** | **Xác minh phân phối Backlog chính** | **Tổng số Phases:** 5 | **Tổng số Tags Backlog:** 58 | **Tổng số Tags đã phân phối:** 58 | **Tổng số công việc đã phân phối:** 19 | **Trạng thái & Tuân thủ:** Đã xác minh (100%) |

<!--END_PHASE_SYNOPSIS_GRID-->

## 🔬 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1 - Quản lý người dùng và vai trò

- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu, tích hợp đăng nhập qua Firebase, Google, Facebook. Xây dựng chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).

- **Ma trận bản đồ thư mục vật lý mục tiêu:** Tạo danh sách kiểm tra kỹ thuật chi tiết liệt kê 100% các tệp vật lý riêng lẻ, đường dẫn tương đối dưới `./sources/` được tạo, tái cấu trúc hoặc xử lý trong phạm vi giai đoạn này. Mỗi dòng mục được tạo ra phải đại diện cho một thực thể tệp cụ thể kết thúc với phần mở rộng tệp cấu trúc rõ ràng, với các TagID theo dõi tương ứng được đính kèm inline.

- **Chuyên gia cơ sở dữ liệu DDL SQL:** Cung cấp các câu lệnh di chuyển DDL SQL đầy đủ, hoàn chỉnh và hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG được dịch).

- **Hợp đồng định tuyến API và sự kiện:** Tài liệu các hợp đồng kỹ thuật đầy đủ (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ tải JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG được dịch).

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh vào Tiếng Việt.

#### 📅 Nhật ký phân phối nhiệm vụ theo ngày của giai đoạn (Giai đoạn 1)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-001]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/auth/src/main/java/com/hub/AuthService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu. Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng đăng ký người dùng

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-001]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/auth/src/main/java/com/hub/AuthService.java;./sources/backend/auth/src/test/java/com/hub/AuthTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đăng ký người dùng với xác thực email và mật khẩu.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng đăng ký người dùng

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-001]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/auth.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đăng ký người dùng với xác thực email và mật khẩu.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng đăng nhập qua Firebase, Google, Facebook

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-002]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/auth/src/main/java/com/hub/SocialAuthService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đăng nhập qua Firebase, Google, Facebook.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng đăng nhập qua Firebase, Google, Facebook

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-002]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/auth/src/main/java/com/hub/SocialAuthService.java;./sources/backend/auth/src/test/java/com/hub/SocialAuthTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đăng nhập qua Firebase, Google, Facebook.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng đăng nhập qua Firebase, Google, Facebook

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-002]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/auth.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đăng nhập qua Firebase, Google, Facebook.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Xây dựng chức năng gán và thay đổi vai trò người dùng

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-003]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/user/src/main/java/com/hub/UserRoleService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Viết kiểm thử cho chức năng gán và thay đổi vai trò người dùng

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-003]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/user/src/main/java/com/hub/UserRoleService.java;./sources/backend/user/src/test/java/com/hub/UserRoleTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 9: Tài liệu chức năng gán và thay đổi vai trò người dùng

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-003]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/user.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Xây dựng chức năng gán và thay đổi vai trò người dùng

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng gán và thay đổi vai trò người dùng

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-003]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/user/src/main/java/com/hub/UserRoleService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng gán và thay đổi vai trò người dùng

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-003]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/user/src/main/java/com/hub/UserRoleService.java;./sources/backend/user/src/test/java/com/hub/UserRoleTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng gán và thay đổi vai trò người dùng

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-003]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/user.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gán và thay đổi vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

### 📈 Giai đoạn 2 - Quản lý trung tâm và khóa học

- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Xây dựng chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm. Xây dựng chức năng xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học. Xây dựng chức năng xem danh sách khóa học, đăng ký khóa học cho học viên

- **Ma trận bản đồ thư mục vật lý mục tiêu:** Tạo danh sách kiểm tra kỹ thuật toàn diện, chi tiết về tất cả các đường dẫn tệp vật lý riêng lẻ nằm dưới `./sources/` được tạo, tái cấu trúc hoặc xử lý trong phạm vi giai đoạn này. Mỗi dòng mục được tạo ra phải đại diện cho một thực thể tệp cụ thể kết thúc bằng phần mở rộng tệp cấu trúc rõ ràng, với các TagID theo dõi được đính kèm trực tiếp.

    *   *Giới hạn tài liệu:* Bất kỳ dòng nào đại diện cho một tài liệu quy định doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bản thiết kế kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.

- **Chuyên gia công việc con:** [Coder]

- **TagID mục tiêu:** [REQ-004] [REQ-005] [REQ-006] [REQ-007] [REQ-008] [REQ-009] [REQ-010] [REQ-011]

- **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/center/, ./sources/backend/course/, ./sources/backend/enrollment/

- **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm. Xây dựng chức năng xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học. Xây dựng chức năng xem danh sách khóa học, đăng ký khóa học cho học viên

#### 📅 Nhật ký phân phối nhiệm vụ theo ngày của giai đoạn (Giai đoạn 2)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Xây dựng chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng xem danh sách trung tâm

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-004]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/center/src/main/java/com/hub/CenterService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem danh sách trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng xem danh sách trung tâm

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-004]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/center/src/main/java/com/hub/CenterService.java;./sources/backend/center/src/test/java/com/hub/CenterTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem danh sách trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng xem danh sách trung tâm

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-004]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/center.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem danh sách trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng thêm, sửa, xóa trung tâm

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-005]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/center/src/main/java/com/hub/CenterService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng thêm, sửa, xóa trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng thêm, sửa, xóa trung tâm

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-005]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/center/src/main/java/com/hub/CenterService.java;./sources/backend/center/src/test/java/com/hub/CenterTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng thêm, sửa, xóa trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng thêm, sửa, xóa trung tâm

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-005]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/center.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng thêm, sửa, xóa trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Xây dựng chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-006]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/center/src/main/java/com/hub/CenterAdminService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Viết kiểm thử cho chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-006]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/center/src/main/java/com/hub/CenterAdminService.java;./sources/backend/center/src/test/java/com/hub/CenterAdminTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 9: Tài liệu chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-006]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/center.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể.

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 2: Xây dựng chức năng xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng xem danh sách khóa học

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-007]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/course/src/main/java/com/hub/CourseService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem danh sách khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng xem danh sách khóa học

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-007]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/course/src/main/java/com/hub/CourseService.java;./sources/backend/course/src/test/java/com/hub/CourseTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem danh sách khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng xem danh sách khóa học

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-007]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/course.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem danh sách khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng thêm, sửa, xóa khóa học

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-008]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/course/src/main/java/com/hub/CourseService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng thêm, sửa, xóa khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng thêm, sửa, xóa khóa học

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-008]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/course/src/main/java/com/hub/CourseService.java;./sources/backend/course/src/test/java/com/hub/CourseTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng thêm, sửa, xóa khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng thêm, sửa, xóa khóa học

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-008]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/course.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng thêm, sửa, xóa khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Xây dựng chức năng gán giáo viên cho khóa học

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/course/src/main/java/com/hub/CourseTeacherService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gán giáo viên cho khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Viết kiểm thử cho chức năng gán giáo viên cho khóa học

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/course/src/main/java/com/hub/CourseTeacherService.java;./sources/backend/course/src/test/java/com/hub/CourseTeacherTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gán giáo viên cho khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 9: Tài liệu chức năng gán giáo viên cho khóa học

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/course.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gán giáo viên cho khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 3: Xây dựng chức năng xem danh sách khóa học, đăng ký khóa học cho học viên

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng xem danh sách khóa học

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-010]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/enrollment/src/main/java/com/hub/EnrollmentService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem danh sách khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng xem danh sách khóa học

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-010]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/enrollment/src/main/java/com/hub/EnrollmentService.java;./sources/backend/enrollment/src/test/java/com/hub/EnrollmentTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem danh sách khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng xem danh sách khóa học

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-010]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/enrollment.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem danh sách khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng đăng ký khóa học cho học viên

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-011]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/enrollment/src/main/java/com/hub/EnrollmentService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đăng ký khóa học cho học viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng đăng ký khóa học cho học viên

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-011]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/enrollment/src/main/java/com/hub/EnrollmentService.java;./sources/backend/enrollment/src/test/java/com/hub/EnrollmentTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đăng ký khóa học cho học viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng đăng ký khóa học cho học viên

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-011]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/enrollment.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đăng ký khóa học cho học viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

### 📈 Giai đoạn 3 - Quản lý điểm danh và thẻ thành viên

- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Xây dựng chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh. Xây dựng chức năng xem thông tin thẻ thành viên, gia hạn thẻ thành viên

- **Ma trận bản đồ thư mục vật lý mục tiêu:** Tạo danh sách kỹ thuật chi tiết, toàn diện về tất cả các đường dẫn tệp vật lý riêng lẻ nằm dưới `./sources/` được tạo, tái cấu trúc hoặc xử lý trong phạm vi giai đoạn này. Mỗi dòng mục đã tạo phải đại diện cho một thực thể tệp cụ thể kết thúc bằng phần mở rộng tệp rõ ràng, với các TagID theo dõi được đính kèm trực tiếp.
    *   *Giới hạn biên giới tài liệu:* Bất kỳ dòng nào đại diện cho một tài liệu quy định doanh nghiệp, bản thiết kế tham khảo, bản đồ ánh xạ cơ sở dữ liệu quan hệ hoặc bản thiết kế kiến trúc phải nằm nghiêm ngặt dưới thư mục gốc thống nhất: `./sources/docs/`.

- **Chuyên gia cơ sở dữ liệu DDL SQL Chỉ định [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL đầy đủ, hoàn chỉnh và hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu topology dự án không có cơ sở dữ liệu hoặc lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).

- **Hợp đồng định tuyến API và sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu các hợp đồng kỹ thuật đầy đủ (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ tải JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG ĐƯỢC dịch).

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh vào Vietnamese.

#### 📅 Nhật ký phân phối nhiệm vụ hàng ngày theo chuyên gia con (Giai đoạn 3)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Xây dựng chức năng quét mã QR để điểm danh

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng quét mã QR để điểm danh

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-012]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/attendance/src/main/java/com/hub/AttendanceService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng quét mã QR để điểm danh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng quét mã QR để điểm danh

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-012]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/attendance/src/main/java/com/hub/AttendanceService.java;./sources/backend/attendance/src/test/java/com/hub/AttendanceTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng quét mã QR để điểm danh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng quét mã QR để điểm danh

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-012]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/attendance.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng quét mã QR để điểm danh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng đảm bảo tính idempotency cho điểm danh

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-013]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/attendance/src/main/java/com/hub/AttendanceService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đảm bảo tính idempotency cho điểm danh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng đảm bảo tính idempotency cho điểm danh

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-013]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/attendance/src/main/java/com/hub/AttendanceService.java;./sources/backend/attendance/src/test/java/com/hub/AttendanceTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đảm bảo tính idempotency cho điểm danh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng đảm bảo tính idempotency cho điểm danh

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-013]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/attendance.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đảm bảo tính idempotency cho điểm danh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Xây dựng chức năng xem thông tin thẻ thành viên, gia hạn thẻ thành viên

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng xem thông tin thẻ thành viên

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-014]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/studentcard/src/main/java/com/hub/StudentCardService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem thông tin thẻ thành viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng xem thông tin thẻ thành viên

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-014]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/studentcard/src/main/java/com/hub/StudentCardService.java;./sources/backend/studentcard/src/test/java/com/hub/StudentCardTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem thông tin thẻ thành viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng xem thông tin thẻ thành viên

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-014]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/studentcard.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem thông tin thẻ thành viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng gia hạn thẻ thành viên

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-015]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/studentcard/src/main/java/com/hub/StudentCardService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gia hạn thẻ thành viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng gia hạn thẻ thành viên

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-015]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/studentcard/src/main/java/com/hub/StudentCardService.java;./sources/backend/studentcard/src/test/java/com/hub/StudentCardTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gia hạn thẻ thành viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng gia hạn thẻ thành viên

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-015]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/studentcard.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gia hạn thẻ thành viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

### 📈 Giai đoạn 4 - Quản lý thông báo, khuyến mãi, thông báo và tích hợp chatbot AI

- **Mục tiêu chính của giai đoạn & Mục đích:** Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm. Xây dựng chức năng tạo, sửa, xóa khuyến mãi. Xây dựng chức năng tạo, sửa, xóa thông báo. Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp

- **Thư mục vật lý mục tiêu:** Generate an exhaustive, granular engineering checklist mapping out 100% of all discrete, individual physical relative file paths (NOT folders or directories) underneath `./sources/` that are actively created, refactored, or processed within this phase scope. Every single generated line item MUST represent a concrete file entity ending with its explicit structural file extension, with its matching traceability Tag IDs appended inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.

- **Chuyên gia cơ sở dữ liệu DDL SQL:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).

```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(50),
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE
);

CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(30) UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);

CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
```

- **Hợp đồng định tuyến API và sự kiện:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).

```json
{
  "endpoints": [
    {
      "path": "/api/notifications",
      "method": "POST",
      "request": {
        "user_id": "UUID",
        "group_zalo": "string",
        "message": "string"
      },
      "response": {
        "notification_id": "UUID",
        "status": "string"
      }
    },
    {
      "path": "/api/promotions",
      "method": "POST",
      "request": {
        "code": "string",
        "discount_percent": "integer",
        "start_date": "date",
        "end_date": "date",
        "description": "string"
      },
      "response": {
        "promo_id": "UUID",
        "status": "string"
      }
    },
    {
      "path": "/api/announcements",
      "method": "POST",
      "request": {
        "title": "string",
        "content": "string",
        "start_date": "date",
        "end_date": "date"
      },
      "response": {
        "announcement_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```

- **Bộ xử lý ngoại lệ giai đoạn:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into Vietnamese.

#### 📅 Nhật ký phân phối nhiệm vụ hàng ngày theo chuyên gia (Giai đoạn 4)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-016]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/notification/src/main/java/com/hub/NotificationService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-016]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/notification/src/main/java/com/hub/NotificationService.java;./sources/backend/notification/src/test/java/com/hub/NotificationTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-016]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/notification.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng tạo, sửa, xóa khuyến mãi

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-017]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/promotion/src/main/java/com/hub/PromotionService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo, sửa, xóa khuyến mãi.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng tạo, sửa, xóa khuyến mãi

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-017]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/promotion/src/main/java/com/hub/PromotionService.java;./sources/backend/promotion/src/test/java/com/hub/PromotionTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo, sửa, xóa khuyến mãi.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng tạo, sửa, xóa khuyến mãi

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-017]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/promotion.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo, sửa, xóa khuyến mãi.

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 2: Xây dựng chức năng tạo, sửa, xóa thông báo và tích hợp chatbot AI

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng tạo, sửa, xóa thông báo

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-018]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/announcement/src/main/java/com/hub/AnnouncementService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo, sửa, xóa thông báo.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng tạo, sửa, xóa thông báo

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-018]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/announcement/src/main/java/com/hub/AnnouncementService.java;./sources/backend/announcement/src/test/java/com/hub/AnnouncementTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo, sửa, xóa thông báo.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng tạo, sửa, xóa thông báo

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-018]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/announcement.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo, sửa, xóa thông báo.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-019]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/chatbot/src/main/java/com/hub/ChatbotService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-019]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/chatbot/src/main/java/com/hub/ChatbotService.java;./sources/backend/chatbot/src/test/java/com/hub/ChatbotTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-019]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/chatbot.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

### 📈 Giai đoạn 5 - Tích hợp các tính năng ứng dụng di động và cơ sở hạ tầng DevOps

- **Mục tiêu chính của giai đoạn & Mục đích:** Tích hợp các tính năng ứng dụng di động bao gồm giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.), gửi thông báo đẩy cho người dùng trên thiết bị di động, phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha). Ngoài ra, xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

- **Ma trận bản đồ đường dẫn vật lý mục tiêu:** Tạo ra một danh sách kỹ thuật chi tiết về tất cả các tệp vật lý riêng lẻ nằm dưới `./sources/` được tạo, tái cấu trúc hoặc xử lý trong phạm vi giai đoạn này. Mỗi dòng mục lục phải đại diện cho một thực thể tệp cụ thể kết thúc bằng phần mở rộng tệp rõ ràng, với các TagID theo dõi được đính kèm trực tiếp.
    * *Giới hạn tài liệu:* Bất kỳ dòng nào đại diện cho một tài liệu quy trình doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bản thiết kế kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.

- **Chuyên gia DevOps:** Xây dựng các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

- **Chuyên gia GCP:** Thiết lập cơ sở hạ tầng đám mây bao gồm các dịch vụ VPC, IAM, Storage và các dịch vụ đám mây khác.

- **Chuyên gia GKE:** Thiết lập và quản lý cụm Kubernetes bao gồm các biểu mẫu triển khai, dịch vụ và cấu hình quy mô.

#### 📅 Nhật ký phân phối nhiệm vụ hàng ngày theo chuyên gia (Giai đoạn 5)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Tích hợp các tính năng ứng dụng di động và cơ sở hạ tầng DevOps

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng giao diện người dùng phù hợp với vai trò của người dùng

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-020]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/frontend/src/components/UserDashboard.js

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho giao diện người dùng phù hợp với vai trò của người dùng

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-020]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/frontend/src/components/UserDashboard.js;./sources/frontend/src/tests/UserDashboard.test.js

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu giao diện người dùng phù hợp với vai trò của người dùng

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-020]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/frontend.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-021]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/notification/src/main/java/com/hub/PushNotificationService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-021]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/notification/src/main/java/com/hub/PushNotificationService.java;./sources/backend/notification/src/test/java/com/hub/PushNotificationTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-021]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/notification.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Xây dựng chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-022] [REQ-023]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/frontend/src/utils/LocaleDetector.js

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Viết kiểm thử cho chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-022] [REQ-023]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/frontend/src/utils/LocaleDetector.js;./sources/frontend/src/tests/LocaleDetector.test.js

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 9: Tài liệu chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-022] [REQ-023]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/frontend.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 10: Xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes

* **Chuyên gia công việc con:** [Docker] [GCP] [GKE]

* **TagID mục tiêu:** [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/infra/docker/Dockerfile;./sources/infra/terraform/main.tf;./sources/infra/k8s/deployment.yaml

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 11: Viết kiểm thử cho cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009]

* **Thành phần mục tiêu (đường dẫn tệp):** INTEGRATION_SCOPE;./sources/infra/tests/integration_test.go

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 12: Tài liệu cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/infra.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Xây dựng chức năng tạo báo cáo điểm danh hàng ngày và bảng điều khiển tổng quan cho quản trị viên trung tâm

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Xây dựng chức năng tạo báo cáo điểm danh hàng ngày

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-024]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/report/src/main/java/com/hub/AttendanceReportService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo báo cáo điểm danh hàng ngày.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Viết kiểm thử cho chức năng tạo báo cáo điểm danh hàng ngày

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-024]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/report/src/main/java/com/hub/AttendanceReportService.java;./sources/backend/report/src/test/java/com/hub/AttendanceReportTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo báo cáo điểm danh hàng ngày.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Tài liệu chức năng tạo báo cáo điểm danh hàng ngày

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-024]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/report.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo báo cáo điểm danh hàng ngày.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Xây dựng bảng điều khiển tổng quan cho quản trị viên trung tâm

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [REQ-025]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/report/src/main/java/com/hub/DashboardService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng bảng điều khiển tổng quan cho quản trị viên trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Viết kiểm thử cho bảng điều khiển tổng quan cho quản trị viên trung tâm

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [REQ-025]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/report/src/main/java/com/hub/DashboardService.java;./sources/backend/report/src/test/java/com/hub/DashboardTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho bảng điều khiển tổng quan cho quản trị viên trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Tài liệu bảng điều khiển tổng quan cho quản trị viên trung tâm

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [REQ-025]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/report.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu bảng điều khiển tổng quan cho quản trị viên trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Xây dựng chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/exception/src/main/java/com/hub/ExceptionHandler.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Viết kiểm thử cho chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/exception/src/main/java/com/hub/ExceptionHandler.java;./sources/backend/exception/src/test/java/com/hub/ExceptionHandlerTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 9: Tài liệu chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/exception.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 10: Xây dựng cơ sở dữ liệu và xác thực mã thông báo cho hệ thống

* **Chuyên gia công việc con:** [Coder]

* **TagID mục tiêu:** [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/architecture/src/main/java/com/hub/DatabaseService.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng cơ sở dữ liệu và xác thực mã thông báo cho hệ thống.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 11: Viết kiểm thử cho cơ sở dữ liệu và xác thực mã thông báo cho hệ thống

* **Chuyên gia công việc con:** [Tester]

* **TagID mục tiêu:** [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/backend/architecture/src/main/java/com/hub/DatabaseService.java;./sources/backend/architecture/src/test/java/com/hub/DatabaseTest.java

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho cơ sở dữ liệu và xác thực mã thông báo cho hệ thống.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 12: Tài liệu cơ sở dữ liệu và xác thực mã thông báo cho hệ thống

* **Chuyên gia công việc con:** [Doc]

* **TagID mục tiêu:** [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009]

* **Thành phần mục tiêu (đường dẫn tệp):** ./sources/docs/architecture.md

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu cơ sở dữ liệu và xác thực mã thông báo cho hệ thống.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🕵️ BÁO CÁO KIỂM TRA TỰ ĐỘNG KIẾN TRÚC CỦA HỆ THỐNG:

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=2
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=19
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=48
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

## ☣️ 6. MÃ BẢO MẬT VÀ ĐIỀU KHIỂN TIÊU THỤ ĐẦU VÀO NHIỆT ĐỚI [NFR-XXX]
### 1. ĐIỀU KHIỂN TIÊU THỤ ĐẦU VÀO NHIỆT ĐỚI ĐỐI VỚI SQL (SQLi) (Chi tiết về các câu lệnh chuẩn bị, tham số truy vấn vị trí và danh sách trắng sắp xếp động thông qua Hibernate ORM).
- **Mã Tag:** [NFR-003]
- **Mô tả:** Đảm bảo rằng tất cả các truy vấn SQL được thực hiện thông qua các câu lệnh chuẩn bị với tham số vị trí. Sử dụng Hibernate ORM để tự động hóa việc sắp xếp đầu vào và tránh các cuộc tấn công tiêm SQL.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```java
  @Repository
  public class UserRepository {
      @PersistenceContext
      private EntityManager entityManager;

      public User findByEmail(String email) {
          String query = "SELECT u FROM User u WHERE u.email = :email";
          TypedQuery<User> typedQuery = entityManager.createQuery(query, User.class);
          typedQuery.setParameter("email", email);
          return typedQuery.getSingleResult();
      }
  }
  ```

### 2. ĐIỀU KHIỂN TIÊU THỤ ĐẦU VÀO NHIỆT ĐỚI ĐỐI VỚI XSS & CSP (Chi tiết về tự động hóa sàng lọc ngữ cảnh, tự động thoát JSX và chèn động các tiêu đề CSP HTTP nghiêm ngặt vào Cổng vào).
- **Mã Tag:** [NFR-003]
- **Mô tả:** Áp dụng các cơ chế tự động hóa để sàng lọc và thoát đầu vào từ các cuộc tấn công XSS. Đảm bảo rằng tất cả các đầu ra JSX được thoát tự động và các tiêu đề CSP HTTP nghiêm ngặt được chèn vào Cổng vào.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```java
  @RestController
  public class UserController {
      @GetMapping("/user")
      public ResponseEntity<String> getUser(@RequestParam String name) {
          String sanitizedName = Jsoup.clean(name, Safelist.basic());
          return ResponseEntity.ok()
              .header("Content-Security-Policy", "default-src 'self'; script-src 'self'")
              .body(sanitizedName);
      }
  }
  ```

### 3. ĐIỀU KHIỂN TIÊU THỤ ĐẦU VÀO NHIỆT ĐỚI ĐỐI VỚI CORS (Xác định rõ ràng các nguồn gốc và kiểm tra ranh giới người dùng đa người dùng).
- **Mã Tag:** [NFR-003]
- **Mô tả:** Cấu hình CORS để chỉ cho phép các nguồn gốc được xác định rõ ràng và thực hiện kiểm tra ranh giới người dùng đa người dùng để ngăn chặn các cuộc tấn công CORS.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```java
  @Configuration
  public class CorsConfig implements WebMvcConfigurer {
      @Override
      public void addCorsMappings(CorsRegistry registry) {
          registry.addMapping("/**")
              .allowedOrigins("https://trusted-domain.com")
              .allowedMethods("GET", "POST", "PUT", "DELETE");
      }
  }
  ```

### 4. ĐIỀU KHIỂN TIÊU THỤ ĐẦU VÀO NHIỆT ĐỚI ĐỐI VỚI PII (Đảm bảo rằng dữ liệu PII được che giấu tự động và các bộ sàng lọc dữ liệu được áp dụng).
- **Mã Tag:** [NFR-003]
- **Mô tả:** Áp dụng các bộ sàng lọc dữ liệu để tự động hóa việc che giấu dữ liệu PII. Sử dụng các bộ sàng lọc dữ liệu để đảm bảo rằng dữ liệu nhạy cảm không bị tiết lộ.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```java
  @JsonSerialize(using = MaskingSerializer.class)
  private String email;

  public class MaskingSerializer extends JsonSerializer<String> {
      @Override
      public void serialize(String value, JsonGenerator gen, SerializerProvider serializers) throws IOException {
          if (value != null) {
              String maskedValue = value.replaceAll("(?<=.{3}).(?=.*@)", "*");
              gen.writeString(maskedValue);
          }
      }
  }
  ```

## 📱 7. QUY TẮC TUÂN THỦ HỢP NHẤT VÀ CƠ CHẾ SEO ĐỘC QUYỀN
### 1. QUY TẮC TUÂN THỦ HỢP NHẤT ĐỐI VỚI DI ĐỘNG (Xác định rõ ràng các ràng buộc tuân thủ hợp nhất và các cơ chế đồng bộ lưu trữ gốc sử dụng `@capacitor/preferences`).
- **Mã Tag:** [NFR-007]
- **Mô tả:** Đảm bảo rằng tất cả các yêu cầu tuân thủ hợp nhất được thực hiện rõ ràng và các cơ chế đồng bộ lưu trữ gốc được sử dụng để đảm bảo tính nhất quán.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```javascript
  import { Preferences } from '@capacitor/preferences';

  async function saveData(key, value) {
      await Preferences.set({ key, value });
  }

  async function getData(key) {
      const { value } = await Preferences.get({ key });
      return value;
  }
  ```

### 2. QUY TẮC TUÂN THỦ HỢP NHẤT ĐỐI VỚI SEO (Chi tiết về các cơ chế nhận diện ngôn ngữ động và chèn thuộc tính hreflang tự động).
- **Mã Tag:** [NFR-007]
- **Mô tả:** Áp dụng các cơ chế nhận diện ngôn ngữ động để tự động hóa việc chèn thuộc tính hreflang vào các trang web.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```javascript
  function generateHreflangTags(languages) {
      return languages.map(lang => `<link rel="alternate" hreflang="${lang}" href="https://example.com/${lang}/" />`).join('
');
  }
  ```

## 🚀 8. LUỒNG ĐIỀU PHỐI TỰ ĐỘNG HÀNG NGÀY CỦA PIPELINE GIT BRANCH
### 1. ĐIỀU PHỐI TỰ ĐỘNG CỦA KHÔNG GIAN LÀM VIỆC (Chi tiết về các điều khiển phân nhánh tách biệt theo chương trình cho các cấu hình nhánh `features/development-phase-X-day-Y` trong đó X là giai đoạn và Y là ngày).
- **Mã Tag:** [NFR-006]
- **Mô tả:** Đảm bảo rằng tất cả các nhánh được tạo theo chương trình và các nhánh được đặt tên theo định dạng `features/development-phase-X-day-Y`.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```bash
  git checkout -b features/development-phase-1-day-1
  ```

### 2. CỔNG ĐIỀU PHỐI XÁC THỰC TỰ ĐỘNG (Thiết lập các quy tắc thực thi nghiêm ngặt cho biên dịch tự động, các cổng kiểm tra chất lượng SonarQube và các mục tiêu kiểm tra tự động được đặt nghiêm ngặt ở `>= 85%`).
- **Mã Tag:** [NFR-006]
- **Mô tả:** Đảm bảo rằng tất cả các quy tắc thực thi nghiêm ngặt được áp dụng và các mục tiêu kiểm tra tự động được đặt nghiêm ngặt ở `>= 85%`.
- **Hướng dẫn kỹ thuật chi tiết:**
  ```yaml
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - name: Set up JDK
          uses: actions/setup-java@v1
          with:
            java-version: '11'
        - name: Build with Maven
          run: mvn clean install
        - name: Run SonarQube
          run: mvn sonar:sonar -Dsonar.projectKey=my-project -Dsonar.host.url=http://sonarqube.example.com -Dsonar.login=${SONAR_TOKEN}
  ```

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 12, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]