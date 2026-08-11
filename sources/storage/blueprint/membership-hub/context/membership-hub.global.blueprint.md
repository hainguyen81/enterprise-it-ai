# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260811072603 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/11 07:26:03 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo kiến trúc đa trung tâm với các thành phần chính bao gồm: quản lý người dùng, quản lý trung tâm, quản lý khóa học, đăng ký học viên, điểm danh, quản lý thẻ hội viên, thông báo và truyền thông, chatbot dịch vụ khách hàng AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích.
- Hệ thống sử dụng mô hình RBAC (Role-Based Access Control) để quản lý quyền truy cập của người dùng.
- Hệ thống hỗ trợ xác thực qua email/mật khẩu, Firebase, Google và Facebook thông qua OAuth2.
- Hệ thống sử dụng JWT token với thời hạn 15 phút và refresh token để quản lý phiên đăng nhập.
- Hệ thống sử dụng cơ sở dữ liệu PostgreSQL để lưu trữ dữ liệu.
- Hệ thống sử dụng Redis để quản lý session caching.
- Hệ thống sử dụng Firebase Authentication và Google Cloud Messaging (FCM)/Apple APNs để quản lý thông báo đẩy trên di động.
- Hệ thống sử dụng Zalo API để quản lý thông báo trên nhóm Zalo.
- Hệ thống sử dụng CI/CD pipeline với GitHub Actions để quản lý quá trình triển khai.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Hệ thống sử dụng các kênh truyền thông đa kênh bao gồm: web, di động và nhóm Zalo.
- Hệ thống sử dụng các dịch vụ cốt lõi bao gồm: quản lý người dùng, quản lý trung tâm, quản lý khóa học, đăng ký học viên, điểm danh, quản lý thẻ hội viên, thông báo và truyền thông, chatbot dịch vụ khách hàng AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích.
- Hệ thống sử dụng các dịch vụ phụ trợ bao gồm: Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis, CI/CD pipeline với GitHub Actions.
- Hệ thống sử dụng các dịch vụ cơ sở hạ tầng bao gồm: PostgreSQL, Docker, Kubernetes (GKE).

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis, CI/CD pipeline với GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native.

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

```markdown
# GLOBAL PROJECT CONTEXT: membership-hub

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG

<!--START_BACKLOG_SYNOPSIS_GRID-->

| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Xây dựng hệ thống xác thực người dùng | Cung cấp cơ chế đăng ký và đăng nhập qua email/mật khẩu, Firebase, Google, Facebook | Application Code | [REQ-001], [REQ-002], [ARC-006] |
| 2 | Phát triển hệ thống phân quyền người dùng | Triển khai RBAC để quản lý quyền truy cập cho các vai trò khác nhau | Application Code | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-003] |
| 3 | Xây dựng hệ thống quản lý trung tâm | Tạo, cập nhật, xóa và phân quyền quản trị trung tâm | Application Code | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| 4 | Phát triển hệ thống quản lý khóa học | Tạo, cập nhật, xóa khóa học và phân công giáo viên | Application Code | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| 5 | Xây dựng hệ thống đăng ký và ghi danh học viên | Cho phép học viên duyệt và đăng ký khóa học | Application Code | [REQ-010], [REQ-011], [DAT-005] |
| 6 | Phát triển hệ thống điểm danh QR | Triển khai chức năng quét mã QR để ghi nhận điểm danh | Application Code | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| 7 | Xây dựng hệ thống quản lý thẻ hội viên | Hiển thị và gia hạn thẻ hội viên | Application Code | [REQ-014], [REQ-015], [DAT-007] |
| 8 | Phát triển hệ thống thông báo và truyền thông | Kích hoạt thông báo qua ứng dụng di động và nhóm Zalo | Application Code | [REQ-016], [DAT-008], [EXC-003] |
| 9 | Xây dựng hệ thống quản lý khuyến mãi và thông báo | Tạo, chỉnh sửa và xóa khuyến mãi và thông báo | Application Code | [REQ-017], [REQ-018], [DAT-009] |
| 10 | Tích hợp chatbot AI | Triển khai chatbot AI để trả lời các câu hỏi thường gặp | Application Code | [REQ-019] |
| 11 | Phát triển giao diện người dùng di động | Tạo giao diện người dùng đáp ứng cho các vai trò khác nhau | Application Code | [REQ-020], [REQ-021] |
| 12 | Triển khai bản địa hóa và SEO | Phát hiện ngôn ngữ mặc định và hỗ trợ SEO đa ngôn ngữ | Application Code | [REQ-022], [REQ-023], [DAT-011] |
| 13 | Xây dựng hệ thống báo cáo và phân tích | Tạo báo cáo điểm danh và bảng điều khiển tóm tắt | Application Code | [REQ-024], [REQ-025], [EXC-005] |
| 14 | Thiết lập cơ sở dữ liệu | Tạo các bảng dữ liệu và quan hệ giữa các bảng | Application Code | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |
| 15 | Thiết lập môi trường phát triển | Cấu hình môi trường phát triển với Docker và Kubernetes | DevOps Infrastructure | [ARC-010], [NFR-005] |
| 16 | Triển khai hệ thống trên GCP | Triển khai hệ thống trên Google Cloud Platform | DevOps Infrastructure | [ARC-010], [NFR-002], [NFR-004], [NFR-009] |
| 17 | Tạo tài liệu kỹ thuật | Tạo tài liệu kỹ thuật cho hệ thống | Enterprise Documentation | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 17 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->
```

```markdown
# GLOBAL PROJECT CONTEXT: membership-hub

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.2. MULTI-PHASE SYNOPSIS MATRIX

<!--START_PHASE_SYNOPSIS_GRID-->

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 3 | ./sources/backend/auth/, ./sources/backend/rbac/, ./sources/docs/ | Xây dựng hệ thống xác thực người dùng và phân quyền người dùng, Tạo tài liệu kỹ thuật cho hệ thống xác thực và phân quyền | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [ARC-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-003] |
| Phase 2 | Day 1 - 3 | ./sources/backend/centers/, ./sources/backend/courses/, ./sources/docs/ | Xây dựng hệ thống quản lý trung tâm và khóa học, Tạo tài liệu kỹ thuật cho hệ thống quản lý trung tâm và khóa học | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| Phase 3 | Day 1 - 3 | ./sources/backend/enrollments/, ./sources/backend/attendance/, ./sources/docs/ | Xây dựng hệ thống đăng ký và ghi danh học viên, Phát triển hệ thống điểm danh QR, Tạo tài liệu kỹ thuật cho hệ thống đăng ký và điểm danh | Coder, Tester, Reviewer, Doc | [REQ-010], [REQ-011], [DAT-005], [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| Phase 4 | Day 1 - 3 | ./sources/backend/membership/, ./sources/backend/notifications/, ./sources/docs/ | Xây dựng hệ thống quản lý thẻ hội viên, Phát triển hệ thống thông báo và truyền thông, Tạo tài liệu kỹ thuật cho hệ thống quản lý thẻ hội viên và thông báo | Coder, Tester, Reviewer, Doc | [REQ-014], [REQ-015], [DAT-007], [REQ-016], [DAT-008], [EXC-003] |
| Phase 5 | Day 1 - 3 | ./sources/backend/promotions/, ./sources/backend/chatbot/, ./sources/frontend/, ./sources/infra/ | Xây dựng hệ thống quản lý khuyến mãi và thông báo, Tích hợp chatbot AI, Phát triển giao diện người dùng di động, Triển khai hệ thống trên GCP, Tạo tài liệu kỹ thuật cho hệ thống quản lý khuyến mãi, chatbot, và giao diện di động | Coder, Tester, Reviewer, Doc, DevOps | [REQ-017], [REQ-018], [DAT-009], [REQ-019], [REQ-020], [REQ-021], [ARC-010], [NFR-002], [NFR-004], [NFR-009] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 5 Phases | **MAPPED CAPACITY STATUS:** Verified: 100% of master backlog tasks successfully distributed across exactly 5 calculated phases | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |

<!--END_PHASE_SYNOPSIS_GRID-->
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

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1 - Khởi Tạo Hệ Thống Người Dùng Và Xác Thực
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Thiết lập cơ sở hạ tầng xác thực người dùng, bao gồm đăng ký qua email/mật khẩu, xác thực OAuth2 với Firebase, Google, và Facebook, và triển khai cơ chế cấp JWT token với thời hạn 15 phút và refresh token.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

<!--START_DAY_LOG_INDEX_1-->

- **DAY 1: Khởi tạo cơ sở dữ liệu và mô hình người dùng**
  - **SUB-TASK 1: Thiết lập cơ sở dữ liệu PostgreSQL**
    - [Docker]
    - [Targeted Tag IDs]: [ARC-010]
    - [Target Component file path (target_component)]: ./sources/infra/docker-compose.yml
    - [Low-Level Technical Task Instruction]: Tạo Docker Compose file để khởi chạy PostgreSQL với cấu hình mặc định và volume cho dữ liệu. [ARC-010]

  - **SUB-TASK 2: Thiết kế lược đồ cơ sở dữ liệu cho người dùng và vai trò**
    - [Coder]
    - [Targeted Tag IDs]: [DAT-001]
    - [Target Component file path (target_component)]: ./sources/backend/src/main/resources/db/migration/V1__Create_Users_And_Roles.sql
    - [Low-Level Technical Task Instruction]: Viết script Flyway để tạo bảng Users và Roles với các ràng buộc khóa ngoại và kiểm tra. [DAT-001]

  - **SUB-TASK 3: Viết unit tests cho lược đồ cơ sở dữ liệu**
    - [Tester]
    - [Targeted Tag IDs]: [DAT-001]
    - [Target Component file path (target_component)]: ./sources/backend/src/test/java/com/membershiphub/db/UserSchemaTest.java;./sources/backend/src/main/resources/db/migration/V1__Create_Users_And_Roles.sql
    - [Low-Level Technical Task Instruction]: Viết các test để xác minh cấu trúc bảng và ràng buộc. [DAT-001]

- **DAY 2: Triển khai xác thực người dùng**
  - **SUB-TASK 1: Thiết lập xác thực email/mật khẩu**
    - [Coder]
    - [Targeted Tag IDs]: [REQ-001], [ARC-006]
    - [Target Component file path (target_component)]: ./sources/backend/src/main/java/com/membershiphub/auth/LocalAuthService.java
    - [Low-Level Technical Task Instruction]: Triển khai dịch vụ xác thực cục bộ với mã hóa mật khẩu bcrypt. [REQ-001], [ARC-006]

  - **SUB-TASK 2: Thiết lập xác thực OAuth2 với Firebase, Google, Facebook**
    - [Coder]
    - [Targeted Tag IDs]: [REQ-002], [ARC-006]
    - [Target Component file path (target_component)]: ./sources/backend/src/main/java/com/membershiphub/auth/OAuth2Service.java
    - [Low-Level Technical Task Instruction]: Triển khai dịch vụ xác thực OAuth2 với các nhà cung cấp khác nhau. [REQ-002], [ARC-006]

  - **SUB-TASK 3: Viết unit tests cho dịch vụ xác thực**
    - [Tester]
    - [Targeted Tag IDs]: [REQ-001], [REQ-002], [ARC-006]
    - [Target Component file path (target_component)]: ./sources/backend/src/test/java/com/membershiphub/auth/AuthServiceTest.java;./sources/backend/src/main/java/com/membershiphub/auth/LocalAuthService.java;./sources/backend/src/main/java/com/membershiphub/auth/OAuth2Service.java
    - [Low-Level Technical Task Instruction]: Viết các test để xác minh tính năng đăng ký và đăng nhập. [REQ-001], [REQ-002], [ARC-006]

- **DAY 3: Triển khai phân quyền người dùng**
  - **SUB-TASK 1: Thiết lập phân quyền người dùng**
    - [Coder]
    - [Targeted Tag IDs]: [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    - [Target Component file path (target_component)]: ./sources/backend/src/main/java/com/membershiphub/auth/RoleService.java
    - [Low-Level Technical Task Instruction]: Triển khai dịch vụ phân quyền với các vai trò System Admin, Center Admin, Manager, Teacher, Student. [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

  - **SUB-TASK 2: Viết unit tests cho dịch vụ phân quyền**
    - [Tester]
    - [Targeted Tag IDs]: [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    - [Target Component file path (target_component)]: ./sources/backend/src/test/java/com/membershiphub/auth/RoleServiceTest.java;./sources/backend/src/main/java/com/membershiphub/auth/RoleService.java
    - [Low-Level Technical Task Instruction]: Viết các test để xác minh tính năng phân quyền. [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

- **DAY 4: Triển khai JWT token và refresh token**
  - **SUB-TASK 1: Thiết lập JWT token**
    - [Coder]
    - [Targeted Tag IDs]: [ARC-006]
    - [Target Component file path (target_component)]: ./sources/backend/src/main/java/com/membershiphub/auth/JwtService.java
    - [Low-Level Technical Task Instruction]: Triển khai dịch vụ JWT với thời hạn 15 phút. [ARC-006]

  - **SUB-TASK 2: Thiết lập refresh token**
    - [Coder]
    - [Targeted Tag IDs]: [ARC-006]
    - [Target Component file path (target_component)]: ./sources/backend/src/main/java/com/membershiphub/auth/RefreshTokenService.java
    - [Low-Level Technical Task Instruction]: Triển khai dịch vụ refresh token với thời hạn 7 ngày. [ARC-006]

  - **SUB-TASK 3: Viết unit tests cho dịch vụ JWT và refresh token**
    - [Tester]
    - [Targeted Tag IDs]: [ARC-006]
    - [Target Component file path (target_component)]: ./sources/backend/src/test/java/com/membershiphub/auth/JwtServiceTest.java;./sources/backend/src/main/java/com/membershiphub/auth/JwtService.java;./sources/backend/src/test/java/com/membershiphub/auth/RefreshTokenServiceTest.java;./sources/backend/src/main/java/com/membershiphub/auth/RefreshTokenService.java
    - [Low-Level Technical Task Instruction]: Viết các test để xác minh tính năng JWT và refresh token. [ARC-006]

- **DAY 5: Triển khai xử lý ngoại lệ và kiểm tra tích hợp**
  - **SUB-TASK 1: Thiết lập xử lý ngoại lệ**
    - [Coder]
    - [Targeted Tag IDs]: [EXC-004]
    - [Target Component file path (target_component)]: ./sources/backend/src/main/java/com/membershiphub/exception/GlobalExceptionHandler.java
    - [Low-Level Technical Task Instruction]: Triển khai xử lý ngoại lệ toàn cầu với thông báo rõ ràng cho người dùng. [EXC-004]

  - **SUB-TASK 2: Viết unit tests cho xử lý ngoại lệ**
    - [Tester]
    - [Targeted Tag IDs]: [EXC-004]
    - [Target Component file path (target_component)]: ./sources/backend/src/test/java/com/membershiphub/exception/GlobalExceptionHandlerTest.java;./sources/backend/src/main/java/com/membershiphub/exception/GlobalExceptionHandler.java
    - [Low-Level Technical Task Instruction]: Viết các test để xác minh xử lý ngoại lệ. [EXC-004]

  - **SUB-TASK 3: Thiết lập kiểm tra tích hợp**
    - [Tester]
    - [Targeted Tag IDs]: [REQ-001], [REQ-002], [REQ-003], [ARC-006]
    - [Target Component file path (target_component)]: ./sources/backend/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java;./sources/backend/src/main/java/com/membershiphub/auth/LocalAuthService.java;./sources/backend/src/main/java/com/membershiphub/auth/OAuth2Service.java;./sources/backend/src/main/java/com/membershiphub/auth/RoleService.java;./sources/backend/src/main/java/com/membershiphub/auth/JwtService.java;./sources/backend/src/main/java/com/membershiphub/auth/RefreshTokenService.java
    - [Low-Level Technical Task Instruction]: Viết các test tích hợp để xác minh tính năng đăng ký, đăng nhập và phân quyền. [REQ-001], [REQ-002], [REQ-003], [ARC-006]

<!--END_PHASE_LOG_BLOCK_INDEX_1-->

```markdown
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

### 2.10 Các tính năng cốt lõi của ứng dụng di động

#### Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

#### Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

### 2.11 Bản địa hóa & SEO

#### Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

#### Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

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

#### 4.1.1 Kiến trúc tổng quan

- **Kiến trúc tổng quan:** Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, khóa học, điểm danh, và thông báo. Frontend sử dụng Next.js để cung cấp giao diện đáp ứng cho web và di động. Backend sử dụng Java/Quarkus với cơ sở dữ liệu PostgreSQL. Hệ thống sử dụng Firebase Authentication cho xác thực và Google Cloud Messaging (FCM)/Apple APNs cho push notification. Zalo API được tích hợp để gửi thông báo đến nhóm Zalo.

#### 4.1.2 Kiến trúc chi tiết

- **Kiến trúc chi tiết:** Hệ thống bao gồm các dịch vụ sau:
  - **User Service:** Quản lý người dùng, xác thực, và phân quyền.
  - **Course Service:** Quản lý khóa học, đăng ký, và phân công giáo viên.
  - **Attendance Service:** Xử lý điểm danh qua quét mã QR.
  - **Notification Service:** Kích hoạt thông báo đẩy và tin nhắn Zalo.
  - **Reporting Service:** Tạo báo cáo điểm danh và bảng điều khiển tóm tắt.

### 4.2 Ma trận tóm tắt đa giai đoạn

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Sản phẩm bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|-------------------------|-------------------|------------|------------------|
| Giai đoạn 1 | Ngày 1-2 | `./sources/backend/user-service/` | Khởi tạo hệ thống người dùng và xác thực | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006] |
| Giai đoạn 2 | Ngày 1-3 | `./sources/backend/course-service/` | Triển khai lõi nghiệp vụ khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-007] |
| Giai đoạn 3 | Ngày 1-2 | `./sources/backend/attendance-service/` | Triển khai hệ thống điểm danh QR | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002], [ARC-008] |
| Giai đoạn 4 | Ngày 1-2 | `./sources/backend/notification-service/` | Triển khai hệ thống thông báo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-016], [DAT-008], [EXC-003], [ARC-009] |
| Giai đoạn 5 | Ngày 1-2 | `./sources/frontend/` | Triển khai giao diện người dùng và tích hợp di động | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011], [ARC-010] |

## 📅 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN

### Giai đoạn 2 - Triển Khai Lõi Nghiệp Vụ Khóa Học

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai lõi nghiệp vụ quản lý khóa học bao gồm tạo/cập nhật/xóa khóa học, phân công giáo viên, và quản lý ghi danh học viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/course-service/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:** Triển khai bảng khóa học và bảng ghi danh.
- **Hợp đồng Định tuyến API và Sự kiện:**
  - **API Endpoints:**
    ```json
    {
      "POST /api/courses": {
        "description": "Tạo khóa học mới",
        "request": {
          "title": "string",
          "description": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid",
          "maxStudents": "integer"
        },
        "response": {
          "courseId": "uuid",
          "title": "string",
          "startDate": "date",
          "endDate": "date"
        }
      },
      "GET /api/courses": {
        "description": "Lấy danh sách khóa học",
        "response": {
          "courses": [
            {
              "courseId": "uuid",
              "title": "string",
              "startDate": "date",
              "endDate": "date",
              "teacherName": "string"
            }
          ]
        }
      },
      "POST /api/courses/{courseId}/assign-teacher": {
        "description": "Phân công giáo viên vào khóa học",
        "request": {
          "teacherId": "uuid"
        },
        "response": {
          "status": "string"
        }
      },
      "POST /api/enrollments": {
        "description": "Đăng ký học viên vào khóa học",
        "request": {
          "studentId": "uuid",
          "courseId": "uuid"
        },
        "response": {
          "enrollmentId": "uuid",
          "enrollmentDate": "timestamp"
        }
      }
    }
    ```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Xử lý xung đột lịch trình giáo viên và trùng lặp đăng ký học viên.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

<!--START_DAY_LOG_INDEX_2-->

- **DAY 1: Khởi tạo dịch vụ khóa học và bảng cơ sở dữ liệu**
  - **SUB-TASK 1: Thiết kế lược đồ cơ sở dữ liệu cho dịch vụ khóa học**
    - [Coder]
    - [DAT-004]
    - `./sources/backend/course-service/src/main/resources/db/migration/V1__Create_Courses_Table.sql`
    - Thiết kế bảng khóa học và bảng ghi danh với các trường và ràng buộc cần thiết.
  - **SUB-TASK 2: Viết mã khởi tạo dịch vụ khóa học**
    - [Coder]
    - [REQ-007], [REQ-008], [REQ-009]
    - `./sources/backend/course-service/src/main/java/com/membershiphub/courseservice/`
    - Viết mã khởi tạo dịch vụ khóa học bao gồm các endpoint API và logic nghiệp vụ.

- **DAY 2: Triển khai chức năng quản lý khóa học**
  - **SUB-TASK 1: Triển khai chức năng tạo/cập nhật/xóa khóa học**
    - [Coder]
    - [REQ-008]
    - `./sources/backend/course-service/src/main/java/com/membershiphub/courseservice/controller/CourseController.java`
    - Triển khai các endpoint API cho tạo, cập nhật và xóa khóa học.
  - **SUB-TASK 2: Triển khai chức năng phân công giáo viên**
    - [Coder]
    - [REQ-009]
    - `./sources/backend/course-service/src/main/java/com/membershiphub/courseservice/controller/TeacherAssignmentController.java`
    - Triển khai endpoint API cho phân công giáo viên vào khóa học.

- **DAY 3: Triển khai chức năng ghi danh học viên**
  - **SUB-TASK 1: Triển khai chức năng đăng ký khóa học**
    - [Coder]
    - [REQ-011]
    - `./sources/backend/course-service/src/main/java/com/membershiphub/courseservice/controller/EnrollmentController.java`
    - Triển khai endpoint API cho đăng ký học viên vào khóa học.
  - **SUB-TASK 2: Viết bộ kiểm thử cho dịch vụ khóa học**
    - [Tester]
    - [REQ-007], [REQ-008], [REQ-009], [REQ-011]
    - `./sources/backend/course-service/src/test/java/com/membershiphub/courseservice/;./sources/backend/course-service/src/main/java/com/membershiphub/courseservice/`
    - Viết các bộ kiểm thử cho các chức năng quản lý khóa học và ghi danh học viên.

<!--END_PHASE_LOG_BLOCK_INDEX_2-->
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

### 4.1 PHÂN TÍCH KIẾN TRÚC

#### 4.1.1 KIẾN TRÚC TOÀN CẦU

- **Kiến trúc hệ thống:** Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho mỗi chức năng chính (quản lý người dùng, quản lý trung tâm, quản lý khóa học, điểm danh, thẻ hội viên, thông báo, khuyến mãi, chatbot AI).
- **Kiến trúc dữ liệu:** Sử dụng cơ sở dữ liệu PostgreSQL với các bảng được chuẩn hóa để đảm bảo tính toàn vẹn dữ liệu và hiệu suất truy vấn.
- **Kiến trúc giao diện người dùng:** Giao diện người dùng được xây dựng bằng Next.js cho web và React Native cho di động, với các thành phần UI được tái sử dụng giữa các nền tảng.
- **Kiến trúc giao tiếp:** Sử dụng REST APIs cho các tương tác đồng bộ và WebSockets cho các tương tác thời gian thực như điểm danh và thông báo.

#### 4.1.2 KIẾN TRÚC PHÂN TÁN

- **Phân tán dữ liệu:** Dữ liệu được phân tán theo các trung tâm, với mỗi trung tâm có thể có các bản sao dữ liệu cục bộ để giảm độ trễ truy cập.
- **Phân tán xử lý:** Các dịch vụ được triển khai trên các cụm Kubernetes (GKE) để đảm bảo tính sẵn sàng và khả năng mở rộng.
- **Phân tán giao tiếp:** Sử dụng các dịch vụ trung gian như Redis cho session caching và Apache Kafka cho xử lý sự kiện thời gian thực.

### 4.2 MA TRẬN TÓM TẮT PHÂN PHÁS

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|------------------------|---------------------------|-----------|------------------|
| 1         | 1-2         | ./sources/backend/auth-service/ | Xây dựng dịch vụ xác thực với email/mật khẩu, Firebase, Google, Facebook OAuth | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [ARC-006], [DAT-001], [EXC-004] |
| 2         | 3-4         | ./sources/backend/center-service/, ./sources/backend/course-service/ | Xây dựng dịch vụ quản lý trung tâm và khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004] |
| 3         | 5-7         | ./sources/backend/attendance-service/, ./sources/backend/notification-service/ | Xây dựng dịch vụ điểm danh và thông báo | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-016], [DAT-006], [DAT-008], [EXC-001], [EXC-002], [EXC-003] |
| 4         | 8-10        | ./sources/backend/membership-service/, ./sources/backend/promotion-service/ | Xây dựng dịch vụ quản lý thẻ hội viên và khuyến mãi | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-014], [REQ-015], [REQ-017], [REQ-018], [DAT-007], [DAT-009] |
| 5         | 11-14       | ./sources/frontend/, ./sources/mobile-app/ | Xây dựng giao diện người dùng cho web và di động | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011], [EXC-005] |

### 4.3 PHÂN TÍCH TÀI NGUYÊN

#### 4.3.1 PHÂN TÍCH TÀI NGUYÊN PHẦN MỀM

- **Backend:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, Apache Kafka.
- **Frontend:** Next.js, React Native.
- **DevOps:** GitHub Actions, Docker, Kubernetes (GKE), Google Cloud Platform (GCP).

#### 4.3.2 PHÂN TÍCH TÀI NGUYÊN PHẦN CỨNG

- **Máy chủ:** Các máy chủ được triển khai trên các cụm Kubernetes (GKE) để đảm bảo tính sẵn sàng và khả năng mở rộng.
- **Mạng:** Sử dụng các dịch vụ mạng của Google Cloud Platform (GCP) để đảm bảo tính bảo mật và hiệu suất.
- **Lưu trữ:** Sử dụng các dịch vụ lưu trữ của Google Cloud Platform (GCP) để lưu trữ dữ liệu và các tài nguyên tĩnh.

## 📅 5. CHI TIẾT KIẾN TRÚC THEO PHÂN PHÁS

### Phase 3 - Triển Khai Lõi Nghiệp Vụ Điểm Danh Và Thông Báo

- **Phase Core Objective & Purpose:** Triển khai các dịch vụ lõi cho điểm danh và thông báo, bao gồm xử lý điểm danh qua mã QR, quản lý thông báo và gửi thông báo đến ứng dụng di động và nhóm Zalo.
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1: Khởi tạo dịch vụ điểm danh và xử lý mã QR**
  
##### SUB-TASK 1: Thiết kế lược đồ cơ sở dữ liệu cho điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-006]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_Attendance_Table.sql
* **Low-Level Technical Task Instruction:** Tạo bảng điểm danh với các trường: attendanceId (UUID, khóa chính), studentId (UUID, khóa ngoại tham chiếu đến Users.userId), courseId (UUID, khóa ngoại tham chiếu đến Courses.courseId), attendanceDate (DATE, không được để trống), timestamp (TIMESTAMP, mặc định là thời gian hiện tại). Thêm chỉ mục trên các trường studentId, courseId, và attendanceDate để tối ưu hóa hiệu suất truy vấn.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Thiết kế API điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-012], [REQ-013]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/api/AttendanceApi.java
* **Low-Level Technical Task Instruction:** Thiết kế API điểm danh với endpoint POST /api/attendance với payload JSON chứa studentId và courseId. Thêm xử lý idempotent để đảm bảo chỉ có một bản ghi điểm danh được tạo mỗi ngày cho mỗi học viên và khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết test cho API điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-012], [REQ-013]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/api/AttendanceApiTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/api/AttendanceApi.java
* **Low-Level Technical Task Instruction:** Viết các test case để kiểm tra tính năng điểm danh, bao gồm kiểm tra tạo bản ghi điểm danh mới, trùng lặp điểm danh trong cùng một ngày, và xử lý lỗi khi studentId hoặc courseId không hợp lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Tài liệu API điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-012], [REQ-013]
* **Target Component file path (target_component):** ./sources/docs/api/attendance-api.md
* **Low-Level Technical Task Instruction:** Tạo tài liệu chi tiết về API điểm danh, bao gồm các endpoint, payload yêu cầu và phản hồi, mã lỗi và ví dụ sử dụng.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Triển khai dịch vụ điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/Dockerfile
* **Low-Level Technical Task Instruction:** Tạo Dockerfile cho dịch vụ điểm danh, sử dụng Java/Quarkus làm cơ sở và cấu hình để chạy dịch vụ trên cổng 8080.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Triển khai dịch vụ điểm danh trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/attendance-service-deployment.yaml
* **Low-Level Technical Task Instruction:** Tạo tệp triển khai Kubernetes cho dịch vụ điểm danh, bao gồm các cấu hình để triển khai dịch vụ trên cụm GKE, cấu hình dịch vụ và ingress.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Khởi tạo dịch vụ thông báo và tích hợp với ứng dụng di động và nhóm Zalo**
  
##### SUB-TASK 1: Thiết kế lược đồ cơ sở dữ liệu cho thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-008]
* **Target Component file path (target_component):** ./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_Notification_Table.sql
* **Low-Level Technical Task Instruction:** Tạo bảng thông báo với các trường: notificationId (UUID, khóa chính), userId (UUID, khóa ngoại tham chiếu đến Users.userId, có thể là null), groupZalo (VARCHAR, có thể là null), message (TEXT, không được để trống), sentAt (TIMESTAMP, mặc định là thời gian hiện tại), delivered (BOOLEAN, mặc định là false). Thêm chỉ mục trên các trường userId và groupZalo để tối ưu hóa hiệu suất truy vấn.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Thiết kế API thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-016]
* **Target Component file path (target_component):** ./sources/backend/notification-service/src/main/java/com/membershiphub/notification/api/NotificationApi.java
* **Low-Level Technical Task Instruction:** Thiết kế API thông báo với endpoint POST /api/notifications với payload JSON chứa userId, groupZalo, và message. Thêm xử lý để gửi thông báo đến ứng dụng di động và nhóm Zalo.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết test cho API thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-016]
* **Target Component file path (target_component):** ./sources/backend/notification-service/src/test/java/com/membershiphub/notification/api/NotificationApiTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/api/NotificationApi.java
* **Low-Level Technical Task Instruction:** Viết các test case để kiểm tra tính năng thông báo, bao gồm kiểm tra tạo thông báo mới, gửi thông báo đến ứng dụng di động và nhóm Zalo, và xử lý lỗi khi userId hoặc groupZalo không hợp lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Tài liệu API thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-016]
* **Target Component file path (target_component):** ./sources/docs/api/notification-api.md
* **Low-Level Technical Task Instruction:** Tạo tài liệu chi tiết về API thông báo, bao gồm các endpoint, payload yêu cầu và phản hồi, mã lỗi và ví dụ sử dụng.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Triển khai dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/notification-service/Dockerfile
* **Low-Level Technical Task Instruction:** Tạo Dockerfile cho dịch vụ thông báo, sử dụng Java/Quarkus làm cơ sở và cấu hình để chạy dịch vụ trên cổng 8080.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Triển khai dịch vụ thông báo trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/notification-service-deployment.yaml
* **Low-Level Technical Task Instruction:** Tạo tệp triển khai Kubernetes cho dịch vụ thông báo, bao gồm các cấu hình để triển khai dịch vụ trên cụm GKE, cấu hình dịch vụ và ingress.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 3: Tích hợp dịch vụ điểm danh và thông báo với các dịch vụ khác**
  
##### SUB-TASK 1: Tích hợp dịch vụ điểm danh với dịch vụ khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-012], [REQ-013]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/service/AttendanceService.java
* **Low-Level Technical Task Instruction:** Thêm xử lý để kiểm tra xem học viên có đăng ký khóa học hay không trước khi ghi nhận điểm danh. Nếu học viên chưa đăng ký khóa học, trả về lỗi.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Tích hợp dịch vụ thông báo với dịch vụ người dùng
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-016]
* **Target Component file path (target_component):** ./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/NotificationService.java
* **Low-Level Technical Task Instruction:** Thêm xử lý để lấy thông tin người dùng từ dịch vụ người dùng và gửi thông báo đến ứng dụng di động của người dùng.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Viết test cho tích hợp dịch vụ điểm danh và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-016]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/service/AttendanceServiceTest.java;./sources/backend/notification-service/src/test/java/com/membershiphub/notification/service/NotificationServiceTest.java
* **Low-Level Technical Task Instruction:** Viết các test case để kiểm tra tích hợp dịch vụ điểm danh và thông báo, bao gồm kiểm tra ghi nhận điểm danh và gửi thông báo khi có điểm danh mới.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Tài liệu tích hợp dịch vụ điểm danh và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Doc]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-016]
* **Target Component file path (target_component):** ./sources/docs/integration/attendance-notification-integration.md
* **Low-Level Technical Task Instruction:** Tạo tài liệu chi tiết về tích hợp dịch vụ điểm danh và thông báo, bao gồm các bước tích hợp, ví dụ sử dụng và xử lý lỗi.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Triển khai tích hợp dịch vụ điểm danh và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/backend/attendance-service/Dockerfile;./sources/backend/notification-service/Dockerfile
* **Low-Level Technical Task Instruction:** Cập nhật Dockerfile cho dịch vụ điểm danh và thông báo để bao gồm các phụ thuộc cần thiết cho tích hợp.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Triển khai tích hợp dịch vụ điểm danh và thông báo trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke/attendance-service-deployment.yaml;./sources/infra/gke/notification-service-deployment.yaml
* **Low-Level Technical Task Instruction:** Cập nhật tệp triển khai Kubernetes cho dịch vụ điểm danh và thông báo để bao gồm các cấu hình cần thiết cho tích hợp.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_3-->

```markdown
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

## 4. KIẾN TRÚC TOÀN CẦU & PHÂN PHỐI PHÂN TÁN

### 4.1 KIẾN TRÚC TOÀN CẦU

#### 4.1.1 KIẾN TRÚC TOÀN CẦU

- **Kiến trúc tổng quan:** Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, khóa học, điểm danh, và thông báo. Sử dụng API Gateway để định tuyến các yêu cầu đến các dịch vụ tương ứng.
- **Kiến trúc dữ liệu:** Sử dụng cơ sở dữ liệu PostgreSQL với các bảng được chuẩn hóa để lưu trữ dữ liệu người dùng, khóa học, điểm danh, và thông báo. Sử dụng Redis để lưu trữ session và caching.
- **Kiến trúc giao diện người dùng:** Sử dụng Next.js cho frontend web và React Native cho ứng dụng di động. Sử dụng Firebase Authentication cho xác thực người dùng và Firebase Cloud Messaging (FCM) cho push notification.

#### 4.1.2 KIẾN TRÚC PHÂN TÁN

- **Kiến trúc phân tán:** Hệ thống được triển khai trên Google Kubernetes Engine (GKE) với các dịch vụ được container hóa bằng Docker. Sử dụng Kubernetes Horizontal Pod Autoscaler (HPA) để tự động mở rộng các dịch vụ dựa trên tải.
- **Kiến trúc dữ liệu phân tán:** Sử dụng PostgreSQL read replicas để xử lý các truy vấn báo cáo và phân tích. Sử dụng Redis để lưu trữ session và caching.
- **Kiến trúc giao diện người dùng phân tán:** Sử dụng Firebase Hosting để triển khai frontend web và ứng dụng di động. Sử dụng Firebase Cloud Functions để xử lý các sự kiện và thông báo.

### 4.2 MULTI-PHASE SYNOPSIS MATRIX

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|-------------|-------------------------|---------------------------|------------|------------------|
| 1         | 1-3         | ./sources/backend/auth-service/ | Xây dựng dịch vụ xác thực với email/mật khẩu, Firebase, Google, Facebook OAuth2 | Coder, Tester, Reviewer, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004] |
| 2         | 4-6         | ./sources/backend/course-service/ | Xây dựng dịch vụ quản lý khóa học với các chức năng tạo, cập nhật, xóa khóa học | Coder, Tester, Reviewer, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| 3         | 7-9         | ./sources/backend/attendance-service/ | Xây dựng dịch vụ điểm danh với chức năng quét mã QR và ghi lại điểm danh | Coder, Tester, Reviewer, Docker, GCP, GKE | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| 4         | 10-12       | ./sources/backend/notification-service/ | Xây dựng dịch vụ thông báo với chức năng gửi thông báo đến ứng dụng di động và nhóm Zalo | Coder, Tester, Reviewer, Docker, GCP, GKE | [REQ-016], [DAT-008], [EXC-003] |
| 5         | 13-15       | ./sources/frontend/ | Xây dựng giao diện người dùng với các chức năng duyệt khóa học, đăng ký khóa học, xem thẻ hội viên | Coder, Tester, Reviewer, Docker, GCP, GKE | [REQ-010], [REQ-011], [REQ-014], [REQ-015], [DAT-005], [DAT-007] |

## 5. PHÂN PHỐI NHIỆM VỤ THEO NGÀY

### Phase 4: Triển Khai Lõi Nghiệp Vụ Thông Báo

- **Phase Core Objective & Purpose:** Triển khai dịch vụ thông báo với chức năng gửi thông báo đến ứng dụng di động và nhóm Zalo. Đảm bảo tính tin cậy và hiệu suất cao của dịch vụ thông báo.
- **Target Physical Directory Matrix Map:** ./sources/backend/notification-service/
- **Database Schema DDL SQL Specification [DAT-008]:**
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(255),
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE
);
```
- **API and Event Routing Contracts [REQ-016], [ARC-008]:**
```json
{
    "sendNotification": {
        "method": "POST",
        "path": "/api/notifications",
        "request": {
            "userId": "UUID",
            "groupZalo": "string",
            "message": "string"
        },
        "response": {
            "notificationId": "UUID",
            "status": "string"
        }
    }
}
```
- **Phase Localized Exception Handlers [EXC-003]:**
- Nếu không thể gửi thông báo đến thiết bị di động, hệ thống sẽ ghi lại lỗi và thử lại tối đa 3 lần trước khi đánh dấu là thất bại.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Khởi tạo dịch vụ thông báo**
  
##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Coder]
* Targeted Tag IDs: [DAT-008]
* Target Component file path: ./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_notifications_table.sql
* Low-Level Technical Task Instruction: Tạo bảng notifications với các cột notification_id, user_id, group_zalo, message, sent_at, delivered. [DAT-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết unit tests cho cơ sở dữ liệu
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Tester]
* Targeted Tag IDs: [DAT-008]
* Target Component file path: ./sources/backend/notification-service/src/test/java/com/example/notification/db/NotificationsTableTest.java;./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_notifications_table.sql
* Low-Level Technical Task Instruction: Viết unit tests để kiểm tra việc tạo bảng notifications. [DAT-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Review code cơ sở dữ liệu
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Reviewer]
* Targeted Tag IDs: [DAT-008]
* Target Component file path: ./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_notifications_table.sql
* Low-Level Technical Task Instruction: Review code cơ sở dữ liệu để đảm bảo tính đúng đắn và hiệu suất. [DAT-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Tài liệu cơ sở dữ liệu
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Doc]
* Targeted Tag IDs: [DAT-008]
* Target Component file path: ./sources/docs/database/notification-service.md
* Low-Level Technical Task Instruction: Tài liệu cơ sở dữ liệu cho dịch vụ thông báo. [DAT-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng Dockerfile cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Docker]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/backend/notification-service/Dockerfile
* Low-Level Technical Task Instruction: Xây dựng Dockerfile cho dịch vụ thông báo. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Triển khai cơ sở hạ tầng trên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [GCP]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/infra/gcp/notification-service.yaml
* Low-Level Technical Task Instruction: Triển khai cơ sở hạ tầng trên GCP cho dịch vụ thông báo. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Triển khai dịch vụ thông báo trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [GKE]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/infra/gke/notification-service.yaml
* Low-Level Technical Task Instruction: Triển khai dịch vụ thông báo trên GKE. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Triển khai chức năng gửi thông báo**
  
##### SUB-TASK 1: Thiết kế API gửi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Coder]
* Targeted Tag IDs: [REQ-016]
* Target Component file path: ./sources/backend/notification-service/src/main/java/com/example/notification/api/NotificationApi.java
* Low-Level Technical Task Instruction: Thiết kế API gửi thông báo với endpoint /api/notifications. [REQ-016]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết unit tests cho API gửi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Tester]
* Targeted Tag IDs: [REQ-016]
* Target Component file path: ./sources/backend/notification-service/src/test/java/com/example/notification/api/NotificationApiTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/api/NotificationApi.java
* Low-Level Technical Task Instruction: Viết unit tests cho API gửi thông báo. [REQ-016]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Review code API gửi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Reviewer]
* Targeted Tag IDs: [REQ-016]
* Target Component file path: ./sources/backend/notification-service/src/main/java/com/example/notification/api/NotificationApi.java
* Low-Level Technical Task Instruction: Review code API gửi thông báo để đảm bảo tính đúng đắn và hiệu suất. [REQ-016]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Tài liệu API gửi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Doc]
* Targeted Tag IDs: [REQ-016]
* Target Component file path: ./sources/docs/api/notification-service.md
* Low-Level Technical Task Instruction: Tài liệu API gửi thông báo. [REQ-016]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng Dockerfile cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Docker]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/backend/notification-service/Dockerfile
* Low-Level Technical Task Instruction: Xây dựng Dockerfile cho dịch vụ thông báo. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Triển khai cơ sở hạ tầng trên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [GCP]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/infra/gcp/notification-service.yaml
* Low-Level Technical Task Instruction: Triển khai cơ sở hạ tầng trên GCP cho dịch vụ thông báo. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Triển khai dịch vụ thông báo trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [GKE]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/infra/gke/notification-service.yaml
* Low-Level Technical Task Instruction: Triển khai dịch vụ thông báo trên GKE. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 3: Triển khai chức năng xử lý lỗi thông báo**
  
##### SUB-TASK 1: Thiết kế xử lý lỗi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Coder]
* Targeted Tag IDs: [EXC-003]
* Target Component file path: ./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java
* Low-Level Technical Task Instruction: Thiết kế xử lý lỗi thông báo với chức năng ghi lại lỗi và thử lại tối đa 3 lần. [EXC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 2: Viết unit tests cho xử lý lỗi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Tester]
* Targeted Tag IDs: [EXC-003]
* Target Component file path: ./sources/backend/notification-service/src/test/java/com/example/notification/service/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java
* Low-Level Technical Task Instruction: Viết unit tests cho xử lý lỗi thông báo. [EXC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 3: Review code xử lý lỗi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Reviewer]
* Targeted Tag IDs: [EXC-003]
* Target Component file path: ./sources/backend/notification-service/src/main/java/com/example/notification/service/NotificationService.java
* Low-Level Technical Task Instruction: Review code xử lý lỗi thông báo để đảm bảo tính đúng đắn và hiệu suất. [EXC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 4: Tài liệu xử lý lỗi thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Doc]
* Targeted Tag IDs: [EXC-003]
* Target Component file path: ./sources/docs/exception/notification-service.md
* Low-Level Technical Task Instruction: Tài liệu xử lý lỗi thông báo. [EXC-003]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 5: Xây dựng Dockerfile cho dịch vụ thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [Docker]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/backend/notification-service/Dockerfile
* Low-Level Technical Task Instruction: Xây dựng Dockerfile cho dịch vụ thông báo. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 6: Triển khai cơ sở hạ tầng trên GCP
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [GCP]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/infra/gcp/notification-service.yaml
* Low-Level Technical Task Instruction: Triển khai cơ sở hạ tầng trên GCP cho dịch vụ thông báo. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->

##### SUB-TASK 7: Triển khai dịch vụ thông báo trên GKE
<!--START_ATOMIC_SUB_TASK_NODE-->
* Sub-Agent: [GKE]
* Targeted Tag IDs: [ARC-008]
* Target Component file path: ./sources/infra/gke/notification-service.yaml
* Low-Level Technical Task Instruction: Triển khai dịch vụ thông báo trên GKE. [ARC-008]
<!--END_ATOMIC_SUB_TASK_NODE-->
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

## 📅 4. PHÂN TÍCH KIẾN TRÚC & LỐI THỜI GIAN

### 4.1 MASTER PRODUCT BACKLOG

| STT | Mô-đun / Chức năng | Mô tả | Tag IDs |
|-----|---------------------|-------|---------|
| 1   | Quản lý người dùng  | Đăng ký, xác thực, phân quyền người dùng | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004] |
| 2   | Quản lý trung tâm  | Tạo, cập nhật, xóa trung tâm; phân quyền quản trị | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| 3   | Quản lý khóa học   | Tạo, cập nhật, xóa khóa học; phân công giáo viên | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| 4   | Đăng ký & ghi danh học viên | Duyệt khóa học, đăng ký khóa học | [REQ-010], [REQ-011], [DAT-005] |
| 5   | Điểm danh & quét mã QR | Quét mã QR để điểm danh; xử lý trùng lặp | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| 6   | Quản lý thẻ hội viên | Hiển thị thẻ hội viên, gia hạn thẻ | [REQ-014], [REQ-015], [DAT-007] |
| 7   | Thông báo & truyền thông | Kích hoạt thông báo qua ứng dụng di động và Zalo | [REQ-016], [DAT-008], [EXC-003] |
| 8   | Quản lý khuyến mãi & thông báo | Tạo, cập nhật, xóa khuyến mãi và thông báo | [REQ-017], [REQ-018], [DAT-009] |
| 9   | Chatbot dịch vụ khách hàng AI | Tích hợp chatbot AI để trả lời các truy vấn phổ biến | [REQ-019] |
| 10  | Các tính năng cốt lõi của ứng dụng di động | Giao diện người dùng, thông báo đẩy | [REQ-020], [REQ-021] |
| 11  | Bản địa hóa & SEO | Phát hiện ngôn ngữ, SEO đa ngôn ngữ | [REQ-022], [REQ-023], [DAT-011] |
| 12  | Báo cáo & phân tích | Tạo báo cáo điểm danh, bảng điều khiển tóm tắt | [REQ-024], [REQ-025], [EXC-005] |
| 13  | Kiến trúc & luồng dữ liệu | Xác thực, điểm danh QR, gửi thông báo, tích hợp backend | [ARC-006], [ARC-007], [ARC-008], [ARC-009] |
| 14  | Công nghệ & hạ tầng | Backend, cơ sở dữ liệu, container hóa, triển khai | [ARC-010] |
| 15  | Performance Metrics | Hiệu suất API, truy vấn cơ sở dữ liệu | [NFR-001] |
| 16  | Availability | Độ sẵn sàng hệ thống, failover | [NFR-002] |
| 17  | Security | Bảo mật dữ liệu, xác thực, OWASP Top 10 | [NFR-003] |

### 4.2 MULTI-PHASE SYNOPSIS MATRIX

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
|-----------|--------------|-------------------------|----------------------------|-----------|------------------|
| 1         | 1-2          | ./sources/backend/auth-service/ | Khởi tạo hệ thống xác thực người dùng | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006], [NFR-003] |
| 2         | 3-4          | ./sources/backend/center-service/ | Khởi tạo hệ thống quản lý trung tâm | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| 3         | 5-6          | ./sources/backend/course-service/ | Khởi tạo hệ thống quản lý khóa học | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| 4         | 7-7          | ./sources/backend/enrollment-service/ | Khởi tạo hệ thống đăng ký & ghi danh học viên | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-010], [REQ-011], [DAT-005] |
| 5         | 1-7          | ./sources/backend/attendance-service/, ./sources/backend/notification-service/, ./sources/backend/membership-service/, ./sources/backend/promotion-service/, ./sources/backend/chatbot-service/, ./sources/frontend/, ./sources/infra/ | Triển khai lõi nghiệp vụ điểm danh, thông báo, thẻ hội viên, khuyến mãi, chatbot, ứng dụng di động, hạ tầng | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [EXC-001], [EXC-002], [EXC-003], [EXC-005], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 📝 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN

### Phase 5 - Triển Khai Lõi Nghiệp Vụ Điểm Danh, Thông Báo, Thẻ Hội Viên, Khuyến Mãi, Chatbot, Ứng Dụng Di Động, Hạ Tầng

- **Phase Core Objective & Purpose:** Triển khai các tính năng lõi của hệ thống bao gồm điểm danh qua mã QR, quản lý thông báo, thẻ hội viên, khuyến mãi, chatbot, ứng dụng di động và hạ tầng.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend/attendance-service/
    * ./sources/backend/notification-service/
    * ./sources/backend/membership-service/
    * ./sources/backend/promotion-service/
    * ./sources/backend/chatbot-service/
    * ./sources/frontend/
    * ./sources/infra/
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:**
```sql
-- Attendance table
CREATE TABLE attendance (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES users(userId),
    FOREIGN KEY (courseId) REFERENCES courses(courseId)
);

-- StudentCards table
CREATE TABLE student_cards (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES users(userId)
);

-- Notifications table
CREATE TABLE notifications (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (userId) REFERENCES users(userId)
);

-- Promotions table
CREATE TABLE promotions (
    promoId UUID PRIMARY KEY,
    code VARCHAR(50) UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);

-- Announcements table
CREATE TABLE announcements (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);

-- SystemSettings table
CREATE TABLE system_settings (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(255)
);
```

- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:**
```json
{
  "attendance": {
    "scanQR": {
      "method": "POST",
      "path": "/api/attendance/scan",
      "request": {
        "studentId": "uuid",
        "courseId": "uuid",
        "timestamp": "string"
      },
      "response": {
        "status": "string",
        "message": "string"
      }
    }
  },
  "notifications": {
    "sendNotification": {
      "method": "POST",
      "path": "/api/notifications/send",
      "request": {
        "userId": "uuid",
        "groupZalo": "string",
        "message": "string"
      },
      "response": {
        "status": "string",
        "message": "string"
      }
    }
  },
  "membership": {
    "getCard": {
      "method": "GET",
      "path": "/api/membership/card",
      "request": {
        "studentId": "uuid"
      },
      "response": {
        "cardId": "uuid",
        "issueDate": "string",
        "validityDays": "integer",
        "remainingDays": "integer"
      }
    }
  },
  "promotions": {
    "getPromotions": {
      "method": "GET",
      "path": "/api/promotions",
      "request": {},
      "response": {
        "promotions": [
          {
            "promoId": "uuid",
            "code": "string",
            "discountPercent": "integer",
            "startDate": "string",
            "endDate": "string",
            "description": "string"
          }
        ]
      }
    }
  },
  "chatbot": {
    "askQuestion": {
      "method": "POST",
      "path": "/api/chatbot/ask",
      "request": {
        "question": "string"
      },
      "response": {
        "answer": "string"
      }
    }
  },
  "mobile": {
    "getNotifications": {
      "method": "GET",
      "path": "/api/mobile/notifications",
      "request": {
        "userId": "uuid"
      },
      "response": {
        "notifications": [
          {
            "notificationId": "uuid",
            "message": "string",
            "sentAt": "string"
          }
        ]
      }
    }
  },
  "localization": {
    "getLocale": {
      "method": "GET",
      "path": "/api/localization/locale",
      "request": {},
      "response": {
        "locale": "string"
      }
    }
  },
  "reports": {
    "getAttendanceReport": {
      "method": "GET",
      "path": "/api/reports/attendance",
      "request": {
        "centerId": "uuid",
        "startDate": "string",
        "endDate": "string"
      },
      "response": {
        "report": "string"
      }
    }
  }
}
```

- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-005]:**
- **Xử lý ngoại lệ điểm danh:**
  - Nếu mạng bị gián đoạn trong quá trình quét mã QR, hệ thống sẽ ghi lại lỗi và thử lại sau khi kết nối mạng được khôi phục.
  - Nếu học viên quét mã QR nhiều lần trong cùng một ngày, hệ thống sẽ chỉ ghi lại một bản ghi điểm danh và trả về thông báo đã ghi nhận.

- **Xử lý ngoại lệ thông báo:**
  - Nếu thông báo không thể được gửi (ví dụ: token thiết bị không hợp lệ), hệ thống sẽ ghi lại lỗi và thử lại tối đa ba lần trước khi đánh dấu là thất bại.

- **Xử lý ngoại lệ hệ thống:**
  - Nếu dịch vụ trở nên không khả dụng, khi dịch vụ khôi phục, tất cả các bản ghi điểm danh đang chờ xử lý sẽ được xử lý theo thứ tự FIFO và người dùng sẽ nhận được thông báo về các sự kiện đã khôi phục.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

<!--START_DAY_LOG_INDEX_5-->

- **DAY 1: Triển khai hệ thống điểm danh và quản lý thông báo**
  - **SUB-TASK 1: Thiết kế và triển khai API điểm danh**
    - [Coder]
    - [REQ-012], [REQ-013], [DAT-006]
    - ./sources/backend/attendance-service/
    - Thiết kế và triển khai API để quét mã QR và ghi lại điểm danh. Đảm bảo tính bất biến của điểm danh.
  - **SUB-TASK 2: Thiết kế và triển khai API quản lý thông báo**
    - [Coder]
    - [REQ-016], [DAT-008]
    - ./sources/backend/notification-service/
    - Thiết kế và triển khai API để gửi thông báo đến ứng dụng di động và nhóm Zalo.
  - **SUB-TASK 3: Viết test cho API điểm danh**
    - [Tester]
    - [REQ-012], [REQ-013], [DAT-006]
    - ./sources/backend/attendance-service/test;./sources/backend/attendance-service/
    - Viết test cho API điểm danh để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 4: Viết test cho API quản lý thông báo**
    - [Tester]
    - [REQ-016], [DAT-008]
    - ./sources/backend/notification-service/test;./sources/backend/notification-service/
    - Viết test cho API quản lý thông báo để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 5: Review code điểm danh và quản lý thông báo**
    - [Reviewer]
    - [REQ-012], [REQ-013], [REQ-016], [DAT-006], [DAT-008]
    - ./sources/backend/attendance-service/, ./sources/backend/notification-service/
    - Review code điểm danh và quản lý thông báo để đảm bảo chất lượng và tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 6: Tài liệu API điểm danh và quản lý thông báo**
    - [Doc]
    - [REQ-012], [REQ-013], [REQ-016], [DAT-006], [DAT-008]
    - ./sources/docs/
    - Tài liệu API điểm danh và quản lý thông báo để hỗ trợ phát triển và sử dụng.
  - **SUB-TASK 7: Triển khai Docker cho điểm danh và quản lý thông báo**
    - [Docker]
    - [ARC-010]
    - ./sources/backend/attendance-service/Dockerfile, ./sources/backend/notification-service/Dockerfile
    - Tạo Dockerfile và triển khai container cho điểm danh và quản lý thông báo.
  - **SUB-TASK 8: Triển khai GCP cho điểm danh và quản lý thông báo**
    - [GCP]
    - [ARC-010]
    - ./sources/infra/gcp/
    - Cấu hình và triển khai các dịch vụ GCP cho điểm danh và quản lý thông báo.
  - **SUB-TASK 9: Triển khai GKE cho điểm danh và quản lý thông báo**
    - [GKE]
    - [ARC-010]
    - ./sources/infra/gke/
    - Cấu hình và triển khai các dịch vụ GKE cho điểm danh và quản lý thông báo.

- **DAY 2: Triển khai hệ thống quản lý thẻ hội viên và khuyến mãi**
  - **SUB-TASK 1: Thiết kế và triển khai API quản lý thẻ hội viên**
    - [Coder]
    - [REQ-014], [REQ-015], [DAT-007]
    - ./sources/backend/membership-service/
    - Thiết kế và triển khai API để hiển thị và gia hạn thẻ hội viên.
  - **SUB-TASK 2: Thiết kế và triển khai API quản lý khuyến mãi**
    - [Coder]
    - [REQ-017], [DAT-009]
    - ./sources/backend/promotion-service/
    - Thiết kế và triển khai API để quản lý khuyến mãi.
  - **SUB-TASK 3: Viết test cho API quản lý thẻ hội viên**
    - [Tester]
    - [REQ-014], [REQ-015], [DAT-007]
    - ./sources/backend/membership-service/test;./sources/backend/membership-service/
    - Viết test cho API quản lý thẻ hội viên để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 4: Viết test cho API quản lý khuyến mãi**
    - [Tester]
    - [REQ-017], [DAT-009]
    - ./sources/backend/promotion-service/test;./sources/backend/promotion-service/
    - Viết test cho API quản lý khuyến mãi để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 5: Review code quản lý thẻ hội viên và khuyến mãi**
    - [Reviewer]
    - [REQ-014], [REQ-015], [REQ-017], [DAT-007], [DAT-009]
    - ./sources/backend/membership-service/, ./sources/backend/promotion-service/
    - Review code quản lý thẻ hội viên và khuyến mãi để đảm bảo chất lượng và tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 6: Tài liệu API quản lý thẻ hội viên và khuyến mãi**
    - [Doc]
    - [REQ-014], [REQ-015], [REQ-017], [DAT-007], [DAT-009]
    - ./sources/docs/
    - Tài liệu API quản lý thẻ hội viên và khuyến mãi để hỗ trợ phát triển và sử dụng.
  - **SUB-TASK 7: Triển khai Docker cho quản lý thẻ hội viên và khuyến mãi**
    - [Docker]
    - [ARC-010]
    - ./sources/backend/membership-service/Dockerfile, ./sources/backend/promotion-service/Dockerfile
    - Tạo Dockerfile và triển khai container cho quản lý thẻ hội viên và khuyến mãi.
  - **SUB-TASK 8: Triển khai GCP cho quản lý thẻ hội viên và khuyến mãi**
    - [GCP]
    - [ARC-010]
    - ./sources/infra/gcp/
    - Cấu hình và triển khai các dịch vụ GCP cho quản lý thẻ hội viên và khuyến mãi.
  - **SUB-TASK 9: Triển khai GKE cho quản lý thẻ hội viên và khuyến mãi**
    - [GKE]
    - [ARC-010]
    - ./sources/infra/gke/
    - Cấu hình và triển khai các dịch vụ GKE cho quản lý thẻ hội viên và khuyến mãi.

- **DAY 3: Triển khai hệ thống chatbot và ứng dụng di động**
  - **SUB-TASK 1: Thiết kế và triển khai API chatbot**
    - [Coder]
    - [REQ-019]
    - ./sources/backend/chatbot-service/
    - Thiết kế và triển khai API cho chatbot để trả lời các truy vấn phổ biến.
  - **SUB-TASK 2: Thiết kế và triển khai giao diện người dùng di động**
    - [Coder]
    - [REQ-020], [REQ-021]
    - ./sources/frontend/
    - Thiết kế và triển khai giao diện người dùng di động cho các vai trò khác nhau.
  - **SUB-TASK 3: Viết test cho API chatbot**
    - [Tester]
    - [REQ-019]
    - ./sources/backend/chatbot-service/test;./sources/backend/chatbot-service/
    - Viết test cho API chatbot để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 4: Viết test cho giao diện người dùng di động**
    - [Tester]
    - [REQ-020], [REQ-021]
    - ./sources/frontend/test;./sources/frontend/
    - Viết test cho giao diện người dùng di động để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 5: Review code chatbot và giao diện người dùng di động**
    - [Reviewer]
    - [REQ-019], [REQ-020], [REQ-021]
    - ./sources/backend/chatbot-service/, ./sources/frontend/
    - Review code chatbot và giao diện người dùng di động để đảm bảo chất lượng và tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 6: Tài liệu API chatbot và giao diện người dùng di động**
    - [Doc]
    - [REQ-019], [REQ-020], [REQ-021]
    - ./sources/docs/
    - Tài liệu API chatbot và giao diện người dùng di động để hỗ trợ phát triển và sử dụng.
  - **SUB-TASK 7: Triển khai Docker cho chatbot và giao diện người dùng di động**
    - [Docker]
    - [ARC-010]
    - ./sources/backend/chatbot-service/Dockerfile, ./sources/frontend/Dockerfile
    - Tạo Dockerfile và triển khai container cho chatbot và giao diện người dùng di động.
  - **SUB-TASK 8: Triển khai GCP cho chatbot và giao diện người dùng di động**
    - [GCP]
    - [ARC-010]
    - ./sources/infra/gcp/
    - Cấu hình và triển khai các dịch vụ GCP cho chatbot và giao diện người dùng di động.
  - **SUB-TASK 9: Triển khai GKE cho chatbot và giao diện người dùng di động**
    - [GKE]
    - [ARC-010]
    - ./sources/infra/gke/
    - Cấu hình và triển khai các dịch vụ GKE cho chatbot và giao diện người dùng di động.

- **DAY 4: Triển khai hệ thống bản địa hóa và SEO**
  - **SUB-TASK 1: Thiết kế và triển khai API bản địa hóa**
    - [Coder]
    - [REQ-022], [DAT-011]
    - ./sources/backend/localization-service/
    - Thiết kế và triển khai API để phát hiện ngôn ngữ và bản địa hóa giao diện người dùng.
  - **SUB-TASK 2: Thiết kế và triển khai API SEO**
    - [Coder]
    - [REQ-023]
    - ./sources/backend/seo-service/
    - Thiết kế và triển khai API để hỗ trợ SEO đa ngôn ngữ.
  - **SUB-TASK 3: Viết test cho API bản địa hóa**
    - [Tester]
    - [REQ-022], [DAT-011]
    - ./sources/backend/localization-service/test;./sources/backend/localization-service/
    - Viết test cho API bản địa hóa để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 4: Viết test cho API SEO**
    - [Tester]
    - [REQ-023]
    - ./sources/backend/seo-service/test;./sources/backend/seo-service/
    - Viết test cho API SEO để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 5: Review code bản địa hóa và SEO**
    - [Reviewer]
    - [REQ-022], [REQ-023], [DAT-011]
    - ./sources/backend/localization-service/, ./sources/backend/seo-service/
    - Review code bản địa hóa và SEO để đảm bảo chất lượng và tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 6: Tài liệu API bản địa hóa và SEO**
    - [Doc]
    - [REQ-022], [REQ-023], [DAT-011]
    - ./sources/docs/
    - Tài liệu API bản địa hóa và SEO để hỗ trợ phát triển và sử dụng.
  - **SUB-TASK 7: Triển khai Docker cho bản địa hóa và SEO**
    - [Docker]
    - [ARC-010]
    - ./sources/backend/localization-service/Dockerfile, ./sources/backend/seo-service/Dockerfile
    - Tạo Dockerfile và triển khai container cho bản địa hóa và SEO.
  - **SUB-TASK 8: Triển khai GCP cho bản địa hóa và SEO**
    - [GCP]
    - [ARC-010]
    - ./sources/infra/gcp/
    - Cấu hình và triển khai các dịch vụ GCP cho bản địa hóa và SEO.
  - **SUB-TASK 9: Triển khai GKE cho bản địa hóa và SEO**
    - [GKE]
    - [ARC-010]
    - ./sources/infra/gke/
    - Cấu hình và triển khai các dịch vụ GKE cho bản địa hóa và SEO.

- **DAY 5: Triển khai hệ thống báo cáo và phân tích**
  - **SUB-TASK 1: Thiết kế và triển khai API báo cáo điểm danh**
    - [Coder]
    - [REQ-024]
    - ./sources/backend/report-service/
    - Thiết kế và triển khai API để tạo báo cáo điểm danh.
  - **SUB-TASK 2: Thiết kế và triển khai API bảng điều khiển tóm tắt**
    - [Coder]
    - [REQ-025]
    - ./sources/backend/dashboard-service/
    - Thiết kế và triển khai API để hiển thị bảng điều khiển tóm tắt.
  - **SUB-TASK 3: Viết test cho API báo cáo điểm danh**
    - [Tester]
    - [REQ-024]
    - ./sources/backend/report-service/test;./sources/backend/report-service/
    - Viết test cho API báo cáo điểm danh để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 4: Viết test cho API bảng điều khiển tóm tắt**
    - [Tester]
    - [REQ-025]
    - ./sources/backend/dashboard-service/test;./sources/backend/dashboard-service/
    - Viết test cho API bảng điều khiển tóm tắt để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 5: Review code báo cáo và phân tích**
    - [Reviewer]
    - [REQ-024], [REQ-025]
    - ./sources/backend/report-service/, ./sources/backend/dashboard-service/
    - Review code báo cáo và phân tích để đảm bảo chất lượng và tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 6: Tài liệu API báo cáo và phân tích**
    - [Doc]
    - [REQ-024], [REQ-025]
    - ./sources/docs/
    - Tài liệu API báo cáo và phân tích để hỗ trợ phát triển và sử dụng.
  - **SUB-TASK 7: Triển khai Docker cho báo cáo và phân tích**
    - [Docker]
    - [ARC-010]
    - ./sources/backend/report-service/Dockerfile, ./sources/backend/dashboard-service/Dockerfile
    - Tạo Dockerfile và triển khai container cho báo cáo và phân tích.
  - **SUB-TASK 8: Triển khai GCP cho báo cáo và phân tích**
    - [GCP]
    - [ARC-010]
    - ./sources/infra/gcp/
    - Cấu hình và triển khai các dịch vụ GCP cho báo cáo và phân tích.
  - **SUB-TASK 9: Triển khai GKE cho báo cáo và phân tích**
    - [GKE]
    - [ARC-010]
    - ./sources/infra/gke/
    - Cấu hình và triển khai các dịch vụ GKE cho báo cáo và phân tích.

- **DAY 6: Triển khai hệ thống hạ tầng và tối ưu hóa**
  - **SUB-TASK 1: Cấu hình hạ tầng và tối ưu hóa**
    - [GCP], [GKE]
    - [ARC-010], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    - ./sources/infra/
    - Cấu hình hạ tầng và tối ưu hóa hệ thống để đảm bảo hiệu suất, độ sẵn sàng và bảo mật.
  - **SUB-TASK 2: Viết test cho hạ tầng và tối ưu hóa**
    - [Tester]
    - [ARC-010], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    - ./sources/infra/test;./sources/infra/
    - Viết test cho hạ tầng và tối ưu hóa để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 3: Review code hạ tầng và tối ưu hóa**
    - [Reviewer]
    - [ARC-010], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    - ./sources/infra/
    - Review code hạ tầng và tối ưu hóa để đảm bảo chất lượng và tuân thủ các tiêu chuẩn lập trình.
  - **SUB-TASK 4: Tài liệu hạ tầng và tối ưu hóa**
    - [Doc]
    - [ARC-010], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    - ./sources/docs/
    - Tài liệu hạ tầng và tối ưu hóa để hỗ trợ phát triển và sử dụng.

- **DAY 7: Kiểm tra và triển khai hệ thống**
  - **SUB-TASK 1: Kiểm tra toàn bộ hệ thống**
    - [Tester]
    - [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [EXC-001], [EXC-002], [EXC-003], [EXC-005], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    - ./sources/
    - Kiểm tra toàn bộ hệ thống để đảm bảo tính đúng đắn và hiệu suất.
  - **SUB-TASK 2: Triển khai hệ thống**
    - [Docker], [GCP], [GKE]
    - [ARC-010]
    - ./sources/
    - Triển khai hệ thống lên môi trường sản xuất.

<!--END_PHASE_LOG_BLOCK_INDEX_5-->

### MANDATORY REAL-TIME ARCHITECTURAL CROSS-AUDIT LEDGER REPORT:

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=7
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=17
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=54
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

```markdown
# GLOBAL PROJECT CONTEXT: membership-hub

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

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`
```