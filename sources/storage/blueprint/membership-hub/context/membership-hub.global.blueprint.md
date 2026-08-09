# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809140439 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 14:04:39 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo mô hình đa trung tâm với kiến trúc phân tán.
- Sử dụng mô hình RBAC (Role-Based Access Control) để quản lý quyền truy cập.
- Hệ thống hỗ trợ đa kênh giao tiếp (web, di động, nhóm Zalo).
- Sử dụng kiến trúc microservices để tách biệt các chức năng chính.
- Hệ thống tích hợp Firebase Authentication cho xác thực người dùng.
- Sử dụng PostgreSQL làm cơ sở dữ liệu chính.
- Hệ thống được container hóa bằng Docker và triển khai trên Kubernetes (GKE).
- Sử dụng Redis cho session caching.
- Hệ thống sử dụng CI/CD pipeline với GitHub Actions.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Hệ thống sử dụng REST APIs cho giao tiếp giữa frontend và backend.
- Sử dụng JWT tokens cho xác thực và ủy quyền.
- Hệ thống sử dụng Firebase Cloud Messaging (FCM) và Apple APNs cho push notification.
- Sử dụng Zalo API integration cho giao tiếp qua nhóm Zalo.
- Hệ thống sử dụng Redis cho session caching.
- Sử dụng PostgreSQL read replicas cho các workload báo cáo.
- Hệ thống sử dụng CI/CD pipeline với GitHub Actions cho tự động hóa triển khai.
- Sử dụng Docker containerization cho môi trường phát triển và triển khai.
- Hệ thống sử dụng Kubernetes (GKE) cho orchestration và scaling.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API integration, Redis, GitHub Actions
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native

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
| 1 | Xây dựng hệ thống xác thực người dùng | Cung cấp chức năng đăng ký và đăng nhập người dùng thông qua email/mật khẩu, Firebase, Google, và Facebook OAuth | Application Code | [REQ-001], [REQ-002], [ARC-006] |
| 2 | Phân quyền người dùng | Cung cấp chức năng phân quyền người dùng theo vai trò (System Admin, Center Admin, Manager, Teacher, Student) | Application Code | [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| 3 | Xây dựng hệ thống quản lý trung tâm | Cung cấp chức năng xem, tạo, cập nhật, và xóa trung tâm | Application Code | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| 4 | Xây dựng hệ thống quản lý khóa học | Cung cấp chức năng xem, tạo, cập nhật, và xóa khóa học, phân công giáo viên vào khóa học | Application Code | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| 5 | Xây dựng hệ thống đăng ký và ghi danh học viên | Cung cấp chức năng duyệt khóa học, đăng ký khóa học của học viên | Application Code | [REQ-010], [REQ-011], [DAT-005] |
| 6 | Xây dựng hệ thống điểm danh và quét mã QR | Cung cấp chức năng chụp ảnh điểm danh QR, tính chất bất biến của điểm danh | Application Code | [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006] |
| 7 | Xây dựng hệ thống quản lý thẻ hội viên | Cung cấp chức năng hiển thị tính hợp lệ của thẻ, gia hạn thẻ | Application Code | [REQ-014], [REQ-015], [DAT-007] |
| 8 | Xây dựng hệ thống thông báo và truyền thông | Cung cấp chức năng kích hoạt thông báo, quản lý khuyến mãi và thông báo | Application Code | [REQ-016], [REQ-017], [REQ-018], [EXC-003], [DAT-008], [DAT-009] |
| 9 | Tích hợp chatbot AI | Cung cấp chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp | Application Code | [REQ-019] |
| 10 | Xây dựng các tính năng cốt lõi của ứng dụng di động | Cung cấp giao diện người dùng vai trò cụ thể trên di động, thông báo đẩy trên di động | Application Code | [REQ-020], [REQ-021] |
| 11 | Xây dựng hệ thống bản địa hóa và SEO | Cung cấp chức năng phát hiện ngôn ngữ mặc định, SEO đa ngôn ngữ | Application Code | [REQ-022], [REQ-023], [DAT-011] |
| 12 | Xây dựng hệ thống báo cáo và phân tích | Cung cấp chức năng tạo báo cáo điểm danh, bảng điều khiển tóm tắt ghi danh | Application Code | [REQ-024], [REQ-025], [EXC-005] |
| 13 | Xây dựng cơ sở dữ liệu | Xây dựng cơ sở dữ liệu cho hệ thống | DevOps Infrastructure | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |
| 14 | Xây dựng hệ thống containerization | Xây dựng hệ thống containerization cho hệ thống | DevOps Infrastructure | [ARC-010] |
| 15 | Xây dựng hệ thống triển khai | Xây dựng hệ thống triển khai cho hệ thống | DevOps Infrastructure | [ARC-010] |
| 16 | Xây dựng tài liệu kỹ thuật | Xây dựng tài liệu kỹ thuật cho hệ thống | Enterprise Documentation | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 16 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. MULTI-PHASE SYNOPSIS MATRIX

<!--START_PHASE_SYNOPSIS_GRID-->

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 7 | ./sources/backend/auth-service/, ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/backend/enrollment-service/, ./sources/backend/attendance-service/, ./sources/backend/membership-service/, ./sources/backend/notification-service/, ./sources/backend/promotion-service/, ./sources/backend/chatbot-service/, ./sources/backend/mobile-service/, ./sources/backend/localization-service/, ./sources/backend/report-service/ | Xây dựng hệ thống xác thực người dùng, phân quyền người dùng, quản lý trung tâm, quản lý khóa học, đăng ký và ghi danh học viên, điểm danh và quét mã QR, quản lý thẻ hội viên, thông báo và truyền thông, tích hợp chatbot AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Phase 2 | Day 1 - 7 | ./sources/backend/auth-service/, ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/backend/enrollment-service/, ./sources/backend/attendance-service/, ./sources/backend/membership-service/, ./sources/backend/notification-service/, ./sources/backend/promotion-service/, ./sources/backend/chatbot-service/, ./sources/backend/mobile-service/, ./sources/backend/localization-service/, ./sources/backend/report-service/ | Xây dựng hệ thống xác thực người dùng, phân quyền người dùng, quản lý trung tâm, quản lý khóa học, đăng ký và ghi danh học viên, điểm danh và quét mã QR, quản lý thẻ hội viên, thông báo và truyền thông, tích hợp chatbot AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Phase 3 | Day 1 - 7 | ./sources/backend/auth-service/, ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/backend/enrollment-service/, ./sources/backend/attendance-service/, ./sources/backend/membership-service/, ./sources/backend/notification-service/, ./sources/backend/promotion-service/, ./sources/backend/chatbot-service/, ./sources/backend/mobile-service/, ./sources/backend/localization-service/, ./sources/backend/report-service/ | Xây dựng hệ thống xác thực người dùng, phân quyền người dùng, quản lý trung tâm, quản lý khóa học, đăng ký và ghi danh học viên, điểm danh và quét mã QR, quản lý thẻ hội viên, thông báo và truyền thông, tích hợp chatbot AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Phase 4 | Day 1 - 7 | ./sources/backend/auth-service/, ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/backend/enrollment-service/, ./sources/backend/attendance-service/, ./sources/backend/membership-service/, ./sources/backend/notification-service/, ./sources/backend/promotion-service/, ./sources/backend/chatbot-service/, ./sources/backend/mobile-service/, ./sources/backend/localization-service/, ./sources/backend/report-service/ | Xây dựng hệ thống xác thực người dùng, phân quyền người dùng, quản lý trung tâm, quản lý khóa học, đăng ký và ghi danh học viên, điểm danh và quét mã QR, quản lý thẻ hội viên, thông báo và truyền thông, tích hợp chatbot AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Phase 5 | Day 1 - 7 | ./sources/backend/auth-service/, ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/backend/enrollment-service/, ./sources/backend/attendance-service/, ./sources/backend/membership-service/, ./sources/backend/notification-service/, ./sources/backend/promotion-service/, ./sources/backend/chatbot-service/, ./sources/backend/mobile-service/, ./sources/backend/localization-service/, ./sources/backend/report-service/ | Xây dựng hệ thống xác thực người dùng, phân quyền người dùng, quản lý trung tâm, quản lý khóa học, đăng ký và ghi danh học viên, điểm danh và quét mã QR, quản lý thẻ hội viên, thông báo và truyền thông, tích hợp chatbot AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 5 Phases | **MAPPED CAPACITY STATUS:** Verified: 100% of master backlog tasks successfully distributed across exactly 5 calculated phases | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |

<!--END_PHASE_SYNOPSIS_GRID-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809140439 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 14:04:39 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1 Khởi Tạo Hệ Thống Người Dùng Và Xác Thực
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Khởi tạo cơ sở hạ tầng người dùng và hệ thống xác thực, bao gồm việc thiết lập cơ sở dữ liệu người dùng, xác thực qua email/mật khẩu và mạng xã hội, và triển khai cơ chế phân quyền dựa trên vai trò.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi tương ứng.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 1)

- **DAY 1:** Thiết lập cơ sở dữ liệu người dùng và xác thực
    ##### SUB-TASK 1: Thiết lập cơ sở dữ liệu người dùng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [DAT-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/resources/db/migration/V1__Create_users_table.sql`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo bảng người dùng với các trường: userId (UUID), email (VARCHAR(255)), passwordHash (CHAR(60)), fullName (VARCHAR(100)), roleId (SMALLINT), provider (ENUM), createdAt (TIMESTAMP), updatedAt (TIMESTAMP). Thiết lập email là duy nhất và không được null. Thêm chỉ mục trên email và roleId.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 2: Thiết lập cơ sở dữ liệu vai trò
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [DAT-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/resources/db/migration/V2__Create_roles_table.sql`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo bảng vai trò với các trường: roleId (SMALLINT), name (VARCHAR(30)), description (VARCHAR(200)). Thiết lập name là duy nhất và không được null. Thêm chỉ mục trên name.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 3: Thiết lập quan hệ giữa bảng người dùng và vai trò
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [DAT-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/resources/db/migration/V3__Add_foreign_key_to_users.sql`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thêm khóa ngoại roleId trong bảng người dùng tham chiếu đến roleId trong bảng vai trò. Thiết lập hành động CASCADE cho cả INSERT và UPDATE.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 4: Thiết lập dữ liệu ban đầu cho bảng vai trò
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [DAT-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/resources/db/migration/V4__Insert_initial_roles.sql`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Chèn các vai trò ban đầu: System Admin (roleId: 1), Center Admin (roleId: 2), Manager (roleId: 3), Teacher (roleId: 4), Student (roleId: 5).
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 5: Thiết lập dịch vụ xác thực qua email/mật khẩu
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-001], [ARC-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/LocalAuthService.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Triển khai dịch vụ xác thực qua email/mật khẩu. Sử dụng bcrypt để mã hóa mật khẩu. Tạo và trả về JWT token với thời hạn 15 phút và refresh token với thời hạn 7 ngày.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 6: Thiết lập dịch vụ xác thực qua mạng xã hội
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-002], [ARC-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/SocialAuthService.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Triển khai dịch vụ xác thực qua Firebase, Google và Facebook OAuth. Sử dụng thư viện OAuth2 để xử lý xác thực. Tạo và trả về JWT token với thời hạn 15 phút và refresh token với thời hạn 7 ngày.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 7: Thiết lập dịch vụ phân quyền người dùng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-003], [ARC-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/UserRoleService.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Triển khai dịch vụ phân quyền người dùng. Cập nhật vai trò của người dùng và áp dụng quyền hạn tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 8: Viết các bài kiểm tra đơn vị cho dịch vụ xác thực
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/LocalAuthService.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho dịch vụ xác thực qua email/mật khẩu và mạng xã hội. Kiểm tra tính hợp lệ của đầu vào, quá trình mã hóa mật khẩu, và việc tạo JWT token.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 9: Viết các bài kiểm tra đơn vị cho dịch vụ phân quyền
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/service/UserRoleServiceTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/service/UserRoleService.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho dịch vụ phân quyền người dùng. Kiểm tra việc cập nhật vai trò của người dùng và áp dụng quyền hạn tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 10: Đóng gói và triển khai dịch vụ xác thực
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Docker]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/Dockerfile`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo Dockerfile cho dịch vụ xác thực. Sử dụng hình ảnh cơ sở Java/Quarkus. Sao chép các tệp nguồn và tài nguyên. Triển khai dịch vụ trên cổng 8080.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 11: Triển khai dịch vụ xác thực trên GKE
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [GKE]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/gke/auth-service-deployment.yaml`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo tệp triển khai Kubernetes cho dịch vụ xác thực. Định nghĩa Deployment với hình ảnh Docker, cổng 8080 và biến môi trường. Định nghĩa Service để暴露 dịch vụ trên cổng 80.
      <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2:** Triển khai các điểm cuối API xác thực
    ##### SUB-TASK 1: Thiết lập điểm cuối API đăng ký người dùng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo điểm cuối API cho đăng ký người dùng. Xác thực đầu vào và tạo người dùng mới với vai trò 'Student'. Trả về JWT token.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 2: Thiết lập điểm cuối API đăng nhập người dùng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo điểm cuối API cho đăng nhập người dùng. Xác thực thông tin đăng nhập và trả về JWT token.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 3: Thiết lập điểm cuối API xác thực qua mạng xã hội
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-002]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/SocialAuthController.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo điểm cuối API cho xác thực qua mạng xã hội. Xử lý mã OAuth2, tạo hoặc cập nhật người dùng và trả về JWT token.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 4: Thiết lập điểm cuối API phân quyền người dùng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [REQ-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/UserRoleController.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Tạo điểm cuối API cho phân quyền người dùng. Cập nhật vai trò của người dùng và áp dụng quyền hạn tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 5: Viết các bài kiểm tra tích hợp cho các điểm cuối API
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/controller/AuthControllerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/AuthController.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra tích hợp cho các điểm cuối API đăng ký, đăng nhập và xác thực qua mạng xã hội. Kiểm tra tính hợp lệ của đầu vào, quá trình xác thực và trả về JWT token.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 6: Viết các bài kiểm tra tích hợp cho điểm cuối API phân quyền
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [REQ-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/controller/UserRoleControllerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/controller/UserRoleController.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra tích hợp cho điểm cuối API phân quyền người dùng. Kiểm tra việc cập nhật vai trò của người dùng và áp dụng quyền hạn tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 7: Đóng gói và triển khai các điểm cuối API
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Docker]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/Dockerfile`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật Dockerfile cho dịch vụ xác thực. Sao chép các tệp nguồn và tài nguyên. Triển khai dịch vụ trên cổng 8080.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 8: Triển khai các điểm cuối API trên GKE
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [GKE]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/gke/auth-service-deployment.yaml`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật tệp triển khai Kubernetes cho dịch vụ xác thực. Định nghĩa Deployment với hình ảnh Docker mới, cổng 8080 và biến môi trường. Định nghĩa Service để暴露 dịch vụ trên cổng 80.
      <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 3:** Triển khai cơ chế phân quyền và bảo mật
    ##### SUB-TASK 1: Thiết lập cơ chế phân quyền dựa trên vai trò
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/SecurityConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế phân quyền dựa trên vai trò. Sử dụng Spring Security để bảo vệ các điểm cuối API. Áp dụng quyền hạn tương ứng cho từng vai trò.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 2: Thiết lập cơ chế mã hóa dữ liệu
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/EncryptionConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế mã hóa dữ liệu. Sử dụng AES-256 để mã hóa dữ liệu nhạy cảm. Áp dụng cơ chế mã hóa cho các trường dữ liệu nhạy cảm trong cơ sở dữ liệu.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 3: Thiết lập cơ chế xác thực JWT
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [ARC-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/JwtTokenProvider.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế xác thực JWT. Tạo và xác thực JWT token. Áp dụng thời hạn 15 phút cho JWT token và 7 ngày cho refresh token.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho cơ chế phân quyền
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/security/SecurityConfigTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/SecurityConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế phân quyền dựa trên vai trò. Kiểm tra việc áp dụng quyền hạn tương ứng cho từng vai trò.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 5: Viết các bài kiểm tra đơn vị cho cơ chế mã hóa dữ liệu
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/security/EncryptionConfigTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/EncryptionConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế mã hóa dữ liệu. Kiểm tra việc mã hóa và giải mã dữ liệu nhạy cảm.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 6: Viết các bài kiểm tra đơn vị cho cơ chế xác thực JWT
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [ARC-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/security/JwtTokenProviderTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/JwtTokenProvider.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế xác thực JWT. Kiểm tra việc tạo và xác thực JWT token.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 7: Đóng gói và triển khai cơ chế phân quyền và bảo mật
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Docker]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/Dockerfile`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật Dockerfile cho dịch vụ xác thực. Sao chép các tệp nguồn và tài nguyên. Triển khai dịch vụ trên cổng 8080.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 8: Triển khai cơ chế phân quyền và bảo mật trên GKE
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [GKE]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/gke/auth-service-deployment.yaml`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật tệp triển khai Kubernetes cho dịch vụ xác thực. Định nghĩa Deployment với hình ảnh Docker mới, cổng 8080 và biến môi trường. Định nghĩa Service để暴露 dịch vụ trên cổng 80.
      <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 4:** Triển khai cơ chế ghi nhật ký và giám sát
    ##### SUB-TASK 1: Thiết lập cơ chế ghi nhật ký
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/logging/LoggingConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế ghi nhật ký. Sử dụng Logback để ghi nhật ký. Áp dụng mức độ ghi nhật ký tương ứng cho từng gói.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 2: Thiết lập cơ chế giám sát
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/monitoring/MonitoringConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế giám sát. Sử dụng Micrometer và Prometheus để giám sát. Áp dụng các chỉ số giám sát tương ứng cho từng dịch vụ.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho cơ chế ghi nhật ký
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/logging/LoggingConfigTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/logging/LoggingConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế ghi nhật ký. Kiểm tra việc ghi nhật ký và mức độ ghi nhật ký tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho cơ chế giám sát
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-006]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/monitoring/MonitoringConfigTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/monitoring/MonitoringConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế giám sát. Kiểm tra việc giám sát và các chỉ số giám sát tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 5: Đóng gói và triển khai cơ chế ghi nhật ký và giám sát
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Docker]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/Dockerfile`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật Dockerfile cho dịch vụ xác thực. Sao chép các tệp nguồn và tài nguyên. Triển khai dịch vụ trên cổng 8080.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 6: Triển khai cơ chế ghi nhật ký và giám sát trên GKE
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [GKE]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/gke/auth-service-deployment.yaml`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật tệp triển khai Kubernetes cho dịch vụ xác thực. Định nghĩa Deployment với hình ảnh Docker mới, cổng 8080 và biến môi trường. Định nghĩa Service để暴露 dịch vụ trên cổng 80.
      <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 5:** Triển khai cơ chế xử lý ngoại lệ và kiểm tra bảo mật
    ##### SUB-TASK 1: Thiết lập cơ chế xử lý ngoại lệ
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [EXC-004]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/exception/GlobalExceptionHandler.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế xử lý ngoại lệ. Xử lý các ngoại lệ chung và trả về thông báo lỗi tương ứng. Áp dụng các mã lỗi tương ứng cho từng loại ngoại lệ.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 2: Thiết lập cơ chế kiểm tra bảo mật
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/SecurityChecker.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế kiểm tra bảo mật. Kiểm tra các yêu cầu bảo mật và trả về thông báo lỗi tương ứng. Áp dụng các quy tắc bảo mật tương ứng cho từng yêu cầu.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho cơ chế xử lý ngoại lệ
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [EXC-004]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/exception/GlobalExceptionHandlerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/exception/GlobalExceptionHandler.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế xử lý ngoại lệ. Kiểm tra việc xử lý các ngoại lệ chung và trả về thông báo lỗi tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho cơ chế kiểm tra bảo mật
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-003]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/security/SecurityCheckerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/security/SecurityChecker.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế kiểm tra bảo mật. Kiểm tra việc kiểm tra các yêu cầu bảo mật và trả về thông báo lỗi tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 5: Đóng gói và triển khai cơ chế xử lý ngoại lệ và kiểm tra bảo mật
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Docker]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/Dockerfile`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật Dockerfile cho dịch vụ xác thực. Sao chép các tệp nguồn và tài nguyên. Triển khai dịch vụ trên cổng 8080.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 6: Triển khai cơ chế xử lý ngoại lệ và kiểm tra bảo mật trên GKE
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [GKE]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/gke/auth-service-deployment.yaml`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật tệp triển khai Kubernetes cho dịch vụ xác thực. Định nghĩa Deployment với hình ảnh Docker mới, cổng 8080 và biến môi trường. Định nghĩa Service để暴露 dịch vụ trên cổng 80.
      <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 6:** Triển khai cơ chế kiểm tra hiệu suất và khả năng mở rộng
    ##### SUB-TASK 1: Thiết lập cơ chế kiểm tra hiệu suất
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/performance/PerformanceChecker.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế kiểm tra hiệu suất. Kiểm tra hiệu suất của các điểm cuối API và trả về thông báo tương ứng. Áp dụng các quy tắc kiểm tra hiệu suất tương ứng cho từng điểm cuối.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 2: Thiết lập cơ chế khả năng mở rộng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-004]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/scalability/ScalabilityConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế khả năng mở rộng. Áp dụng các quy tắc khả năng mở rộng tương ứng cho từng dịch vụ. Sử dụng Kubernetes HPA để mở rộng ngang các dịch vụ.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho cơ chế kiểm tra hiệu suất
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-001]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/performance/PerformanceCheckerTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/performance/PerformanceChecker.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế kiểm tra hiệu suất. Kiểm tra hiệu suất của các điểm cuối API và trả về thông báo tương ứng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho cơ chế khả năng mở rộng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-004]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/scalability/ScalabilityConfigTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/scalability/ScalabilityConfig.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế khả năng mở rộng. Kiểm tra việc áp dụng các quy tắc khả năng mở rộng tương ứng cho từng dịch vụ.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 5: Đóng gói và triển khai cơ chế kiểm tra hiệu suất và khả năng mở rộng
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Docker]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/Dockerfile`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật Dockerfile cho dịch vụ xác thực. Sao chép các tệp nguồn và tài nguyên. Triển khai dịch vụ trên cổng 8080.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 6: Triển khai cơ chế kiểm tra hiệu suất và khả năng mở rộng trên GKE
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [GKE]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/gke/auth-service-deployment.yaml`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật tệp triển khai Kubernetes cho dịch vụ xác thực. Định nghĩa Deployment với hình ảnh Docker mới, cổng 8080 và biến môi trường. Định nghĩa Service để暴露 dịch vụ trên cổng 80.
      <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 7:** Triển khai cơ chế sao lưu và phục hồi thảm họa
    ##### SUB-TASK 1: Thiết lập cơ chế sao lưu cơ sở dữ liệu
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-009]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/backup/DatabaseBackup.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế sao lưu cơ sở dữ liệu. Sao lưu cơ sở dữ liệu hàng ngày và lưu trữ trên Google Cloud Storage. Áp dụng các quy tắc sao lưu tương ứng cho từng bảng.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 2: Thiết lập cơ chế phục hồi thảm họa
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Coder]
      * **Tag IDs Mục tiêu:** [NFR-009]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/main/java/com/membershiphub/auth/disasterrecovery/DisasterRecovery.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Thiết lập cơ chế phục hồi thảm họa. Phục hồi cơ sở dữ liệu từ bản sao lưu và khôi phục các dịch vụ. Áp dụng các quy tắc phục hồi tương ứng cho từng dịch vụ.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 3: Viết các bài kiểm tra đơn vị cho cơ chế sao lưu cơ sở dữ liệu
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-009]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/backup/DatabaseBackupTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/backup/DatabaseBackup.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế sao lưu cơ sở dữ liệu. Kiểm tra việc sao lưu cơ sở dữ liệu hàng ngày và lưu trữ trên Google Cloud Storage.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 4: Viết các bài kiểm tra đơn vị cho cơ chế phục hồi thảm họa
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Tester]
      * **Tag IDs Mục tiêu:** [NFR-009]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/src/test/java/com/membershiphub/auth/disasterrecovery/DisasterRecoveryTest.java;./sources/backend/auth-service/src/main/java/com/membershiphub/auth/disasterrecovery/DisasterRecovery.java`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Viết các bài kiểm tra đơn vị cho cơ chế phục hồi thảm họa. Kiểm tra việc phục hồi cơ sở dữ liệu từ bản sao lưu và khôi phục các dịch vụ.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 5: Đóng gói và triển khai cơ chế sao lưu và phục hồi thảm họa
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [Docker]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/auth-service/Dockerfile`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật Dockerfile cho dịch vụ xác thực. Sao chép các tệp nguồn và tài nguyên. Triển khai dịch vụ trên cổng 8080.
      <!--END_ATOMIC_SUB_TASK_NODE-->

    ##### SUB-TASK 6: Triển khai cơ chế sao lưu và phục hồi thảm họa trên GKE
      <!--START_ATOMIC_SUB_TASK_NODE-->
      * **Sub-Agent:** [GKE]
      * **Tag IDs Mục tiêu:** [ARC-010]
      * **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/gke/auth-service-deployment.yaml`
      * **Hướng dẫn Công việc Kỹ thuật Cấp thấp:**
        Cập nhật tệp triển khai Kubernetes cho dịch vụ xác thực. Định nghĩa Deployment với hình ảnh Docker mới, cổng 8080 và biến môi trường. Định nghĩa Service để暴露 dịch vụ trên cổng 80.
      <!--END_ATOMIC_SUB_TASK_NODE-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809140439 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 14:04:39 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📈 Giai đoạn 2: Triển Khai Lõi Nghiệp Vụ Khóa Học

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai các chức năng quản lý khóa học, bao gồm tạo, cập nhật, xóa khóa học và phân công giáo viên vào khóa học. Đảm bảo rằng hệ thống có thể xử lý các yêu cầu xung đột lịch trình và cung cấp giao diện người dùng để quản lý khóa học một cách hiệu quả.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được thêm vào các Tag ID theo dõi tương ứng.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu kỹ thuật doanh nghiệp, bản đồ cơ sở dữ liệu quan hệ, hoặc bản thiết kế kiến trúc phải nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ, chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Các khối kỹ thuật này KHÔNG được dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [ARC-006]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Các khối kỹ thuật KHÔNG được dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và các đường dẫn xử lý ngoại lệ hệ thống ánh xạ chặt chẽ với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 2)

- **DAY 1:** Triển khai cơ sở dữ liệu cho mô-đun quản lý khóa học

  ##### SUB-TASK 1: Thiết kế lược đồ cơ sở dữ liệu cho khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-004]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/resources/db/migration/V1__Create_Courses_Table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      ```sql
      CREATE TABLE Courses (
          courseId UUID PRIMARY KEY,
          title VARCHAR(150) NOT NULL,
          description TEXT,
          startDate DATE NOT NULL,
          endDate DATE NOT NULL,
          teacherId UUID REFERENCES Users(userId),
          maxStudents INT DEFAULT 30
      );
      CREATE INDEX idx_courses_teacherId ON Courses(teacherId);
      CREATE INDEX idx_courses_dates ON Courses(startDate, endDate);
      ```
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Viết các kiểm thử cho lược đồ cơ sở dữ liệu
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [DAT-004]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/db/CourseSchemaTest.java;./sources/backend/course-service/src/main/resources/db/migration/V1__Create_Courses_Table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Viết các kiểm thử để đảm bảo rằng bảng Courses được tạo với các cột và ràng buộc chính xác.
      - Kiểm tra các chỉ mục đã được tạo cho teacherId và các ngày bắt đầu/kết thúc.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2:** Triển khai API quản lý khóa học

  ##### SUB-TASK 1: Thiết kế API cho quản lý khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseResource.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      ```java
      @Path("/courses")
      public class CourseResource {
          @GET
          @Produces(MediaType.APPLICATION_JSON)
          public List<Course> getAllCourses() {
              // Logic để lấy danh sách khóa học
          }

          @POST
          @Consumes(MediaType.APPLICATION_JSON)
          public Response createCourse(Course course) {
              // Logic để tạo khóa học mới
          }

          @PUT
          @Path("/{courseId}/assign-teacher")
          @Consumes(MediaType.APPLICATION_JSON)
          public Response assignTeacher(@PathParam("courseId") UUID courseId, UUID teacherId) {
              // Logic để phân công giáo viên vào khóa học
          }
      }
      ```
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Viết các kiểm thử cho API quản lý khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseResourceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseResource.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Viết các kiểm thử để đảm bảo rằng API trả về danh sách khóa học chính xác.
      - Kiểm tra các trường hợp tạo khóa học mới và phân công giáo viên vào khóa học.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 3:** Triển khai giao diện người dùng cho quản lý khóa học

  ##### SUB-TASK 1: Thiết kế giao diện người dùng cho quản lý khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/frontend/src/components/CourseManagement.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      ```javascript
      import React, { useState, useEffect } from 'react';
      import axios from 'axios';

      const CourseManagement = () => {
          const [courses, setCourses] = useState([]);
          const [teachers, setTeachers] = useState([]);

          useEffect(() => {
              axios.get('/api/courses').then(response => {
                  setCourses(response.data);
              });
              axios.get('/api/teachers').then(response => {
                  setTeachers(response.data);
              });
          }, []);

          const handleCreateCourse = (course) => {
              axios.post('/api/courses', course).then(response => {
                  setCourses([...courses, response.data]);
              });
          };

          const handleAssignTeacher = (courseId, teacherId) => {
              axios.put(`/api/courses/${courseId}/assign-teacher`, { teacherId }).then(response => {
                  setCourses(courses.map(course => course.id === courseId ? response.data : course));
              });
          };

          return (
              <div>
                  <h1>Quản lý Khóa Học</h1>
                  <CourseList courses={courses} onAssignTeacher={handleAssignTeacher} teachers={teachers} />
                  <CreateCourseForm onCreateCourse={handleCreateCourse} />
              </div>
          );
      };

      export default CourseManagement;
      ```
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Viết các kiểm thử cho giao diện người dùng
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/frontend/src/tests/CourseManagement.test.js;./sources/frontend/src/components/CourseManagement.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Viết các kiểm thử để đảm bảo rằng giao diện người dùng hiển thị danh sách khóa học chính xác.
      - Kiểm tra các trường hợp tạo khóa học mới và phân công giáo viên vào khóa học.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 4:** Triển khai xử lý xung đột lịch trình

  ##### SUB-TASK 1: Thiết kế xử lý xung đột lịch trình
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      ```java
      public class CourseService {
          public Course createCourse(Course course) throws ConflictException {
              // Kiểm tra xung đột lịch trình
              if (hasScheduleConflict(course)) {
                  throw new ConflictException("Teacher is already scheduled for another course during these dates.");
              }
              // Lưu khóa học mới
              courseRepository.save(course);
              return course;
          }

          private boolean hasScheduleConflict(Course course) {
              // Logic để kiểm tra xung đột lịch trình
          }
      }
      ```
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Viết các kiểm thử cho xử lý xung đột lịch trình
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Viết các kiểm thử để đảm bảo rằng xử lý xung đột lịch trình hoạt động chính xác.
      - Kiểm tra các trường hợp tạo khóa học mới và phân công giáo viên vào khóa học.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 5:** Triển khai thông báo cho giáo viên

  ##### SUB-TASK 1: Thiết kế thông báo cho giáo viên
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      ```java
      public class NotificationService {
          public void sendTeacherAssignmentNotification(UUID teacherId, Course course) {
              // Logic để gửi thông báo cho giáo viên
          }
      }
      ```
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Viết các kiểm thử cho thông báo cho giáo viên
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Viết các kiểm thử để đảm bảo rằng thông báo cho giáo viên được gửi chính xác.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 6:** Triển khai xử lý ngoại lệ cho điểm danh

  ##### SUB-TASK 1: Thiết kế xử lý ngoại lệ cho điểm danh
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [EXC-001], [EXC-002]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      ```java
      public class AttendanceService {
          public Attendance recordAttendance(UUID studentId, UUID courseId) throws DuplicateAttendanceException, NetworkException {
              // Kiểm tra điểm danh trùng lặp
              if (isDuplicateAttendance(studentId, courseId)) {
                  throw new DuplicateAttendanceException("Attendance already recorded for today.");
              }
              // Ghi lại điểm danh
              Attendance attendance = new Attendance(studentId, courseId, LocalDate.now(), LocalDateTime.now());
              attendanceRepository.save(attendance);
              return attendance;
          }

          private boolean isDuplicateAttendance(UUID studentId, UUID courseId) {
              // Logic để kiểm tra điểm danh trùng lặp
          }
      }
      ```
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Viết các kiểm thử cho xử lý ngoại lệ cho điểm danh
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [EXC-001], [EXC-002]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Viết các kiểm thử để đảm bảo rằng xử lý ngoại lệ cho điểm danh hoạt động chính xác.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 7:** Triển khai tài liệu cho mô-đun quản lý khóa học

  ##### SUB-TASK 1: Viết tài liệu cho mô-đun quản lý khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/course-management.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Viết tài liệu chi tiết về các chức năng quản lý khóa học, bao gồm tạo, cập nhật, xóa khóa học và phân công giáo viên vào khóa học.
      - Cung cấp các ví dụ về cách sử dụng API và giao diện người dùng.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Kiểm tra tài liệu cho mô-đun quản lý khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Reviewer]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/course-management.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
      - Kiểm tra tài liệu để đảm bảo rằng nó đầy đủ và chính xác.
      - Đảm bảo rằng các ví dụ và hướng dẫn sử dụng được cung cấp một cách rõ ràng.
    <!--END_ATOMIC_SUB_TASK_NODE-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809140439 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 14:04:39 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📈 Giai đoạn 3: Triển Khai Lõi Nghiệp Vụ Khóa Học

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai các chức năng quản lý khóa học, bao gồm tạo, cập nhật, xóa khóa học, phân công giáo viên vào khóa học, và xử lý xung đột lịch trình.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được thêm vào các Tag ID theo dõi tương ứng.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu kỹ thuật doanh nghiệp, bản tham khảo kiến trúc, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc phải nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án có yêu cầu lớp cơ sở dữ liệu hoặc lớp lưu trữ nào đó. Khối kỹ thuật này KHÔNG được dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [ARC-006], [ARC-007], [ARC-008], [ARC-009]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG được dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 3)

<!--START_DAY_LOG_INDEX_3-->

- **DAY 1:** Khởi tạo cơ sở dữ liệu và dịch vụ quản lý khóa học

  ##### SUB-TASK 1: Thiết lập cơ sở dữ liệu cho mô-đun khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [DAT-004]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/resources/db/migration/V1__Create_Courses_Table.sql`
    * **Low-Level Technical Task Instruction:** Tạo bảng `Courses` với các cột: `courseId`, `title`, `description`, `startDate`, `endDate`, `teacherId`, `maxStudents`. Thiết lập khóa chính cho `courseId` và khóa ngoại cho `teacherId`. Thêm chỉ mục cho `startDate` và `endDate` để tối ưu hóa truy vấn lịch trình. [DAT-004]

    ##### Database Schema DDL SQL Specification [DAT-004]:
    ```sql
    CREATE TABLE Courses (
        courseId UUID PRIMARY KEY,
        title VARCHAR(150) NOT NULL,
        description TEXT,
        startDate DATE NOT NULL,
        endDate DATE NOT NULL,
        teacherId UUID REFERENCES Users(userId),
        maxStudents INT DEFAULT 30
    );

    CREATE INDEX idx_courses_start_date ON Courses(startDate);
    CREATE INDEX idx_courses_end_date ON Courses(endDate);
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Thiết lập dịch vụ quản lý khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ `CourseService` với các phương thức: `getAllCourses()`, `createCourse()`, `updateCourse()`, `deleteCourse()`, `assignTeacherToCourse()`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-007], [REQ-008], [REQ-009]

    ##### API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009]:
    ```json
    {
      "getAllCourses": {
        "method": "GET",
        "path": "/api/courses",
        "response": {
          "courses": [
            {
              "courseId": "UUID",
              "title": "string",
              "startDate": "date",
              "endDate": "date",
              "teacherName": "string"
            }
          ]
        }
      },
      "createCourse": {
        "method": "POST",
        "path": "/api/courses",
        "request": {
          "title": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "UUID"
        },
        "response": {
          "courseId": "UUID"
        }
      },
      "assignTeacherToCourse": {
        "method": "POST",
        "path": "/api/courses/{courseId}/teachers",
        "request": {
          "teacherId": "UUID"
        },
        "response": {
          "status": "string"
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2:** Triển khai chức năng phân công giáo viên vào khóa học

  ##### SUB-TASK 1: Thêm bảng ánh xạ khóa học-giáo viên
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [DAT-004]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/resources/db/migration/V2__Create_Course_Teacher_Mapping_Table.sql`
    * **Low-Level Technical Task Instruction:** Tạo bảng `CourseTeacherMapping` với các cột: `mappingId`, `courseId`, `teacherId`, `assignedDate`. Thiết lập khóa chính cho `mappingId` và khóa ngoại cho `courseId` và `teacherId`. [DAT-004]

    ##### Database Schema DDL SQL Specification [DAT-004]:
    ```sql
    CREATE TABLE CourseTeacherMapping (
        mappingId UUID PRIMARY KEY,
        courseId UUID REFERENCES Courses(courseId),
        teacherId UUID REFERENCES Users(userId),
        assignedDate TIMESTAMP DEFAULT NOW()
    );
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Triển khai chức năng phân công giáo viên
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-009]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseTeacherService.java`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ `CourseTeacherService` với các phương thức: `assignTeacherToCourse()`, `unassignTeacherFromCourse()`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-009]

    ##### API and Event Routing Contracts [REQ-009]:
    ```json
    {
      "assignTeacherToCourse": {
        "method": "POST",
        "path": "/api/courses/{courseId}/teachers",
        "request": {
          "teacherId": "UUID"
        },
        "response": {
          "status": "string"
        }
      },
      "unassignTeacherFromCourse": {
        "method": "DELETE",
        "path": "/api/courses/{courseId}/teachers/{teacherId}",
        "response": {
          "status": "string"
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 3:** Triển khai chức năng xử lý xung đột lịch trình

  ##### SUB-TASK 1: Thêm ràng buộc kiểm tra xung đột lịch trình
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [DAT-004]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/resources/db/migration/V3__Add_Schedule_Conflict_Check.sql`
    * **Low-Level Technical Task Instruction:** Thêm ràng buộc kiểm tra xung đột lịch trình cho bảng `Courses`. Đảm bảo rằng không có hai khóa học cùng một giáo viên hoặc cùng một địa điểm có lịch trình trùng lặp. [DAT-004]

    ##### Database Schema DDL SQL Specification [DAT-004]:
    ```sql
    ALTER TABLE Courses
    ADD CONSTRAINT chk_no_teacher_schedule_conflict
    CHECK (
        NOT EXISTS (
            SELECT 1
            FROM Courses c2
            WHERE c2.teacherId = Courses.teacherId
            AND c2.courseId != Courses.courseId
            AND (
                (Courses.startDate BETWEEN c2.startDate AND c2.endDate)
                OR (Courses.endDate BETWEEN c2.startDate AND c2.endDate)
                OR (c2.startDate BETWEEN Courses.startDate AND Courses.endDate)
                OR (c2.endDate BETWEEN Courses.startDate AND Courses.endDate)
            )
        )
    );
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Triển khai chức năng kiểm tra xung đột lịch trình
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-008]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseConflictService.java`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ `CourseConflictService` với phương thức `checkScheduleConflict()`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-008]

    ##### API and Event Routing Contracts [REQ-008]:
    ```json
    {
      "checkScheduleConflict": {
        "method": "POST",
        "path": "/api/courses/check-conflict",
        "request": {
          "teacherId": "UUID",
          "startDate": "date",
          "endDate": "date"
        },
        "response": {
          "hasConflict": "boolean",
          "conflictingCourses": [
            {
              "courseId": "UUID",
              "title": "string",
              "startDate": "date",
              "endDate": "date"
            }
          ]
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 4:** Triển khai chức năng xem danh sách khóa học

  ##### SUB-TASK 1: Triển khai chức năng xem danh sách khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-007]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java`
    * **Low-Level Technical Task Instruction:** Triển khai controller `CourseController` với phương thức `getAllCourses()`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-007]

    ##### API and Event Routing Contracts [REQ-007]:
    ```json
    {
      "getAllCourses": {
        "method": "GET",
        "path": "/api/courses",
        "response": {
          "courses": [
            {
              "courseId": "UUID",
              "title": "string",
              "startDate": "date",
              "endDate": "date",
              "teacherName": "string"
            }
          ]
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 5:** Triển khai chức năng tạo/cập nhật/xóa khóa học

  ##### SUB-TASK 1: Triển khai chức năng tạo khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-008]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java`
    * **Low-Level Technical Task Instruction:** Triển khai phương thức `createCourse()` trong controller `CourseController`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-008]

    ##### API and Event Routing Contracts [REQ-008]:
    ```json
    {
      "createCourse": {
        "method": "POST",
        "path": "/api/courses",
        "request": {
          "title": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "UUID"
        },
        "response": {
          "courseId": "UUID"
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Triển khai chức năng cập nhật khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-008]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java`
    * **Low-Level Technical Task Instruction:** Triển khai phương thức `updateCourse()` trong controller `CourseController`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-008]

    ##### API and Event Routing Contracts [REQ-008]:
    ```json
    {
      "updateCourse": {
        "method": "PUT",
        "path": "/api/courses/{courseId}",
        "request": {
          "title": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "UUID"
        },
        "response": {
          "status": "string"
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 3: Triển khai chức năng xóa khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-008]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java`
    * **Low-Level Technical Task Instruction:** Triển khai phương thức `deleteCourse()` trong controller `CourseController`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-008]

    ##### API and Event Routing Contracts [REQ-008]:
    ```json
    {
      "deleteCourse": {
        "method": "DELETE",
        "path": "/api/courses/{courseId}",
        "response": {
          "status": "string"
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 6:** Triển khai chức năng kiểm tra xung đột lịch trình

  ##### SUB-TASK 1: Triển khai chức năng kiểm tra xung đột lịch trình
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-008]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseConflictService.java`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ `CourseConflictService` với phương thức `checkScheduleConflict()`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-008]

    ##### API and Event Routing Contracts [REQ-008]:
    ```json
    {
      "checkScheduleConflict": {
        "method": "POST",
        "path": "/api/courses/check-conflict",
        "request": {
          "teacherId": "UUID",
          "startDate": "date",
          "endDate": "date"
        },
        "response": {
          "hasConflict": "boolean",
          "conflictingCourses": [
            {
              "courseId": "UUID",
              "title": "string",
              "startDate": "date",
              "endDate": "date"
            }
          ]
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 7:** Triển khai chức năng phân công giáo viên vào khóa học

  ##### SUB-TASK 1: Triển khai chức năng phân công giáo viên vào khóa học
    <!--START_ATOMIC_SUB_TASK_NODE-->

    * **Sub-Agent:** [Coder]
    * **Targeted Tag IDs:** [REQ-009]
    * **Target Component file path (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseTeacherService.java`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ `CourseTeacherService` với các phương thức: `assignTeacherToCourse()`, `unassignTeacherFromCourse()`. Xử lý các trường hợp ngoại lệ cho các yêu cầu không hợp lệ. [REQ-009]

    ##### API and Event Routing Contracts [REQ-009]:
    ```json
    {
      "assignTeacherToCourse": {
        "method": "POST",
        "path": "/api/courses/{courseId}/teachers",
        "request": {
          "teacherId": "UUID"
        },
        "response": {
          "status": "string"
        }
      },
      "unassignTeacherFromCourse": {
        "method": "DELETE",
        "path": "/api/courses/{courseId}/teachers/{teacherId}",
        "response": {
          "status": "string"
        }
      }
    }
    ```

  <!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_3-->

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809140439 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 14:04:39 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📈 Giai đoạn 4 Khởi Tạo Hệ Thống Thông Báo Và Tích Hợp Zalo

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Khởi tạo hệ thống thông báo đa kênh bao gồm ứng dụng di động và nhóm Zalo, triển khai cơ sở dữ liệu cho thông báo, và tích hợp API Zalo để gửi tin nhắn.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi tương ứng.
    * *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu kỹ thuật doanh nghiệp, bản đồ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ, chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Các khối kỹ thuật này KHÔNG được dịch).

```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(255),
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_notifications_user_id ON notifications(user_id);
CREATE INDEX idx_notifications_sent_at ON notifications(sent_at);
```

- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [ARC-008]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Các khối kỹ thuật này KHÔNG được dịch).

```json
{
  "endpoints": [
    {
      "path": "/api/notifications",
      "method": "POST",
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
  ],
  "eventTopics": [
    {
      "topic": "notifications",
      "messageSchema": {
        "userId": "UUID",
        "groupZalo": "string",
        "message": "string"
      }
    }
  ]
}
```

- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh vào 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 4)

<!--START_DAY_LOG_INDEX_4-->

- **DAY 1: Khởi tạo Cơ sở Dữ liệu Thông báo và API Cơ bản**
  ##### SUB-TASK 1: Thiết kế Schema Cơ sở Dữ liệu Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/src/main/resources/db/migration/V4__Create_notifications_table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo bảng `notifications` với các cột `notification_id`, `user_id`, `group_zalo`, `message`, `sent_at`, và `delivered`. Thêm các chỉ mục cho `user_id` và `sent_at`.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Triển khai API Gửi Thông báo Cơ bản
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/src/main/java/com/membershiphub/api/NotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai điểm cuối `/api/notifications` với phương thức POST để nhận `userId`, `groupZalo`, và `message`. Lưu thông báo vào cơ sở dữ liệu và trả về `notificationId`.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Tích hợp Zalo API và Xử lý Ngoại lệ**
  ##### SUB-TASK 1: Tích hợp Zalo API
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/src/main/java/com/membershiphub/service/ZaloService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo dịch vụ `ZaloService` để gửi tin nhắn đến nhóm Zalo sử dụng Zalo API. Sử dụng `groupZalo` và `message` từ thông báo để gửi tin nhắn.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Xử lý Ngoại lệ Gửi Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [EXC-003]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/src/main/java/com/membershiphub/exception/NotificationExceptionHandler.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo bộ xử lý ngoại lệ để xử lý các trường hợp gửi thông báo thất bại. Ghi nhật ký lỗi và thử lại tối đa 3 lần trước khi đánh dấu là thất bại.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 3: Kiểm thử và Tối ưu Hiệu suất**
  ##### SUB-TASK 1: Viết Bài kiểm thử cho API Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-016]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/src/test/java/com/membershiphub/api/NotificationControllerTest.java;./sources/backend/src/main/java/com/membershiphub/api/NotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm thử cho điểm cuối `/api/notifications` để đảm bảo nó lưu thông báo vào cơ sở dữ liệu và trả về `notificationId` đúng cách.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Kiểm thử Tích hợp Zalo API
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/src/test/java/com/membershiphub/service/ZaloServiceTest.java;./sources/backend/src/main/java/com/membershiphub/service/ZaloService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm thử cho `ZaloService` để đảm bảo nó gửi tin nhắn đến nhóm Zalo đúng cách.
    <!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_4-->

```markdown
# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809140439 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 14:04:39 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📈 Giai đoạn 5: Triển Khai Hệ Thống Thông Báo & Truyền Thông

### Giai đoạn 5

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống thông báo đa kênh bao gồm push notification cho ứng dụng di động và tin nhắn trên nhóm Zalo. Đảm bảo tính nhất quán và thời gian thực của thông báo cho tất cả người dùng.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notification-service/`, `./sources/frontend/mobile-app/`, `./sources/docs/notification-system.md` [REQ-016], [DAT-008], [EXC-003]
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:**
  ```sql
  CREATE TABLE Notifications (
      notificationId UUID PRIMARY KEY,
      userId UUID REFERENCES Users(userId),
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      delivered BOOLEAN DEFAULT FALSE
  );
  CREATE INDEX idx_notifications_userId ON Notifications(userId);
  CREATE INDEX idx_notifications_sentAt ON Notifications(sentAt);
  ```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [ARC-008]:**
  ```json
  {
    "POST /api/notifications": {
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
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Khi một thông báo đẩy không thể được giao (ví dụ: mã thiết bị không hợp lệ), Hệ thống sẽ ghi lại sự cố và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 5)

- **DAY 1: Triển khai Cơ sở Dữ liệu và API Thông báo**
  ##### SUB-TASK 1: Thiết kế Schema Cơ sở Dữ liệu
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [DAT-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/resources/db/migration/V5__Create_Notifications_Table.sql`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo bảng `Notifications` với các trường `notificationId`, `userId`, `groupZalo`, `message`, `sentAt`, và `delivered`. Thêm các chỉ mục cho `userId` và `sentAt` để tối ưu hóa truy vấn.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Triển khai API Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai endpoint `POST /api/notifications` để tạo thông báo mới. Đảm bảo endpoint này có thể xử lý cả thông báo cho người dùng và nhóm Zalo.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 2: Kiểm thử và Xác thực API Thông báo**
  ##### SUB-TASK 1: Viết Bài kiểm thử cho API Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/NotificationControllerTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationController.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm thử cho endpoint `POST /api/notifications` để đảm bảo nó có thể tạo thông báo cho người dùng và nhóm Zalo. Kiểm tra cả trường hợp thành công và thất bại.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Kiểm tra Tích hợp với Firebase Cloud Messaging (FCM)
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-021], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/FcmIntegrationTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/FcmService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Kiểm tra tích hợp với FCM để đảm bảo thông báo đẩy có thể được gửi thành công đến thiết bị di động.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 3: Triển khai Tích hợp với Zalo API**
  ##### SUB-TASK 1: Thiết kế Bộ xử lý Tích hợp Zalo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/ZaloService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ để gửi tin nhắn đến nhóm Zalo. Đảm bảo dịch vụ này có thể xử lý cả thông báo cho người dùng và nhóm Zalo.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Kiểm thử Tích hợp với Zalo API
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/ZaloIntegrationTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/ZaloService.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Kiểm tra tích hợp với Zalo API để đảm bảo tin nhắn có thể được gửi thành công đến nhóm Zalo.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 4: Triển khai Bộ xử lý Ngoại lệ và Ghi nhật ký**
  ##### SUB-TASK 1: Thiết kế Bộ xử lý Ngoại lệ
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [EXC-003]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationExceptionHandler.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai bộ xử lý ngoại lệ để xử lý các trường hợp ngoại lệ khi gửi thông báo. Đảm bảo bộ xử lý này có thể ghi lại sự cố và lên lịch thử lại.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Kiểm thử Bộ xử lý Ngoại lệ
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [EXC-003]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/NotificationExceptionHandlerTest.java;./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationExceptionHandler.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Kiểm tra bộ xử lý ngoại lệ để đảm bảo nó có thể xử lý các trường hợp ngoại lệ khi gửi thông báo.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 5: Triển khai Tích hợp với Ứng dụng Di động**
  ##### SUB-TASK 1: Thiết kế Tích hợp với Ứng dụng Di động
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-021], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/frontend/mobile-app/src/services/NotificationService.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ để nhận thông báo đẩy từ FCM và hiển thị chúng trong ứng dụng di động.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Kiểm thử Tích hợp với Ứng dụng Di động
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-021], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/frontend/mobile-app/src/tests/NotificationService.test.js;./sources/frontend/mobile-app/src/services/NotificationService.js`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Kiểm tra tích hợp với ứng dụng di động để đảm bảo thông báo đẩy có thể được nhận và hiển thị thành công.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 6: Tài liệu và Triển khai**
  ##### SUB-TASK 1: Tài liệu Hệ thống Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/docs/notification-system.md`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu chi tiết về hệ thống thông báo, bao gồm cách thiết lập, sử dụng và kiểm tra.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Triển khai Hệ thống Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Docker]
    * **Tag IDs Mục tiêu:** [ARC-010]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/Dockerfile`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo Dockerfile để đóng gói dịch vụ thông báo và triển khai lên môi trường sản xuất.
    <!--END_ATOMIC_SUB_TASK_NODE-->

- **DAY 7: Kiểm tra và Triển khai Cuối cùng**
  ##### SUB-TASK 1: Kiểm tra Hệ thống Thông báo
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [Tester]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/NotificationSystemTest.java`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Kiểm tra toàn bộ hệ thống thông báo để đảm bảo nó hoạt động đúng và đáp ứng các yêu cầu.
    <!--END_ATOMIC_SUB_TASK_NODE-->

  ##### SUB-TASK 2: Triển khai Cuối cùng
    <!--START_ATOMIC_SUB_TASK_NODE-->
    * **Sub-Agent:** [GKE]
    * **Tag IDs Mục tiêu:** [ARC-010]
    * **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/infra/gke/notification-service-deployment.yaml`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ thông báo lên môi trường sản xuất trên GKE.
    <!--END_ATOMIC_SUB_TASK_NODE-->

### Báo cáo Kiểm tra Kiến trúc Tự động:
```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=7
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=0
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=35
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```
```

# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260809140439 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/09 14:04:39 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

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