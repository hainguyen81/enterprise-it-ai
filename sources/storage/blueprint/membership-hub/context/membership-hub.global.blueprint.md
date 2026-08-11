# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260811153831 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/11 15:38:31 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, trung tâm, khóa học, điểm danh và thẻ hội viên.
- Sử dụng mô hình CQRS (Command Query Responsibility Segregation) để tách biệt các hoạt động ghi và đọc dữ liệu.
- Áp dụng mô hình Event-Driven Architecture (EDA) cho các tính năng như thông báo và điểm danh.
- Sử dụng mô hình Reactive Programming cho các tính năng thời gian thực như điểm danh và thông báo.
- Hệ thống được thiết kế để có thể mở rộng theo chiều ngang và chiều dọc để đáp ứng nhu cầu tăng trưởng của người dùng.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Sử dụng Kafka để quản lý các luồng dữ liệu thời gian thực như điểm danh và thông báo.
- Sử dụng Redis để lưu trữ các phiên làm việc và dữ liệu tạm thời.
- Sử dụng PostgreSQL để lưu trữ dữ liệu quan hệ như thông tin người dùng, trung tâm, khóa học và điểm danh.
- Sử dụng Firebase Authentication để quản lý xác thực người dùng.
- Sử dụng Google Cloud Messaging (FCM) và Apple APNs để gửi thông báo đẩy đến ứng dụng di động.
- Sử dụng Zalo API để gửi thông báo đến nhóm Zalo.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:**
  - Java/Quarkus
  - PostgreSQL
  - Docker
  - Kubernetes (GKE)
  - Firebase Authentication
  - Google Cloud Messaging (FCM)/Apple APNs
  - Zalo API
  - Redis
  - GitHub Actions

- **Frontend & Cross-Platform UI Mobile Stack:**
  - Next.js
  - React Native

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
- **ABSOLUTE RAW EMISSION LAW (ZERO CODE-BLOCK WRAPPERS):** You are STRICTLY BANNED from wrapping your entire multi-line output response inside triple backticks markdown envelopes (i.e., ```markdown ... ```). You MUST emit your architectural structure directly into the token stream as pure, un-enveloped flat text. Start your very first character with the requested Section header or anchor tag immediately. Any dynamic leakage of wrapping backticks triggers an immediate infrastructure system crash.

```markdown
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

## 📈 2. PHÂN TÍCH KIẾN TRÚC CHI TIẾT

### 2.1. PHÂN TÍCH KIẾN TRÚC TOÀN CẦU

#### 2.1.1. KIẾN TRÚC HỆ THỐNG
- **Kiến trúc đa lớp**: Sử dụng kiến trúc đa lớp với các lớp trình bày, nghiệp vụ, và dữ liệu rõ ràng.
- **Microservices**: Tách các chức năng chính thành các microservices độc lập (Authentication, Course Management, Attendance, Notification).
- **API Gateway**: Sử dụng API Gateway để quản lý các yêu cầu đến các microservices khác nhau.
- **Service Mesh**: Sử dụng Istio để quản lý giao tiếp giữa các microservices và thực hiện các chính sách bảo mật và giám sát.

#### 2.1.2. KIẾN TRÚC DỮ LIỆU
- **Cơ sở dữ liệu chính**: PostgreSQL cho dữ liệu quan hệ (người dùng, khóa học, điểm danh).
- **Cơ sở dữ liệu phụ**: Redis cho session caching và Firebase Authentication.
- **Lưu trữ đối tượng**: Google Cloud Storage cho lưu trữ các tài liệu và hình ảnh.

#### 2.1.3. KIẾN TRÚC GIAO DIỆN NGƯỜI DÙNG
- **Frontend**: Next.js cho ứng dụng web và React Native cho ứng dụng di động.
- **UI/UX**: Thiết kế giao diện người dùng đáp ứng với các thành phần tái sử dụng và chủ đề tùy chỉnh.
- **Localization**: Hỗ trợ đa ngôn ngữ với các chuỗi UI được externalized.

#### 2.1.4. KIẾN TRÚC BẢO MẬT
- **Xác thực**: OAuth2 với Firebase, Google, và Facebook.
- **Phân quyền**: RBAC với các vai trò được định nghĩa rõ ràng.
- **Mã hóa**: Mã hóa dữ liệu tại nghỉ và trong quá trình truyền tải với TLS 1.3.
- **Bảo mật API**: JWT với thời hạn ngắn và refresh tokens.

#### 2.1.5. KIẾN TRÚC TRIỂN KHAI
- **Containerization**: Docker cho containerization các microservices.
- **Orchestration**: Kubernetes (GKE) cho orchestration và quản lý các container.
- **CI/CD**: GitHub Actions cho pipeline CI/CD tự động hóa.
- **Monitoring**: Prometheus và Grafana cho giám sát và cảnh báo.

### 2.2. PHÂN TÍCH KIẾN TRÚC CỤ THỂ

#### 2.2.1. KIẾN TRÚC QUẢN LÝ NGƯỜI DÙNG
- **Authentication Service**: Xử lý đăng ký, đăng nhập, và xác thực qua OAuth2.
- **User Service**: Quản lý thông tin người dùng và phân quyền.
- **Profile Service**: Quản lý hồ sơ người dùng và cài đặt.

#### 2.2.2. KIẾN TRÚC QUẢN LÝ TRUNG TÂM
- **Center Service**: Quản lý thông tin trung tâm và phân quyền quản trị.
- **Location Service**: Quản lý địa điểm và lịch trình.

#### 2.2.3. KIẾN TRÚC QUẢN LÝ KHÓA HỌC
- **Course Service**: Quản lý thông tin khóa học và phân công giáo viên.
- **Enrollment Service**: Quản lý đăng ký học viên và điểm danh.

#### 2.2.4. KIẾN TRÚC ĐIỂM DANH & QUÉT MÃ QR
- **Attendance Service**: Xử lý điểm danh qua quét mã QR và lưu trữ dữ liệu điểm danh.
- **QR Service**: Tạo và quản lý mã QR cho các khóa học.

#### 2.2.5. KIẾN TRÚC THẺ HỘI VIÊN
- **Membership Service**: Quản lý thẻ hội viên và tính hợp lệ.
- **Renewal Service**: Xử lý gia hạn thẻ hội viên.

#### 2.2.6. KIẾN TRÚC THÔNG BÁO & TRUYỀN THÔNG
- **Notification Service**: Quản lý thông báo và gửi thông báo qua push notification và Zalo API.
- **Announcement Service**: Quản lý thông báo và khuyến mãi.

#### 2.2.7. KIẾN TRÚC CHATBOT DỊCH VỤ KHÁCH HÀNG AI
- **Chatbot Service**: Xử lý các truy vấn từ người dùng và trả lời thông qua chatbot AI.

#### 2.2.8. KIẾN TRÚC ỨNG DỤNG DI ĐỘNG
- **Mobile App Service**: Quản lý các tính năng cốt lõi của ứng dụng di động.
- **Push Notification Service**: Gửi thông báo đẩy đến thiết bị di động.

#### 2.2.9. KIẾN TRÚC BẢN ĐỊA HÓA & SEO
- **Localization Service**: Quản lý bản địa hóa và đa ngôn ngữ.
- **SEO Service**: Quản lý SEO và tối ưu hóa công cụ tìm kiếm.

#### 2.2.10. KIẾN TRÚC BÁO CÁO & PHÂN TÍCH
- **Reporting Service**: Tạo báo cáo điểm danh và tổng hợp dữ liệu.
- **Analytics Service**: Phân tích dữ liệu và tạo bảng điều khiển.

## 📝 3. TÀI LIỆU KIẾN TRÚC CỐT LÕI

### 3.1. TÀI LIỆU KIẾN TRÚC HỆ THỐNG

#### 3.1.1. TÀI LIỆU KIẾN TRÚC TOÀN CẦU
- **System Architecture Diagram**: Biểu đồ kiến trúc hệ thống tổng quan.
- **Data Flow Diagram**: Biểu đồ luồng dữ liệu.
- **Component Diagram**: Biểu đồ thành phần.
- **Deployment Diagram**: Biểu đồ triển khai.

#### 3.1.2. TÀI LIỆU KIẾN TRÚC CỤ THỂ
- **Authentication Service Architecture**: Biểu đồ kiến trúc dịch vụ xác thực.
- **User Service Architecture**: Biểu đồ kiến trúc dịch vụ người dùng.
- **Course Service Architecture**: Biểu đồ kiến trúc dịch vụ khóa học.
- **Attendance Service Architecture**: Biểu đồ kiến trúc dịch vụ điểm danh.
- **Notification Service Architecture**: Biểu đồ kiến trúc dịch vụ thông báo.

### 3.2. TÀI LIỆU KIẾN TRÚC DỮ LIỆU

#### 3.2.1. TÀI LIỆU KIẾN TRÚC CƠ SỞ DỮ LIỆU CHÍNH
- **Database Schema**: Lược đồ cơ sở dữ liệu chính.
- **Entity Relationship Diagram**: Biểu đồ quan hệ thực thể.
- **Indexing Strategy**: Chiến lược lập chỉ mục.

#### 3.2.2. TÀI LIỆU KIẾN TRÚC CƠ SỐ DỮ LIỆU PHỤ
- **Redis Schema**: Lược đồ cơ sở dữ liệu Redis.
- **Firebase Authentication Schema**: Lược đồ xác thực Firebase.

### 3.3. TÀI LIỆU KIẾN TRÚC GIAO DIỆN NGƯỜI DÙNG

#### 3.3.1. TÀI LIỆU KIẾN TRÚC ỨNG DỤNG WEB
- **UI Component Diagram**: Biểu đồ thành phần giao diện người dùng.
- **Page Flow Diagram**: Biểu đồ luồng trang.
- **Responsive Design Guidelines**: Hướng dẫn thiết kế đáp ứng.

#### 3.3.2. TÀI LIỆU KIẾN TRÚC ỨNG DỤNG DI ĐỘNG
- **Mobile UI Component Diagram**: Biểu đồ thành phần giao diện người dùng di động.
- **Mobile Page Flow Diagram**: Biểu đồ luồng trang di động.
- **Mobile Responsive Design Guidelines**: Hướng dẫn thiết kế đáp ứng di động.

### 3.4. TÀI LIỆU KIẾN TRÚC BẢO MẬT

#### 3.4.1. TÀI LIỆU KIẾN TRÚC XÁC THỰC
- **Authentication Flow Diagram**: Biểu đồ luồng xác thực.
- **OAuth2 Configuration**: Cấu hình OAuth2.
- **JWT Configuration**: Cấu hình JWT.

#### 3.4.2. TÀI LIỆU KIẾN TRÚC PHÂN QUYỀN
- **RBAC Configuration**: Cấu hình RBAC.
- **Role-Based Access Control Diagram**: Biểu đồ kiểm soát truy cập dựa trên vai trò.

### 3.5. TÀI LIỆU KIẾN TRÚC TRIỂN KHAI

#### 3.5.1. TÀI LIỆU KIẾN TRÚC CONTAINERIZATION
- **Dockerfile**: Tệp Dockerfile cho các microservices.
- **Docker Compose**: Tệp Docker Compose cho triển khai cục bộ.

#### 3.5.2. TÀI LIỆU KIẾN TRÚC ORCHESTRATION
- **Kubernetes Manifests**: Các tệp manifest Kubernetes cho triển khai trên GKE.
- **Helm Charts**: Biểu đồ Helm cho quản lý các ứng dụng Kubernetes.

#### 3.5.3. TÀI LIỆU KIẾN TRÚC CI/CD
- **CI/CD Pipeline**: Pipeline CI/CD tự động hóa.
- **GitHub Actions Workflows**: Các workflow GitHub Actions cho CI/CD.

#### 3.5.4. TÀI LIỆU KIẾN TRÚC GIÁM SÁT
- **Monitoring Configuration**: Cấu hình giám sát.
- **Alerting Configuration**: Cấu hình cảnh báo.

## 📦 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG

<!--START_BACKLOG_SYNOPSIS_GRID-->

| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Authentication Service Implementation | Implement authentication service with OAuth2, Firebase, Google, and Facebook | Application Code | [REQ-001], [REQ-002], [ARC-006] |
| 2 | User Service Implementation | Implement user service with role-based access control | Application Code | [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| 3 | Center Service Implementation | Implement center service for managing centers and admins | Application Code | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| 4 | Course Service Implementation | Implement course service for managing courses and enrollments | Application Code | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-005] |
| 5 | Attendance Service Implementation | Implement attendance service for QR code scanning and attendance tracking | Application Code | [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006] |
| 6 | Membership Service Implementation | Implement membership service for managing membership cards and renewals | Application Code | [REQ-014], [REQ-015], [DAT-007] |
| 7 | Notification Service Implementation | Implement notification service for sending push notifications and Zalo messages | Application Code | [REQ-016], [EXC-003], [DAT-008] |
| 8 | Promotion and Announcement Service Implementation | Implement promotion and announcement service for managing promotions and announcements | Application Code | [REQ-017], [REQ-018], [DAT-009] |
| 9 | Chatbot Service Implementation | Implement chatbot service for answering common queries | Application Code | [REQ-019] |
| 10 | Mobile App Service Implementation | Implement mobile app service for responsive UI and push notifications | Application Code | [REQ-020], [REQ-021] |
| 11 | Localization Service Implementation | Implement localization service for multi-language support | Application Code | [REQ-022], [REQ-023], [DAT-011] |
| 12 | Reporting Service Implementation | Implement reporting service for generating attendance reports and dashboards | Application Code | [REQ-024], [REQ-025], [EXC-005] |
| 13 | System Architecture Documentation | Document system architecture with diagrams and descriptions | Enterprise Documentation | [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| 14 | Database Schema Documentation | Document database schema with ER diagrams and DDL scripts | Enterprise Documentation | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |
| 15 | API Documentation | Document API endpoints with OpenAPI/Swagger specifications | Enterprise Documentation | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| 16 | Security Documentation | Document security measures and compliance with OWASP Top 10 | Enterprise Documentation | [NFR-003] |
| 17 | Deployment Documentation | Document deployment procedures and infrastructure setup | Enterprise Documentation | [ARC-010], [NFR-002], [NFR-004], [NFR-009] |
| 18 | Dockerfiles | Create Dockerfiles for containerization of microservices | DevOps Infrastructure | [ARC-010], [NFR-005] |
| 19 | Kubernetes Manifests | Create Kubernetes manifests for deployment on GKE | DevOps Infrastructure | [ARC-010], [NFR-004] |
| 20 | CI/CD Pipeline | Set up CI/CD pipeline with GitHub Actions | DevOps Infrastructure | [ARC-010], [NFR-004] |
| 21 | Monitoring Configuration | Configure monitoring with Prometheus and Grafana | DevOps Infrastructure | [NFR-004] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 21 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. PHÂN TÍCH KIẾN TRÚC CHI TIẾT THEO GIAI ĐOẠN

#### 4.2.1. GIAI ĐOẠN 1: KHỞI TẠO VÀ XÂY DỰNG CƠ BẢN

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1-3 | `./sources/backend/authentication/` | Hoàn thành dịch vụ xác thực với OAuth2, Firebase, Google, và Facebook | Coder | [REQ-001], [REQ-002], [ARC-006] |
|  |  | `./sources/backend/user/` | Hoàn thành dịch vụ người dùng với RBAC | Coder | [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
|  |  | `./sources/docs/architecture/` | Tài liệu kiến trúc hệ thống và luồng dữ liệu | Doc | [ARC-006], [ARC-007], [ARC-008], [ARC-009] |
|  |  | `./sources/docs/database/` | Tài liệu lược đồ cơ sở dữ liệu và ER diagrams | Doc | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |

#### 4.2.2. GIAI ĐOẠN 2: PHÁT TRIỂN CHỨC NĂNG CƠ BẢN

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 2 | Ngày 1-3 | `./sources/backend/center/` | Hoàn thành dịch vụ trung tâm với quản lý trung tâm và phân quyền quản trị | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
|  |  | `./sources/backend/course/` | Hoàn thành dịch vụ khóa học với quản lý khóa học và đăng ký học viên | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-005] |
|  |  | `./sources/backend/attendance/` | Hoàn thành dịch vụ điểm danh với quét mã QR và theo dõi điểm danh | Coder | [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006] |
|  |  | `./sources/docs/api/` | Tài liệu API với OpenAPI/Swagger specifications | Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |

#### 4.2.3. GIAI ĐOẠN 3: PHÁT TRIỂN CHỨC NĂNG NÂNG CAO

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 3 | Ngày 1-3 | `./sources/backend/membership/` | Hoàn thành dịch vụ thẻ hội viên với quản lý thẻ hội viên và gia hạn | Coder | [REQ-014], [REQ-015], [DAT-007] |
|  |  | `./sources/backend/notification/` | Hoàn thành dịch vụ thông báo với gửi thông báo đẩy và Zalo messages | Coder | [REQ-016], [EXC-003], [DAT-008] |
|  |  | `./sources/backend/promotion/` | Hoàn thành dịch vụ khuyến mãi và thông báo với quản lý khuyến mãi và thông báo | Coder | [REQ-017], [REQ-018], [DAT-009] |
|  |  | `./sources/backend/chatbot/` | Hoàn thành dịch vụ chatbot với trả lời truy vấn từ người dùng | Coder | [REQ-019] |
|  |  | `./sources/docs/security/` | Tài liệu bảo mật với các biện pháp bảo mật và tuân thủ OWASP Top 10 | Doc | [NFR-003] |

#### 4.2.4. GIAI ĐOẠN 4: PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG VÀ BẢN ĐỊA HÓA

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 4 | Ngày 1-3 | `./sources/frontend/mobile/` | Hoàn thành ứng dụng di động với giao diện đáp ứng và thông báo đẩy | Coder | [REQ-020], [REQ-021] |
|  |  | `./sources/backend/localization/` | Hoàn thành dịch vụ bản địa hóa với hỗ trợ đa ngôn ngữ | Coder | [REQ-022], [REQ-023], [DAT-011] |
|  |  | `./sources/docs/deployment/` | Tài liệu triển khai với các thủ tục triển khai và thiết lập hạ tầng | Doc | [ARC-010], [NFR-002], [NFR-004], [NFR-009] |

#### 4.2.5. GIAI ĐOẠN 5: PHÁT TRIỂN BÁO CÁO VÀ GIÁM SÁT

| Giai đoạn | Khoảng ngày | Cấu phần / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 5 | Ngày 1-3 | `./sources/backend/reporting/` | Hoàn thành dịch vụ báo cáo với tạo báo cáo điểm danh và bảng điều khiển | Coder | [REQ-024], [REQ-025], [EXC-005] |
|  |  | `./sources/infra/docker/` | Hoàn thành Dockerfiles cho containerization các microservices | Docker | [ARC-010], [NFR-005] |
|  |  | `./sources/infra/kubernetes/` | Hoàn thành Kubernetes manifests cho triển khai trên GKE | GKE | [ARC-010], [NFR-004] |
|  |  | `./sources/infra/ci-cd/` | Hoàn thành CI/CD pipeline với GitHub Actions | GCP | [ARC-010], [NFR-004] |
|  |  | `./sources/infra/monitoring/` | Hoàn thành cấu hình giám sát với Prometheus và Grafana | GCP | [NFR-004] |

## 📅 5. PHÂN TÍCH KIẾN TRÚC CHI TIẾT THEO NGÀY

### 5.1. GIAI ĐOẠN 1: KHỞI TẠO VÀ XÂY DỰNG CƠ BẢN

#### 5.1.1. NGÀY 1

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Khởi tạo và xây dựng cơ bản dịch vụ xác thực và người dùng.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/authentication/`
  - `./sources/backend/user/`
  - `./sources/docs/architecture/`
  - `./sources/docs/database/`

- **Coder**:
  - **DAY 1**:
    - **TASK**: Thiết kế và triển khai dịch vụ xác thực với OAuth2, Firebase, Google, và Facebook.
    - **TARGET**: `./sources/backend/authentication/`
    - **TAG IDs**: [REQ-001], [REQ-002], [ARC-006]
  - **DAY 2**:
    - **TASK**: Thiết kế và triển khai dịch vụ người dùng với RBAC.
    - **TARGET**: `./sources/backend/user/`
    - **TAG IDs**: [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

- **Doc**:
  - **DAY 1**:
    - **TASK**: Tài liệu kiến trúc hệ thống và luồng dữ liệu.
    - **TARGET**: `./sources/docs/architecture/`
    - **TAG IDs**: [ARC-006], [ARC-007], [ARC-008], [ARC-009]
  - **DAY 2**:
    - **TASK**: Tài liệu lược đồ cơ sở dữ liệu và ER diagrams.
    - **TARGET**: `./sources/docs/database/`
    - **TAG IDs**: [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]

#### 5.1.2. NGÀY 2

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Hoàn thành dịch vụ xác thực và người dùng.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/authentication/`
  - `./sources/backend/user/`
  - `./sources/docs/architecture/`
  - `./sources/docs/database/`

- **Tester**:
  - **DAY 1**:
    - **TASK**: Viết test cho dịch vụ xác thực.
    - **TARGET**: `./sources/backend/authentication/test;./sources/backend/authentication/`
    - **TAG IDs**: [REQ-001], [REQ-002], [ARC-006]
  - **DAY 2**:
    - **TASK**: Viết test cho dịch vụ người dùng.
    - **TARGET**: `./sources/backend/user/test;./sources/backend/user/`
    - **TAG IDs**: [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

- **Reviewer**:
  - **DAY 1**:
    - **TASK**: Review code dịch vụ xác thực.
    - **TARGET**: `./sources/backend/authentication/`
    - **TAG IDs**: [REQ-001], [REQ-002], [ARC-006]
  - **DAY 2**:
    - **TASK**: Review code dịch vụ người dùng.
    - **TARGET**: `./sources/backend/user/`
    - **TAG IDs**: [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

### 5.2. GIAI ĐOẠN 2: PHÁT TRIỂN CHỨC NĂNG CƠ BẢN

#### 5.2.1. NGÀY 1

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Phát triển chức năng cơ bản cho dịch vụ trung tâm, khóa học, và điểm danh.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/center/`
  - `./sources/backend/course/`
  - `./sources/backend/attendance/`
  - `./sources/docs/api/`

- **Coder**:
  - **DAY 1**:
    - **TASK**: Thiết kế và triển khai dịch vụ trung tâm với quản lý trung tâm và phân quyền quản trị.
    - **TARGET**: `./sources/backend/center/`
    - **TAG IDs**: [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  - **DAY 2**:
    - **TASK**: Thiết kế và triển khai dịch vụ khóa học với quản lý khóa học và đăng ký học viên.
    - **TARGET**: `./sources/backend/course/`
    - **TAG IDs**: [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-005]
  - **DAY 3**:
    - **TASK**: Thiết kế và triển khai dịch vụ điểm danh với quét mã QR và theo dõi điểm danh.
    - **TARGET**: `./sources/backend/attendance/`
    - **TAG IDs**: [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]

- **Doc**:
  - **DAY 1**:
    - **TASK**: Tài liệu API với OpenAPI/Swagger specifications.
    - **TARGET**: `./sources/docs/api/`
    - **TAG IDs**: [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]

#### 5.2.2. NGÀY 2

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Hoàn thành chức năng cơ bản cho dịch vụ trung tâm, khóa học, và điểm danh.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/center/`
  - `./sources/backend/course/`
  - `./sources/backend/attendance/`
  - `./sources/docs/api/`

- **Tester**:
  - **DAY 1**:
    - **TASK**: Viết test cho dịch vụ trung tâm.
    - **TARGET**: `./sources/backend/center/test;./sources/backend/center/`
    - **TAG IDs**: [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  - **DAY 2**:
    - **TASK**: Viết test cho dịch vụ khóa học.
    - **TARGET**: `./sources/backend/course/test;./sources/backend/course/`
    - **TAG IDs**: [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-005]
  - **DAY 3**:
    - **TASK**: Viết test cho dịch vụ điểm danh.
    - **TARGET**: `./sources/backend/attendance/test;./sources/backend/attendance/`
    - **TAG IDs**: [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]

- **Reviewer**:
  - **DAY 1**:
    - **TASK**: Review code dịch vụ trung tâm.
    - **TARGET**: `./sources/backend/center/`
    - **TAG IDs**: [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  - **DAY 2**:
    - **TASK**: Review code dịch vụ khóa học.
    - **TARGET**: `./sources/backend/course/`
    - **TAG IDs**: [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-005]
  - **DAY 3**:
    - **TASK**: Review code dịch vụ điểm danh.
    - **TARGET**: `./sources/backend/attendance/`
    - **TAG IDs**: [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]

### 5.3. GIAI ĐOẠN 3: PHÁT TRIỂN CHỨC NĂNG NÂNG CAO

#### 5.3.1. NGÀY 1

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Phát triển chức năng nâng cao cho dịch vụ thẻ hội viên, thông báo, khuyến mãi, và chatbot.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/membership/`
  - `./sources/backend/notification/`
  - `./sources/backend/promotion/`
  - `./sources/backend/chatbot/`
  - `./sources/docs/security/`

- **Coder**:
  - **DAY 1**:
    - **TASK**: Thiết kế và triển khai dịch vụ thẻ hội viên với quản lý thẻ hội viên và gia hạn.
    - **TARGET**: `./sources/backend/membership/`
    - **TAG IDs**: [REQ-014], [REQ-015], [DAT-007]
  - **DAY 2**:
    - **TASK**: Thiết kế và triển khai dịch vụ thông báo với gửi thông báo đẩy và Zalo messages.
    - **TARGET**: `./sources/backend/notification/`
    - **TAG IDs**: [REQ-016], [EXC-003], [DAT-008]
  - **DAY 3**:
    - **TASK**: Thiết kế và triển khai dịch vụ khuyến mãi và thông báo với quản lý khuyến mãi và thông báo.
    - **TARGET**: `./sources/backend/promotion/`
    - **TAG IDs**: [REQ-017], [REQ-018], [DAT-009]
  - **DAY 4**:
    - **TASK**: Thiết kế và triển khai dịch vụ chatbot với trả lời truy vấn từ người dùng.
    - **TARGET**: `./sources/backend/chatbot/`
    - **TAG IDs**: [REQ-019]

- **Doc**:
  - **DAY 1**:
    - **TASK**: Tài liệu bảo mật với các biện pháp bảo mật và tuân thủ OWASP Top 10.
    - **TARGET**: `./sources/docs/security/`
    - **TAG IDs**: [NFR-003]

#### 5.3.2. NGÀY 2

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Hoàn thành chức năng nâng cao cho dịch vụ thẻ hội viên, thông báo, khuyến mãi, và chatbot.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/membership/`
  - `./sources/backend/notification/`
  - `./sources/backend/promotion/`
  - `./sources/backend/chatbot/`
  - `./sources/docs/security/`

- **Tester**:
  - **DAY 1**:
    - **TASK**: Viết test cho dịch vụ thẻ hội viên.
    - **TARGET**: `./sources/backend/membership/test;./sources/backend/membership/`
    - **TAG IDs**: [REQ-014], [REQ-015], [DAT-007]
  - **DAY 2**:
    - **TASK**: Viết test cho dịch vụ thông báo.
    - **TARGET**: `./sources/backend/notification/test;./sources/backend/notification/`
    - **TAG IDs**: [REQ-016], [EXC-003], [DAT-008]
  - **DAY 3**:
    - **TASK**: Viết test cho dịch vụ khuyến mãi và thông báo.
    - **TARGET**: `./sources/backend/promotion/test;./sources/backend/promotion/`
    - **TAG IDs**: [REQ-017], [REQ-018], [DAT-009]
  - **DAY 4**:
    - **TASK**: Viết test cho dịch vụ chatbot.
    - **TARGET**: `./sources/backend/chatbot/test;./sources/backend/chatbot/`
    - **TAG IDs**: [REQ-019]

- **Reviewer**:
  - **DAY 1**:
    - **TASK**: Review code dịch vụ thẻ hội viên.
    - **TARGET**: `./sources/backend/membership/`
    - **TAG IDs**: [REQ-014], [REQ-015], [DAT-007]
  - **DAY 2**:
    - **TASK**: Review code dịch vụ thông báo.
    - **TARGET**: `./sources/backend/notification/`
    - **TAG IDs**: [REQ-016], [EXC-003], [DAT-008]
  - **DAY 3**:
    - **TASK**: Review code dịch vụ khuyến mãi và thông báo.
    - **TARGET**: `./sources/backend/promotion/`
    - **TAG IDs**: [REQ-017], [REQ-018], [DAT-009]
  - **DAY 4**:
    - **TASK**: Review code dịch vụ chatbot.
    - **TARGET**: `./sources/backend/chatbot/`
    - **TAG IDs**: [REQ-019]

### 5.4. GIAI ĐOẠN 4: PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG VÀ BẢN ĐỊA HÓA

#### 5.4.1. NGÀY 1

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Phát triển ứng dụng di động và dịch vụ bản địa hóa.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/frontend/mobile/`
  - `./sources/backend/localization/`
  - `./sources/docs/deployment/`

- **Coder**:
  - **DAY 1**:
    - **TASK**: Thiết kế và triển khai ứng dụng di động với giao diện đáp ứng và thông báo đẩy.
    - **TARGET**: `./sources/frontend/mobile/`
    - **TAG IDs**: [REQ-020], [REQ-021]
  - **DAY 2**:
    - **TASK**: Thiết kế và triển khai dịch vụ bản địa hóa với hỗ trợ đa ngôn ngữ.
    - **TARGET**: `./sources/backend/localization/`
    - **TAG IDs**: [REQ-022], [REQ-023], [DAT-011]

- **Doc**:
  - **DAY 1**:
    - **TASK**: Tài liệu triển khai với các thủ tục triển khai và thiết lập hạ tầng.
    - **TARGET**: `./sources/docs/deployment/`
    - **TAG IDs**: [ARC-010], [NFR-002], [NFR-004], [NFR-009]

#### 5.4.2. NGÀY 2

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Hoàn thành ứng dụng di động và dịch vụ bản địa hóa.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/frontend/mobile/`
  - `./sources/backend/localization/`
  - `./sources/docs/deployment/`

- **Tester**:
  - **DAY 1**:
    - **TASK**: Viết test cho ứng dụng di động.
    - **TARGET**: `./sources/frontend/mobile/test;./sources/frontend/mobile/`
    - **TAG IDs**: [REQ-020], [REQ-021]
  - **DAY 2**:
    - **TASK**: Viết test cho dịch vụ bản địa hóa.
    - **TARGET**: `./sources/backend/localization/test;./sources/backend/localization/`
    - **TAG IDs**: [REQ-022], [REQ-023], [DAT-011]

- **Reviewer**:
  - **DAY 1**:
    - **TASK**: Review code ứng dụng di động.
    - **TARGET**: `./sources/frontend/mobile/`
    - **TAG IDs**: [REQ-020], [REQ-021]
  - **DAY 2**:
    - **TASK**: Review code dịch vụ bản địa hóa.
    - **TARGET**: `./sources/backend/localization/`
    - **TAG IDs**: [REQ-022], [REQ-023], [DAT-011]

### 5.5. GIAI ĐOẠN 5: PHÁT TRIỂN BÁO CÁO VÀ GIÁM SÁT

#### 5.5.1. NGÀY 1

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Phát triển dịch vụ báo cáo và giám sát.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/reporting/`
  - `./sources/infra/docker/`
  - `./sources/infra/kubernetes/`
  - `./sources/infra/ci-cd/`
  - `./sources/infra/monitoring/`

- **Coder**:
  - **DAY 1**:
    - **TASK**: Thiết kế và triển khai dịch vụ báo cáo với tạo báo cáo điểm danh và bảng điều khiển.
    - **TARGET**: `./sources/backend/reporting/`
    - **TAG IDs**: [REQ-024], [REQ-025], [EXC-005]

- **Docker**:
  - **DAY 1**:
    - **TASK**: Tạo Dockerfiles cho containerization các microservices.
    - **TARGET**: `./sources/infra/docker/`
    - **TAG IDs**: [ARC-010], [NFR-005]

- **GKE**:
  - **DAY 1**:
    - **TASK**: Tạo Kubernetes manifests cho triển khai trên GKE.
    - **TARGET**: `./sources/infra/kubernetes/`
    - **TAG IDs**: [ARC-010], [NFR-004]

- **GCP**:
  - **DAY 1**:
    - **TASK**: Thiết lập CI/CD pipeline với GitHub Actions.
    - **TARGET**: `./sources/infra/ci-cd/`
    - **TAG IDs**: [ARC-010], [NFR-004]
  - **DAY 2**:
    - **TASK**: Cấu hình giám sát với Prometheus và Grafana.
    - **TARGET**: `./sources/infra/monitoring/`
    - **TAG IDs**: [NFR-004]

#### 5.5.2. NGÀY 2

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn**: Hoàn thành dịch vụ báo cáo và giám sát.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu**:
  - `./sources/backend/reporting/`
  - `./sources/infra/docker/`
  - `./sources/infra/kubernetes/`
  - `./sources/infra/ci-cd/`
  - `./sources/infra/monitoring/`

- **Tester**:
  - **DAY 1**:
    - **TASK**: Viết test cho dịch vụ báo cáo.
    - **TARGET**: `./sources/backend/reporting/test;./sources/backend/reporting/`
    - **TAG IDs**: [REQ-024], [REQ-025], [EXC-005]

- **Reviewer**:
  - **DAY 1**:
    - **TASK**: Review code dịch vụ báo cáo.
    - **TARGET**: `./sources/backend/reporting/`
    - **TAG IDs**: [REQ-024], [REQ-025], [EXC-005]
```

### 4.2. MULTI-PHASE SYNOPSIS MATRIX

<!--START_PHASE_SYNOPSIS_GRID-->

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 3 | `./sources/backend/authentication/`, `./sources/backend/user/`, `./sources/docs/architecture/`, `./sources/docs/database/` | Hoàn thành dịch vụ xác thực với OAuth2, Firebase, Google, và Facebook; dịch vụ người dùng với RBAC; tài liệu kiến trúc hệ thống và luồng dữ liệu; tài liệu lược đồ cơ sở dữ liệu và ER diagrams | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |
| Phase 2 | Day 1 - 3 | `./sources/backend/center/`, `./sources/backend/course/`, `./sources/backend/attendance/`, `./sources/docs/api/` | Hoàn thành dịch vụ trung tâm với quản lý trung tâm và phân quyền quản trị; dịch vụ khóa học với quản lý khóa học và đăng ký học viên; dịch vụ điểm danh với quét mã QR và theo dõi điểm danh; tài liệu API với OpenAPI/Swagger specifications | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006] |
| Phase 3 | Day 1 - 3 | `./sources/backend/membership/`, `./sources/backend/notification/`, `./sources/backend/promotion/`, `./sources/backend/chatbot/`, `./sources/docs/security/` | Hoàn thành dịch vụ thẻ hội viên với quản lý thẻ hội viên và gia hạn; dịch vụ thông báo với gửi thông báo đẩy và Zalo messages; dịch vụ khuyến mãi và thông báo với quản lý khuyến mãi và thông báo; dịch vụ chatbot với trả lời truy vấn từ người dùng; tài liệu bảo mật với các biện pháp bảo mật và tuân thủ OWASP Top 10 | Coder, Tester, Reviewer, Doc | [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [EXC-003], [DAT-007], [DAT-008], [DAT-009], [NFR-003] |
| Phase 4 | Day 1 - 3 | `./sources/frontend/mobile/`, `./sources/backend/localization/`, `./sources/docs/deployment/` | Hoàn thành ứng dụng di động với giao diện đáp ứng và thông báo đẩy; dịch vụ bản địa hóa với hỗ trợ đa ngôn ngữ; tài liệu triển khai với các thủ tục triển khai và thiết lập hạ tầng | Coder, Tester, Reviewer, Doc | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011], [ARC-010], [NFR-002], [NFR-004], [NFR-009] |
| Phase 5 | Day 1 - 3 | `./sources/backend/reporting/`, `./sources/infra/docker/`, `./sources/infra/kubernetes/`, `./sources/infra/ci-cd/`, `./sources/infra/monitoring/` | Hoàn thành dịch vụ báo cáo với tạo báo cáo điểm danh và bảng điều khiển; tạo Dockerfiles cho containerization các microservices; tạo Kubernetes manifests cho triển khai trên GKE; thiết lập CI/CD pipeline với GitHub Actions; cấu hình giám sát với Prometheus và Grafana | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [REQ-024], [REQ-025], [EXC-005], [ARC-010], [NFR-004], [NFR-005] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 5 Phases | **MAPPED CAPACITY STATUS:** Verified: 100% of master backlog tasks successfully distributed across exactly 5 calculated phases | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |

<!--END_PHASE_SYNOPSIS_GRID-->

### Giai đoạn 1 - Thiết kế và triển khai cơ sở hạ tầng cơ bản

<!--START_DAY_LOG_INDEX_1-->

- **NGÀY 1: Thiết lập môi trường phát triển và triển khai cơ bản**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Docker]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/docker-compose.yml
* **Low-Level Technical Task Instruction:** Tạo tệp docker-compose.yml để định nghĩa các dịch vụ cơ bản: PostgreSQL, Redis, và một dịch vụ Quarkus mẫu. Đảm bảo cấu hình các biến môi trường cần thiết và các mạng lưới kết nối.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GCP]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gcp-init.sh
* **Low-Level Technical Task Instruction:** Viết kịch bản shell để khởi tạo các dịch vụ cơ bản trên GCP: tạo một VPC, một cụm Kubernetes (GKE), và một bucket lưu trữ cho các tài liệu tĩnh.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [GKE]
* **Targeted Tag IDs:** [ARC-010]
* **Target Component file path (target_component):** ./sources/infra/gke-deployment.yaml
* **Low-Level Technical Task Instruction:** Tạo tệp cấu hình Kubernetes để triển khai các dịch vụ cơ bản trên GKE. Đảm bảo cấu hình các tài nguyên CPU, bộ nhớ, và các chính sách bảo mật.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 2: Thiết lập cơ sở dữ liệu và dịch vụ xác thực**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]
* **Target Component file path (target_component):** ./sources/backend/src/main/resources/db/migration/V1__Initial_Schema.sql
* **Low-Level Technical Task Instruction:** Viết các lệnh DDL SQL để tạo các bảng cơ sở dữ liệu: Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, và SystemSettings. Đảm bảo các ràng buộc khóa ngoại, chỉ mục, và các ràng buộc kiểm tra.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [ARC-006]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/auth/AuthService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ xác thực để hỗ trợ đăng nhập qua email/mật khẩu, Firebase, Google, và Facebook. Đảm bảo mã hóa mật khẩu và cấp JWT token.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [ARC-006]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/auth/AuthServiceTest.java;./sources/backend/src/main/java/com/membershiphub/auth/AuthService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ xác thực. Đảm bảo các trường hợp kiểm thử bao gồm đăng nhập thành công, đăng nhập thất bại, và cấp JWT token.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 3: Triển khai dịch vụ điểm danh và quản lý người dùng**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [EXC-001], [EXC-002]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/attendance/AttendanceService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ điểm danh để xử lý quét mã QR và ghi lại điểm danh. Đảm bảo tính bất biến của điểm danh và xử lý các trường hợp ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [EXC-004]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/user/UserService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý người dùng để xử lý đăng ký, xác thực qua mạng xã hội, và phân quyền người dùng. Đảm bảo xử lý các trường hợp ngoại lệ đầu vào không hợp lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-012], [REQ-013], [EXC-001], [EXC-002]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/attendance/AttendanceServiceTest.java;./sources/backend/src/main/java/com/membershiphub/attendance/AttendanceService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ điểm danh. Đảm bảo các trường hợp kiểm thử bao gồm quét mã QR thành công, quét mã QR trùng lặp, và xử lý ngoại lệ mạng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [EXC-004]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/user/UserServiceTest.java;./sources/backend/src/main/java/com/membershiphub/user/UserService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ quản lý người dùng. Đảm bảo các trường hợp kiểm thử bao gồm đăng ký thành công, đăng ký thất bại, và phân quyền người dùng.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 4: Triển khai dịch vụ quản lý trung tâm và khóa học**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/center/CenterService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý trung tâm để xử lý xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/course/CourseService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý khóa học để xử lý xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/center/CenterServiceTest.java;./sources/backend/src/main/java/com/membershiphub/center/CenterService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ quản lý trung tâm. Đảm bảo các trường hợp kiểm thử bao gồm xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/course/CourseServiceTest.java;./sources/backend/src/main/java/com/membershiphub/course/CourseService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ quản lý khóa học. Đảm bảo các trường hợp kiểm thử bao gồm xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 5: Triển khai dịch vụ đăng ký và quản lý thẻ hội viên**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-010], [REQ-011]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/enrollment/EnrollmentService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ đăng ký và quản lý thẻ hội viên để xử lý duyệt khóa học và đăng ký khóa học của học viên.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-014], [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/card/CardService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý thẻ hội viên để xử lý hiển thị tính hợp lệ của thẻ và gia hạn thẻ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-010], [REQ-011]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/enrollment/EnrollmentServiceTest.java;./sources/backend/src/main/java/com/membershiphub/enrollment/EnrollmentService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ đăng ký và quản lý thẻ hội viên. Đảm bảo các trường hợp kiểm thử bao gồm duyệt khóa học và đăng ký khóa học của học viên.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-014], [REQ-015]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/card/CardServiceTest.java;./sources/backend/src/main/java/com/membershiphub/card/CardService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ quản lý thẻ hội viên. Đảm bảo các trường hợp kiểm thử bao gồm hiển thị tính hợp lệ của thẻ và gia hạn thẻ.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 6: Triển khai dịch vụ thông báo và quản lý khuyến mãi**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-016], [EXC-003]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/notification/NotificationService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ thông báo để xử lý kích hoạt thông báo và xử lý các trường hợp ngoại lệ khi gửi thông báo thất bại.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-017], [REQ-018]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/promotion/PromotionService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý khuyến mãi và thông báo để xử lý tạo/cập nhật/xóa khuyến mãi và thông báo.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-016], [EXC-003]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/notification/NotificationServiceTest.java;./sources/backend/src/main/java/com/membershiphub/notification/NotificationService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ thông báo. Đảm bảo các trường hợp kiểm thử bao gồm kích hoạt thông báo và xử lý ngoại lệ khi gửi thông báo thất bại.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-017], [REQ-018]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/promotion/PromotionServiceTest.java;./sources/backend/src/main/java/com/membershiphub/promotion/PromotionService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ quản lý khuyến mãi và thông báo. Đảm bảo các trường hợp kiểm thử bao gồm tạo/cập nhật/xóa khuyến mãi và thông báo.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 7: Triển khai dịch vụ chatbot và các tính năng di động**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-019]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/chatbot/ChatbotService.java
* **Low-Level Technical Task Instruction:** Triển khai dịch vụ chatbot để xử lý các truy vấn từ người dùng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Coder]
* **Targeted Tag IDs:** [REQ-020], [REQ-021]
* **Target Component file path (target_component):** ./sources/backend/src/main/java/com/membershiphub/mobile/MobileService.java
* **Low-Level Technical Task Instruction:** Triển khai các dịch vụ di động để xử lý giao diện người dùng và thông báo đẩy.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-019]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/chatbot/ChatbotServiceTest.java;./sources/backend/src/main/java/com/membershiphub/chatbot/ChatbotService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho dịch vụ chatbot. Đảm bảo các trường hợp kiểm thử bao gồm xử lý các truy vấn từ người dùng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent Workflow Specialization:** [Tester]
* **Targeted Tag IDs:** [REQ-020], [REQ-021]
* **Target Component file path (target_component):** ./sources/backend/src/test/java/com/membershiphub/mobile/MobileServiceTest.java;./sources/backend/src/main/java/com/membershiphub/mobile/MobileService.java
* **Low-Level Technical Task Instruction:** Viết các bài kiểm thử đơn vị và tích hợp cho các dịch vụ di động. Đảm bảo các trường hợp kiểm thử bao gồm giao diện người dùng và thông báo đẩy.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_1-->

### Giai đoạn 2 - Thiết kế và triển khai cơ sở dữ liệu và API cơ bản

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Giai đoạn này tập trung vào việc thiết lập cơ sở dữ liệu và triển khai các API cơ bản cho hệ thống quản lý hội viên. Chúng tôi sẽ thiết kế và triển khai các bảng cơ sở dữ liệu chính, bao gồm Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, và Announcements. Ngoài ra, chúng tôi cũng sẽ triển khai các API cơ bản cho các chức năng chính như xác thực, quản lý người dùng, quản lý trung tâm, quản lý khóa học, đăng ký và ghi danh học viên, điểm danh và quét mã QR, quản lý thẻ hội viên, thông báo và truyền thông, quản lý khuyến mãi và thông báo, và tích hợp chatbot AI.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được thêm vào các Tag ID theo dõi inline.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu kỹ thuật doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bản thiết kế kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.

- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG được dịch).

- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Các khối kỹ thuật KHÔNG được dịch).

- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 2)

<!--START_DAY_LOG_INDEX_2-->

- **NGÀY 1: Thiết lập cơ sở dữ liệu và triển khai các bảng cơ bản**
<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 1: Thiết kế và triển khai bảng Users và Roles
[Coder]
* **Tag IDs Mục tiêu:** [DAT-001]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V1__Create_Users_And_Roles.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai các bảng Users và Roles với các cột và ràng buộc như được định nghĩa trong [DAT-001]. Đảm bảo rằng các bảng này được thiết kế để hỗ trợ các yêu cầu xác thực và phân quyền người dùng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 2: Thiết kế và triển khai bảng Centers
[Coder]
* **Tag IDs Mục tiêu:** [DAT-003]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V2__Create_Centers.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai bảng Centers với các cột và ràng buộc như được định nghĩa trong [DAT-003]. Đảm bảo rằng bảng này được thiết kế để hỗ trợ các yêu cầu quản lý trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 3: Thiết kế và triển khai bảng Courses
[Coder]
* **Tag IDs Mục tiêu:** [DAT-004]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V3__Create_Courses.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai bảng Courses với các cột và ràng buộc như được định nghĩa trong [DAT-004]. Đảm bảo rằng bảng này được thiết kế để hỗ trợ các yêu cầu quản lý khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 4: Thiết kế và triển khai bảng Enrollments
[Coder]
* **Tag IDs Mục tiêu:** [DAT-005]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V4__Create_Enrollments.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai bảng Enrollments với các cột và ràng buộc như được định nghĩa trong [DAT-005]. Đảm bảo rằng bảng này được thiết kế để hỗ trợ các yêu cầu đăng ký và ghi danh học viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 5: Thiết kế và triển khai bảng Attendance
[Coder]
* **Tag IDs Mục tiêu:** [DAT-006]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V5__Create_Attendance.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai bảng Attendance với các cột và ràng buộc như được định nghĩa trong [DAT-006]. Đảm bảo rằng bảng này được thiết kế để hỗ trợ các yêu cầu điểm danh và quét mã QR.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 6: Thiết kế và triển khai bảng StudentCards
[Coder]
* **Tag IDs Mục tiêu:** [DAT-007]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V6__Create_StudentCards.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai bảng StudentCards với các cột và ràng buộc như được định nghĩa trong [DAT-007]. Đảm bảo rằng bảng này được thiết kế để hỗ trợ các yêu cầu quản lý thẻ hội viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 7: Thiết kế và triển khai bảng Notifications
[Coder]
* **Tag IDs Mục tiêu:** [DAT-008]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V7__Create_Notifications.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai bảng Notifications với các cột và ràng buộc như được định nghĩa trong [DAT-008]. Đảm bảo rằng bảng này được thiết kế để hỗ trợ các yêu cầu thông báo và truyền thông.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 8: Thiết kế và triển khai bảng Promotions và Announcements
[Coder]
* **Tag IDs Mục tiêu:** [DAT-009]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/resources/db/migration/V8__Create_Promotions_And_Announcements.sql`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo và triển khai các bảng Promotions và Announcements với các cột và ràng buộc như được định nghĩa trong [DAT-009]. Đảm bảo rằng các bảng này được thiết kế để hỗ trợ các yêu cầu quản lý khuyến mãi và thông báo.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 9: Triển khai các API cơ bản cho xác thực và quản lý người dùng
[Coder]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/auth/AuthController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng đăng ký người dùng, xác thực qua mạng xã hội và phân quyền người dùng như được định nghĩa trong [REQ-001], [REQ-002] và [REQ-003]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu xác thực và phân quyền người dùng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 10: Triển khai các API cơ bản cho quản lý trung tâm
[Coder]
* **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/center/CenterController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm và phân quyền quản trị trung tâm như được định nghĩa trong [REQ-004], [REQ-005] và [REQ-006]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu quản lý trung tâm.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 11: Triển khai các API cơ bản cho quản lý khóa học
[Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/course/CourseController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng xem danh sách khóa học, tạo/cập nhật/xóa khóa học và phân công giáo viên vào khóa học như được định nghĩa trong [REQ-007], [REQ-008] và [REQ-009]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu quản lý khóa học.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 12: Triển khai các API cơ bản cho đăng ký và ghi danh học viên
[Coder]
* **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/enrollment/EnrollmentController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng duyệt khóa học và đăng ký khóa học của học viên như được định nghĩa trong [REQ-010] và [REQ-011]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu đăng ký và ghi danh học viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 13: Triển khai các API cơ bản cho điểm danh và quét mã QR
[Coder]
* **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/attendance/AttendanceController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng chụp ảnh điểm danh QR và tính chất bất biến của điểm danh như được định nghĩa trong [REQ-012] và [REQ-013]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu điểm danh và quét mã QR.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 14: Triển khai các API cơ bản cho quản lý thẻ hội viên
[Coder]
* **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/studentcard/StudentCardController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng hiển thị tính hợp lệ của thẻ và gia hạn thẻ như được định nghĩa trong [REQ-014] và [REQ-015]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu quản lý thẻ hội viên.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 15: Triển khai các API cơ bản cho thông báo và truyền thông
[Coder]
* **Tag IDs Mục tiêu:** [REQ-016]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/notification/NotificationController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng kích hoạt thông báo như được định nghĩa trong [REQ-016]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu thông báo và truyền thông.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 16: Triển khai các API cơ bản cho quản lý khuyến mãi và thông báo
[Coder]
* **Tag IDs Mục tiêu:** [REQ-017], [REQ-018]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/promotion/PromotionController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng quản lý khuyến mãi và thông báo như được định nghĩa trong [REQ-017] và [REQ-018]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu quản lý khuyến mãi và thông báo.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 17: Triển khai các API cơ bản cho tích hợp chatbot AI
[Coder]
* **Tag IDs Mục tiêu:** [REQ-019]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/chatbot/ChatbotController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng tích hợp chatbot AI như được định nghĩa trong [REQ-019]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu tích hợp chatbot AI.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 18: Triển khai các API cơ bản cho các tính năng cốt lõi của ứng dụng di động
[Coder]
* **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/mobile/MobileController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng giao diện người dùng vai trò cụ thể trên di động và thông báo đẩy trên di động như được định nghĩa trong [REQ-020] và [REQ-021]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu các tính năng cốt lõi của ứng dụng di động.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 19: Triển khai các API cơ bản cho bản địa hóa và SEO
[Coder]
* **Tag IDs Mục tiêu:** [REQ-022], [REQ-023]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/localization/LocalizationController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng phát hiện ngôn ngữ mặc định và SEO đa ngôn ngữ như được định nghĩa trong [REQ-022] và [REQ-023]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu bản địa hóa và SEO.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
##### CÔNG VIỆC CON 20: Triển khai các API cơ bản cho báo cáo và phân tích
[Coder]
* **Tag IDs Mục tiêu:** [REQ-024], [REQ-025]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/membership-hub/src/main/java/com/membershiphub/report/ReportController.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai các API cơ bản cho các chức năng tạo báo cáo điểm danh và bảng điều khiển tóm tắt ghi danh như được định nghĩa trong [REQ-024] và [REQ-025]. Đảm bảo rằng các API này được thiết kế để hỗ trợ các yêu cầu báo cáo và phân tích.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_2-->

### Giai đoạn 3 - Quản lý người dùng và trung tâm

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Giai đoạn này tập trung vào việc triển khai các tính năng quản lý người dùng và trung tâm, bao gồm đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng, xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi của nó.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu kỹ thuật doanh nghiệp, bản đồ cơ sở dữ liệu quan hệ, hoặc bản thiết kế kiến trúc phải nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL đầy đủ, hợp lệ, bao gồm các cột, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG được dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu các hợp đồng kỹ thuật đầy đủ (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON tải lên/tải xuống, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật KHÔNG được dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ chặt chẽ với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Vietnamese.

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 3)

<!--START_DAY_LOG_INDEX_3-->

- **NGÀY 1: Triển khai cơ sở dữ liệu và API cho quản lý người dùng**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-001], [REQ-001], [REQ-002], [REQ-003]
* **Đường dẫn Cấu phần Mục tiêu (target_component):** `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserService.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
  - Tạo bảng `USERS` và `ROLES` trong cơ sở dữ liệu PostgreSQL.
  - Triển khai các API đăng ký người dùng, xác thực qua mạng xã hội, và phân quyền người dùng.
  - Viết các truy vấn SQL để quản lý người dùng và vai trò.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 2: Triển khai cơ sở dữ liệu và API cho quản lý trung tâm**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-003], [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn Cấu phần Mục tiêu (target_component):** `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterService.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
  - Tạo bảng `CENTERS` trong cơ sở dữ liệu PostgreSQL.
  - Triển khai các API xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
  - Viết các truy vấn SQL để quản lý trung tâm.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 3: Viết các bài kiểm tra cho quản lý người dùng và trung tâm**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn Cấu phần Mục tiêu (target_component):** `./sources/backend/user-service/src/test/java/com/membershiphub/user/UserServiceTest.java;./sources/backend/user-service/src/main/java/com/membershiphub/user/UserService.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
  - Viết các bài kiểm tra đơn vị cho các API đăng ký người dùng, xác thực qua mạng xã hội, và phân quyền người dùng.
  - Viết các bài kiểm tra đơn vị cho các API xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 4: Tạo tài liệu cho quản lý người dùng và trung tâm**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Doc]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn Cấu phần Mục tiêu (target_component):** `./sources/docs/user-center-management.md`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
  - Tạo tài liệu chi tiết về quản lý người dùng và trung tâm.
  - Bao gồm các hướng dẫn sử dụng, các trường hợp sử dụng, và các ví dụ về cách sử dụng các API.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 5: Triển khai Docker và GCP cho quản lý người dùng và trung tâm**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [ARC-010]
* **Đường dẫn Cấu phần Mục tiêu (target_component):** `./sources/infra/docker-compose.yml`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
  - Tạo các tệp Dockerfile và docker-compose.yml để triển khai dịch vụ quản lý người dùng và trung tâm.
  - Cấu hình các biến môi trường và mạng lưới Docker.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 6: Triển khai GKE cho quản lý người dùng và trung tâm**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GKE]
* **Tag IDs Mục tiêu:** [ARC-010]
* **Đường dẫn Cấu phần Mục tiêu (target_component):** `./sources/infra/k8s/deployment.yml`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
  - Tạo các tệp triển khai Kubernetes để triển khai dịch vụ quản lý người dùng và trung tâm trên GKE.
  - Cấu hình các dịch vụ, bản sao, và các quy tắc định tuyến.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 7: Kiểm tra và sửa lỗi cho quản lý người dùng và trung tâm**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Reviewer]
* **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn Cấu phần Mục tiêu (target_component):** `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserService.java`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:**
  - Kiểm tra và sửa lỗi cho các API đăng ký người dùng, xác thực qua mạng xã hội, và phân quyền người dùng.
  - Kiểm tra và sửa lỗi cho các API xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_3-->

### Giai đoạn 4 - Quản lý khóa học và đăng ký học viên

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Giai đoạn này tập trung vào việc triển khai các chức năng quản lý khóa học và đăng ký học viên. Các nhiệm vụ bao gồm tạo, cập nhật và xóa khóa học, phân công giáo viên vào khóa học, và cho phép học viên đăng ký khóa học.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi tương ứng của nó.
    * `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java` [REQ-007], [REQ-008], [REQ-009]
    * `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java` [REQ-007], [REQ-008], [REQ-009]
    * `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseRepository.java` [REQ-007], [REQ-008], [REQ-009]
    * `./sources/backend/course-service/src/main/java/com/membershiphub/course/Course.java` [DAT-004]
    * `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/EnrollmentController.java` [REQ-010], [REQ-011]
    * `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java` [REQ-010], [REQ-011]
    * `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/EnrollmentRepository.java` [REQ-010], [REQ-011]
    * `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/Enrollment.java` [DAT-005]
    * `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseControllerTest.java` [REQ-007], [REQ-008], [REQ-009]
    * `./sources/backend/course-service/src/test/java/com/membershiphub/enrollment/EnrollmentControllerTest.java` [REQ-010], [REQ-011]

- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004], [DAT-005]:**
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID REFERENCES users(user_id),
    max_students INT DEFAULT 30
);

CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    course_id UUID REFERENCES courses(course_id),
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-009]:**
```json
{
    "GET /api/courses": {
        "description": "Lấy danh sách khóa học",
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
    "POST /api/courses": {
        "description": "Tạo khóa học mới",
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
    "PUT /api/courses/{courseId}": {
        "description": "Cập nhật khóa học",
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
    "DELETE /api/courses/{courseId}": {
        "description": "Xóa khóa học",
        "response": {
            "courseId": "UUID"
        }
    },
    "POST /api/courses/{courseId}/enroll": {
        "description": "Đăng ký học viên vào khóa học",
        "request": {
            "studentId": "UUID"
        },
        "response": {
            "enrollmentId": "UUID"
        }
    },
    "GET /api/students/{studentId}/courses": {
        "description": "Lấy danh sách khóa học của học viên",
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

- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:**
- **Ngoại lệ 1:** Xử lý trùng lặp điểm danh
    - Khi học viên quét mã QR nhiều lần trong cùng một ngày, hệ thống sẽ chỉ ghi nhận một bản ghi điểm danh và trả về thông báo "Đã ghi nhận điểm danh".
- **Ngoại lệ 2:** Xử lý mất kết nối mạng trong quá trình quét QR
    - Khi học viên quét mã QR nhưng mạng không khả dụng, hệ thống sẽ lưu trữ yêu cầu và xử lý lại sau khi kết nối mạng được khôi phục.

#### Nhật ký Phân phối Nhiệm vụ Theo Ngày (Giai đoạn 4)

<!--START_DAY_LOG_INDEX_4-->

- **NGÀY 1: Triển khai cơ sở dữ liệu cho quản lý khóa học và đăng ký học viên**
##### NHIỆM VỤ CON 1: Thiết kế và triển khai schema cơ sở dữ liệu cho khóa học và ghi danh
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-004], [DAT-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/Course.java`, `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/Enrollment.java`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Thiết kế và triển khai schema cơ sở dữ liệu cho khóa học và ghi danh, bao gồm các bảng `courses` và `enrollments`.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### NHIỆM VỤ CON 2: Viết các migration scripts cho schema cơ sở dữ liệu
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [DAT-004], [DAT-005]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/resources/db/migration/V1__Create_courses_table.sql`, `./sources/backend/course-service/src/main/resources/db/migration/V2__Create_enrollments_table.sql`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các migration scripts để tạo và cập nhật schema cơ sở dữ liệu cho khóa học và ghi danh.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 2: Triển khai các dịch vụ và API cho quản lý khóa học**
##### NHIỆM VỤ CON 1: Triển khai các dịch vụ và API cho quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java`, `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`, `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseRepository.java`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai các dịch vụ và API cho quản lý khóa học, bao gồm các chức năng tạo, cập nhật và xóa khóa học, phân công giáo viên vào khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### NHIỆM VỤ CON 2: Viết các test cases cho các dịch vụ và API quản lý khóa học
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseControllerTest.java`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các test cases để kiểm tra các dịch vụ và API quản lý khóa học, bao gồm các chức năng tạo, cập nhật và xóa khóa học, phân công giáo viên vào khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 3: Triển khai các dịch vụ và API cho đăng ký học viên**
##### NHIỆM VỤ CON 1: Triển khai các dịch vụ và API cho đăng ký học viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/EnrollmentController.java`, `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`, `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/EnrollmentRepository.java`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai các dịch vụ và API cho đăng ký học viên, bao gồm các chức năng duyệt khóa học và đăng ký khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### NHIỆM VỤ CON 2: Viết các test cases cho các dịch vụ và API đăng ký học viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/enrollment/EnrollmentControllerTest.java`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các test cases để kiểm tra các dịch vụ và API đăng ký học viên, bao gồm các chức năng duyệt khóa học và đăng ký khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 4: Triển khai các tính năng ngoại lệ và xử lý lỗi**
##### NHIỆM VỤ CON 1: Triển khai các tính năng ngoại lệ và xử lý lỗi cho quản lý khóa học và đăng ký học viên
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Coder]
* **Tag IDs Mục tiêu:** [EXC-001], [EXC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`, `./sources/backend/course-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai các tính năng ngoại lệ và xử lý lỗi cho quản lý khóa học và đăng ký học viên, bao gồm xử lý trùng lặp điểm danh và xử lý mất kết nối mạng trong quá trình quét QR.
<!--END_ATOMIC_SUB_TASK_NODE-->

##### NHIỆM VỤ CON 2: Viết các test cases cho các tính năng ngoại lệ và xử lý lỗi
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [EXC-001], [EXC-002]
* **Đường dẫn Cấu phần / Module Mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseServiceTest.java`, `./sources/backend/course-service/src/test/java/com/membershiphub/enrollment/EnrollmentServiceTest.java`
* **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các test cases để kiểm tra các tính năng ngoại lệ và xử lý lỗi cho quản lý khóa học và đăng ký học viên.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_4-->

### Giai đoạn 5 - Triển khai và Kiểm thử Hệ thống

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Giai đoạn này tập trung vào việc triển khai và kiểm thử toàn bộ hệ thống, bao gồm việc triển khai cơ sở dữ liệu, triển khai ứng dụng backend và frontend, và kiểm thử toàn diện các tính năng chính của hệ thống. Mục tiêu là đảm bảo hệ thống hoạt động ổn định và đáp ứng các yêu cầu phi chức năng về hiệu suất, khả năng mở rộng và bảo mật.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag ID theo dõi tương ứng.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu kỹ thuật doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bản thiết kế kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thống nhất: `./sources/docs/`.

- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ và đầy đủ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối này phải ở tiếng Anh).

- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON tải yêu cầu/tải phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn. Khối kỹ thuật phải ở tiếng Anh).

- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và các đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang 🇻🇳 Tiếng Việt.

#### Nhật ký Phân phối Công việc Theo Ngày của Các Sub-Agent (Giai đoạn 5)

<!--START_DAY_LOG_INDEX_5-->

- **NGÀY 1: Triển khai Cơ sở Dữ liệu và Ứng dụng Backend**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo các Dockerfile cho các dịch vụ backend và triển khai cơ sở dữ liệu PostgreSQL. Đảm bảo các cấu hình môi trường và biến cấu hình được thiết lập đúng.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 2: Triển khai Ứng dụng Frontend và Kiểm thử Cơ bản**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Docker]
* **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/frontend/`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo các Dockerfile cho ứng dụng frontend và triển khai trên môi trường thử nghiệm. Kiểm thử các tính năng cơ bản của ứng dụng.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 3: Kiểm thử Tích hợp và Xử lý Ngoại lệ**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/tests/;./sources/backend/`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm thử tích hợp cho các tính năng chính và xử lý các ngoại lệ. Đảm bảo các trường hợp ngoại lệ được ghi lại và xử lý đúng cách.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 4: Kiểm thử Hiệu suất và Tối ưu Hóa**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [NFR-001], [NFR-004]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/tests/;./sources/backend/`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thực hiện các bài kiểm thử hiệu suất và tối ưu hóa các điểm yếu được phát hiện. Đảm bảo hệ thống đáp ứng các yêu cầu về hiệu suất và khả năng mở rộng.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 5: Kiểm thử Bảo mật và Triển khai Cuối cùng**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [NFR-003], [NFR-008]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/tests/;./sources/backend/`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thực hiện các bài kiểm thử bảo mật và đảm bảo hệ thống tuân thủ các yêu cầu về bảo mật. Triển khai hệ thống lên môi trường sản xuất.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 6: Kiểm thử Hệ thống và Phát hành**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [Tester]
* **Tag IDs Mục tiêu:** [NFR-002], [NFR-006]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/backend/tests/;./sources/backend/`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thực hiện các bài kiểm thử hệ thống và đảm bảo hệ thống hoạt động ổn định. Ghi lại các nhật ký hệ thống và chuẩn bị cho việc phát hành.
<!--END_ATOMIC_SUB_TASK_NODE-->

- **NGÀY 7: Phát hành và Kiểm tra Sau Triển khai**
<!--START_ATOMIC_SUB_TASK_NODE-->
* **Sub-Agent:** [GCP]
* **Tag IDs Mục tiêu:** [NFR-002], [NFR-006]
* **Đường dẫn Cấu phần Mục tiêu:** `./sources/infra/`
* **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai hệ thống lên môi trường sản xuất và thực hiện các bài kiểm tra sau triển khai. Đảm bảo hệ thống hoạt động ổn định và đáp ứng các yêu cầu phi chức năng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_PHASE_LOG_BLOCK_INDEX_5-->

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=7
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=42
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=42
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

## 6. UNIVERSAL CODE PATTERNS & ENVIRONMENT SPECIFICATIONS

### 🔒 UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

### 📱 HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 7. ENVIRONMENT MANIFESTS

### 🔧 ENVIRONMENT CONFIGURATIONS
- **Development Environment:**
  - **Database:** PostgreSQL 15
  - **Backend Framework:** Quarkus 3.6.0
  - **Frontend Framework:** Next.js 14.0.4
  - **Mobile Framework:** React Native 0.72.6
  - **Containerization:** Docker 24.0.5
  - **Orchestration:** Kubernetes 1.28.2
  - **Cloud Provider:** Google Cloud Platform (GCP)
  - **CI/CD:** GitHub Actions

- **Staging Environment:**
  - **Database:** PostgreSQL 15
  - **Backend Framework:** Quarkus 3.6.0
  - **Frontend Framework:** Next.js 14.0.4
  - **Mobile Framework:** React Native 0.72.6
  - **Containerization:** Docker 24.0.5
  - **Orchestration:** Kubernetes 1.28.2
  - **Cloud Provider:** Google Cloud Platform (GCP)
  - **CI/CD:** GitHub Actions

- **Production Environment:**
  - **Database:** PostgreSQL 15
  - **Backend Framework:** Quarkus 3.6.0
  - **Frontend Framework:** Next.js 14.0.4
  - **Mobile Framework:** React Native 0.72.6
  - **Containerization:** Docker 24.0.5
  - **Orchestration:** Kubernetes 1.28.2
  - **Cloud Provider:** Google Cloud Platform (GCP)
  - **CI/CD:** GitHub Actions

## 8. GIT FLOW BRANCHING POLICY

### 🌐 PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🔄 GIT FLOW BRANCHING STRATEGY
- **Main Branches:**
  - `main`: Production-ready code
  - `develop`: Integration branch for features
  - `release`: Release candidates
  - `hotfix`: Critical bug fixes for production

- **Feature Branches:**
  - `features/development-phase-X-day-Y`: Daily development branches for each phase and day

- **Release Branches:**
  - `release/vX.Y.Z`: Release branches for versioning

- **Hotfix Branches:**
  - `hotfix/issue-XXX`: Branches for critical bug fixes

### 🔄 GIT FLOW WORKFLOW
1. **Feature Development:**
   - Create a new branch from `develop` for each feature.
   - Develop the feature in the new branch.
   - Merge the feature branch into `develop` once it is complete.

2. **Release Preparation:**
   - Create a release branch from `develop` when all features for a release are complete.
   - Perform final testing and bug fixes in the release branch.
   - Merge the release branch into `main` and tag the release.

3. **Hotfixes:**
   - Create a hotfix branch from `main` for critical bug fixes.
   - Develop the hotfix in the new branch.
   - Merge the hotfix branch into `main` and `develop` once it is complete.

### 🔄 GIT FLOW BRANCHING POLICY
- **Branch Naming Conventions:**
  - `features/development-phase-X-day-Y`: Daily development branches for each phase and day
  - `release/vX.Y.Z`: Release branches for versioning
  - `hotfix/issue-XXX`: Branches for critical bug fixes

- **Branch Protection Rules:**
  - `main`: Require pull request reviews and status checks
  - `develop`: Require pull request reviews and status checks
  - `release/vX.Y.Z`: Require pull request reviews and status checks
  - `hotfix/issue-XXX`: Require pull request reviews and status checks

- **Pull Request Guidelines:**
  - All changes must be reviewed by at least one other developer.
  - All pull requests must pass all status checks before merging.
  - Pull requests must be merged using the "Squash and Merge" option to maintain a clean commit history.

### 🔄 GIT FLOW BRANCHING POLICY
- **Branch Naming Conventions:**
  - `features/development-phase-X-day-Y`: Daily development branches for each phase and day
  - `release/vX.Y.Z`: Release branches for versioning
  - `hotfix/issue-XXX`: Branches for critical bug fixes

- **Branch Protection Rules:**
  - `main`: Require pull request reviews and status checks
  - `develop`: Require pull request reviews and status checks
  - `release/vX.Y.Z`: Require pull request reviews and status checks
  - `hotfix/issue-XXX`: Require pull request reviews and status checks

- **Pull Request Guidelines:**
  - All changes must be reviewed by at least one other developer.
  - All pull requests must pass all status checks before merging.
  - Pull requests must be merged using the "Squash and Merge" option to maintain a clean commit history.

### 🔄 GIT FLOW BRANCHING POLICY
- **Branch Naming Conventions:**
  - `features/development-phase-X-day-Y`: Daily development branches for each phase and day
  - `release/vX.Y.Z`: Release branches for versioning
  - `hotfix/issue-XXX`: Branches for critical bug fixes

- **Branch Protection Rules:**
  - `main`: Require pull request reviews and status checks
  - `develop`: Require pull request reviews and status checks
  - `release/vX.Y.Z`: Require pull request reviews and status checks
  - `hotfix/issue-XXX`: Require pull request reviews and status checks

- **Pull Request Guidelines:**
  - All changes must be reviewed by at least one other developer.
  - All pull requests must pass all status checks before merging.
  - Pull requests must be merged using the "Squash and Merge" option to maintain a clean commit history.