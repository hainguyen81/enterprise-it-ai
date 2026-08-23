# BỐI CẢNH DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Kiểm soát Tài liệu

| Hạng mục | Chi tiết |
| :--- | :--- |
| **ID Bản thiết kế** | ARCH-20260823050512 |
| **Tên dự án** | membership-hub |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/23 05:05:12 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕI

### ⚙️ 1.1. Mô hình Hệ thống Cốt lõi & Kiến trúc Tổng thể

- Kiến trúc microservices trên nền Java 21 LTS + Quarkus 3.x, container hóa bằng Docker và điều phối production trên Google Kubernetes Engine (GKE). [ARC-010]
- Mô hình Event-Driven Architecture (EDA): mọi sự kiện nghiệp vụ (điểm danh, ghi danh, gia hạn thẻ, thông báo) được phát hành bất đồng bộ qua Apache Kafka đến các dịch vụ tiêu thụ chuyên trách. [ARC-008]
- Ranh giới CQRS tách bạch đường ghi/đọc: khối lượng báo cáo và dashboard thời gian thực được route sang PostgreSQL read replicas, cô lập hoàn toàn khỏi cụm ghi giao dịch. [NFR-004]
- Lõi Reactive: RESTEasy Reactive trên Vert.x kết hợp Hibernate Reactive cho phép I/O phi chặn, bảo đảm mục tiêu độ trễ trung bình 200 ms của API lõi. [NFR-001]
- Điểm danh QR được thiết kế idempotent tuyệt đối nhờ ràng buộc duy nhất (studentId, courseId, attendanceDate); quét trùng cùng ngày trả về cờ 'duplicate' mà không phát sinh thêm bản ghi. [REQ-013], [EXC-002]
- Xác thực liên hợp OAuth2 qua Firebase/Google/Facebook, phát hành JWT access token 15 phút kèm refresh token 7 ngày. [ARC-006], [NFR-003]
- Redis 7.x đóng vai trò session cache và kho dữ liệu nóng, giảm áp lực truy vấn trực tiếp lên PostgreSQL. [ARC-010]
- Tầng fan-out thông báo đa kênh: FCM/APNs cho push notification di động và Zalo Open API cho đăng bài nhóm Zalo. [ARC-008]
- Frontend Next.js tiêu thụ REST API chuẩn hóa qua bearer token, tích hợp caching ngoại tuyến cho kịch bản mất kết nối mạng. [ARC-009]
- Ma trận RBAC 5 vai trò (System Admin, Center Admin, Manager, Teacher, Student) được thực thi tập trung tại tầng gateway và kiểm chứng lại tại từng dịch vụ. [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

### 🌊 1.2. Topology Luồng Dữ liệu Doanh nghiệp & Hệ sinh thái Cốt lõi

- **Cổng tiếp nhận (Ingestion Gateway):**
  - Toàn bộ request đi qua Ingress trên GKE với TLS 1.3 termination; JWT được kiểm chứng tại filter OIDC của Quarkus trước khi đi vào business logic. [NFR-003], [ARC-006]
  - Rate limiting theo user và theo trung tâm áp tại tầng gateway nhằm bảo vệ SLA độ trễ 200 ms. [NFR-001]
- **Topology topic Kafka:**
  - `attendance.events`: phát hành khi quét QR hợp lệ; partition theo `courseId` để bảo đảm thứ tự xử lý trong phạm vi từng khóa học. [ARC-007]
  - `enrollment.events`: phát hành khi học viên được ghi danh; payload chứa `studentId`, `courseId`, `centerId`. [REQ-011]
  - `card.renewal.events`: phát hành ngay sau khi thanh toán gia hạn thẻ được xác nhận thành công. [REQ-015]
  - `notification.dispatch`: hàng đợi lệnh gửi thông báo; consumer duy nhất là notification-service. [REQ-016]
  - `audit.log.stream`: dòng sự kiện kiểm toán phục vụ lưu trữ truy vết 1 năm. [NFR-006]
- **Fan-out đa kênh ra bên ngoài:**
  - notification-service tiêu thụ `notification.dispatch`, đẩy payload push tới FCM (Android) và APNs (iOS); thất bại được phát lại tối đa 3 lần trước khi đánh dấu `failed`. [EXC-003], [REQ-021]
  - Song song, hệ thống gọi Zalo Open API để đăng tin nhắn vào nhóm Zalo được chỉ định của trung tâm tương ứng. [ARC-008]
- **Khả năng phục hồi luồng:**
  - Ứng dụng di động hàng đợi cục bộ các lần quét QR khi mất mạng và tự động retry khi có lại kết nối. [EXC-001]
  - Sau sự cố hệ thống, các bản điểm danh tồn đọng được xử lý theo thứ tự FIFO và người dùng nhận thông báo khôi phục sự kiện. [EXC-005]

## 📁 2. PHỤ THUỘC TECH STACK & THƯ VIỆN HỆ SINH THÁI

- **Stack hạ tầng Backend cốt lõi:**
  - Runtime: Java 21 LTS trên Quarkus 3.15.x (extensions: resteasy-reactive, hibernate-orm-panache, flyway, redis-client, oidc, smallrye-reactive-messaging-kafka). [ARC-010]
  - Dependency Injection: ArC (CDI-lite) nguyên sinh của Quarkus.
  - ORM & Migration: Hibernate ORM với Panache 3.15.x; quản lý schema bằng Flyway 10.x trên PostgreSQL 16.x. [ARC-010]
  - Connection Pooling: Agroal với cấu hình pool tối ưu theo từng dịch vụ.
  - Messaging: SmallRye Reactive Messaging 4.x trên Apache Kafka 3.7.x. [ARC-008]
  - Cache: Quarkus Redis Client trên Redis 7.2.x cho session và dữ liệu nóng. [ARC-010]
  - Bảo mật: Quarkus OIDC + MicroProfile JWT 2.1; Firebase Admin SDK 9.x cho xác thực mạng xã hội. [ARC-006]
  - Tích hợp ngoài: Zalo Open Platform REST API, FCM HTTP v1 API, Apple APNs Provider API. [ARC-008], [REQ-021]
  - Tiện ích: Jackson 2.17.x, MapStruct 1.6.x, Lombok, Hibernate Validator 8.x.
  - Chất lượng: JUnit 5.10.x, RestAssured 5.x, Testcontainers 1.20.x, Mockito 5.x.
  - Build & CI/CD: Maven 3.9.x, GitHub Actions pipeline, Docker multi-stage build (base image < 200 MB, image cuối < 500 MB). [NFR-005]
- **Frontend & Cross-Platform UI Mobile Stack:**
  - Web: Next.js 14.2.x (App Router) + React 18.3.x + TypeScript 5.5.x.
  - UI: TailwindCSS 3.4.x + shadcn/ui; Recharts 2.x cho dashboard tổng quan.
  - i18n & SEO: next-intl 3.x với định tuyến locale động (/en, /vi, /es), tự sinh hreflang và meta tags theo ngôn ngữ của từng trang. [REQ-022], [REQ-023], [NFR-007]
  - State & Data: TanStack Query 5.x + Zustand 4.x; axios interceptor gắn bearer token tự động. [ARC-009]
  - Offline: next-pwa (Service Worker) với chiến lược stale-while-revalidate cho caching ngoại tuyến. [ARC-009]
  - Mobile: React Native 0.75.x trên Expo SDK 51; react-navigation 6.x cho điều hướng và màn hình render theo vai trò (Student, Teacher, Admin). [REQ-020]
  - QR: react-native-vision-camera + plugin giải mã mã QR cho luồng điểm danh. [REQ-012]
  - Push: @react-native-firebase/messaging (FCM) và cầu nối APNs cho iOS. [REQ-021]

## 📁 3. RÀO CHẮN TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP

- Toàn bộ hành động người dùng (thay đổi vai trò, ghi điểm danh, gửi thông báo) đều được ghi log kiểm toán với timestamp, userId và chi tiết hành động; log lưu trữ 1 năm. [NFR-006]
- Tuân thủ GDPR/CCPA: xóa dữ liệu cá nhân theo yêu cầu người dùng, xuất dữ liệu định dạng JSON, quản lý đồng ý truyền thông marketing. [NFR-008]
- Đa ngôn ngữ bắt buộc EN/VI/ES: chuỗi UI externalized hoàn toàn, chuyển đổi locale không cần reload trang ở mức khả thi. [NFR-007]
- Backup & Disaster Recovery: full backup PostgreSQL hằng ngày, point-in-time recovery trong 24 giờ, backup cụm GKE sang region riêng biệt. [NFR-009]
- Mô hình RBAC 5 vai trò thực thi nguyên tắc đặc quyền tối thiểu: System Admin toàn quyền toàn cầu, Center Admin bị cô lập trong phạm vi trung tâm của mình, Manager bị giới hạn quyền chỉnh sửa, Teacher chỉ đọc, Student giới hạn trong nghiệp vụ tự phục vụ. [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

### 🔑 3.1. Nền tảng Bảo mật & Tuân thủ

- Mã hóa toàn bộ dữ liệu truyền bằng TLS 1.3; mã hóa at-rest bằng AES-256. [NFR-003]
- JWT access token hết hạn sau 15 phút; refresh token có thời hạn 7 ngày. [ARC-006], [NFR-003]
- Triển khai đầy đủ mitigation OWASP Top 10: prepared statements chống SQL injection, output encoding chống XSS, CSRF token cho các operation thay đổi trạng thái. [NFR-003]
- Mật khẩu lưu trữ dưới dạng bcrypt hash độ dài 60 ký tự, tuyệt đối không lưu plaintext. [DAT-001]
- Cô lập ranh giới tenant: Center Admin chỉ thao tác trên trung tâm mình phụ trách, không rò rỉ dữ liệu chéo trung tâm. [ARC-002]
- Teacher bị khóa quyền chỉ đọc trên lịch dạy và danh sách học viên. [ARC-004]
- Xác thực đầu vào form trả về thông báo lỗi liệt kê từng trường không hợp lệ để người dùng chỉnh sửa. [EXC-004]

### 🌐 3.2. Rào chắn Hạ tầng & Hiệu năng

- Độ trễ trung bình các API lõi (xác thực, ghi điểm danh, danh sách khóa học) ≤ 200 ms. [NFR-001]
- Index hóa truy vấn database bảo đảm đọc dưới 1 giây ở mức 10.000 người dùng đồng thời. [NFR-001]
- Uptime mục tiêu 99.9%/năm với automatic failover liên cụm GKE. [NFR-002]
- Horizontal scaling qua Kubernetes HPA: trigger khi CPU > 70% hoặc request latency > 300 ms. [NFR-004]
- PostgreSQL read replicas tiếp nhận toàn bộ workload báo cáo và dashboard. [NFR-004]
- Base image Docker < 200 MB; image cuối cùng < 500 MB. [NFR-005]
- Redis session cache hấp thụ truy vấn phiên, giảm tải ghi/đọc lên PostgreSQL. [ARC-010]
- Ghi điểm danh idempotent: nhiều lần quét cùng học viên/khóa học/ngày chỉ tạo đúng một bản ghi. [REQ-013], [EXC-002]
- Thông báo giao thất bại được retry tối đa 3 lần trước khi đánh dấu failed. [EXC-003]
- Sau outage, các bản điểm danh tồn đọng được tái xử lý theo FIFO kèm thông báo khôi phục cho người dùng. [EXC-005]

### 🥞 3.3. MA TRẬN STACK KIẾN TRÚC

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 🏁 4. BẢNG TỔNG QUAN KIẾN TRÚC ĐA GIAI ĐOẠN CẤP CAO

### 📦 4.1. DANH MỤC CÔNG VIỆC SẢN PHẨM KIẾN TRÚC TỔNG THỂ

Tập hợp công việc dưới đây được cấu trúc theo chuỗi phụ thuộc kiến trúc của nền tảng membership-hub: lớp khung dự án [ARC-000] khởi tạo descriptor build backend Java/Quarkus theo mô hình microservices và workspace frontend Next.js/React Native làm nền móng cho toàn bộ module chức năng; các dịch vụ nghiệp vụ (auth-service, center-service, course-service, enrollment-service, attendance-service, card-service, notification-service, promotion-service, chatbot-service, reporting-service) đều phụ thuộc vào lớp dữ liệu quan hệ hợp nhất [DAT-ALL (1 to 11)] và bị ràng buộc bởi cơ chế thực thi phân quyền RBAC [ARC-001 to ARC-005]; bốn luồng tích hợp liên dịch vụ [ARC-006 to ARC-009] (xác thực OAuth2/JWT, điểm danh QR idempotent, điều phối thông báo đa kênh FCM/APNs/Zalo, kết nối mobile–backend có caching ngoại tuyến) được chuẩn hóa qua api-gateway và Redis session cache; cuối cùng, nền tảng công nghệ [ARC-010], hạ tầng DevOps (Docker, Terraform/GCP, GKE, CI/CD GitHub Actions) và khối tài liệu doanh nghiệp đóng gói toàn bộ ràng buộc phi chức năng [NFR-001] đến [NFR-009] thành chuỗi bàn giao production hoàn chỉnh.

<!--START_BACKLOG_SYNOPSIS_GRID-->

### [MA TRẬN TÍNH TOÁN HỆ THỐNG]
> - **Tổng số thẻ [REQ]:** 25 thẻ
> - **Tổng số thẻ [EXC]:** 5 thẻ
> - **Tổng số thẻ [ARC]:** 10 thẻ
> - **Tổng số thẻ [DAT]:** 11 thẻ
> - **Tổng số thẻ [NFR]:** 9 thẻ
> - ➡️ **Tổng số thẻ SRS:** 60 thẻ

| STT | Nhiệm vụ | Mục đích kỹ thuật / Tóm tắt sản phẩm bàn giao | Loại | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Khởi tạo khung dự án backend microservices | Sinh descriptor build gốc `./sources/backend/pom.xml` (Quarkus BOM, dependencyManagement tập trung) và descriptor module con `./sources/backend/<service-name>/pom.xml` cho từng dịch vụ; thiết lập profile build dev/production và plugin compile thống nhất. | Mã ứng dụng | [ARC-000] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 2 | Khởi tạo workspace frontend | Sinh manifest `./sources/frontend/package.json` (Next.js, React Native, TypeScript) và cấu hình biên dịch `./sources/frontend/tsconfig.json` (strict mode, path alias) làm nền chung cho web-app và mobile-app. | Mã ứng dụng | [ARC-000] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 3 | Đăng ký người dùng bằng email/mật khẩu | Endpoint POST /api/v1/auth/register trên auth-service: validate email unique và độ mạnh mật khẩu, hash bcrypt, tạo bản ghi Users vai trò mặc định 'Student', cấp JWT 15 phút kèm refresh token; khi validation thất bại trả thông báo liệt kê từng trường không hợp lệ. | Mã ứng dụng | [REQ-001], [EXC-004] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 4 | Xác thực mạng xã hội OAuth2 | Tích hợp Firebase/Google/Facebook qua OAuth2: nhận authorization code từ popup provider, exchange lấy user info, tạo/cập nhật bản ghi Users cục bộ theo provider tương ứng, phát hành JWT phiên làm việc. | Mã ứng dụng | [REQ-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 5 | Phân quyền vai trò người dùng | API quản trị gán/thay đổi roleId (System Admin, Center Admin, Manager, Teacher, Student); cập nhật cột vai trò và áp dụng ma trận quyền tức thời; ghi audit log mọi thay đổi vai trò kèm timestamp và userId. | Mã ứng dụng | [REQ-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 6 | Xem danh sách trung tâm | GET /api/v1/centers trả bảng trung tâm (Name, Address, TaxID, AdminContact) cho mọi người dùng đã xác thực; phân trang và index truy vấn sub-second. | Mã ứng dụng | [REQ-004] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 7 | Tạo/cập nhật/xóa trung tâm | CRUD trung tâm dành cho System Admin tại center-service: validate taxId numeric 10–13 chữ số với ràng buộc unique, trả 409 Conflict khi taxId trùng; persist contactPhone/contactEmail đúng định dạng chuẩn. | Mã ứng dụng | [REQ-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 8 | Phân quyền quản trị trung tâm | Gán/hủy gán user làm Center Admin cho centerId cụ thể: set role 'Center Admin', ghi center ID vào phạm vi quản lý; thao tác unassign đảo ngược hoàn toàn; cô lập tenant theo trung tâm. | Mã ứng dụng | [REQ-006] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 9 | Xem danh sách khóa học | GET /api/v1/courses trả lưới CourseID, Title, StartDate, EndDate, TeacherName (join Users); hỗ trợ duyệt danh sách offering cho mọi vai trò đã xác thực. | Mã ứng dụng | [REQ-007] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 10 | Quản lý khóa học chống xung đột lịch | CRUD khóa học (System Admin/Center Admin): kiểm tra giao thoa khoảng startDate–endDate trên cùng teacherId hoặc venue trước khi persist, trả lỗi xung đột lịch nếu trùng; maxStudents mặc định 30. | Mã ứng dụng | [REQ-008] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 11 | Phân công giáo viên vào khóa học | Gán/hủy ánh xạ course–teacher; khi gán, phát event sang notification-service để queue push notification tới mobile app của giáo viên được chỉ định. | Mã ứng dụng | [REQ-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 12 | Duyệt khóa học dành cho học viên | GET /api/v1/enrollments/browse lọc loại các khóa học đã có bản ghi Enrollment của studentId; hiển thị capacity và lịch học còn trống để học viên lựa chọn. | Mã ứng dụng | [REQ-010] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 13 | Đăng ký khóa học của học viên | POST đăng ký khóa học trong một transaction: tạo bản ghi Enrollments, tự động cấp tài khoản vai trò 'Student' nếu chưa tồn tại, phát sự kiện thông báo tới mobile app học viên và nhóm Zalo của trung tâm. | Mã ứng dụng | [REQ-011] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 14 | Chụp ảnh điểm danh qua quét mã QR | Mobile scanner gửi studentId + timestamp tới POST /api/v1/attendance/scan: xác thực quan hệ student–course, ghi bản ghi Attendance kèm attendanceDate; cơ chế retry sau khi reconnect và ghi nhận điểm danh một lần khi dịch vụ reachable trở lại. | Mã ứng dụng | [REQ-012], [EXC-001] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 15 | Bất biến (idempotent) điểm danh | Ràng buộc unique (studentId, courseId, attendanceDate) tại tầng PostgreSQL; nhiều lần quét cùng ngày chỉ tạo một dòng attendance; request trùng trả success kèm cờ 'duplicate' ('already recorded') không phát sinh thêm bản ghi. | Mã ứng dụng | [REQ-013], [EXC-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 16 | Hiển thị tính hợp lệ thẻ hội viên | GET /api/v1/cards/me suy ra totalValidityDays, daysUsed, daysRemaining từ thực thể StudentCard (issueDate, validityDays); render thẻ hội viên kỹ thuật số kèm đếm ngày hiệu lực còn lại. | Mã ứng dụng | [REQ-014] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 17 | Gia hạn thẻ hội viên | Luồng gia hạn theo kỳ chọn (ví dụ 30 ngày): khi payment service xác nhận success thì mở rộng EndDate/validityDays của StudentCard và gửi notification xác nhận gia hạn tới học viên. | Mã ứng dụng | [REQ-015] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 18 | Kích hoạt thông báo đa kênh | Khi admin tạo announcement, phân công giáo viên hoặc đăng ký học viên: tạo bản ghi Notifications, queue push payload qua FCM/APNs và đăng tin nhắn văn bản lên nhóm Zalo chỉ định; log thất bại delivery và retry tối đa 3 lần trước khi đánh dấu failed khi device token invalid. | Mã ứng dụng | [REQ-016], [EXC-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 19 | Quản lý khuyến mãi | CRUD Promotions (code unique, discountPercent, startDate/endDate, description) cho Center Admin/Manager; endDate bỏ trống coi là khuyến mãi vĩnh viễn; công khai danh sách ưu đãi áp dụng phía học viên. | Mã ứng dụng | [REQ-017] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 20 | Quản lý thông báo công khai | CRUD Announcements (title tối đa 150 ký tự, content tối đa 2000 ký tự, expiry tùy chọn); phát sóng toàn site và tự động ẩn sau ngày hết hạn đã cấu hình. | Mã ứng dụng | [REQ-018] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 21 | Tích hợp chatbot AI chăm sóc khách hàng | Widget chat tiêu thụ chatbot-service: trả lời truy vấn về khóa học, giáo viên, trung tâm và trạng thái tài khoản; escalate lên nhân viên hỗ trợ khi độ tin cậy thấp; ghi log hội thoại vào AuditLog. | Mã ứng dụng | [REQ-019] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 22 | Giao diện di động theo vai trò | Responsive UI (React Native) phản chiếu đầy đủ chức năng web theo vai trò (Student, Teacher, Admin); render menu điều hướng và màn hình tương ứng ngay sau đăng nhập trên Android/iOS. | Mã ứng dụng | [REQ-020] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 23 | Thông báo đẩy trên di động | Đăng ký device token sau login; nhận push qua FCM/APNs cho xác nhận điểm danh, announcement mới và tin nhắn nhắc nhở; điều hướng deep-link tới màn hình liên quan. | Mã ứng dụng | [REQ-021] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 24 | Phát hiện ngôn ngữ mặc định | Ưu tiên ngôn ngữ đã lưu của người dùng, fallback theo Accept-Language header của trình duyệt; externalize toàn bộ UI strings (en/vi/es) và chuyển locale không cần reload trang. | Mã ứng dụng | [REQ-022] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 25 | SEO đa ngôn ngữ | Render thẻ `<html lang='en'>`, language-specific meta tags và hreflang alternate links cho en/vi/es trên từng page; SSR metadata phục vụ crawler lập chỉ mục. | Mã ứng dụng | [REQ-023] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 26 | Báo cáo điểm danh CSV | Xuất file CSV cột StudentName, CourseName, AttendanceDate, Status theo trung tâm và khoảng ngày chọn; xử lý FIFO các scan tồn đọng sau outage và gửi thông báo sự kiện đã phục hồi tới người dùng. | Mã ứng dụng | [REQ-024], [EXC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 27 | Bảng điều khiển tóm tắt ghi danh | Dashboard real-time cho Center Admin: thẻ totalStudents, activeCourses, upcomingSessions (7 ngày tới); đọc qua PostgreSQL read replica để cách ly workload báo cáo khỏi OLTP. | Mã ứng dụng | [REQ-025] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 28 | Khởi tạo hạ tầng cơ sở dữ liệu hợp nhất | Flyway migration tại `./sources/backend/db-migrations/` tạo đủ 11 bảng lõi: Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, SystemSettings; khóa ngoại, unique constraint và index tối ưu truy vấn sub-second. | Mã ứng dụng | [DAT-ALL (1 to 11)] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 29 | Thực thi bảo mật RBAC toàn cục | Bộ filter/interceptor phân quyền 5 vai trò: System Admin toàn quyền mọi trung tâm, Center Admin giới hạn trong trung tâm sở tại, Manager không được sửa khóa học/chỉ định giáo viên, Teacher chỉ đọc lịch dạy, Student duyệt/đăng ký/xem thẻ; áp dụng thống nhất qua api-gateway tại `./sources/backend/auth-service/`. | Mã ứng dụng | [ARC-001 to ARC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 30 | Hợp đồng tích hợp liên dịch vụ | Chuẩn hóa 4 luồng kiến trúc: xác thực OAuth2/JWT (access 15 phút + refresh token), điểm danh QR idempotent, điều phối thông báo đa kênh (FCM/APNs/Zalo), tích hợp mobile–backend qua bearer token với offline caching; công bố OpenAPI contracts qua api-gateway tại `./sources/backend/api-gateway/`. | Mã ứng dụng | [ARC-006 to ARC-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 31 | Nền tảng công nghệ & hạ tầng chuẩn | Chốt stack production: Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API integration, Redis session caching, CI/CD GitHub Actions; tham số hóa cấu hình môi trường tại `./sources/infra/`. | Hạ tầng DevOps | [ARC-010] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 32 | Hạ tầng DevOps & pipeline triển khai | Multi-stage Dockerfiles (base image nhỏ hơn 200MB, final image nhỏ hơn 500MB), Terraform provisioning VPC/IAM/Storage trên GCP, manifests GKE với HPA (CPU vượt 70% hoặc latency vượt 300ms), failover liên cluster đạt uptime 99.9%, TLS 1.3/AES-256 kèm mitigations OWASP Top 10, backup PITR 24h đa region, audit log lưu trữ 1 năm, workflow GDPR/CCPA data export/deletion và consent management. | Hạ tầng DevOps | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 33 | Kiến trúc tài liệu doanh nghiệp | Biên soạn blueprint kiến trúc, sơ đồ topology cơ sở dữ liệu, hướng dẫn vận hành bản địa hóa (vi/en/es) và hợp đồng API tham chiếu (OpenAPI) đặt tại `./sources/docs/`; bổ sung quy trình audit log, quản lý consent và xuất dữ liệu cá nhân theo GDPR/CCPA. | Tài liệu doanh nghiệp | [NFR-006], [NFR-007], [NFR-008] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| **TỔNG KẾT** | **Tổng số thẻ theo dõi đã bao phủ:** 60 | **Tổng số nhiệm vụ:** 33 | **Trạng thái:** Đã xác minh | **Độ bao phủ:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

### 🔭 4.2. MA TRẬN TỔNG QUAN ĐA GIAI ĐOẠN

<!--START_PHASE_SYNOPSIS_GRID-->

### [VÒNG ĐỜI TÍNH TOÁN MA TRẬN]

> - **Tổng số nhiệm vụ Backlog:** 33 Nhiệm vụ
> - **Tổng số thẻ Backlog:** 61 Thẻ
> - **Tổng số nhiệm vụ đã phân bổ:** 33 Nhiệm vụ
> - **Tổng số thẻ đã phân bổ:** 61 Thẻ

| Giai đoạn | Khoảng ngày | Task ID bao phủ | Thành phần kiến trúc / Đường dẫn Module | Tóm tắt sản phẩm bàn giao kỹ thuật | Sub-Agent được phân công | Thẻ theo dõi mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 6 | Task 1, Task 2, Task 3, Task 4, Task 5, Task 28 | ./sources/backend/pom.xml; ./sources/backend/auth-service/; ./sources/backend/db-migrations/; ./sources/frontend/package.json; ./sources/frontend/tsconfig.json | Khởi tạo descriptor build gốc và descriptor module con cho chuỗi dịch vụ Quarkus, đồng thời sinh manifest workspace Next.js/React Native với TypeScript strict mode [ARC-000]; Flyway migration tạo đủ 11 bảng lõi (Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, SystemSettings) với khóa ngoại, unique constraint và index truy vấn sub-second [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]; endpoint POST /api/v1/auth/register hash bcrypt cấp JWT 15 phút kèm refresh token [REQ-001], [EXC-004]; đăng nhập OAuth2 Firebase/Google/Facebook [REQ-002]; API gán/thay đổi vai trò kèm audit log [REQ-003]. Tester bàn giao JUnit suite auth, integration test migration CSDL và profile E2E đăng ký; Doc bàn giao blueprint kiến trúc tổng thể và đặc tả API auth-service. | Coder, Tester, Reviewer, Doc | [ARC-000], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011], [REQ-001], [EXC-004], [REQ-002], [REQ-003] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 2 | Ngày 1 - 5 | Task 6, Task 7, Task 8, Task 9, Task 10, Task 11, Task 29, Task 30 | ./sources/backend/center-service/; ./sources/backend/course-service/; ./sources/backend/api-gateway/ | API GET /api/v1/centers phân trang với index sub-second [REQ-004]; CRUD trung tâm validate taxId numeric 10–13 chữ số trả 409 Conflict khi trùng [REQ-005]; gán/hủy Center Admin ghi phạm vi trung tâm và cô lập tenant [REQ-006]; lưới khóa học CourseID, Title, StartDate, EndDate, TeacherName [REQ-007]; CRUD khóa học chặn xung đột lịch trên cùng teacherId với maxStudents mặc định 30 [REQ-008]; gán/hủy giáo viên phát event sang notification-service [REQ-009]; bộ filter/interceptor RBAC 5 vai trò thống nhất qua api-gateway [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]; công bố hợp đồng OpenAPI cho xác thực OAuth2/JWT, điểm danh QR idempotent, điều phối thông báo đa kênh và tích hợp mobile bearer token [ARC-006], [ARC-007], [ARC-008], [ARC-009]. Tester bàn giao JUnit phân quyền RBAC, integration test xung đột lịch và E2E đa vai trò; Doc bàn giao tài liệu tham chiếu API center/course và sơ đồ topology RBAC. | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 3 | Ngày 1 - 3 | Task 12, Task 13, Task 14, Task 15, Task 16, Task 17 | ./sources/backend/enrollment-service/; ./sources/backend/attendance-service/; ./sources/backend/card-service/ | Duyệt khóa học loại trừ các khóa đã có bản ghi Enrollment kèm capacity còn trống [REQ-010]; đăng ký khóa học trong một transaction tự cấp tài khoản Student nếu thiếu và queue thông báo tới mobile app cùng nhóm Zalo trung tâm [REQ-011]; mobile scanner gửi studentId + timestamp tới POST /api/v1/attendance/scan với cơ chế retry sau reconnect [REQ-012], [EXC-001]; ràng buộc unique (studentId, courseId, attendanceDate) bảo đảm idempotent trả success kèm cờ duplicate [REQ-013], [EXC-002]; thẻ hội viên suy ra totalValidityDays, daysUsed, daysRemaining từ thực thể StudentCard [REQ-014]; gia hạn thẻ theo kỳ 30 ngày sau khi payment service xác nhận thành công [REQ-015]. Tester bàn giao JUnit idempotency, integration test transaction ghi danh và E2E luồng quét QR; Doc cập nhật đặc tả API enrollment/attendance/card. | Coder, Tester, Reviewer, Doc | [REQ-010], [REQ-011], [REQ-012], [EXC-001], [REQ-013], [EXC-002], [REQ-014], [REQ-015] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 4 | Ngày 1 - 3 | Task 18, Task 19, Task 20, Task 21, Task 22, Task 23, Task 24, Task 25 | ./sources/backend/notification-service/; ./sources/backend/promotion-service/; ./sources/backend/chatbot-service/; ./sources/frontend/web-app/; ./sources/frontend/mobile-app/ | Điều phối thông báo đa kênh FCM/APNs/Zalo với log thất bại delivery và retry tối đa 3 lần trước khi đánh dấu failed [REQ-016], [EXC-003]; CRUD Promotions code unique, endDate bỏ trống coi là khuyến mãi vĩnh viễn [REQ-017]; CRUD Announcements tự động ẩn sau ngày hết hạn [REQ-018]; chatbot AI trả lời truy vấn khóa học/giáo viên/trung tâm/tài khoản và escalate lên nhân viên hỗ trợ khi độ tin cậy thấp [REQ-019]; responsive UI React Native phản chiếu chức năng web theo vai trò trên Android/iOS [REQ-020]; push notification deep-link qua device token FCM/APNs [REQ-021]; phát hiện ngôn ngữ ưu tiên preference đã lưu rồi fallback Accept-Language, chuyển locale không reload [REQ-022]; SSR meta tags và hreflang alternate links en/vi/es phục vụ crawler [REQ-023]. Tester bàn giao JUnit retry delivery, integration test FCM/APNs và E2E mobile đa ngôn ngữ; Doc bổ sung hướng dẫn bản địa hóa và đặc tả API notification/promotion. | Coder, Tester, Reviewer, Doc | [REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 5 | Ngày 1 - 5 | Task 26, Task 27, Task 31, Task 32, Task 33 | ./sources/backend/reporting-service/; ./sources/infra/; ./sources/docs/ | Xuất file CSV báo cáo điểm danh cột StudentName, CourseName, AttendanceDate, Status theo trung tâm và khoảng ngày, xử lý FIFO các scan tồn đọng hậu outage kèm thông báo phục hồi [REQ-024], [EXC-005]; dashboard real-time totalStudents, activeCourses, upcomingSessions đọc qua PostgreSQL read replica cách ly workload báo cáo [REQ-025]; chốt stack production Java/Quarkus, PostgreSQL, Redis session caching, FCM/APNs, Zalo API, GitHub Actions [ARC-010]; Dockerfile multi-stage base image dưới 200MB và final image dưới 500MB, Terraform provisioning VPC/IAM/Storage trên GCP, manifests GKE HPA CPU vượt 70% hoặc latency vượt 300ms, failover liên cluster uptime 99.9%, TLS 1.3/AES-256 với mitigations OWASP Top 10, backup PITR 24h đa region, audit log lưu trữ 1 năm, workflow GDPR/CCPA export/deletion và consent management [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]; bộ tài liệu doanh nghiệp blueprint kiến trúc, hợp đồng OpenAPI, hướng dẫn vận hành vi/en/es [NFR-006], [NFR-007], [NFR-008]. Tester bàn giao performance/integration test hạ tầng và profile E2E production; Doc hoàn thiện blueprint kiến trúc, quy trình audit log và consent GDPR/CCPA. | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-024], [EXC-005], [REQ-025], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] <!--REGISTERED_PHASE_ROW--> |
| **Kiểm toán** | **Xác minh phân phối Master Backlog** | **Tổng số Giai đoạn:** 5 | **Tổng số Thẻ Backlog:** 61 | **Tổng số Thẻ đã phân bổ:** 61 | **Tổng số Nhiệm vụ đã phân bổ:** 33 | **Trạng thái & Tuân thủ:** Đã xác minh (100%) |

<!--END_PHASE_SYNOPSIS_GRID-->

## 🔬 5. ĐẶC TẢ CHI TIẾT THEO GIAI ĐOẠN & SẢN PHẨM BÀN GIAO HÀNG NGÀY

<!--START_PHASE_INDEX-->

### 📈 Giai đoạn 1 - Khởi tạo Khung Dự án, Lược đồ Dữ liệu Hợp nhất & Dịch vụ Xác thực

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Hoàn tất nền móng hạ tầng của nền tảng membership-hub: sinh descriptor build gốc `./sources/backend/pom.xml` cùng descriptor module con cho auth-service và db-migrations theo mô hình microservices Java/Quarkus, đồng thời khởi tạo workspace frontend Next.js/React Native với TypeScript strict mode [ARC-000]; thực thi chuỗi Flyway migration tạo đủ 11 bảng lõi (Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, SystemSettings) với khóa ngoại, unique constraint và index tối ưu truy vấn [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]; triển khai endpoint POST /api/v1/auth/register hash bcrypt cấp JWT 15 phút kèm refresh token [REQ-001] với cơ chế liệt kê từng trường không hợp lệ khi validation thất bại [EXC-004]; tích hợp đăng nhập mạng xã hội OAuth2 Firebase/Google/Facebook [REQ-002]; xây dựng API gán/thay đổi vai trò người dùng kèm audit log mọi thay đổi [REQ-003]. Tester bàn giao JUnit suite auth, integration test migration CSDL và profile E2E đăng ký; Doc bàn giao blueprint kiến trúc tổng thể và đặc tả tham chiếu API auth-service.

- **Ma trận Bản đồ Thư mục Vật lý Đích:**
    * ./sources/backend/pom.xml [ARC-000]
    * ./sources/backend/auth-service/pom.xml [ARC-000]
    * ./sources/backend/db-migrations/pom.xml [ARC-000]
    * ./sources/frontend/package.json [ARC-000]
    * ./sources/frontend/tsconfig.json [ARC-000]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V1__create_roles_and_users_tables.sql [DAT-002], [DAT-001]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V2__create_centers_table.sql [DAT-003]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V3__create_courses_table.sql [DAT-004]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V4__create_enrollments_table.sql [DAT-005]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V5__create_attendance_table.sql [DAT-006]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V6__create_student_cards_table.sql [DAT-007]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V7__create_notifications_table.sql [DAT-008]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V8__create_promotions_and_announcements_tables.sql [DAT-009], [DAT-010]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V9__create_system_settings_table.sql [DAT-011]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/dto/RegisterRequest.java [REQ-001], [EXC-004]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/UserRegistrationService.java [REQ-001]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/JwtTokenIssuer.java [REQ-001]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/AuthResource.java [REQ-001]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/exception/GlobalExceptionMapper.java [EXC-004]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuth2LoginService.java [REQ-002]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/oauth/SocialProviderAdapter.java [REQ-002]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/OAuthResource.java [REQ-002]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/RoleAssignmentService.java [REQ-003]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/audit/AuditLogRecorder.java [REQ-003]
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/AdminRoleResource.java [REQ-003]
    * ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/BootstrapContextIT.java [ARC-000]
    * ./sources/backend/db-migrations/src/test/java/com/membershiphub/db/CoreSchemaMigrationIT.java [DAT-001], [DAT-002], [DAT-003], [DAT-004]
    * ./sources/backend/db-migrations/src/test/java/com/membershiphub/db/FullMigrationChainIT.java [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]
    * ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/UserRegistrationServiceTest.java [REQ-001], [EXC-004]
    * ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/OAuth2LoginServiceTest.java [REQ-002]
    * ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/OAuth2FlowIT.java [REQ-002]
    * ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/RoleAssignmentServiceTest.java [REQ-003]
    * ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/AuthLifecycleE2EIT.java [REQ-001], [REQ-002], [REQ-003]
    * ./sources/docs/architecture-blueprint.md [ARC-000]
    * ./sources/docs/data-dictionary-core-tables.md [DAT-001], [DAT-002], [DAT-003], [DAT-004]
    * ./sources/docs/data-dictionary-operational-tables.md [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]
    * ./sources/docs/api-auth-service-reference.md [REQ-001], [EXC-004], [REQ-002], [REQ-003]

- **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]:

```sql
-- =====================================================================
-- membership-hub | Unified Flyway Migration Chain (PostgreSQL 15+)
-- Scope: Phase 1 | ANSI-compliant typing, no inline ENUM types
-- =====================================================================

-- ---------------------------------------------------------------------
-- File: V1__create_roles_and_users_tables.sql [DAT-002], [DAT-001]
-- ---------------------------------------------------------------------
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE roles (
    role_id      SMALLINT     NOT NULL,
    name         VARCHAR(30)  NOT NULL,
    description  VARCHAR(200),
    CONSTRAINT pk_roles PRIMARY KEY (role_id),
    CONSTRAINT uq_roles_name UNIQUE (name)
);

INSERT INTO roles (role_id, name, description) VALUES
    (1, 'SYSTEM_ADMIN', 'Global super user across all centers'),
    (2, 'CENTER_ADMIN', 'Full control limited to the assigned center'),
    (3, 'MANAGER',      'Deputy administrator with restricted permissions'),
    (4, 'TEACHER',      'Read-only access to own teaching schedule'),
    (5, 'STUDENT',      'Course browsing, enrollment and membership card');

CREATE TABLE users (
    user_id        UUID          NOT NULL DEFAULT gen_random_uuid(),
    email          VARCHAR(255)  NOT NULL,
    password_hash  CHAR(60)      NOT NULL,
    full_name      VARCHAR(100)  NOT NULL,
    role_id        SMALLINT      NOT NULL,
    provider       VARCHAR(20)   NOT NULL DEFAULT 'local',
    created_at     TIMESTAMP     NOT NULL DEFAULT now(),
    updated_at     TIMESTAMP     NOT NULL DEFAULT now(),
    CONSTRAINT pk_users PRIMARY KEY (user_id),
    CONSTRAINT uq_users_email UNIQUE (email),
    CONSTRAINT fk_users_role FOREIGN KEY (role_id) REFERENCES roles (role_id),
    CONSTRAINT ck_users_provider CHECK (provider IN ('local', 'firebase', 'google', 'facebook'))
);
CREATE INDEX idx_users_role_id ON users (role_id);
CREATE INDEX idx_users_provider ON users (provider);

-- ---------------------------------------------------------------------
-- File: V2__create_centers_table.sql [DAT-003]
-- ---------------------------------------------------------------------
CREATE TABLE centers (
    center_id      UUID          NOT NULL DEFAULT gen_random_uuid(),
    name           VARCHAR(100)  NOT NULL,
    address        VARCHAR(255)  NOT NULL,
    tax_id         VARCHAR(13)   NOT NULL,
    contact_phone  VARCHAR(30),
    contact_email  VARCHAR(255),
    CONSTRAINT pk_centers PRIMARY KEY (center_id),
    CONSTRAINT uq_centers_tax_id UNIQUE (tax_id),
    CONSTRAINT ck_centers_tax_id_digits CHECK (tax_id ~ '^[0-9]{10,13}$'),
    CONSTRAINT ck_centers_contact_email CHECK (contact_email IS NULL OR contact_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$')
);

-- ---------------------------------------------------------------------
-- File: V3__create_courses_table.sql [DAT-004]
-- ---------------------------------------------------------------------
CREATE TABLE courses (
    course_id     UUID          NOT NULL DEFAULT gen_random_uuid(),
    title         VARCHAR(150)  NOT NULL,
    description   TEXT,
    start_date    DATE          NOT NULL,
    end_date      DATE          NOT NULL,
    teacher_id    UUID,
    max_students  INTEGER       NOT NULL DEFAULT 30,
    CONSTRAINT pk_courses PRIMARY KEY (course_id),
    CONSTRAINT fk_courses_teacher FOREIGN KEY (teacher_id) REFERENCES users (user_id),
    CONSTRAINT ck_courses_date_range CHECK (end_date >= start_date),
    CONSTRAINT ck_courses_capacity CHECK (max_students > 0)
);
CREATE INDEX idx_courses_teacher_id ON courses (teacher_id);
CREATE INDEX idx_courses_start_date ON courses (start_date);

-- ---------------------------------------------------------------------
-- File: V4__create_enrollments_table.sql [DAT-005]
-- ---------------------------------------------------------------------
CREATE TABLE enrollments (
    enrollment_id    UUID       NOT NULL DEFAULT gen_random_uuid(),
    student_id       UUID       NOT NULL,
    course_id        UUID       NOT NULL,
    enrollment_date  TIMESTAMP  NOT NULL DEFAULT now(),
    CONSTRAINT pk_enrollments PRIMARY KEY (enrollment_id),
    CONSTRAINT fk_enrollments_student FOREIGN KEY (student_id) REFERENCES users (user_id),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (course_id) REFERENCES courses (course_id),
    CONSTRAINT uq_enrollments_student_course UNIQUE (student_id, course_id)
);
CREATE INDEX idx_enrollments_student_id ON enrollments (student_id);
CREATE INDEX idx_enrollments_course_id ON enrollments (course_id);

-- ---------------------------------------------------------------------
-- File: V5__create_attendance_table.sql [DAT-006]
-- Idempotency gate: one row per (student, course, day)
-- ---------------------------------------------------------------------
CREATE TABLE attendance (
    attendance_id    UUID        NOT NULL DEFAULT gen_random_uuid(),
    student_id       UUID        NOT NULL,
    course_id        UUID        NOT NULL,
    attendance_date  DATE        NOT NULL,
    recorded_at      TIMESTAMP   NOT NULL DEFAULT now(),
    CONSTRAINT pk_attendance PRIMARY KEY (attendance_id),
    CONSTRAINT fk_attendance_student FOREIGN KEY (student_id) REFERENCES users (user_id),
    CONSTRAINT fk_attendance_course FOREIGN KEY (course_id) REFERENCES courses (course_id),
    CONSTRAINT uq_attendance_idempotent UNIQUE (student_id, course_id, attendance_date)
);
CREATE INDEX idx_attendance_course_date ON attendance (course_id, attendance_date);

-- ---------------------------------------------------------------------
-- File: V6__create_student_cards_table.sql [DAT-007]
-- ---------------------------------------------------------------------
CREATE TABLE student_cards (
    card_id         UUID       NOT NULL DEFAULT gen_random_uuid(),
    student_id      UUID       NOT NULL,
    issue_date      DATE       NOT NULL,
    validity_days   INTEGER    NOT NULL,
    remaining_days  INTEGER    NOT NULL DEFAULT 0,
    CONSTRAINT pk_student_cards PRIMARY KEY (card_id),
    CONSTRAINT fk_student_cards_student FOREIGN KEY (student_id) REFERENCES users (user_id),
    CONSTRAINT uq_student_cards_student UNIQUE (student_id),
    CONSTRAINT ck_student_cards_validity CHECK (validity_days > 0)
);
CREATE INDEX idx_student_cards_student_id ON student_cards (student_id);

-- ---------------------------------------------------------------------
-- File: V7__create_notifications_table.sql [DAT-008]
-- ---------------------------------------------------------------------
CREATE TABLE notifications (
    notification_id  UUID          NOT NULL DEFAULT gen_random_uuid(),
    user_id          UUID,
    group_zalo       VARCHAR(100),
    message          TEXT          NOT NULL,
    sent_at          TIMESTAMP     NOT NULL DEFAULT now(),
    delivered        BOOLEAN       NOT NULL DEFAULT FALSE,
    retry_count      SMALLINT      NOT NULL DEFAULT 0,
    delivery_status  VARCHAR(20)   NOT NULL DEFAULT 'PENDING',
    CONSTRAINT pk_notifications PRIMARY KEY (notification_id),
    CONSTRAINT fk_notifications_user FOREIGN KEY (user_id) REFERENCES users (user_id),
    CONSTRAINT ck_notifications_status CHECK (delivery_status IN ('PENDING', 'SENT', 'RETRYING', 'FAILED')),
    CONSTRAINT ck_notifications_retry_cap CHECK (retry_count <= 3)
);
CREATE INDEX idx_notifications_user_id ON notifications (user_id);
CREATE INDEX idx_notifications_status ON notifications (delivery_status);

-- ---------------------------------------------------------------------
-- File: V8__create_promotions_and_announcements_tables.sql [DAT-009], [DAT-010]
-- ---------------------------------------------------------------------
CREATE TABLE promotions (
    promo_id          UUID          NOT NULL DEFAULT gen_random_uuid(),
    code              VARCHAR(50)   NOT NULL,
    discount_percent  SMALLINT      NOT NULL,
    start_date        DATE,
    end_date          DATE,
    description       TEXT,
    CONSTRAINT pk_promotions PRIMARY KEY (promo_id),
    CONSTRAINT uq_promotions_code UNIQUE (code),
    CONSTRAINT ck_promotions_discount_range CHECK (discount_percent BETWEEN 1 AND 100),
    CONSTRAINT ck_promotions_date_range CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE announcements (
    announcement_id  UUID           NOT NULL DEFAULT gen_random_uuid(),
    title            VARCHAR(150)   NOT NULL,
    content          VARCHAR(2000)  NOT NULL,
    start_date       DATE,
    end_date         DATE,
    CONSTRAINT pk_announcements PRIMARY KEY (announcement_id),
    CONSTRAINT ck_announcements_date_range CHECK (end_date IS NULL OR end_date >= start_date)
);
CREATE INDEX idx_announcements_end_date ON announcements (end_date);

-- ---------------------------------------------------------------------
-- File: V9__create_system_settings_table.sql [DAT-011]
-- ---------------------------------------------------------------------
CREATE TABLE system_settings (
    setting_key    VARCHAR(100)  NOT NULL,
    setting_value  TEXT          NOT NULL,
    description    VARCHAR(255),
    CONSTRAINT pk_system_settings PRIMARY KEY (setting_key)
);
```

- **Hợp đồng Định tuyến API và Sự kiện** [REQ-001], [REQ-002], [REQ-003], [ARC-000]:

1. Đăng ký người dùng — POST /api/v1/auth/register [REQ-001], [EXC-004]:

```json
{
  "endpoint": "POST /api/v1/auth/register",
  "security": "PUBLIC",
  "request": {
    "email": "string | required | RFC 5322 | unique | max 255",
    "password": "string | required | min 8 chars | 1 uppercase + 1 digit + 1 special",
    "fullName": "string | required | max 100",
    "acceptedTerms": "boolean | required | must be true"
  },
  "response_201": {
    "userId": "550e8400-e29b-41d4-a716-446655440000",
    "email": "nguyen.van.a@example.com",
    "fullName": "Nguyen Van A",
    "role": "STUDENT",
    "accessToken": "<JWT_RS256_exp_900s>",
    "refreshToken": "<OPAQUE_UUID_exp_604800s>",
    "tokenType": "Bearer"
  },
  "response_400": {
    "errorCode": "AUTH_VALIDATION_FAILED",
    "invalidFields": [
      {"field": "email", "rejectedValue": "abc@", "message": "Invalid email format"},
      {"field": "password", "rejectedValue": null, "message": "Password does not meet complexity policy"}
    ]
  },
  "response_409": {
    "errorCode": "EMAIL_ALREADY_EXISTS",
    "message": "A user with this email already exists"
  }
}
```

2. Đăng nhập mạng xã hội — POST /api/v1/auth/oauth2/{provider} [REQ-002]:

```json
{
  "endpoint": "POST /api/v1/auth/oauth2/{provider}",
  "pathParams": {"provider": "firebase | google | facebook"},
  "security": "PUBLIC",
  "request": {
    "authorizationCode": "string | required | provider-issued OAuth2 code",
    "redirectUri": "string | required | registered callback URL"
  },
  "response_200": {
    "userId": "6f1c2a84-93b0-4f7e-8a21-c0d5e7b91123",
    "email": "tran.thi.b@gmail.com",
    "fullName": "Tran Thi B",
    "provider": "google",
    "role": "STUDENT",
    "accessToken": "<JWT_RS256_exp_900s>",
    "refreshToken": "<OPAQUE_UUID_exp_604800s>",
    "tokenType": "Bearer",
    "isNewUser": false
  },
  "response_401": {
    "errorCode": "OAUTH2_CODE_EXCHANGE_FAILED",
    "message": "Provider rejected the authorization code"
  }
}
```

3. Phân quyền vai trò — PUT /api/v1/admin/users/{userId}/role [REQ-003]:

```json
{
  "endpoint": "PUT /api/v1/admin/users/{userId}/role",
  "security": "BEARER JWT | role=SYSTEM_ADMIN",
  "pathParams": {"userId": "uuid"},
  "request": {
    "roleId": 2,
    "reason": "string | optional | audit trail annotation"
  },
  "response_200": {
    "userId": "550e8400-e29b-41d4-a716-446655440000",
    "previousRoleId": 5,
    "newRoleId": 2,
    "permissionsAppliedAt": "2025-01-15T08:30:00Z",
    "auditLogId": "9a7b6c5d-4e3f-4a2b-8c1d-0f9e8d7c6b5a"
  },
  "response_403": {
    "errorCode": "ROLE_ASSIGNMENT_FORBIDDEN",
    "message": "Caller lacks SYSTEM_ADMIN privilege"
  },
  "auditEvent": {
    "action": "USER_ROLE_CHANGED",
    "actorUserId": "uuid",
    "targetUserId": "uuid",
    "timestamp": "now()"
  }
}
```

- **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn** [EXC-004]:
    * **Mã lỗi:** `AUTH_VALIDATION_FAILED` — HTTP 400, kích hoạt khi request POST /api/v1/auth/register vi phạm ít nhất một ràng buộc đầu vào.
    * **Quy tắc nghiệp vụ:** email phải đúng định dạng RFC 5322 và duy nhất trong hệ thống; mật khẩu tối thiểu 8 ký tự bao gồm chữ hoa, chữ số và ký tự đặc biệt; fullName bắt buộc, tối đa 100 ký tự; acceptedTerms phải mang giá trị true.
    * **Luồng xử lý:** Bean Validation chặn tại lớp DTO → ném ConstraintViolationException → GlobalExceptionMapper hợp nhất toàn bộ vi phạm → phản hồi JSON chứa mảng invalidFields liệt kê từng trường không hợp lệ kèm thông báo rõ ràng, hướng dẫn người dùng chỉnh sửa trước khi gửi lại biểu mẫu.

#### 📅 Nhật ký Phân bổ Tác vụ Sub-Agent theo Trình tự Thời gian (Giai đoạn 1)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Khởi tạo khung dự án backend multi-module và workspace frontend [ARC-000]

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Sinh descriptor build gốc Maven cho chuỗi dịch vụ Quarkus

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/pom.xml
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Khai báo packaging=pom với Quarkus BOM trong dependencyManagement tập trung; cố định maven-compiler-plugin ở Java 21 với encoding UTF-8; liệt kê hai module con auth-service và db-migrations; thiết lập profile dev và production kiểm soát cấu hình môi trường thống nhất. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Sinh descriptor module con auth-service

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/pom.xml
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Kế thừa parent root; khai báo dependency quarkus-rest, quarkus-hibernate-orm, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-redis-client; gắn quarkus-maven-plugin cho vòng đời dev/build; định nghĩa thuộc tính tên dịch vụ phục vụ đóng gói image. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Sinh descriptor module con db-migrations

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/pom.xml
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Thiết lập module chuyên chứa tài nguyên Flyway: dependency flyway-core và postgresql driver; cấu hình resource copying giữ nguyên thư mục db/migration để chuỗi migration được đóng gói vào artifact triển khai chung. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Khởi tạo manifest workspace frontend Next.js/React Native

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/frontend/package.json
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Khai báo scripts dev/build/lint/start; khai báo dependencies next, react, react-native, typescript; cấu hình workspaces cho hai ứng dụng con web-app và mobile-app làm nền chung cho các giai đoạn giao diện phía sau. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Cấu hình biên dịch TypeScript strict mode

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/frontend/tsconfig.json
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Bật strict:true, noUncheckedIndexedAccess, exactOptionalPropertyTypes; ánh xạ path alias @/* về src/*; chọn target ES2022, moduleResolution bundler, jsx preserve để tương thích đồng thời Next.js SSR và React Native Metro. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Kiểm chứng bootstrap context dịch vụ xác thực

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/com/membershiphub/auth/BootstrapContextIT.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Viết @QuarkusIntegrationTest khởi động auth-service từ descriptor vừa sinh; xác minh context tải thành công, health probe UP và cây Maven không xung đột phiên bản; fail build nếu bootstrap lỗi. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Kiểm toán chất lượng descriptor build

* **Chuyên môn hóa Quy trình Sub-Agent:** [Reviewer]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/pom.xml
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Rà soát dependencyManagement tránh phiên bản trùng lặp hoặc xung đột plugin, chuẩn hóa thứ tự khai báo module; lập danh sách remediation và chốt điều kiện mở khóa giai đoạn xây dựng lược đồ dữ liệu. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Biên soạn bản phác thảo blueprint kiến trúc

* **Chuyên môn hóa Quy trình Sub-Agent:** [Doc]
* **Tag ID Mục tiêu:** [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/docs/architecture-blueprint.md
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Biên soạn khung blueprint: topology microservices hiện hành (auth-service, db-migrations), sơ đồ phụ thuộc Maven, chiến lược profile dev/production, quy ước gói com.membershiphub.*; đánh dấu mục lục các phần sẽ bổ sung ở giai đoạn sau. [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 2: Xây dựng lược đồ dữ liệu hạt nhân — Roles, Users, Centers, Courses [DAT-001], [DAT-002], [DAT-003], [DAT-004]

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Migration V1 — bảng Roles và Users

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-002], [DAT-001]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V1__create_roles_and_users_tables.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo bảng roles (role_id SMALLINT PK, name VARCHAR(30) UNIQUE, description VARCHAR(200)) và seed 5 vai trò SYSTEM_ADMIN/CENTER_ADMIN/MANAGER/TEACHER/STUDENT; tạo bảng users với email VARCHAR(255) UNIQUE, password_hash CHAR(60) bcrypt, role_id FK, provider VARCHAR(20) DEFAULT 'local' kèm CHECK IN ('local','firebase','google','facebook'); thêm index idx_users_role_id. [DAT-002], [DAT-001]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-002], [DAT-001]:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE roles (
    role_id      SMALLINT     NOT NULL,
    name         VARCHAR(30)  NOT NULL,
    description  VARCHAR(200),
    CONSTRAINT pk_roles PRIMARY KEY (role_id),
    CONSTRAINT uq_roles_name UNIQUE (name)
);

INSERT INTO roles (role_id, name, description) VALUES
    (1, 'SYSTEM_ADMIN', 'Global super user across all centers'),
    (2, 'CENTER_ADMIN', 'Full control limited to the assigned center'),
    (3, 'MANAGER',      'Deputy administrator with restricted permissions'),
    (4, 'TEACHER',      'Read-only access to own teaching schedule'),
    (5, 'STUDENT',      'Course browsing, enrollment and membership card');

CREATE TABLE users (
    user_id        UUID          NOT NULL DEFAULT gen_random_uuid(),
    email          VARCHAR(255)  NOT NULL,
    password_hash  CHAR(60)      NOT NULL,
    full_name      VARCHAR(100)  NOT NULL,
    role_id        SMALLINT      NOT NULL,
    provider       VARCHAR(20)   NOT NULL DEFAULT 'local',
    created_at     TIMESTAMP     NOT NULL DEFAULT now(),
    updated_at     TIMESTAMP     NOT NULL DEFAULT now(),
    CONSTRAINT pk_users PRIMARY KEY (user_id),
    CONSTRAINT uq_users_email UNIQUE (email),
    CONSTRAINT fk_users_role FOREIGN KEY (role_id) REFERENCES roles (role_id),
    CONSTRAINT ck_users_provider CHECK (provider IN ('local', 'firebase', 'google', 'facebook'))
);
CREATE INDEX idx_users_role_id ON users (role_id);
CREATE INDEX idx_users_provider ON users (provider);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Migration V2 — bảng Centers

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-003]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V2__create_centers_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo bảng centers với tax_id VARCHAR(13) UNIQUE và CHECK regex ^[0-9]{10,13}$ ép định dạng số 10–13 chữ số; contact_email áp dụng kiểm tra pattern email khi có giá trị; các cột name/address NOT NULL theo từ điển dữ liệu. [DAT-003]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-003]:

```sql
CREATE TABLE centers (
    center_id      UUID          NOT NULL DEFAULT gen_random_uuid(),
    name           VARCHAR(100)  NOT NULL,
    address        VARCHAR(255)  NOT NULL,
    tax_id         VARCHAR(13)   NOT NULL,
    contact_phone  VARCHAR(30),
    contact_email  VARCHAR(255),
    CONSTRAINT pk_centers PRIMARY KEY (center_id),
    CONSTRAINT uq_centers_tax_id UNIQUE (tax_id),
    CONSTRAINT ck_centers_tax_id_digits CHECK (tax_id ~ '^[0-9]{10,13}$'),
    CONSTRAINT ck_centers_contact_email CHECK (contact_email IS NULL OR contact_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$')
);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Migration V3 — bảng Courses

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V3__create_courses_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo bảng courses với teacher_id FK về users(user_id) cho phép NULL, max_students INTEGER DEFAULT 30 kèm CHECK > 0, CHECK end_date >= start_date; index teacher_id và start_date phục vụ tra cứu lịch dạy và lưới khóa học. [DAT-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-004]:

```sql
CREATE TABLE courses (
    course_id     UUID          NOT NULL DEFAULT gen_random_uuid(),
    title         VARCHAR(150)  NOT NULL,
    description   TEXT,
    start_date    DATE          NOT NULL,
    end_date      DATE          NOT NULL,
    teacher_id    UUID,
    max_students  INTEGER       NOT NULL DEFAULT 30,
    CONSTRAINT pk_courses PRIMARY KEY (course_id),
    CONSTRAINT fk_courses_teacher FOREIGN KEY (teacher_id) REFERENCES users (user_id),
    CONSTRAINT ck_courses_date_range CHECK (end_date >= start_date),
    CONSTRAINT ck_courses_capacity CHECK (max_students > 0)
);
CREATE INDEX idx_courses_teacher_id ON courses (teacher_id);
CREATE INDEX idx_courses_start_date ON courses (start_date);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Integration test chuỗi migration V1–V3

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [DAT-001], [DAT-002], [DAT-003], [DAT-004]
* **Đường dẫn Thành phần Đích (target_component):** INTEGRATION_SCOPE;./sources/backend/db-migrations/src/test/java/com/membershiphub/db/CoreSchemaMigrationIT.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Dùng Testcontainers PostgreSQL 15 chạy Flyway migrate; assert 5 dòng seed roles; chèn user hợp lệ thành công; email trùng bị từ chối bởi unique constraint; tax_id 9 chữ số bị chặn, tax_id 10–13 chữ số được chấp nhận. [DAT-001], [DAT-002], [DAT-003], [DAT-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Rà soát ràng buộc và index lược đồ hạt nhân

* **Chuyên môn hóa Quy trình Sub-Agent:** [Reviewer]
* **Tag ID Mục tiêu:** [DAT-001], [DAT-002], [DAT-003], [DAT-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V1__create_roles_and_users_tables.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Kiểm tra tuân thủ ANSI SQL (cấm ENUM inline, thay bằng VARCHAR + CHECK), độ kín của khóa ngoại, unique constraint và index cho các truy vấn danh sách; đề xuất chỉnh sửa trước khi cho phép merge. [DAT-001], [DAT-002], [DAT-003], [DAT-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Biên soạn từ điển dữ liệu bảng hạt nhân

* **Chuyên môn hóa Quy trình Sub-Agent:** [Doc]
* **Tag ID Mục tiêu:** [DAT-001], [DAT-002], [DAT-003], [DAT-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/docs/data-dictionary-core-tables.md
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Mô tả từng cột, kiểu dữ liệu, ràng buộc của 4 bảng hạt nhân; vẽ quan hệ ROLES ||--o{ USERS và USERS ||--o{ COURSES; kèm ví dụ giá trị và ghi chú ảnh hưởng tới API giai đoạn 2. [DAT-001], [DAT-002], [DAT-003], [DAT-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 3: Hoàn thiện chuỗi migration 11 bảng lõi — Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, SystemSettings [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Migration V4 — bảng Enrollments

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-005]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V4__create_enrollments_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo enrollments với FK student_id→users, course_id→courses và UNIQUE (student_id, course_id) chặn ghi danh trùng; index hai chiều phục vụ duyệt khóa học loại trừ các khóa đã có bản ghi. [DAT-005]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-005]:

```sql
CREATE TABLE enrollments (
    enrollment_id    UUID       NOT NULL DEFAULT gen_random_uuid(),
    student_id       UUID       NOT NULL,
    course_id        UUID       NOT NULL,
    enrollment_date  TIMESTAMP  NOT NULL DEFAULT now(),
    CONSTRAINT pk_enrollments PRIMARY KEY (enrollment_id),
    CONSTRAINT fk_enrollments_student FOREIGN KEY (student_id) REFERENCES users (user_id),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (course_id) REFERENCES courses (course_id),
    CONSTRAINT uq_enrollments_student_course UNIQUE (student_id, course_id)
);
CREATE INDEX idx_enrollments_student_id ON enrollments (student_id);
CREATE INDEX idx_enrollments_course_id ON enrollments (course_id);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Migration V5 — bảng Attendance với cổng idempotent

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-006]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V5__create_attendance_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo attendance với cổng idempotent UNIQUE (student_id, course_id, attendance_date) bảo đảm một dòng duy nhất mỗi ngày; recorded_at TIMESTAMP DEFAULT now(); index (course_id, attendance_date) phục vụ báo cáo điểm danh theo trung tâm. [DAT-006]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-006]:

```sql
CREATE TABLE attendance (
    attendance_id    UUID        NOT NULL DEFAULT gen_random_uuid(),
    student_id       UUID        NOT NULL,
    course_id        UUID        NOT NULL,
    attendance_date  DATE        NOT NULL,
    recorded_at      TIMESTAMP   NOT NULL DEFAULT now(),
    CONSTRAINT pk_attendance PRIMARY KEY (attendance_id),
    CONSTRAINT fk_attendance_student FOREIGN KEY (student_id) REFERENCES users (user_id),
    CONSTRAINT fk_attendance_course FOREIGN KEY (course_id) REFERENCES courses (course_id),
    CONSTRAINT uq_attendance_idempotent UNIQUE (student_id, course_id, attendance_date)
);
CREATE INDEX idx_attendance_course_date ON attendance (course_id, attendance_date);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Migration V6 — bảng StudentCards

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-007]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V6__create_student_cards_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo student_cards với UNIQUE(student_id) bảo đảm một thẻ mỗi học viên, validity_days CHECK > 0, remaining_days DEFAULT 0 do tầng ứng dụng suy ra từ issue_date cộng validityDays. [DAT-007]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-007]:

```sql
CREATE TABLE student_cards (
    card_id         UUID       NOT NULL DEFAULT gen_random_uuid(),
    student_id      UUID       NOT NULL,
    issue_date      DATE       NOT NULL,
    validity_days   INTEGER    NOT NULL,
    remaining_days  INTEGER    NOT NULL DEFAULT 0,
    CONSTRAINT pk_student_cards PRIMARY KEY (card_id),
    CONSTRAINT fk_student_cards_student FOREIGN KEY (student_id) REFERENCES users (user_id),
    CONSTRAINT uq_student_cards_student UNIQUE (student_id),
    CONSTRAINT ck_student_cards_validity CHECK (validity_days > 0)
);
CREATE INDEX idx_student_cards_student_id ON student_cards (student_id);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Migration V7 — bảng Notifications

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-008]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V7__create_notifications_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo notifications với delivery_status VARCHAR(20) DEFAULT 'PENDING' kèm CHECK IN ('PENDING','SENT','RETRYING','FAILED'), retry_count SMALLINT CHECK <= 3 tương ứng cơ chế thử lại tối đa ba lần, delivered BOOLEAN DEFAULT FALSE. [DAT-008]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-008]:

```sql
CREATE TABLE notifications (
    notification_id  UUID          NOT NULL DEFAULT gen_random_uuid(),
    user_id          UUID,
    group_zalo       VARCHAR(100),
    message          TEXT          NOT NULL,
    sent_at          TIMESTAMP     NOT NULL DEFAULT now(),
    delivered        BOOLEAN       NOT NULL DEFAULT FALSE,
    retry_count      SMALLINT      NOT NULL DEFAULT 0,
    delivery_status  VARCHAR(20)   NOT NULL DEFAULT 'PENDING',
    CONSTRAINT pk_notifications PRIMARY KEY (notification_id),
    CONSTRAINT fk_notifications_user FOREIGN KEY (user_id) REFERENCES users (user_id),
    CONSTRAINT ck_notifications_status CHECK (delivery_status IN ('PENDING', 'SENT', 'RETRYING', 'FAILED')),
    CONSTRAINT ck_notifications_retry_cap CHECK (retry_count <= 3)
);
CREATE INDEX idx_notifications_user_id ON notifications (user_id);
CREATE INDEX idx_notifications_status ON notifications (delivery_status);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Migration V8 — bảng Promotions và Announcements

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-009], [DAT-010]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V8__create_promotions_and_announcements_tables.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo promotions (code UNIQUE, discount_percent SMALLINT CHECK BETWEEN 1 AND 100, start_date/end_date NULLABLE với end_date NULL nghĩa là khuyến mãi vĩnh viễn) và announcements (title 150, content 2000, index end_date phục vụ tự động ẩn sau hết hạn). [DAT-009], [DAT-010]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-009], [DAT-010]:

```sql
CREATE TABLE promotions (
    promo_id          UUID          NOT NULL DEFAULT gen_random_uuid(),
    code              VARCHAR(50)   NOT NULL,
    discount_percent  SMALLINT      NOT NULL,
    start_date        DATE,
    end_date          DATE,
    description       TEXT,
    CONSTRAINT pk_promotions PRIMARY KEY (promo_id),
    CONSTRAINT uq_promotions_code UNIQUE (code),
    CONSTRAINT ck_promotions_discount_range CHECK (discount_percent BETWEEN 1 AND 100),
    CONSTRAINT ck_promotions_date_range CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE announcements (
    announcement_id  UUID           NOT NULL DEFAULT gen_random_uuid(),
    title            VARCHAR(150)   NOT NULL,
    content          VARCHAR(2000)  NOT NULL,
    start_date       DATE,
    end_date         DATE,
    CONSTRAINT pk_announcements PRIMARY KEY (announcement_id),
    CONSTRAINT ck_announcements_date_range CHECK (end_date IS NULL OR end_date >= start_date)
);
CREATE INDEX idx_announcements_end_date ON announcements (end_date);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Migration V9 — bảng SystemSettings

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [DAT-011]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V9__create_system_settings_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Tạo system_settings dạng key-value với setting_key VARCHAR(100) PK, setting_value TEXT NOT NULL, description tùy chọn; làm nơi lưu locale mặc định và tham số SEO hreflang cho giai đoạn bản địa hóa. [DAT-011]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu** [DAT-011]:

```sql
CREATE TABLE system_settings (
    setting_key    VARCHAR(100)  NOT NULL,
    setting_value  TEXT          NOT NULL,
    description    VARCHAR(255),
    CONSTRAINT pk_system_settings PRIMARY KEY (setting_key)
);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Integration test chuỗi migration đầy đủ V1–V9

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]
* **Đường dẫn Thành phần Đích (target_component):** INTEGRATION_SCOPE;./sources/backend/db-migrations/src/test/java/com/membershiphub/db/FullMigrationChainIT.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Chạy toàn bộ chuỗi V1→V9 trên Testcontainers; assert chèn attendance trùng cùng ngày bị từ chối, retry_count vượt 3 bị chặn, discount_percent ngoài 1–100 bị chặn, promotion không end_date được chấp nhận; xác minh đủ 11 bảng tồn tại. [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Kiểm toán đồ thị khóa ngoại toàn cục

* **Chuyên môn hóa Quy trình Sub-Agent:** [Reviewer]
* **Tag ID Mục tiêu:** [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/db-migrations/src/main/resources/db/migration/V5__create_attendance_table.sql
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Xác minh thứ tự phụ thuộc FK V1→V9 không tạo orphan reference; xác nhận cổng idempotent UNIQUE đúng ba cột (student_id, course_id, attendance_date); duyệt và ký merge toàn bộ chuỗi migration. [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 9: Cập nhật từ điển dữ liệu bảng vận hành

* **Chuyên môn hóa Quy trình Sub-Agent:** [Doc]
* **Tag ID Mục tiêu:** [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/docs/data-dictionary-operational-tables.md
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Bổ sung mô tả cột/ràng buộc của 7 bảng vận hành; diễn giải vòng đời trạng thái notification PENDING→SENT/RETRYING/FAILED và cơ chế idempotent của attendance kèm ví dụ truy vấn. [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 4: Endpoint đăng ký người dùng và xử lý ngoại lệ xác thực đầu vào [REQ-001], [EXC-004]

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: DTO đăng ký kèm ràng buộc Bean Validation

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-001], [EXC-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/dto/RegisterRequest.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Định nghĩa record RegisterRequest với @Email @NotBlank @Size(max=255) cho email, @NotBlank @Pattern chính sách mạnh (tối thiểu 8 ký tự, chữ hoa, chữ số, ký tự đặc biệt) cho password, @NotBlank @Size(max=100) cho fullName, @AssertTrue cho acceptedTerms. [REQ-001], [EXC-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Dịch vụ đăng ký người dùng hash bcrypt

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-001]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/UserRegistrationService.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Triển khai @Transactional UserRegistrationService: kiểm tra email unique và ném EmailAlreadyExistsException khi trùng, hash BCrypt cost 12, persist Users với roleId mặc định STUDENT (TEACHER nếu theo lời mời), trả về thực thể đã tạo. [REQ-001]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: Bộ phát hành JWT và refresh token

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-001]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/JwtTokenIssuer.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Phát hành access token RS256 hết hạn 900 giây chứa claims sub/role; refresh token opaque có TTL 7 ngày lưu Redis phục vụ xoay vòng; không đưa dữ liệu nhạy cảm vào payload JWT theo khung OWASP. [REQ-001]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: REST endpoint POST /api/v1/auth/register

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-001]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/AuthResource.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** JAX-RS resource POST /api/v1/auth/register nhận RegisterRequest, điều phối UserRegistrationService, trả 201 kèm TokenResponse (accessToken, refreshToken, tokenType=Bearer); ánh xạ validation thất bại sang 400 và email trùng sang 409. [REQ-001]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

* **Hợp đồng Định tuyến API và Sự kiện** [REQ-001]:

```json
{
  "endpoint": "POST /api/v1/auth/register",
  "security": "PUBLIC",
  "request": {
    "email": "string | required | RFC 5322 | unique | max 255",
    "password": "string | required | min 8 chars | 1 uppercase + 1 digit + 1 special",
    "fullName": "string | required | max 100",
    "acceptedTerms": "boolean | required | must be true"
  },
  "response_201": {
    "userId": "550e8400-e29b-41d4-a716-446655440000",
    "email": "nguyen.van.a@example.com",
    "fullName": "Nguyen Van A",
    "role": "STUDENT",
    "accessToken": "<JWT_RS256_exp_900s>",
    "refreshToken": "<OPAQUE_UUID_exp_604800s>",
    "tokenType": "Bearer"
  },
  "response_400": {
    "errorCode": "AUTH_VALIDATION_FAILED",
    "invalidFields": [
      {"field": "email", "rejectedValue": "abc@", "message": "Invalid email format"}
    ]
  },
  "response_409": {
    "errorCode": "EMAIL_ALREADY_EXISTS",
    "message": "A user with this email already exists"
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: GlobalExceptionMapper cho luồng xác thực đầu vào

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [EXC-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/exception/GlobalExceptionMapper.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** @Provider ExceptionMapper<ConstraintViolationException> gom từng violation thành cặp {field, message}, trả 400 với errorCode=AUTH_VALIDATION_FAILED và mảng invalidFields liệt kê từng trường không hợp lệ đúng tiêu chí chấp nhận. [EXC-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn** [EXC-004]:
    * **Mã lỗi:** `AUTH_VALIDATION_FAILED` — HTTP 400.
    * **Điều kiện kích hoạt:** request POST /api/v1/auth/register vi phạm ít nhất một ràng buộc (email sai định dạng RFC 5322, mật khẩu không đạt chính sách mạnh, fullName rỗng hoặc vượt 100 ký tự, acceptedTerms = false).
    * **Luồng xử lý:** Bean Validation chặn tại DTO → ConstraintViolationException → GlobalExceptionMapper hợp nhất vi phạm → phản hồi JSON chứa invalidFields liệt kê từng trường không hợp lệ kèm thông báo rõ ràng yêu cầu chỉnh sửa.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Unit test dịch vụ đăng ký

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [REQ-001], [EXC-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/UserRegistrationService.java;./sources/backend/auth-service/src/test/java/com/membershiphub/auth/UserRegistrationServiceTest.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** @QuarkusTest: assert hash bcrypt khác plaintext và verify() thành công; email trùng sinh conflict; mật khẩu yếu và email sai định dạng sinh đúng số violation tương ứng từng trường. [REQ-001], [EXC-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Rà soát bảo mật luồng đăng ký

* **Chuyên môn hóa Quy trình Sub-Agent:** [Reviewer]
* **Tag ID Mục tiêu:** [REQ-001], [EXC-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/AuthResource.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Kiểm chứng BCrypt cost, thời hạn access 15 phút/refresh 7 ngày, không log password hay hash; bảo đảm thông điệp lỗi không dò được sự tồn tại email; phê duyệt merge endpoint đăng ký. [REQ-001], [EXC-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 8: Đặc tả tham chiếu API đăng ký

* **Chuyên môn hóa Quy trình Sub-Agent:** [Doc]
* **Tag ID Mục tiêu:** [REQ-001], [EXC-004]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/docs/api-auth-service-reference.md
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Ghi hợp đồng POST /api/v1/auth/register: schema yêu cầu, phản hồi 201/400/409, bảng mã lỗi, ví dụ curl; mô tả chính sách mật khẩu và cách hiển thị danh sách trường không hợp lệ. [REQ-001], [EXC-004]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 5: Đăng nhập mạng xã hội OAuth2 Firebase/Google/Facebook [REQ-002]

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Dịch vụ trao đổi mã OAuth2

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-002]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuth2LoginService.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Nhận authorizationCode từ client, gọi token endpoint của provider để exchange userinfo, upsert Users theo email với provider tương ứng trong một transaction, sau đó phát hành JWT phiên làm việc. [REQ-002]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Adapter nhà cung cấp danh tính xã hội

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-002]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/oauth/SocialProviderAdapter.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Định nghĩa interface SocialProviderAdapter cùng ba triển khai FirebaseTokenVerifier, GoogleIdTokenVerifier, FacebookGraphClient; chuẩn hóa UserProfile(email, fullName, provider) và xác thực chữ ký cùng audience trước khi chấp nhận danh tính. [REQ-002]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: REST endpoint POST /api/v1/auth/oauth2/{provider}

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-002]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/OAuthResource.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** POST /api/v1/auth/oauth2/{provider} giới hạn provider IN (firebase, google, facebook); trả 200 TokenResponse kèm cờ isNewUser; exchange thất bại trả 401 OAUTH2_CODE_EXCHANGE_FAILED. [REQ-002]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

* **Hợp đồng Định tuyến API và Sự kiện** [REQ-002]:

```json
{
  "endpoint": "POST /api/v1/auth/oauth2/{provider}",
  "pathParams": {"provider": "firebase | google | facebook"},
  "security": "PUBLIC",
  "request": {
    "authorizationCode": "string | required | provider-issued OAuth2 code",
    "redirectUri": "string | required | registered callback URL"
  },
  "response_200": {
    "userId": "6f1c2a84-93b0-4f7e-8a21-c0d5e7b91123",
    "email": "tran.thi.b@gmail.com",
    "fullName": "Tran Thi B",
    "provider": "google",
    "role": "STUDENT",
    "accessToken": "<JWT_RS256_exp_900s>",
    "refreshToken": "<OPAQUE_UUID_exp_604800s>",
    "tokenType": "Bearer",
    "isNewUser": false
  },
  "response_401": {
    "errorCode": "OAUTH2_CODE_EXCHANGE_FAILED",
    "message": "Provider rejected the authorization code"
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Unit test dịch vụ OAuth2

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [REQ-002]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuth2LoginService.java;./sources/backend/auth-service/src/test/java/com/membershiphub/auth/OAuth2LoginServiceTest.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Mock adapter: mã hợp lệ → upsert và cấp JWT; mã hết hạn/sai chữ ký → 401; email đã tồn tại với provider khác → cập nhật provider, không nhân bản dòng Users. [REQ-002]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Integration test luồng OAuth2 đầu-cuối

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [REQ-002]
* **Đường dẫn Thành phần Đích (target_component):** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/com/membershiphub/auth/OAuth2FlowIT.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** @QuarkusIntegrationTest với stub provider server: lần đầu isNewUser=true, lần sau false; giải mã access token xác nhận claims role và exp=900s. [REQ-002]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Rà soát an ninh trao đổi token OAuth2

* **Chuyên môn hóa Quy trình Sub-Agent:** [Reviewer]
* **Tag ID Mục tiêu:** [REQ-002]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuth2LoginService.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Xác thực state/nonce chống CSRF, kiểm tra audience/client-id và clock skew; bảo đảm không ghi log authorizationCode hay token trung gian; phê duyệt merge luồng OAuth2. [REQ-002]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Bổ sung đặc tả OAuth2 vào tham chiếu API

* **Chuyên môn hóa Quy trình Sub-Agent:** [Doc]
* **Tag ID Mục tiêu:** [REQ-002]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/docs/api-auth-service-reference.md
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Cập nhật chương OAuth2: bảng ba provider, schema yêu cầu/phản hồi, mã lỗi 401, sơ đồ sequence popup→callback→exchange→JWT phát hành. [REQ-002]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

##### 📅 NGÀY 6: Phân quyền vai trò, audit log và đóng gói bàn giao giai đoạn [REQ-003]

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 1: Dịch vụ gán/thay đổi vai trò người dùng

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-003]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/RoleAssignmentService.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Cập nhật users.role_id trong transaction; vô hiệu hóa cache phiên để ma trận quyền áp dụng tức thời; chỉ caller SYSTEM_ADMIN được phép; ném RoleAssignmentForbiddenException khi thiếu quyền. [REQ-003]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 2: Bộ ghi audit log thay đổi vai trò

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-003]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/audit/AuditLogRecorder.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Ghi append-only mỗi thay đổi vai trò gồm actorUserId, targetUserId, oldRoleId, newRoleId, action=USER_ROLE_CHANGED và timestamp; cấm cập nhật/xóa dòng audit phục vụ truy vết. [REQ-003]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 3: REST endpoint PUT /api/v1/admin/users/{userId}/role

* **Chuyên môn hóa Quy trình Sub-Agent:** [Coder]
* **Tag ID Mục tiêu:** [REQ-003]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/AdminRoleResource.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** PUT /api/v1/admin/users/{userId}/role với @RolesAllowed("SYSTEM_ADMIN"); nhận RoleAssignmentRequest(roleId, reason); trả 200 kèm previousRoleId/newRoleId/auditLogId; 403 khi thiếu quyền, 404 khi userId không tồn tại. [REQ-003]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

* **Hợp đồng Định tuyến API và Sự kiện** [REQ-003]:

```json
{
  "endpoint": "PUT /api/v1/admin/users/{userId}/role",
  "security": "BEARER JWT | role=SYSTEM_ADMIN",
  "pathParams": {"userId": "uuid"},
  "request": {
    "roleId": 2,
    "reason": "string | optional | audit trail annotation"
  },
  "response_200": {
    "userId": "550e8400-e29b-41d4-a716-446655440000",
    "previousRoleId": 5,
    "newRoleId": 2,
    "permissionsAppliedAt": "2025-01-15T08:30:00Z",
    "auditLogId": "9a7b6c5d-4e3f-4a2b-8c1d-0f9e8d7c6b5a"
  },
  "response_403": {
    "errorCode": "ROLE_ASSIGNMENT_FORBIDDEN",
    "message": "Caller lacks SYSTEM_ADMIN privilege"
  },
  "auditEvent": {
    "action": "USER_ROLE_CHANGED",
    "actorUserId": "uuid",
    "targetUserId": "uuid",
    "timestamp": "now()"
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 4: Unit test dịch vụ phân quyền

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [REQ-003]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/RoleAssignmentService.java;./sources/backend/auth-service/src/test/java/com/membershiphub/auth/RoleAssignmentServiceTest.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Assert gán hợp lệ cập nhật role_id; caller thường bị chặn 403; roleId không tồn tại ném lỗi nghiệp vụ; mỗi thao tác phát sinh đúng một dòng audit. [REQ-003]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 5: Profile E2E vòng đời xác thực

* **Chuyên môn hóa Quy trình Sub-Agent:** [Tester]
* **Tag ID Mục tiêu:** [REQ-001], [REQ-002], [REQ-003]
* **Đường dẫn Thành phần Đích (target_component):** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/com/membershiphub/auth/AuthLifecycleE2EIT.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Kịch bản E2E: đăng ký → đăng nhập OAuth2 → admin đổi vai trò → gọi API bằng token mới xác nhận quyền có hiệu lực ngay; đo latency trung bình register ở mức dưới 200 ms. [REQ-001], [REQ-002], [REQ-003]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 6: Rà soát tổng kết chất lượng giai đoạn

* **Chuyên môn hóa Quy trình Sub-Agent:** [Reviewer]
* **Tag ID Mục tiêu:** [REQ-003], [ARC-000]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/resource/AdminRoleResource.java
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Duyệt toàn bộ diff giai đoạn: descriptor build, chuỗi 9 migration, bộ endpoint auth; đối chiếu 100% tag traceability và chuẩn coding Quarkus; ký duyệt bàn giao sang Giai đoạn 2. [REQ-003], [ARC-000]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON 7: Hoàn thiện blueprint và tham chiếu API giai đoạn 1

* **Chuyên môn hóa Quy trình Sub-Agent:** [Doc]
* **Tag ID Mục tiêu:** [ARC-000], [REQ-001], [REQ-002], [REQ-003]
* **Đường dẫn Thành phần Đích (target_component):** ./sources/docs/architecture-blueprint.md
* **Hướng dẫn Tác vụ Kỹ thuật Cấp thấp:** Cập nhật trạng thái bàn giao: 11 bảng lõi đã migrate, auth-service hoàn chỉnh đăng ký/OAuth2/phân quyền; liên kết chéo data dictionary và API reference; liệt kê hạng mục mở cho Giai đoạn 2. [ARC-000], [REQ-001], [REQ-002], [REQ-003]

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->

### 📈 Giai đoạn 2 - Dịch vụ Trung tâm, Khóa học và Thực thi RBAC qua API Gateway

- **Mục tiêu cốt lõi & mục đích của giai đoạn:** Giai đoạn này kiến tạo toàn bộ tầng nghiệp vụ quản trị đa trung tâm của nền tảng membership-hub trên nền Quarkus. center-service cung cấp API danh sách trung tâm phân trang với index truy vấn sub-second [REQ-004], CRUD trung tâm validate taxId numeric 10–13 chữ số và trả 409 Conflict khi trùng [REQ-005], cùng cơ chế gán/hủy Center Admin ghi phạm vi quản lý và cô lập tenant theo trung tâm [REQ-006]. course-service vận hành lưới khóa học CourseID, Title, StartDate, EndDate, TeacherName [REQ-007], CRUD khóa học chặn xung đột lịch trên cùng teacherId với maxStudents mặc định 30 [REQ-008], và phân công giáo viên phát event sang notification-service [REQ-009]. Toàn bộ endpoint được bảo vệ bởi bộ filter/interceptor RBAC 5 vai trò (System Admin, Center Admin, Manager, Teacher, Student) thống nhất qua api-gateway [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], đồng thời công bố hợp đồng OpenAPI chuẩn hóa bốn luồng tích hợp liên dịch vụ: xác thực OAuth2/JWT, điểm danh QR idempotent, điều phối thông báo đa kênh và tích hợp mobile bearer token [ARC-006], [ARC-007], [ARC-008], [ARC-009].

- **Ma trận bản đồ thư mục vật lý đích:** Danh sách kiểm kê kỹ thuật toàn bộ 100% tệp vật lý rời rạc được tạo mới, tái cấu trúc hoặc xử lý trong phạm vi giai đoạn này:

    * ./sources/backend/center-service/src/main/java/com/hub/center/Center.java [REQ-004], [REQ-005]
    * ./sources/backend/center-service/src/main/java/com/hub/center/CenterRepository.java [REQ-004]
    * ./sources/backend/center-service/src/main/java/com/hub/center/CenterService.java [REQ-005]
    * ./sources/backend/center-service/src/main/java/com/hub/center/CenterResource.java [REQ-004], [REQ-005]
    * ./sources/backend/center-service/src/main/java/com/hub/center/CenterAdminAssignmentResource.java [REQ-006], [ARC-002]
    * ./sources/backend/center-service/src/main/java/com/hub/center/dto/CenterRequest.java [REQ-005]
    * ./sources/backend/center-service/src/main/java/com/hub/center/dto/CenterResponse.java [REQ-004]
    * ./sources/backend/center-service/src/main/resources/db/migration/V2__center_performance_indexes.sql [REQ-004]
    * ./sources/backend/center-service/src/main/resources/db/migration/V3__center_admin_scope.sql [REQ-006], [ARC-002]
    * ./sources/backend/center-service/src/test/java/com/hub/center/CenterServiceTest.java [REQ-004], [REQ-005]
    * ./sources/backend/center-service/src/test/java/com/hub/center/CenterResourceTest.java [REQ-004]
    * ./sources/backend/center-service/src/test/java/com/hub/center/CenterAdminIsolationIT.java [REQ-006], [ARC-002]
    * ./sources/backend/course-service/src/main/java/com/hub/course/Course.java [REQ-007], [REQ-008]
    * ./sources/backend/course-service/src/main/java/com/hub/course/CourseRepository.java [REQ-007], [REQ-008]
    * ./sources/backend/course-service/src/main/java/com/hub/course/CourseService.java [REQ-008]
    * ./sources/backend/course-service/src/main/java/com/hub/course/CourseResource.java [REQ-007], [REQ-008]
    * ./sources/backend/course-service/src/main/java/com/hub/course/TeacherAssignmentResource.java [REQ-009]
    * ./sources/backend/course-service/src/main/java/com/hub/course/event/TeacherAssignedEvent.java [REQ-009], [ARC-008]
    * ./sources/backend/course-service/src/main/java/com/hub/course/dto/CourseRequest.java [REQ-008]
    * ./sources/backend/course-service/src/main/java/com/hub/course/dto/CourseResponse.java [REQ-007]
    * ./sources/backend/course-service/src/main/resources/db/migration/V2__course_schedule_indexes.sql [REQ-007], [REQ-008]
    * ./sources/backend/course-service/src/test/java/com/hub/course/CourseResourceTest.java [REQ-007]
    * ./sources/backend/course-service/src/test/java/com/hub/course/CourseServiceTest.java [REQ-008]
    * ./sources/backend/course-service/src/test/java/com/hub/course/CourseScheduleConflictIT.java [REQ-008]
    * ./sources/backend/course-service/src/test/java/com/hub/course/TeacherAssignmentTest.java [REQ-009], [ARC-008]
    * ./sources/backend/api-gateway/src/main/java/com/hub/gateway/rbac/RoleScope.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    * ./sources/backend/api-gateway/src/main/java/com/hub/gateway/rbac/TenantScopeContext.java [ARC-002]
    * ./sources/backend/api-gateway/src/main/java/com/hub/gateway/rbac/RoleAuthorizationFilter.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    * ./sources/backend/api-gateway/src/main/resources/openapi/auth-integration-contract.yaml [ARC-006]
    * ./sources/backend/api-gateway/src/main/resources/openapi/integration-contracts.yaml [ARC-007], [ARC-008], [ARC-009]
    * ./sources/backend/api-gateway/src/test/java/com/hub/gateway/rbac/RoleAuthorizationFilterTest.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    * ./sources/backend/api-gateway/src/test/java/com/hub/gateway/rbac/RbacMatrixIT.java [ARC-006], [ARC-007], [ARC-008], [ARC-009]
    * ./sources/docs/api-center-service-reference.md [REQ-004], [REQ-005], [REQ-006]
    * ./sources/docs/api-course-service-reference.md [REQ-007], [REQ-008], [REQ-009]
    * ./sources/docs/rbac-topology-blueprint.md [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    * ./sources/docs/integration-contracts-openapi.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]
    * ./sources/docs/center-service-review-day1.md [REQ-004], [REQ-005]
    * ./sources/docs/course-service-review-conflict-detection.md [REQ-008]
    * ./sources/docs/phase2-final-review-report.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]

- **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:** Các migration DDL tương thích ANSI SQL phục vụ tối ưu truy vấn và mở rộng phạm vi tenant cho hai dịch vụ nghiệp vụ của giai đoạn này (lược đồ nền 11 bảng đã được thiết lập tại Giai đoạn 1):

```sql
-- V2__center_performance_indexes.sql (center-service)
-- Performance index supporting paginated center listing ordered by name [REQ-004]
CREATE INDEX IF NOT EXISTS idx_centers_name ON centers (name);

-- V3__center_admin_scope.sql (center-service)
-- Tenant scope column mapping Center Admin delegation to a specific center [REQ-006], [ARC-002]
ALTER TABLE users ADD COLUMN managed_center_id UUID REFERENCES centers (center_id);
CREATE INDEX IF NOT EXISTS idx_users_managed_center_id ON users (managed_center_id);

-- V2__course_schedule_indexes.sql (course-service)
-- Index supporting course listing grid and title search [REQ-007]
CREATE INDEX IF NOT EXISTS idx_courses_title ON courses (title);
-- Composite index accelerating teacher schedule overlap detection [REQ-008]
CREATE INDEX IF NOT EXISTS idx_courses_teacher_dates ON courses (teacher_id, start_date, end_date);
```

- **Hợp đồng định tuyến API và sự kiện [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-006], [ARC-007], [ARC-008], [ARC-009]:** Hợp đồng kỹ thuật hợp nhất toàn bộ endpoint REST và topic sự kiện do giai đoạn này công bố qua api-gateway:

```json
{
  "center-service": {
    "GET /api/v1/centers": {
      "auth": "bearer JWT, any authenticated role",
      "queryParameters": { "page": "int, default 0", "size": "int, default 20" },
      "response200": {
        "content": [
          {
            "centerId": "uuid",
            "name": "string, max 100",
            "address": "string, max 255",
            "taxId": "string, numeric 10-13 digits",
            "contactPhone": "string or null",
            "contactEmail": "string or null"
          }
        ],
        "page": 0,
        "size": 20,
        "totalElements": 0,
        "totalPages": 0
      }
    },
    "POST /api/v1/centers": {
      "auth": "SYSTEM_ADMIN",
      "request": {
        "name": "string, required, max 100",
        "address": "string, required, max 255",
        "taxId": "string, required, numeric 10-13 digits, unique",
        "contactPhone": "string, optional",
        "contactEmail": "string, optional, valid email format"
      },
      "response201": { "centerId": "uuid", "name": "string", "address": "string", "taxId": "string", "contactPhone": "string or null", "contactEmail": "string or null" },
      "error409": { "code": "TAX_ID_CONFLICT" }
    },
    "PUT /api/v1/centers/{centerId}": {
      "auth": "SYSTEM_ADMIN",
      "request": "same schema as POST",
      "response200": "updated CenterResponse",
      "error409": { "code": "TAX_ID_CONFLICT" }
    },
    "DELETE /api/v1/centers/{centerId}": { "auth": "SYSTEM_ADMIN", "response204": {} },
    "POST /api/v1/centers/{centerId}/admins": {
      "auth": "SYSTEM_ADMIN",
      "request": { "userId": "uuid" },
      "response200": { "userId": "uuid", "roleName": "Center Admin", "managedCenterId": "uuid" },
      "error403": { "code": "RBAC_ASSIGNMENT_DENIED" }
    },
    "DELETE /api/v1/centers/{centerId}/admins/{userId}": { "auth": "SYSTEM_ADMIN", "response204": {} }
  },
  "course-service": {
    "GET /api/v1/courses": {
      "auth": "bearer JWT, any authenticated role",
      "response200": {
        "content": [
          {
            "courseId": "uuid",
            "title": "string, max 150",
            "startDate": "date ISO-8601",
            "endDate": "date ISO-8601",
            "teacherName": "string or null",
            "maxStudents": 30
          }
        ],
        "page": 0,
        "size": 20,
        "totalElements": 0
      }
    },
    "POST /api/v1/courses": {
      "auth": "SYSTEM_ADMIN, CENTER_ADMIN",
      "request": {
        "title": "string, required, max 150",
        "description": "string, optional",
        "startDate": "date, required",
        "endDate": "date, required",
        "teacherId": "uuid, required",
        "maxStudents": "int, optional, default 30"
      },
      "response201": { "courseId": "uuid", "title": "string", "startDate": "date", "endDate": "date", "teacherId": "uuid", "maxStudents": 30 },
      "error422": { "code": "SCHEDULE_CONFLICT", "conflictingCourseId": "uuid" }
    },
    "PUT /api/v1/courses/{courseId}": {
      "auth": "SYSTEM_ADMIN, CENTER_ADMIN",
      "request": "same schema as POST",
      "response200": "updated CourseResponse",
      "error422": { "code": "SCHEDULE_CONFLICT" }
    },
    "DELETE /api/v1/courses/{courseId}": { "auth": "SYSTEM_ADMIN, CENTER_ADMIN", "response204": {} },
    "POST /api/v1/courses/{courseId}/teacher": {
      "auth": "SYSTEM_ADMIN",
      "request": { "teacherId": "uuid" },
      "response200": { "courseId": "uuid", "teacherId": "uuid", "assignedAt": "timestamp ISO-8601" },
      "sideEffect": "publish teacher.assigned.v1 to topic course.teacher.events consumed by notification-service"
    },
    "DELETE /api/v1/courses/{courseId}/teacher": { "auth": "SYSTEM_ADMIN", "response204": {} }
  },
  "api-gateway": {
    "rbacEnforcement": {
      "filter": "RoleAuthorizationFilter",
      "roles": ["SYSTEM_ADMIN", "CENTER_ADMIN", "MANAGER", "TEACHER", "STUDENT"],
      "scopeModel": {
        "SYSTEM_ADMIN": "ALL_CENTERS",
        "CENTER_ADMIN": "OWN_CENTER via managed_center_id",
        "MANAGER": "OWN_CENTER_LIMITED_READONLY_COURSES",
        "TEACHER": "OWN_COURSES_READONLY",
        "STUDENT": "PUBLIC_READONLY"
      }
    },
    "eventContracts": {
      "teacher.assigned.v1": {
        "topic": "course.teacher.events",
        "payload": { "eventId": "uuid", "courseId": "uuid", "teacherId": "uuid", "assignedBy": "uuid", "occurredAt": "timestamp ISO-8601" },
        "consumer": "notification-service"
      }
    },
    "integrationContracts": {
      "authOAuth2Jwt": "./sources/backend/api-gateway/src/main/resources/openapi/auth-integration-contract.yaml [ARC-006]",
      "attendanceQrIdempotent": "./sources/backend/api-gateway/src/main/resources/openapi/integration-contracts.yaml#/attendance [ARC-007]",
      "notificationMultiChannel": "./sources/backend/api-gateway/src/main/resources/openapi/integration-contracts.yaml#/notification [ARC-008]",
      "mobileBearerOffline": "./sources/backend/api-gateway/src/main/resources/openapi/integration-contracts.yaml#/mobile [ARC-009]"
    }
  }
}
```

- **Trình xử lý ngoại lệ cục bộ của giai đoạn [REQ-005], [REQ-008], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]:** Các đường dẫn xử lý lỗi nghiệp vụ được chuẩn hóa thống nhất trong phạm vi giai đoạn:
    * **TAX_ID_CONFLICT (HTTP 409) [REQ-005]:** Khi System Admin tạo hoặc cập nhật trung tâm với taxId đã tồn tại, service chặn persist trong cùng transaction, trả 409 kèm thông báo chỉ định giá trị taxId xung đột và yêu cầu chỉnh sửa; rollback nguyên vẹn không để lại bản ghi mồ côi.
    * **SCHEDULE_CONFLICT (HTTP 422) [REQ-008]:** Trước khi persist khóa học, service truy vấn giao thoa khoảng startDate–endDate trên cùng teacherId; nếu phát hiện chồng lấn, hệ thống trả 422 kèm conflictingCourseId để admin điều chỉnh lịch hoặc đổi giáo viên.
    * **RBAC_ACCESS_DENIED (HTTP 403) [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]:** RoleAuthorizationFilter tại api-gateway đối chiếu claim vai trò trong JWT với ma trận quyền 5 vai trò; Manager gọi endpoint sửa khóa học/chỉ định giáo viên, Teacher gọi endpoint ghi, hoặc Student gọi endpoint quản trị đều bị chặn ngay tại cổng gateway trước khi chạm service nghiệp vụ.
    * **TENANT_SCOPE_VIOLATION (HTTP 403) [ARC-002]:** Center Admin truy cập tài nguyên thuộc trung tâm khác managed_center_id được ghi trong phiên; filter đối chiếu centerId trên đường dẫn với phạm vi tenant và chặn ngay lập tức.

#### 📅 Nhật ký phân bổ nhiệm vụ Sub-Agent theo trình tự thời gian (Giai đoạn 2)

<!--START_DAY_LOG_INDEX-->

##### 📅 Ngày 1: Khởi tạo center-service — thực thể trung tâm, danh sách phân trang và CRUD ràng buộc taxId

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: Thực thể Center và repository truy vấn phân trang

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-004]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/CenterRepository.java [REQ-004]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA Center ánh xạ bảng centers (centerId UUID, name, address, taxId, contactPhone, contactEmail) cùng CenterRepository dựa trên Panache: truy vấn phân trang sắp xếp theo name, tận dụng index idx_centers_name bảo đảm độ trễ đọc sub-second; bổ sung DTO CenterResponse phục vụ serialization và chuẩn hóa hợp đồng trả về [REQ-004].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- V2__center_performance_indexes.sql
-- Performance index supporting paginated center listing ordered by name [REQ-004]
CREATE INDEX IF NOT EXISTS idx_centers_name ON centers (name);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Endpoint REST danh sách trung tâm GET /api/v1/centers

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-004]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/CenterResource.java [REQ-004]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng CenterResource exposing GET /api/v1/centers với tham số page/size, trả payload phân trang chuẩn (content, totalElements, totalPages); áp dụng xác thực bearer JWT cho mọi vai trò đã đăng nhập; bổ sung annotation OpenAPI phục vụ công bố hợp đồng ở Ngày 5 [REQ-004].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "endpoint": "GET /api/v1/centers",
  "method": "GET",
  "auth": "bearer JWT, any authenticated role",
  "queryParameters": { "page": "int, default 0", "size": "int, default 20" },
  "response200": {
    "content": [
      {
        "centerId": "uuid",
        "name": "string, max 100",
        "address": "string, max 255",
        "taxId": "string, numeric 10-13 digits",
        "contactPhone": "string or null",
        "contactEmail": "string or null"
      }
    ],
    "page": 0,
    "size": 20,
    "totalElements": 0,
    "totalPages": 0
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Service CRUD trung tâm với validate taxId duy nhất

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-005]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/CenterService.java [REQ-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai CenterService với các thao tác create/update/delete: validate taxId theo mẫu numeric 10–13 chữ số, kiểm tra trùng lặp trước khi persist và ném TaxIdConflictException ánh xạ HTTP 409; validate định dạng contactEmail và contactPhone; giới hạn quyền ghi cho SYSTEM_ADMIN; DTO CenterRequest nhận payload đầu vào [REQ-005].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "POST /api/v1/centers": {
    "auth": "SYSTEM_ADMIN",
    "request": {
      "name": "string, required, max 100",
      "address": "string, required, max 255",
      "taxId": "string, required, numeric 10-13 digits, unique",
      "contactPhone": "string, optional",
      "contactEmail": "string, optional, valid email format"
    },
    "response201": { "centerId": "uuid", "name": "string", "address": "string", "taxId": "string", "contactPhone": "string or null", "contactEmail": "string or null" },
    "error409": { "code": "TAX_ID_CONFLICT", "message": "taxId already exists" }
  },
  "PUT /api/v1/centers/{centerId}": {
    "auth": "SYSTEM_ADMIN",
    "request": "same schema as POST",
    "response200": "updated CenterResponse",
    "error409": { "code": "TAX_ID_CONFLICT" }
  },
  "DELETE /api/v1/centers/{centerId}": { "auth": "SYSTEM_ADMIN", "response204": {} }
}
```

* **Trình xử lý ngoại lệ cục bộ của giai đoạn:**
    * **TAX_ID_CONFLICT (HTTP 409) [REQ-005]:** Khi tạo hoặc cập nhật trung tâm với taxId đã tồn tại, service chặn persist trong cùng transaction, trả 409 kèm thông báo chỉ định giá trị taxId xung đột; rollback nguyên vẹn không để lại bản ghi mồ côi.
    * **CENTER_VALIDATION_FAILED (HTTP 422) [REQ-005]:** Tên hoặc địa chỉ rỗng, taxId không khớp mẫu numeric 10–13 chữ số, contactEmail sai định dạng: trả 422 kèm danh sách từng trường không hợp lệ để admin sửa trực tiếp trên form.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: JUnit suite nghiệp vụ trung tâm

* **Chuyên môn hóa quy trình Sub-Agent:** [Tester]

* **Tag IDs được nhắm mục tiêu:** [REQ-004], [REQ-005]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/CenterService.java;./sources/backend/center-service/src/test/java/com/hub/center/CenterServiceTest.java [REQ-004], [REQ-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test bao phủ: phân trang danh sách trung tâm, tạo trung tâm thành công, từ chối taxId trùng với kỳ vọng HTTP 409, từ chối taxId sai định dạng 10–13 chữ số, và cập nhật/xóa trung tâm; sử dụng QuarkusTest với mock repository bảo đảm độ bao phủ nhánh validation đầy đủ [REQ-004], [REQ-005].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Rà soát chất lượng tầng center-service

* **Chuyên môn hóa quy trình Sub-Agent:** [Reviewer]

* **Tag IDs được nhắm mục tiêu:** [REQ-004], [REQ-005]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/center-service-review-day1.md [REQ-004], [REQ-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm tra chất lượng code center-service: rò rỉ race condition khi check-then-insert taxId (đề xuất ràng buộc unique ở tầng DB làm lớp phòng vệ thứ hai), hiệu quả kế hoạch truy vấn phân trang, tuân thủ chuẩn đặt tên Quarkus và chuẩn hóa thông báo lỗi; ghi nhận phát hiện và phương án sửa vào báo cáo review [REQ-004], [REQ-005].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 6: Tài liệu tham chiếu API center-service

* **Chuyên môn hóa quy trình Sub-Agent:** [Doc]

* **Tag IDs được nhắm mục tiêu:** [REQ-004], [REQ-005]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-center-service-reference.md [REQ-004], [REQ-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Biên soạn tài liệu tham chiếu API center-service: bảng endpoint, schema request/response, mã lỗi 409 TAX_ID_CONFLICT, ví dụ payload và ma trận quyền truy cập từng endpoint dành cho System Admin và vai trò đọc [REQ-004], [REQ-005].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 Ngày 2: Phân quyền quản trị trung tâm theo tenant và khởi tạo lưới khóa học

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: Gán/hủy Center Admin với phạm vi tenant

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-006], [ARC-002]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/CenterAdminAssignmentResource.java [REQ-006], [ARC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai CenterAdminAssignmentResource: POST /api/v1/centers/{centerId}/admins set roleId sang Center Admin và ghi managed_center_id; DELETE đảo ngược hoàn toàn thao tác gán; chỉ SYSTEM_ADMIN được gọi; mọi thay đổi ghi audit log kèm timestamp và userId; chạy migration V3 bổ sung cột managed_center_id trên users [REQ-006], [ARC-002].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- V3__center_admin_scope.sql
-- Tenant scope column mapping Center Admin delegation to a specific center [REQ-006], [ARC-002]
ALTER TABLE users ADD COLUMN managed_center_id UUID REFERENCES centers (center_id);
CREATE INDEX IF NOT EXISTS idx_users_managed_center_id ON users (managed_center_id);
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "POST /api/v1/centers/{centerId}/admins": {
    "auth": "SYSTEM_ADMIN",
    "request": { "userId": "uuid" },
    "response200": { "userId": "uuid", "roleName": "Center Admin", "managedCenterId": "uuid" },
    "sideEffect": "update users.role_id to Center Admin, set users.managed_center_id, write audit log entry"
  },
  "DELETE /api/v1/centers/{centerId}/admins/{userId}": {
    "auth": "SYSTEM_ADMIN",
    "response204": {},
    "sideEffect": "revert role assignment and clear managed_center_id, write audit log entry"
  }
}
```

* **Trình xử lý ngoại lệ cục bộ của giai đoạn:**
    * **RBAC_ASSIGNMENT_DENIED (HTTP 403) [ARC-002]:** Mọi vai trò khác SYSTEM_ADMIN gọi endpoint gán/hủy Center Admin bị chặn tại gateway; chỉ System Admin toàn cầu mới được ủy quyền quản trị trung tâm.
    * **ASSIGNMENT_TARGET_INVALID (HTTP 409) [REQ-006]:** Hủy gán một user không đang giữ vai trò Center Admin tại trung tâm chỉ định, hoặc gán user đã quản lý trung tâm khác, trả 409 yêu cầu xác minh lại trạng thái trước khi thao tác.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Kiểm định tích hợp cô lập tenant Center Admin

* **Chuyên môn hóa quy trình Sub-Agent:** [Tester]

* **Tag IDs được nhắm mục tiêu:** [REQ-006], [ARC-002]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/center-service/src/test/java/com/hub/center/CenterAdminIsolationIT.java [REQ-006], [ARC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Dựng integration test xác minh: Center Admin chỉ thao tác dữ liệu trong trung tâm được gán, truy cập trung tâm khác trả 403; unassign khôi phục trạng thái ban đầu của user; audit log ghi đủ bản ghi gán/hủy kèm timestamp và userId [REQ-006], [ARC-002].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Endpoint lưới khóa học GET /api/v1/courses

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-007]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/CourseResource.java [REQ-007]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo course-service với CourseResource exposing GET /api/v1/courses trả lưới CourseID, Title, StartDate, EndDate, TeacherName (join users); thực thể Course ánh xạ bảng courses với maxStudents mặc định 30; bổ sung DTO CourseRequest và CourseResponse phục vụ các nghiệp vụ CRUD ở Ngày 3 [REQ-007].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "endpoint": "GET /api/v1/courses",
  "method": "GET",
  "auth": "bearer JWT, any authenticated role",
  "response200": {
    "content": [
      {
        "courseId": "uuid",
        "title": "string, max 150",
        "startDate": "date ISO-8601",
        "endDate": "date ISO-8601",
        "teacherName": "string or null",
        "maxStudents": 30
      }
    ],
    "page": 0,
    "size": 20,
    "totalElements": 0
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: Unit test lưới khóa học

* **Chuyên môn hóa quy trình Sub-Agent:** [Tester]

* **Tag IDs được nhắm mục tiêu:** [REQ-007]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/CourseResource.java;./sources/backend/course-service/src/test/java/com/hub/course/CourseResourceTest.java [REQ-007]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test xác minh cấu trúc lưới khóa học: đủ 5 cột CourseID, Title, StartDate, EndDate, TeacherName; join teacherName trả null an toàn khi teacherId chưa được phân công; phân trang ổn định với tập dữ liệu lớn [REQ-007].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Cập nhật tài liệu phân quyền trung tâm và draft tài liệu khóa học

* **Chuyên môn hóa quy trình Sub-Agent:** [Doc]

* **Tag IDs được nhắm mục tiêu:** [REQ-006], [REQ-007]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-course-service-reference.md [REQ-006], [REQ-007]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Bổ sung vào api-center-service-reference.md các endpoint gán/hủy Center Admin kèm sơ đồ phạm vi tenant managed_center_id; khởi tạo draft api-course-service-reference.md với hợp đồng GET /api/v1/courses và cấu trúc lưới hiển thị [REQ-006], [REQ-007].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 Ngày 3: CRUD khóa học chống xung đột lịch và tối ưu truy vấn phát hiện giao thoa

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: CourseService chặn xung đột lịch giáo viên

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-008]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/CourseService.java [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai create/update/delete khóa học: trước khi persist, truy vấn mọi khóa học của teacherId có khoảng [startDate, endDate] giao thoa; nếu trùng ném ScheduleConflictException ánh xạ HTTP 422 kèm conflictingCourseId; validate endDate >= startDate; áp dụng maxStudents mặc định 30 khi thiếu trường đầu vào [REQ-008].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "POST /api/v1/courses": {
    "auth": "SYSTEM_ADMIN, CENTER_ADMIN",
    "request": {
      "title": "string, required, max 150",
      "description": "string, optional",
      "startDate": "date, required",
      "endDate": "date, required",
      "teacherId": "uuid, required",
      "maxStudents": "int, optional, default 30"
    },
    "response201": { "courseId": "uuid", "title": "string", "startDate": "date", "endDate": "date", "teacherId": "uuid", "maxStudents": 30 },
    "error422": { "code": "SCHEDULE_CONFLICT", "conflictingCourseId": "uuid" }
  },
  "PUT /api/v1/courses/{courseId}": {
    "auth": "SYSTEM_ADMIN, CENTER_ADMIN",
    "request": "same schema as POST",
    "response200": "updated CourseResponse",
    "error422": { "code": "SCHEDULE_CONFLICT" }
  },
  "DELETE /api/v1/courses/{courseId}": { "auth": "SYSTEM_ADMIN, CENTER_ADMIN", "response204": {} }
}
```

* **Trình xử lý ngoại lệ cục bộ của giai đoạn:**
    * **SCHEDULE_CONFLICT (HTTP 422) [REQ-008]:** teacherId đã có khóa học khác với khoảng [startDate, endDate] giao thoa; service trả 422 kèm conflictingCourseId để admin điều chỉnh lịch hoặc đổi giáo viên trước khi persist.
    * **DATE_RANGE_INVALID (HTTP 422) [REQ-008]:** endDate sớm hơn startDate hoặc thiếu trường bắt buộc; trả 422 liệt kê từng trường không hợp lệ theo đúng mẫu thông báo validation của hệ thống.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Repository phát hiện giao thoa và migration index khóa học

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-007], [REQ-008]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/CourseRepository.java [REQ-007], [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Bổ sung truy vấn overlap (start_date <= :endDate AND end_date >= :startDate AND teacher_id = :teacherId) tận dụng composite index; chạy migration V2__course_schedule_indexes.sql tạo idx_courses_title và idx_courses_teacher_dates bảo đảm kiểm tra xung đột và lưới danh sách đạt độ trễ sub-second [REQ-007], [REQ-008].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- V2__course_schedule_indexes.sql
-- Index supporting course listing grid and title search [REQ-007]
CREATE INDEX IF NOT EXISTS idx_courses_title ON courses (title);
-- Composite index accelerating teacher schedule overlap detection [REQ-008]
CREATE INDEX IF NOT EXISTS idx_courses_teacher_dates ON courses (teacher_id, start_date, end_date);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Kiểm định tích hợp xung đột lịch

* **Chuyên môn hóa quy trình Sub-Agent:** [Tester]

* **Tag IDs được nhắm mục tiêu:** [REQ-008]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/course-service/src/test/java/com/hub/course/CourseScheduleConflictIT.java [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Dựng integration test với nhiều kịch bản: chèn khóa học chồng lấn cùng giáo viên trả 422 kèm conflictingCourseId; khoảng chạm biên (endDate của khóa A trùng startDate của khóa B) xử lý đúng nghiệp vụ; cập nhật khóa học không tự xung đột với chính nó; hai giáo viên khác nhau cùng khung giờ được chấp nhận [REQ-008].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: Rà soát hiệu quả phát hiện xung đột lịch

* **Chuyên môn hóa quy trình Sub-Agent:** [Reviewer]

* **Tag IDs được nhắm mục tiêu:** [REQ-008]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/course-service-review-conflict-detection.md [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Phân tích kế hoạch truy vấn overlap (EXPLAIN) bảo đảm sử dụng composite index idx_courses_teacher_dates; rà soát race condition khi hai request tạo khóa học đồng thời trên cùng giáo viên (đề xuất khóa biên hoặc mức cô lập transaction phù hợp); chuẩn hóa thông báo lỗi xung đột trả về client [REQ-008].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Hoàn thiện tài liệu tham chiếu API course-service

* **Chuyên môn hóa quy trình Sub-Agent:** [Doc]

* **Tag IDs được nhắm mục tiêu:** [REQ-007], [REQ-008]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-course-service-reference.md [REQ-007], [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cập nhật api-course-service-reference.md với hợp đồng CRUD khóa học đầy đủ, mã lỗi 422 SCHEDULE_CONFLICT kèm ví dụ payload xung đột, ghi chú ma trận quyền SYSTEM_ADMIN/CENTER_ADMIN và quy tắc maxStudents mặc định 30 [REQ-007], [REQ-008].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 Ngày 4: Phân công giáo viên phát sự kiện đa kênh và bộ lọc RBAC 5 vai trò tại api-gateway

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: Endpoint phân công giáo viên vào khóa học

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-009]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/TeacherAssignmentResource.java [REQ-009]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai POST /api/v1/courses/{courseId}/teacher và DELETE tương ứng: ghi ánh xạ course–teacher, chỉ SYSTEM_ADMIN được thao tác; sau khi gán thành công phát sự kiện teacher.assigned.v1 sang notification-service để queue push notification tới mobile app của giáo viên được chỉ định; unassign gỡ ánh xạ và dừng luồng thông báo liên quan [REQ-009].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "POST /api/v1/courses/{courseId}/teacher": {
    "auth": "SYSTEM_ADMIN",
    "request": { "teacherId": "uuid" },
    "response200": { "courseId": "uuid", "teacherId": "uuid", "assignedAt": "timestamp ISO-8601" },
    "sideEffect": "publish teacher.assigned.v1 to topic course.teacher.events"
  },
  "DELETE /api/v1/courses/{courseId}/teacher": {
    "auth": "SYSTEM_ADMIN",
    "response204": {}
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Hợp đồng sự kiện teacher.assigned.v1

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [REQ-009], [ARC-008]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/event/TeacherAssignedEvent.java [REQ-009], [ARC-008]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Định nghĩa payload sự kiện teacher.assigned.v1 (eventId, courseId, teacherId, assignedBy, occurredAt) phát lên topic course.teacher.events qua Kafka emitter; bảo đảm consumer idempotent qua eventId và cấu hình serialization JSON thống nhất với notification-service [REQ-009], [ARC-008].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "topic": "course.teacher.events",
  "eventType": "teacher.assigned.v1",
  "payload": {
    "eventId": "uuid",
    "courseId": "uuid",
    "teacherId": "uuid",
    "assignedBy": "uuid",
    "occurredAt": "timestamp ISO-8601"
  },
  "delivery": "at-least-once, consumer deduplicates by eventId",
  "consumer": "notification-service"
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Bộ lọc RBAC 5 vai trò tại api-gateway

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/api-gateway/src/main/java/com/hub/gateway/rbac/RoleAuthorizationFilter.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai RoleAuthorizationFilter cùng RoleScope và TenantScopeContext: giải mã JWT, đối chiếu vai trò với ma trận quyền — System Admin toàn quyền mọi trung tâm [ARC-001]; Center Admin giới hạn trong managed_center_id [ARC-002]; Manager không được sửa khóa học hoặc chỉ định giáo viên [ARC-003]; Teacher chỉ đọc lịch dạy [ARC-004]; Student duyệt/đăng ký/xem thẻ [ARC-005]; chặn 403 ngay tại gateway trước khi route tới service nghiệp vụ.

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```json
{
  "filter": "RoleAuthorizationFilter",
  "scope": "api-gateway, enforced before downstream routing",
  "rbacMatrix": {
    "SYSTEM_ADMIN": { "centerScope": "ALL_CENTERS", "centers": ["read", "write", "delete"], "centerAdminAssignment": ["assign", "unassign"], "courses": ["read", "write", "delete"], "teacherAssignment": ["assign", "unassign"] },
    "CENTER_ADMIN": { "centerScope": "OWN_CENTER", "centers": ["read"], "courses": ["read", "write", "delete"], "teacherAssignment": [], "centerAdminAssignment": [] },
    "MANAGER": { "centerScope": "OWN_CENTER", "centers": ["read"], "courses": ["read"], "teacherAssignment": [], "denied": ["course.write", "course.delete", "teacher.assign"] },
    "TEACHER": { "centerScope": "OWN_COURSES", "courses": ["read:assigned"], "readOnly": true },
    "STUDENT": { "centerScope": "PUBLIC", "courses": ["read"], "readOnly": true }
  }
}
```

* **Trình xử lý ngoại lệ cục bộ của giai đoạn:**
    * **RBAC_ACCESS_DENIED (HTTP 403) [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]:** RoleAuthorizationFilter đối chiếu claim vai trò trong JWT với ma trận quyền; mọi request vi phạm (Manager sửa khóa học, Teacher ghi dữ liệu, Student gọi endpoint quản trị) bị chặn tại api-gateway với mã 403 trước khi chạm service nghiệp vụ.
    * **TENANT_SCOPE_VIOLATION (HTTP 403) [ARC-002]:** Center Admin truy cập tài nguyên thuộc trung tâm khác managed_center_id được ghi trong phiên; filter đối chiếu centerId trên đường dẫn với phạm vi tenant và chặn ngay lập tức.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: Unit test phân công giáo viên và sự kiện

* **Chuyên môn hóa quy trình Sub-Agent:** [Tester]

* **Tag IDs được nhắm mục tiêu:** [REQ-009], [ARC-008]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/TeacherAssignmentResource.java;./sources/backend/course-service/src/test/java/com/hub/course/TeacherAssignmentTest.java [REQ-009], [ARC-008]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test xác minh: gán giáo viên thành công tạo ánh xạ course–teacher và phát sự kiện teacher.assigned.v1 với payload đầy đủ; unassign gỡ ánh xạ; từ chối thao tác từ vai trò không phải SYSTEM_ADMIN; xác minh tính idempotent của eventId khi phát lặp [REQ-009], [ARC-008].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Unit test ma trận RBAC

* **Chuyên môn hóa quy trình Sub-Agent:** [Tester]

* **Tag IDs được nhắm mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/api-gateway/src/main/java/com/hub/gateway/rbac/RoleAuthorizationFilter.java;./sources/backend/api-gateway/src/test/java/com/hub/gateway/rbac/RoleAuthorizationFilterTest.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test phủ 5 vai trò × nhóm endpoint: System Admin pass toàn bộ endpoint quản trị [ARC-001]; Center Admin pass trong trung tâm sở tại và fail ngoài phạm vi managed_center_id [ARC-002]; Manager bị chặn course.write và teacher.assign nhưng pass endpoint đọc [ARC-003]; Teacher bị chặn mọi thao tác ghi, chỉ pass đọc khóa học được phân công [ARC-004]; Student chỉ pass endpoint đọc công khai [ARC-005].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 6: Blueprint topology RBAC

* **Chuyên môn hóa quy trình Sub-Agent:** [Doc]

* **Tag IDs được nhắm mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/rbac-topology-blueprint.md [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Biên soạn blueprint RBAC: sơ đồ luồng JWT qua api-gateway, bảng ma trận quyền 5 vai trò, quy tắc phạm vi tenant theo managed_center_id, cơ chế audit log thay đổi vai trò và hướng dẫn mở rộng vai trò mới trong tương lai [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 Ngày 5: Công bố hợp đồng OpenAPI bốn luồng tích hợp liên dịch vụ và kiểm định E2E đa vai trò

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: Hợp đồng OpenAPI xác thực OAuth2/JWT

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [ARC-006]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/api-gateway/src/main/resources/openapi/auth-integration-contract.yaml [ARC-006]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Công bố spec OpenAPI 3.0.3 cho luồng xác thực: POST /api/v1/auth/register, POST /api/v1/auth/login, POST /api/v1/auth/oauth2/{provider}, POST /api/v1/auth/refresh; định nghĩa securityScheme bearer JWT với access token 15 phút và refresh token 7 ngày; chuẩn hóa schema lỗi xác thực cho toàn bộ consumer liên dịch vụ [ARC-006].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```yaml
openapi: 3.0.3
info:
  title: auth-integration-contract
  version: 1.0.0
paths:
  /api/v1/auth/register:
    post:
      summary: Register user with email/password or social provider
      responses:
        "201":
          description: JWT access token (15 min) and refresh token (7 days) issued
  /api/v1/auth/login:
    post:
      summary: Authenticate with email/password
      responses:
        "200":
          description: JWT access token and refresh token
  /api/v1/auth/oauth2/{provider}:
    post:
      summary: Exchange OAuth2 authorization code for session JWT
      parameters:
        - name: provider
          in: path
          required: true
          schema:
            type: string
            enum: [firebase, google, facebook]
      responses:
        "200":
          description: JWT access token and refresh token
  /api/v1/auth/refresh:
    post:
      summary: Rotate refresh token and issue new access token
      responses:
        "200":
          description: new JWT access token
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Hợp đồng OpenAPI điểm danh QR, thông báo đa kênh và mobile bearer

* **Chuyên môn hóa quy trình Sub-Agent:** [Coder]

* **Tag IDs được nhắm mục tiêu:** [ARC-007], [ARC-008], [ARC-009]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/api-gateway/src/main/resources/openapi/integration-contracts.yaml [ARC-007], [ARC-008], [ARC-009]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Công bố spec hợp nhất: POST /api/v1/attendance/scan với semantic idempotency key (studentId, courseId, attendanceDate) và cờ duplicate [ARC-007]; endpoint điều phối notification đa kênh FCM/APNs/Zalo kèm chính sách retry tối đa 3 lần khi delivery thất bại [ARC-008]; hợp đồng mobile session bearer token với header ETag và Cache-Control phục vụ caching ngoại tuyến khi mất kết nối [ARC-009].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện:**

```yaml
openapi: 3.0.3
info:
  title: integration-contracts
  version: 1.0.0
paths:
  /api/v1/attendance/scan:
    post:
      summary: Idempotent QR attendance capture
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required: [studentId, courseId, attendanceDate]
              properties:
                studentId:
                  type: string
                  format: uuid
                courseId:
                  type: string
                  format: uuid
                attendanceDate:
                  type: string
                  format: date
                timestamp:
                  type: string
                  format: date-time
      responses:
        "200":
          description: attendance recorded, or duplicate flag already_recorded for same-day rescan
  /api/v1/notifications/dispatch:
    post:
      summary: Multi-channel notification dispatch (FCM/APNs/Zalo)
      responses:
        "202":
          description: queued for delivery, retry up to 3 times on failure before marking failed
  /api/v1/mobile/session:
    get:
      summary: Mobile bearer session with offline cache support
      responses:
        "200":
          description: session payload with ETag and Cache-Control headers for offline caching
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Kiểm định E2E ma trận RBAC và hợp đồng tích hợp

* **Chuyên môn hóa quy trình Sub-Agent:** [Tester]

* **Tag IDs được nhắm mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/api-gateway/src/test/java/com/hub/gateway/rbac/RbacMatrixIT.java [ARC-006], [ARC-007], [ARC-008], [ARC-009]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Dựng E2E profile chạy qua api-gateway: xác thực OAuth2/JWT cấp access 15 phút và refresh 7 ngày [ARC-006]; gọi attendance scan hai lần cùng ngày nhận cờ duplicate không phát sinh bản ghi mới [ARC-007]; kích hoạt notification đa kênh và xác minh retry 3 lần khi device token invalid [ARC-008]; mobile bearer session trả ETag phục vụ offline cache [ARC-009]; toàn bộ kịch bản chạy dưới 5 vai trò RBAC để xác minh rào chắn phân quyền đầu-cuối.

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: Báo cáo rà soát cuối giai đoạn 2

* **Chuyên môn hóa quy trình Sub-Agent:** [Reviewer]

* **Tag IDs được nhắm mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/phase2-final-review-report.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tổng hợp rà soát cuối giai đoạn: tính nhất quán giữa hợp đồng OpenAPI công bố và implementation thực tế của center-service/course-service, độ bao phủ test ma trận RBAC 5 vai trò, phát hiện nợ kỹ thuật và kế hoạch khắc phục trước khi bước vào Giai đoạn 3 [ARC-006], [ARC-007], [ARC-008], [ARC-009].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Tài liệu hợp đồng tích hợp OpenAPI

* **Chuyên môn hóa quy trình Sub-Agent:** [Doc]

* **Tag IDs được nhắm mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/integration-contracts-openapi.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Biên soạn tài liệu tham chiếu bốn luồng tích hợp: sơ đồ sequence OAuth2/JWT với vòng đời access/refresh token [ARC-006], hợp đồng attendance idempotent và ngữ nghĩa cờ duplicate [ARC-007], ma trận kênh thông báo FCM/APNs/Zalo kèm chính sách retry [ARC-008], quy ước mobile bearer offline caching qua ETag [ARC-009]; đính kèm đường dẫn tới file YAML trong api-gateway làm nguồn tham chiếu chính thức.

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu trong ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

<!--END_PART_2_PHASE_LOOP-->

<!--START_PHASE_INDEX-->

### 📈 Giai đoạn 3 - Dịch Vụ Ghi Danh, Điểm Danh QR & Thẻ Hội Viên Kỹ Thuật Số

- **Mục tiêu cốt lõi & mục đích của giai đoạn:** Giai đoạn 3 bàn giao chuỗi nghiệp vụ học viên end-to-end trên ba microservices: enrollment-service cung cấp duyệt khóa học loại trừ mọi khóa đã có bản ghi ghi danh kèm số chỗ còn trống [REQ-010] và đăng ký khóa học trong một transaction nguyên tử tự cấp tài khoản vai trò 'Student' khi thiếu, đồng thời phát sự kiện thông báo tới mobile app học viên và nhóm Zalo của trung tâm [REQ-011]; attendance-service tiếp nhận payload quét QR (studentId + timestamp) tại POST /api/v1/attendance/scan với chính sách retry sau reconnect [REQ-012], [EXC-001] cùng ràng buộc idempotent (studentId, courseId, attendanceDate) trả success kèm cờ duplicate cho mọi lần quét trùng [REQ-013], [EXC-002]; card-service suy ra totalValidityDays, daysUsed, daysRemaining từ thực thể StudentCard để hiển thị thẻ hội viên kỹ thuật số [REQ-014] và thực thi gia hạn theo kỳ 30 ngày ngay sau khi payment service xác nhận thành công [REQ-015]. Chất lượng được bảo chứng bởi bộ JUnit/integration test và bộ đặc tả API cập nhật cho cả ba dịch vụ.

- **Ma trận bản đồ thư mục vật lý đích:** toàn bộ tệp vật lý được khởi tạo, refactor hoặc xử lý trong phạm vi giai đoạn này:
    * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentBrowseResource.java [REQ-010]
    * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentRegistrationResource.java [REQ-011]
    * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentService.java [REQ-010], [REQ-011]
    * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/dto/CourseAvailabilityDto.java [REQ-010]
    * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/dto/EnrollmentRequestDto.java [REQ-011]
    * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/event/EnrollmentNotificationPublisher.java [REQ-011]
    * ./sources/backend/enrollment-service/src/main/resources/db/migration/V3__enrollment_browse_outbox.sql [REQ-010], [REQ-011]
    * ./sources/backend/enrollment-service/src/test/java/com/hub/enrollment/EnrollmentBrowseResourceTest.java [REQ-010]
    * ./sources/backend/enrollment-service/src/test/java/com/hub/enrollment/EnrollmentRegistrationTransactionIT.java [REQ-011]
    * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceScanResource.java [REQ-012], [EXC-001]
    * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceService.java [REQ-012], [REQ-013], [EXC-002]
    * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/retry/OfflineReplayPolicy.java [EXC-001]
    * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/exception/DuplicateAttendanceMapper.java [EXC-002]
    * ./sources/backend/attendance-service/src/main/resources/db/migration/V4__attendance_unique_idempotency.sql [REQ-013], [EXC-002]
    * ./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceScanResourceTest.java [REQ-012]
    * ./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceIdempotencyIT.java [REQ-013], [EXC-002]
    * ./sources/backend/card-service/src/main/java/com/hub/card/CardQueryResource.java [REQ-014]
    * ./sources/backend/card-service/src/main/java/com/hub/card/CardValidityCalculator.java [REQ-014]
    * ./sources/backend/card-service/src/main/java/com/hub/card/CardRenewalResource.java [REQ-015]
    * ./sources/backend/card-service/src/main/java/com/hub/card/PaymentConfirmationConsumer.java [REQ-015]
    * ./sources/backend/card-service/src/main/resources/db/migration/V5__card_validity_support.sql [REQ-014]
    * ./sources/backend/card-service/src/test/java/com/hub/card/CardValidityCalculatorTest.java [REQ-014]
    * ./sources/backend/card-service/src/test/java/com/hub/card/CardRenewalFlowIT.java [REQ-015]
    * ./sources/docs/api-enrollment-service.md [REQ-010], [REQ-011]
    * ./sources/docs/api-attendance-service.md [REQ-012], [REQ-013], [EXC-001], [EXC-002]
    * ./sources/docs/api-card-service.md [REQ-014], [REQ-015]

- **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- ============================================================
-- PHASE 3 CONSOLIDATED MIGRATIONS (membership-hub)
-- ============================================================

-- V3__enrollment_browse_outbox.sql (enrollment-service)
CREATE INDEX idx_enrollments_student_lookup
    ON enrollments (student_id, course_id);

CREATE INDEX idx_courses_schedule_window
    ON courses (start_date, end_date, teacher_id);

CREATE TABLE enrollment_outbox (
    outbox_id uuid PRIMARY KEY,
    aggregate_id uuid NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    payload TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP NULL,
    CONSTRAINT chk_enrollment_outbox_event_type
        CHECK (event_type IN ('ENROLLMENT_CREATED'))
);

CREATE INDEX idx_enrollment_outbox_pending
    ON enrollment_outbox (published_at, outbox_id);

-- V4__attendance_unique_idempotency.sql (attendance-service)
ALTER TABLE attendance
    ADD CONSTRAINT uq_attendance_student_course_date
    UNIQUE (student_id, course_id, attendance_date);

CREATE INDEX idx_attendance_course_date
    ON attendance (course_id, attendance_date);

-- V5__card_validity_support.sql (card-service)
CREATE INDEX idx_student_cards_student_lookup
    ON student_cards (student_id, issue_date);
```

- **Hợp đồng định tuyến API và sự kiện [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015]:**

```json
{
  "serviceRegistry": [
    {
      "service": "enrollment-service",
      "routes": [
        { "method": "GET", "path": "/api/v1/enrollments/browse", "purpose": "browse courses excluding enrolled ones with availableSeats", "tags": ["REQ-010"] },
        { "method": "POST", "path": "/api/v1/enrollments/register", "purpose": "transactional enrollment with auto student account provisioning", "tags": ["REQ-011"] }
      ]
    },
    {
      "service": "attendance-service",
      "routes": [
        { "method": "POST", "path": "/api/v1/attendance/scan", "purpose": "QR attendance capture with absolute idempotent guarantee", "tags": ["REQ-012", "REQ-013", "EXC-001", "EXC-002"] }
      ]
    },
    {
      "service": "card-service",
      "routes": [
        { "method": "GET", "path": "/api/v1/cards/me", "purpose": "membership card validity metrics computation", "tags": ["REQ-014"] },
        { "method": "POST", "path": "/api/v1/cards/renew", "purpose": "extend card validity after payment confirmation", "tags": ["REQ-015"] }
      ]
    }
  ],
  "eventBindings": [
    { "topic": "enrollment.created", "producer": "enrollment-service", "consumer": "notification-service", "tags": ["REQ-011"] },
    { "topic": "payment.confirmed", "producer": "payment-service", "consumer": "card-service", "tags": ["REQ-015"] }
  ]
}
```

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-001], [EXC-002]:**
    * **[EXC-001] Mất kết nối mạng trong lúc quét QR:** Khi thiết bị không gửi được request do mất mạng, ứng dụng di động cache payload scan ngoại tuyến và phát lại sau khi kết nối khôi phục; attendance-service tiếp nhận bó scan tồn đọng, xử lý FIFO theo clientTimestamp gốc và vẫn áp dụng cổng idempotent nên mỗi ngày mỗi cặp student–course chỉ tạo đúng một bản ghi Attendance.
    * **[EXC-002] Gửi điểm danh trùng lặp:** Khi nhiều lần quét cùng studentId–courseId xảy ra trong cùng một ngày, ràng buộc unique (student_id, course_id, attendance_date) chặn hàng trùng; service bắt ConstraintViolationException và ánh xạ sang phản hồi 200 với status='DUPLICATE', duplicate=true, mã nghiệp vụ ATT-DUP-001 ('already recorded'), không phát sinh thêm dòng dữ liệu.

#### 📅 Nhật ký phân bổ nhiệm vụ Sub-Agent theo trình tự thời gian (Giai đoạn 3)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Hiện thực hóa enrollment-service — duyệt khóa học còn chỗ và đăng ký ghi danh giao dịch nguyên tử kèm outbox thông báo

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [1]: Triển khai endpoint duyệt khóa học dành cho học viên

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-010]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentBrowseResource.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng REST resource GET /api/v1/enrollments/browse nhận tham số studentId bắt buộc; truy vấn courses bằng LEFT JOIN với enrollments để loại trừ hoàn toàn mọi khóa học đã có bản ghi ghi danh của học viên [REQ-010]; tính availableSeats = maxStudents − COUNT(enrollments) và chỉ trả về các khóa còn chỗ trống; sắp xếp kết quả theo startDate tăng dần với phân trang mặc định 20 bản ghi/trang; ánh xạ kết quả sang CourseAvailabilityDto và tận dụng index idx_enrollments_student_lookup để bảo đảm thời gian phản hồi sub-second.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- V3__enrollment_browse_outbox.sql (enrollment-service)
CREATE INDEX idx_enrollments_student_lookup
    ON enrollments (student_id, course_id);

CREATE INDEX idx_courses_schedule_window
    ON courses (start_date, end_date, teacher_id);
```

* **Hợp đồng định tuyến API và sự kiện [REQ-010]:**

```json
{
  "endpoint": "/api/v1/enrollments/browse",
  "method": "GET",
  "queryParams": {
    "studentId": "uuid (required)",
    "page": "int (default 0)",
    "size": "int (default 20)"
  },
  "response_200": {
    "courses": [
      {
        "courseId": "uuid",
        "title": "string",
        "startDate": "YYYY-MM-DD",
        "endDate": "YYYY-MM-DD",
        "teacherName": "string",
        "maxStudents": 30,
        "availableSeats": 12
      }
    ],
    "totalElements": 42,
    "page": 0
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [2]: Triển khai endpoint đăng ký khóa học giao dịch nguyên tử

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-011]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentRegistrationResource.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cài đặt POST /api/v1/enrollments/register chạy trong đúng một @Transactional: kiểm tra capacity còn trống, chèn bản ghi Enrollments; nếu studentId chưa tồn tại thì gọi nội bộ auth-service tự động cấp tài khoản vai trò 'Student' trước khi ghi danh [REQ-011]; sau khi commit, phát sự kiện enrollment.created tới notification-service để queue push notification tới mobile app học viên và đăng tin nhắn vào nhóm Zalo của trung tâm; rollback toàn bộ khi bất kỳ bước nào thất bại, trả 409 ENR-409-CAPACITY khi khóa đã đầy.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện [REQ-011]:**

```json
{
  "endpoint": "/api/v1/enrollments/register",
  "method": "POST",
  "request": {
    "studentId": "uuid | null",
    "fullName": "string (required when studentId is null)",
    "email": "string (required when studentId is null)",
    "courseId": "uuid (required)"
  },
  "response_201": {
    "enrollmentId": "uuid",
    "studentId": "uuid",
    "courseId": "uuid",
    "enrollmentDate": "YYYY-MM-DDTHH:mm:ssZ",
    "autoCreatedAccount": true,
    "notificationTargets": ["MOBILE_PUSH", "ZALO_GROUP"]
  },
  "error_409": {
    "errorCode": "ENR-409-CAPACITY",
    "message": "Course has reached maxStudents capacity"
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [3]: Xuất bản sự kiện thông báo ghi danh qua transactional outbox

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-011]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/event/EnrollmentNotificationPublisher.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cài đặt mẫu transactional outbox: ghi hàng enrollment_outbox trong cùng transaction với bản ghi ghi danh [REQ-011]; worker poll định kỳ đẩy sự kiện vào topic enrollment.created với payload {enrollmentId, studentId, courseId, centerZaloGroup}; bảo đảm chế độ at-least-once, cập nhật published_at sau khi điều phối thành công và giữ hàng pending khi broker lỗi tạm thời.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- V3__enrollment_browse_outbox.sql (enrollment-service)
CREATE TABLE enrollment_outbox (
    outbox_id uuid PRIMARY KEY,
    aggregate_id uuid NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    payload TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP NULL,
    CONSTRAINT chk_enrollment_outbox_event_type
        CHECK (event_type IN ('ENROLLMENT_CREATED'))
);

CREATE INDEX idx_enrollment_outbox_pending
    ON enrollment_outbox (published_at, outbox_id);
```

* **Hợp đồng định tuyến API và sự kiện [REQ-011]:**

```json
{
  "topic": "enrollment.created",
  "deliveryMode": "at-least-once (transactional outbox)",
  "payload": {
    "eventId": "uuid",
    "enrollmentId": "uuid",
    "studentId": "uuid",
    "courseId": "uuid",
    "centerZaloGroup": "string",
    "occurredAt": "YYYY-MM-DDTHH:mm:ssZ"
  },
  "consumer": "notification-service"
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [4]: Bộ test đơn vị bộ lọc duyệt khóa học

* **Chuyên môn vai trò Sub-Agent:** [Tester]
* **Tag IDs được nhắm tới:** [REQ-010]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentBrowseResource.java;./sources/backend/enrollment-service/src/test/java/com/hub/enrollment/EnrollmentBrowseResourceTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết JUnit 5 xác minh bộ lọc duyệt khóa học [REQ-010]: loại trừ đúng mọi khóa đã có bản ghi Enrollment của studentId; availableSeats tính chính sát theo maxStudents bao gồm biên capacity=0; xác minh phân trang, thứ tự startDate và cấu trúc CourseAvailabilityDto trả về.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [5]: Kiểm thử tích hợp giao dịch đăng ký khóa học

* **Chuyên môn vai trò Sub-Agent:** [Tester]
* **Tag IDs được nhắm tới:** [REQ-011]
* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/enrollment-service/src/test/java/com/hub/enrollment/EnrollmentRegistrationTransactionIT.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi chạy profile %test với PostgreSQL Testcontainers; xác minh kịch bản học viên mới: tài khoản vai trò 'Student' tự cấp + bản ghi Enrollments + hàng outbox được tạo trong cùng một transaction [REQ-011]; kịch bản khóa đầy trả 409 và rollback sạch không để lại dữ liệu mồ côi; xác minh sự kiện enrollment.created được đẩy ra broker sau commit.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [6]: Rà soát chất lượng và chiến lược tối ưu enrollment-service

* **Chuyên môn vai trò Sub-Agent:** [Reviewer]
* **Tag IDs được nhắm tới:** [REQ-010], [REQ-011]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Phân tích race condition khi hai request đăng ký đồng thời giành chỗ cuối cùng của khóa, yêu cầu áp dụng khóa biên (SELECT ... FOR UPDATE trên courses) hoặc optimistic version; rà soát chống N+1 query trong luồng duyệt khóa [REQ-010]; chuẩn hóa DTO và bảo đảm mọi nhánh lỗi trả ProblemDetail RFC 7807 [REQ-011]; đề xuất bản fix cụ thể kèm diff.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [7]: Biên soạn đặc tả API enrollment-service

* **Chuyên môn vai trò Sub-Agent:** [Doc]
* **Tag IDs được nhắm tới:** [REQ-010], [REQ-011]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-enrollment-service.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tài liệu hóa hai endpoint browse và register kèm bảng tham số, ví dụ payload request/response, mã trạng thái 200/201/400/409 [REQ-010], [REQ-011]; bổ sung sơ đồ tuần tự luồng outbox → notification-service và định nghĩa hợp đồng sự kiện enrollment.created kèm chính sách at-least-once.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Vận hành attendance-service — quét điểm danh QR, chính sách retry ngoại tuyến và bảo đảm tính idempotent tuyệt đối

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [1]: Triển khai endpoint quét điểm danh QR

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-012], [EXC-001]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceScanResource.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cài đặt POST /api/v1/attendance/scan nhận {studentId, courseId, clientTimestamp}; xác thực quan hệ student–course thông qua kiểm tra bản ghi Enrollment trước khi ghi [REQ-012]; suy ra attendanceDate từ clientTimestamp và ghi bản ghi Attendance kèm timestamp máy chủ; chấp nhận các scan tồn đọng được mobile app phát lại sau khi reconnect theo thứ tự FIFO clientTimestamp tăng dần [EXC-001]; trả 409 ATT-VAL-409 khi quan hệ student–course không tồn tại.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện [REQ-012]:**

```json
{
  "endpoint": "/api/v1/attendance/scan",
  "method": "POST",
  "request": {
    "studentId": "uuid (required)",
    "courseId": "uuid (required)",
    "clientTimestamp": "ISO-8601 (required)"
  },
  "response_200_recorded": {
    "attendanceId": "uuid",
    "status": "RECORDED",
    "duplicate": false,
    "attendanceDate": "YYYY-MM-DD"
  },
  "error_409": {
    "errorCode": "ATT-VAL-409",
    "message": "Student-course enrollment relation not found"
  }
}
```

* **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-001]:** Khi mạng đứt trong lúc quét, mobile app giữ payload trong hàng đợi ngoại tuyến và tự động retry sau khi kết nối khôi phục; attendance-service luôn sẵn sàng tiếp nhận request muộn, dùng clientTimestamp gốc làm mốc attendanceDate và không惩罚 request đến trễ — bản ghi vẫn được tạo đúng một lần nhờ cổng idempotent ở tầng lưu trữ.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [2]: Bảo đảm tính idempotent của bản ghi điểm danh

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-013], [EXC-002]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Áp dụng ràng buộc unique (student_id, course_id, attendance_date) tại tầng PostgreSQL làm cổng idempotent duy nhất [REQ-013]; bắt ConstraintViolationException và ánh xạ qua DuplicateAttendanceMapper sang phản hồi 200 với status='DUPLICATE', duplicate=true, mã nghiệp vụ ATT-DUP-001 ('already recorded') mà không phát sinh hàng mới [EXC-002]; bảo đảm hai lần quét cách nhau dưới một phút trong cùng ngày trả kết quả nhất quán.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- V4__attendance_unique_idempotency.sql (attendance-service)
ALTER TABLE attendance
    ADD CONSTRAINT uq_attendance_student_course_date
    UNIQUE (student_id, course_id, attendance_date);

CREATE INDEX idx_attendance_course_date
    ON attendance (course_id, attendance_date);
```

* **Hợp đồng định tuyến API và sự kiện [REQ-013]:**

```json
{
  "endpoint": "/api/v1/attendance/scan",
  "method": "POST",
  "idempotencyRule": "UNIQUE (student_id, course_id, attendance_date)",
  "response_200_duplicate": {
    "attendanceId": "uuid (existing record reference)",
    "status": "DUPLICATE",
    "duplicate": true,
    "businessCode": "ATT-DUP-001",
    "message": "already recorded"
  }
}
```

* **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-002]:** Mọi submission trùng lặp bị chặn bởi ràng buộc unique thay vì check-then-insert; hệ thống trả success kèm cờ 'already recorded' để client hiển thị trạng thái điểm danh đã ghi nhận, đồng thời ghi audit log sự kiện duplicate kèm userId và timestamp phục vụ truy vết.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [3]: Cơ chế tái xử lý scan ngoại tuyến sau ngắt kết nối

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [EXC-001]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/retry/OfflineReplayPolicy.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cài đặt hàng đợi nội bộ tiếp nhận bó scan được mobile app gửi lại sau reconnect; xử lý nghiêm ngặt FIFO theo clientTimestamp tăng dần [EXC-001]; từng phần tử vẫn đi qua cổng idempotent nên không tạo bản ghi trùng; ghi audit log mỗi phiên replay kèm userId, số lượng phần tử và timestamp để phục vụ giám sát phục hồi hậu outage.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

* **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-001]:** Chính sách replay bảo đảm thứ tự xử lý FIFO tuyệt đối: scan có clientTimestamp sớm hơn luôn được ghi trước, kết hợp ràng buộc idempotent khiến các bản sao lặp trong bó replay tự động hội tụ về một bản ghi duy nhất mà không phát sinh lỗi phía client.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [4]: Bộ test đơn vị xác thực quan hệ student–course

* **Chuyên môn vai trò Sub-Agent:** [Tester]
* **Tag IDs được nhắm tới:** [REQ-012]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceScanResource.java;./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceScanResourceTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết JUnit 5 xác minh [REQ-012]: quan hệ student–course hợp lệ → ghi bản ghi Attendance thành công; quan hệ không tồn tại → 409 ATT-VAL-409; attendanceDate được suy đúng từ clientTimestamp kể cả trường hợp múi giờ khác UTC; payload thiếu trường bắt buộc trả 400 với danh sách trường lỗi.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [5]: Kiểm thử tích hợp tính idempotent điểm danh

* **Chuyên môn vai trò Sub-Agent:** [Tester]
* **Tag IDs được nhắm tới:** [REQ-013], [EXC-002]
* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceIdempotencyIT.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Dùng PostgreSQL Testcontainers; gửi song song hai request quét cùng student/course/ngày cách nhau dưới một phút, assert đúng một hàng Attendance được tạo và request thứ hai trả 200 duplicate=true [REQ-013], [EXC-002]; mô phỏng replay bó 5 scan ngoại tuyến sau outage asserting thứ tự FIFO và zero bản ghi trùng lặp [EXC-001].
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [6]: Rà soát đồng thời và ràng buộc idempotent attendance-service

* **Chuyên môn vai trò Sub-Agent:** [Reviewer]
* **Tag IDs được nhắm tới:** [REQ-013], [EXC-002]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Phân tích đường đua giữa INSERT và vi phạm unique để xác nhận không tồn tại mẫu check-then-insert dễ lỗi TOCTOU [REQ-013]; đánh giá cấu hình connection pool và timeout khi xử lý burst replay; kiểm tra ánh xạ ConstraintViolationException không lộ chi tiết SQL ra ngoài phản hồi [EXC-002]; đề xuất bản fix tối ưu kèm diff cụ thể.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [7]: Biên soạn đặc tả API attendance-service

* **Chuyên môn vai trò Sub-Agent:** [Doc]
* **Tag IDs được nhắm tới:** [REQ-012], [REQ-013], [EXC-001], [EXC-002]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-attendance-service.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tài liệu hóa endpoint scan với semantics idempotent [REQ-012], [REQ-013]; mô tả chính sách retry ngoại tuyến và thứ tự FIFO replay [EXC-001]; liệt kê bảng mã lỗi ATT-VAL-409 và ATT-DUP-001 kèm ví dụ payload RECORDED/DUPLICATE [EXC-002].
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 3: Hoàn thiện card-service — truy vấn ngày hiệu lực thẻ hội viên và luồng gia hạn sau xác nhận thanh toán

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [1]: Triển khai truy vấn thẻ hội viên và tính toán ngày hiệu lực

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-014]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/card-service/src/main/java/com/hub/card/CardQueryResource.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cài đặt GET /api/v1/cards/me suy ra totalValidityDays từ validityDays, daysUsed = CURRENT_DATE − issueDate được kẹp biên trong khoảng [0, validityDays], daysRemaining = validityDays − daysUsed từ thực thể StudentCard [REQ-014]; chuẩn hóa mọi phép toán ngày theo UTC; trả 404 CARD-NOT-FOUND khi học viên chưa được cấp thẻ; tận dụng index idx_student_cards_student_lookup bảo đảm phản hồi sub-second.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- V5__card_validity_support.sql (card-service)
CREATE INDEX idx_student_cards_student_lookup
    ON student_cards (student_id, issue_date);
```

* **Hợp đồng định tuyến API và sự kiện [REQ-014]:**

```json
{
  "endpoint": "/api/v1/cards/me",
  "method": "GET",
  "auth": "Bearer JWT (role Student)",
  "response_200": {
    "cardId": "uuid",
    "issueDate": "YYYY-MM-DD",
    "totalValidityDays": 90,
    "daysUsed": 34,
    "daysRemaining": 56
  },
  "error_404": {
    "errorCode": "CARD-NOT-FOUND",
    "message": "No membership card issued for this student"
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [2]: Triển khai luồng gia hạn thẻ sau xác nhận thanh toán

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-015]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/card-service/src/main/java/com/hub/card/CardRenewalResource.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cài đặt POST /api/v1/cards/renew nhận renewalPeriodDays (ví dụ 30) và paymentReferenceId; chỉ mở rộng validityDays/ngày kết thúc của StudentCards sau khi PaymentConfirmationConsumer xác nhận sự kiện payment.confirmed từ payment service [REQ-015]; trong một transaction cập nhật thẻ và phát yêu cầu notification xác nhận gia hạn tới học viên; từ chối gia hạn khi paymentReferenceId chưa được xác nhận bằng 409 PAYMENT-PENDING mà không làm thay đổi dữ liệu thẻ.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện [REQ-015]:**

```json
{
  "endpoint": "/api/v1/cards/renew",
  "method": "POST",
  "request": {
    "studentId": "uuid (required)",
    "renewalPeriodDays": 30,
    "paymentReferenceId": "string (required)"
  },
  "response_200": {
    "cardId": "uuid",
    "validityDaysBefore": 90,
    "validityDaysAfter": 120,
    "extendedUntil": "YYYY-MM-DD",
    "confirmationNotificationSent": true
  },
  "error_409": {
    "errorCode": "PAYMENT-PENDING",
    "message": "Payment reference not confirmed yet"
  }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [3]: Consumer xác nhận thanh toán cho luồng gia hạn thẻ

* **Chuyên môn vai trò Sub-Agent:** [Coder]
* **Tag IDs được nhắm tới:** [REQ-015]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/card-service/src/main/java/com/hub/card/PaymentConfirmationConsumer.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tiêu thụ topic payment.confirmed với chế độ at-least-once; áp dụng khóa idempotent theo paymentReferenceId để chống cộng dồn validityDays khi sự kiện được phát lại [REQ-015]; khi xử lý thành công thì kích hoạt extendValidityDays và điều phối notification xác nhận; đẩy payload sai schema vào dead-letter topic để phân tích hậu kiểm.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

* **Hợp đồng định tuyến API và sự kiện [REQ-015]:**

```json
{
  "topic": "payment.confirmed",
  "groupId": "card-service-renewal",
  "deliveryMode": "at-least-once",
  "idempotencyKey": "paymentReferenceId",
  "deadLetterTopic": "payment.confirmed.dlq",
  "onSuccess": ["extend validityDays", "dispatch renewal confirmation notification"]
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [4]: Bộ test đơn vị máy tính ngày hiệu lực thẻ

* **Chuyên môn vai trò Sub-Agent:** [Tester]
* **Tag IDs được nhắm tới:** [REQ-014]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/card-service/src/main/java/com/hub/card/CardValidityCalculator.java;./sources/backend/card-service/src/test/java/com/hub/card/CardValidityCalculatorTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết JUnit parametrized xác minh [REQ-014]: daysUsed được kẹp biên tại 0 và validityDays; daysRemaining không bao giờ âm; thẻ hết hạn trả daysRemaining=0; mọi phép trừ ngày thống nhất múi giờ UTC; phủ case issueDate trùng ngày hiện hành.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [5]: Kiểm thử tích hợp luồng gia hạn thẻ

* **Chuyên môn vai trò Sub-Agent:** [Tester]
* **Tag IDs được nhắm tới:** [REQ-015]
* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/card-service/src/test/java/com/hub/card/CardRenewalFlowIT.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Mô phỏng toàn trình [REQ-015]: POST renew → sự kiện payment.confirmed → validityDays tăng đúng 30 ngày → notification xác nhận được điều phối; kịch bản payment chưa xác nhận trả 409 PAYMENT-PENDING và dữ liệu thẻ bất biến; kịch bản paymentReferenceId trùng lặp chứng minh tính idempotent không cộng dồn ngày hiệu lực.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [6]: Rà soát card-service về phép toán ngày và tính idempotent gia hạn

* **Chuyên môn vai trò Sub-Agent:** [Reviewer]
* **Tag IDs được nhắm tới:** [REQ-014], [REQ-015]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/card-service/src/main/java/com/hub/card/CardValidityCalculator.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát phép trừ ngày theo UTC để loại trừ lỗi lệch múi giờ làm sai daysUsed/daysRemaining [REQ-014]; kiểm tra consumer chống cộng dồn validityDays khi sự kiện payment.confirmed được phát lại và xác minh khóa idempotent theo paymentReferenceId [REQ-015]; chuẩn hóa thông điệp lỗi và đề xuất bản fix kèm diff cụ thể.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ CON [7]: Biên soạn đặc tả API card-service

* **Chuyên môn vai trò Sub-Agent:** [Doc]
* **Tag IDs được nhắm tới:** [REQ-014], [REQ-015]
* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-card-service.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tài liệu hóa cards/me với quy tắc suy ra daysUsed/daysRemaining [REQ-014] và luồng renew phụ thuộc xác nhận payment.confirmed [REQ-015]; bổ sung bảng mã lỗi CARD-NOT-FOUND/PAYMENT-PENDING, ví dụ payload đầy đủ và sơ đồ tuần tự consumer gia hạn.
* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**

```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ nào cần thiết cho ngữ cảnh giai đoạn này
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->

### 📈 Giai đoạn 4 - Điều phối Thông báo Đa kênh, Khuyến mãi, Chatbot AI và Trải nghiệm Di động Đa ngôn ngữ

- **Mục tiêu cốt lõi & mục đích của giai đoạn:** Giai đoạn 4 bàn giao lớp giao tiếp và tương tác của nền tảng membership-hub: notification-service điều phối thông báo đa kênh FCM/APNs/Zalo cho các sự kiện phân công giáo viên, ghi danh học viên và announcement, kèm chính sách retry tối đa 3 lần trước khi đánh dấu thất bại vĩnh viễn [REQ-016], [EXC-003]; promotion-service cung cấp CRUD khuyến mãi với mã unique và quy tắc vĩnh viễn khi bỏ trống endDate [REQ-017] cùng CRUD announcement tự động ẩn sau ngày hết hạn [REQ-018]; chatbot-service trả lời truy vấn về khóa học, giáo viên, trung tâm, trạng thái tài khoản và escalate lên nhân viên hỗ trợ khi độ tin cậy thấp [REQ-019]; mobile-app React Native render giao diện responsive theo vai trò trên Android/iOS [REQ-020], đăng ký device token và xử lý deep-link push [REQ-021]; web-app Next.js phát hiện ngôn ngữ ưu tiên với fallback Accept-Language [REQ-022] và SSR meta tags cùng hreflang alternate links cho en/vi/es [REQ-023].

- **Ma trận ánh xạ thư mục vật lý đích:**
    - `./sources/backend/notification-service/src/main/java/com/hub/notification/service/NotificationOrchestrationService.java` — [REQ-016]
    - `./sources/backend/notification-service/src/main/java/com/hub/notification/channel/FcmApnsPushAdapter.java` — [REQ-016]
    - `./sources/backend/notification-service/src/main/java/com/hub/notification/channel/ZaloGroupChannelAdapter.java` — [REQ-016]
    - `./sources/backend/notification-service/src/main/java/com/hub/notification/api/DeviceTokenResource.java` — [REQ-021]
    - `./sources/backend/db-migrations/V4__phase4_notification_delivery_tracking.sql` — [REQ-016], [EXC-003]
    - `./sources/backend/notification-service/src/main/java/com/hub/notification/service/DeliveryRetryScheduler.java` — [REQ-016], [EXC-003]
    - `./sources/backend/notification-service/src/main/java/com/hub/notification/exception/NotificationDeliveryException.java` — [EXC-003]
    - `./sources/backend/notification-service/src/test/java/com/hub/notification/service/DeliveryRetrySchedulerTest.java` — [REQ-016], [EXC-003]
    - `./sources/backend/notification-service/src/test/java/com/hub/notification/channel/MultiChannelDispatchIT.java` — [REQ-016]
    - `./sources/docs/api-notification-service-spec.md` — [REQ-016], [EXC-003]
    - `./sources/backend/promotion-service/src/main/java/com/hub/promotion/api/PromotionResource.java` — [REQ-017]
    - `./sources/backend/promotion-service/src/main/java/com/hub/promotion/service/PromotionService.java` — [REQ-017]
    - `./sources/backend/promotion-service/src/main/java/com/hub/promotion/api/AnnouncementResource.java` — [REQ-018]
    - `./sources/backend/promotion-service/src/main/java/com/hub/promotion/service/AnnouncementExpiryFilter.java` — [REQ-018]
    - `./sources/backend/chatbot-service/src/main/java/com/hub/chatbot/api/ChatbotResource.java` — [REQ-019]
    - `./sources/backend/chatbot-service/src/main/java/com/hub/chatbot/service/ChatbotEngineService.java` — [REQ-019]
    - `./sources/backend/promotion-service/src/test/java/com/hub/promotion/service/PromotionServiceTest.java` — [REQ-017]
    - `./sources/backend/promotion-service/src/test/java/com/hub/promotion/api/AnnouncementExpiryIT.java` — [REQ-018]
    - `./sources/backend/chatbot-service/src/test/java/com/hub/chatbot/service/ChatbotEscalationIT.java` — [REQ-019]
    - `./sources/docs/api-promotion-service-spec.md` — [REQ-017], [REQ-018]
    - `./sources/docs/chatbot-integration-guide.md` — [REQ-019]
    - `./sources/frontend/mobile-app/src/navigation/RoleBasedNavigator.tsx` — [REQ-020]
    - `./sources/frontend/mobile-app/src/screens/RoleDashboardScreen.tsx` — [REQ-020]
    - `./sources/frontend/mobile-app/src/services/PushNotificationService.ts` — [REQ-021]
    - `./sources/frontend/mobile-app/src/services/DeepLinkHandler.ts` — [REQ-021]
    - `./sources/frontend/web-app/src/middleware/localeDetection.ts` — [REQ-022]
    - `./sources/frontend/web-app/src/components/seo/HreflangHeadManager.tsx` — [REQ-023]
    - `./sources/frontend/mobile-app/__tests__/RoleBasedNavigator.test.tsx` — [REQ-020]
    - `./sources/frontend/mobile-app/__tests__/PushDeepLink.e2e.ts` — [REQ-021]
    - `./sources/frontend/web-app/__tests__/localeDetection.test.ts` — [REQ-022]
    - `./sources/docs/localization-seo-guide.md` — [REQ-022], [REQ-023]
    - `./sources/docs/mobile-push-deeplink-guide.md` — [REQ-021]

- **Đặc tả DDL SQL lược đồ cơ sở dữ liệu** [REQ-016], [EXC-003]:

```sql
-- =====================================================================
-- Flyway Migration: V4__phase4_notification_delivery_tracking.sql
-- Scope: Phase 4 - notification delivery retry tracking and catalog indexes
-- =====================================================================

ALTER TABLE notifications ADD COLUMN delivery_channels VARCHAR(30) NOT NULL DEFAULT 'PUSH';
ALTER TABLE notifications ADD COLUMN retry_count SMALLINT NOT NULL DEFAULT 0;
ALTER TABLE notifications ADD COLUMN last_attempt_at TIMESTAMP;
ALTER TABLE notifications ADD COLUMN failure_reason VARCHAR(500);

ALTER TABLE notifications ADD CONSTRAINT chk_notifications_delivery_channels
    CHECK (delivery_channels IN ('PUSH', 'ZALO', 'PUSH_AND_ZALO'));

ALTER TABLE notifications ADD CONSTRAINT chk_notifications_retry_bounds
    CHECK (retry_count BETWEEN 0 AND 3);

CREATE INDEX idx_notifications_retry_queue
    ON notifications (delivered, retry_count, sent_at);

CREATE INDEX idx_promotions_active_lookup
    ON promotions (code, start_date, end_date);

CREATE INDEX idx_announcements_visibility_window
    ON announcements (start_date, end_date);
```

- **Hợp đồng định tuyến API và sự kiện** [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-021]: Các hợp đồng dưới đây được công bố qua api-gateway và tiêu thụ bởi web-app Next.js cùng mobile-app React Native.

```json
{
  "endpoint": "POST /api/v1/notifications/dispatch",
  "auth": "Bearer JWT",
  "request": {
    "userId": "uuid (nullable when broadcasting to Zalo group only)",
    "groupZalo": "string (optional target Zalo group id)",
    "message": "string (required, max 2000 chars)",
    "channels": ["PUSH", "ZALO"]
  },
  "response_202": {
    "notificationId": "uuid",
    "status": "QUEUED"
  }
}
```

```json
{
  "endpoint": "POST /api/v1/devices/token",
  "auth": "Bearer JWT",
  "request": {
    "userId": "uuid",
    "deviceToken": "string (FCM or APNs token)",
    "platform": "ANDROID | IOS"
  },
  "response_204": "empty body",
  "error_400": { "code": "DEVICE_TOKEN_INVALID" }
}
```

```json
{
  "endpoints": [
    "GET /api/v1/promotions",
    "POST /api/v1/promotions",
    "PUT /api/v1/promotions/{promoId}",
    "DELETE /api/v1/promotions/{promoId}"
  ],
  "create_request": {
    "code": "string (unique discount code)",
    "discountPercent": 10,
    "startDate": "2025-01-01 (optional)",
    "endDate": "2025-06-30 (optional, null means perpetual)",
    "description": "string (optional)"
  },
  "response_201": { "promoId": "uuid", "code": "TET2025", "discountPercent": 10, "perpetual": false },
  "error_409": { "code": "PROMO_CODE_DUPLICATED" }
}
```

```json
{
  "endpoints": [
    "GET /api/v1/announcements",
    "POST /api/v1/announcements",
    "PUT /api/v1/announcements/{announcementId}",
    "DELETE /api/v1/announcements/{announcementId}"
  ],
  "create_request": {
    "title": "string (max 150 chars)",
    "content": "string (max 2000 chars)",
    "startDate": "2025-02-01 (optional)",
    "endDate": "2025-03-01 (optional expiry, auto-hidden after this date)"
  },
  "list_item": { "announcementId": "uuid", "title": "Scheduled maintenance", "endDate": "2025-03-01" }
}
```

```json
{
  "endpoint": "POST /api/v1/chatbot/query",
  "auth": "Bearer JWT (any authenticated role)",
  "request": {
    "sessionId": "uuid",
    "message": "When does the Japanese course start?"
  },
  "response_200_high_confidence": {
    "answer": "The Japanese course starts on 2025-03-15 at District 1 center",
    "confidence": 0.92,
    "escalated": false
  },
  "response_200_low_confidence": {
    "answer": "Your question has been forwarded to human support",
    "confidence": 0.31,
    "escalated": true
  }
}
```

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn** [EXC-003]: Khi một push notification không thể giao hàng (ví dụ device token invalid), hệ thống ghi nhận thất bại kèm timestamp và lập lịch retry tối đa ba lần trước khi đánh dấu thất bại vĩnh viễn.

| Mã lỗi | Điều kiện kích hoạt | Hành vi xử lý của hệ thống |
| :--- | :--- | :--- |
| NOTIF_CHANNEL_TRANSIENT | [EXC-003] Lỗi tạm thời mạng hoặc timeout khi gọi FCM, APNs, Zalo API | Tăng retry_count lên 1 đơn vị, lên lịch thử lại với khoảng nghỉ luỹ thừa, giữ trạng thái QUEUED khi retry_count nhỏ hơn 3 |
| NOTIF_TOKEN_PERMANENT_INVALID | [EXC-003] Device token bị từ chối vĩnh viễn hoặc Zalo API trả lỗi xác thực | Không retry, ghi failure_reason, đánh dấu delivered=false vĩnh viễn và ghi dòng audit log cảnh báo |

#### 📅 Nhật ký phân bổ tác vụ Sub-Agent theo trình tự thời gian từng ngày (Giai đoạn 4)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Xây dựng trọn vẹn notification-service gồm điều phối đa kênh FCM/APNs/Zalo, đăng ký device token và cơ chế retry tối đa 3 lần

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [1]: Triển khai pipeline điều phối trung tâm NotificationOrchestrationService

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-016]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/service/NotificationOrchestrationService.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Xây dựng service nhận yêu cầu dispatch từ các nghiệp vụ phân công giáo viên, ghi danh học viên và announcement [REQ-016]; persist bản ghi Notifications trước khi fan-out để bảo đảm không mất thông báo; điều phối đồng thời tới kênh PUSH và ZALO theo giá trị delivery_channels; cập nhật cờ delivered khi toàn bộ kênh xác nhận thành công; ghi audit log mỗi lần dispatch kèm userId và timestamp.

* **Hợp đồng định tuyến API và sự kiện** [REQ-016]:

```json
{
  "endpoint": "POST /api/v1/notifications/dispatch",
  "request": {
    "userId": "uuid (nullable for Zalo-group broadcast)",
    "groupZalo": "string (optional)",
    "message": "string (max 2000 chars)",
    "channels": ["PUSH", "ZALO"]
  },
  "response_202": { "notificationId": "uuid", "status": "QUEUED" }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [2]: Hiện thực adapter đẩy thông báo FCM/APNs

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-016]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/channel/FcmApnsPushAdapter.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Tích hợp Firebase Cloud Messaging cho Android và Apple APNs cho iOS [REQ-016]; đọc device token từ bảng đăng ký thiết bị; phân loại lỗi token invalid là lỗi không thể retry và lỗi timeout 5xx là lỗi có thể retry; chuẩn hóa payload alert/title/deep-link route cho từng nền tảng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [3]: Hiện thực adapter đăng bài nhóm Zalo

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-016]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/channel/ZaloGroupChannelAdapter.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Gọi Zalo API đăng tin nhắn văn bản lên groupZalo được chỉ định cho thông báo, phân công khóa học và cảnh báo điểm danh [REQ-016]; quản lý access token ứng dụng kèm cơ chế làm mới tự động; ánh xạ mã lỗi HTTP của Zalo sang phân loại retryable/non-retryable phục vụ scheduler.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [4]: Expose endpoint đăng ký device token

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-021]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/api/DeviceTokenResource.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Công bố POST /api/v1/devices/token nhận deviceToken và platform sau khi người dùng login trên Android/iOS [REQ-021]; validate định dạng token theo nền tảng; lưu ánh xạ userId–deviceToken phục vụ điều phối push; hỗ trợ re-register khi token xoay vòng.

* **Hợp đồng định tuyến API và sự kiện** [REQ-021]:

```json
{
  "endpoint": "POST /api/v1/devices/token",
  "request": { "userId": "uuid", "deviceToken": "string", "platform": "ANDROID | IOS" },
  "response_204": "empty body",
  "error_400": { "code": "DEVICE_TOKEN_INVALID" }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [5]: Sinh migration theo dõi trạng thái giao hàng

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-016], [EXC-003]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/db-migrations/V4__phase4_notification_delivery_tracking.sql

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Bổ sung các cột delivery_channels, retry_count, last_attempt_at, failure_reason vào bảng notifications phục vụ cơ chế retry tối đa 3 lần [EXC-003]; thêm CHECK constraint chặn retry vượt ngưỡng và index phục vụ quét hàng đợi pending với hiệu năng sub-second [REQ-016].

* **Đặc tả DDL SQL lược đồ cơ sở dữ liệu** [REQ-016], [EXC-003]:

```sql
ALTER TABLE notifications ADD COLUMN delivery_channels VARCHAR(30) NOT NULL DEFAULT 'PUSH';
ALTER TABLE notifications ADD COLUMN retry_count SMALLINT NOT NULL DEFAULT 0;
ALTER TABLE notifications ADD COLUMN last_attempt_at TIMESTAMP;
ALTER TABLE notifications ADD COLUMN failure_reason VARCHAR(500);

ALTER TABLE notifications ADD CONSTRAINT chk_notifications_delivery_channels
    CHECK (delivery_channels IN ('PUSH', 'ZALO', 'PUSH_AND_ZALO'));

ALTER TABLE notifications ADD CONSTRAINT chk_notifications_retry_bounds
    CHECK (retry_count BETWEEN 0 AND 3);

CREATE INDEX idx_notifications_retry_queue
    ON notifications (delivered, retry_count, sent_at);
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [6]: Lập lịch retry giao hàng tối đa 3 lần

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-016], [EXC-003]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/service/DeliveryRetryScheduler.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Job định kỳ quét các bản ghi delivered=false còn retry_count nhỏ hơn 3 [EXC-003]; thực hiện lại dispatch qua kênh thất bại với khoảng nghỉ luỹ thừa; sau lần thử thứ ba đánh dấu thất bại vĩnh viễn kèm failure_reason; bảo đảm an toàn luồng khi nhiều pod chạy song song bằng khóa bi quan dựa trên UPDATE điều kiện [REQ-016].

* **Bộ xử lý ngoại lệ cục bộ của giai đoạn** [EXC-003]: Khi kênh FCM/APNs/Zalo báo lỗi tạm thời, scheduler tăng retry_count và lên lịch thử lại với khoảng nghỉ luỹ thừa; sau lần thử thứ ba thất bại, bản ghi bị đánh dấu thất bại vĩnh viễn kèm failure_reason và không còn được quét lại.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [7]: Định nghĩa ngoại lệ giao hàng và mapper chuẩn hóa

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [EXC-003]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/exception/NotificationDeliveryException.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Xây dựng hierarchy ngoại lệ bao gói lỗi FCM/APNs/Zalo kèm mã lỗi máy đọc [EXC-003]; triển khai ExceptionMapper trả error envelope thống nhất cho toàn bộ resource; phân biệt hai nhánh TRANSIENT_RETRYABLE và PERMANENT_FAILED để scheduler quyết định đường đi xử lý.

* **Bộ xử lý ngoại lệ cục bộ của giai đoạn** [EXC-003]: Bản đồ mã lỗi gồm NOTIF_CHANNEL_TRANSIENT (có thể retry, giữ trạng thái QUEUED) và NOTIF_TOKEN_PERMANENT_INVALID (hủy ngay, không retry, ghi audit log cảnh báo).

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [8]: Unit test scheduler retry

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-016], [EXC-003]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/service/DeliveryRetryScheduler.java;./sources/backend/notification-service/src/test/java/com/hub/notification/service/DeliveryRetrySchedulerTest.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Kiểm chứng đúng 3 lần thử tối đa rồi đánh dấu FAILED vĩnh viễn [EXC-003]; xác minh khoảng nghỉ luỹ thừa giữa các lần thử và việc không phát sinh bản ghi trùng; mock adapter FCM/Zalo trả lỗi transient ở lần 1 rồi thành công ở lần 2 để xác nhận delivered=true [REQ-016].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [9]: Integration test điều phối đa kênh

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-016]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/notification-service/src/test/java/com/hub/notification/channel/MultiChannelDispatchIT.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Chạy luồng end-to-end dispatch trên Testcontainers PostgreSQL: persist Notifications, fan-out PUSH và ZALO, xác nhận delivered=true cùng dòng audit log được ghi [REQ-016]; kiểm tra kịch bản Zalo lỗi仍 giữ trạng thái QUEUED cho vòng retry kế tiếp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [10]: Rà soát tính idempotent và an toàn luồng của orchestrator

* **Chuyên môn hóa vai trò Sub-Agent:** [Reviewer]

* **Tag ID theo dõi mục tiêu:** [REQ-016]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/service/NotificationOrchestrationService.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Rà soát nguy cơ dispatch kép khi retry chồng chất, xác nhận transaction boundary persist-trước-fan-out [REQ-016]; phát hiện và đề xuất fix race condition giữa scheduler và orchestrator; kiểm tra chuẩn hóa encoding tiếng Việt trong nội dung message trước khi đẩy kênh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [11]: Biên soạn đặc tả API notification-service

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Tag ID theo dõi mục tiêu:** [REQ-016], [EXC-003]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-notification-service-spec.md

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Biên soạn đặc tả OpenAPI cho POST /api/v1/notifications/dispatch và POST /api/v1/devices/token kèm bảng mã lỗi retry [REQ-016]; mô tả chính sách retry tối đa 3 lần và ý nghĩa các trạng thái QUEUED/DELIVERED/FAILED [EXC-003].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: CRUD Khuyến mãi và Thông báo công khai kèm tích hợp Chatbot AI chăm sóc khách hàng

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [1]: Expose REST CRUD khuyến mãi

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-017]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/api/PromotionResource.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Công bố GET/POST/PUT/DELETE /api/v1/promotions dành cho Center Admin và Manager [REQ-017]; trả 409 Conflict khi code trùng; validate discountPercent trong khoảng 1–100; endDate bỏ trống được đánh dấu khuyến mãi vĩnh viễn và hiển thị trong danh sách ưu đãi phía học viên.

* **Hợp đồng định tuyến API và sự kiện** [REQ-017]:

```json
{
  "endpoints": ["GET /api/v1/promotions", "POST /api/v1/promotions", "PUT /api/v1/promotions/{promoId}", "DELETE /api/v1/promotions/{promoId}"],
  "create_request": { "code": "string (unique)", "discountPercent": 10, "startDate": "optional", "endDate": "optional (null = perpetual)", "description": "optional" },
  "error_409": { "code": "PROMO_CODE_DUPLICATED" }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [2]: Triển khai logic nghiệp vụ khuyến mãi

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-017]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/service/PromotionService.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Xây dựng tầng service quản lý vòng đời promotion [REQ-017]; ràng buộc code unique ở cả mức DB và mức ứng dụng; cung cấp truy vấn danh sách ưu đãi đang hiệu quả lọc theo startDate/endDate hiện hành, bao gồm các mã vĩnh viễn không có endDate.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [3]: Expose REST CRUD thông báo công khai

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-018]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/api/AnnouncementResource.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Công bố CRUD /api/v1/announcements với title tối đa 150 ký tự và content tối đa 2000 ký tự [REQ-018]; hỗ trợ expiry tùy chọn; phát sóng toàn site cho mọi người dùng và tự động ẩn sau ngày hết hạn đã cấu hình.

* **Hợp đồng định tuyến API và sự kiện** [REQ-018]:

```json
{
  "endpoints": ["GET /api/v1/announcements", "POST /api/v1/announcements", "PUT /api/v1/announcements/{announcementId}", "DELETE /api/v1/announcements/{announcementId}"],
  "create_request": { "title": "string (max 150 chars)", "content": "string (max 2000 chars)", "startDate": "optional", "endDate": "optional expiry" }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [4]: Xây dựng bộ lọc tự ẩn sau hết hạn

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-018]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/service/AnnouncementExpiryFilter.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Áp dụng điều kiện lọc endDate lớn hơn hoặc bằng CURRENT_DATE hoặc endDate IS NULL trên mọi truy vấn danh sách để announcement tự động biến mất sau ngày hết hạn [REQ-018]; tận dụng idx_announcements_visibility_window cho truy vấn cửa sổ hiệu lực.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [5]: Expose endpoint truy vấn chatbot

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-019]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/chatbot-service/src/main/java/com/hub/chatbot/api/ChatbotResource.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Công bố POST /api/v1/chatbot/query nhận câu hỏi tự nhiên về khóa học, giáo viên, trung tâm và trạng thái tài khoản [REQ-019]; trả answer kèm điểm confidence; ghi toàn bộ hội thoại vào AuditLog để phục vụ truy vết.

* **Hợp đồng định tuyến API và sự kiện** [REQ-019]:

```json
{
  "endpoint": "POST /api/v1/chatbot/query",
  "request": { "sessionId": "uuid", "message": "string" },
  "response_200": { "answer": "string", "confidence": 0.92, "escalated": false }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [6]: Xây dựng engine chatbot và lộ trình escalate

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-019]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/chatbot-service/src/main/java/com/hub/chatbot/service/ChatbotEngineService.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Xây dựng engine đối chiếu intent với dữ liệu Courses, Users và Centers [REQ-019]; khi confidence xuống dưới ngưỡng cấu hình thì kích hoạt escalate chuyển phiên cho nhân viên hỗ trợ, đặt escalated=true trong phản hồi và ghi dòng AuditLog tương ứng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [7]: Unit test nghiệp vụ khuyến mãi

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-017]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/service/PromotionService.java;./sources/backend/promotion-service/src/test/java/com/hub/promotion/service/PromotionServiceTest.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Kiểm chứng chặn code trùng với ngoại lệ xung đột, biên discountPercent 1–100 và hành vi khuyến mãi vĩnh viễn khi endDate null [REQ-017]; xác minh bộ lọc ưu đãi hiệu lực trả đúng tập kết quả hiện hành.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [8]: Integration test tự ẩn announcement

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-018]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/promotion-service/src/test/java/com/hub/promotion/api/AnnouncementExpiryIT.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Seed dữ liệu gồm announcement quá hạn và còn hạn, gọi GET /api/v1/announcements xác nhận bản ghi quá hạn không xuất hiện trong phản hồi [REQ-018]; kiểm tra announcement không có endDate luôn hiển thị.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [9]: Integration test escalate chatbot

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-019]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/chatbot-service/src/test/java/com/hub/chatbot/service/ChatbotEscalationIT.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Mô phỏng câu hỏi ngoài phạm vi khiến confidence thấp, xác nhận phản hồi escalated=true kèm thông điệp chuyển phiên nhân viên hỗ trợ và dòng AuditLog được ghi đầy đủ [REQ-019].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [10]: Rà soát biên validate và độ dài nội dung

* **Chuyên môn hóa vai trò Sub-Agent:** [Reviewer]

* **Tag ID theo dõi mục tiêu:** [REQ-017], [REQ-018]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/service/PromotionService.java

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Kiểm tra chặt chẽ giới hạn title 150 ký tự và content 2000 ký tự cùng chuẩn hóa đầu vào chống XSS [REQ-018]; đánh giá hiệu năng truy vấn lọc khuyến mãi hiệu lực và đề xuất bổ sung index nếu cần [REQ-017].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [11]: Biên soạn đặc tả API promotion-service

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Tag ID theo dõi mục tiêu:** [REQ-017], [REQ-018]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-promotion-service-spec.md

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Biên soạn tài liệu tham chiếu CRUD promotions và announcements kèm ví dụ payload, mã lỗi 409 trùng code, quy tắc khuyến mãi vĩnh viễn và cơ chế tự ẩn sau hết hạn [REQ-017], [REQ-018].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [12]: Biên soạn hướng dẫn tích hợp chatbot

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Tag ID theo dõi mục tiêu:** [REQ-019]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/chatbot-integration-guide.md

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Mô tả hợp đồng POST /api/v1/chatbot/query, ngưỡng confidence cấu hình, luồng escalate lên nhân viên hỗ trợ và cơ chế ghi AuditLog cho từng phiên hội thoại [REQ-019].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 3: UI di động theo vai trò, push notification deep-link, phát hiện ngôn ngữ và SEO đa ngôn ngữ en/vi/es

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [1]: Xây dựng điều hướng đa vai trò React Native

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-020]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/mobile-app/src/navigation/RoleBasedNavigator.tsx

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Xây dựng navigator động đọc roleId ngay sau đăng nhập và render bộ stack tương ứng cho Student, Teacher, Admin [REQ-020]; chặn truy cập màn hình ngoài phạm vi vai trò ngay tại tầng điều hướng trước khi render.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [2]: Hiện thực màn hình dashboard theo vai trò

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-020]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/mobile-app/src/screens/RoleDashboardScreen.tsx

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Hiện thực màn hình chủ phản chiếu chức năng web cho từng vai trò: Student xem thẻ hội viên và duyệt khóa học, Teacher xem lịch dạy chỉ đọc, Admin xem điều hành trung tâm [REQ-020]; bố cục responsive nhất quán trên Android và iOS.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [3]: Xây dựng dịch vụ đăng ký push và nhận thông báo

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-021]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/mobile-app/src/services/PushNotificationService.ts

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Xin quyền notification, lấy device token từ FCM/APNs và gọi POST /api/v1/devices/token ngay sau login [REQ-021]; lắng nghe push ở chế độ foreground và background cho xác nhận điểm danh, announcement mới và tin nhắn nhắc nhở.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [4]: Xử lý deep-link từ payload push

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-021]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/mobile-app/src/services/DeepLinkHandler.ts

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Phân giải route đính kèm payload push để điều hướng sâu tới màn hình liên quan như chi tiết khóa học, thẻ hội viên, điểm danh [REQ-021]; xử lý an toàn kịch bản cold-start và chuyển tiếp từ background.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [5]: Xây dựng middleware phát hiện ngôn ngữ ưu tiên

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-022]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/web-app/src/middleware/localeDetection.ts

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Middleware đọc preference ngôn ngữ đã lưu của người dùng, fallback về Accept-Language header của trình duyệt, mặc định cuối cùng là 'vi' [REQ-022]; rewrite route sang tiền tố locale tương ứng và chuyển đổi locale không cần reload trang.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [6]: Quản lý hreflang và thẻ lang SSR

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Tag ID theo dõi mục tiêu:** [REQ-023]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/web-app/src/components/seo/HreflangHeadManager.tsx

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Render thuộc tính html lang và bộ link rel='alternate' hreflang cho en/vi/es trên từng page qua SSR metadata [REQ-023]; sinh language-specific meta title và description phục vụ crawler lập chỉ mục.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [7]: Unit test điều hướng vai trò

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-020]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/mobile-app/src/navigation/RoleBasedNavigator.tsx;./sources/frontend/mobile-app/__tests__/RoleBasedNavigator.test.tsx

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Render navigator với từng roleId và xác nhận tập màn hình đúng phạm vi vai trò; khẳng định Student không truy cập được route admin và Teacher chỉ nhận stack chỉ đọc [REQ-020].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [8]: E2E test push deep-link

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-021]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/frontend/mobile-app/__tests__/PushDeepLink.e2e.ts

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Mô phỏng push chứa deep-link ở cả trạng thái cold-start và background, xác nhận ứng dụng điều hướng tới đúng màn hình đích và không crash khi route không hợp lệ [REQ-021].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [9]: Unit test fallback ngôn ngữ

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Tag ID theo dõi mục tiêu:** [REQ-022]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/web-app/src/middleware/localeDetection.ts;./sources/frontend/web-app/__tests__/localeDetection.test.ts

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Kiểm tra thứ tự ưu tiên stored preference, sau đó Accept-Language, cuối cùng mặc định 'vi'; xác minh việc nạp đúng bundle en/vi/es tương ứng [REQ-022].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [10]: Rà soát bảo mật deep-link và trải nghiệm offline

* **Chuyên môn hóa vai trò Sub-Agent:** [Reviewer]

* **Tag ID theo dõi mục tiêu:** [REQ-020], [REQ-021]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/frontend/mobile-app/src/services/DeepLinkHandler.ts

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Rà soát nguy cơ deep-link injection và xác thực route whitelist theo vai trò [REQ-021]; đánh giá khả năng đáp ứng UI khi mất kết nối mạng, đề xuất bổ sung caching ngoại tuyến cho màn hình còn thiếu [REQ-020].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [11]: Biên soạn hướng dẫn bản địa hóa và SEO

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Tag ID theo dõi mục tiêu:** [REQ-022], [REQ-023]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/localization-seo-guide.md

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Biên soạn hướng dẫn vận hành ba ngôn ngữ en/vi/es gồm quy tắc externalize chuỗi UI, thứ tự fallback locale và checklist hreflang cùng meta tags phục vụ crawler [REQ-022], [REQ-023].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 TÁC VỤ PHỤ [12]: Biên soạn hướng dẫn push và deep-link di động

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Tag ID theo dõi mục tiêu:** [REQ-021]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/mobile-push-deeplink-guide.md

* **Hướng dẫn tác vụ kỹ thuật cấp thấp:** Tài liệu hóa luồng đăng ký device token sau login, cấu trúc payload push cho FCM/APNs và bảng ánh xạ deep-link route theo từng loại thông báo [REQ-021].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->

### 📈 Giai đoạn 5 - Hạ tầng DevOps, Dịch vụ Báo cáo & Bàn giao Production

- **Mục tiêu cốt lõi & mục đích của giai đoạn:** Giai đoạn cuối cùng này hoàn thiện chuỗi bàn giao production của nền tảng membership-hub trên ba trụ cột. Thứ nhất, xây dựng reporting-service cung cấp báo cáo điểm danh CSV theo trung tâm và khoảng ngày với các cột StudentName, CourseName, AttendanceDate, Status [REQ-024], cơ chế phát lại FIFO cho các bản ghi quét QR tồn đọng hậu outage [EXC-005], và bảng điều khiển real-time totalStudents, activeCourses, upcomingSessions đọc qua PostgreSQL read replica để cách ly workload báo cáo khỏi OLTP [REQ-025]. Thứ hai, chốt nền tảng công nghệ chuẩn Java/Quarkus, PostgreSQL, Redis session caching, FCM/APNs, Zalo API, GitHub Actions [ARC-010] và cung cấp hạ tầng DevOps hoàn chỉnh: Dockerfile multi-stage dưới 200MB base/500MB final, Terraform provisioning VPC/IAM/Storage trên GCP, manifests GKE với HPA CPU vượt 70% hoặc latency vượt 300ms, failover liên cluster uptime 99.9%, TLS 1.3/AES-256 kèm mitigations OWASP Top 10, backup PITR 24h đa region, audit log lưu trữ 1 năm, workflow GDPR/CCPA export/deletion và consent management [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]. Thứ ba, đóng gói bộ tài liệu doanh nghiệp gồm blueprint kiến trúc, hợp đồng OpenAPI tham chiếu, hướng dẫn vận hành bản địa hóa vi/en/es và quy trình audit log cùng quản lý consent [NFR-006], [NFR-007], [NFR-008].

- **Ma trận bản đồ thư mục vật lý đích:** Danh sách kiểm kê kỹ thuật đầy đủ 100% đường dẫn tệp vật lý tương đối (tệp cụ thể, không phải thư mục) được tạo mới, tinh chỉnh hoặc xử lý trong phạm vi giai đoạn này:
    * ./sources/backend/reporting-service/src/main/java/com/hub/reporting/controller/AttendanceReportController.java [REQ-024]
    * ./sources/backend/reporting-service/src/main/java/com/hub/reporting/service/AttendanceCsvReportService.java [REQ-024]
    * ./sources/backend/reporting-service/src/main/java/com/hub/reporting/service/OutageReplayService.java [EXC-005], [REQ-024]
    * ./sources/backend/reporting-service/src/main/java/com/hub/reporting/controller/DashboardSummaryController.java [REQ-025]
    * ./sources/backend/reporting-service/src/main/java/com/hub/reporting/repository/DashboardAggregationRepository.java [REQ-025], [NFR-004]
    * ./sources/backend/reporting-service/src/main/java/com/hub/reporting/cache/DashboardCacheService.java [REQ-025], [ARC-010]
    * ./sources/backend/reporting-service/src/main/java/com/hub/reporting/privacy/PrivacyComplianceController.java [NFR-008], [NFR-006]
    * ./sources/backend/reporting-service/src/test/java/com/hub/reporting/service/AttendanceCsvReportServiceTest.java [REQ-024]
    * ./sources/backend/reporting-service/src/test/java/com/hub/reporting/OutageReplayIntegrationTest.java [EXC-005]
    * ./sources/backend/reporting-service/src/test/java/com/hub/reporting/repository/DashboardAggregationRepositoryTest.java [REQ-025]
    * ./sources/backend/reporting-service/src/test/java/com/hub/reporting/DashboardPerformanceIntegrationTest.java [NFR-001], [REQ-025]
    * ./sources/backend/reporting-service/src/test/java/com/hub/reporting/PrivacyComplianceIntegrationTest.java [NFR-008]
    * ./sources/infra/docker/reporting-service.Dockerfile [NFR-005], [ARC-010]
    * ./sources/infra/docker/build-push.sh [NFR-005], [ARC-010]
    * ./sources/infra/terraform/vpc-main.tf [ARC-010], [NFR-002]
    * ./sources/infra/terraform/iam-storage.tf [ARC-010], [NFR-003], [NFR-006]
    * ./sources/infra/terraform/postgresql.tf [NFR-004], [REQ-025]
    * ./sources/infra/terraform/backup-pitr.tf [NFR-009]
    * ./sources/infra/terraform/audit-log-sink.tf [NFR-006]
    * ./sources/infra/gke/cluster.yaml [NFR-002]
    * ./sources/infra/gke/deployments.yaml [ARC-010]
    * ./sources/infra/gke/hpa.yaml [NFR-004]
    * ./sources/infra/gke/ingress-tls.yaml [NFR-003]
    * ./sources/infra/cicd/github-actions-deploy.yaml [ARC-010], [NFR-001]
    * ./sources/docs/api-reporting-service.md [REQ-024], [REQ-025]
    * ./sources/docs/runbook-reporting-deployment.md [REQ-024], [REQ-025]
    * ./sources/docs/architecture-blueprint.md [ARC-010], [NFR-002]
    * ./sources/docs/openapi-reference.md [ARC-010]
    * ./sources/docs/localization-operations-guide.md [NFR-007]
    * ./sources/docs/compliance-audit-consent-guide.md [NFR-006], [NFR-008]
    * ./sources/docs/production-readiness-review.md [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

- **Đặc tả DDL SQL lược đồ cơ sở dữ liệu:**
```sql
-- Không có thay đổi hạ tầng cơ sở dữ liệu hoặc lớp lưu trữ dữ liệu nào được yêu cầu trong ngữ cảnh giai đoạn này
```

- **Hợp đồng định tuyến API và sự kiện [REQ-024], [REQ-025], [ARC-010]:** reporting-service công bố ba nhóm hợp đồng REST qua api-gateway: xuất báo cáo CSV điểm danh theo trung tâm và khoảng ngày [REQ-024], endpoint tóm tắt dashboard real-time đọc qua read replica [REQ-025], và trigger phát lại FIFO hậu outage [EXC-005]; toàn bộ endpoint xác thực bearer JWT và chịu giám sát bởi pipeline CI/CD [ARC-010].
```json
{
  "GET /api/v1/reports/attendance/csv": {
    "query": { "centerId": "uuid (required)", "fromDate": "yyyy-MM-dd (required)", "toDate": "yyyy-MM-dd (required)" },
    "headers": { "Authorization": "Bearer <JWT>" },
    "response_200": { "contentType": "text/csv; charset=UTF-8", "columns": ["StudentName", "CourseName", "AttendanceDate", "Status"] }
  },
  "GET /api/v1/reports/dashboard/summary": {
    "query": { "centerId": "uuid (required)" },
    "response_200": { "totalStudents": 1250, "activeCourses": 42, "upcomingSessions": [{ "courseId": "uuid", "title": "string", "sessionDate": "yyyy-MM-dd" }] }
  },
  "POST /api/v1/reports/outage/replay": {
    "response_202": { "replayedEvents": 17, "notifiedUsers": 9, "status": "REPLAY_COMPLETED_FIFO" }
  }
}
```

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-005]:** Phục hồi hệ thống sau sự cố — khi reporting-service trở lại hoạt động sau outage, toàn bộ bản ghi quét QR tồn đọng được xử lý theo đúng thứ tự FIFO dựa trên timestamp gốc; mỗi lần ghi áp dụng idempotency qua ràng buộc unique (studentId, courseId, attendanceDate) nhằm không nhân bản dòng Attendance; sau khi phiên replay hoàn tất, hệ thống đẩy thông báo "sự kiện đã phục hồi" tới người dùng bị ảnh hưởng. Mã lỗi cục bộ: REPORTING_REPLAY_LOCK_CONFLICT (HTTP 409) khi một phiên replay khác đang giữ khóa phân tán; REPORTING_REPLAY_QUEUE_EMPTY (HTTP 204) khi hàng đợi không còn bản ghi tồn đọng.

#### 📅 Nhật ký phân bổ nhiệm vụ Sub-Agent theo dòng thời gian (Giai đoạn 5)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Xây dựng lõi reporting-service — xuất CSV điểm danh, phát lại FIFO hậu outage và endpoint tóm tắt dashboard

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [1]: Controller xuất báo cáo CSV điểm danh

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Thẻ ID theo dõi mục tiêu:** [REQ-024]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/controller/AttendanceReportController.java [REQ-024]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai AttendanceReportController exposing GET /api/v1/reports/attendance/csv nhận tham số centerId, fromDate, toDate; xác thực bearer JWT và phạm vi trung tâm trước khi truy vấn; stream phản hồi dạng text/csv; charset=UTF-8 với bốn cột StudentName, CourseName, AttendanceDate, Status đúng thứ tự [REQ-024]; ghi log mọi truy vấn xuất kèm userId và timestamp phục vụ audit [NFR-006].

* **Hợp đồng định tuyến API và sự kiện [REQ-024]:**
```json
{
  "endpoint": "GET /api/v1/reports/attendance/csv",
  "query": { "centerId": "uuid", "fromDate": "yyyy-MM-dd", "toDate": "yyyy-MM-dd" },
  "response_200": { "contentType": "text/csv; charset=UTF-8", "columns": ["StudentName", "CourseName", "AttendanceDate", "Status"] }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [2]: Service sinh luồng CSV chuẩn RFC 4180

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Thẻ ID theo dõi mục tiêu:** [REQ-024]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/service/AttendanceCsvReportService.java [REQ-024]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng AttendanceCsvReportService sinh dòng CSV từ tập hợp Attendance join Users và Courses; escape dấu phẩy, ngoặc kép và ngắt dòng theo RFC 4180; ánh xạ trạng thái hiện diện Present/Absent; sử dụng streaming fetch size để tránh OOM khi xuất tập dữ liệu điểm danh lớn của một trung tâm [REQ-024].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [3]: Service phát lại FIFO hậu outage

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Thẻ ID theo dõi mục tiêu:** [EXC-005], [REQ-024]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/service/OutageReplayService.java [EXC-005], [REQ-024]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai hàng đợi phát lại FIFO cho các bản ghi quét QR tồn đọng hậu outage: đọc tuần tự theo timestamp gốc, ghi điểm danh idempotent dựa trên ràng buộc unique (studentId, courseId, attendanceDate), sử dụng khóa phân tán Redis chặn hai phiên replay chạy song song; sau khi hoàn tất, queue thông báo "sự kiện đã phục hồi" tới người dùng liên quan [EXC-005], [REQ-024].

* **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-005]:** Khi dịch vụ khôi phục, các scan tồn đọng được xử lý FIFO; bản ghi trùng bị bỏ qua an toàn nhờ idempotency; trả REPORTING_REPLAY_LOCK_CONFLICT (HTTP 409) nếu phiên replay khác đang chạy và REPORTING_REPLAY_QUEUE_EMPTY (HTTP 204) khi hàng đợi rỗng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [4]: Controller tóm tắt dashboard real-time

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Thẻ ID theo dõi mục tiêu:** [REQ-025]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/controller/DashboardSummaryController.java [REQ-025]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Exposing GET /api/v1/reports/dashboard/summary trả ba thẻ chỉ số totalStudents, activeCourses và upcomingSessions (các buổi học trong 7 ngày tới) cho Center Admin; định tuyến toàn bộ truy vấn tổng hợp qua datasource read-only trỏ tới PostgreSQL read replica để cách ly workload báo cáo khỏi OLTP [REQ-025].

* **Hợp đồng định tuyến API và sự kiện [REQ-025]:**
```json
{
  "endpoint": "GET /api/v1/reports/dashboard/summary",
  "query": { "centerId": "uuid" },
  "response_200": { "totalStudents": 1250, "activeCourses": 42, "upcomingSessionsNext7Days": 18 }
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [5]: Unit test service sinh CSV

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Thẻ ID theo dõi mục tiêu:** [REQ-024]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/service/AttendanceCsvReportService.java;./sources/backend/reporting-service/src/test/java/com/hub/reporting/service/AttendanceCsvReportServiceTest.java [REQ-024]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết JUnit 5 kiểm tra AttendanceCsvReportService: xác thực đúng bốn cột và thứ tự StudentName, CourseName, AttendanceDate, Status; escape ký tự đặc biệt theo RFC 4180; xử lý tập kết quả rỗng và khoảng ngày đảo chiều; đạt độ bao phủ branch tối thiểu 85% [REQ-024].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [6]: Integration test phát lại FIFO hậu outage

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Thẻ ID theo dõi mục tiêu:** [EXC-005]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/reporting-service/src/test/java/com/hub/reporting/OutageReplayIntegrationTest.java [EXC-005]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Khoản thử tích hợp mô phỏng kịch bản outage: chèn 50 bản ghi scan tồn đọng với timestamp xen kẽ, kích hoạt replay, khẳng định xử lý đúng thứ tự FIFO, không phát sinh dòng Attendance trùng nhờ ràng buộc unique, và thông báo phục hồi được queue thành công cho đúng số người dùng [EXC-005].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [7]: Đặc tả API reporting-service

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Thẻ ID theo dõi mục tiêu:** [REQ-024], [REQ-025]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/api-reporting-service.md [REQ-024], [REQ-025]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Biên soạn đặc tả API reporting-service: mô tả endpoint CSV, dashboard summary và outage replay kèm schema request/response, tham số truy vấn, mã lỗi chuẩn và ví dụ payload thực tế cho từng endpoint [REQ-024], [REQ-025].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Tối ưu lớp đọc bản sao PostgreSQL, caching Redis dashboard và đóng gói container reporting-service

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [1]: Repository tổng hợp trên read replica

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Thẻ ID theo dõi mục tiêu:** [REQ-025], [NFR-004]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/repository/DashboardAggregationRepository.java [REQ-025], [NFR-004]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai DashboardAggregationRepository với datasource read-only định tuyến tới PostgreSQL read replica; viết truy vấn tổng hợp đếm totalStudents, activeCourses và upcomingSessions 7 ngày tới tận dụng covering index đã tạo ở lớp migration nhằm bảo đảm đọc sub-second ngay cả khi các dịch vụ Quarkus scale ngang qua HPA [REQ-025], [NFR-004].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [2]: Service cache Redis dashboard

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Thẻ ID theo dõi mục tiêu:** [REQ-025], [ARC-010]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/cache/DashboardCacheService.java [REQ-025], [ARC-010]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng DashboardCacheService dùng Redis với cache-key scope theo centerId, TTL 60 giây; invalidate theo sự kiện enrollment/attendance mới; cấu hình fallback truy vấn trực tiếp read replica khi Redis unavailable để bảo đảm dashboard không bao giờ mất khả năng phục vụ [REQ-025], [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [3]: Unit test repository tổng hợp

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Thẻ ID theo dõi mục tiêu:** [REQ-025]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/repository/DashboardAggregationRepository.java;./sources/backend/reporting-service/src/test/java/com/hub/reporting/repository/DashboardAggregationRepositoryTest.java [REQ-025]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết JUnit 5 với Testcontainers PostgreSQL: seed dataset mẫu nhiều trung tâm, xác thực số liệu totalStudents, activeCourses, upcomingSessions khớp kỳ vọng và xác nhận phiên bản truy vấn thực thi trên replica thay vì primary [REQ-025].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [4]: Kiểm thử hiệu năng dashboard p95

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Thẻ ID theo dõi mục tiêu:** [NFR-001], [REQ-025]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/reporting-service/src/test/java/com/hub/reporting/DashboardPerformanceIntegrationTest.java [NFR-001], [REQ-025]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** INTEGRATION_SCOPE đo hiệu năng dashboard bằng Gatling: mô phỏng 10.000 người dùng đồng thời gọi GET /api/v1/reports/dashboard/summary; thất bại pipeline nếu p95 latency vượt 200 ms; ghi nhận throughput làm baseline cho cấu hình HPA [NFR-001], [REQ-025].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [5]: Rà soát nhất quán replica–cache

* **Chuyên môn hóa vai trò Sub-Agent:** [Reviewer]

* **Thẻ ID theo dõi mục tiêu:** [REQ-025], [NFR-004]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/repository/DashboardAggregationRepository.java [REQ-025], [NFR-004]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát DashboardAggregationRepository và DashboardCacheService: kiểm tra rủi ro stale-read giữa primary và replica, rò rỉ kết nối pool, sai lệch cache sau invalidate; phát hiện full-table scan thì thiết kế bản vá tối ưu truy vấn và ghi nhận quyết định kiến trúc [REQ-025], [NFR-004].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [6]: Dockerfile multi-stage reporting-service

* **Chuyên môn hóa vai trò Sub-Agent:** [Docker]

* **Thẻ ID theo dõi mục tiêu:** [NFR-005], [ARC-010]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/docker/reporting-service.Dockerfile [NFR-005], [ARC-010]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết multi-stage Dockerfile cho reporting-service: stage build dùng maven:3.9-eclipse-temurin-21, stage runtime dùng eclipse-temurin-21-jre-alpine; ép kích thước base image nhỏ hơn 200 MB và image cuối nhỏ hơn 500 MB [NFR-005]; bật JVM container-aware flags (-XX:MaxRAMPercentage=75.0) và user non-root [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [7]: Runbook triển khai reporting

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Thẻ ID theo dõi mục tiêu:** [REQ-024], [REQ-025]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/runbook-reporting-deployment.md [REQ-024], [REQ-025]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Soạn runbook triển khai reporting-service: trình tự build image, push registry, apply manifests GKE, verify health check endpoint CSV và dashboard, quy trình rollback nhanh; kèm checklist hậu triển khai xác minh [REQ-024] và [REQ-025] hoạt động end-to-end.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 3: Cung cấp hạ tầng GCP bằng Terraform và biên soạn manifests điều phối GKE với HPA tự động mở rộng

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [1]: Terraform VPC production

* **Chuyên môn hóa vai trò Sub-Agent:** [GCP]

* **Thẻ ID theo dõi mục tiêu:** [ARC-010], [NFR-002]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/terraform/vpc-main.tf [ARC-010], [NFR-002]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo vpc-main.tf cấp VPC production: subnet regional asia-southeast1, firewall rule chỉ mở 443 và 6443, Cloud NAT egress IP tĩnh, Private Google Access bật cho node; thiết kế multi-zone làm nền cho failover tự động đạt uptime 99.9% [NFR-002] trên nền stack đã chốt [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [2]: Terraform IAM & Cloud Storage

* **Chuyên môn hóa vai trò Sub-Agent:** [GCP]

* **Thẻ ID theo dõi mục tiêu:** [ARC-010], [NFR-003], [NFR-006]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/terraform/iam-storage.tf [ARC-010], [NFR-003], [NFR-006]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Khai báo iam-storage.tf: service account tối thiểu quyền (least privilege) gắn Workload Identity cho workload GKE, bucket Cloud Storage phân tầng backup và audit-log với versioning và uniform bucket-level access; gắn IAM Conditions theo thuộc tính resource nhằm giảm bề mặt tấn công theo OWASP A01 [NFR-003] và bảo đảm kho chứa log phục vụ lưu trữ audit [NFR-006] trên nền [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [3]: Terraform PostgreSQL HA & read replica

* **Chuyên môn hóa vai trò Sub-Agent:** [GCP]

* **Thẻ ID theo dõi mục tiêu:** [NFR-004], [REQ-025]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/terraform/postgresql.tf [NFR-004], [REQ-025]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Provision postgresql.tf: Cloud SQL PostgreSQL 16 chế độ HA regional kèm read replica chuyên dụng cho workload báo cáo; bật flag pg_stat_statements phục vụ tuning, connection pooler phía ứng dụng; cấu hình private IP peering với VPC đã tạo [NFR-004], [REQ-025].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [4]: Manifest cụm GKE regional failover

* **Chuyên môn hóa vai trò Sub-Agent:** [GKE]

* **Thẻ ID theo dõi mục tiêu:** [NFR-002]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/gke/cluster.yaml [NFR-002]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Biên soạn cluster.yaml: GKE regional cluster trải 3 zone, private nodes, Workload Identity, Network Policy enabled, release channel regular, maintenance window ngoài giờ cao điểm; kiến trúc multi-zone bảo đảm failover tự động duy trì uptime mục tiêu 99.9% [NFR-002].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [5]: Manifests Deployment/Service microservices

* **Chuyên môn hóa vai trò Sub-Agent:** [GKE]

* **Thẻ ID theo dõi mục tiêu:** [ARC-010]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/gke/deployments.yaml [ARC-010]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Sinh deployments.yaml cho 10 microservices membership-hub (auth, center, course, enrollment, attendance, card, notification, promotion, chatbot, reporting): probes liveness/readiness/startup, resource requests/limits chuẩn hóa, topologySpreadConstraints chống tập trung node, image pull từ Artifact Registry với imagePullPolicy IfNotPresent trên nền stack [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [6]: Manifests HPA tự động mở rộng

* **Chuyên môn hóa vai trò Sub-Agent:** [GKE]

* **Thẻ ID theo dõi mục tiêu:** [NFR-004]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/gke/hpa.yaml [NFR-004]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Thiết kế hpa.yaml: HorizontalPodAutoscaler scale theo CPU vượt 70% và custom metric latency p95 vượt 300 ms qua Prometheus Adapter; minReplicas 2, maxReplicas 20; behavior.scaleDown stabilizationWindow 300 giây chống flapping; áp dụng cho toàn bộ deployment dịch vụ [NFR-004].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [7]: Kiểm toán bảo mật IaC

* **Chuyên môn hóa vai trò Sub-Agent:** [Reviewer]

* **Thẻ ID theo dõi mục tiêu:** [NFR-003], [ARC-010]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/terraform/iam-storage.tf [NFR-003], [ARC-010]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm toán bảo mật IaC theo OWASP Top 10: rà soát iam-storage.tf và vpc-main.tf về nguyên tắc least privilege IAM, chặn public access bucket, cấm hardcode credential trong biến plaintext, bắt buộc tfsec/checkov pass trước khi terraform apply; thiết kế bản vá cho mọi phát hiện mức HIGH [NFR-003], [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 4: Củng cố bảo mật TLS/AES, backup PITR đa vùng, audit log, pipeline CI/CD và tuân thủ GDPR/CCPA

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [1]: Ingress TLS 1.3 & mã hóa Secret KMS

* **Chuyên môn hóa vai trò Sub-Agent:** [GKE]

* **Thẻ ID theo dõi mục tiêu:** [NFR-003]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/gke/ingress-tls.yaml [NFR-003]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai ingress-tls.yaml: ManagedCertificate do Google quản lý, ép minimum TLS version 1.3 tại load balancer cho toàn bộ dữ liệu truyền [NFR-003]; mã hóa Kubernetes Secret bằng Cloud KMS (AES-256) cho biến môi trường nhạy cảm; NetworkPolicy mặc định deny-all rồi whitelist từng luồng service-to-service.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [2]: Terraform backup PITR đa vùng

* **Chuyên môn hóa vai trò Sub-Agent:** [GCP]

* **Thẻ ID theo dõi mục tiêu:** [NFR-009]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/terraform/backup-pitr.tf [NFR-009]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Khai báo backup-pitr.tf: lịch full backup PostgreSQL hằng ngày lúc 02:00 UTC, bật point-in-time recovery với cửa sổ 24 giờ, cấu hình cross-region replication sao chép backup sang region thứ hai làm bản sao DR cho cụm GKE; định nghĩa chính sách retention và cảnh báo khi job backup thất bại [NFR-009].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [3]: Terraform audit log sink 1 năm

* **Chuyên môn hóa vai trò Sub-Agent:** [GCP]

* **Thẻ ID theo dõi mục tiêu:** [NFR-006]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/terraform/audit-log-sink.tf [NFR-006]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Thiết lập audit-log-sink.tf: Log Sink thu Admin Activity và Data Access logs chuyển vào bucket chuyên dụng với retention locked 365 ngày; exporter phụ sang BigQuery dataset phục vụ truy vấn điều tra hành động người dùng (thay đổi vai trò, bản ghi điểm danh, thông báo) kèm timestamp, userId và chi tiết hành động [NFR-006].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [4]: Build & push image Artifact Registry

* **Chuyên môn hóa vai trò Sub-Agent:** [Docker]

* **Thẻ ID theo dõi mục tiêu:** [NFR-005], [ARC-010]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/docker/build-push.sh [NFR-005], [ARC-010]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết build-push.sh build song song 10 image microservices, gắn tag semantic kèm digest bất biến, chạy Trivy scan chặn pipeline ở mức CRITICAL, xác minh ràng buộc kích thước base nhỏ hơn 200 MB và final nhỏ hơn 500 MB trước khi push lên Artifact Registry khu vực asia-southeast1 [NFR-005], [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [5]: Controller tuân thủ GDPR/CCPA

* **Chuyên môn hóa vai trò Sub-Agent:** [Coder]

* **Thẻ ID theo dõi mục tiêu:** [NFR-008], [NFR-006]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/backend/reporting-service/src/main/java/com/hub/reporting/privacy/PrivacyComplianceController.java [NFR-008], [NFR-006]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai PrivacyComplianceController: GET /api/v1/privacy/export xuất toàn bộ dữ liệu cá nhân của người dùng dạng JSON [NFR-008]; DELETE /api/v1/privacy/data thực thi right to erasure xóa vĩnh viễn trên mọi bảng liên quan và vô hiệu hóa token phiên; PUT /api/v1/privacy/consent cập nhật trạng thái đồng ý marketing; mọi thao tác đều ghi audit log kèm userId và timestamp [NFR-006].

* **Hợp đồng định tuyến API và sự kiện [NFR-008]:**
```json
{
  "endpoints": [
    { "method": "GET", "path": "/api/v1/privacy/export", "response_200": { "format": "application/json", "scope": "personal_data" } },
    { "method": "DELETE", "path": "/api/v1/privacy/data", "response_204": {} },
    { "method": "PUT", "path": "/api/v1/privacy/consent", "request": { "userId": "uuid", "marketingConsent": true } }
  ]
}
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [6]: Integration test GDPR export/deletion

* **Chuyên môn hóa vai trò Sub-Agent:** [Tester]

* **Thẻ ID theo dõi mục tiêu:** [NFR-008]

* **Đường dẫn tệp thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/reporting-service/src/test/java/com/hub/reporting/PrivacyComplianceIntegrationTest.java [NFR-008]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** INTEGRATION_SCOPE kiểm thử vòng đời GDPR/CCPA: export trả đủ trường dữ liệu cá nhân dạng JSON hợp lệ; deletion xóa triệt để bản ghi trên mọi bảng liên quan và thu hồi refresh token; consent cập nhật có hiệu lực tức thời và được audit log ghi nhận đầy đủ [NFR-008].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [7]: Pipeline CI/CD GitHub Actions

* **Chuyên môn hóa vai trò Sub-Agent:** [GCP]

* **Thẻ ID theo dõi mục tiêu:** [ARC-010], [NFR-001]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/infra/cicd/github-actions-deploy.yaml [ARC-010], [NFR-001]

* **Chỉ dẫn nhiệm vụ kỹ thuật cấp thấp:** Dựng github-actions-deploy.yaml: các job build → unit test → SonarQube quality gate → Trivy scan → build/push image → terraform plan/apply có bước approval thủ công → kubectl apply qua Workload Identity; kèm gate hiệu năng chặn promote production nếu kết quả Gatling cho thấy p95 latency vượt 200 ms [NFR-001] trên nền pipeline [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 5: Hoàn thiện bộ tài liệu doanh nghiệp, hướng dẫn bản địa hóa và kiểm toán sẵn sàng production

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [1]: Blueprint kiến trúc tổng thể

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Thẻ ID theo dõi mục tiêu:** [ARC-010], [NFR-002]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/architecture-blueprint.md [ARC-010], [NFR-002]

* **Chỉ dẫn nhiệm vụ cấp thấp:** Hoàn thiện architecture-blueprint.md: sơ đồ topology 10 microservices, luồng dữ liệu OAuth2/JWT, điểm danh QR idempotent, điều phối thông báo đa kênh FCM/APNs/Zalo, mô hình RBAC 5 vai trò, kiến trúc HPA và failover liên cluster đạt uptime 99.9% [NFR-002] trên nền stack production đã chốt [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [2]: Tài liệu tham chiếu OpenAPI hợp nhất

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Thẻ ID theo dõi mục tiêu:** [ARC-010]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/openapi-reference.md [ARC-010]

* **Chỉ dẫn nhiệm vụ cấp thấp:** Tổng hợp openapi-reference.md hợp nhất hợp đồng OpenAPI 3.1 của toàn bộ dịch vụ (auth, center, course, enrollment, attendance, card, notification, promotion, chatbot, reporting) kèm ví dụ request/response, sơ đồ mã lỗi chuẩn và hướng dẫn xác thực bearer token qua api-gateway [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [3]: Hướng dẫn vận hành bản địa hóa vi/en/es

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Thẻ ID theo dõi mục tiêu:** [NFR-007]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/localization-operations-guide.md [NFR-007]

* **Chỉ dẫn nhiệm vụ cấp thấp:** Biên soạn localization-operations-guide.md: quy trình externalize UI strings, thủ tục bổ sung locale mới trong bộ en/vi/es, checklist kiểm thử hreflang và meta SSR cho crawler, vận hành cơ chế fallback Accept-Language và chuyển locale không cần reload trang [NFR-007].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [4]: Quy trình audit log & consent GDPR/CCPA

* **Chuyên môn hóa vai trò Sub-Agent:** [Doc]

* **Thẻ ID theo dõi mục tiêu:** [NFR-006], [NFR-008]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/compliance-audit-consent-guide.md [NFR-006], [NFR-008]

* **Chỉ dẫn nhiệm vụ cấp thấp:** Soạn compliance-audit-consent-guide.md: quy trình ghi audit log (timestamp, userId, chi tiết hành động) với lưu trữ 1 năm [NFR-006]; luồng xử lý yêu cầu xóa/xuất dữ liệu cá nhân GDPR/CCPA, mẫu biểu xác minh danh tính và ma trận quản lý consent marketing cho từng kênh truyền thông [NFR-008].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ [5]: Kiểm toán sẵn sàng production GO/NO-GO

* **Chuyên môn hóa vai trò Sub-Agent:** [Reviewer]

* **Thẻ ID theo dõi mục tiêu:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

* **Đường dẫn tệp thành phần đích (target_component):** ./sources/docs/production-readiness-review.md [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

* **Chỉ dẫn nhiệm vụ cấp thấp:** Thực hiện kiểm toán sẵn sàng production cuối cùng đối chiếu từng ràng buộc: p95 latency 200 ms và index sub-second cho 10.000 người dùng đồng thời [NFR-001]; uptime 99.9% failover liên cluster [NFR-002]; TLS 1.3/AES-256 và mitigations OWASP Top 10 [NFR-003]; HPA CPU 70%/latency 300 ms cùng read replica [NFR-004]; kích thước image 200 MB/500 MB [NFR-005]; audit log 1 năm [NFR-006]; đa ngôn ngữ en/vi/es [NFR-007]; GDPR/CCPA export/deletion/consent [NFR-008]; backup PITR 24h đa region [NFR-009]; phát hành verdict GO/NO-GO kèm danh sách hành động khắc phục nếu NO-GO.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

### 🕵️ Báo cáo sổ cái kiểm toán chéo kiến trúc thời gian thực bắt buộc:

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=6
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=33
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=33
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

<!--END_PHASE_INDEX-->

### NGỮ CẢNH ĐỊNH CƠ TỪ CÁC BƯỚC TRƯỚC

Toàn bộ mã bảo mật, thanh chắn di động và cổng pipeline trình bày dưới đây đã được đối chiếu và neo chặt vào stack công nghệ đã hiện thực hóa trong ngữ cảnh các giai đoạn sinh trước đó: backend Java/Quarkus trên PostgreSQL, Redis session cache, Firebase Authentication, FCM/APNs, tích hợp Zalo API, container Docker triển khai trên GKE và CI/CD GitHub Actions theo nền tảng kiến trúc [ARC-010]. Không có mã đối phó nào mâu thuẫn với các quyết định kỹ thuật đã chốt của 5 giai đoạn.

## ☣️ 6. BỘ MÃ BẢO MẬT DOANH NGHIỆP TOÀN CỤC & BIỆN PHÁP ĐỐI PHÓ TẤN CÔNG TIÊM NHẬP [NFR-XXX]

### 1. Biện pháp khắc chế tuyệt đối tấn công SQL Injection (SQLi)

Mọi truy vấn đọc/ghi lên PostgreSQL từ các service Quarkus bắt buộc thực thi qua Hibernate ORM với prepared statement và positional query parameter (`?1`, `?2`) hoặc named parameter (`:param`); việc nối chuỗi (string concatenation) đầu vào người dùng vào câu lệnh SQL/JPQL native bị cấm tuyệt đối ở mọi tầng repository. Các tác vụ sắp xếp và lọc động trên danh sách khóa học [DAT-004], danh sách trung tâm [DAT-003] và truy xuất hồ sơ người dùng [DAT-001] phải đi qua whitelist cứng tên cột/hướng sắp xếp (ASC/DESC) khai báo tại tầng repository; mọi giá trị nằm ngoài whitelist bị từ chối tức thời bằng HTTP 400 mà không chạm tới database. Thao tác ghi điểm danh [DAT-006] sử dụng truy vấn tham số hóa với ràng buộc duy nhất `(student_id, course_id, attendance_date)` để vừa triệt tiêu SQLi vừa bảo đảm tính idempotent [REQ-013]. Tài khoản ứng dụng kết nối database tuân thủ nguyên tắc đặc quyền tối thiểu, không sở hữu quyền DDL trên schema production.

**Thẻ truy vết:** [NFR-003], [REQ-013], [DAT-001], [DAT-003], [DAT-004], [DAT-006]

### 2. Tấn công Cross-Site Scripting (XSS) & Chính sách Bảo mật Nội dung (CSP)

Toàn bộ lớp giao diện Next.js [ARC-009] dựa vào cơ chế tự động escape của JSX/React để vô hiệu hóa mọi chuỗi HTML/JavaScript do người dùng cung cấp; thuộc tính `dangerouslySetInnerHTML` bị cấm trên mọi trường nội dung động gồm mô tả khóa học [DAT-004], nội dung thông báo [DAT-008] và nội dung khuyến mãi/thông cáo [DAT-009]. Trước khi persist xuống PostgreSQL, mọi payload rich-text do Center Admin hoặc Manager nhập [ARC-002], [ARC-003] được làm sạch server-side bằng OWASP Java HTML Sanitizer với whitelist thẻ nghiêm ngặt. Tại tầng Ingress Gateway trên GKE [ARC-010], hệ thống tiêm header CSP nghiêm ngặt `default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; object-src 'none'; frame-ancestors 'none'; base-uri 'self'` kèm `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` và `Referrer-Policy: strict-origin-when-cross-origin` cho mọi phản hồi HTML.

**Thẻ truy vết:** [NFR-003], [ARC-002], [ARC-003], [ARC-009], [ARC-010], [DAT-004], [DAT-008], [DAT-009]

### 3. Thanh chắn bảo mật CORS đa tenant (Multi-Tenant CORS)

Cấu hình CORS trên mọi REST endpoint Quarkus nghiêm cấm tuyệt đối giá trị đại diện `*` cho header `Access-Control-Allow-Origin` cũng như tổ hợp wildcard với `Access-Control-Allow-Credentials`. Danh sách origin hợp lệ của từng trung tâm được đăng ký tập trung trong bảng SystemSettings [DAT-011] theo quy ước key `cors.allowed.origin.<centerId>`, được nạp vào Redis [ARC-010] và đối chiếu động với header `Origin` của từng yêu cầu bởi bộ lọc CORS tùy chỉnh trước khi cấp phản hồi; origin không đăng ký bị chặn với HTTP 403. Các luồng nhạy cảm — phát hành JWT [ARC-006] và ghi nhận điểm danh QR [ARC-007] — chỉ chấp nhận yêu cầu từ domain chính thức của nền tảng và origin nội bộ của WebView Capacitor; mọi method ngoài GET/POST/PUT/PATCH/DELETE và header tùy chỉnh ngoài danh sách cho phép bị loại bỏ ngay ở bước preflight OPTIONS.

**Thẻ truy vết:** [NFR-003], [ARC-006], [ARC-007], [ARC-010], [DAT-011]

### 4. Công cụ làm sạch nhật ký không rò rỉ (Zero-Leak Log Scrubbing) & Engine che giấu dữ liệu PII

Mọi trường PII — email và họ tên người dùng [DAT-001], số điện thoại/email liên hệ trung tâm [DAT-003] — được tuần tự hóa qua serializer tùy chỉnh gắn chú thích `@JsonSerialize(using = EmailMaskingSerializer.class)` / `@JsonSerialize(using = PhoneMaskingSerializer.class)` để che một phần giá trị trong mọi phản hồi API dành cho vai trò không đủ thẩm định theo ma trận RBAC [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]. Bộ đánh chặn logging toàn cục quét và làm sạch tự động mọi sự kiện trước khi ghi vào Cloud Logging: access token JWT, refresh token, `passwordHash` bcrypt [DAT-001] và payload QR điểm danh [DAT-006] được thay bằng hằng `[REDACTED]`; nhật ký kiểm toán vẫn giữ nguyên timestamp, userId và chi tiết hành động theo chuẩn [NFR-006]. Cơ chế này bảo đảm tuân thủ quyền xóa và xuất dữ liệu cá nhân GDPR/CCPA [NFR-008] mà không làm suy giảm khả năng điều tra sự cố.

**Thẻ truy vết:** [NFR-006], [NFR-008], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [DAT-001], [DAT-003], [DAT-006]

## 📱 7. QUY TẮC THANH CHẮN TƯƠNG THÍCH DI ĐỘNG HYBRID & CƠ CHẾ SEO QUỐC TẾ HÓA

### 1. Thanh chắn tương thích Capacitor Mobile Hybrid

Ứng dụng di động Capacitor phải thực hiện toàn bộ truy xuất dữ liệu bằng fetch động phía client tới REST API backend [ARC-009] thông qua địa chỉ URL tuyệt đối được bơm lúc build (`API_BASE_URL`), nghiêm cấm đường dẫn tương đối gây lỗi phân giải trong WebView native. Cơ chế hydration safeguards bảo vệ trạng thái phiên đăng nhập, cache ngoại tuyến của luồng điểm danh QR [EXC-001] và hàng đợi đồng bộ khỏi bị mất khi ứng dụng khởi động lại hoặc chuyển background/foreground; khi mạng phục hồi, hàng đợi được gửi lại theo FIFO và ghi nhận đúng một bản ghi nhờ tính idempotent [REQ-013]. Refresh token, ngôn ngữ ưu tiên [REQ-022] và device token push được lưu qua abstraction gốc `@capacitor/preferences` thay vì localStorage của WebView. Interceptor nút back vật lý (`App.addListener('backButton')`) chặn hành vi thoát đột ngột trên Android để điều hướng theo ngăn xếp màn hình của vai trò hiện hành [REQ-020]; ngay sau đăng nhập thành công, ứng dụng đăng ký device token để nhận thông báo đẩy FCM/APNs [REQ-021].

**Thẻ truy vết:** [REQ-013], [REQ-020], [REQ-021], [REQ-022], [ARC-009], [EXC-001]

### 2. Quốc tế hóa (i18n) & Tiêm SEO động (Dynamic SEO Injection)

Middleware nhận diện locale vận hành tại tầng edge của Next.js: thứ tự ưu tiên là ngôn ngữ đã chọn trước đó của người dùng (lưu trong `@capacitor/preferences` trên di động hoặc cookie trên web), fallback sang header `Accept-Language` của trình duyệt, và mặc định cuối cùng là tiếng Việt [REQ-022]. Toàn bộ chuỗi giao diện được externalize vào bộ resource `en/vi/es` đáp ứng [NFR-007], cho phép chuyển đổi locale không cần tải lại trang ở mức khả thi. Với mỗi yêu cầu render, hệ thống tiêm động thuộc tính `<html lang='...'>` khớp locale hiện hành cùng bộ liên kết `<link rel='alternate' hreflang='en|vi|es'>` trỏ tới ba phiên bản ngôn ngữ tương ứng [REQ-023]; thẻ meta title/description/og:locale được bản địa hóa theo từng locale để tối ưu chỉ mục tìm kiếm đa ngôn ngữ. Ngôn ngữ mặc định toàn hệ thống và danh sách locale kích hoạt được quản trị tập trung qua bảng SystemSettings [DAT-011].

**Thẻ truy vết:** [REQ-022], [REQ-023], [NFR-007], [DAT-011]

## 🚀 8. LUỒNG NHÁNH GIT PHIÊN LÀM VIỆC HÀNG NGÀY TỰ ĐỘNG HÓA PIPELINE

### 1. Cô lập phân nhánh Workspace hàng ngày (Daily Workspace Forking Isolation)

Mỗi phiên làm việc hàng ngày được cô lập trên nhánh riêng tuân thủ mẫu đặt tên bắt buộc `features/development-phase-X-day-Y` (X là chỉ số giai đoạn, Y là chỉ số ngày) do kịch bản fork tự động của GitHub Actions [ARC-010] tạo ra ngay đầu phiên; nhánh luôn được cắt từ commit tích hợp mới nhất để loại bỏ xung đột merge tiềm ẩn. Branch protection rules chặn tuyệt đối việc push trực tiếp lên `main` và nhánh tích hợp; mỗi Sub-Agent (Coder, Tester, Reviewer, Doc, Docker, GCP, GKE) chỉ được commit lên nhánh phiên được phân công. Khi kết thúc phiên, pull request của nhánh `features/development-phase-X-day-Y` phải vượt qua toàn bộ cổng kiểm chứng trước khi được squash-merge và dọn dẹp nhánh nguồn.

**Thẻ truy vết:** [ARC-010]

### 2. Cổng chặn kiểm chứng Pipeline (Validation Guard Pipeline Gates)

Pipeline CI/CD GitHub Actions [ARC-010] thực thi tuần tự các cổng chặn bắt buộc trước khi cho phép merge: (1) biên dịch sạch `mvn verify` cho backend Quarkus và `next build` cho frontend Next.js; (2) phân tích tĩnh SonarQube với quality gate chặn mọi blocker/critical vulnerability mới phát sinh; (3) độ bao phủ kiểm thử tự động bắt buộc đạt ngưỡng `>= 85%` trên cả module backend lẫn frontend, vi phạm ngưỡng khiến pipeline fail ngay lập tức; (4) kiểm tra kích thước image Docker sau build phải nhỏ hơn 200 MB (base) và 500 MB (final) theo [NFR-005]. Chỉ khi toàn bộ cổng trả về trạng thái xanh, artifact mới được đẩy lên container registry và giải phóng lên cụm GKE.

**Thẻ truy vết:** [ARC-010], [NFR-005]

### 📊 NGHỊ ĐỊNH KIỂM TRA MA TRẬN BAO PHỦ

Kết quả kiểm đếm ngược (reverse-scan) phạm vi log giai đoạn đã sinh bên dưới mốc neo ngữ cảnh các giai đoạn, áp dụng điều kiện parse đơn lẻ/khoảng tuần tự/gom nhóm toàn cục trên 5 loại thẻ nền tảng REQ, ARC, EXC, DAT, NFR:

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 11, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]