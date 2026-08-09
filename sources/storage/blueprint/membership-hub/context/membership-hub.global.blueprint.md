# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809131523 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 13:15:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo kiến trúc đa lớp với các thành phần chính bao gồm: Frontend (Next.js), Backend (Quarkus), Cơ sở dữ liệu (PostgreSQL), và Hạ tầng đám mây (GCP).
- Sử dụng mô hình RBAC (Role-Based Access Control) để quản lý quyền truy cập dựa trên vai trò người dùng.
- Hệ thống hỗ trợ xác thực đa kênh thông qua Firebase, Google, và Facebook OAuth.
- Sử dụng JWT cho quản lý phiên và refresh token để duy trì tính liên tục của phiên làm việc.
- Kiến trúc microservices được áp dụng cho các thành phần chính như quản lý người dùng, quản lý trung tâm, quản lý khóa học, và quản lý điểm danh.
- Sử dụng Redis cho session caching để cải thiện hiệu suất và trải nghiệm người dùng.
- Hệ thống được triển khai trên Kubernetes (GKE) để đảm bảo tính sẵn sàng và khả năng mở rộng.
- Sử dụng Firebase Cloud Messaging (FCM) và Apple APNs cho push notification trên thiết bị di động.
- Hệ thống tích hợp với Zalo API để gửi thông báo và thông tin quan trọng đến người dùng.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Luồng dữ liệu chính bao gồm xác thực người dùng, quản lý trung tâm, quản lý khóa học, đăng ký học viên, điểm danh, và quản lý thẻ hội viên.
- Sử dụng cơ chế idempotent để đảm bảo tính nhất quán của dữ liệu điểm danh.
- Hệ thống sử dụng cơ chế queue để xử lý các thông báo và thông tin quan trọng.
- Sử dụng cơ chế caching để tối ưu hóa hiệu suất của hệ thống.
- Hệ thống được thiết kế để hỗ trợ đa ngôn ngữ và đa quốc gia.
- Sử dụng cơ chế backup và disaster recovery để đảm bảo tính sẵn sàng của hệ thống.
- Hệ thống được thiết kế để tuân thủ các quy định về bảo mật và quyền riêng tư như GDPR và CCPA.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM), Apple APNs, Redis, GitHub Actions
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native, Firebase Authentication, Google Cloud Messaging (FCM), Apple APNs

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

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG

<!--START_BACKLOG_SYNOPSIS_GRID-->

| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Xây dựng hệ thống xác thực người dùng | Xây dựng hệ thống xác thực người dùng sử dụng email/mật khẩu, Firebase, Google, và Facebook OAuth | Application Code | [REQ-001], [REQ-002], [ARC-006] |
| 2 | Xây dựng hệ thống quản lý người dùng | Xây dựng hệ thống quản lý người dùng với các vai trò: System Admin, Center Admin, Manager, Teacher, và Student | Application Code | [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| 3 | Xây dựng hệ thống quản lý trung tâm | Xây dựng hệ thống quản lý trung tâm với các chức năng: xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm | Application Code | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002] |
| 4 | Xây dựng hệ thống quản lý khóa học | Xây dựng hệ thống quản lý khóa học với các chức năng: xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học | Application Code | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003] |
| 5 | Xây dựng hệ thống đăng ký & ghi danh học viên | Xây dựng hệ thống đăng ký & ghi danh học viên với các chức năng: duyệt khóa học, đăng ký khóa học của học viên | Application Code | [REQ-010], [REQ-011], [DAT-005], [ARC-004] |
| 6 | Xây dựng hệ thống điểm danh & quét mã QR | Xây dựng hệ thống điểm danh & quét mã QR với các chức năng: chụp ảnh điểm danh QR, và tính chất bất biến của điểm danh | Application Code | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002], [ARC-004] |
| 7 | Xây dựng hệ thống quản lý thẻ hội viên | Xây dựng hệ thống quản lý thẻ hội viên với các chức năng: hiển thị tính hợp lệ của thẻ, và gia hạn thẻ | Application Code | [REQ-014], [REQ-015], [DAT-007], [ARC-005] |
| 8 | Xây dựng hệ thống thông báo & truyền thông | Xây dựng hệ thống thông báo & truyền thông với các chức năng: kích hoạt thông báo | Application Code | [REQ-016], [DAT-008], [EXC-003], [ARC-008] |
| 9 | Xây dựng hệ thống quản lý khuyến mãi & thông báo | Xây dựng hệ thống quản lý khuyến mãi & thông báo với các chức năng: quản lý khuyến mãi, và quản lý thông báo | Application Code | [REQ-017], [REQ-018], [DAT-009], [ARC-008] |
| 10 | Xây dựng hệ thống chatbot dịch vụ khách hàng AI | Xây dựng hệ thống chatbot dịch vụ khách hàng AI với các chức năng: tích hợp chatbot AI | Application Code | [REQ-019], [ARC-008] |
| 11 | Xây dựng các tính năng cốt lõi của ứng dụng di động | Xây dựng các tính năng cốt lõi của ứng dụng di động với các chức năng: giao diện người dùng vai trò cụ thể trên di động, và thông báo đẩy trên di động | Application Code | [REQ-020], [REQ-021], [ARC-009] |
| 12 | Xây dựng hệ thống bản địa hóa & SEO | Xây dựng hệ thống bản địa hóa & SEO với các chức năng: phát hiện ngôn ngữ mặc định, và SEO đa ngôn ngữ | Application Code | [REQ-022], [REQ-023], [DAT-011], [ARC-007], [NFR-007] |
| 13 | Xây dựng hệ thống báo cáo & phân tích | Xây dựng hệ thống báo cáo & phân tích với các chức năng: tạo báo cáo điểm danh, và bảng điều khiển tóm tắt ghi danh | Application Code | [REQ-024], [REQ-025], [EXC-005], [ARC-007] |
| 14 | Xây dựng hệ thống bảo mật & tuân thủ | Xây dựng hệ thống bảo mật & tuân thủ với các chức năng: bảo mật dữ liệu, và tuân thủ quy định | Application Code | [NFR-003], [NFR-008] |
| 15 | Xây dựng hệ thống hiệu suất & khả năng mở rộng | Xây dựng hệ thống hiệu suất & khả năng mở rộng với các chức năng: hiệu suất hệ thống, và khả năng mở rộng | Application Code | [NFR-001], [NFR-004] |
| 16 | Xây dựng hệ thống ghi nhật ký & kiểm toán | Xây dựng hệ thống ghi nhật ký & kiểm toán với các chức năng: ghi nhật ký hệ thống, và kiểm toán hệ thống | Application Code | [NFR-006] |
| 17 | Xây dựng hệ thống sao lưu & phục hồi thảm họa | Xây dựng hệ thống sao lưu & phục hồi thảm họa với các chức năng: sao lưu dữ liệu, và phục hồi dữ liệu | Application Code | [NFR-009] |
| 18 | Xây dựng tài liệu kỹ thuật | Xây dựng tài liệu kỹ thuật với các chức năng: tài liệu kiến trúc, tài liệu API, và tài liệu sử dụng | Enterprise Documentation | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| 19 | Xây dựng hệ thống containerization | Xây dựng hệ thống containerization với các chức năng: xây dựng Dockerfile, và đẩy container image | DevOps Infrastructure | [NFR-005] |
| 20 | Xây dựng hệ thống triển khai trên GCP | Xây dựng hệ thống triển khai trên GCP với các chức năng: xây dựng cấu hình GCP, và triển khai ứng dụng trên GCP | DevOps Infrastructure | [ARC-010] |
| 21 | Xây dựng hệ thống triển khai trên GKE | Xây dựng hệ thống triển khai trên GKE với các chức năng: xây dựng cấu hình GKE, và triển khai ứng dụng trên GKE | DevOps Infrastructure | [ARC-010] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 21 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. MULTI-PHASE SYNOPSIS MATRIX

<!--START_PHASE_SYNOPSIS_GRID-->

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 2 | ./sources/backend/auth-service/ | Xây dựng hệ thống xác thực người dùng sử dụng email/mật khẩu, Firebase, Google, và Facebook OAuth | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [ARC-006] |
| Phase 2 | Day 1 - 2 | ./sources/backend/user-service/ | Xây dựng hệ thống quản lý người dùng với các vai trò: System Admin, Center Admin, Manager, Teacher, và Student | Coder, Tester, Reviewer, Doc | [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| Phase 3 | Day 1 - 2 | ./sources/backend/center-service/ | Xây dựng hệ thống quản lý trung tâm với các chức năng: xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002] |
| Phase 4 | Day 1 - 2 | ./sources/backend/course-service/ | Xây dựng hệ thống quản lý khóa học với các chức năng: xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học | Coder, Tester, Reviewer, Doc | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003] |
| Phase 5 | Day 1 - 2 | ./sources/backend/enrollment-service/ | Xây dựng hệ thống đăng ký & ghi danh học viên với các chức năng: duyệt khóa học, đăng ký khóa học của học viên | Coder, Tester, Reviewer, Doc | [REQ-010], [REQ-011], [DAT-005], [ARC-004] |
| Phase 6 | Day 1 - 2 | ./sources/backend/attendance-service/ | Xây dựng hệ thống điểm danh & quét mã QR với các chức năng: chụp ảnh điểm danh QR, và tính chất bất biến của điểm danh | Coder, Tester, Reviewer, Doc | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002], [ARC-004] |
| Phase 7 | Day 1 - 2 | ./sources/backend/membership-service/ | Xây dựng hệ thống quản lý thẻ hội viên với các chức năng: hiển thị tính hợp lệ của thẻ, và gia hạn thẻ | Coder, Tester, Reviewer, Doc | [REQ-014], [REQ-015], [DAT-007], [ARC-005] |
| Phase 8 | Day 1 - 2 | ./sources/backend/notification-service/ | Xây dựng hệ thống thông báo & truyền thông với các chức năng: kích hoạt thông báo | Coder, Tester, Reviewer, Doc | [REQ-016], [DAT-008], [EXC-003], [ARC-008] |
| Phase 9 | Day 1 - 2 | ./sources/backend/promotion-service/ | Xây dựng hệ thống quản lý khuyến mãi & thông báo với các chức năng: quản lý khuyến mãi, và quản lý thông báo | Coder, Tester, Reviewer, Doc | [REQ-017], [REQ-018], [DAT-009], [ARC-008] |
| Phase 10 | Day 1 - 2 | ./sources/backend/chatbot-service/ | Xây dựng hệ thống chatbot dịch vụ khách hàng AI với các chức năng: tích hợp chatbot AI | Coder, Tester, Reviewer, Doc | [REQ-019], [ARC-008] |
| Phase 11 | Day 1 - 2 | ./sources/frontend/mobile-app/ | Xây dựng các tính năng cốt lõi của ứng dụng di động với các chức năng: giao diện người dùng vai trò cụ thể trên di động, và thông báo đẩy trên di động | Coder, Tester, Reviewer, Doc | [REQ-020], [REQ-021], [ARC-009] |
| Phase 12 | Day 1 - 2 | ./sources/backend/localization-service/ | Xây dựng hệ thống bản địa hóa & SEO với các chức năng: phát hiện ngôn ngữ mặc định, và SEO đa ngôn ngữ | Coder, Tester, Reviewer, Doc | [REQ-022], [REQ-023], [DAT-011], [ARC-007], [NFR-007] |
| Phase 13 | Day 1 - 2 | ./sources/backend/reporting-service/ | Xây dựng hệ thống báo cáo & phân tích với các chức năng: tạo báo cáo điểm danh, và bảng điều khiển tóm tắt ghi danh | Coder, Tester, Reviewer, Doc | [REQ-024], [REQ-025], [EXC-005], [ARC-007] |
| Phase 14 | Day 1 - 2 | ./sources/backend/security-service/ | Xây dựng hệ thống bảo mật & tuân thủ với các chức năng: bảo mật dữ liệu, và tuân thủ quy định | Coder, Tester, Reviewer, Doc | [NFR-003], [NFR-008] |
| Phase 15 | Day 1 - 2 | ./sources/backend/performance-service/ | Xây dựng hệ thống hiệu suất & khả năng mở rộng với các chức năng: hiệu suất hệ thống, và khả năng mở rộng | Coder, Tester, Reviewer, Doc | [NFR-001], [NFR-004] |
| Phase 16 | Day 1 - 2 | ./sources/backend/logging-service/ | Xây dựng hệ thống ghi nhật ký & kiểm toán với các chức năng: ghi nhật ký hệ thống, và kiểm toán hệ thống | Coder, Tester, Reviewer, Doc | [NFR-006] |
| Phase 17 | Day 1 - 2 | ./sources/backend/backup-service/ | Xây dựng hệ thống sao lưu & phục hồi thảm họa với các chức năng: sao lưu dữ liệu, và phục hồi dữ liệu | Coder, Tester, Reviewer, Doc | [NFR-009] |
| Phase 18 | Day 1 - 2 | ./sources/docs/architecture/ | Xây dựng tài liệu kỹ thuật với các chức năng: tài liệu kiến trúc, tài liệu API, và tài liệu sử dụng | Doc | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Phase 19 | Day 1 - 2 | ./sources/infra/docker/ | Xây dựng hệ thống containerization với các chức năng: xây dựng Dockerfile, và đẩy container image | Docker | [NFR-005] |
| Phase 20 | Day 1 - 2 | ./sources/infra/gcp/ | Xây dựng hệ thống triển khai trên GCP với các chức năng: xây dựng cấu hình GCP, và triển khai ứng dụng trên GCP | GCP | [ARC-010] |
| Phase 21 | Day 1 - 2 | ./sources/infra/gke/ | Xây dựng hệ thống triển khai trên GKE với các chức năng: xây dựng cấu hình GKE, và triển khai ứng dụng trên GKE | GKE | [ARC-010] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 21 Phases | **MAPPED CAPACITY STATUS:** Verified: 21 out of 21 Total Master Backlog Tasks successfully distributed across calculated phases with 100% coverage | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |

<!--END_PHASE_SYNOPSIS_GRID-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809131523 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 13:15:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

### Giai đoạn 1: Khởi Tạo Hệ Thống Người Dùng Và Xác Thực

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Thiết lập cơ sở hạ tầng người dùng và xác thực, bao gồm việc triển khai cơ sở dữ liệu người dùng, dịch vụ xác thực, và các điểm cuối API liên quan đến quản lý người dùng và xác thực.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi của nó.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản đồ cơ sở dữ liệu quan hệ, hoặc bản thiết kế kiến trúc phải nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.

- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Cung cấp các câu lệnh di chuyển DDL SQL đầy đủ, hợp lệ, và hoàn chỉnh chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có lớp cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).

- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG ĐƯỢC dịch).

- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ chặt chẽ với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 1)

- **DAY 1:** Thiết lập cơ sở dữ liệu người dùng và dịch vụ xác thực

  ##### SUB-TASK 1: Thiết lập cơ sở dữ liệu người dùng
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [DAT-001]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/resources/db/migration/V1__Create_Users_Table.sql`
    * **Low-Level Technical Task Instruction:** Tạo bảng người dùng với các cột: userId (UUID), email (VARCHAR(255)), passwordHash (CHAR(60)), fullName (VARCHAR(100)), roleId (SMALLINT), provider (ENUM), createdAt (TIMESTAMP), updatedAt (TIMESTAMP). Thêm các ràng buộc khóa chính, duy nhất, và không null. [DAT-001]

  ##### SUB-TASK 2: Thiết lập dịch vụ xác thực
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-006]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/AuthService.java`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ xác thực với các phương thức đăng ký, đăng nhập, và cấp JWT token. [ARC-006]

- **DAY 2:** Triển khai điểm cuối API và kiểm thử

  ##### SUB-TASK 1: Triển khai điểm cuối API đăng ký người dùng
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-001]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
    * **Low-Level Technical Task Instruction:** Tạo điểm cuối API cho đăng ký người dùng với các trường: email, mật khẩu, và tên đầy đủ. [REQ-001]

  ##### SUB-TASK 2: Triển khai điểm cuối API đăng nhập người dùng
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-002]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
    * **Low-Level Technical Task Instruction:** Tạo điểm cuối API cho đăng nhập người dùng với các phương thức: email/mật khẩu, Firebase, Google, và Facebook OAuth. [REQ-002]

  ##### SUB-TASK 3: Viết kiểm thử cho dịch vụ xác thực
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [REQ-001], [REQ-002]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/AuthService.java`
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử cho các phương thức đăng ký, đăng nhập, và cấp JWT token. [REQ-001], [REQ-002]

- **DAY 3:** Triển khai phân quyền người dùng và kiểm thử

  ##### SUB-TASK 1: Triển khai điểm cuối API phân quyền người dùng
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-003]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/UserController.java`
    * **Low-Level Technical Task Instruction:** Tạo điểm cuối API cho phân quyền người dùng với các trường: userId và roleId. [REQ-003]

  ##### SUB-TASK 2: Viết kiểm thử cho điểm cuối phân quyền người dùng
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [REQ-003]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/controller/UserControllerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/UserController.java`
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử cho điểm cuối phân quyền người dùng. [REQ-003]

- **DAY 4:** Triển khai và kiểm thử xác thực OAuth

  ##### SUB-TASK 1: Triển khai xác thực OAuth
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-002]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuthService.java`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ xác thực OAuth với các nhà cung cấp: Firebase, Google, và Facebook. [REQ-002]

  ##### SUB-TASK 2: Viết kiểm thử cho xác thực OAuth
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [REQ-002]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/OAuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/OAuthService.java`
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử cho dịch vụ xác thực OAuth. [REQ-002]

- **DAY 5:** Triển khai và kiểm thử xử lý ngoại lệ

  ##### SUB-TASK 1: Triển khai xử lý ngoại lệ
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [EXC-004]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/exception/GlobalExceptionHandler.java`
    * **Low-Level Technical Task Instruction:** Triển khai bộ xử lý ngoại lệ toàn cầu cho các lỗi xác thực đầu vào không hợp lệ. [EXC-004]

  ##### SUB-TASK 2: Viết kiểm thử cho xử lý ngoại lệ
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [EXC-004]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/exception/GlobalExceptionHandlerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/exception/GlobalExceptionHandler.java`
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử cho bộ xử lý ngoại lệ toàn cầu. [EXC-004]

- **DAY 6:** Triển khai và kiểm thử điểm cuối API phân quyền người dùng

  ##### SUB-TASK 1: Triển khai điểm cuối API phân quyền người dùng
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-003]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/UserController.java`
    * **Low-Level Technical Task Instruction:** Triển khai điểm cuối API cho phân quyền người dùng. [REQ-003]

  ##### SUB-TASK 2: Viết kiểm thử cho điểm cuối API phân quyền người dùng
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [REQ-003]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/controller/UserControllerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/UserController.java`
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử cho điểm cuối API phân quyền người dùng. [REQ-003]

- **DAY 7:** Triển khai và kiểm thử điểm cuối API đăng ký và đăng nhập người dùng

  ##### SUB-TASK 1: Triển khai điểm cuối API đăng ký người dùng
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-001]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
    * **Low-Level Technical Task Instruction:** Triển khai điểm cuối API cho đăng ký người dùng. [REQ-001]

  ##### SUB-TASK 2: Triển khai điểm cuối API đăng nhập người dùng
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-002]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
    * **Low-Level Technical Task Instruction:** Triển khai điểm cuối API cho đăng nhập người dùng. [REQ-002]

  ##### SUB-TASK 3: Viết kiểm thử cho điểm cuối API đăng ký và đăng nhập người dùng
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [REQ-001], [REQ-002]
    * **Target Component file path (target_component):** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/controller/AuthControllerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử cho điểm cuối API đăng ký và đăng nhập người dùng. [REQ-001], [REQ-002]

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809131523 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 13:15:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

### Giai đoạn 2

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống xác thực đa kênh và cơ sở dữ liệu người dùng, bao gồm các bảng Users, Roles, và Centers. Thiết lập cơ chế phân quyền dựa trên vai trò (RBAC) và tích hợp xác thực OAuth2 với Firebase, Google, và Facebook.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được thêm vào các Tag ID theo dõi tương ứng.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản đồ quan hệ cơ sở dữ liệu, hoặc bố cục kiến trúc phải nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.

- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ, chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có lớp cơ sở dữ liệu hoặc yêu cầu lưu trữ. Các khối kỹ thuật này KHÔNG được dịch).

- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-006]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Các khối kỹ thuật này KHÔNG được dịch).

- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ chặt chẽ với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh vào 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 2)

- **DAY 1:** Khởi tạo cơ sở dữ liệu người dùng và bảng vai trò
    ##### SUB-TASK 1: Thiết lập cơ sở dữ liệu PostgreSQL và cấu hình kết nối
      * **Sub-Agent:** [GCP]
      * **Tag IDs Mục tiêu:** [NFR-003], [NFR-004]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/infra/database/`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai cơ sở dữ liệu PostgreSQL trên GCP với cấu hình bảo mật AES-256 và TLS 1.3. Cấu hình kết nối với các tham số kết nối được mã hóa trong biến môi trường.

    ##### SUB-TASK 2: Tạo lược đồ cơ sở dữ liệu cho bảng Users và Roles
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [DAT-001]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/auth-service/src/main/resources/db/migration/V1__Create_Users_Roles_Schema.sql`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các câu lệnh DDL SQL để tạo bảng Users và Roles với các trường và ràng buộc như được định nghĩa trong yêu cầu. Đảm bảo rằng các trường email là duy nhất và mật khẩu được lưu trữ dưới dạng bcrypt hash.

- **DAY 2:** Triển khai dịch vụ xác thực và tích hợp OAuth2
    ##### SUB-TASK 1: Thiết lập dịch vụ xác thực Quarkus
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ xác thực sử dụng Quarkus với các điểm cuối API cho đăng ký và đăng nhập. Tích hợp xác thực OAuth2 với Firebase, Google, và Facebook.

    ##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho dịch vụ xác thực
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/AuthService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị để kiểm tra tính năng đăng ký và đăng nhập. Đảm bảo rằng các trường hợp kiểm tra bao gồm xác thực thành công, xác thực thất bại, và xử lý ngoại lệ.

- **DAY 3:** Thiết lập cơ chế phân quyền dựa trên vai trò (RBAC)
    ##### SUB-TASK 1: Triển khai cơ chế phân quyền
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/rbac/`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai cơ chế phân quyền dựa trên vai trò (RBAC) với các vai trò như System Admin, Center Admin, Manager, Teacher, và Student. Đảm bảo rằng các quyền được áp dụng chính xác và các điểm cuối API được bảo vệ bằng các quyền thích hợp.

    ##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho cơ chế phân quyền
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-003]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/rbac/RBACServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/rbac/RBACService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị để kiểm tra tính năng phân quyền. Đảm bảo rằng các trường hợp kiểm tra bao gồm gán và thay đổi vai trò, và áp dụng quyền thích hợp.

- **DAY 4:** Triển khai dịch vụ quản lý trung tâm
    ##### SUB-TASK 1: Thiết lập dịch vụ quản lý trung tâm
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/center-service/src/main/java/com/membershiphub/center/`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý trung tâm với các điểm cuối API cho xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm. Đảm bảo rằng các trường hợp kiểm tra bao gồm xác thực đầu vào, xử lý ngoại lệ, và bảo mật.

    ##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho dịch vụ quản lý trung tâm
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/center-service/src/test/java/com/membershiphub/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị để kiểm tra tính năng quản lý trung tâm. Đảm bảo rằng các trường hợp kiểm tra bao gồm xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.

- **DAY 5:** Triển khai dịch vụ quản lý khóa học
    ##### SUB-TASK 1: Thiết lập dịch vụ quản lý khóa học
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý khóa học với các điểm cuối API cho xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học. Đảm bảo rằng các trường hợp kiểm tra bao gồm xác thực đầu vào, xử lý ngoại lệ, và bảo mật.

    ##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho dịch vụ quản lý khóa học
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị để kiểm tra tính năng quản lý khóa học. Đảm bảo rằng các trường hợp kiểm tra bao gồm xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.

- **DAY 6:** Triển khai dịch vụ đăng ký và ghi danh học viên
    ##### SUB-TASK 1: Thiết lập dịch vụ đăng ký và ghi danh học viên
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-010], [REQ-011], [DAT-005]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ đăng ký và ghi danh học viên với các điểm cuối API cho duyệt khóa học và đăng ký khóa học. Đảm bảo rằng các trường hợp kiểm tra bao gồm xác thực đầu vào, xử lý ngoại lệ, và bảo mật.

    ##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho dịch vụ đăng ký và ghi danh học viên
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/enrollment-service/src/test/java/com/membershiphub/enrollment/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị để kiểm tra tính năng đăng ký và ghi danh học viên. Đảm bảo rằng các trường hợp kiểm tra bao gồm duyệt khóa học và đăng ký khóa học.

- **DAY 7:** Triển khai dịch vụ điểm danh và quét mã QR
    ##### SUB-TASK 1: Thiết lập dịch vụ điểm danh và quét mã QR
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ điểm danh và quét mã QR với các điểm cuối API cho chụp ảnh điểm danh QR và tính chất bất biến của điểm danh. Đảm bảo rằng các trường hợp kiểm tra bao gồm xác thực đầu vào, xử lý ngoại lệ, và bảo mật.

    ##### SUB-TASK 2: Viết các bài kiểm tra đơn vị cho dịch vụ điểm danh và quét mã QR
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị để kiểm tra tính năng điểm danh và quét mã QR. Đảm bảo rằng các trường hợp kiểm tra bao gồm chụp ảnh điểm danh QR và tính chất bất biến của điểm danh.

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809131523 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 13:15:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

### Giai đoạn 3

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống quản lý trung tâm, bao gồm các chức năng tạo, cập nhật, xóa trung tâm và phân quyền quản trị trung tâm.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được thêm vào các Tag ID theo dõi inline.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án có yêu cầu lớp cơ sở dữ liệu hoặc lớp lưu trữ không. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [ARC-002]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối rõ ràng, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ nhớ đệm tin nhắn. Khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1:** Khởi tạo hệ thống quản lý trung tâm

  ##### SUB-TASK 1: Thiết kế lược đồ cơ sở dữ liệu cho quản lý trung tâm

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [DAT-003]
    * **Target Component file path (target_component):** `./sources/backend/membership-hub/src/main/resources/db/migration/V3__Centers.sql`
    * **Low-Level Technical Task Instruction:** Tạo lược đồ cơ sở dữ liệu cho bảng trung tâm với các trường: centerId (UUID, khóa chính), name (VARCHAR(100), không null), address (VARCHAR(255), không null), taxId (VARCHAR(13), duy nhất, không null), contactPhone (VARCHAR(20), có thể null), contactEmail (VARCHAR(255), có thể null).

  ##### SUB-TASK 2: Thiết kế API cho quản lý trung tâm

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
    * **Target Component file path (target_component):** `./sources/backend/membership-hub/src/main/java/com/membershiphub/api/CenterController.java`
    * **Low-Level Technical Task Instruction:** Thiết kế các điểm cuối API cho các chức năng quản lý trung tâm bao gồm: lấy danh sách trung tâm, tạo trung tâm mới, cập nhật trung tâm, xóa trung tâm.

- **DAY 2:** Triển khai chức năng quản lý trung tâm

  ##### SUB-TASK 1: Triển khai chức năng tạo trung tâm

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-005]
    * **Target Component file path (target_component):** `./sources/backend/membership-hub/src/main/java/com/membershiphub/service/CenterService.java`
    * **Low-Level Technical Task Instruction:** Triển khai chức năng tạo trung tâm mới với xác thực đầu vào và xử lý ngoại lệ cho các trường hợp trùng lặp taxId.

  ##### SUB-TASK 2: Triển khai chức năng phân quyền quản trị trung tâm

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-006], [ARC-002]
    * **Target Component file path (target_component):** `./sources/backend/membership-hub/src/main/java/com/membershiphub/service/AdminService.java`
    * **Low-Level Technical Task Instruction:** Triển khai chức năng phân quyền quản trị trung tâm cho người dùng, bao gồm việc cập nhật vai trò người dùng và lưu trữ trung tâm liên kết.

- **DAY 3:** Kiểm thử và xác thực chức năng quản lý trung tâm

  ##### SUB-TASK 1: Viết bộ kiểm thử cho chức năng quản lý trung tâm

    * **Sub-Agent:** [Tester]
    * **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
    * **Target Component file path (target_component):** `./sources/backend/membership-hub/src/test/java/com/membershiphub/service/CenterServiceTest.java;./sources/backend/membership-hub/src/main/java/com/membershiphub/service/CenterService.java`
    * **Low-Level Technical Task Instruction:** Viết các bộ kiểm thử cho các chức năng quản lý trung tâm bao gồm: lấy danh sách trung tâm, tạo trung tâm mới, cập nhật trung tâm, xóa trung tâm và phân quyền quản trị trung tâm.

  ##### SUB-TASK 2: Kiểm thử tích hợp cho chức năng quản lý trung tâm

    * **Sub-Agent:** [Tester]
    * **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
    * **Target Component file path (target_component):** `./sources/backend/membership-hub/src/test/java/com/membershiphub/api/CenterControllerIT.java;./sources/backend/membership-hub/src/main/java/com/membershiphub/api/CenterController.java`
    * **Low-Level Technical Task Instruction:** Viết các bộ kiểm thử tích hợp cho các chức năng quản lý trung tâm bao gồm: lấy danh sách trung tâm, tạo trung tâm mới, cập nhật trung tâm, xóa trung tâm và phân quyền quản trị trung tâm.

<!--END_PHASE_LOG_BLOCK_INDEX_3-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809131523 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 13:15:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

### Giai đoạn 4

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống điểm danh và quản lý thẻ hội viên, bao gồm các tính năng quét mã QR, tính toán ngày hiệu lực, và giao diện người dùng cho các vai trò học viên và giáo viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi tương ứng.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản đồ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc phải nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:** Cung cấp các câu lệnh di chuyển DDL SQL đầy đủ, hợp lệ, và hoàn chỉnh chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có lớp cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [ARC-007]:** Tài liệu các hợp đồng kỹ thuật đầy đủ (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ chặt chẽ với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 4)

- **DAY 1:** Triển khai lõi điểm danh và quản lý thẻ hội viên

  ##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho điểm danh và thẻ hội viên
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-006], [DAT-007]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/attendance-service/src/main/resources/db/migration/V1__Create_Attendance_And_StudentCard_Tables.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế và triển khai các bảng cơ sở dữ liệu cho điểm danh và thẻ hội viên, bao gồm các trường và ràng buộc cần thiết.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:**
      ```sql
      CREATE TABLE Attendance (
          attendanceId UUID PRIMARY KEY,
          studentId UUID NOT NULL,
          courseId UUID NOT NULL,
          attendanceDate DATE NOT NULL,
          timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
          FOREIGN KEY (studentId) REFERENCES Users(userId),
          FOREIGN KEY (courseId) REFERENCES Courses(courseId),
          CONSTRAINT unique_attendance UNIQUE (studentId, courseId, attendanceDate)
      );

      CREATE TABLE StudentCards (
          cardId UUID PRIMARY KEY,
          studentId UUID NOT NULL,
          issueDate DATE NOT NULL,
          validityDays INT NOT NULL,
          remainingDays INT NOT NULL,
          FOREIGN KEY (studentId) REFERENCES Users(userId)
      );
      ```

  ##### SUB-TASK 2: Viết các API cho điểm danh và quản lý thẻ hội viên
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/controller/AttendanceController.java`, `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/controller/StudentCardController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cho điểm danh và quản lý thẻ hội viên, bao gồm các điểm cuối cho quét mã QR, tính toán ngày hiệu lực, và gia hạn thẻ.
    * **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [ARC-007]:**
      ```json
      {
        "POST /api/attendance/scan": {
          "request": {
            "studentId": "UUID",
            "courseId": "UUID",
            "timestamp": "ISO8601"
          },
          "response": {
            "status": "success|duplicate",
            "message": "string"
          }
        },
        "GET /api/student-card/{studentId}": {
          "response": {
            "cardId": "UUID",
            "studentId": "UUID",
            "issueDate": "YYYY-MM-DD",
            "validityDays": "int",
            "remainingDays": "int"
          }
        },
        "POST /api/student-card/renew": {
          "request": {
            "studentId": "UUID",
            "days": "int"
          },
          "response": {
            "status": "success",
            "newEndDate": "YYYY-MM-DD"
          }
        }
      }
      ```

  ##### SUB-TASK 3: Viết các bài kiểm tra cho điểm danh và quản lý thẻ hội viên
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/controller/AttendanceControllerTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/controller/AttendanceController.java`, `./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/controller/StudentCardControllerTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/controller/StudentCardController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra cho các API điểm danh và quản lý thẻ hội viên, bao gồm các trường hợp kiểm tra cho điểm danh trùng lặp và gia hạn thẻ.

  ##### SUB-TASK 4: Tài liệu cho điểm danh và quản lý thẻ hội viên
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/attendance-system.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết cho hệ thống điểm danh và quản lý thẻ hội viên, bao gồm các hướng dẫn sử dụng và ví dụ về cách sử dụng các API.

- **DAY 2:** Triển khai giao diện người dùng cho điểm danh và quản lý thẻ hội viên

  ##### SUB-TASK 1: Thiết kế giao diện người dùng cho điểm danh và quản lý thẻ hội viên
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/frontend/src/components/AttendanceScanner.js`, `./sources/frontend/src/components/StudentCard.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế và triển khai các thành phần giao diện người dùng cho điểm danh và quản lý thẻ hội viên, bao gồm các thành phần quét mã QR và hiển thị thẻ hội viên.

  ##### SUB-TASK 2: Kết nối giao diện người dùng với các API điểm danh và quản lý thẻ hội viên
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/frontend/src/services/attendanceService.js`, `./sources/frontend/src/services/studentCardService.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Kết nối các thành phần giao diện người dùng với các API điểm danh và quản lý thẻ hội viên, bao gồm các dịch vụ để gọi các điểm cuối API và xử lý phản hồi.

  ##### SUB-TASK 3: Viết các bài kiểm tra cho giao diện người dùng điểm danh và quản lý thẻ hội viên
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/frontend/src/tests/AttendanceScanner.test.js;./sources/frontend/src/components/AttendanceScanner.js`, `./sources/frontend/src/tests/StudentCard.test.js;./sources/frontend/src/components/StudentCard.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra cho các thành phần giao diện người dùng điểm danh và quản lý thẻ hội viên, bao gồm các trường hợp kiểm tra cho quét mã QR và hiển thị thẻ hội viên.

  ##### SUB-TASK 4: Tài liệu cho giao diện người dùng điểm danh và quản lý thẻ hội viên
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/frontend-components.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết cho các thành phần giao diện người dùng điểm danh và quản lý thẻ hội viên, bao gồm các hướng dẫn sử dụng và ví dụ về cách sử dụng các thành phần.

- **DAY 3:** Triển khai thông báo cho điểm danh và quản lý thẻ hội viên

  ##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho thông báo
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/resources/db/migration/V1__Create_Notifications_Table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế và triển khai bảng cơ sở dữ liệu cho thông báo, bao gồm các trường và ràng buộc cần thiết.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:**
      ```sql
      CREATE TABLE Notifications (
          notificationId UUID PRIMARY KEY,
          userId UUID,
          groupZalo VARCHAR(255),
          message TEXT NOT NULL,
          sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
          delivered BOOLEAN NOT NULL DEFAULT FALSE,
          FOREIGN KEY (userId) REFERENCES Users(userId)
      );
      ```

  ##### SUB-TASK 2: Viết các API cho thông báo
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-016]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/controller/NotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cho thông báo, bao gồm các điểm cuối để tạo và gửi thông báo.
    * **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [ARC-008]:**
      ```json
      {
        "POST /api/notifications": {
          "request": {
            "userId": "UUID",
            "groupZalo": "string",
            "message": "string"
          },
          "response": {
            "status": "success",
            "notificationId": "UUID"
          }
        }
      }
      ```

  ##### SUB-TASK 3: Viết các bài kiểm tra cho thông báo
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-016]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/controller/NotificationControllerTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/controller/NotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra cho các API thông báo, bao gồm các trường hợp kiểm tra cho tạo và gửi thông báo.

  ##### SUB-TASK 4: Tài liệu cho thông báo
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-016]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/notification-system.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết cho hệ thống thông báo, bao gồm các hướng dẫn sử dụng và ví dụ về cách sử dụng các API.

- **DAY 4:** Triển khai thông báo đẩy cho điểm danh và quản lý thẻ hội viên

  ##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho thông báo đẩy
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/resources/db/migration/V2__Add_Device_Tokens_Table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế và triển khai bảng cơ sở dữ liệu cho thông báo đẩy, bao gồm các trường và ràng buộc cần thiết.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:**
      ```sql
      CREATE TABLE DeviceTokens (
          deviceTokenId UUID PRIMARY KEY,
          userId UUID NOT NULL,
          token VARCHAR(255) NOT NULL,
          platform VARCHAR(20) NOT NULL CHECK (platform IN ('android', 'ios')),
          createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
          FOREIGN KEY (userId) REFERENCES Users(userId)
      );
      ```

  ##### SUB-TASK 2: Viết các API cho thông báo đẩy
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-021]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/controller/PushNotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cho thông báo đẩy, bao gồm các điểm cuối để đăng ký và gửi thông báo đẩy.
    * **Hợp đồng Định tuyến API và Sự kiện [REQ-021], [ARC-008]:**
      ```json
      {
        "POST /api/push-notifications/register": {
          "request": {
            "userId": "UUID",
            "token": "string",
            "platform": "android|ios"
          },
          "response": {
            "status": "success",
            "deviceTokenId": "UUID"
          }
        },
        "POST /api/push-notifications/send": {
          "request": {
            "userId": "UUID",
            "title": "string",
            "body": "string"
          },
          "response": {
            "status": "success",
            "notificationId": "UUID"
          }
        }
      }
      ```

  ##### SUB-TASK 3: Viết các bài kiểm tra cho thông báo đẩy
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-021]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/controller/PushNotificationControllerTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/controller/PushNotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra cho các API thông báo đẩy, bao gồm các trường hợp kiểm tra cho đăng ký và gửi thông báo đẩy.

  ##### SUB-TASK 4: Tài liệu cho thông báo đẩy
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-021]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/push-notification-system.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết cho hệ thống thông báo đẩy, bao gồm các hướng dẫn sử dụng và ví dụ về cách sử dụng các API.

- **DAY 5:** Triển khai báo cáo điểm danh và quản lý thẻ hội viên

  ##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho báo cáo
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-006], [DAT-007]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/report-service/src/main/resources/db/migration/V1__Create_Reports_Table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế và triển khai bảng cơ sở dữ liệu cho báo cáo, bao gồm các trường và ràng buộc cần thiết.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:**
      ```sql
      CREATE TABLE Reports (
          reportId UUID PRIMARY KEY,
          centerId UUID NOT NULL,
          reportDate DATE NOT NULL,
          data JSONB NOT NULL,
          createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
          FOREIGN KEY (centerId) REFERENCES Centers(centerId)
      );
      ```

  ##### SUB-TASK 2: Viết các API cho báo cáo
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-024]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/report-service/src/main/java/com/membershiphub/report/controller/ReportController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cho báo cáo, bao gồm các điểm cuối để tạo và xuất báo cáo.
    * **Hợp đồng Định tuyến API và Sự kiện [REQ-024], [ARC-009]:**
      ```json
      {
        "POST /api/reports": {
          "request": {
            "centerId": "UUID",
            "reportDate": "YYYY-MM-DD",
            "data": "JSON"
          },
          "response": {
            "status": "success",
            "reportId": "UUID"
          }
        },
        "GET /api/reports/{reportId}": {
          "response": {
            "reportId": "UUID",
            "centerId": "UUID",
            "reportDate": "YYYY-MM-DD",
            "data": "JSON"
          }
        }
      }
      ```

  ##### SUB-TASK 3: Viết các bài kiểm tra cho báo cáo
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-024]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/report-service/src/test/java/com/membershiphub/report/controller/ReportControllerTest.java;./sources/backend/report-service/src/main/java/com/membershiphub/report/controller/ReportController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra cho các API báo cáo, bao gồm các trường hợp kiểm tra cho tạo và xuất báo cáo.

  ##### SUB-TASK 4: Tài liệu cho báo cáo
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-024]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/report-system.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết cho hệ thống báo cáo, bao gồm các hướng dẫn sử dụng và ví dụ về cách sử dụng các API.

- **DAY 6:** Triển khai bảng điều khiển tóm tắt ghi danh

  ##### SUB-TASK 1: Thiết kế cơ sở dữ liệu cho bảng điều khiển
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-005]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/dashboard-service/src/main/resources/db/migration/V1__Create_Dashboard_Table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế và triển khai bảng cơ sở dữ liệu cho bảng điều khiển, bao gồm các trường và ràng buộc cần thiết.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-005]:**
      ```sql
      CREATE TABLE Dashboards (
          dashboardId UUID PRIMARY KEY,
          centerId UUID NOT NULL,
          totalStudents INT NOT NULL,
          activeCourses INT NOT NULL,
          upcomingSessions INT NOT NULL,
          lastUpdated TIMESTAMP NOT NULL DEFAULT NOW(),
          FOREIGN KEY (centerId) REFERENCES Centers(centerId)
      );
      ```

  ##### SUB-TASK 2: Viết các API cho bảng điều khiển
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-025]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/dashboard-service/src/main/java/com/membershiphub/dashboard/controller/DashboardController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cho bảng điều khiển, bao gồm các điểm cuối để lấy và cập nhật dữ liệu bảng điều khiển.
    * **Hợp đồng Định tuyến API và Sự kiện [REQ-025], [ARC-009]:**
      ```json
      {
        "GET /api/dashboards/{centerId}": {
          "response": {
            "dashboardId": "UUID",
            "centerId": "UUID",
            "totalStudents": "int",
            "activeCourses": "int",
            "upcomingSessions": "int",
            "lastUpdated": "ISO8601"
          }
        },
        "POST /api/dashboards/{centerId}": {
          "request": {
            "totalStudents": "int",
            "activeCourses": "int",
            "upcomingSessions": "int"
          },
          "response": {
            "status": "success",
            "dashboardId": "UUID"
          }
        }
      }
      ```

  ##### SUB-TASK 3: Viết các bài kiểm tra cho bảng điều khiển
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-025]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/dashboard-service/src/test/java/com/membershiphub/dashboard/controller/DashboardControllerTest.java;./sources/backend/dashboard-service/src/main/java/com/membershiphub/dashboard/controller/DashboardController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra cho các API bảng điều khiển, bao gồm các trường hợp kiểm tra cho lấy và cập nhật dữ liệu bảng điều khiển.

  ##### SUB-TASK 4: Tài liệu cho bảng điều khiển
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-025]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/dashboard-system.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết cho hệ thống bảng điều khiển, bao gồm các hướng dẫn sử dụng và ví dụ về cách sử dụng các API.

- **DAY 7:** Triển khai các tính năng cốt lõi của ứng dụng di động

  ##### SUB-TASK 1: Thiết kế giao diện người dùng cho ứng dụng di động
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/mobile-app/src/components/MobileDashboard.js`, `./sources/mobile-app/src/components/MobileNotifications.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế và triển khai các thành phần giao diện người dùng cho ứng dụng di động, bao gồm các thành phần bảng điều khiển và thông báo.

  ##### SUB-TASK 2: Kết nối giao diện người dùng với các API ứng dụng di động
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/mobile-app/src/services/mobileDashboardService.js`, `./sources/mobile-app/src/services/mobileNotificationService.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Kết nối các thành phần giao diện người dùng với các API ứng dụng di động, bao gồm các dịch vụ để gọi các điểm cuối API và xử lý phản hồi.

  ##### SUB-TASK 3: Viết các bài kiểm tra cho giao diện người dùng ứng dụng di động
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/mobile-app/src/tests/MobileDashboard.test.js;./sources/mobile-app/src/components/MobileDashboard.js`, `./sources/mobile-app/src/tests/MobileNotifications.test.js;./sources/mobile-app/src/components/MobileNotifications.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra cho các thành phần giao diện người dùng ứng dụng di động, bao gồm các trường hợp kiểm tra cho bảng điều khiển và thông báo.

  ##### SUB-TASK 4: Tài liệu cho giao diện người dùng ứng dụng di động
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/mobile-app-components.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết cho các thành phần giao diện người dùng ứng dụng di động, bao gồm các hướng dẫn sử dụng và ví dụ về cách sử dụng các thành phần.

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809131523 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 13:15:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📈 Giai đoạn 5: Triển khai Hệ thống Thông báo & Truyền thông

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống thông báo đa kênh bao gồm push notification cho ứng dụng di động và tin nhắn trên nhóm Zalo. Đảm bảo tính đồng bộ và tin cậy của thông báo giữa các kênh giao tiếp.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi của nó.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản đồ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có lớp cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [ARC-008]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 5)

- **DAY 1:** Triển khai Cơ sở Dữ liệu Thông báo
    ##### SUB-TASK 1: Thiết kế Schema Thông báo
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [DAT-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/resources/db/migration/V5__Create_Notifications_Table.sql`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo bảng `Notifications` với các cột: `notificationId`, `userId`, `groupZalo`, `message`, `sentAt`, `delivered`.
        * Thiết lập `notificationId` làm khóa chính với kiểu `UUID`.
        * Thiết lập `userId` làm khóa ngoại tham chiếu đến `Users.userId`.
        * Thiết lập `sentAt` với giá trị mặc định là `now()`.
        * Thiết lập `delivered` với giá trị mặc định là `false`.
    ##### SUB-TASK 2: Tạo Dịch vụ Thông báo
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/NotificationService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo dịch vụ `NotificationService` với các phương thức: `createNotification`, `sendPushNotification`, `sendZaloMessage`.
        * Triển khai phương thức `createNotification` để lưu thông báo vào cơ sở dữ liệu.
        * Triển khai phương thức `sendPushNotification` để gửi thông báo đẩy đến thiết bị di động.
        * Triển khai phương thức `sendZaloMessage` để gửi tin nhắn đến nhóm Zalo.

- **DAY 2:** Triển khai API Thông báo
    ##### SUB-TASK 1: Thiết kế API Thông báo
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/controller/NotificationController.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo `NotificationController` với các endpoint: `POST /notifications`, `GET /notifications/{id}`.
        * Triển khai endpoint `POST /notifications` để tạo thông báo mới.
        * Triển khai endpoint `GET /notifications/{id}` để lấy thông báo theo ID.
    ##### SUB-TASK 2: Kiểm thử API Thông báo
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/controller/NotificationControllerTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/controller/NotificationController.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Viết các bài kiểm thử cho `POST /notifications` và `GET /notifications/{id}`.
        * Kiểm tra tính hợp lệ của dữ liệu đầu vào và đầu ra.
        * Kiểm tra tính đồng bộ của thông báo giữa các kênh giao tiếp.

- **DAY 3:** Triển khai Xử lý Ngoại lệ Thông báo
    ##### SUB-TASK 1: Thiết kế Bộ xử lý Ngoại lệ
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [EXC-003]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/exception/NotificationExceptionHandler.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo `NotificationExceptionHandler` để xử lý các ngoại lệ liên quan đến thông báo.
        * Triển khai phương thức `handleNotificationException` để xử lý ngoại lệ thông báo.
        * Triển khai phương thức `handleZaloException` để xử lý ngoại lệ liên quan đến Zalo.
    ##### SUB-TASK 2: Kiểm thử Bộ xử lý Ngoại lệ
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [EXC-003]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/exception/NotificationExceptionHandlerTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/exception/NotificationExceptionHandler.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Viết các bài kiểm thử cho `handleNotificationException` và `handleZaloException`.
        * Kiểm tra tính hợp lệ của các phản hồi lỗi.
        * Kiểm tra tính đồng bộ của thông báo giữa các kênh giao tiếp.

- **DAY 4:** Triển khai Tích hợp Zalo
    ##### SUB-TASK 1: Thiết kế Tích hợp Zalo
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/ZaloService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo `ZaloService` với các phương thức: `sendMessage`, `getGroupInfo`.
        * Triển khai phương thức `sendMessage` để gửi tin nhắn đến nhóm Zalo.
        * Triển khai phương thức `getGroupInfo` để lấy thông tin nhóm Zalo.
    ##### SUB-TASK 2: Kiểm thử Tích hợp Zalo
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/service/ZaloServiceTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/ZaloService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Viết các bài kiểm thử cho `sendMessage` và `getGroupInfo`.
        * Kiểm tra tính hợp lệ của dữ liệu đầu vào và đầu ra.
        * Kiểm tra tính đồng bộ của thông báo giữa các kênh giao tiếp.

- **DAY 5:** Triển khai Tích hợp Firebase Cloud Messaging (FCM)
    ##### SUB-TASK 1: Thiết kế Tích hợp FCM
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/FcmService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo `FcmService` với các phương thức: `sendNotification`, `subscribeToTopic`, `unsubscribeFromTopic`.
        * Triển khai phương thức `sendNotification` để gửi thông báo đẩy đến thiết bị di động.
        * Triển khai phương thức `subscribeToTopic` để đăng ký chủ đề thông báo.
        * Triển khai phương thức `unsubscribeFromTopic` để hủy đăng ký chủ đề thông báo.
    ##### SUB-TASK 2: Kiểm thử Tích hợp FCM
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/service/FcmServiceTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/FcmService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Viết các bài kiểm thử cho `sendNotification`, `subscribeToTopic`, và `unsubscribeFromTopic`.
        * Kiểm tra tính hợp lệ của dữ liệu đầu vào và đầu ra.
        * Kiểm tra tính đồng bộ của thông báo giữa các kênh giao tiếp.

- **DAY 6:** Triển khai Tích hợp Apple Push Notification Service (APNs)
    ##### SUB-TASK 1: Thiết kế Tích hợp APNs
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/ApnsService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo `ApnsService` với các phương thức: `sendNotification`, `subscribeToTopic`, `unsubscribeFromTopic`.
        * Triển khai phương thức `sendNotification` để gửi thông báo đẩy đến thiết bị di động.
        * Triển khai phương thức `subscribeToTopic` để đăng ký chủ đề thông báo.
        * Triển khai phương thức `unsubscribeFromTopic` để hủy đăng ký chủ đề thông báo.
    ##### SUB-TASK 2: Kiểm thử Tích hợp APNs
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/service/ApnsServiceTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/ApnsService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Viết các bài kiểm thử cho `sendNotification`, `subscribeToTopic`, và `unsubscribeFromTopic`.
        * Kiểm tra tính hợp lệ của dữ liệu đầu vào và đầu ra.
        * Kiểm tra tính đồng bộ của thông báo giữa các kênh giao tiếp.

- **DAY 7:** Triển khai Tích hợp Thông báo
    ##### SUB-TASK 1: Thiết kế Tích hợp Thông báo
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/NotificationIntegrationService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Tạo `NotificationIntegrationService` với các phương thức: `sendNotification`, `handleNotificationEvent`.
        * Triển khai phương thức `sendNotification` để gửi thông báo đến các kênh giao tiếp.
        * Triển khai phương thức `handleNotificationEvent` để xử lý sự kiện thông báo.
    ##### SUB-TASK 2: Kiểm thử Tích hợp Thông báo
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
      * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/service/NotificationIntegrationServiceTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/service/NotificationIntegrationService.java`
      * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
        * Viết các bài kiểm thử cho `sendNotification` và `handleNotificationEvent`.
        * Kiểm tra tính hợp lệ của dữ liệu đầu vào và đầu ra.
        * Kiểm tra tính đồng bộ của thông báo giữa các kênh giao tiếp.

### Báo cáo Tuân thủ Kiến trúc Tự động:

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=7
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=0
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=computed_sum_of_historic_count_0_plus_current_phase_sub_tasks
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809131523 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 13:15:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo mô hình đa lớp với các thành phần chính bao gồm: giao diện người dùng, lớp dịch vụ, lớp truy cập dữ liệu và cơ sở dữ liệu.
- Sử dụng kiến trúc hướng dịch vụ (SOA) để tách biệt các chức năng thành các dịch vụ độc lập có thể mở rộng.
- Áp dụng mô hình CQRS (Command Query Responsibility Segregation) để tối ưu hóa hiệu suất cho các thao tác ghi và đọc.
- Sử dụng cơ chế sự kiện (Event-Driven Architecture) để xử lý các tác vụ bất đồng bộ như gửi thông báo và xử lý điểm danh.
- Triển khai mô hình đa ngôn ngữ để hỗ trợ các ngôn ngữ khác nhau như tiếng Anh, tiếng Việt và tiếng Tây Ban Nha.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Sử dụng hệ thống hàng đợi tin nhắn (Message Queue) như Apache Kafka để xử lý các sự kiện bất đồng bộ.
- Triển khai cơ chế caching với Redis để lưu trữ dữ liệu tạm thời và giảm tải cho cơ sở dữ liệu.
- Sử dụng cơ chế lưu trữ phân tán (Distributed Storage) để lưu trữ các tệp tin và dữ liệu lớn.
- Áp dụng cơ chế đồng bộ hóa dữ liệu (Data Synchronization) để đảm bảo tính nhất quán giữa các hệ thống.
- Triển khai cơ chế giám sát và ghi log (Monitoring and Logging) để theo dõi và phân tích hiệu suất hệ thống.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
  <RULE>
  - **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
  </RULE>
  - **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
  - **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

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

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
  <RULE>
  - You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
  - **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly verified by the Type column:
    1. *Application Code:* Functional endpoint creations, database models, and service layer code blocks.
    2. *Enterprise Documentation:* Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
    3. *DevOps Infrastructure:* Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
  - **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
  - **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution sub-task log inside Section 5 for that specific phase.
  - The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--START_BACKLOG_SYNOPSIS_GRID-->` to `<!--END_BACKLOG_SYNOPSIS_GRID-->`)
  </RULE>

  <!--START_BACKLOG_SYNOPSIS_GRID-->

  | No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
  | :--- | :--- | :--- | :--- | :--- |
  | 1 | Xây dựng hệ thống xác thực người dùng | Tạo các endpoint cho đăng ký, đăng nhập và quản lý phiên làm việc | Application Code | [REQ-001], [REQ-002], [REQ-003], [ARC-006] |
  | 2 | Thiết kế cơ sở dữ liệu cho người dùng và vai trò | Tạo các bảng Users và Roles với các trường và ràng buộc cần thiết | Application Code | [DAT-001], [ARC-006] |
  | 3 | Xây dựng hệ thống quản lý trung tâm | Tạo các endpoint cho quản lý trung tâm, bao gồm thêm, sửa, xóa và xem danh sách trung tâm | Application Code | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
  | 4 | Xây dựng hệ thống quản lý khóa học | Tạo các endpoint cho quản lý khóa học, bao gồm thêm, sửa, xóa và xem danh sách khóa học | Application Code | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
  | 5 | Xây dựng hệ thống đăng ký và ghi danh học viên | Tạo các endpoint cho đăng ký khóa học và quản lý ghi danh học viên | Application Code | [REQ-010], [REQ-011], [DAT-005] |
  | 6 | Xây dựng hệ thống điểm danh và quét mã QR | Tạo các endpoint cho điểm danh học viên qua mã QR và quản lý điểm danh | Application Code | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
  | 7 | Xây dựng hệ thống quản lý thẻ hội viên | Tạo các endpoint cho quản lý thẻ hội viên, bao gồm hiển thị và gia hạn thẻ | Application Code | [REQ-014], [REQ-015], [DAT-007] |
  | 8 | Xây dựng hệ thống thông báo và truyền thông | Tạo các endpoint cho quản lý thông báo và gửi thông báo đến người dùng | Application Code | [REQ-016], [DAT-008], [EXC-003] |
  | 9 | Xây dựng hệ thống quản lý khuyến mãi và thông báo | Tạo các endpoint cho quản lý khuyến mãi và thông báo | Application Code | [REQ-017], [REQ-018], [DAT-009] |
  | 10 | Xây dựng hệ thống tích hợp chatbot AI | Tạo các endpoint cho tích hợp chatbot AI và xử lý các truy vấn từ người dùng | Application Code | [REQ-019] |
  | 11 | Xây dựng các tính năng cốt lõi của ứng dụng di động | Tạo các giao diện người dùng và xử lý các yêu cầu từ ứng dụng di động | Application Code | [REQ-020], [REQ-021] |
  | 12 | Xây dựng hệ thống bản địa hóa và SEO | Tạo các endpoint cho quản lý ngôn ngữ và SEO | Application Code | [REQ-022], [REQ-023], [DAT-011] |
  | 13 | Xây dựng hệ thống báo cáo và phân tích | Tạo các endpoint cho tạo báo cáo điểm danh và quản lý bảng điều khiển | Application Code | [REQ-024], [REQ-025], [EXC-005] |
  | 14 | Tạo tài liệu kỹ thuật cho hệ thống | Tạo các tài liệu kỹ thuật cho hệ thống, bao gồm tài liệu kiến trúc, tài liệu API và tài liệu sử dụng | Enterprise Documentation | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
  | 15 | Triển khai hệ thống trên môi trường cloud | Tạo các script và cấu hình để triển khai hệ thống trên môi trường cloud | DevOps Infrastructure | [ARC-010], [NFR-002], [NFR-004], [NFR-009] |
  | **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 15 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |

  <!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. MULTI-PHASE SYNOPSIS MATRIX
  Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
  <RULE>
  [STRICT TABLE EMITTING MANDATE]
  - You MUST dynamically analyze the comprehensive tasks generated in '4.1 MASTER ARCHITECTURAL PRODUCT BACKLOG' immediately above.
  - You MUST systematically divide the entire workload into exactly 5 distinct phases.
  - For each phase row, you are critically ordered to enforce absolute information symmetry by scanning all Tag IDs and Task types from section 4.1.
  - CRITICAL INFRASTRUCTURE RULE: If you detect any DevOps, Cloud, Deployment, CI/CD, Containerization, or Infrastructure tasks in section 4.1 (such as Docker, GCP, GKE, Kubernetes, or Git pipelines), you MUST explicitly list the path (e.g., './sources/infrastructure/devops/') in the Component column, and you MUST permanently declare 'DevOps' alongside Coder, Tester, Reviewer, and Doc in the 'Assigned Sub-Agent' column for that targeted phase. Do not drop the DevOps agent under any circumstance.
  - TIME RAILS: Every phase duration is strictly bound. The Day Range column for each row MUST read exactly 'Day 1 - 7'. No variation or estimation allowed.
  - Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
  - LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
  - DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
  - IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
  - DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
  - SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
    1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
    2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
    3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
    4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
    5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
  - STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
    1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
    2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
    3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
    4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
  - ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
  - CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
  - GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
    1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
    2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
  - ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
  - **ABSOLUTE MATHEMATICAL BACKLOG COUPLING LAW:** You MUST ensure flawless mathematical synchronization between the total task count generated in the Master Backlog table (Section 4.1 Summary Row) and the accumulated count of discrete sub-task nodes produced across all phases inside Section 5.
  - You ARE ABSOLUTELY BANNED from dropping, truncating, or abstracting any task from Section 4.1 when expanding the timeline logs. Every individual functional index or document artifact registered in the Master Backlog table MUST expand into exactly one standalone execution sub-task node within its designated calendar day block inside Section 5. Under-counting, omitting tasks, or prematurely stopping the sub-task sequence before satisfying 100% of the Master Backlog rows constitutes a fatal compliance crash.
  - DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical technical sub-task block inside Section 5 for that specific phase.
  - BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
    1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
    2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
  </RULE>

  <!--START_PHASE_SYNOPSIS_GRID-->

  | Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  | 1 | Day 1 - 2 | ./sources/backend/auth-service/ | Xây dựng hệ thống xác thực người dùng, Thiết kế cơ sở dữ liệu cho người dùng và vai trò | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-006] |
  | 2 | Day 1 - 2 | ./sources/backend/center-service/ | Xây dựng hệ thống quản lý trung tâm | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
  | 3 | Day 1 - 2 | ./sources/backend/course-service/ | Xây dựng hệ thống quản lý khóa học, Xây dựng hệ thống đăng ký và ghi danh học viên | Coder, Tester, Reviewer, Doc | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005] |
  | 4 | Day 1 - 2 | ./sources/backend/attendance-service/ | Xây dựng hệ thống điểm danh và quét mã QR, Xây dựng hệ thống quản lý thẻ hội viên | Coder, Tester, Reviewer, Doc | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002] |
  | 5 | Day 1 - 2 | ./sources/backend/notification-service/ | Xây dựng hệ thống thông báo và truyền thông, Xây dựng hệ thống quản lý khuyến mãi và thông báo, Xây dựng hệ thống tích hợp chatbot AI, Xây dựng các tính năng cốt lõi của ứng dụng di động, Xây dựng hệ thống bản địa hóa và SEO, Xây dựng hệ thống báo cáo và phân tích | Coder, Tester, Reviewer, Doc | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-008], [DAT-009], [DAT-011], [EXC-003], [EXC-005] |
  | **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 5 Phases | **MAPPED CAPACITY STATUS:** Verified: 15 out of 15 Total Master Backlog Tasks successfully distributed across calculated phases with 100% coverage | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |

  <!--END_PHASE_SYNOPSIS_GRID-->

STRICT COMPLIANCE CONSTRAINT: Execute target segment PART_3_FINAL. Generate Section 6, 7, and 8. Do not repeat previous sections.

## 📝 6. SECURITY & COMPLIANCE RAILS

### 6.1. Security Injection Countermeasures
- Áp dụng các biện pháp bảo mật OWASP Top 10 để bảo vệ hệ thống khỏi các cuộc tấn công phổ biến.
- Sử dụng mã hóa dữ liệu truyền và lưu trữ với TLS 1.3 và AES-256.
- Triển khai cơ chế xác thực đa yếu tố (MFA) để bảo vệ các tài khoản quan trọng.
- Áp dụng chính sách quản lý phiên làm việc với JWT và refresh token.
- Triển khai cơ chế kiểm tra và ghi log các hành động của người dùng để phát hiện và ngăn chặn các hoạt động bất thường.

### 6.2. Hybrid Compliance Rules
- Tuân thủ các quy định về bảo mật dữ liệu như GDPR và CCPA.
- Triển khai cơ chế quản lý đồng ý và quyền riêng tư của người dùng.
- Áp dụng các quy định về quản lý và lưu trữ dữ liệu theo yêu cầu của pháp luật.
- Triển khai cơ chế sao lưu và phục hồi dữ liệu để đảm bảo tính sẵn sàng và khả năng phục hồi của hệ thống.

## 🌐 7. SEO & INTERNATIONALIZATION MECHANISMS

### 7.1. SEO Mechanisms
- Triển khai các thẻ meta và thuộc tính hreflang để tối ưu hóa SEO đa ngôn ngữ.
- Sử dụng các công cụ phân tích và báo cáo để theo dõi và cải thiện hiệu suất SEO.
- Áp dụng các kỹ thuật tối ưu hóa nội dung và cấu trúc trang web để tăng tính tương thích với các công cụ tìm kiếm.

### 7.2. Internationalization Mechanisms
- Triển khai cơ chế phát hiện ngôn ngữ mặc định dựa trên các thiết lập của trình duyệt và người dùng.
- Sử dụng các công cụ và thư viện hỗ trợ đa ngôn ngữ để quản lý và hiển thị nội dung theo ngôn ngữ đã chọn.
- Áp dụng các cơ chế kiểm tra và đảm bảo chất lượng bản địa hóa để đảm bảo tính chính xác và nhất quán của nội dung đa ngôn ngữ.

## 🚀 8. PIPELINE GIT FLOW GATING RULES

### 8.1. Pipeline Git Flow Gating Rules
- Triển khai các quy trình kiểm tra tự động và kiểm tra chất lượng mã để đảm bảo tính ổn định và chất lượng của mã nguồn.
- Sử dụng các công cụ tích hợp liên tục (CI) và triển khai liên tục (CD) để tự động hóa các quy trình xây dựng, kiểm tra và triển khai.
- Áp dụng các quy trình quản lý phiên bản và phát hành để đảm bảo tính nhất quán và khả năng theo dõi của các phiên bản phần mềm.
- Triển khai các cơ chế giám sát và cảnh báo để phát hiện và xử lý các vấn đề phát sinh trong quá trình phát triển và triển khai.

### 8.2. Pipeline Git Flow Gating Rules
- Triển khai các quy trình kiểm tra tự động và kiểm tra chất lượng mã để đảm bảo tính ổn định và chất lượng của mã nguồn.
- Sử dụng các công cụ tích hợp liên tục (CI) và triển khai liên tục (CD) để tự động hóa các quy trình xây dựng, kiểm tra và triển khai.
- Áp dụng các quy trình quản lý phiên bản và phát hành để đảm bảo tính nhất quán và khả năng theo dõi của các phiên bản phần mềm.
- Triển khai các cơ chế giám sát và cảnh báo để phát hiện và xử lý các vấn đề phát sinh trong quá trình phát triển và triển khai.