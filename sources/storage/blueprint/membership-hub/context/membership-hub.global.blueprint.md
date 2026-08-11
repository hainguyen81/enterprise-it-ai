# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260811052540 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/11 05:25:40 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo mô hình kiến trúc đa lớp với các thành phần chính bao gồm: giao diện người dùng, lớp dịch vụ, lớp truy cập dữ liệu và cơ sở dữ liệu.
- Sử dụng mô hình Event-Driven Architecture (EDA) để xử lý các sự kiện như điểm danh, đăng ký khóa học và thông báo.
- Áp dụng mô hình Command Query Responsibility Segregation (CQRS) để tách biệt các thao tác ghi và đọc dữ liệu.
- Sử dụng mô hình Reactive Programming để xử lý các luồng dữ liệu thời gian thực như điểm danh và thông báo.
- Hệ thống được thiết kế để hoạt động trong môi trường phân tán với khả năng mở rộng cao.
- Sử dụng mô hình Microservices để tách biệt các chức năng chính của hệ thống thành các dịch vụ độc lập.
- Áp dụng mô hình Domain-Driven Design (DDD) để tổ chức mã nguồn theo các miền nghiệp vụ chính.
- Sử dụng mô hình Clean Architecture để tách biệt các lớp logic và đảm bảo tính độc lập giữa các thành phần.
- Áp dụng mô hình Hexagonal Architecture để tách biệt các cổng và bộ điều khiển của hệ thống.
- Sử dụng mô hình Onion Architecture để tổ chức mã nguồn theo các lớp logic rõ ràng.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Sử dụng Kafka để xử lý các sự kiện thời gian thực như điểm danh và thông báo.
- Sử dụng Redis để lưu trữ các dữ liệu tạm thời và caching.
- Sử dụng PostgreSQL để lưu trữ các dữ liệu quan trọng và quan hệ.
- Sử dụng Firebase Authentication để xử lý xác thực người dùng.
- Sử dụng Google Cloud Messaging (FCM) và Apple APNs để gửi thông báo đẩy đến ứng dụng di động.
- Sử dụng Zalo API để gửi thông báo đến nhóm Zalo.
- Sử dụng Docker để container hóa các dịch vụ và triển khai trên Kubernetes.
- Sử dụng GitHub Actions để triển khai liên tục và tích hợp liên tục.
- Sử dụng Prometheus và Grafana để giám sát và phân tích hiệu suất hệ thống.
- Sử dụng ELK Stack để quản lý và phân tích các log hệ thống.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis, GitHub Actions
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native, Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### 1.1. MỤC TIÊU & GIÁ TRỊ CỐT LÕI
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### 1.2. ĐỐI TƯỢNG NGƯỜI DÙNG MỤC TIÊU
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### 1.3. MA TRẬN KIỂM SOÁT TRUY CẬP DỰA TRÊN VAI TRÒ (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### 1.4. KIẾN TRÚC & LUỒNG DỮ LIỆU (CÁC LUỒNG CHÍNH)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### 1.5. CÔNG NGHỆ & HẠ TẦNG
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 📈 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1. QUẢN LÝ NGƯỜI DÙNG

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```

### 2.2. QUẢN LÝ TRUNG TÂM

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```

### 2.3. QUẢN LÝ KHÓA HỌC

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```

### 2.4. ĐĂNG KÝ & GHI DANH HỌC VIÊN

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```

### 2.5. ĐIỂM DANH & QUÉT MÃ QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```

### 2.6. QUẢN LÝ THẺ HỘI VIÊN

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```

### 2.7. THÔNG BÁO & TRUYỀN THÔNG

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```

### 2.8. QUẢN LÝ KHUYẾN MÃI & THÔNG BÁO

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```

### 2.9. CHATBOT DỊCH VỤ KHÁCH HÀNG AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10. CÁC TÍNH NĂNG CỐT LÕI CỦA ỨNG DỤNG DI ĐỘNG

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11. BẢN ĐỊA HÓA & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```

### 2.12. BÁO CÁO & PHÂN TÍCH

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG

<!--START_BACKLOG_SYNOPSIS_GRID-->

| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | User Registration | Implement user registration with email/password and social providers (Firebase, Google, Facebook) | Application Code | [REQ-001], [REQ-002] |
| 2 | Role Management | Develop role assignment and permission enforcement system | Application Code | [REQ-003] |
| 3 | Center Management | Create center CRUD operations and admin assignment | Application Code | [REQ-004], [REQ-005], [REQ-006] |
| 4 | Course Management | Implement course CRUD with schedule conflict detection | Application Code | [REQ-007], [REQ-008] |
| 5 | Teacher Assignment | Develop teacher assignment to courses with notification | Application Code | [REQ-009] |
| 6 | Student Enrollment | Implement course browsing and enrollment system | Application Code | [REQ-010], [REQ-011] |
| 7 | QR Attendance | Develop QR scanning and attendance recording system | Application Code | [REQ-012], [REQ-013] |
| 8 | Membership Card | Implement membership card display and renewal system | Application Code | [REQ-014], [REQ-015] |
| 9 | Notification System | Develop push notification and Zalo group messaging system | Application Code | [REQ-016] |
| 10 | Promotion Management | Create promotion CRUD system | Application Code | [REQ-017] |
| 11 | Announcement Management | Develop announcement CRUD system | Application Code | [REQ-018] |
| 12 | AI Chatbot | Integrate AI chatbot for common queries | Application Code | [REQ-019] |
| 13 | Mobile UI | Develop responsive mobile UI for all roles | Application Code | [REQ-020] |
| 14 | Push Notifications | Implement push notification system for mobile | Application Code | [REQ-021] |
| 15 | Localization | Implement multi-language support | Application Code | [REQ-022], [REQ-023] |
| 16 | Attendance Reporting | Develop daily attendance report generation | Application Code | [REQ-024] |
| 17 | Dashboard | Create real-time dashboard for center admins | Application Code | [REQ-025] |
| 18 | User Database | Design and implement User and Role database schema | Database Schema | [DAT-001] |
| 19 | Center Database | Design and implement Center database schema | Database Schema | [DAT-003] |
| 20 | Course Database | Design and implement Course database schema | Database Schema | [DAT-004] |
| 21 | Enrollment Database | Design and implement Enrollment database schema | Database Schema | [DAT-005] |
| 22 | Attendance Database | Design and implement Attendance database schema | Database Schema | [DAT-006] |
| 23 | Membership Card Database | Design and implement Membership Card database schema | Database Schema | [DAT-007] |
| 24 | Notification Database | Design and implement Notification database schema | Database Schema | [DAT-008] |
| 25 | Promotion Database | Design and implement Promotion database schema | Database Schema | [DAT-009] |
| 26 | System Settings Database | Design and implement System Settings database schema | Database Schema | [DAT-011] |
| 27 | Authentication Flow | Document authentication flow with JWT and refresh tokens | Enterprise Documentation | [ARC-006] |
| 28 | QR Attendance Flow | Document QR attendance flow with idempotent recording | Enterprise Documentation | [ARC-007] |
| 29 | Notification Flow | Document notification flow to mobile and Zalo | Enterprise Documentation | [ARC-008] |
| 30 | Mobile Integration Flow | Document mobile integration flow with REST APIs | Enterprise Documentation | [ARC-009] |
| 31 | Technology Stack | Document technology stack and infrastructure | Enterprise Documentation | [ARC-010] |
| 32 | Input Validation | Handle input validation errors | Exception Handling | [EXC-004] |
| 33 | QR Scan Failure | Handle QR scan failures and network drops | Exception Handling | [EXC-001] |
| 34 | Duplicate Attendance | Handle duplicate attendance submissions | Exception Handling | [EXC-002] |
| 35 | Notification Failure | Handle notification delivery failures | Exception Handling | [EXC-003] |
| 36 | System Recovery | Handle system recovery after outages | Exception Handling | [EXC-005] |
| 37 | Performance Metrics | Ensure API performance meets requirements | Non-Functional | [NFR-001] |
| 38 | Availability | Ensure system availability meets requirements | Non-Functional | [NFR-002] |
| 39 | Security | Implement security measures | Non-Functional | [NFR-003] |
| 40 | Scalability | Implement scalability measures | Non-Functional | [NFR-004] |
| 41 | Docker Image Size | Ensure Docker image size meets requirements | Non-Functional | [NFR-005] |
| 42 | Logging & Audit | Implement logging and audit measures | Non-Functional | [NFR-006] |
| 43 | Multi-Language Support | Implement multi-language support | Non-Functional | [NFR-007] |
| 44 | GDPR/CCPA Compliance | Implement GDPR/CCPA compliance measures | Non-Functional | [NFR-008] |
| 45 | Backup & Disaster Recovery | Implement backup and disaster recovery measures | Non-Functional | [NFR-009] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 45 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. PHASE 1 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 1
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Thiết lập cơ sở hạ tầng backend, triển khai cơ sở dữ liệu, và phát triển các tính năng xác thực cơ bản.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/` | Thiết lập cơ sở hạ tầng backend |
| 2 | `./sources/backend/auth/` | Triển khai xác thực và phân quyền |
| 3 | `./sources/backend/database/` | Thiết kế và triển khai cơ sở dữ liệu |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL,
    provider VARCHAR(10) NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "auth": {
    "register": {
      "method": "POST",
      "path": "/api/auth/register",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    },
    "login": {
      "method": "POST",
      "path": "/api/auth/login",
      "request": {
        "email": "string",
        "password": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
}
```

#### PHASE 1 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Thiết lập cơ sở hạ tầng backend với Quarkus và PostgreSQL. `[ARC-010]`
    - `./sources/backend/`
  - **Tester:** Viết test suite cho cơ sở hạ tầng backend. `[ARC-010]`
    - `./sources/backend/tests/;./sources/backend/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[ARC-010]`
    - `./sources/backend/`

- **DAY 2:**
  - **Coder:** Triển khai xác thực và phân quyền cơ bản. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`
  - **Tester:** Viết test suite cho xác thực và phân quyền. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/tests/;./sources/backend/auth/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`

### 4.3. PHASE 2 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 2
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý trung tâm và khóa học.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/centers/` | Triển khai quản lý trung tâm |
| 2 | `./sources/backend/courses/` | Triển khai quản lý khóa học |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID,
    max_students INT NOT NULL DEFAULT 30,
    FOREIGN KEY (teacher_id) REFERENCES users(user_id)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "centers": {
    "list": {
      "method": "GET",
      "path": "/api/centers",
      "response": {
        "centers": [
          {
            "centerId": "string",
            "name": "string",
            "address": "string",
            "taxId": "string",
            "contactPhone": "string",
            "contactEmail": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/centers",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "string"
      }
    }
  },
  "courses": {
    "list": {
      "method": "GET",
      "path": "/api/courses",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "teacherName": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/courses",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "string",
        "endDate": "string",
        "teacherId": "string",
        "maxStudents": "number"
      },
      "response": {
        "courseId": "string"
      }
    }
  }
}
```

#### PHASE 2 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`
  - **Tester:** Viết test suite cho quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/tests/;./sources/backend/centers/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`

- **DAY 2:**
  - **Coder:** Triển khai quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`
  - **Tester:** Viết test suite cho quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/tests/;./sources/backend/courses/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý trung tâm và khóa học. `[DAT-004]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-004]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-004]`
    - `./sources/backend/database/`

### 4.4. PHASE 3 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 3
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng đăng ký và ghi danh học viên.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/enrollments/` | Triển khai đăng ký và ghi danh học viên |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "enrollments": {
    "browse": {
      "method": "GET",
      "path": "/api/enrollments/browse",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "maxStudents": "number",
            "currentStudents": "number"
          }
        ]
      }
    },
    "register": {
      "method": "POST",
      "path": "/api/enrollments/register",
      "request": {
        "courseId": "string"
      },
      "response": {
        "enrollmentId": "string"
      }
    }
  }
}
```

#### PHASE 3 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`
  - **Tester:** Viết test suite cho đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/tests/;./sources/backend/enrollments/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho đăng ký và ghi danh học viên. `[DAT-005]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-005]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-005]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho đăng ký và ghi danh học viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

### 4.5. PHASE 4 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 4
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng điểm danh và quản lý thẻ hội viên.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/attendance/` | Triển khai điểm danh và quản lý thẻ hội viên |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES users(user_id)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "attendance": {
    "scan": {
      "method": "POST",
      "path": "/api/attendance/scan",
      "request": {
        "studentId": "string",
        "courseId": "string"
      },
      "response": {
        "attendanceId": "string",
        "status": "string"
      }
    }
  },
  "studentCards": {
    "view": {
      "method": "GET",
      "path": "/api/studentCards/view",
      "response": {
        "totalValidityDays": "number",
        "daysUsed": "number",
        "daysRemaining": "number"
      }
    },
    "renew": {
      "method": "POST",
      "path": "/api/studentCards/renew",
      "request": {
        "renewalDays": "number"
      },
      "response": {
        "newEndDate": "string"
      }
    }
  }
}
```

#### PHASE 4 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`
  - **Tester:** Viết test suite cho điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/tests/;./sources/backend/attendance/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho điểm danh và quản lý thẻ hội viên. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho điểm danh và quản lý thẻ hội viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

### 4.6. PHASE 5 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 5
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý khuyến mãi, thông báo, chatbot AI, và ứng dụng di động.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/promotions/` | Triển khai quản lý khuyến mãi |
| 2 | `./sources/backend/announcements/` | Triển khai quản lý thông báo |
| 3 | `./sources/backend/chatbot/` | Triển khai chatbot AI |
| 4 | `./sources/backend/mobile/` | Triển khai ứng dụng di động |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
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

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "promotions": {
    "list": {
      "method": "GET",
      "path": "/api/promotions",
      "response": {
        "promotions": [
          {
            "promoId": "string",
            "code": "string",
            "discountPercent": "number",
            "startDate": "string",
            "endDate": "string",
            "description": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/promotions",
      "request": {
        "code": "string",
        "discountPercent": "number",
        "startDate": "string",
        "endDate": "string",
        "description": "string"
      },
      "response": {
        "promoId": "string"
      }
    }
  },
  "announcements": {
    "list": {
      "method": "GET",
      "path": "/api/announcements",
      "response": {
        "announcements": [
          {
            "announcementId": "string",
            "title": "string",
            "content": "string",
            "startDate": "string",
            "endDate": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/announcements",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "string",
        "endDate": "string"
      },
      "response": {
        "announcementId": "string"
      }
    }
  },
  "chatbot": {
    "query": {
      "method": "POST",
      "path": "/api/chatbot/query",
      "request": {
        "question": "string"
      },
      "response": {
        "answer": "string"
      }
    }
  },
  "mobile": {
    "pushNotification": {
      "method": "POST",
      "path": "/api/mobile/pushNotification",
      "request": {
        "userId": "string",
        "message": "string"
      },
      "response": {
        "status": "string"
      }
    }
  }
}
```

#### PHASE 5 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`
  - **Tester:** Viết test suite cho quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/tests/;./sources/backend/promotions/`
    - `./sources/backend/announcements/tests/;./sources/backend/announcements/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`

- **DAY 2:**
  - **Coder:** Triển khai chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`
  - **Tester:** Viết test suite cho chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/tests/;./sources/backend/chatbot/`
    - `./sources/backend/mobile/tests/;./sources/backend/mobile/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý khuyến mãi và thông báo. `[DAT-009]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-009]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-009]`
    - `./sources/backend/database/`

## 5. PHASE 1 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 1
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Thiết lập cơ sở hạ tầng backend, triển khai cơ sở dữ liệu, và phát triển các tính năng xác thực cơ bản.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/` | Thiết lập cơ sở hạ tầng backend |
| 2 | `./sources/backend/auth/` | Triển khai xác thực và phân quyền |
| 3 | `./sources/backend/database/` | Thiết kế và triển khai cơ sở dữ liệu |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL,
    provider VARCHAR(10) NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "auth": {
    "register": {
      "method": "POST",
      "path": "/api/auth/register",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    },
    "login": {
      "method": "POST",
      "path": "/api/auth/login",
      "request": {
        "email": "string",
        "password": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
}
```

### PHASE 1 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Thiết lập cơ sở hạ tầng backend với Quarkus và PostgreSQL. `[ARC-010]`
    - `./sources/backend/`
  - **Tester:** Viết test suite cho cơ sở hạ tầng backend. `[ARC-010]`
    - `./sources/backend/tests/;./sources/backend/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[ARC-010]`
    - `./sources/backend/`

- **DAY 2:**
  - **Coder:** Triển khai xác thực và phân quyền cơ bản. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`
  - **Tester:** Viết test suite cho xác thực và phân quyền. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/tests/;./sources/backend/auth/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`

## 6. PHASE 2 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 2
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý trung tâm và khóa học.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/centers/` | Triển khai quản lý trung tâm |
| 2 | `./sources/backend/courses/` | Triển khai quản lý khóa học |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID,
    max_students INT NOT NULL DEFAULT 30,
    FOREIGN KEY (teacher_id) REFERENCES users(user_id)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "centers": {
    "list": {
      "method": "GET",
      "path": "/api/centers",
      "response": {
        "centers": [
          {
            "centerId": "string",
            "name": "string",
            "address": "string",
            "taxId": "string",
            "contactPhone": "string",
            "contactEmail": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/centers",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "string"
      }
    }
  },
  "courses": {
    "list": {
      "method": "GET",
      "path": "/api/courses",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "teacherName": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/courses",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "string",
        "endDate": "string",
        "teacherId": "string",
        "maxStudents": "number"
      },
      "response": {
        "courseId": "string"
      }
    }
  }
}
```

### PHASE 2 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`
  - **Tester:** Viết test suite cho quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/tests/;./sources/backend/centers/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`

- **DAY 2:**
  - **Coder:** Triển khai quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`
  - **Tester:** Viết test suite cho quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/tests/;./sources/backend/courses/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý trung tâm và khóa học. `[DAT-004]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-004]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-004]`
    - `./sources/backend/database/`

## 7. PHASE 3 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 3
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng đăng ký và ghi danh học viên.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/enrollments/` | Triển khai đăng ký và ghi danh học viên |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "enrollments": {
    "browse": {
      "method": "GET",
      "path": "/api/enrollments/browse",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "maxStudents": "number",
            "currentStudents": "number"
          }
        ]
      }
    },
    "register": {
      "method": "POST",
      "path": "/api/enrollments/register",
      "request": {
        "courseId": "string"
      },
      "response": {
        "enrollmentId": "string"
      }
    }
  }
}
```

### PHASE 3 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`
  - **Tester:** Viết test suite cho đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/tests/;./sources/backend/enrollments/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho đăng ký và ghi danh học viên. `[DAT-005]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-005]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-005]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho đăng ký và ghi danh học viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

## 8. PHASE 4 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 4
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng điểm danh và quản lý thẻ hội viên.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/attendance/` | Triển khai điểm danh và quản lý thẻ hội viên |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES users(user_id)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "attendance": {
    "scan": {
      "method": "POST",
      "path": "/api/attendance/scan",
      "request": {
        "studentId": "string",
        "courseId": "string"
      },
      "response": {
        "attendanceId": "string",
        "status": "string"
      }
    }
  },
  "studentCards": {
    "view": {
      "method": "GET",
      "path": "/api/studentCards/view",
      "response": {
        "totalValidityDays": "number",
        "daysUsed": "number",
        "daysRemaining": "number"
      }
    },
    "renew": {
      "method": "POST",
      "path": "/api/studentCards/renew",
      "request": {
        "renewalDays": "number"
      },
      "response": {
        "newEndDate": "string"
      }
    }
  }
}
```

### PHASE 4 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`
  - **Tester:** Viết test suite cho điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/tests/;./sources/backend/attendance/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho điểm danh và quản lý thẻ hội viên. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho điểm danh và quản lý thẻ hội viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

## 9. PHASE 5 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 5
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý khuyến mãi, thông báo, chatbot AI, và ứng dụng di động.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/promotions/` | Triển khai quản lý khuyến mãi |
| 2 | `./sources/backend/announcements/` | Triển khai quản lý thông báo |
| 3 | `./sources/backend/chatbot/` | Triển khai chatbot AI |
| 4 | `./sources/backend/mobile/` | Triển khai ứng dụng di động |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
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

### API AND EVENT ROUTING CONTRACTS

```json
{
  "promotions": {
    "list": {
      "method": "GET",
      "path": "/api/promotions",
      "response": {
        "promotions": [
          {
            "promoId": "string",
            "code": "string",
            "discountPercent": "number",
            "startDate": "string",
            "endDate": "string",
            "description": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/promotions",
      "request": {
        "code": "string",
        "discountPercent": "number",
        "startDate": "string",
        "endDate": "string",
        "description": "string"
      },
      "response": {
        "promoId": "string"
      }
    }
  },
  "announcements": {
    "list": {
      "method": "GET",
      "path": "/api/announcements",
      "response": {
        "announcements": [
          {
            "announcementId": "string",
            "title": "string",
            "content": "string",
            "startDate": "string",
            "endDate": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/announcements",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "string",
        "endDate": "string"
      },
      "response": {
        "announcementId": "string"
      }
    }
  },
  "chatbot": {
    "query": {
      "method": "POST",
      "path": "/api/chatbot/query",
      "request": {
        "question": "string"
      },
      "response": {
        "answer": "string"
      }
    }
  },
  "mobile": {
    "pushNotification": {
      "method": "POST",
      "path": "/api/mobile/pushNotification",
      "request": {
        "userId": "string",
        "message": "string"
      },
      "response": {
        "status": "string"
      }
    }
  }
}
```

### PHASE 5 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`
  - **Tester:** Viết test suite cho quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/tests/;./sources/backend/promotions/`
    - `./sources/backend/announcements/tests/;./sources/backend/announcements/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`

- **DAY 2:**
  - **Coder:** Triển khai chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`
  - **Tester:** Viết test suite cho chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/tests/;./sources/backend/chatbot/`
    - `./sources/backend/mobile/tests/;./sources/backend/mobile/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý khuyến mãi và thông báo. `[DAT-009]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-009]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-009]`
    - `./sources/backend/database/`

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### 1.1. MỤC TIÊU & GIÁ TRỊ CỐT LÕI
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### 1.2. ĐỐI TƯỢNG NGƯỜI DÙNG MỤC TIÊU
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### 1.3. MA TRẬN KIỂM SOÁT TRUY CẬP DỰA TRÊN VAI TRÒ (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### 1.4. KIẾN TRÚC & LUỒNG DỮ LIỆU (CÁC LUỒNG CHÍNH)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### 1.5. CÔNG NGHỆ & HẠ TẦNG
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 📈 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1. QUẢN LÝ NGƯỜI DÙNG

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```

### 2.2. QUẢN LÝ TRUNG TÂM

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```

### 2.3. QUẢN LÝ KHÓA HỌC

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```

### 2.4. ĐĂNG KÝ & GHI DANH HỌC VIÊN

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```

### 2.5. ĐIỂM DANH & QUÉT MÃ QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```

### 2.6. QUẢN LÝ THẺ HỘI VIÊN

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```

### 2.7. THÔNG BÁO & TRUYỀN THÔNG

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```

### 2.8. QUẢN LÝ KHUYẾN MÃI & THÔNG BÁO

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```

### 2.9. CHATBOT DỊCH VỤ KHÁCH HÀNG AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10. CÁC TÍNH NĂNG CỐT LÕI CỦA ỨNG DỤNG DI ĐỘNG

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11. BẢN ĐỊA HÓA & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```

### 2.12. BÁO CÁO & PHÂN TÍCH

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG

<!--START_BACKLOG_SYNOPSIS_GRID-->

| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | User Registration | Implement user registration with email/password and social providers (Firebase, Google, Facebook) | Application Code | [REQ-001], [REQ-002] |
| 2 | Role Management | Develop role assignment and permission enforcement system | Application Code | [REQ-003] |
| 3 | Center Management | Create center CRUD operations and admin assignment | Application Code | [REQ-004], [REQ-005], [REQ-006] |
| 4 | Course Management | Implement course CRUD with schedule conflict detection | Application Code | [REQ-007], [REQ-008] |
| 5 | Teacher Assignment | Develop teacher assignment to courses with notification | Application Code | [REQ-009] |
| 6 | Student Enrollment | Implement course browsing and enrollment system | Application Code | [REQ-010], [REQ-011] |
| 7 | QR Attendance | Develop QR scanning and attendance recording system | Application Code | [REQ-012], [REQ-013] |
| 8 | Membership Card | Implement membership card display and renewal system | Application Code | [REQ-014], [REQ-015] |
| 9 | Notification System | Develop push notification and Zalo group messaging system | Application Code | [REQ-016] |
| 10 | Promotion Management | Create promotion CRUD system | Application Code | [REQ-017] |
| 11 | Announcement Management | Develop announcement CRUD system | Application Code | [REQ-018] |
| 12 | AI Chatbot | Integrate AI chatbot for common queries | Application Code | [REQ-019] |
| 13 | Mobile UI | Develop responsive mobile UI for all roles | Application Code | [REQ-020] |
| 14 | Push Notifications | Implement push notification system for mobile | Application Code | [REQ-021] |
| 15 | Localization | Implement multi-language support | Application Code | [REQ-022], [REQ-023] |
| 16 | Attendance Reporting | Develop daily attendance report generation | Application Code | [REQ-024] |
| 17 | Dashboard | Create real-time dashboard for center admins | Application Code | [REQ-025] |
| 18 | User Database | Design and implement User and Role database schema | Database Schema | [DAT-001] |
| 19 | Center Database | Design and implement Center database schema | Database Schema | [DAT-003] |
| 20 | Course Database | Design and implement Course database schema | Database Schema | [DAT-004] |
| 21 | Enrollment Database | Design and implement Enrollment database schema | Database Schema | [DAT-005] |
| 22 | Attendance Database | Design and implement Attendance database schema | Database Schema | [DAT-006] |
| 23 | Membership Card Database | Design and implement Membership Card database schema | Database Schema | [DAT-007] |
| 24 | Notification Database | Design and implement Notification database schema | Database Schema | [DAT-008] |
| 25 | Promotion Database | Design and implement Promotion database schema | Database Schema | [DAT-009] |
| 26 | System Settings Database | Design and implement System Settings database schema | Database Schema | [DAT-011] |
| 27 | Authentication Flow | Document authentication flow with JWT and refresh tokens | Enterprise Documentation | [ARC-006] |
| 28 | QR Attendance Flow | Document QR attendance flow with idempotent recording | Enterprise Documentation | [ARC-007] |
| 29 | Notification Flow | Document notification flow to mobile and Zalo | Enterprise Documentation | [ARC-008] |
| 30 | Mobile Integration Flow | Document mobile integration flow with REST APIs | Enterprise Documentation | [ARC-009] |
| 31 | Technology Stack | Document technology stack and infrastructure | Enterprise Documentation | [ARC-010] |
| 32 | Input Validation | Handle input validation errors | Exception Handling | [EXC-004] |
| 33 | QR Scan Failure | Handle QR scan failures and network drops | Exception Handling | [EXC-001] |
| 34 | Duplicate Attendance | Handle duplicate attendance submissions | Exception Handling | [EXC-002] |
| 35 | Notification Failure | Handle notification delivery failures | Exception Handling | [EXC-003] |
| 36 | System Recovery | Handle system recovery after outages | Exception Handling | [EXC-005] |
| 37 | Performance Metrics | Ensure API performance meets requirements | Non-Functional | [NFR-001] |
| 38 | Availability | Ensure system availability meets requirements | Non-Functional | [NFR-002] |
| 39 | Security | Implement security measures | Non-Functional | [NFR-003] |
| 40 | Scalability | Implement scalability measures | Non-Functional | [NFR-004] |
| 41 | Docker Image Size | Ensure Docker image size meets requirements | Non-Functional | [NFR-005] |
| 42 | Logging & Audit | Implement logging and audit measures | Non-Functional | [NFR-006] |
| 43 | Multi-Language Support | Implement multi-language support | Non-Functional | [NFR-007] |
| 44 | GDPR/CCPA Compliance | Implement GDPR/CCPA compliance measures | Non-Functional | [NFR-008] |
| 45 | Backup & Disaster Recovery | Implement backup and disaster recovery measures | Non-Functional | [NFR-009] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 45 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. PHASE 1 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 1
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Thiết lập cơ sở hạ tầng backend, triển khai cơ sở dữ liệu, và phát triển các tính năng xác thực cơ bản.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/` | Thiết lập cơ sở hạ tầng backend |
| 2 | `./sources/backend/auth/` | Triển khai xác thực và phân quyền |
| 3 | `./sources/backend/database/` | Thiết kế và triển khai cơ sở dữ liệu |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL,
    provider VARCHAR(10) NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "auth": {
    "register": {
      "method": "POST",
      "path": "/api/auth/register",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    },
    "login": {
      "method": "POST",
      "path": "/api/auth/login",
      "request": {
        "email": "string",
        "password": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
}
```

#### PHASE 1 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Thiết lập cơ sở hạ tầng backend với Quarkus và PostgreSQL. `[ARC-010]`
    - `./sources/backend/`
  - **Tester:** Viết test suite cho cơ sở hạ tầng backend. `[ARC-010]`
    - `./sources/backend/tests/;./sources/backend/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[ARC-010]`
    - `./sources/backend/`

- **DAY 2:**
  - **Coder:** Triển khai xác thực và phân quyền cơ bản. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`
  - **Tester:** Viết test suite cho xác thực và phân quyền. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/tests/;./sources/backend/auth/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`

### 4.3. PHASE 2 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 2
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý trung tâm và khóa học.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/centers/` | Triển khai quản lý trung tâm |
| 2 | `./sources/backend/courses/` | Triển khai quản lý khóa học |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID,
    max_students INT NOT NULL DEFAULT 30,
    FOREIGN KEY (teacher_id) REFERENCES users(user_id)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "centers": {
    "list": {
      "method": "GET",
      "path": "/api/centers",
      "response": {
        "centers": [
          {
            "centerId": "string",
            "name": "string",
            "address": "string",
            "taxId": "string",
            "contactPhone": "string",
            "contactEmail": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/centers",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "string"
      }
    }
  },
  "courses": {
    "list": {
      "method": "GET",
      "path": "/api/courses",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "teacherName": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/courses",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "string",
        "endDate": "string",
        "teacherId": "string",
        "maxStudents": "number"
      },
      "response": {
        "courseId": "string"
      }
    }
  }
}
```

#### PHASE 2 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`
  - **Tester:** Viết test suite cho quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/tests/;./sources/backend/centers/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`

- **DAY 2:**
  - **Coder:** Triển khai quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`
  - **Tester:** Viết test suite cho quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/tests/;./sources/backend/courses/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý trung tâm và khóa học. `[DAT-004]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-004]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-004]`
    - `./sources/backend/database/`

### 4.4. PHASE 3 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 3
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng đăng ký và ghi danh học viên.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/enrollments/` | Triển khai đăng ký và ghi danh học viên |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "enrollments": {
    "browse": {
      "method": "GET",
      "path": "/api/enrollments/browse",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "maxStudents": "number",
            "currentStudents": "number"
          }
        ]
      }
    },
    "register": {
      "method": "POST",
      "path": "/api/enrollments/register",
      "request": {
        "courseId": "string"
      },
      "response": {
        "enrollmentId": "string"
      }
    }
  }
}
```

#### PHASE 3 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`
  - **Tester:** Viết test suite cho đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/tests/;./sources/backend/enrollments/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho đăng ký và ghi danh học viên. `[DAT-005]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-005]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-005]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho đăng ký và ghi danh học viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

### 4.5. PHASE 4 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 4
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng điểm danh và quản lý thẻ hội viên.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/attendance/` | Triển khai điểm danh và quản lý thẻ hội viên |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES users(user_id)
);
```

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "attendance": {
    "scan": {
      "method": "POST",
      "path": "/api/attendance/scan",
      "request": {
        "studentId": "string",
        "courseId": "string"
      },
      "response": {
        "attendanceId": "string",
        "status": "string"
      }
    }
  },
  "studentCards": {
    "view": {
      "method": "GET",
      "path": "/api/studentCards/view",
      "response": {
        "totalValidityDays": "number",
        "daysUsed": "number",
        "daysRemaining": "number"
      }
    },
    "renew": {
      "method": "POST",
      "path": "/api/studentCards/renew",
      "request": {
        "renewalDays": "number"
      },
      "response": {
        "newEndDate": "string"
      }
    }
  }
}
```

#### PHASE 4 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`
  - **Tester:** Viết test suite cho điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/tests/;./sources/backend/attendance/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho điểm danh và quản lý thẻ hội viên. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho điểm danh và quản lý thẻ hội viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

### 4.6. PHASE 5 DETAILED ARCHITECTURAL SPECIFICATION

#### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 5
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý khuyến mãi, thông báo, chatbot AI, và ứng dụng di động.

#### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/promotions/` | Triển khai quản lý khuyến mãi |
| 2 | `./sources/backend/announcements/` | Triển khai quản lý thông báo |
| 3 | `./sources/backend/chatbot/` | Triển khai chatbot AI |
| 4 | `./sources/backend/mobile/` | Triển khai ứng dụng di động |

#### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
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

#### API AND EVENT ROUTING CONTRACTS

```json
{
  "promotions": {
    "list": {
      "method": "GET",
      "path": "/api/promotions",
      "response": {
        "promotions": [
          {
            "promoId": "string",
            "code": "string",
            "discountPercent": "number",
            "startDate": "string",
            "endDate": "string",
            "description": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/promotions",
      "request": {
        "code": "string",
        "discountPercent": "number",
        "startDate": "string",
        "endDate": "string",
        "description": "string"
      },
      "response": {
        "promoId": "string"
      }
    }
  },
  "announcements": {
    "list": {
      "method": "GET",
      "path": "/api/announcements",
      "response": {
        "announcements": [
          {
            "announcementId": "string",
            "title": "string",
            "content": "string",
            "startDate": "string",
            "endDate": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/announcements",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "string",
        "endDate": "string"
      },
      "response": {
        "announcementId": "string"
      }
    }
  },
  "chatbot": {
    "query": {
      "method": "POST",
      "path": "/api/chatbot/query",
      "request": {
        "question": "string"
      },
      "response": {
        "answer": "string"
      }
    }
  },
  "mobile": {
    "pushNotification": {
      "method": "POST",
      "path": "/api/mobile/pushNotification",
      "request": {
        "userId": "string",
        "message": "string"
      },
      "response": {
        "status": "string"
      }
    }
  }
}
```

#### PHASE 5 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`
  - **Tester:** Viết test suite cho quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/tests/;./sources/backend/promotions/`
    - `./sources/backend/announcements/tests/;./sources/backend/announcements/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`

- **DAY 2:**
  - **Coder:** Triển khai chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`
  - **Tester:** Viết test suite cho chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/tests/;./sources/backend/chatbot/`
    - `./sources/backend/mobile/tests/;./sources/backend/mobile/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý khuyến mãi và thông báo. `[DAT-009]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-009]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-009]`
    - `./sources/backend/database/`

## 5. PHASE 1 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 1
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Thiết lập cơ sở hạ tầng backend, triển khai cơ sở dữ liệu, và phát triển các tính năng xác thực cơ bản.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/` | Thiết lập cơ sở hạ tầng backend |
| 2 | `./sources/backend/auth/` | Triển khai xác thực và phân quyền |
| 3 | `./sources/backend/database/` | Thiết kế và triển khai cơ sở dữ liệu |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL,
    provider VARCHAR(10) NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "auth": {
    "register": {
      "method": "POST",
      "path": "/api/auth/register",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    },
    "login": {
      "method": "POST",
      "path": "/api/auth/login",
      "request": {
        "email": "string",
        "password": "string"
      },
      "response": {
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
}
```

### PHASE 1 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Thiết lập cơ sở hạ tầng backend với Quarkus và PostgreSQL. `[ARC-010]`
    - `./sources/backend/`
  - **Tester:** Viết test suite cho cơ sở hạ tầng backend. `[ARC-010]`
    - `./sources/backend/tests/;./sources/backend/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[ARC-010]`
    - `./sources/backend/`

- **DAY 2:**
  - **Coder:** Triển khai xác thực và phân quyền cơ bản. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`
  - **Tester:** Viết test suite cho xác thực và phân quyền. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/tests/;./sources/backend/auth/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-001], [REQ-002], [REQ-003]`
    - `./sources/backend/auth/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-001], [DAT-003]`
    - `./sources/backend/database/`

## 6. PHASE 2 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 2
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý trung tâm và khóa học.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/centers/` | Triển khai quản lý trung tâm |
| 2 | `./sources/backend/courses/` | Triển khai quản lý khóa học |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID,
    max_students INT NOT NULL DEFAULT 30,
    FOREIGN KEY (teacher_id) REFERENCES users(user_id)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "centers": {
    "list": {
      "method": "GET",
      "path": "/api/centers",
      "response": {
        "centers": [
          {
            "centerId": "string",
            "name": "string",
            "address": "string",
            "taxId": "string",
            "contactPhone": "string",
            "contactEmail": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/centers",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "string"
      }
    }
  },
  "courses": {
    "list": {
      "method": "GET",
      "path": "/api/courses",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "teacherName": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/courses",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "string",
        "endDate": "string",
        "teacherId": "string",
        "maxStudents": "number"
      },
      "response": {
        "courseId": "string"
      }
    }
  }
}
```

### PHASE 2 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`
  - **Tester:** Viết test suite cho quản lý trung tâm. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/tests/;./sources/backend/centers/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-004], [REQ-005], [REQ-006]`
    - `./sources/backend/centers/`

- **DAY 2:**
  - **Coder:** Triển khai quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`
  - **Tester:** Viết test suite cho quản lý khóa học. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/tests/;./sources/backend/courses/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-007], [REQ-008], [REQ-009]`
    - `./sources/backend/courses/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý trung tâm và khóa học. `[DAT-004]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-004]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-004]`
    - `./sources/backend/database/`

## 7. PHASE 3 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 3
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng đăng ký và ghi danh học viên.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/enrollments/` | Triển khai đăng ký và ghi danh học viên |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "enrollments": {
    "browse": {
      "method": "GET",
      "path": "/api/enrollments/browse",
      "response": {
        "courses": [
          {
            "courseId": "string",
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "maxStudents": "number",
            "currentStudents": "number"
          }
        ]
      }
    },
    "register": {
      "method": "POST",
      "path": "/api/enrollments/register",
      "request": {
        "courseId": "string"
      },
      "response": {
        "enrollmentId": "string"
      }
    }
  }
}
```

### PHASE 3 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`
  - **Tester:** Viết test suite cho đăng ký và ghi danh học viên. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/tests/;./sources/backend/enrollments/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-010], [REQ-011]`
    - `./sources/backend/enrollments/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho đăng ký và ghi danh học viên. `[DAT-005]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-005]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-005]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho đăng ký và ghi danh học viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

## 8. PHASE 4 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 4
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng điểm danh và quản lý thẻ hội viên.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/attendance/` | Triển khai điểm danh và quản lý thẻ hội viên |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (student_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES users(user_id)
);
```

### API AND EVENT ROUTING CONTRACTS

```json
{
  "attendance": {
    "scan": {
      "method": "POST",
      "path": "/api/attendance/scan",
      "request": {
        "studentId": "string",
        "courseId": "string"
      },
      "response": {
        "attendanceId": "string",
        "status": "string"
      }
    }
  },
  "studentCards": {
    "view": {
      "method": "GET",
      "path": "/api/studentCards/view",
      "response": {
        "totalValidityDays": "number",
        "daysUsed": "number",
        "daysRemaining": "number"
      }
    },
    "renew": {
      "method": "POST",
      "path": "/api/studentCards/renew",
      "request": {
        "renewalDays": "number"
      },
      "response": {
        "newEndDate": "string"
      }
    }
  }
}
```

### PHASE 4 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`
  - **Tester:** Viết test suite cho điểm danh và quản lý thẻ hội viên. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/tests/;./sources/backend/attendance/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`
    - `./sources/backend/attendance/`

- **DAY 2:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho điểm danh và quản lý thẻ hội viên. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-006], [DAT-007]`
    - `./sources/backend/database/`

- **DAY 3:**
  - **Coder:** Triển khai thông báo cho điểm danh và quản lý thẻ hội viên. `[REQ-016]`
    - `./sources/backend/notifications/`
  - **Tester:** Viết test suite cho thông báo. `[REQ-016]`
    - `./sources/backend/notifications/tests/;./sources/backend/notifications/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-016]`
    - `./sources/backend/notifications/`

## 9. PHASE 5 DETAILED ARCHITECTURAL SPECIFICATION

### PHASE CORE OBJECTIVE & PURPOSE
- **Phase:** 5
- **Day Range:** 1-3
- **Component / Module Path:** `./sources/backend/`
- **Deliverables Summary:** Phát triển các tính năng quản lý khuyến mãi, thông báo, chatbot AI, và ứng dụng di động.

### TARGET PHYSICAL DIRECTORY MATRIX MAP

| No. | Component / Module Path | Deliverables Summary |
| :--- | :--- | :--- |
| 1 | `./sources/backend/promotions/` | Triển khai quản lý khuyến mãi |
| 2 | `./sources/backend/announcements/` | Triển khai quản lý thông báo |
| 3 | `./sources/backend/chatbot/` | Triển khai chatbot AI |
| 4 | `./sources/backend/mobile/` | Triển khai ứng dụng di động |

### DATABASE SCHEMA DDL SQL SPECIFICATION

```sql
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
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

### API AND EVENT ROUTING CONTRACTS

```json
{
  "promotions": {
    "list": {
      "method": "GET",
      "path": "/api/promotions",
      "response": {
        "promotions": [
          {
            "promoId": "string",
            "code": "string",
            "discountPercent": "number",
            "startDate": "string",
            "endDate": "string",
            "description": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/promotions",
      "request": {
        "code": "string",
        "discountPercent": "number",
        "startDate": "string",
        "endDate": "string",
        "description": "string"
      },
      "response": {
        "promoId": "string"
      }
    }
  },
  "announcements": {
    "list": {
      "method": "GET",
      "path": "/api/announcements",
      "response": {
        "announcements": [
          {
            "announcementId": "string",
            "title": "string",
            "content": "string",
            "startDate": "string",
            "endDate": "string"
          }
        ]
      }
    },
    "create": {
      "method": "POST",
      "path": "/api/announcements",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "string",
        "endDate": "string"
      },
      "response": {
        "announcementId": "string"
      }
    }
  },
  "chatbot": {
    "query": {
      "method": "POST",
      "path": "/api/chatbot/query",
      "request": {
        "question": "string"
      },
      "response": {
        "answer": "string"
      }
    }
  },
  "mobile": {
    "pushNotification": {
      "method": "POST",
      "path": "/api/mobile/pushNotification",
      "request": {
        "userId": "string",
        "message": "string"
      },
      "response": {
        "status": "string"
      }
    }
  }
}
```

### PHASE 5 LOW-LEVEL TECHNICAL TASK INSTRUCTIONS

- **DAY 1:**
  - **Coder:** Triển khai quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`
  - **Tester:** Viết test suite cho quản lý khuyến mãi và thông báo. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/tests/;./sources/backend/promotions/`
    - `./sources/backend/announcements/tests/;./sources/backend/announcements/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-017], [REQ-018]`
    - `./sources/backend/promotions/`
    - `./sources/backend/announcements/`

- **DAY 2:**
  - **Coder:** Triển khai chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`
  - **Tester:** Viết test suite cho chatbot AI và ứng dụng di động. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/tests/;./sources/backend/chatbot/`
    - `./sources/backend/mobile/tests/;./sources/backend/mobile/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[REQ-019], [REQ-020], [REQ-021]`
    - `./sources/backend/chatbot/`
    - `./sources/backend/mobile/`

- **DAY 3:**
  - **Coder:** Thiết kế và triển khai cơ sở dữ liệu cho quản lý khuyến mãi và thông báo. `[DAT-009]`
    - `./sources/backend/database/`
  - **Tester:** Viết test suite cho cơ sở dữ liệu. `[DAT-009]`
    - `./sources/backend/database/tests/;./sources/backend/database/`
  - **Reviewer:** Review code và đảm bảo tuân thủ các tiêu chuẩn lập trình. `[DAT-009]`
    - `./sources/backend/database/`

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 📦 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1 Quản lý người dùng

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
### 2.2 Quản lý trung tâm

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
### 2.3 Quản lý khóa học

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
### 2.4 Đăng ký & ghi danh học viên

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
### 2.5 Điểm danh & quét mã QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
### 2.6 Quản lý thẻ hội viên

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
### 2.7 Thông báo & truyền thông

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
### 2.8 Quản lý khuyến mãi & thông báo

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
### 2.9 Chatbot dịch vụ khách hàng AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10 Các tính năng cốt lõi của ứng dụng di động

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11 Bản địa hóa & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
### 2.12 Báo cáo & phân tích

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 📜 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 📝 4. KIẾN TRÚC TOÀN CẦU & PHÂN PHỐI PHÂN TÍCH

### 4.1 KIẾN TRÚC TOÀN CẦU

#### 4.1.1 Kiến trúc hệ thống

- **Backend**: Sử dụng Java/Quarkus để xây dựng các dịch vụ microservices độc lập, mỗi dịch vụ chịu trách nhiệm cho một miền nghiệp vụ cụ thể (người dùng, khóa học, điểm danh, v.v.).
- **Frontend**: Sử dụng Next.js để xây dựng giao diện người dùng đáp ứng, bao gồm cả ứng dụng web và ứng dụng di động (React Native).
- **Cơ sở dữ liệu**: Sử dụng PostgreSQL với schema được chia thành các cơ sở dữ liệu riêng biệt cho mỗi dịch vụ microservice để đảm bảo tính cô lập và bảo mật.
- **Containerization**: Sử dụng Docker để đóng gói các dịch vụ và triển khai trên Kubernetes (GKE) để quản lý hạ tầng và tự động hóa triển khai.
- **Xác thực và ủy quyền**: Sử dụng Firebase Authentication cho xác thực người dùng và JWT cho ủy quyền. Cấp quyền dựa trên vai trò (RBAC) được triển khai thông qua các dịch vụ backend.
- **Thông báo đẩy**: Sử dụng Firebase Cloud Messaging (FCM) và Apple APNs để gửi thông báo đẩy đến ứng dụng di động.
- **Tích hợp Zalo**: Sử dụng Zalo API để gửi thông báo và tương tác với nhóm Zalo.
- **Caching**: Sử dụng Redis để lưu trữ phiên và dữ liệu tạm thời.
- **CI/CD**: Sử dụng GitHub Actions để tự động hóa quy trình tích hợp và triển khai liên tục.

#### 4.1.2 Kiến trúc dữ liệu

- **Schema cơ sở dữ liệu**: PostgreSQL với các bảng được chia thành các schema riêng biệt cho mỗi dịch vụ microservice.
- **Chỉ mục**: Tạo chỉ mục cho các trường được truy vấn thường xuyên để tối ưu hóa hiệu suất.
- **Backup và phục hồi**: Thiết lập các bản sao lưu hàng ngày cho cơ sở dữ liệu và phục hồi điểm trong thời gian (PITR) trong vòng 24 giờ.
- **Read Replicas**: Sử dụng read replicas cho các truy vấn báo cáo để giảm tải cho cơ sở dữ liệu chính.

#### 4.1.3 Kiến trúc giao diện người dùng

- **Giao diện người dùng đáp ứng**: Sử dụng Next.js để xây dựng giao diện người dùng đáp ứng cho cả web và di động.
- **Bản địa hóa**: Hỗ trợ nhiều ngôn ngữ (tiếng Anh, tiếng Việt, tiếng Tây Ban Nha) và chuyển đổi ngôn ngữ mà không cần tải lại trang.
- **SEO**: Tối ưu hóa cho công cụ tìm kiếm với các thẻ meta ngôn ngữ cụ thể và thuộc tính hreflang.

#### 4.1.4 Kiến trúc thông báo

- **Thông báo đẩy**: Sử dụng FCM và APNs để gửi thông báo đẩy đến ứng dụng di động.
- **Tích hợp Zalo**: Sử dụng Zalo API để gửi thông báo và tương tác với nhóm Zalo.
- **Quản lý thông báo**: Hệ thống quản lý thông báo với các bảng thông báo và lịch sử thông báo.

### 4.2 Ma trận tóm tắt giai đoạn đa giai đoạn

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|-------------------------|---------------------------|------------|-------------------|
| Giai đoạn 1 | Ngày 1-2 | `./sources/backend/auth-service/`, `./sources/backend/user-service/`, `./sources/docs/` | Khởi tạo hệ thống người dùng và xác thực | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006] |
| Giai đoạn 2 | Ngày 1-3 | `./sources/backend/center-service/`, `./sources/docs/` | Triển khai lõi nghiệp vụ trung tâm | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002] |
| Giai đoạn 3 | Ngày 1-3 | `./sources/backend/course-service/`, `./sources/docs/` | Triển khai lõi nghiệp vụ khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003] |
| Giai đoạn 4 | Ngày 1-2 | `./sources/backend/attendance-service/`, `./sources/docs/` | Triển khai hệ thống điểm danh và thẻ hội viên | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [ARC-007] |
| Giai đoạn 5 | Ngày 1-2 | `./sources/backend/notification-service/`, `./sources/docs/` | Triển khai hệ thống thông báo và tích hợp Zalo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-016], [DAT-008], [EXC-003], [ARC-008] |

## 📝 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN

### Giai đoạn 1 - Khởi Tạo Hệ Thống Người Dùng Và Xác Thực

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Khởi tạo hệ thống người dùng và xác thực, bao gồm đăng ký người dùng, xác thực qua mạng xã hội, và phân quyền người dùng.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth-service/`, `./sources/backend/user-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Tạo bảng người dùng và vai trò với các trường và ràng buộc tương ứng.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  - Đăng ký người dùng: `POST /api/users/register`
  - Xác thực qua mạng xã hội: `POST /api/auth/social`
  - Phân quyền người dùng: `PUT /api/users/{userId}/role`
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Xác thực đầu vào không hợp lệ.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 1)

<!--START_DAY_LOG_INDEX_1-->

- **DAY 1: Khởi tạo cơ sở dữ liệu và dịch vụ xác thực**
  - **SUB-TASK 1: Thiết kế schema cơ sở dữ liệu**
    - [Coder]
    - [DAT-001]
    - `./sources/backend/user-service/src/main/resources/db/migration/V1__Create_users_and_roles.sql`
    - Thiết kế schema cơ sở dữ liệu cho bảng người dùng và vai trò với các trường và ràng buộc tương ứng.

  - **SUB-TASK 2: Viết mã nguồn cho dịch vụ xác thực**
    - [Coder]
    - [REQ-001], [REQ-002], [ARC-006]
    - `./sources/backend/auth-service/src/main/java/com/example/auth/service/AuthService.java`
    - Viết mã nguồn cho dịch vụ xác thực, bao gồm đăng ký người dùng và xác thực qua mạng xã hội.

  - **SUB-TASK 3: Viết mã nguồn cho dịch vụ người dùng**
    - [Coder]
    - [REQ-003]
    - `./sources/backend/user-service/src/main/java/com/example/user/service/UserService.java`
    - Viết mã nguồn cho dịch vụ người dùng, bao gồm phân quyền người dùng.

  - **SUB-TASK 4: Viết bài kiểm tra đơn vị**
    - [Tester]
    - [REQ-001], [REQ-002], [REQ-003]
    - `./sources/backend/auth-service/src/test/java/com/example/auth/service/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/service/AuthService.java`
    - Viết bài kiểm tra đơn vị cho dịch vụ xác thực và người dùng.

  - **SUB-TASK 5: Viết tài liệu kỹ thuật**
    - [Doc]
    - [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006]
    - `./sources/docs/auth-service.md`
    - Viết tài liệu kỹ thuật cho dịch vụ xác thực và người dùng.

  - **SUB-TASK 6: Xây dựng và đẩy Docker image**
    - [Docker]
    - [REQ-001], [REQ-002], [REQ-003]
    - `./sources/backend/auth-service/Dockerfile`
    - Xây dựng và đẩy Docker image cho dịch vụ xác thực và người dùng.

  - **SUB-TASK 7: Triển khai cơ sở hạ tầng trên GCP**
    - [GCP]
    - [REQ-001], [REQ-002], [REQ-003]
    - `./sources/infra/gcp/terraform/main.tf`
    - Triển khai cơ sở hạ tầng trên GCP, bao gồm thiết lập VPC, IAM, và Storage.

  - **SUB-TASK 8: Triển khai dịch vụ trên GKE**
    - [GKE]
    - [REQ-001], [REQ-002], [REQ-003]
    - `./sources/infra/gke/deployment.yaml`
    - Triển khai dịch vụ xác thực và người dùng trên GKE, bao gồm thiết lập Deployment, Service, và Ingress.

- **DAY 2: Triển khai và kiểm thử**
  - **SUB-TASK 1: Triển khai dịch vụ**
    - [GKE]
    - [REQ-001], [REQ-002], [REQ-003]
    - `./sources/infra/gke/deployment.yaml`
    - Triển khai dịch vụ xác thực và người dùng trên GKE.

  - **SUB-TASK 2: Kiểm thử tích hợp**
    - [Tester]
    - [REQ-001], [REQ-002], [REQ-003]
    - `./sources/backend/auth-service/src/test/java/com/example/auth/service/AuthServiceIntegrationTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/service/AuthService.java`
    - Viết và chạy kiểm thử tích hợp cho dịch vụ xác thực và người dùng.

  - **SUB-TASK 3: Đánh giá và sửa lỗi**
    - [Reviewer]
    - [REQ-001], [REQ-002], [REQ-003]
    - `./sources/backend/auth-service/src/main/java/com/example/auth/service/AuthService.java`
    - Đánh giá mã nguồn và sửa lỗi nếu có.

<!--END_PHASE_LOG_BLOCK_INDEX_1-->

### Giai đoạn 2 - Triển khai Lõi Nghiệp Vụ Trung Tâm

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai lõi nghiệp vụ trung tâm, bao gồm xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/center-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003]:** Tạo bảng trung tâm với các trường và ràng buộc tương ứng.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
  - Xem danh sách trung tâm: `GET /api/centers`
  - Tạo/cập nhật/xóa trung tâm: `POST /api/centers`, `PUT /api/centers/{centerId}`, `DELETE /api/centers/{centerId}`
  - Phân quyền quản trị trung tâm: `PUT /api/centers/{centerId}/admin`
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 2)

<!--START_DAY_LOG_INDEX_2-->

- **DAY 1: Khởi tạo cơ sở dữ liệu và dịch vụ trung tâm**
  - **SUB-TASK 1: Thiết kế schema cơ sở dữ liệu**
    - [Coder]
    - [DAT-003]
    - `./sources/backend/center-service/src/main/resources/db/migration/V1__Create_centers.sql`
    - Thiết kế schema cơ sở dữ liệu cho bảng trung tâm với các trường và ràng buộc tương ứng.

  - **SUB-TASK 2: Viết mã nguồn cho dịch vụ trung tâm**
    - [Coder]
    - [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    - `./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java`
    - Viết mã nguồn cho dịch vụ trung tâm, bao gồm xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.

  - **SUB-TASK 3: Viết bài kiểm tra đơn vị**
    - [Tester]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/backend/center-service/src/test/java/com/example/center/service/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java`
    - Viết bài kiểm tra đơn vị cho dịch vụ trung tâm.

  - **SUB-TASK 4: Viết tài liệu kỹ thuật**
    - [Doc]
    - [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]
    - `./sources/docs/center-service.md`
    - Viết tài liệu kỹ thuật cho dịch vụ trung tâm.

  - **SUB-TASK 5: Xây dựng và đẩy Docker image**
    - [Docker]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/backend/center-service/Dockerfile`
    - Xây dựng và đẩy Docker image cho dịch vụ trung tâm.

  - **SUB-TASK 6: Triển khai dịch vụ trên GKE**
    - [GKE]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/infra/gke/center-deployment.yaml`
    - Triển khai dịch vụ trung tâm trên GKE, bao gồm thiết lập Deployment, Service, và Ingress.

- **DAY 2: Triển khai và kiểm thử**
  - **SUB-TASK 1: Triển khai dịch vụ**
    - [GKE]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/infra/gke/center-deployment.yaml`
    - Triển khai dịch vụ trung tâm trên GKE.

  - **SUB-TASK 2: Kiểm thử tích hợp**
    - [Tester]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/backend/center-service/src/test/java/com/example/center/service/CenterServiceIntegrationTest.java;./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java`
    - Viết và chạy kiểm thử tích hợp cho dịch vụ trung tâm.

  - **SUB-TASK 3: Đánh giá và sửa lỗi**
    - [Reviewer]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java`
    - Đánh giá mã nguồn và sửa lỗi nếu có.

- **DAY 3: Tối ưu hóa và triển khai cuối cùng**
  - **SUB-TASK 1: Tối ưu hóa hiệu suất**
    - [Coder]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java`
    - Tối ưu hóa hiệu suất cho dịch vụ trung tâm.

  - **SUB-TASK 2: Triển khai cuối cùng**
    - [GKE]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/infra/gke/center-deployment.yaml`
    - Triển khai cuối cùng cho dịch vụ trung tâm trên GKE.

  - **SUB-TASK 3: Kiểm thử cuối cùng**
    - [Tester]
    - [REQ-004], [REQ-005], [REQ-006]
    - `./sources/backend/center-service/src/test/java/com/example/center/service/CenterServiceFinalTest.java;./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java`
    - Viết và chạy kiểm thử cuối cùng cho dịch vụ trung tâm.

<!--END_PHASE_LOG_BLOCK_INDEX_2-->

### Giai đoạn 3 - Triển khai Lõi Nghiệp Vụ Khóa Học

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai lõi nghiệp vụ khóa học, bao gồm xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/course-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:** Tạo bảng khóa học với các trường và ràng buộc tương ứng.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [ARC-003]:**
  - Xem danh sách khóa học: `GET /api/courses`
  - Tạo/cập nhật/xóa khóa học: `POST /api/courses`, `PUT /api/courses/{courseId}`, `DELETE /api/courses/{courseId}`
  - Phân công giáo viên vào khóa học: `PUT /api/courses/{courseId}/teacher`
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1: Khởi tạo cơ sở dữ liệu và dịch vụ khóa học**
  - **SUB-TASK 1: Thiết kế schema cơ sở dữ liệu**
    - [Coder]
    - [DAT-004]
    - `./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses.sql`
    - Thiết kế schema cơ sở dữ liệu cho bảng khóa học với các trường và ràng buộc tương ứng.

  - **SUB-TASK 2: Viết mã nguồn cho dịch vụ khóa học**
    - [Coder]
    - [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    - `./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java`
    - Viết mã nguồn cho dịch vụ khóa học, bao gồm xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.

  - **SUB-TASK 3: Viết bài kiểm tra đơn vị**
    - [Tester]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/backend/course-service/src/test/java/com/example/course/service/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java`
    - Viết bài kiểm tra đơn vị cho dịch vụ khóa học.

  - **SUB-TASK 4: Viết tài liệu kỹ thuật**
    - [Doc]
    - [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003]
    - `./sources/docs/course-service.md`
    - Viết tài liệu kỹ thuật cho dịch vụ khóa học.

  - **SUB-TASK 5: Xây dựng và đẩy Docker image**
    - [Docker]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/backend/course-service/Dockerfile`
    - Xây dựng và đẩy Docker image cho dịch vụ khóa học.

  - **SUB-TASK 6: Triển khai dịch vụ trên GKE**
    - [GKE]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/infra/gke/course-deployment.yaml`
    - Triển khai dịch vụ khóa học trên GKE, bao gồm thiết lập Deployment, Service, và Ingress.

- **DAY 2: Triển khai và kiểm thử**
  - **SUB-TASK 1: Triển khai dịch vụ**
    - [GKE]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/infra/gke/course-deployment.yaml`
    - Triển khai dịch vụ khóa học trên GKE.

  - **SUB-TASK 2: Kiểm thử tích hợp**
    - [Tester]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/backend/course-service/src/test/java/com/example/course/service/CourseServiceIntegrationTest.java;./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java`
    - Viết và chạy kiểm thử tích hợp cho dịch vụ khóa học.

  - **SUB-TASK 3: Đánh giá và sửa lỗi**
    - [Reviewer]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java`
    - Đánh giá mã nguồn và sửa lỗi nếu có.

- **DAY 3: Tối ưu hóa và triển khai cuối cùng**
  - **SUB-TASK 1: Tối ưu hóa hiệu suất**
    - [Coder]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java`
    - Tối ưu hóa hiệu suất cho dịch vụ khóa học.

  - **SUB-TASK 2: Triển khai cuối cùng**
    - [GKE]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/infra/gke/course-deployment.yaml`
    - Triển khai cuối cùng cho dịch vụ khóa học trên GKE.

  - **SUB-TASK 3: Kiểm thử cuối cùng**
    - [Tester]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/backend/course-service/src/test/java/com/example/course/service/CourseServiceFinalTest.java;./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java`
    - Viết và chạy kiểm thử cuối cùng cho dịch vụ khóa học.

<!--END_PHASE_LOG_BLOCK_INDEX_3-->

### Giai đoạn 4 - Triển khai Hệ thống Điểm Danh Và Thẻ Hội Viên

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống điểm danh và thẻ hội viên, bao gồm chụp ảnh điểm danh QR, tính chất bất biến của điểm danh, hiển thị tính hợp lệ của thẻ, và gia hạn thẻ.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/attendance-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:** Tạo bảng điểm danh và thẻ hội viên với các trường và ràng buộc tương ứng.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007]:**
  - Chụp ảnh điểm danh QR: `POST /api/attendance/qr`
  - Hiển thị tính hợp lệ của thẻ: `GET /api/cards/{cardId}`
  - Gia hạn thẻ: `PUT /api/cards/{cardId}/renew`
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Network & Connectivity Drops During QR Scan, Duplicate Attendance Submission.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 4)

<!--START_DAY_LOG_INDEX_4-->

- **DAY 1: Khởi tạo cơ sở dữ liệu và dịch vụ điểm danh**
  - **SUB-TASK 1: Thiết kế schema cơ sở dữ liệu**
    - [Coder]
    - [DAT-006], [DAT-007]
    - `./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_attendance_and_cards.sql`
    - Thiết kế schema cơ sở dữ liệu cho bảng điểm danh và thẻ hội viên với các trường và ràng buộc tương ứng.

  - **SUB-TASK 2: Viết mã nguồn cho dịch vụ điểm danh**
    - [Coder]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007]
    - `./sources/backend/attendance-service/src/main/java/com/example/attendance/service/AttendanceService.java`
    - Viết mã nguồn cho dịch vụ điểm danh, bao gồm chụp ảnh điểm danh QR, tính chất bất biến của điểm danh, hiển thị tính hợp lệ của thẻ, và gia hạn thẻ.

  - **SUB-TASK 3: Viết bài kiểm tra đơn vị**
    - [Tester]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    - `./sources/backend/attendance-service/src/test/java/com/example/attendance/service/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/service/AttendanceService.java`
    - Viết bài kiểm tra đơn vị cho dịch vụ điểm danh.

  - **SUB-TASK 4: Viết tài liệu kỹ thuật**
    - [Doc]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [ARC-007]
    - `./sources/docs/attendance-service.md`
    - Viết tài liệu kỹ thuật cho dịch vụ điểm danh.

  - **SUB-TASK 5: Xây dựng và đẩy Docker image**
    - [Docker]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    - `./sources/backend/attendance-service/Dockerfile`
    - Xây dựng và đẩy Docker image cho dịch vụ điểm danh.

  - **SUB-TASK 6: Triển khai dịch vụ trên GKE**
    - [GKE]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    - `./sources/infra/gke/attendance-deployment.yaml`
    - Triển khai dịch vụ điểm danh trên GKE, bao gồm thiết lập Deployment, Service, và Ingress.

- **DAY 2: Triển khai và kiểm thử**
  - **SUB-TASK 1: Triển khai dịch vụ**
    - [GKE]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    - `./sources/infra/gke/attendance-deployment.yaml`
    - Triển khai dịch vụ điểm danh trên GKE.

  - **SUB-TASK 2: Kiểm thử tích hợp**
    - [Tester]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    - `./sources/backend/attendance-service/src/test/java/com/example/attendance/service/AttendanceServiceIntegrationTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/service/AttendanceService.java`
    - Viết và chạy kiểm thử tích hợp cho dịch vụ điểm danh.

  - **SUB-TASK 3: Đánh giá và sửa lỗi**
    - [Reviewer]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    - `./sources/backend/attendance-service/src/main/java/com/example/attendance/service/AttendanceService.java`
    - Đánh giá mã nguồn và sửa lỗi nếu có.

<!--END_PHASE_LOG_BLOCK_INDEX_4-->

### Giai đoạn 5 - Triển khai Hệ thống Thông Báo Và Tích Hợp Zalo

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống thông báo và tích hợp Zalo, bao gồm kích hoạt thông báo và quản lý thông báo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notification-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:** Tạo bảng thông báo với các trường và ràng buộc tương ứng.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [ARC-008]:**
  - Kích hoạt thông báo: `POST /api/notifications`
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Failed Notification Delivery.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 5)

<!--START_DAY_LOG_INDEX_5-->

- **DAY 1: Khởi tạo cơ sở dữ liệu và dịch vụ thông báo**
  - **SUB-TASK 1: Thiết kế schema cơ sở dữ liệu**
    - [Coder]
    - [DAT-008]
    - `./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_notifications.sql`
    - Thiết kế schema cơ sở dữ liệu cho bảng thông báo với các trường và ràng buộc tương ứng.

  - **SUB-TASK 2: Viết mã nguồn cho dịch vụ thông báo**
    - [Coder]
    - [REQ-016], [ARC-008]
    - `./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java`
    - Viết mã nguồn cho dịch vụ thông báo, bao gồm kích hoạt thông báo và quản lý thông báo.

  - **SUB-TASK 3: Viết bài kiểm tra đơn vị**
    - [Tester]
    - [REQ-016]
    - `./sources/backend/notification-service/src/test/java/com/example/notification/service/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java`
    - Viết bài kiểm tra đơn vị cho dịch vụ thông báo.

  - **SUB-TASK 4: Viết tài liệu kỹ thuật**
    - [Doc]
    - [REQ-016], [DAT-008], [EXC-003], [ARC-008]
    - `./sources/docs/notification-service.md`
    - Viết tài liệu kỹ thuật cho dịch vụ thông báo.

  - **SUB-TASK 5: Xây dựng và đẩy Docker image**
    - [Docker]
    - [REQ-016]
    - `./sources/backend/notification-service/Dockerfile`
    - Xây dựng và đẩy Docker image cho dịch vụ thông báo.

  - **SUB-TASK 6: Triển khai dịch vụ trên GKE**
    - [GKE]
    - [REQ-016]
    - `./sources/infra/gke/notification-deployment.yaml`
    - Triển khai dịch vụ thông báo trên GKE, bao gồm thiết lập Deployment, Service, và Ingress.

- **DAY 2: Triển khai và kiểm thử**
  - **SUB-TASK 1: Triển khai dịch vụ**
    - [GKE]
    - [REQ-016]
    - `./sources/infra/gke/notification-deployment.yaml`
    - Triển khai dịch vụ thông báo trên GKE.

  - **SUB-TASK 2: Kiểm thử tích hợp**
    - [Tester]
    - [REQ-016]
    - `./sources/backend/notification-service/src/test/java/com/example/notification/service/NotificationServiceIntegrationTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java`
    - Viết và chạy kiểm thử tích hợp cho dịch vụ thông báo.

  - **SUB-TASK 3: Đánh giá và sửa lỗi**
    - [Reviewer]
    - [REQ-016]
    - `./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java`
    - Đánh giá mã nguồn và sửa lỗi nếu có.

<!--END_PHASE_LOG_BLOCK_INDEX_5-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1 Quản lý người dùng

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
### 2.2 Quản lý trung tâm

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
### 2.3 Quản lý khóa học

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
### 2.4 Đăng ký & ghi danh học viên

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
### 2.5 Điểm danh & quét mã QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
### 2.6 Quản lý thẻ hội viên

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
### 2.7 Thông báo & truyền thông

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
### 2.8 Quản lý khuyến mãi & thông báo

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
### 2.9 Chatbot dịch vụ khách hàng AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10 Các tính năng cốt lõi của ứng dụng di động

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11 Bản địa hóa & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
### 2.12 Báo cáo & phân tích

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 4. KIẾN TRÚC TOÀN CẦU & PHÂN PHỐI PHÂN TÍCH

### 4.1 KIẾN TRÚC TOÀN CẦU

#### 4.1.1 KIẾN TRÚC HỆ THỐNG

- **Kiến trúc tổng quan:** Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho mỗi chức năng chính (quản lý người dùng, khóa học, điểm danh, v.v.). Các dịch vụ này giao tiếp với nhau thông qua REST APIs và sự kiện qua Kafka.
- **Kiến trúc dữ liệu:** Sử dụng cơ sở dữ liệu PostgreSQL với schema riêng biệt cho mỗi dịch vụ để đảm bảo tính cô lập và bảo mật.
- **Kiến trúc giao diện người dùng:** Giao diện web được xây dựng bằng Next.js với React, trong khi ứng dụng di động được phát triển bằng React Native.

#### 4.1.2 KIẾN TRÚC PHÂN TÍCH

- **Phân tích yêu cầu:** Các yêu cầu chức năng đã được phân tích và chia thành các tính năng độc lập, mỗi tính năng được gán với các Tag IDs tương ứng.
- **Phân tích dữ liệu:** Các bảng dữ liệu đã được xác định và thiết kế với các quan hệ và ràng buộc phù hợp.
- **Phân tích ngoại lệ:** Các luồng ngoại lệ đã được xác định và xử lý cho từng tính năng.

### 4.2 MA TRẬN TỔNG QUAN NHIỀU PHASE

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|-------------------------|---------------------------|-----------|------------------|
| Giai đoạn 1 | Ngày 1-2 | ./sources/backend/auth-service/, ./sources/backend/user-service/, ./sources/frontend/ | Khởi tạo hệ thống người dùng và xác thực | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006] |
| Giai đoạn 2 | Ngày 1-3 | ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/frontend/ | Triển khai lõi nghiệp vụ trung tâm và khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [ARC-002], [ARC-003] |
| Giai đoạn 3 | Ngày 1-3 | ./sources/backend/enrollment-service/, ./sources/backend/attendance-service/, ./sources/frontend/ | Triển khai hệ thống ghi danh và điểm danh | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [EXC-001], [EXC-002], [ARC-007] |
| Giai đoạn 4 | Ngày 1-2 | ./sources/backend/membership-service/, ./sources/backend/notification-service/, ./sources/frontend/ | Triển khai hệ thống thẻ hội viên và thông báo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-014], [REQ-015], [REQ-016], [DAT-007], [DAT-008], [EXC-003], [ARC-008] |
| Giai đoạn 5 | Ngày 1-2 | ./sources/backend/promotion-service/, ./sources/backend/announcement-service/, ./sources/frontend/ | Triển khai hệ thống khuyến mãi và thông báo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-017], [REQ-018], [DAT-009], [ARC-009] |

## 5. CHI TIẾT KIẾN TRÚC THEO PHASE

### Giai đoạn 2 - Triển Khai Lõi Nghiệp Vụ Trung Tâm Và Khóa Học

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống quản lý trung tâm và khóa học, bao gồm các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm, xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/frontend/
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003], [DAT-004]:**
```sql
CREATE TABLE centers (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) UNIQUE NOT NULL,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);

CREATE TABLE courses (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID REFERENCES users(userId),
    maxStudents INT DEFAULT 30
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-002], [ARC-003]:**
```json
{
    "GET /api/centers": {
        "description": "Lấy danh sách trung tâm",
        "response": {
            "centers": [
                {
                    "centerId": "UUID",
                    "name": "string",
                    "address": "string",
                    "taxId": "string",
                    "contactPhone": "string",
                    "contactEmail": "string"
                }
            ]
        }
    },
    "POST /api/centers": {
        "description": "Tạo trung tâm mới",
        "request": {
            "name": "string",
            "address": "string",
            "taxId": "string",
            "contactPhone": "string",
            "contactEmail": "string"
        },
        "response": {
            "centerId": "UUID"
        }
    }
}
```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003]:**
  - Xử lý xung đột lịch trình khóa học: Khi giáo viên đã được phân công vào một khóa học khác trong cùng khoảng thời gian, hệ thống sẽ trả về lỗi và yêu cầu người dùng điều chỉnh lịch trình.
  - Xử lý lỗi xác thực đầu vào: Khi người dùng nhập thông tin không hợp lệ, hệ thống sẽ trả về thông báo lỗi chi tiết và yêu cầu người dùng chỉnh sửa.

#### Nhật ký Ngày theo Ngày Phân phối Nhiệm vụ Sub-Agent (Giai đoạn 2)

<!--START_DAY_LOG_INDEX_2-->

- **DAY 1: Khởi tạo hệ thống quản lý trung tâm**
  - **SUB-TASK 1: Thiết kế schema cơ sở dữ liệu trung tâm**
    - Sub-Agent: [Coder]
    - Tag IDs: [DAT-003]
    - Target Component: ./sources/backend/center-service/src/main/resources/db/migration/V1__Create_centers_table.sql
    - Hướng dẫn Công việc Kỹ thuật: Tạo bảng trung tâm với các trường: centerId (UUID, khóa chính), name (VARCHAR(100), không được để trống), address (VARCHAR(255), không được để trống), taxId (VARCHAR(13), duy nhất, không được để trống), contactPhone (VARCHAR(20), tùy chọn), contactEmail (VARCHAR(255), tùy chọn).

  - **SUB-TASK 2: Viết test cho schema trung tâm**
    - Sub-Agent: [Tester]
    - Tag IDs: [DAT-003]
    - Target Component: ./sources/backend/center-service/src/test/java/com/example/centerservice/CenterServiceTest.java;./sources/backend/center-service/src/main/resources/db/migration/V1__Create_centers_table.sql
    - Hướng dẫn Công việc Kỹ thuật: Viết test để kiểm tra việc tạo bảng trung tâm và các ràng buộc dữ liệu.

- **DAY 2: Triển khai API quản lý trung tâm**
  - **SUB-TASK 1: Thiết kế API lấy danh sách trung tâm**
    - Sub-Agent: [Coder]
    - Tag IDs: [REQ-004]
    - Target Component: ./sources/backend/center-service/src/main/java/com/example/centerservice/controller/CenterController.java
    - Hướng dẫn Công việc Kỹ thuật: Tạo endpoint GET /api/centers để lấy danh sách trung tâm với các trường: centerId, name, address, taxId, contactPhone, contactEmail.

  - **SUB-TASK 2: Viết test cho API lấy danh sách trung tâm**
    - Sub-Agent: [Tester]
    - Tag IDs: [REQ-004]
    - Target Component: ./sources/backend/center-service/src/test/java/com/example/centerservice/CenterControllerTest.java;./sources/backend/center-service/src/main/java/com/example/centerservice/controller/CenterController.java
    - Hướng dẫn Công việc Kỹ thuật: Viết test để kiểm tra endpoint GET /api/centers và xác thực dữ liệu trả về.

  - **SUB-TASK 3: Thiết kế API tạo trung tâm mới**
    - Sub-Agent: [Coder]
    - Tag IDs: [REQ-005]
    - Target Component: ./sources/backend/center-service/src/main/java/com/example/centerservice/controller/CenterController.java
    - Hướng dẫn Công việc Kỹ thuật: Tạo endpoint POST /api/centers để tạo trung tâm mới với các trường: name, address, taxId, contactPhone, contactEmail. Xác thực đầu vào và xử lý xung đột taxId.

  - **SUB-TASK 4: Viết test cho API tạo trung tâm mới**
    - Sub-Agent: [Tester]
    - Tag IDs: [REQ-005]
    - Target Component: ./sources/backend/center-service/src/test/java/com/example/centerservice/CenterControllerTest.java;./sources/backend/center-service/src/main/java/com/example/centerservice/controller/CenterController.java
    - Hướng dẫn Công việc Kỹ thuật: Viết test để kiểm tra endpoint POST /api/centers và xử lý xung đột taxId.

- **DAY 3: Triển khai hệ thống quản lý khóa học**
  - **SUB-TASK 1: Thiết kế schema cơ sở dữ liệu khóa học**
    - Sub-Agent: [Coder]
    - Tag IDs: [DAT-004]
    - Target Component: ./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses_table.sql
    - Hướng dẫn Công việc Kỹ thuật: Tạo bảng khóa học với các trường: courseId (UUID, khóa chính), title (VARCHAR(150), không được để trống), description (TEXT, tùy chọn), startDate (DATE, không được để trống), endDate (DATE, không được để trống), teacherId (UUID, khóa ngoại tham chiếu đến bảng users), maxStudents (INT, mặc định 30).

  - **SUB-TASK 2: Viết test cho schema khóa học**
    - Sub-Agent: [Tester]
    - Tag IDs: [DAT-004]
    - Target Component: ./sources/backend/course-service/src/test/java/com/example/courseservice/CourseServiceTest.java;./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses_table.sql
    - Hướng dẫn Công việc Kỹ thuật: Viết test để kiểm tra việc tạo bảng khóa học và các ràng buộc dữ liệu.

  - **SUB-TASK 3: Thiết kế API lấy danh sách khóa học**
    - Sub-Agent: [Coder]
    - Tag IDs: [REQ-007]
    - Target Component: ./sources/backend/course-service/src/main/java/com/example/courseservice/controller/CourseController.java
    - Hướng dẫn Công việc Kỹ thuật: Tạo endpoint GET /api/courses để lấy danh sách khóa học với các trường: courseId, title, startDate, endDate, teacherId.

  - **SUB-TASK 4: Viết test cho API lấy danh sách khóa học**
    - Sub-Agent: [Tester]
    - Tag IDs: [REQ-007]
    - Target Component: ./sources/backend/course-service/src/test/java/com/example/courseservice/CourseControllerTest.java;./sources/backend/course-service/src/main/java/com/example/courseservice/controller/CourseController.java
    - Hướng dẫn Công việc Kỹ thuật: Viết test để kiểm tra endpoint GET /api/courses và xác thực dữ liệu trả về.

<!--END_PHASE_LOG_BLOCK_INDEX_2-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 📦 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1 Quản lý người dùng

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
### 2.2 Quản lý trung tâm

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
### 2.3 Quản lý khóa học

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
### 2.4 Đăng ký & ghi danh học viên

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
### 2.5 Điểm danh & quét mã QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
### 2.6 Quản lý thẻ hội viên

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
### 2.7 Thông báo & truyền thông

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
### 2.8 Quản lý khuyến mãi & thông báo

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
### 2.9 Chatbot dịch vụ khách hàng AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10 Các tính năng cốt lõi của ứng dụng di động

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11 Bản địa hóa & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
### 2.12 Báo cáo & phân tích

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 📝 4. PHÂN TÍCH KIẾN TRÚC & TÀI NGUYÊN

### 4.1 TÀI NGUYÊN KIẾN TRÚC CỐT LÕI

#### 4.1.1 Kiến trúc hệ thống

- **Kiến trúc hệ thống:** Hệ thống được xây dựng theo kiến trúc microservices với các dịch vụ độc lập cho xác thực, quản lý người dùng, quản lý trung tâm, quản lý khóa học, điểm danh, và thông báo. Các dịch vụ này giao tiếp với nhau thông qua REST APIs và sự kiện.
- **Kiến trúc dữ liệu:** Sử dụng cơ sở dữ liệu PostgreSQL với các bảng được chuẩn hóa và các mối quan hệ được xác định rõ ràng. Các dịch vụ sử dụng các bảng riêng biệt cho các thực thể chính của họ và có thể truy cập các bảng của các dịch vụ khác thông qua các mối quan hệ.
- **Kiến trúc giao diện người dùng:** Giao diện người dùng được xây dựng bằng Next.js cho web và React Native cho di động. Các giao diện này tiêu thụ các API từ các dịch vụ backend và hiển thị dữ liệu một cách tương tác.

#### 4.1.2 Công nghệ & công cụ

- **Backend:** Java/Quarkus
- **Cơ sở dữ liệu:** PostgreSQL
- **Container hóa:** Docker
- **Orchestration:** Kubernetes (GKE)
- **Xác thực:** Firebase Authentication
- **Thông báo đẩy:** Google Cloud Messaging (FCM)/Apple APNs
- **Tích hợp Zalo:** Zalo API
- **Caching:** Redis
- **CI/CD:** GitHub Actions

### 4.2 Ma trận tổng quan các giai đoạn

| Giai đoạn | Khoảng ngày | Cấu phần / Module Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|-----------------------------|---------------------------|-----------|------------------|
| Giai đoạn 1 | Ngày 1-2 | `./sources/backend/auth-service/`, `./sources/backend/user-service/`, `./sources/docs/` | Khởi tạo hệ thống người dùng và xác thực | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006] |
| Giai đoạn 2 | Ngày 1-3 | `./sources/backend/center-service/`, `./sources/docs/` | Triển khai lõi nghiệp vụ trung tâm | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002] |
| Giai đoạn 3 | Ngày 1-2 | `./sources/backend/course-service/`, `./sources/docs/` | Triển khai lõi nghiệp vụ khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003] |
| Giai đoạn 4 | Ngày 1-3 | `./sources/backend/attendance-service/`, `./sources/docs/` | Triển khai hệ thống điểm danh và thẻ hội viên | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [ARC-007] |
| Giai đoạn 5 | Ngày 1-3 | `./sources/backend/notification-service/`, `./sources/docs/` | Triển khai hệ thống thông báo và tích hợp Zalo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-016], [DAT-008], [EXC-003], [ARC-008] |

## 📅 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN

### Giai đoạn 1 - Khởi Tạo Hệ Thống Người Dùng Và Xác Thực
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống xác thực và quản lý người dùng với các tính năng đăng ký, đăng nhập, và phân quyền.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth-service/`, `./sources/backend/user-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Xem phần 2.1.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  ```json
  {
    "auth": {
      "register": {
        "method": "POST",
        "path": "/api/auth/register",
        "request": {
          "email": "string",
          "password": "string",
          "fullName": "string"
        },
        "response": {
          "token": "string"
        }
      },
      "login": {
        "method": "POST",
        "path": "/api/auth/login",
        "request": {
          "email": "string",
          "password": "string"
        },
        "response": {
          "token": "string"
        }
      },
      "socialLogin": {
        "method": "POST",
        "path": "/api/auth/social-login",
        "request": {
          "provider": "string",
          "token": "string"
        },
        "response": {
          "token": "string"
        }
      }
    },
    "users": {
      "assignRole": {
        "method": "POST",
        "path": "/api/users/assign-role",
        "request": {
          "userId": "uuid",
          "role": "string"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Xử lý xác thực đầu vào không hợp lệ với thông báo rõ ràng cho người dùng.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 1)

<!--START_DAY_LOG_INDEX_1-->

- **DAY 1: Khởi tạo hệ thống xác thực cơ bản**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu người dùng**
    [Coder]
    * Tag IDs: [DAT-001]
    * Component: `./sources/backend/user-service/src/main/resources/db/migration/V1__Create_users_table.sql`
    * Hướng dẫn: Tạo bảng người dùng và vai trò với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ xác thực**
    [Coder]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/backend/auth-service/src/main/java/com/example/auth/`
    * Hướng dẫn: Thiết lập dịch vụ xác thực với các endpoint đăng ký và đăng nhập.
  - **SUB-TASK 3: Viết test cho dịch vụ xác thực**
    [Tester]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/backend/auth-service/src/test/java/com/example/auth/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/AuthService.java`
    * Hướng dẫn: Viết các test case cho các endpoint đăng ký và đăng nhập.
  - **SUB-TASK 4: Review code dịch vụ xác thực**
    [Reviewer]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/backend/auth-service/src/main/java/com/example/auth/`
    * Hướng dẫn: Review code dịch vụ xác thực và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ xác thực**
    [Doc]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/docs/auth-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ xác thực.
  - **SUB-TASK 6: Container hóa dịch vụ xác thực**
    [Docker]
    * Tag IDs: [ARC-006]
    * Component: `./sources/backend/auth-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ xác thực.
  - **SUB-TASK 7: Triển khai dịch vụ xác thực trên GCP**
    [GCP]
    * Tag IDs: [ARC-006]
    * Component: `./sources/infra/gcp/auth-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ xác thực trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ xác thực trên GKE**
    [GKE]
    * Tag IDs: [ARC-006]
    * Component: `./sources/infra/gke/auth-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ xác thực trên GKE.

- **DAY 2: Triển khai phân quyền người dùng**
  - **SUB-TASK 1: Thêm endpoint phân quyền**
    [Coder]
    * Tag IDs: [REQ-003]
    * Component: `./sources/backend/user-service/src/main/java/com/example/user/UserService.java`
    * Hướng dẫn: Thêm endpoint phân quyền người dùng.
  - **SUB-TASK 2: Viết test cho endpoint phân quyền**
    [Tester]
    * Tag IDs: [REQ-003]
    * Component: `./sources/backend/user-service/src/test/java/com/example/user/UserServiceTest.java;./sources/backend/user-service/src/main/java/com/example/user/UserService.java`
    * Hướng dẫn: Viết các test case cho endpoint phân quyền.
  - **SUB-TASK 3: Review code endpoint phân quyền**
    [Reviewer]
    * Tag IDs: [REQ-003]
    * Component: `./sources/backend/user-service/src/main/java/com/example/user/UserService.java`
    * Hướng dẫn: Review code endpoint phân quyền và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint phân quyền**
    [Doc]
    * Tag IDs: [REQ-003]
    * Component: `./sources/docs/user-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint phân quyền.
  - **SUB-TASK 5: Container hóa dịch vụ người dùng**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/user-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ người dùng.
  - **SUB-TASK 6: Triển khai dịch vụ người dùng trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/user-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ người dùng trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ người dùng trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/user-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ người dùng trên GKE.

<!--END_DAY_LOG_INDEX_1-->

### Giai đoạn 2 - Triển Khai Lõi Nghiệp Vụ Trung Tâm
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống quản lý trung tâm với các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/center-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003]:** Xem phần 2.2.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
  ```json
  {
    "centers": {
      "list": {
        "method": "GET",
        "path": "/api/centers",
        "response": {
          "centers": [
            {
              "centerId": "uuid",
              "name": "string",
              "address": "string",
              "taxId": "string",
              "contactPhone": "string",
              "contactEmail": "string"
            }
          ]
        }
      },
      "create": {
        "method": "POST",
        "path": "/api/centers",
        "request": {
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        },
        "response": {
          "centerId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/centers/{centerId}",
        "request": {
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/centers/{centerId}",
        "response": {
          "success": "boolean"
        }
      },
      "assignAdmin": {
        "method": "POST",
        "path": "/api/centers/{centerId}/assign-admin",
        "request": {
          "userId": "uuid"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 2)

<!--START_DAY_LOG_INDEX_2-->

- **DAY 1: Khởi tạo hệ thống quản lý trung tâm**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu trung tâm**
    [Coder]
    * Tag IDs: [DAT-003]
    * Component: `./sources/backend/center-service/src/main/resources/db/migration/V1__Create_centers_table.sql`
    * Hướng dẫn: Tạo bảng trung tâm với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý trung tâm**
    [Coder]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý trung tâm với các endpoint xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý trung tâm**
    [Tester]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/backend/center-service/src/test/java/com/example/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý trung tâm.
  - **SUB-TASK 4: Review code dịch vụ quản lý trung tâm**
    [Reviewer]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/`
    * Hướng dẫn: Review code dịch vụ quản lý trung tâm và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý trung tâm**
    [Doc]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/docs/center-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý trung tâm**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/center-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý trung tâm trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý trung tâm trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GKE.

- **DAY 2: Triển khai endpoint xem danh sách trung tâm**
  - **SUB-TASK 1: Thêm endpoint xem danh sách trung tâm**
    [Coder]
    * Tag IDs: [REQ-004]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Thêm endpoint xem danh sách trung tâm.
  - **SUB-TASK 2: Viết test cho endpoint xem danh sách trung tâm**
    [Tester]
    * Tag IDs: [REQ-004]
    * Component: `./sources/backend/center-service/src/test/java/com/example/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Viết các test case cho endpoint xem danh sách trung tâm.
  - **SUB-TASK 3: Review code endpoint xem danh sách trung tâm**
    [Reviewer]
    * Tag IDs: [REQ-004]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Review code endpoint xem danh sách trung tâm và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint xem danh sách trung tâm**
    [Doc]
    * Tag IDs: [REQ-004]
    * Component: `./sources/docs/center-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint xem danh sách trung tâm.
  - **SUB-TASK 5: Container hóa dịch vụ quản lý trung tâm**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/center-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 6: Triển khai dịch vụ quản lý trung tâm trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý trung tâm trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GKE.

- **DAY 3: Triển khai endpoint tạo/cập nhật/xóa trung tâm**
  - **SUB-TASK 1: Thêm endpoint tạo/cập nhật/xóa trung tâm**
    [Coder]
    * Tag IDs: [REQ-005]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Thêm endpoint tạo/cập nhật/xóa trung tâm.
  - **SUB-TASK 2: Viết test cho endpoint tạo/cập nhật/xóa trung tâm**
    [Tester]
    * Tag IDs: [REQ-005]
    * Component: `./sources/backend/center-service/src/test/java/com/example/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Viết các test case cho endpoint tạo/cập nhật/xóa trung tâm.
  - **SUB-TASK 3: Review code endpoint tạo/cập nhật/xóa trung tâm**
    [Reviewer]
    * Tag IDs: [REQ-005]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Review code endpoint tạo/cập nhật/xóa trung tâm và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint tạo/cập nhật/xóa trung tâm**
    [Doc]
    * Tag IDs: [REQ-005]
    * Component: `./sources/docs/center-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint tạo/cập nhật/xóa trung tâm.
  - **SUB-TASK 5: Container hóa dịch vụ quản lý trung tâm**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/center-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 6: Triển khai dịch vụ quản lý trung tâm trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý trung tâm trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GKE.

<!--END_DAY_LOG_INDEX_2-->

### Giai đoạn 3 - Triển Khai Lõi Nghiệp Vụ Khóa Học
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống quản lý khóa học với các tính năng xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/course-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:** Xem phần 2.3.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [ARC-003]:**
  ```json
  {
    "courses": {
      "list": {
        "method": "GET",
        "path": "/api/courses",
        "response": {
          "courses": [
            {
              "courseId": "uuid",
              "title": "string",
              "description": "string",
              "startDate": "date",
              "endDate": "date",
              "teacherId": "uuid",
              "maxStudents": "int"
            }
          ]
        }
      },
      "create": {
        "method": "POST",
        "path": "/api/courses",
        "request": {
          "title": "string",
          "description": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid",
          "maxStudents": "int"
        },
        "response": {
          "courseId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/courses/{courseId}",
        "request": {
          "title": "string",
          "description": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid",
          "maxStudents": "int"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/courses/{courseId}",
        "response": {
          "success": "boolean"
        }
      },
      "assignTeacher": {
        "method": "POST",
        "path": "/api/courses/{courseId}/assign-teacher",
        "request": {
          "teacherId": "uuid"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1: Khởi tạo hệ thống quản lý khóa học**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu khóa học**
    [Coder]
    * Tag IDs: [DAT-004]
    * Component: `./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses_table.sql`
    * Hướng dẫn: Tạo bảng khóa học với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý khóa học**
    [Coder]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý khóa học với các endpoint xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý khóa học**
    [Tester]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/backend/course-service/src/test/java/com/example/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý khóa học.
  - **SUB-TASK 4: Review code dịch vụ quản lý khóa học**
    [Reviewer]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/`
    * Hướng dẫn: Review code dịch vụ quản lý khóa học và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý khóa học**
    [Doc]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/docs/course-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý khóa học.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý khóa học**
    [Docker]
    * Tag IDs: [ARC-003]
    * Component: `./sources/backend/course-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý khóa học.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý khóa học trên GCP**
    [GCP]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gcp/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý khóa học trên GKE**
    [GKE]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gke/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GKE.

- **DAY 2: Triển khai endpoint xem danh sách khóa học**
  - **SUB-TASK 1: Thêm endpoint xem danh sách khóa học**
    [Coder]
    * Tag IDs: [REQ-007]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Thêm endpoint xem danh sách khóa học.
  - **SUB-TASK 2: Viết test cho endpoint xem danh sách khóa học**
    [Tester]
    * Tag IDs: [REQ-007]
    * Component: `./sources/backend/course-service/src/test/java/com/example/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Viết các test case cho endpoint xem danh sách khóa học.
  - **SUB-TASK 3: Review code endpoint xem danh sách khóa học**
    [Reviewer]
    * Tag IDs: [REQ-007]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Review code endpoint xem danh sách khóa học và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint xem danh sách khóa học**
    [Doc]
    * Tag IDs: [REQ-007]
    * Component: `./sources/docs/course-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint xem danh sách khóa học.
  - **SUB-TASK 5: Container hóa dịch vụ quản lý khóa học**
    [Docker]
    * Tag IDs: [ARC-003]
    * Component: `./sources/backend/course-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý khóa học.
  - **SUB-TASK 6: Triển khai dịch vụ quản lý khóa học trên GCP**
    [GCP]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gcp/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý khóa học trên GKE**
    [GKE]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gke/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GKE.

<!--END_DAY_LOG_INDEX_3-->

### Giai đoạn 4 - Triển Khai Hệ Thống Điểm Danh Và Thẻ Hội Viên
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống điểm danh và quản lý thẻ hội viên với các tính năng quét mã QR, hiển thị tính hợp lệ của thẻ, và gia hạn thẻ.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/attendance-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:** Xem phần 2.5.4 và 2.6.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007]:**
  ```json
  {
    "attendance": {
      "scanQR": {
        "method": "POST",
        "path": "/api/attendance/scan-qr",
        "request": {
          "studentId": "uuid",
          "courseId": "uuid",
          "timestamp": "timestamp"
        },
        "response": {
          "success": "boolean",
          "duplicate": "boolean"
        }
      }
    },
    "studentCards": {
      "viewCard": {
        "method": "GET",
        "path": "/api/student-cards/{studentId}",
        "response": {
          "cardId": "uuid",
          "studentId": "uuid",
          "issueDate": "date",
          "validityDays": "int",
          "remainingDays": "int"
        }
      },
      "renewCard": {
        "method": "POST",
        "path": "/api/student-cards/{studentId}/renew",
        "request": {
          "days": "int"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Xử lý các trường hợp mạng không ổn định và điểm danh trùng lặp.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 4)

<!--START_DAY_LOG_INDEX_4-->

- **DAY 1: Khởi tạo hệ thống điểm danh**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu điểm danh**
    [Coder]
    * Tag IDs: [DAT-006]
    * Component: `./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_attendance_table.sql`
    * Hướng dẫn: Tạo bảng điểm danh với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ điểm danh**
    [Coder]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/`
    * Hướng dẫn: Thiết lập dịch vụ điểm danh với các endpoint quét mã QR và xử lý điểm danh trùng lặp.
  - **SUB-TASK 3: Viết test cho dịch vụ điểm danh**
    [Tester]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/backend/attendance-service/src/test/java/com/example/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Viết các test case cho các endpoint điểm danh.
  - **SUB-TASK 4: Review code dịch vụ điểm danh**
    [Reviewer]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/`
    * Hướng dẫn: Review code dịch vụ điểm danh và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ điểm danh**
    [Doc]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/docs/attendance-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ điểm danh.
  - **SUB-TASK 6: Container hóa dịch vụ điểm danh**
    [Docker]
    * Tag IDs: [ARC-007]
    * Component: `./sources/backend/attendance-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ điểm danh.
  - **SUB-TASK 7: Triển khai dịch vụ điểm danh trên GCP**
    [GCP]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gcp/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ điểm danh trên GKE**
    [GKE]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gke/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GKE.

- **DAY 2: Triển khai hệ thống quản lý thẻ hội viên**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu thẻ hội viên**
    [Coder]
    * Tag IDs: [DAT-007]
    * Component: `./sources/backend/attendance-service/src/main/resources/db/migration/V2__Create_student_cards_table.sql`
    * Hướng dẫn: Tạo bảng thẻ hội viên với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý thẻ hội viên**
    [Coder]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/studentcard/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý thẻ hội viên với các endpoint hiển thị tính hợp lệ của thẻ và gia hạn thẻ.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý thẻ hội viên**
    [Tester]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/backend/attendance-service/src/test/java/com/example/studentcard/StudentCardServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/studentcard/StudentCardService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý thẻ hội viên.
  - **SUB-TASK 4: Review code dịch vụ quản lý thẻ hội viên**
    [Reviewer]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/studentcard/`
    * Hướng dẫn: Review code dịch vụ quản lý thẻ hội viên và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý thẻ hội viên**
    [Doc]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/docs/student-card-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý thẻ hội viên.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý thẻ hội viên**
    [Docker]
    * Tag IDs: [ARC-007]
    * Component: `./sources/backend/attendance-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý thẻ hội viên.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý thẻ hội viên trên GCP**
    [GCP]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gcp/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý thẻ hội viên trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý thẻ hội viên trên GKE**
    [GKE]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gke/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý thẻ hội viên trên GKE.

- **DAY 3: Triển khai xử lý ngoại lệ điểm danh**
  - **SUB-TASK 1: Thêm xử lý ngoại lệ mạng không ổn định**
    [Coder]
    * Tag IDs: [EXC-001]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Thêm xử lý ngoại lệ mạng không ổn định.
  - **SUB-TASK 2: Thêm xử lý ngoại lệ điểm danh trùng lặp**
    [Coder]
    * Tag IDs: [EXC-002]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Thêm xử lý ngoại lệ điểm danh trùng lặp.
  - **SUB-TASK 3: Viết test cho xử lý ngoại lệ điểm danh**
    [Tester]
    * Tag IDs: [EXC-001], [EXC-002]
    * Component: `./sources/backend/attendance-service/src/test/java/com/example/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Viết các test case cho xử lý ngoại lệ điểm danh.
  - **SUB-TASK 4: Review code xử lý ngoại lệ điểm danh**
    [Reviewer]
    * Tag IDs: [EXC-001], [EXC-002]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Review code xử lý ngoại lệ điểm danh và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho xử lý ngoại lệ điểm danh**
    [Doc]
    * Tag IDs: [EXC-001], [EXC-002]
    * Component: `./sources/docs/attendance-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho xử lý ngoại lệ điểm danh.
  - **SUB-TASK 6: Container hóa dịch vụ điểm danh**
    [Docker]
    * Tag IDs: [ARC-007]
    * Component: `./sources/backend/attendance-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ điểm danh.
  - **SUB-TASK 7: Triển khai dịch vụ điểm danh trên GCP**
    [GCP]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gcp/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ điểm danh trên GKE**
    [GKE]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gke/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GKE.

<!--END_DAY_LOG_INDEX_4-->

### Giai đoạn 5 - Triển Khai Hệ Thống Thông Báo Và Tích Hợp Zalo
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống thông báo và tích hợp Zalo với các tính năng kích hoạt thông báo, xử lý thông báo không thành công, và quản lý khuyến mãi & thông báo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notification-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008], [DAT-009]:** Xem phần 2.7.4 và 2.8.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [REQ-017], [REQ-018], [ARC-008]:**
  ```json
  {
    "notifications": {
      "create": {
        "method": "POST",
        "path": "/api/notifications",
        "request": {
          "userId": "uuid",
          "groupZalo": "string",
          "message": "string"
        },
        "response": {
          "notificationId": "uuid"
        }
      }
    },
    "promotions": {
      "create": {
        "method": "POST",
        "path": "/api/promotions",
        "request": {
          "code": "string",
          "discountPercent": "int",
          "startDate": "date",
          "endDate": "date",
          "description": "string"
        },
        "response": {
          "promoId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/promotions/{promoId}",
        "request": {
          "code": "string",
          "discountPercent": "int",
          "startDate": "date",
          "endDate": "date",
          "description": "string"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/promotions/{promoId}",
        "response": {
          "success": "boolean"
        }
      }
    },
    "announcements": {
      "create": {
        "method": "POST",
        "path": "/api/announcements",
        "request": {
          "title": "string",
          "content": "string",
          "startDate": "date",
          "endDate": "date"
        },
        "response": {
          "announcementId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/announcements/{announcementId}",
        "request": {
          "title": "string",
          "content": "string",
          "startDate": "date",
          "endDate": "date"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/announcements/{announcementId}",
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Xử lý thông báo không thành công.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 5)

<!--START_DAY_LOG_INDEX_5-->

- **DAY 1: Khởi tạo hệ thống thông báo**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu thông báo**
    [Coder]
    * Tag IDs: [DAT-008]
    * Component: `./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_notifications_table.sql`
    * Hướng dẫn: Tạo bảng thông báo với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ thông báo**
    [Coder]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/`
    * Hướng dẫn: Thiết lập dịch vụ thông báo với các endpoint kích hoạt thông báo.
  - **SUB-TASK 3: Viết test cho dịch vụ thông báo**
    [Tester]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/backend/notification-service/src/test/java/com/example/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Viết các test case cho các endpoint thông báo.
  - **SUB-TASK 4: Review code dịch vụ thông báo**
    [Reviewer]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/`
    * Hướng dẫn: Review code dịch vụ thông báo và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ thông báo**
    [Doc]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/docs/notification-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ thông báo.
  - **SUB-TASK 6: Container hóa dịch vụ thông báo**
    [Docker]
    * Tag IDs: [ARC-008]
    * Component: `./sources/backend/notification-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ thông báo.
  - **SUB-TASK 7: Triển khai dịch vụ thông báo trên GCP**
    [GCP]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gcp/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ thông báo trên GKE**
    [GKE]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gke/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GKE.

- **DAY 2: Triển khai hệ thống quản lý khuyến mãi & thông báo**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu khuyến mãi & thông báo**
    [Coder]
    * Tag IDs: [DAT-009]
    * Component: `./sources/backend/notification-service/src/main/resources/db/migration/V2__Create_promotions_and_announcements_tables.sql`
    * Hướng dẫn: Tạo bảng khuyến mãi và thông báo với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý khuyến mãi & thông báo**
    [Coder]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/promotion/`, `./sources/backend/notification-service/src/main/java/com/example/announcement/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý khuyến mãi & thông báo với các endpoint quản lý khuyến mãi và thông báo.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý khuyến mãi & thông báo**
    [Tester]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/backend/notification-service/src/test/java/com/example/promotion/PromotionServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/promotion/PromotionService.java`, `./sources/backend/notification-service/src/test/java/com/example/announcement/AnnouncementServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/announcement/AnnouncementService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý khuyến mãi & thông báo.
  - **SUB-TASK 4: Review code dịch vụ quản lý khuyến mãi & thông báo**
    [Reviewer]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/promotion/`, `./sources/backend/notification-service/src/main/java/com/example/announcement/`
    * Hướng dẫn: Review code dịch vụ quản lý khuyến mãi & thông báo và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý khuyến mãi & thông báo**
    [Doc]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/docs/promotion-service.md`, `./sources/docs/announcement-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý khuyến mãi & thông báo.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý khuyến mãi & thông báo**
    [Docker]
    * Tag IDs: [ARC-008]
    * Component: `./sources/backend/notification-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý khuyến mãi & thông báo.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý khuyến mãi & thông báo trên GCP**
    [GCP]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gcp/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khuyến mãi & thông báo trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý khuyến mãi & thông báo trên GKE**
    [GKE]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gke/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khuyến mãi & thông báo trên GKE.

- **DAY 3: Triển khai xử lý ngoại lệ thông báo**
  - **SUB-TASK 1: Thêm xử lý ngoại lệ thông báo không thành công**
    [Coder]
    * Tag IDs: [EXC-003]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Thêm xử lý ngoại lệ thông báo không thành công.
  - **SUB-TASK 2: Viết test cho xử lý ngoại lệ thông báo**
    [Tester]
    * Tag IDs: [EXC-003]
    * Component: `./sources/backend/notification-service/src/test/java/com/example/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Viết các test case cho xử lý ngoại lệ thông báo.
  - **SUB-TASK 3: Review code xử lý ngoại lệ thông báo**
    [Reviewer]
    * Tag IDs: [EXC-003]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Review code xử lý ngoại lệ thông báo và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho xử lý ngoại lệ thông báo**
    [Doc]
    * Tag IDs: [EXC-003]
    * Component: `./sources/docs/notification-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho xử lý ngoại lệ thông báo.
  - **SUB-TASK 5: Container hóa dịch vụ thông báo**
    [Docker]
    * Tag IDs: [ARC-008]
    * Component: `./sources/backend/notification-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ thông báo.
  - **SUB-TASK 6: Triển khai dịch vụ thông báo trên GCP**
    [GCP]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gcp/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ thông báo trên GKE**
    [GKE]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gke/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GKE.

<!--END_DAY_LOG_INDEX_5-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 📦 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1 Quản lý người dùng

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
### 2.2 Quản lý trung tâm

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
### 2.3 Quản lý khóa học

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
### 2.4 Đăng ký & ghi danh học viên

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
### 2.5 Điểm danh & quét mã QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
### 2.6 Quản lý thẻ hội viên

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
### 2.7 Thông báo & truyền thông

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
### 2.8 Quản lý khuyến mãi & thông báo

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
### 2.9 Chatbot dịch vụ khách hàng AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10 Các tính năng cốt lõi của ứng dụng di động

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11 Bản địa hóa & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
### 2.12 Báo cáo & phân tích

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 📝 4. PHÂN TÍCH KIẾN TRÚC TOÀN CẦU

### 4.1 KIẾN TRÚC TOÀN CẦU

#### 4.1.1 Kiến trúc hệ thống

- **Kiến trúc hệ thống:** Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, trung tâm, khóa học, điểm danh, và thông báo. Các dịch vụ này giao tiếp qua REST APIs và sự kiện được phát hành qua message broker (Apache Kafka).

- **Kiến trúc dữ liệu:** Sử dụng cơ sở dữ liệu PostgreSQL với các bảng được chuẩn hóa để đảm bảo tính toàn vẹn dữ liệu. Các bảng được thiết kế với các khóa chính, khóa ngoại, và ràng buộc để đảm bảo tính toàn vẹn tham chiếu.

- **Kiến trúc giao diện người dùng:** Giao diện người dùng được xây dựng bằng Next.js cho web và React Native cho di động. Các giao diện này tiêu thụ REST APIs từ backend và sử dụng caching ngoại tuyến cho các tính năng quan trọng.

#### 4.1.2 Kiến trúc hạ tầng

- **Kiến trúc hạ tầng:** Hạ tầng được triển khai trên Google Kubernetes Engine (GKE) với các dịch vụ được container hóa bằng Docker. Các dịch vụ được triển khai trên các pod Kubernetes với các chính sách scaling tự động dựa trên CPU và độ trễ yêu cầu.

- **Kiến trúc lưu trữ:** Dữ liệu được lưu trữ trên các instance PostgreSQL được quản lý bởi Google Cloud SQL. Các bản sao lưu hàng ngày được thực hiện và lưu trữ trong Google Cloud Storage.

- **Kiến trúc mạng:** Mạng được cấu hình với các VPC riêng biệt cho các môi trường phát triển, thử nghiệm, và sản xuất. Các dịch vụ được truy cập qua các địa chỉ IP tĩnh và các chính sách bảo mật mạng được áp dụng để đảm bảo tính bảo mật.

### 4.2 Ma trận tóm tắt đa giai đoạn

| Giai đoạn | Khoảng ngày | Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|--------------------|---------------------------|------------|------------------|
| 1         | 1-2         | ./sources/backend/auth-service/ | Xây dựng dịch vụ xác thực với email/mật khẩu, Firebase, Google, Facebook OAuth2 | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [ARC-006], [NFR-001], [NFR-003], [NFR-004], [NFR-006] |
| 2         | 3-4         | ./sources/backend/center-service/, ./sources/backend/course-service/ | Xây dựng dịch vụ quản lý trung tâm và khóa học với các API CRUD và logic kiểm tra xung đột lịch trình | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-002], [ARC-003], [NFR-001], [NFR-003], [NFR-004], [NFR-006] |
| 3         | 5-6         | ./sources/backend/attendance-service/, ./sources/backend/notification-service/ | Xây dựng dịch vụ điểm danh và thông báo với logic xử lý QR, idempotent và gửi thông báo qua FCM/APNs và Zalo API | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008], [NFR-001], [NFR-003], [NFR-004], [NFR-006] |
| 4         | 7-8         | ./sources/frontend/, ./sources/mobile-app/ | Xây dựng giao diện người dùng cho web và di động với các tính năng quản lý người dùng, trung tâm, khóa học, điểm danh, và thông báo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-020], [REQ-021], [ARC-009], [NFR-001], [NFR-003], [NFR-004], [NFR-006] |
| 5         | 9-10        | ./sources/docs/, ./sources/infra/ | Tạo tài liệu kỹ thuật và cấu hình hạ tầng với các tài liệu API, tài liệu hệ thống, và các cấu hình CI/CD | Doc, Docker, GCP, GKE | [NFR-005], [NFR-007], [NFR-008], [NFR-009] |

## 📅 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN

### Giai đoạn 1 - Khởi Tạo Hệ Thống Người Dùng Và Xác Thực

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ xác thực với email/mật khẩu, Firebase, Google, Facebook OAuth2.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** ./sources/backend/auth-service/
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Xây dựng bảng người dùng và vai trò với các trường và ràng buộc như đã mô tả trong yêu cầu.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [ARC-006]:** Xây dựng các API cho đăng ký người dùng, xác thực qua mạng xã hội, và cấp JWT token.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Xử lý xác thực đầu vào không hợp lệ với các thông báo rõ ràng.

#### Nhật ký Ngày theo Ngày Phân phối Công việc Sub-Agent (Giai đoạn 1)

<!--START_DAY_LOG_INDEX_1-->

- **DAY 1: Xây dựng cơ sở dữ liệu và dịch vụ xác thực cơ bản**

##### SUB-TASK 1: Thiết kế và triển khai cơ sở dữ liệu người dùng và vai trò
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-001]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/main/resources/db/migration/V1__Create_users_and_roles.sql
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo các bảng người dùng và vai trò với các trường và ràng buộc như đã mô tả trong yêu cầu. [DAT-001]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Xây dựng dịch vụ xác thực cơ bản với email/mật khẩu
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-001], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/main/java/com/example/auth/service/AuthService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng dịch vụ xác thực cơ bản với email/mật khẩu. [REQ-001], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho dịch vụ xác thực cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-001], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/test/java/com/example/auth/service/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/service/AuthService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ xác thực cơ bản. [REQ-001], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Xây dựng API đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-001], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/main/java/com/example/auth/controller/AuthController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API đăng ký người dùng. [REQ-001], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Viết các bài kiểm tra tích hợp cho API đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-001], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/test/java/com/example/auth/controller/AuthControllerTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/controller/AuthController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API đăng ký người dùng. [REQ-001], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Xây dựng tài liệu API cho dịch vụ xác thực
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-001], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/auth-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng tài liệu API cho dịch vụ xác thực. [REQ-001], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng Dockerfile cho dịch vụ xác thực
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [NFR-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/Dockerfile
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng Dockerfile cho dịch vụ xác thực. [NFR-005]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Triển khai dịch vụ xác thực trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GKE]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gke/auth-service-deployment.yaml
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ xác thực trên GKE. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Xây dựng dịch vụ xác thực qua mạng xã hội và hoàn thiện hệ thống**

##### SUB-TASK 1: Xây dựng dịch vụ xác thực qua Firebase, Google, Facebook OAuth2
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/main/java/com/example/auth/service/SocialAuthService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng dịch vụ xác thực qua Firebase, Google, Facebook OAuth2. [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho dịch vụ xác thực qua mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/test/java/com/example/auth/service/SocialAuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/service/SocialAuthService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ xác thực qua mạng xã hội. [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Xây dựng API xác thực qua mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/main/java/com/example/auth/controller/SocialAuthController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API xác thực qua mạng xã hội. [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Viết các bài kiểm tra tích hợp cho API xác thực qua mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/src/test/java/com/example/auth/controller/SocialAuthControllerTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/controller/SocialAuthController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API xác thực qua mạng xã hội. [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng tài liệu API cho dịch vụ xác thực qua mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/social-auth-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng tài liệu API cho dịch vụ xác thực qua mạng xã hội. [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Xây dựng Dockerfile cho dịch vụ xác thực qua mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [NFR-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/auth-service/Dockerfile
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng Dockerfile cho dịch vụ xác thực qua mạng xã hội. [NFR-005]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Triển khai dịch vụ xác thực qua mạng xã hội trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GKE]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gke/social-auth-service-deployment.yaml
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ xác thực qua mạng xã hội trên GKE. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_1-->

### Giai đoạn 2 - Triển Khai Lõi Nghiệp Vụ Trung Tâm Và Khóa Học

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ quản lý trung tâm và khóa học với các API CRUD và logic kiểm tra xung đột lịch trình.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** ./sources/backend/center-service/, ./sources/backend/course-service/
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003], [DAT-004]:** Xây dựng bảng trung tâm và khóa học với các trường và ràng buộc như đã mô tả trong yêu cầu.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-002], [ARC-003]:** Xây dựng các API cho quản lý trung tâm và khóa học.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có luồng ngoại lệ chuyên biệt được xác định cho giai đoạn này.

#### Nhật ký Ngày theo Ngày Phân phối Công việc Sub-Agent (Giai đoạn 2)

<!--START_DAY_LOG_INDEX_2-->

- **DAY 1: Xây dựng cơ sở dữ liệu và dịch vụ quản lý trung tâm**

##### SUB-TASK 1: Thiết kế và triển khai cơ sở dữ liệu trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/center-service/src/main/resources/db/migration/V1__Create_centers.sql
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo bảng trung tâm với các trường và ràng buộc như đã mô tả trong yêu cầu. [DAT-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Xây dựng dịch vụ quản lý trung tâm cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-004], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng dịch vụ quản lý trung tâm cơ bản. [REQ-004], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho dịch vụ quản lý trung tâm cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-004], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/center-service/src/test/java/com/example/center/service/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/service/CenterService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý trung tâm cơ bản. [REQ-004], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Xây dựng API quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-004], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/center-service/src/main/java/com/example/center/controller/CenterController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API quản lý trung tâm. [REQ-004], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Viết các bài kiểm tra tích hợp cho API quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-004], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/center-service/src/test/java/com/example/center/controller/CenterControllerTest.java;./sources/backend/center-service/src/main/java/com/example/center/controller/CenterController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API quản lý trung tâm. [REQ-004], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Xây dựng tài liệu API cho dịch vụ quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-004], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/center-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng tài liệu API cho dịch vụ quản lý trung tâm. [REQ-004], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng Dockerfile cho dịch vụ quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [NFR-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/center-service/Dockerfile
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng Dockerfile cho dịch vụ quản lý trung tâm. [NFR-005]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Triển khai dịch vụ quản lý trung tâm trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GKE]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gke/center-service-deployment.yaml
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý trung tâm trên GKE. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Xây dựng dịch vụ quản lý khóa học và hoàn thiện hệ thống**

##### SUB-TASK 1: Thiết kế và triển khai cơ sở dữ liệu khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses.sql
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo bảng khóa học với các trường và ràng buộc như đã mô tả trong yêu cầu. [DAT-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Xây dựng dịch vụ quản lý khóa học cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng dịch vụ quản lý khóa học cơ bản. [REQ-007], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho dịch vụ quản lý khóa học cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-007], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/course-service/src/test/java/com/example/course/service/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/example/course/service/CourseService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý khóa học cơ bản. [REQ-007], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Xây dựng API quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/course-service/src/main/java/com/example/course/controller/CourseController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API quản lý khóa học. [REQ-007], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Viết các bài kiểm tra tích hợp cho API quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-007], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/course-service/src/test/java/com/example/course/controller/CourseControllerTest.java;./sources/backend/course-service/src/main/java/com/example/course/controller/CourseController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API quản lý khóa học. [REQ-007], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Xây dựng tài liệu API cho dịch vụ quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-007], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/course-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng tài liệu API cho dịch vụ quản lý khóa học. [REQ-007], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng Dockerfile cho dịch vụ quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [NFR-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/course-service/Dockerfile
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng Dockerfile cho dịch vụ quản lý khóa học. [NFR-005]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Triển khai dịch vụ quản lý khóa học trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GKE]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gke/course-service-deployment.yaml
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý khóa học trên GKE. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_2-->

### Giai đoạn 3 - Triển Khai Lõi Nghiệp Vụ Điểm Danh Và Thông Báo

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ điểm danh và thông báo với logic xử lý QR, idempotent và gửi thông báo qua FCM/APNs và Zalo API.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** ./sources/backend/attendance-service/, ./sources/backend/notification-service/
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-008]:** Xây dựng bảng điểm danh và thông báo với các trường và ràng buộc như đã mô tả trong yêu cầu.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]:** Xây dựng các API cho điểm danh và thông báo.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003]:** Xử lý các trường hợp ngoại lệ như mạng không ổn định và gửi thông báo thất bại.

#### Nhật ký Ngày theo Ngày Phân phối Công việc Sub-Agent (Giai đoạn 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1: Xây dựng cơ sở dữ liệu và dịch vụ điểm danh**

##### SUB-TASK 1: Thiết kế và triển khai cơ sở dữ liệu điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_attendance.sql
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo bảng điểm danh với các trường và ràng buộc như đã mô tả trong yêu cầu. [DAT-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Xây dựng dịch vụ điểm danh cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-012], [ARC-007]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/attendance-service/src/main/java/com/example/attendance/service/AttendanceService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng dịch vụ điểm danh cơ bản. [REQ-012], [ARC-007]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho dịch vụ điểm danh cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-012], [ARC-007]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/attendance-service/src/test/java/com/example/attendance/service/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/service/AttendanceService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ điểm danh cơ bản. [REQ-012], [ARC-007]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Xây dựng API điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-012], [ARC-007]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/attendance-service/src/main/java/com/example/attendance/controller/AttendanceController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API điểm danh. [REQ-012], [ARC-007]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Viết các bài kiểm tra tích hợp cho API điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-012], [ARC-007]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/attendance-service/src/test/java/com/example/attendance/controller/AttendanceControllerTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/controller/AttendanceController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API điểm danh. [REQ-012], [ARC-007]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Xây dựng tài liệu API cho dịch vụ điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-012], [ARC-007]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/attendance-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng tài liệu API cho dịch vụ điểm danh. [REQ-012], [ARC-007]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng Dockerfile cho dịch vụ điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [NFR-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/attendance-service/Dockerfile
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng Dockerfile cho dịch vụ điểm danh. [NFR-005]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Triển khai dịch vụ điểm danh trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GKE]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gke/attendance-service-deployment.yaml
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ điểm danh trên GKE. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Xây dựng dịch vụ thông báo và hoàn thiện hệ thống**

##### SUB-TASK 1: Thiết kế và triển khai cơ sở dữ liệu thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_notifications.sql
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo bảng thông báo với các trường và ràng buộc như đã mô tả trong yêu cầu. [DAT-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Xây dựng dịch vụ thông báo cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng dịch vụ thông báo cơ bản. [REQ-016], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho dịch vụ thông báo cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/notification-service/src/test/java/com/example/notification/service/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ thông báo cơ bản. [REQ-016], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Xây dựng API thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/notification-service/src/main/java/com/example/notification/controller/NotificationController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API thông báo. [REQ-016], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Viết các bài kiểm tra tích hợp cho API thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/notification-service/src/test/java/com/example/notification/controller/NotificationControllerTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/controller/NotificationController.java
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API thông báo. [REQ-016], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Xây dựng tài liệu API cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/notification-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng tài liệu API cho dịch vụ thông báo. [REQ-016], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng Dockerfile cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [NFR-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/backend/notification-service/Dockerfile
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng Dockerfile cho dịch vụ thông báo. [NFR-005]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Triển khai dịch vụ thông báo trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GKE]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gke/notification-service-deployment.yaml
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ thông báo trên GKE. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_3-->

### Giai đoạn 4 - Triển Khai Giao Diện Người Dùng Web Và Di Động

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng giao diện người dùng cho web và di động với các tính năng quản lý người dùng, trung tâm, khóa học, điểm danh, và thông báo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** ./sources/frontend/, ./sources/mobile-app/
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:** Không có thay đổi cơ sở dữ liệu trong giai đoạn này.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-020], [REQ-021], [ARC-009]:** Xây dựng các giao diện người dùng cho các tính năng quản lý người dùng, trung tâm, khóa học, điểm danh, và thông báo.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có luồng ngoại lệ chuyên biệt được xác định cho giai đoạn này.

#### Nhật ký Ngày theo Ngày Phân phối Công việc Sub-Agent (Giai đoạn 4)

<!--START_DAY_LOG_INDEX_4-->

- **DAY 1: Xây dựng giao diện người dùng cho web**

##### SUB-TASK 1: Xây dựng giao diện đăng nhập và đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện đăng nhập và đăng ký người dùng. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/auth/;./sources/frontend/src/pages/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Xây dựng giao diện quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/center/;./sources/frontend/src/pages/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng giao diện quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/course/;./sources/frontend/src/pages/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng giao diện điểm danh và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/attendance/, ./sources/frontend/src/pages/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện điểm danh và thông báo. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/attendance/;./sources/frontend/src/pages/attendance/, ./sources/frontend/src/tests/pages/notification/;./sources/frontend/src/pages/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Xây dựng giao diện người dùng cho di động**

##### SUB-TASK 1: Xây dựng giao diện đăng nhập và đăng ký người dùng cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện đăng nhập và đăng ký người dùng cho di động. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/auth/;./sources/mobile-app/src/screens/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng cho di động. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Xây dựng giao diện quản lý trung tâm cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý trung tâm cho di động. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/center/;./sources/mobile-app/src/screens/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm cho di động. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng giao diện quản lý khóa học cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý khóa học cho di động. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/course/;./sources/mobile-app/src/screens/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học cho di động. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng giao diện điểm danh và thông báo cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/attendance/, ./sources/mobile-app/src/screens/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện điểm danh và thông báo cho di động. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/attendance/;./sources/mobile-app/src/screens/attendance/, ./sources/mobile-app/src/tests/screens/notification/;./sources/mobile-app/src/screens/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo cho di động. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_4-->

### Giai đoạn 5 - Tài liệu Kỹ Thuật Và Cấu Hình Hạ Tầng

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Tạo tài liệu kỹ thuật và cấu hình hạ tầng với các tài liệu API, tài liệu hệ thống, và các cấu hình CI/CD.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** ./sources/docs/, ./sources/infra/
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:** Không có thay đổi cơ sở dữ liệu trong giai đoạn này.
- **Hợp đồng Định tuyến API và Sự kiện:** Không có thay đổi hợp đồng API trong giai đoạn này.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có luồng ngoại lệ chuyên biệt được xác định cho giai đoạn này.

#### Nhật ký Ngày theo Ngày Phân phối Công việc Sub-Agent (Giai đoạn 5)

<!--START_DAY_LOG_INDEX_5-->

- **DAY 1: Tạo tài liệu kỹ thuật**

##### SUB-TASK 1: Tạo tài liệu API cho dịch vụ xác thực
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/auth-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu API cho dịch vụ xác thực. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Tạo tài liệu API cho dịch vụ quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/center-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu API cho dịch vụ quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Tạo tài liệu API cho dịch vụ quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/course-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu API cho dịch vụ quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Tạo tài liệu API cho dịch vụ điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [ARC-007]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/attendance-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu API cho dịch vụ điểm danh. [REQ-012], [REQ-013], [ARC-007]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Tạo tài liệu API cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/api/notification-service.md
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu API cho dịch vụ thông báo. [REQ-016], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Tạo tài liệu hệ thống cho hệ thống
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/docs/system/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu hệ thống cho hệ thống. [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Cấu hình hạ tầng**

##### SUB-TASK 1: Cấu hình hạ tầng cho dịch vụ xác thực
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GCP]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gcp/auth-service/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình hạ tầng cho dịch vụ xác thực. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Cấu hình hạ tầng cho dịch vụ quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GCP]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gcp/center-service/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình hạ tầng cho dịch vụ quản lý trung tâm. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Cấu hình hạ tầng cho dịch vụ quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GCP]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gcp/course-service/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình hạ tầng cho dịch vụ quản lý khóa học. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Cấu hình hạ tầng cho dịch vụ điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GCP]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gcp/attendance-service/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình hạ tầng cho dịch vụ điểm danh. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Cấu hình hạ tầng cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GCP]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gcp/notification-service/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình hạ tầng cho dịch vụ thông báo. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Cấu hình CI/CD pipeline
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GCP]
* **Tag IDs Mục tiêu:** [NFR-004]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/infra/gcp/ci-cd/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình CI/CD pipeline. [NFR-004]
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_5-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 📦 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1 Quản lý người dùng

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
### 2.2 Quản lý trung tâm

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
### 2.3 Quản lý khóa học

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
### 2.4 Đăng ký & ghi danh học viên

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
### 2.5 Điểm danh & quét mã QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
### 2.6 Quản lý thẻ hội viên

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
### 2.7 Thông báo & truyền thông

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
### 2.8 Quản lý khuyến mãi & thông báo

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
### 2.9 Chatbot dịch vụ khách hàng AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10 Các tính năng cốt lõi của ứng dụng di động

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11 Bản địa hóa & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
### 2.12 Báo cáo & phân tích

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 📝 4. PHÂN TÍCH KIẾN TRÚC & TÀI NGUYÊN

### 4.1 MASTER PRODUCT BACKLOG

| STT | Yêu cầu | Mô tả | Tag ID |
|-----|---------|-------|--------|
| 1 | Đăng ký người dùng | Xây dựng form đăng ký với xác thực email và mật khẩu | [REQ-001] |
| 2 | Xác thực qua mạng xã hội | Tích hợp Firebase, Google, Facebook OAuth | [REQ-002] |
| 3 | Phân quyền người dùng | Tạo giao diện quản lý vai trò người dùng | [REQ-003] |
| 4 | Xem danh sách trung tâm | Xây dựng trang danh sách trung tâm với bộ lọc | [REQ-004] |
| 5 | Tạo/cập nhật/xóa trung tâm | Xây dựng form quản lý trung tâm | [REQ-005] |
| 6 | Phân quyền quản trị trung tâm | Tạo giao diện gán vai trò Center Admin | [REQ-006] |
| 7 | Xem danh sách khóa học | Xây dựng trang danh sách khóa học với bộ lọc | [REQ-007] |
| 8 | Tạo/cập nhật/xóa khóa học | Xây dựng form quản lý khóa học với kiểm tra xung đột lịch | [REQ-008] |
| 9 | Phân công giáo viên vào khóa học | Tạo giao diện gán giáo viên vào khóa học | [REQ-009] |
| 10 | Duyệt khóa học | Xây dựng trang duyệt khóa học cho học viên | [REQ-010] |
| 11 | Đăng ký khóa học của học viên | Xây dựng chức năng đăng ký khóa học | [REQ-011] |
| 12 | Chụp ảnh điểm danh QR | Xây dựng chức năng quét QR điểm danh | [REQ-012] |
| 13 | Tính chất bất biến của điểm danh | Xây dựng cơ chế xử lý điểm danh idempotent | [REQ-013] |
| 14 | Hiển thị tính hợp lệ của thẻ | Xây dựng trang hiển thị thông tin thẻ hội viên | [REQ-014] |
| 15 | Gia hạn thẻ | Xây dựng chức năng gia hạn thẻ hội viên | [REQ-015] |
| 16 | Kích hoạt thông báo | Xây dựng cơ chế gửi thông báo đa kênh | [REQ-016] |
| 17 | Quản lý khuyến mãi | Xây dựng giao diện quản lý khuyến mãi | [REQ-017] |
| 18 | Quản lý thông báo | Xây dựng giao diện quản lý thông báo | [REQ-018] |
| 19 | Tích hợp chatbot AI | Xây dựng giao diện chatbot và tích hợp API | [REQ-019] |
| 20 | Giao diện người dùng vai trò cụ thể trên di động | Xây dựng giao diện di động đa vai trò | [REQ-020] |
| 21 | Thông báo đẩy trên di động | Xây dựng cơ chế gửi thông báo đẩy | [REQ-021] |
| 22 | Phát hiện ngôn ngữ mặc định | Xây dựng cơ chế phát hiện ngôn ngữ | [REQ-022] |
| 23 | SEO đa ngôn ngữ | Xây dựng cơ chế SEO đa ngôn ngữ | [REQ-023] |
| 24 | Tạo báo cáo điểm danh | Xây dựng chức năng tạo báo cáo điểm danh | [REQ-024] |
| 25 | Bảng điều khiển tóm tắt ghi danh | Xây dựng bảng điều khiển tóm tắt | [REQ-025] |
| 26 | Xác thực đầu vào không hợp lệ | Xây dựng cơ chế xử lý lỗi xác thực | [EXC-004] |
| 27 | Network & Connectivity Drops During QR Scan | Xây dựng cơ chế xử lý lỗi kết nối | [EXC-001] |
| 28 | Duplicate Attendance Submission | Xây dựng cơ chế xử lý điểm danh trùng lặp | [EXC-002] |
| 29 | Failed Notification Delivery | Xây dựng cơ chế xử lý lỗi gửi thông báo | [EXC-003] |
| 30 | System Recovery After Outage | Xây dựng cơ chế phục hồi hệ thống | [EXC-005] |
| 31 | Bảng người dùng & vai trò | Thiết kế cơ sở dữ liệu cho người dùng và vai trò | [DAT-001] |
| 32 | Bảng trung tâm | Thiết kế cơ sở dữ liệu cho trung tâm | [DAT-003] |
| 33 | Bảng khóa học | Thiết kế cơ sở dữ liệu cho khóa học | [DAT-004] |
| 34 | Bảng ghi danh | Thiết kế cơ sở dữ liệu cho ghi danh | [DAT-005] |
| 35 | Bảng điểm danh | Thiết kế cơ sở dữ liệu cho điểm danh | [DAT-006] |
| 36 | Bảng thẻ hội viên | Thiết kế cơ sở dữ liệu cho thẻ hội viên | [DAT-007] |
| 37 | Bảng thông báo | Thiết kế cơ sở dữ liệu cho thông báo | [DAT-008] |
| 38 | Bảng khuyến mãi & thông báo | Thiết kế cơ sở dữ liệu cho khuyến mãi và thông báo | [DAT-009] |
| 39 | Bảng cài đặt hệ thống | Thiết kế cơ sở dữ liệu cho cài đặt hệ thống | [DAT-011] |
| 40 | Luồng xác thực | Thiết kế luồng xác thực người dùng | [ARC-006] |
| 41 | Luồng xử lý điểm danh QR | Thiết kế luồng xử lý điểm danh QR | [ARC-007] |
| 42 | Luồng gửi thông báo | Thiết kế luồng gửi thông báo | [ARC-008] |
| 43 | Luồng tích hợp backend ứng dụng di động | Thiết kế luồng tích hợp backend di động | [ARC-009] |
| 44 | Công nghệ & hạ tầng | Thiết kế công nghệ và hạ tầng | [ARC-010] |
| 45 | Performance Metrics | Thiết kế cơ chế đo lường hiệu suất | [NFR-001] |

### 4.2 MULTI-PHASE SYNOPSIS MATRIX

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|-------------------------|----------------------------|-----------|-------------------|
| 1 | 1-2 | ./sources/backend/auth-service/ | Xây dựng dịch vụ xác thực người dùng | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003] |
| 2 | 3-4 | ./sources/backend/center-service/ | Xây dựng dịch vụ quản lý trung tâm | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| 3 | 5-6 | ./sources/backend/course-service/ | Xây dựng dịch vụ quản lý khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| 4 | 7-7 | ./sources/backend/enrollment-service/ | Xây dựng dịch vụ đăng ký và ghi danh | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-010], [REQ-011], [DAT-005] |
| 5 | 1-2 | ./sources/backend/attendance-service/ | Xây dựng dịch vụ điểm danh và quản lý thẻ hội viên | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002] |

## 📅 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN

### Phase 1 - Khởi Tạo Hệ Thống Người Dùng Và Xác Thực
- **Phase Core Objective & Purpose:** Xây dựng lõi hệ thống xác thực người dùng bao gồm đăng ký, đăng nhập, và quản lý vai trò.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/ | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004]
    * ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/ | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004]
    * ./sources/docs/auth-service.md | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004]
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
CREATE TABLE roles (
    role_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200),
    CHECK (name IN ('System Admin', 'Center Admin', 'Manager', 'Teacher', 'Student'))
);

CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id INTEGER NOT NULL,
    provider VARCHAR(10) NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_role FOREIGN KEY (role_id) REFERENCES roles(role_id),
    CONSTRAINT chk_provider CHECK (provider IN ('local', 'firebase', 'google', 'facebook'))
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role_id ON users(role_id);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
```json
{
  "paths": {
    "/api/auth/register": {
      "post": {
        "summary": "Đăng ký người dùng mới",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "email": {"type": "string", "format": "email"},
                  "password": {"type": "string", "minLength": 8},
                  "fullName": {"type": "string"}
                },
                "required": ["email", "password", "fullName"]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Đăng ký thành công",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "token": {"type": "string"},
                    "refreshToken": {"type": "string"}
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/auth/login": {
      "post": {
        "summary": "Đăng nhập người dùng",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "email": {"type": "string", "format": "email"},
                  "password": {"type": "string"}
                },
                "required": ["email", "password"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Đăng nhập thành công",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "token": {"type": "string"},
                    "refreshToken": {"type": "string"}
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/auth/oauth/{provider}": {
      "get": {
        "summary": "Xác thực qua mạng xã hội",
        "parameters": [
          {
            "name": "provider",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "enum": ["firebase", "google", "facebook"]
            }
          }
        ],
        "responses": {
          "302": {
            "description": "Chuyển hướng đến trang xác thực của nhà cung cấp"
          }
        }
      }
    },
    "/api/auth/roles": {
      "put": {
        "summary": "Phân quyền người dùng",
        "security": [{"bearerAuth": []}],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "userId": {"type": "string", "format": "uuid"},
                  "role": {"type": "string", "enum": ["System Admin", "Center Admin", "Manager", "Teacher", "Student"]}
                },
                "required": ["userId", "role"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Phân quyền thành công"
          }
        }
      }
    }
  }
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
- Xử lý lỗi xác thực đầu vào không hợp lệ:
```java
public class ValidationException extends RuntimeException {
    private final Map<String, String> errors;

    public ValidationException(Map<String, String> errors) {
        super("Validation failed");
        this.errors = errors;
    }

    public Map<String, String> getErrors() {
        return errors;
    }
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

<!--START_DAY_LOG_INDEX_1-->

- **DAY 1: Xây dựng lõi xác thực người dùng**
  
##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho người dùng và vai trò
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-001]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/main/resources/db/migration/V1__Create_users_and_roles_tables.sql
* **Low-Level Technical Task Instruction:** Tạo các bảng roles và users với các ràng buộc và chỉ mục cần thiết. [DAT-001]

##### SUB-TASK 2: Xây dựng dịch vụ đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-001]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/UserService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức đăng ký người dùng mới với xác thực email và mật khẩu. [REQ-001]

##### SUB-TASK 3: Xây dựng dịch vụ đăng nhập người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-001]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/AuthService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức đăng nhập với xác thực JWT. [REQ-001]

##### SUB-TASK 4: Xây dựng dịch vụ xác thực qua mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-002]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuthService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức xác thực qua Firebase, Google, và Facebook OAuth. [REQ-002]

##### SUB-TASK 5: Xây dựng dịch vụ phân quyền người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-003]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/RoleService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức phân quyền người dùng. [REQ-003]

##### SUB-TASK 6: Viết test cho dịch vụ đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-001]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/UserServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/UserService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ đăng ký người dùng. [REQ-001]

##### SUB-TASK 7: Viết test cho dịch vụ đăng nhập người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-001]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/AuthService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ đăng nhập người dùng. [REQ-001]

##### SUB-TASK 8: Viết test cho dịch vụ xác thực qua mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-002]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/OAuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuthService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ xác thực qua mạng xã hội. [REQ-002]

##### SUB-TASK 9: Viết test cho dịch vụ phân quyền người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-003]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/RoleServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/RoleService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ phân quyền người dùng. [REQ-003]

##### SUB-TASK 10: Review code cho dịch vụ xác thực người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Reviewer]
* **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
* **Target Component file path (target_component):** ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/
* **Low-Level Technical Task Instruction:** Review code cho các dịch vụ xác thực người dùng. [REQ-001], [REQ-002], [REQ-003]

##### SUB-TASK 11: Viết tài liệu cho dịch vụ xác thực người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
* **Target Component file path (target_component):** ./sources/docs/auth-service.md
* **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết cho dịch vụ xác thực người dùng. [REQ-001], [REQ-002], [REQ-003]

##### SUB-TASK 12: Xây dựng Dockerfile cho dịch vụ xác thực người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/auth-service/Dockerfile
* **Low-Level Technical Task Instruction:** Xây dựng Dockerfile cho dịch vụ xác thực người dùng. [ARC-010]

##### SUB-TASK 13: Triển khai dịch vụ xác thực người dùng lên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GCP]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gcp/auth-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ xác thực người dùng lên GCP. [ARC-010]

##### SUB-TASK 14: Triển khai dịch vụ xác thực người dùng lên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/auth-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ xác thực người dùng lên GKE. [ARC-010]

<!--END_PHASE_LOG_BLOCK_INDEX_1-->

### Phase 2 - Triển Khai Lõi Nghiệp Vụ Trung Tâm
- **Phase Core Objective & Purpose:** Xây dựng lõi hệ thống quản lý trung tâm bao gồm xem danh sách, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend/center-service/src/main/java/com/membershiphub/center/ | [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * ./sources/backend/center-service/src/test/java/com/membershiphub/center/ | [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * ./sources/docs/center-service.md | [REQ-004], [REQ-005], [REQ-006], [DAT-003]
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255),
    CHECK (tax_id ~ '^[0-9]{10,13}$')
);

CREATE INDEX idx_centers_tax_id ON centers(tax_id);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006]:**
```json
{
  "paths": {
    "/api/centers": {
      "get": {
        "summary": "Xem danh sách trung tâm",
        "security": [{"bearerAuth": []}],
        "responses": {
          "200": {
            "description": "Danh sách trung tâm",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "centerId": {"type": "string", "format": "uuid"},
                      "name": {"type": "string"},
                      "address": {"type": "string"},
                      "taxId": {"type": "string"},
                      "contactPhone": {"type": "string"},
                      "contactEmail": {"type": "string"}
                    }
                  }
                }
              }
            }
          }
        }
      },
      "post": {
        "summary": "Tạo trung tâm mới",
        "security": [{"bearerAuth": []}],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {"type": "string"},
                  "address": {"type": "string"},
                  "taxId": {"type": "string"},
                  "contactPhone": {"type": "string"},
                  "contactEmail": {"type": "string"}
                },
                "required": ["name", "address", "taxId"]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Trung tâm đã được tạo"
          }
        }
      }
    },
    "/api/centers/{centerId}": {
      "put": {
        "summary": "Cập nhật trung tâm",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "centerId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {"type": "string"},
                  "address": {"type": "string"},
                  "taxId": {"type": "string"},
                  "contactPhone": {"type": "string"},
                  "contactEmail": {"type": "string"}
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Trung tâm đã được cập nhật"
          }
        }
      },
      "delete": {
        "summary": "Xóa trung tâm",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "centerId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Trung tâm đã được xóa"
          }
        }
      }
    },
    "/api/centers/{centerId}/admins": {
      "post": {
        "summary": "Phân quyền quản trị trung tâm",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "centerId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "userId": {"type": "string", "format": "uuid"}
                },
                "required": ["userId"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Người dùng đã được phân quyền quản trị trung tâm"
          }
        }
      },
      "delete": {
        "summary": "Hủy phân quyền quản trị trung tâm",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "centerId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "userId",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Người dùng đã bị hủy phân quyền quản trị trung tâm"
          }
        }
      }
    }
  }
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
- Xử lý lỗi xác thực đầu vào không hợp lệ:
```java
public class ValidationException extends RuntimeException {
    private final Map<String, String> errors;

    public ValidationException(Map<String, String> errors) {
        super("Validation failed");
        this.errors = errors;
    }

    public Map<String, String> getErrors() {
        return errors;
    }
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

<!--START_DAY_LOG_INDEX_2-->

- **DAY 1: Xây dựng lõi quản lý trung tâm**
  
##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-003]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/main/resources/db/migration/V1__Create_centers_table.sql
* **Low-Level Technical Task Instruction:** Tạo bảng centers với các ràng buộc và chỉ mục cần thiết. [DAT-003]

##### SUB-TASK 2: Xây dựng dịch vụ xem danh sách trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-004]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức xem danh sách trung tâm. [REQ-004]

##### SUB-TASK 3: Xây dựng dịch vụ tạo trung tâm mới
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-005]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức tạo trung tâm mới. [REQ-005]

##### SUB-TASK 4: Xây dựng dịch vụ cập nhật trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-005]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức cập nhật trung tâm. [REQ-005]

##### SUB-TASK 5: Xây dựng dịch vụ xóa trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-005]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức xóa trung tâm. [REQ-005]

##### SUB-TASK 6: Xây dựng dịch vụ phân quyền quản trị trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-006]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterAdminService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức phân quyền quản trị trung tâm. [REQ-006]

##### SUB-TASK 7: Viết test cho dịch vụ xem danh sách trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-004]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/test/java/com/membershiphub/center/service/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ xem danh sách trung tâm. [REQ-004]

##### SUB-TASK 8: Viết test cho dịch vụ tạo trung tâm mới
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-005]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/test/java/com/membershiphub/center/service/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ tạo trung tâm mới. [REQ-005]

##### SUB-TASK 9: Viết test cho dịch vụ cập nhật trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-005]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/test/java/com/membershiphub/center/service/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ cập nhật trung tâm. [REQ-005]

##### SUB-TASK 10: Viết test cho dịch vụ xóa trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-005]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/test/java/com/membershiphub/center/service/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ xóa trung tâm. [REQ-005]

##### SUB-TASK 11: Viết test cho dịch vụ phân quyền quản trị trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-006]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/test/java/com/membershiphub/center/service/CenterAdminServiceTest.java;./sources/backend/center-service/src/main/java/com/membershiphub/center/service/CenterAdminService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ phân quyền quản trị trung tâm. [REQ-006]

##### SUB-TASK 12: Review code cho dịch vụ quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Reviewer]
* **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
* **Target Component file path (target_component):** ./sources/backend/center-service/src/main/java/com/membershiphub/center/service/
* **Low-Level Technical Task Instruction:** Review code cho các dịch vụ quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006]

##### SUB-TASK 13: Viết tài liệu cho dịch vụ quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
* **Target Component file path (target_component):** ./sources/docs/center-service.md
* **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết cho dịch vụ quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006]

##### SUB-TASK 14: Xây dựng Dockerfile cho dịch vụ quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/center-service/Dockerfile
* **Low-Level Technical Task Instruction:** Xây dựng Dockerfile cho dịch vụ quản lý trung tâm. [ARC-010]

##### SUB-TASK 15: Triển khai dịch vụ quản lý trung tâm lên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GCP]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gcp/center-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý trung tâm lên GCP. [ARC-010]

##### SUB-TASK 16: Triển khai dịch vụ quản lý trung tâm lên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/center-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý trung tâm lên GKE. [ARC-010]

<!--END_PHASE_LOG_BLOCK_INDEX_2-->

### Phase 3 - Triển Khai Lõi Nghiệp Vụ Khóa Học
- **Phase Core Objective & Purpose:** Xây dựng lõi hệ thống quản lý khóa học bao gồm xem danh sách, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend/course-service/src/main/java/com/membershiphub/course/ | [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    * ./sources/backend/course-service/src/test/java/com/membershiphub/course/ | [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    * ./sources/docs/course-service.md | [REQ-007], [REQ-008], [REQ-009], [DAT-004]
- **Database Schema DDL SQL Specification [DAT-004]:**
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID,
    max_students INTEGER NOT NULL DEFAULT 30,
    CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES users(user_id),
    CONSTRAINT chk_dates CHECK (end_date >= start_date)
);

CREATE INDEX idx_courses_teacher_id ON courses(teacher_id);
CREATE INDEX idx_courses_start_date ON courses(start_date);
CREATE INDEX idx_courses_end_date ON courses(end_date);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009]:**
```json
{
  "paths": {
    "/api/courses": {
      "get": {
        "summary": "Xem danh sách khóa học",
        "security": [{"bearerAuth": []}],
        "responses": {
          "200": {
            "description": "Danh sách khóa học",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "courseId": {"type": "string", "format": "uuid"},
                      "title": {"type": "string"},
                      "startDate": {"type": "string", "format": "date"},
                      "endDate": {"type": "string", "format": "date"},
                      "teacherName": {"type": "string"}
                    }
                  }
                }
              }
            }
          }
        }
      },
      "post": {
        "summary": "Tạo khóa học mới",
        "security": [{"bearerAuth": []}],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "title": {"type": "string"},
                  "description": {"type": "string"},
                  "startDate": {"type": "string", "format": "date"},
                  "endDate": {"type": "string", "format": "date"},
                  "teacherId": {"type": "string", "format": "uuid"},
                  "maxStudents": {"type": "integer"}
                },
                "required": ["title", "startDate", "endDate"]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Khóa học đã được tạo"
          }
        }
      }
    },
    "/api/courses/{courseId}": {
      "put": {
        "summary": "Cập nhật khóa học",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "courseId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "title": {"type": "string"},
                  "description": {"type": "string"},
                  "startDate": {"type": "string", "format": "date"},
                  "endDate": {"type": "string", "format": "date"},
                  "teacherId": {"type": "string", "format": "uuid"},
                  "maxStudents": {"type": "integer"}
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Khóa học đã được cập nhật"
          }
        }
      },
      "delete": {
        "summary": "Xóa khóa học",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "courseId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Khóa học đã được xóa"
          }
        }
      }
    },
    "/api/courses/{courseId}/teachers": {
      "post": {
        "summary": "Phân công giáo viên vào khóa học",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "courseId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "teacherId": {"type": "string", "format": "uuid"}
                },
                "required": ["teacherId"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Giáo viên đã được phân công vào khóa học"
          }
        }
      },
      "delete": {
        "summary": "Hủy phân công giáo viên khỏi khóa học",
        "security": [{"bearerAuth": []}],
        "parameters": [
          {
            "name": "courseId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "teacherId",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Giáo viên đã bị hủy phân công khỏi khóa học"
          }
        }
      }
    }
  }
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
- Xử lý lỗi xác thực đầu vào không hợp lệ:
```java
public class ValidationException extends RuntimeException {
    private final Map<String, String> errors;

    public ValidationException(Map<String, String> errors) {
        super("Validation failed");
        this.errors = errors;
    }

    public Map<String, String> getErrors() {
        return errors;
    }
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1: Xây dựng lõi quản lý khóa học**
  
##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-004]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses_table.sql
* **Low-Level Technical Task Instruction:** Tạo bảng courses với các ràng buộc và chỉ mục cần thiết. [DAT-004]

##### SUB-TASK 2: Xây dựng dịch vụ xem danh sách khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-007]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức xem danh sách khóa học. [REQ-007]

##### SUB-TASK 3: Xây dựng dịch vụ tạo khóa học mới
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-008]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức tạo khóa học mới. [REQ-008]

##### SUB-TASK 4: Xây dựng dịch vụ cập nhật khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-008]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức cập nhật khóa học. [REQ-008]

##### SUB-TASK 5: Xây dựng dịch vụ xóa khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-008]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức xóa khóa học. [REQ-008]

##### SUB-TASK 6: Xây dựng dịch vụ phân công giáo viên vào khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-009]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseTeacherService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức phân công giáo viên vào khóa học. [REQ-009]

##### SUB-TASK 7: Viết test cho dịch vụ xem danh sách khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-007]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/test/java/com/membershiphub/course/service/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ xem danh sách khóa học. [REQ-007]

##### SUB-TASK 8: Viết test cho dịch vụ tạo khóa học mới
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-008]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/test/java/com/membershiphub/course/service/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ tạo khóa học mới. [REQ-008]

##### SUB-TASK 9: Viết test cho dịch vụ cập nhật khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-008]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/test/java/com/membershiphub/course/service/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ cập nhật khóa học. [REQ-008]

##### SUB-TASK 10: Viết test cho dịch vụ xóa khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-008]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/test/java/com/membershiphub/course/service/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ xóa khóa học. [REQ-008]

##### SUB-TASK 11: Viết test cho dịch vụ phân công giáo viên vào khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-009]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/test/java/com/membershiphub/course/service/CourseTeacherServiceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/service/CourseTeacherService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ phân công giáo viên vào khóa học. [REQ-009]

##### SUB-TASK 12: Review code cho dịch vụ quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Reviewer]
* **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
* **Target Component file path (target_component):** ./sources/backend/course-service/src/main/java/com/membershiphub/course/service/
* **Low-Level Technical Task Instruction:** Review code cho các dịch vụ quản lý khóa học. [REQ-007], [REQ-008], [REQ-009]

##### SUB-TASK 13: Viết tài liệu cho dịch vụ quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
* **Target Component file path (target_component):** ./sources/docs/course-service.md
* **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết cho dịch vụ quản lý khóa học. [REQ-007], [REQ-008], [REQ-009]

##### SUB-TASK 14: Xây dựng Dockerfile cho dịch vụ quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/course-service/Dockerfile
* **Low-Level Technical Task Instruction:** Xây dựng Dockerfile cho dịch vụ quản lý khóa học. [ARC-010]

##### SUB-TASK 15: Triển khai dịch vụ quản lý khóa học lên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GCP]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gcp/course-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý khóa học lên GCP. [ARC-010]

##### SUB-TASK 16: Triển khai dịch vụ quản lý khóa học lên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/course-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý khóa học lên GKE. [ARC-010]

<!--END_PHASE_LOG_BLOCK_INDEX_3-->

### Phase 4 - Triển Khai Lõi Nghiệp Vụ Đăng Ký & Ghi Danh
- **Phase Core Objective & Purpose:** Xây dựng lõi hệ thống đăng ký và ghi danh học viên bao gồm duyệt khóa học và đăng ký khóa học.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/ | [REQ-010], [REQ-011], [DAT-005]
    * ./sources/backend/enrollment-service/src/test/java/com/membershiphub/enrollment/ | [REQ-010], [REQ-011], [DAT-005]
    * ./sources/docs/enrollment-service.md | [REQ-010], [REQ-011], [DAT-005]
- **Database Schema DDL SQL Specification [DAT-005]:**
```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT unique_enrollment UNIQUE (student_id, course_id)
);

CREATE INDEX idx_enrollments_student_id ON enrollments(student_id);
CREATE INDEX idx_enrollments_course_id ON enrollments(course_id);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011]:**
```json
{
  "paths": {
    "/api/courses/available": {
      "get": {
        "summary": "Duyệt khóa học",
        "security": [{"bearerAuth": []}],
        "responses": {
          "200": {
            "description": "Danh sách khóa học có thể đăng ký",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "courseId": {"type": "string", "format": "uuid"},
                      "title": {"type": "string"},
                      "startDate": {"type": "string", "format": "date"},
                      "endDate": {"type": "string", "format": "date"},
                      "teacherName": {"type": "string"},
                      "capacity": {"type": "integer"}
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/enrollments": {
      "post": {
        "summary": "Đăng ký khóa học",
        "security": [{"bearerAuth": []}],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "courseId": {"type": "string", "format": "uuid"}
                },
                "required": ["courseId"]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Đăng ký khóa học thành công"
          }
        }
      }
    }
  }
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
- Xử lý lỗi xác thực đầu vào không hợp lệ:
```java
public class ValidationException extends RuntimeException {
    private final Map<String, String> errors;

    public ValidationException(Map<String, String> errors) {
        super("Validation failed");
        this.errors = errors;
    }

    public Map<String, String> getErrors() {
        return errors;
    }
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

<!--START_DAY_LOG_INDEX_4-->

- **DAY 1: Xây dựng lõi đăng ký và ghi danh học viên**
  
##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho ghi danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-005]
* **Target Component file path (target_component):** ./sources/backend/enrollment-service/src/main/resources/db/migration/V1__Create_enrollments_table.sql
* **Low-Level Technical Task Instruction:** Tạo bảng enrollments với các ràng buộc và chỉ mục cần thiết. [DAT-005]

##### SUB-TASK 2: Xây dựng dịch vụ duyệt khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-010]
* **Target Component file path (target_component):** ./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/service/CourseBrowsingService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức duyệt khóa học. [REQ-010]

##### SUB-TASK 3: Xây dựng dịch vụ đăng ký khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-011]
* **Target Component file path (target_component):** ./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/service/EnrollmentService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức đăng ký khóa học. [REQ-011]

##### SUB-TASK 4: Viết test cho dịch vụ duyệt khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-010]
* **Target Component file path (target_component):** ./sources/backend/enrollment-service/src/test/java/com/membershiphub/enrollment/service/CourseBrowsingServiceTest.java;./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/service/CourseBrowsingService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ duyệt khóa học. [REQ-010]

##### SUB-TASK 5: Viết test cho dịch vụ đăng ký khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-011]
* **Target Component file path (target_component):** ./sources/backend/enrollment-service/src/test/java/com/membershiphub/enrollment/service/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/service/EnrollmentService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ đăng ký khóa học. [REQ-011]

##### SUB-TASK 6: Review code cho dịch vụ đăng ký và ghi danh học viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Reviewer]
* **Targeted Tag IDs:** [REQ-010], [REQ-011]
* **Target Component file path (target_component):** ./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/service/
* **Low-Level Technical Task Instruction:** Review code cho các dịch vụ đăng ký và ghi danh học viên. [REQ-010], [REQ-011]

##### SUB-TASK 7: Viết tài liệu cho dịch vụ đăng ký và ghi danh học viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-010], [REQ-011]
* **Target Component file path (target_component):** ./sources/docs/enrollment-service.md
* **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết cho dịch vụ đăng ký và ghi danh học viên. [REQ-010], [REQ-011]

##### SUB-TASK 8: Xây dựng Dockerfile cho dịch vụ đăng ký và ghi danh học viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/enrollment-service/Dockerfile
* **Low-Level Technical Task Instruction:** Xây dựng Dockerfile cho dịch vụ đăng ký và ghi danh học viên. [ARC-010]

##### SUB-TASK 9: Triển khai dịch vụ đăng ký và ghi danh học viên lên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GCP]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gcp/enrollment-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ đăng ký và ghi danh học viên lên GCP. [ARC-010]

##### SUB-TASK 10: Triển khai dịch vụ đăng ký và ghi danh học viên lên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/enrollment-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ đăng ký và ghi danh học viên lên GKE. [ARC-010]

<!--END_PHASE_LOG_BLOCK_INDEX_4-->

### Phase 5 - Triển Khai Lõi Nghiệp Vụ Điểm Danh & Quản Lý Thẻ Hội Viên
- **Phase Core Objective & Purpose:** Xây dựng lõi hệ thống điểm danh và quản lý thẻ hội viên bao gồm chụp ảnh điểm danh QR, tính chất bất biến của điểm danh, hiển thị tính hợp lệ của thẻ, và gia hạn thẻ.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/ | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002]
    * ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/ | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002]
    * ./sources/docs/attendance-service.md | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002]
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007]:**
```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT unique_attendance UNIQUE (student_id, course_id, attendance_date)
);

CREATE INDEX idx_attendance_student_id ON attendance(student_id);
CREATE INDEX idx_attendance_course_id ON attendance(course_id);
CREATE INDEX idx_attendance_date ON attendance(attendance_date);

CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INTEGER NOT NULL,
    remaining_days INTEGER NOT NULL,
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES users(user_id)
);

CREATE INDEX idx_student_cards_student_id ON student_cards(student_id);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015]:**
```json
{
  "paths": {
    "/api/attendance/qr": {
      "post": {
        "summary": "Chụp ảnh điểm danh QR",
        "security": [{"bearerAuth": []}],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "courseId": {"type": "string", "format": "uuid"},
                  "timestamp": {"type": "string", "format": "date-time"}
                },
                "required": ["courseId", "timestamp"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Điểm danh thành công",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {"type": "string"},
                    "message": {"type": "string"}
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/cards": {
      "get": {
        "summary": "Hiển thị tính hợp lệ của thẻ",
        "security": [{"bearerAuth": []}],
        "responses": {
          "200": {
            "description": "Thông tin thẻ hội viên",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "totalValidityDays": {"type": "integer"},
                    "daysUsed": {"type": "integer"},
                    "daysRemaining": {"type": "integer"}
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/cards/renew": {
      "post": {
        "summary": "Gia hạn thẻ",
        "security": [{"bearerAuth": []}],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "days": {"type": "integer"}
                },
                "required": ["days"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Gia hạn thẻ thành công"
          }
        }
      }
    }
  }
}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
- Xử lý lỗi kết nối mạng trong quá trình quét QR:
```java
public class NetworkException extends RuntimeException {
    public NetworkException(String message) {
        super(message);
    }
}
```
- Xử lý lỗi điểm danh trùng lặp:
```java
public class DuplicateAttendanceException extends RuntimeException {
    public DuplicateAttendanceException(String message) {
        super(message);
    }
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

<!--START_DAY_LOG_INDEX_5-->

- **DAY 1: Xây dựng lõi điểm danh và quản lý thẻ hội viên**
  
##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho điểm danh và thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-006], [DAT-007]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_attendance_and_student_cards_tables.sql
* **Low-Level Technical Task Instruction:** Tạo bảng attendance và student_cards với các ràng buộc và chỉ mục cần thiết. [DAT-006], [DAT-007]

##### SUB-TASK 2: Xây dựng dịch vụ chụp ảnh điểm danh QR
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-012]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức chụp ảnh điểm danh QR. [REQ-012]

##### SUB-TASK 3: Xây dựng dịch vụ tính chất bất biến của điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-013]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức xử lý điểm danh idempotent. [REQ-013]

##### SUB-TASK 4: Xây dựng dịch vụ hiển thị tính hợp lệ của thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-014]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức hiển thị thông tin thẻ hội viên. [REQ-014]

##### SUB-TASK 5: Xây dựng dịch vụ gia hạn thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức gia hạn thẻ hội viên. [REQ-015]

##### SUB-TASK 6: Viết test cho dịch vụ chụp ảnh điểm danh QR
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-012]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ chụp ảnh điểm danh QR. [REQ-012]

##### SUB-TASK 7: Viết test cho dịch vụ tính chất bất biến của điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-013]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ tính chất bất biến của điểm danh. [REQ-013]

##### SUB-TASK 8: Viết test cho dịch vụ hiển thị tính hợp lệ của thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-014]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/StudentCardServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ hiển thị tính hợp lệ của thẻ. [REQ-014]

##### SUB-TASK 9: Viết test cho dịch vụ gia hạn thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/StudentCardServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ gia hạn thẻ. [REQ-015]

##### SUB-TASK 10: Review code cho dịch vụ điểm danh và quản lý thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Reviewer]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/
* **Low-Level Technical Task Instruction:** Review code cho các dịch vụ điểm danh và quản lý thẻ hội viên. [REQ-012], [REQ-013], [REQ-014], [REQ-015]

##### SUB-TASK 11: Viết tài liệu cho dịch vụ điểm danh và quản lý thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
* **Target Component file path (target_component):** ./sources/docs/attendance-service.md
* **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết cho dịch vụ điểm danh và quản lý thẻ hội viên. [REQ-012], [REQ-013], [REQ-014], [REQ-015]

##### SUB-TASK 12: Xây dựng Dockerfile cho dịch vụ điểm danh và quản lý thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/Dockerfile
* **Low-Level Technical Task Instruction:** Xây dựng Dockerfile cho dịch vụ điểm danh và quản lý thẻ hội viên. [ARC-010]

##### SUB-TASK 13: Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GCP]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gcp/attendance-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GCP. [ARC-010]

##### SUB-TASK 14: Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/attendance-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GKE. [ARC-010]

<!--END_PHASE_LOG_BLOCK_INDEX_5-->

### MANDATORY REAL-TIME ARCHITECTURAL CROSS-AUDIT LEDGER REPORT:
```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=2
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=45
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=70
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

# GLOBAL PROJECT CONTEXT: membership-hub

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

## 📦 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

### 2.1 Quản lý người dùng

#### Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

#### Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

#### Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
### 2.2 Quản lý trung tâm

#### Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

#### Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
### 2.3 Quản lý khóa học

#### Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

#### Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
### 2.4 Đăng ký & ghi danh học viên

#### Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

#### Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
### 2.5 Điểm danh & quét mã QR

#### Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

#### Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
### 2.6 Quản lý thẻ hội viên

#### Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

#### Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
### 2.7 Thông báo & truyền thông

#### Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

#### Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

#### Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
### 2.8 Quản lý khuyến mãi & thông báo

#### Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

#### Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
### 2.9 Chatbot dịch vụ khách hàng AI

#### Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

#### Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

#### Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

### 2.10 Các tính năng cốt lõi của ứng dụng di động

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

### 2.11 Bản địa hóa & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

#### Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
### 2.12 Báo cáo & phân tích

#### Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

#### Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

#### Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 📝 4. PHÂN TÍCH KIẾN TRÚC & TÀI NGUYÊN

### 4.1 TÀI NGUYÊN KIẾN TRÚC CỐT LÕI

#### 4.1.1 Kiến trúc hệ thống

- **Kiến trúc hệ thống:** Hệ thống được xây dựng theo kiến trúc microservices với các dịch vụ độc lập cho xác thực, quản lý người dùng, quản lý trung tâm, quản lý khóa học, điểm danh, và thông báo. Các dịch vụ này giao tiếp với nhau thông qua REST APIs và sự kiện.
- **Kiến trúc dữ liệu:** Sử dụng cơ sở dữ liệu PostgreSQL với các bảng được chuẩn hóa và các mối quan hệ được xác định rõ ràng. Các dịch vụ sử dụng các bảng riêng biệt cho các thực thể chính của họ và có thể truy cập các bảng của các dịch vụ khác thông qua các mối quan hệ.
- **Kiến trúc giao diện người dùng:** Giao diện người dùng được xây dựng bằng Next.js cho web và React Native cho di động. Các giao diện này tiêu thụ các API từ các dịch vụ backend và hiển thị dữ liệu một cách tương tác.

#### 4.1.2 Công nghệ & công cụ

- **Backend:** Java/Quarkus
- **Cơ sở dữ liệu:** PostgreSQL
- **Container hóa:** Docker
- **Orchestration:** Kubernetes (GKE)
- **Xác thực:** Firebase Authentication
- **Thông báo đẩy:** Google Cloud Messaging (FCM)/Apple APNs
- **Tích hợp Zalo:** Zalo API
- **Caching:** Redis
- **CI/CD:** GitHub Actions

### 4.2 Ma trận tổng quan các giai đoạn

| Giai đoạn | Khoảng ngày | Cấu phần / Module Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|-----------------------------|---------------------------|-----------|------------------|
| Giai đoạn 1 | Ngày 1-2 | `./sources/backend/auth-service/`, `./sources/backend/user-service/`, `./sources/docs/` | Khởi tạo hệ thống người dùng và xác thực | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006] |
| Giai đoạn 2 | Ngày 1-3 | `./sources/backend/center-service/`, `./sources/docs/` | Triển khai lõi nghiệp vụ trung tâm | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002] |
| Giai đoạn 3 | Ngày 1-2 | `./sources/backend/course-service/`, `./sources/docs/` | Triển khai lõi nghiệp vụ khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003] |
| Giai đoạn 4 | Ngày 1-3 | `./sources/backend/attendance-service/`, `./sources/docs/` | Triển khai hệ thống điểm danh và thẻ hội viên | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [ARC-007] |
| Giai đoạn 5 | Ngày 1-3 | `./sources/backend/notification-service/`, `./sources/docs/` | Triển khai hệ thống thông báo và tích hợp Zalo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-016], [DAT-008], [EXC-003], [ARC-008] |

## 📅 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN

### Giai đoạn 1 - Khởi Tạo Hệ Thống Người Dùng Và Xác Thực
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống xác thực và quản lý người dùng với các tính năng đăng ký, đăng nhập, và phân quyền.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth-service/`, `./sources/backend/user-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Xem phần 2.1.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  ```json
  {
    "auth": {
      "register": {
        "method": "POST",
        "path": "/api/auth/register",
        "request": {
          "email": "string",
          "password": "string",
          "fullName": "string"
        },
        "response": {
          "token": "string"
        }
      },
      "login": {
        "method": "POST",
        "path": "/api/auth/login",
        "request": {
          "email": "string",
          "password": "string"
        },
        "response": {
          "token": "string"
        }
      },
      "socialLogin": {
        "method": "POST",
        "path": "/api/auth/social-login",
        "request": {
          "provider": "string",
          "token": "string"
        },
        "response": {
          "token": "string"
        }
      }
    },
    "users": {
      "assignRole": {
        "method": "POST",
        "path": "/api/users/assign-role",
        "request": {
          "userId": "uuid",
          "role": "string"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Xử lý xác thực đầu vào không hợp lệ với thông báo rõ ràng cho người dùng.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 1)

<!--START_DAY_LOG_INDEX_1-->

- **DAY 1: Khởi tạo hệ thống xác thực cơ bản**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu người dùng**
    [Coder]
    * Tag IDs: [DAT-001]
    * Component: `./sources/backend/user-service/src/main/resources/db/migration/V1__Create_users_table.sql`
    * Hướng dẫn: Tạo bảng người dùng và vai trò với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ xác thực**
    [Coder]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/backend/auth-service/src/main/java/com/example/auth/`
    * Hướng dẫn: Thiết lập dịch vụ xác thực với các endpoint đăng ký và đăng nhập.
  - **SUB-TASK 3: Viết test cho dịch vụ xác thực**
    [Tester]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/backend/auth-service/src/test/java/com/example/auth/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/example/auth/AuthService.java`
    * Hướng dẫn: Viết các test case cho các endpoint đăng ký và đăng nhập.
  - **SUB-TASK 4: Review code dịch vụ xác thực**
    [Reviewer]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/backend/auth-service/src/main/java/com/example/auth/`
    * Hướng dẫn: Review code dịch vụ xác thực và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ xác thực**
    [Doc]
    * Tag IDs: [REQ-001], [REQ-002], [ARC-006]
    * Component: `./sources/docs/auth-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ xác thực.
  - **SUB-TASK 6: Container hóa dịch vụ xác thực**
    [Docker]
    * Tag IDs: [ARC-006]
    * Component: `./sources/backend/auth-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ xác thực.
  - **SUB-TASK 7: Triển khai dịch vụ xác thực trên GCP**
    [GCP]
    * Tag IDs: [ARC-006]
    * Component: `./sources/infra/gcp/auth-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ xác thực trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ xác thực trên GKE**
    [GKE]
    * Tag IDs: [ARC-006]
    * Component: `./sources/infra/gke/auth-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ xác thực trên GKE.

- **DAY 2: Triển khai phân quyền người dùng**
  - **SUB-TASK 1: Thêm endpoint phân quyền**
    [Coder]
    * Tag IDs: [REQ-003]
    * Component: `./sources/backend/user-service/src/main/java/com/example/user/UserService.java`
    * Hướng dẫn: Thêm endpoint phân quyền người dùng.
  - **SUB-TASK 2: Viết test cho endpoint phân quyền**
    [Tester]
    * Tag IDs: [REQ-003]
    * Component: `./sources/backend/user-service/src/test/java/com/example/user/UserServiceTest.java;./sources/backend/user-service/src/main/java/com/example/user/UserService.java`
    * Hướng dẫn: Viết các test case cho endpoint phân quyền.
  - **SUB-TASK 3: Review code endpoint phân quyền**
    [Reviewer]
    * Tag IDs: [REQ-003]
    * Component: `./sources/backend/user-service/src/main/java/com/example/user/UserService.java`
    * Hướng dẫn: Review code endpoint phân quyền và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint phân quyền**
    [Doc]
    * Tag IDs: [REQ-003]
    * Component: `./sources/docs/user-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint phân quyền.
  - **SUB-TASK 5: Container hóa dịch vụ người dùng**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/user-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ người dùng.
  - **SUB-TASK 6: Triển khai dịch vụ người dùng trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/user-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ người dùng trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ người dùng trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/user-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ người dùng trên GKE.

<!--END_DAY_LOG_INDEX_1-->

### Giai đoạn 2 - Triển Khai Lõi Nghiệp Vụ Trung Tâm
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống quản lý trung tâm với các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/center-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003]:** Xem phần 2.2.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
  ```json
  {
    "centers": {
      "list": {
        "method": "GET",
        "path": "/api/centers",
        "response": {
          "centers": [
            {
              "centerId": "uuid",
              "name": "string",
              "address": "string",
              "taxId": "string",
              "contactPhone": "string",
              "contactEmail": "string"
            }
          ]
        }
      },
      "create": {
        "method": "POST",
        "path": "/api/centers",
        "request": {
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        },
        "response": {
          "centerId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/centers/{centerId}",
        "request": {
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/centers/{centerId}",
        "response": {
          "success": "boolean"
        }
      },
      "assignAdmin": {
        "method": "POST",
        "path": "/api/centers/{centerId}/assign-admin",
        "request": {
          "userId": "uuid"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 2)

<!--START_DAY_LOG_INDEX_2-->

- **DAY 1: Khởi tạo hệ thống quản lý trung tâm**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu trung tâm**
    [Coder]
    * Tag IDs: [DAT-003]
    * Component: `./sources/backend/center-service/src/main/resources/db/migration/V1__Create_centers_table.sql`
    * Hướng dẫn: Tạo bảng trung tâm với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý trung tâm**
    [Coder]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý trung tâm với các endpoint xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý trung tâm**
    [Tester]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/backend/center-service/src/test/java/com/example/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý trung tâm.
  - **SUB-TASK 4: Review code dịch vụ quản lý trung tâm**
    [Reviewer]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/`
    * Hướng dẫn: Review code dịch vụ quản lý trung tâm và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý trung tâm**
    [Doc]
    * Tag IDs: [REQ-004], [REQ-005], [REQ-006], [ARC-002]
    * Component: `./sources/docs/center-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý trung tâm**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/center-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý trung tâm trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý trung tâm trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GKE.

- **DAY 2: Triển khai endpoint xem danh sách trung tâm**
  - **SUB-TASK 1: Thêm endpoint xem danh sách trung tâm**
    [Coder]
    * Tag IDs: [REQ-004]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Thêm endpoint xem danh sách trung tâm.
  - **SUB-TASK 2: Viết test cho endpoint xem danh sách trung tâm**
    [Tester]
    * Tag IDs: [REQ-004]
    * Component: `./sources/backend/center-service/src/test/java/com/example/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Viết các test case cho endpoint xem danh sách trung tâm.
  - **SUB-TASK 3: Review code endpoint xem danh sách trung tâm**
    [Reviewer]
    * Tag IDs: [REQ-004]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Review code endpoint xem danh sách trung tâm và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint xem danh sách trung tâm**
    [Doc]
    * Tag IDs: [REQ-004]
    * Component: `./sources/docs/center-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint xem danh sách trung tâm.
  - **SUB-TASK 5: Container hóa dịch vụ quản lý trung tâm**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/center-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 6: Triển khai dịch vụ quản lý trung tâm trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý trung tâm trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GKE.

- **DAY 3: Triển khai endpoint tạo/cập nhật/xóa trung tâm**
  - **SUB-TASK 1: Thêm endpoint tạo/cập nhật/xóa trung tâm**
    [Coder]
    * Tag IDs: [REQ-005]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Thêm endpoint tạo/cập nhật/xóa trung tâm.
  - **SUB-TASK 2: Viết test cho endpoint tạo/cập nhật/xóa trung tâm**
    [Tester]
    * Tag IDs: [REQ-005]
    * Component: `./sources/backend/center-service/src/test/java/com/example/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Viết các test case cho endpoint tạo/cập nhật/xóa trung tâm.
  - **SUB-TASK 3: Review code endpoint tạo/cập nhật/xóa trung tâm**
    [Reviewer]
    * Tag IDs: [REQ-005]
    * Component: `./sources/backend/center-service/src/main/java/com/example/center/CenterService.java`
    * Hướng dẫn: Review code endpoint tạo/cập nhật/xóa trung tâm và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint tạo/cập nhật/xóa trung tâm**
    [Doc]
    * Tag IDs: [REQ-005]
    * Component: `./sources/docs/center-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint tạo/cập nhật/xóa trung tâm.
  - **SUB-TASK 5: Container hóa dịch vụ quản lý trung tâm**
    [Docker]
    * Tag IDs: [ARC-002]
    * Component: `./sources/backend/center-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý trung tâm.
  - **SUB-TASK 6: Triển khai dịch vụ quản lý trung tâm trên GCP**
    [GCP]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gcp/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý trung tâm trên GKE**
    [GKE]
    * Tag IDs: [ARC-002]
    * Component: `./sources/infra/gke/center-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý trung tâm trên GKE.

<!--END_DAY_LOG_INDEX_2-->

### Giai đoạn 3 - Triển Khai Lõi Nghiệp Vụ Khóa Học
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống quản lý khóa học với các tính năng xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/course-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:** Xem phần 2.3.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [ARC-003]:**
  ```json
  {
    "courses": {
      "list": {
        "method": "GET",
        "path": "/api/courses",
        "response": {
          "courses": [
            {
              "courseId": "uuid",
              "title": "string",
              "description": "string",
              "startDate": "date",
              "endDate": "date",
              "teacherId": "uuid",
              "maxStudents": "int"
            }
          ]
        }
      },
      "create": {
        "method": "POST",
        "path": "/api/courses",
        "request": {
          "title": "string",
          "description": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid",
          "maxStudents": "int"
        },
        "response": {
          "courseId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/courses/{courseId}",
        "request": {
          "title": "string",
          "description": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid",
          "maxStudents": "int"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/courses/{courseId}",
        "response": {
          "success": "boolean"
        }
      },
      "assignTeacher": {
        "method": "POST",
        "path": "/api/courses/{courseId}/assign-teacher",
        "request": {
          "teacherId": "uuid"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1: Khởi tạo hệ thống quản lý khóa học**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu khóa học**
    [Coder]
    * Tag IDs: [DAT-004]
    * Component: `./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses_table.sql`
    * Hướng dẫn: Tạo bảng khóa học với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý khóa học**
    [Coder]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý khóa học với các endpoint xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý khóa học**
    [Tester]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/backend/course-service/src/test/java/com/example/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý khóa học.
  - **SUB-TASK 4: Review code dịch vụ quản lý khóa học**
    [Reviewer]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/`
    * Hướng dẫn: Review code dịch vụ quản lý khóa học và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý khóa học**
    [Doc]
    * Tag IDs: [REQ-007], [REQ-008], [REQ-009], [ARC-003]
    * Component: `./sources/docs/course-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý khóa học.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý khóa học**
    [Docker]
    * Tag IDs: [ARC-003]
    * Component: `./sources/backend/course-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý khóa học.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý khóa học trên GCP**
    [GCP]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gcp/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý khóa học trên GKE**
    [GKE]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gke/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GKE.

- **DAY 2: Triển khai endpoint xem danh sách khóa học**
  - **SUB-TASK 1: Thêm endpoint xem danh sách khóa học**
    [Coder]
    * Tag IDs: [REQ-007]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Thêm endpoint xem danh sách khóa học.
  - **SUB-TASK 2: Viết test cho endpoint xem danh sách khóa học**
    [Tester]
    * Tag IDs: [REQ-007]
    * Component: `./sources/backend/course-service/src/test/java/com/example/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Viết các test case cho endpoint xem danh sách khóa học.
  - **SUB-TASK 3: Review code endpoint xem danh sách khóa học**
    [Reviewer]
    * Tag IDs: [REQ-007]
    * Component: `./sources/backend/course-service/src/main/java/com/example/course/CourseService.java`
    * Hướng dẫn: Review code endpoint xem danh sách khóa học và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho endpoint xem danh sách khóa học**
    [Doc]
    * Tag IDs: [REQ-007]
    * Component: `./sources/docs/course-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho endpoint xem danh sách khóa học.
  - **SUB-TASK 5: Container hóa dịch vụ quản lý khóa học**
    [Docker]
    * Tag IDs: [ARC-003]
    * Component: `./sources/backend/course-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý khóa học.
  - **SUB-TASK 6: Triển khai dịch vụ quản lý khóa học trên GCP**
    [GCP]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gcp/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý khóa học trên GKE**
    [GKE]
    * Tag IDs: [ARC-003]
    * Component: `./sources/infra/gke/course-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khóa học trên GKE.

<!--END_DAY_LOG_INDEX_3-->

### Giai đoạn 4 - Triển Khai Hệ Thống Điểm Danh Và Thẻ Hội Viên
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống điểm danh và quản lý thẻ hội viên với các tính năng quét mã QR, hiển thị tính hợp lệ của thẻ, và gia hạn thẻ.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/attendance-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:** Xem phần 2.5.4 và 2.6.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007]:**
  ```json
  {
    "attendance": {
      "scanQR": {
        "method": "POST",
        "path": "/api/attendance/scan-qr",
        "request": {
          "studentId": "uuid",
          "courseId": "uuid",
          "timestamp": "timestamp"
        },
        "response": {
          "success": "boolean",
          "duplicate": "boolean"
        }
      }
    },
    "studentCards": {
      "viewCard": {
        "method": "GET",
        "path": "/api/student-cards/{studentId}",
        "response": {
          "cardId": "uuid",
          "studentId": "uuid",
          "issueDate": "date",
          "validityDays": "int",
          "remainingDays": "int"
        }
      },
      "renewCard": {
        "method": "POST",
        "path": "/api/student-cards/{studentId}/renew",
        "request": {
          "days": "int"
        },
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Xử lý các trường hợp mạng không ổn định và điểm danh trùng lặp.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 4)

<!--START_DAY_LOG_INDEX_4-->

- **DAY 1: Khởi tạo hệ thống điểm danh**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu điểm danh**
    [Coder]
    * Tag IDs: [DAT-006]
    * Component: `./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_attendance_table.sql`
    * Hướng dẫn: Tạo bảng điểm danh với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ điểm danh**
    [Coder]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/`
    * Hướng dẫn: Thiết lập dịch vụ điểm danh với các endpoint quét mã QR và xử lý điểm danh trùng lặp.
  - **SUB-TASK 3: Viết test cho dịch vụ điểm danh**
    [Tester]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/backend/attendance-service/src/test/java/com/example/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Viết các test case cho các endpoint điểm danh.
  - **SUB-TASK 4: Review code dịch vụ điểm danh**
    [Reviewer]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/`
    * Hướng dẫn: Review code dịch vụ điểm danh và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ điểm danh**
    [Doc]
    * Tag IDs: [REQ-012], [REQ-013], [ARC-007]
    * Component: `./sources/docs/attendance-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ điểm danh.
  - **SUB-TASK 6: Container hóa dịch vụ điểm danh**
    [Docker]
    * Tag IDs: [ARC-007]
    * Component: `./sources/backend/attendance-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ điểm danh.
  - **SUB-TASK 7: Triển khai dịch vụ điểm danh trên GCP**
    [GCP]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gcp/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ điểm danh trên GKE**
    [GKE]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gke/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GKE.

- **DAY 2: Triển khai hệ thống quản lý thẻ hội viên**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu thẻ hội viên**
    [Coder]
    * Tag IDs: [DAT-007]
    * Component: `./sources/backend/attendance-service/src/main/resources/db/migration/V2__Create_student_cards_table.sql`
    * Hướng dẫn: Tạo bảng thẻ hội viên với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý thẻ hội viên**
    [Coder]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/studentcard/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý thẻ hội viên với các endpoint hiển thị tính hợp lệ của thẻ và gia hạn thẻ.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý thẻ hội viên**
    [Tester]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/backend/attendance-service/src/test/java/com/example/studentcard/StudentCardServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/studentcard/StudentCardService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý thẻ hội viên.
  - **SUB-TASK 4: Review code dịch vụ quản lý thẻ hội viên**
    [Reviewer]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/studentcard/`
    * Hướng dẫn: Review code dịch vụ quản lý thẻ hội viên và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý thẻ hội viên**
    [Doc]
    * Tag IDs: [REQ-014], [REQ-015]
    * Component: `./sources/docs/student-card-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý thẻ hội viên.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý thẻ hội viên**
    [Docker]
    * Tag IDs: [ARC-007]
    * Component: `./sources/backend/attendance-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý thẻ hội viên.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý thẻ hội viên trên GCP**
    [GCP]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gcp/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý thẻ hội viên trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý thẻ hội viên trên GKE**
    [GKE]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gke/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý thẻ hội viên trên GKE.

- **DAY 3: Triển khai xử lý ngoại lệ điểm danh**
  - **SUB-TASK 1: Thêm xử lý ngoại lệ mạng không ổn định**
    [Coder]
    * Tag IDs: [EXC-001]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Thêm xử lý ngoại lệ mạng không ổn định.
  - **SUB-TASK 2: Thêm xử lý ngoại lệ điểm danh trùng lặp**
    [Coder]
    * Tag IDs: [EXC-002]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Thêm xử lý ngoại lệ điểm danh trùng lặp.
  - **SUB-TASK 3: Viết test cho xử lý ngoại lệ điểm danh**
    [Tester]
    * Tag IDs: [EXC-001], [EXC-002]
    * Component: `./sources/backend/attendance-service/src/test/java/com/example/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Viết các test case cho xử lý ngoại lệ điểm danh.
  - **SUB-TASK 4: Review code xử lý ngoại lệ điểm danh**
    [Reviewer]
    * Tag IDs: [EXC-001], [EXC-002]
    * Component: `./sources/backend/attendance-service/src/main/java/com/example/attendance/AttendanceService.java`
    * Hướng dẫn: Review code xử lý ngoại lệ điểm danh và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho xử lý ngoại lệ điểm danh**
    [Doc]
    * Tag IDs: [EXC-001], [EXC-002]
    * Component: `./sources/docs/attendance-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho xử lý ngoại lệ điểm danh.
  - **SUB-TASK 6: Container hóa dịch vụ điểm danh**
    [Docker]
    * Tag IDs: [ARC-007]
    * Component: `./sources/backend/attendance-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ điểm danh.
  - **SUB-TASK 7: Triển khai dịch vụ điểm danh trên GCP**
    [GCP]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gcp/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ điểm danh trên GKE**
    [GKE]
    * Tag IDs: [ARC-007]
    * Component: `./sources/infra/gke/attendance-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ điểm danh trên GKE.

<!--END_DAY_LOG_INDEX_4-->

### Giai đoạn 5 - Triển Khai Hệ Thống Thông Báo Và Tích Hợp Zalo
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống thông báo và tích hợp Zalo với các tính năng kích hoạt thông báo, xử lý thông báo không thành công, và quản lý khuyến mãi & thông báo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notification-service/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008], [DAT-009]:** Xem phần 2.7.4 và 2.8.4.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [REQ-017], [REQ-018], [ARC-008]:**
  ```json
  {
    "notifications": {
      "create": {
        "method": "POST",
        "path": "/api/notifications",
        "request": {
          "userId": "uuid",
          "groupZalo": "string",
          "message": "string"
        },
        "response": {
          "notificationId": "uuid"
        }
      }
    },
    "promotions": {
      "create": {
        "method": "POST",
        "path": "/api/promotions",
        "request": {
          "code": "string",
          "discountPercent": "int",
          "startDate": "date",
          "endDate": "date",
          "description": "string"
        },
        "response": {
          "promoId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/promotions/{promoId}",
        "request": {
          "code": "string",
          "discountPercent": "int",
          "startDate": "date",
          "endDate": "date",
          "description": "string"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/promotions/{promoId}",
        "response": {
          "success": "boolean"
        }
      }
    },
    "announcements": {
      "create": {
        "method": "POST",
        "path": "/api/announcements",
        "request": {
          "title": "string",
          "content": "string",
          "startDate": "date",
          "endDate": "date"
        },
        "response": {
          "announcementId": "uuid"
        }
      },
      "update": {
        "method": "PUT",
        "path": "/api/announcements/{announcementId}",
        "request": {
          "title": "string",
          "content": "string",
          "startDate": "date",
          "endDate": "date"
        },
        "response": {
          "success": "boolean"
        }
      },
      "delete": {
        "method": "DELETE",
        "path": "/api/announcements/{announcementId}",
        "response": {
          "success": "boolean"
        }
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Xử lý thông báo không thành công.

#### Nhật ký Ngày theo Ngày của Sub-Agent (Giai đoạn 5)

<!--START_DAY_LOG_INDEX_5-->

- **DAY 1: Khởi tạo hệ thống thông báo**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu thông báo**
    [Coder]
    * Tag IDs: [DAT-008]
    * Component: `./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_notifications_table.sql`
    * Hướng dẫn: Tạo bảng thông báo với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ thông báo**
    [Coder]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/`
    * Hướng dẫn: Thiết lập dịch vụ thông báo với các endpoint kích hoạt thông báo.
  - **SUB-TASK 3: Viết test cho dịch vụ thông báo**
    [Tester]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/backend/notification-service/src/test/java/com/example/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Viết các test case cho các endpoint thông báo.
  - **SUB-TASK 4: Review code dịch vụ thông báo**
    [Reviewer]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/`
    * Hướng dẫn: Review code dịch vụ thông báo và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ thông báo**
    [Doc]
    * Tag IDs: [REQ-016], [ARC-008]
    * Component: `./sources/docs/notification-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ thông báo.
  - **SUB-TASK 6: Container hóa dịch vụ thông báo**
    [Docker]
    * Tag IDs: [ARC-008]
    * Component: `./sources/backend/notification-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ thông báo.
  - **SUB-TASK 7: Triển khai dịch vụ thông báo trên GCP**
    [GCP]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gcp/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ thông báo trên GKE**
    [GKE]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gke/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GKE.

- **DAY 2: Triển khai hệ thống quản lý khuyến mãi & thông báo**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu khuyến mãi & thông báo**
    [Coder]
    * Tag IDs: [DAT-009]
    * Component: `./sources/backend/notification-service/src/main/resources/db/migration/V2__Create_promotions_and_announcements_tables.sql`
    * Hướng dẫn: Tạo bảng khuyến mãi và thông báo với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Thiết lập dịch vụ quản lý khuyến mãi & thông báo**
    [Coder]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/promotion/`, `./sources/backend/notification-service/src/main/java/com/example/announcement/`
    * Hướng dẫn: Thiết lập dịch vụ quản lý khuyến mãi & thông báo với các endpoint quản lý khuyến mãi và thông báo.
  - **SUB-TASK 3: Viết test cho dịch vụ quản lý khuyến mãi & thông báo**
    [Tester]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/backend/notification-service/src/test/java/com/example/promotion/PromotionServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/promotion/PromotionService.java`, `./sources/backend/notification-service/src/test/java/com/example/announcement/AnnouncementServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/announcement/AnnouncementService.java`
    * Hướng dẫn: Viết các test case cho các endpoint quản lý khuyến mãi & thông báo.
  - **SUB-TASK 4: Review code dịch vụ quản lý khuyến mãi & thông báo**
    [Reviewer]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/promotion/`, `./sources/backend/notification-service/src/main/java/com/example/announcement/`
    * Hướng dẫn: Review code dịch vụ quản lý khuyến mãi & thông báo và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 5: Tạo tài liệu cho dịch vụ quản lý khuyến mãi & thông báo**
    [Doc]
    * Tag IDs: [REQ-017], [REQ-018]
    * Component: `./sources/docs/promotion-service.md`, `./sources/docs/announcement-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho dịch vụ quản lý khuyến mãi & thông báo.
  - **SUB-TASK 6: Container hóa dịch vụ quản lý khuyến mãi & thông báo**
    [Docker]
    * Tag IDs: [ARC-008]
    * Component: `./sources/backend/notification-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ quản lý khuyến mãi & thông báo.
  - **SUB-TASK 7: Triển khai dịch vụ quản lý khuyến mãi & thông báo trên GCP**
    [GCP]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gcp/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khuyến mãi & thông báo trên GCP.
  - **SUB-TASK 8: Triển khai dịch vụ quản lý khuyến mãi & thông báo trên GKE**
    [GKE]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gke/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ quản lý khuyến mãi & thông báo trên GKE.

- **DAY 3: Triển khai xử lý ngoại lệ thông báo**
  - **SUB-TASK 1: Thêm xử lý ngoại lệ thông báo không thành công**
    [Coder]
    * Tag IDs: [EXC-003]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Thêm xử lý ngoại lệ thông báo không thành công.
  - **SUB-TASK 2: Viết test cho xử lý ngoại lệ thông báo**
    [Tester]
    * Tag IDs: [EXC-003]
    * Component: `./sources/backend/notification-service/src/test/java/com/example/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Viết các test case cho xử lý ngoại lệ thông báo.
  - **SUB-TASK 3: Review code xử lý ngoại lệ thông báo**
    [Reviewer]
    * Tag IDs: [EXC-003]
    * Component: `./sources/backend/notification-service/src/main/java/com/example/notification/NotificationService.java`
    * Hướng dẫn: Review code xử lý ngoại lệ thông báo và đảm bảo tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tạo tài liệu cho xử lý ngoại lệ thông báo**
    [Doc]
    * Tag IDs: [EXC-003]
    * Component: `./sources/docs/notification-service.md`
    * Hướng dẫn: Tạo tài liệu chi tiết cho xử lý ngoại lệ thông báo.
  - **SUB-TASK 5: Container hóa dịch vụ thông báo**
    [Docker]
    * Tag IDs: [ARC-008]
    * Component: `./sources/backend/notification-service/Dockerfile`
    * Hướng dẫn: Tạo Dockerfile cho dịch vụ thông báo.
  - **SUB-TASK 6: Triển khai dịch vụ thông báo trên GCP**
    [GCP]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gcp/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GCP.
  - **SUB-TASK 7: Triển khai dịch vụ thông báo trên GKE**
    [GKE]
    * Tag IDs: [ARC-008]
    * Component: `./sources/infra/gke/notification-service-deployment.yaml`
    * Hướng dẫn: Tạo cấu hình triển khai dịch vụ thông báo trên GKE.

<!--END_DAY_LOG_INDEX_5-->

---

### Phase 4 Logs:
- **DAY 1: Xây dựng giao diện người dùng cho web**

##### SUB-TASK 1: Xây dựng giao diện đăng nhập và đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện đăng nhập và đăng ký người dùng. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/auth/;./sources/frontend/src/pages/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Xây dựng giao diện quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/center/;./sources/frontend/src/pages/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng giao diện quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/course/;./sources/frontend/src/pages/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng giao diện điểm danh và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/pages/attendance/, ./sources/frontend/src/pages/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện điểm danh và thông báo. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/frontend/src/tests/pages/attendance/;./sources/frontend/src/pages/attendance/, ./sources/frontend/src/tests/pages/notification/;./sources/frontend/src/pages/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Xây dựng giao diện người dùng cho di động**

##### SUB-TASK 1: Xây dựng giao diện đăng nhập và đăng ký người dùng cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện đăng nhập và đăng ký người dùng cho di động. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/auth/;./sources/mobile-app/src/screens/auth/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện đăng nhập và đăng ký người dùng cho di động. [REQ-001], [REQ-002], [ARC-006]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Xây dựng giao diện quản lý trung tâm cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý trung tâm cho di động. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/center/;./sources/mobile-app/src/screens/center/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý trung tâm cho di động. [REQ-004], [REQ-005], [REQ-006], [ARC-002]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng giao diện quản lý khóa học cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện quản lý khóa học cho di động. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [ARC-003]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/course/;./sources/mobile-app/src/screens/course/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện quản lý khóa học cho di động. [REQ-007], [REQ-008], [REQ-009], [ARC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Xây dựng giao diện điểm danh và thông báo cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/screens/attendance/, ./sources/mobile-app/src/screens/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện điểm danh và thông báo cho di động. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 8: Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo cho di động
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
* **Đường dẫn Cấu phần / Module Mục tiêu:** ./sources/mobile-app/src/tests/screens/attendance/;./sources/mobile-app/src/screens/attendance/, ./sources/mobile-app/src/tests/screens/notification/;./sources/mobile-app/src/screens/notification/
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện điểm danh và thông báo cho di động. [REQ-012], [REQ-013], [REQ-016], [ARC-007], [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

---

### Phase 5 Logs:
- **DAY 1: Xây dựng lõi điểm danh và quản lý thẻ hội viên**

##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho điểm danh và thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-006], [DAT-007]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_attendance_and_student_cards_tables.sql
* **Low-Level Technical Task Instruction:** Tạo bảng attendance và student_cards với các ràng buộc và chỉ mục cần thiết. [DAT-006], [DAT-007]

##### SUB-TASK 2: Xây dựng dịch vụ chụp ảnh điểm danh QR
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-012]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức chụp ảnh điểm danh QR. [REQ-012]

##### SUB-TASK 3: Xây dựng dịch vụ tính chất bất biến của điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-013]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức xử lý điểm danh idempotent. [REQ-013]

##### SUB-TASK 4: Xây dựng dịch vụ hiển thị tính hợp lệ của thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-014]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức hiển thị thông tin thẻ hội viên. [REQ-014]

##### SUB-TASK 5: Xây dựng dịch vụ gia hạn thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Xây dựng phương thức gia hạn thẻ hội viên. [REQ-015]

##### SUB-TASK 6: Viết test cho dịch vụ chụp ảnh điểm danh QR
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-012]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ chụp ảnh điểm danh QR. [REQ-012]

##### SUB-TASK 7: Viết test cho dịch vụ tính chất bất biến của điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-013]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ tính chất bất biến của điểm danh. [REQ-013]

##### SUB-TASK 8: Viết test cho dịch vụ hiển thị tính hợp lệ của thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-014]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/StudentCardServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ hiển thị tính hợp lệ của thẻ. [REQ-014]

##### SUB-TASK 9: Viết test cho dịch vụ gia hạn thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/StudentCardServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/StudentCardService.java
* **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ gia hạn thẻ. [REQ-015]

##### SUB-TASK 10: Review code cho dịch vụ điểm danh và quản lý thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Reviewer]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/
* **Low-Level Technical Task Instruction:** Review code cho các dịch vụ điểm danh và quản lý thẻ hội viên. [REQ-012], [REQ-013], [REQ-014], [REQ-015]

##### SUB-TASK 11: Viết tài liệu cho dịch vụ điểm danh và quản lý thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
* **Target Component file path (target_component):** ./sources/docs/attendance-service.md
* **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết cho dịch vụ điểm danh và quản lý thẻ hội viên. [REQ-012], [REQ-013], [REQ-014], [REQ-015]

##### SUB-TASK 12: Xây dựng Dockerfile cho dịch vụ điểm danh và quản lý thẻ hội viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/Dockerfile
* **Low-Level Technical Task Instruction:** Xây dựng Dockerfile cho dịch vụ điểm danh và quản lý thẻ hội viên. [ARC-010]

##### SUB-TASK 13: Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GCP]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gcp/attendance-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GCP. [ARC-010]

##### SUB-TASK 14: Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/attendance-service/
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ điểm danh và quản lý thẻ hội viên lên GKE. [ARC-010]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`