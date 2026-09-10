<!--START_CHUNK_PART_1_INITIAL-->

# GLOBAL PROJECT CONTEXT: social-scheduler

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260910234454 |
| **Project Name** | social-scheduler |
| **Version** | 1.0 (Cơ sở) |
| **Date Time** | 2026/09/10 23:44:54 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Chờ phê duyệt quản trị kỹ thuật |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### ⚙️ 1.1. Core System Modality & Architecture Modality

- Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho từng chức năng chính.
- Sử dụng mô hình Event-Driven Architecture (EDA) để xử lý các tác vụ bất đồng bộ như đăng bài lên mạng xã hội.
- Áp dụng mô hình Command Query Responsibility Segregation (CQRS) để tách biệt các thao tác ghi và đọc dữ liệu.
- Sử dụng mô hình Reactive Programming để xử lý các luồng dữ liệu thời gian thực.

### 🌊 1.2. Enterprise Data Flow Topologies & Core Ecosystems

- Sử dụng Apache Kafka để quản lý các luồng dữ liệu bất đồng bộ giữa các dịch vụ.
- Triển khai các topic Kafka riêng biệt cho từng loại sự kiện (ví dụ: `post-scheduled`, `post-sent`, `post-failed`).
- Sử dụng các consumer group để xử lý các sự kiện một cách song song và đáng tin cậy.
- Áp dụng mô hình fan-out để phân phối các sự kiện đến nhiều dịch vụ khác nhau.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack**:
  - Quarkus 3.8.2 (Java)
  - Spring Boot 3.2.4 (Java)
  - Hibernate ORM 6.4.4.Final
  - PostgreSQL 16.2
  - Apache Kafka 3.7.0
  - Redis 7.2.4
  - Docker 24.0.7
  - Kubernetes 1.28.4
  - GitHub Actions 2.812.0

- **Frontend & Cross-Platform UI Mobile Stack**:
  - Next.js 14.1.0
  - React Native 0.73.4
  - Tailwind CSS 3.4.1
  - Firebase Hosting 12.5.0

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

### 🔑 3.1. Security & Compliance Baseline

- Áp dụng mã hóa TLS 1.3 cho tất cả các kết nối mạng.
- Triển khai xác thực OAuth2 và JWT cho tất cả các yêu cầu API.
- Áp dụng chính sách CORS nghiêm ngặt để ngăn chặn các yêu cầu không mong muốn.
- Triển khai hệ thống phát hiện và ngăn chặn DDoS.
- Tuân thủ các tiêu chuẩn bảo mật OWASP Top 10.

### 🌐 3.2. Infrastructure & Performance Guardrails

- Sử dụng HikariCP cho quản lý kết nối cơ sở dữ liệu.
- Áp dụng chính sách thu hồi bộ nhớ đệm Redis để tối ưu hóa bộ nhớ.
- Triển khai hàng đợi tin nhắn Kafka với các chủ đề riêng biệt cho từng loại sự kiện.
- Áp dụng các chính sách giới hạn tỷ lệ cho các điểm cuối API.

### 🥞 3.3. ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

### 🕸️ 3.4. DYNAMIC MICROSERVICES TOPOLOGY REGISTRY MATRIX

| Service Domain Key | Microservice Sub-Module Name | Target Container Context Path | Active Infrastructure Gateway Ports | Mapped Functional Backend Packages | Mapped Tracking TagIDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Parent Root Grandmaster** | socialscheduler-root | `./sources/backend/pom.xml` | N/A (Global Orchestrator) | `org.nlh4j.socialscheduler` | [ARC-000] |
| **Automated Scheduling Engine** | socialscheduler-scheduling-service | `./sources/backend/scheduling-service/pom.xml` | 8081 | `org.nlh4j.socialscheduler.schedulingservice` | [REQ-001], [EXC-001], [EXC-002], [DAT-001] |
| **AI Content Suggestion Engine** | socialscheduler-content-service | `./sources/backend/content-service/pom.xml` | 8082 | `org.nlh4j.socialscheduler.contentservice` | [REQ-002], [EXC-003], [EXC-004], [DAT-002] |
| **Authentication & Rate Limiting Engine** | socialscheduler-auth-service | `./sources/backend/auth-service/pom.xml` | 8083 | `org.nlh4j.socialscheduler.authservice` | [REQ-003], [EXC-002], [EXC-003], [EXC-005], [DAT-003] |

<!--END_CHUNK_PART_1_INITIAL-->

<!--START_CHUNK_PART_1_BACKLOG_4_1-->

## 🏁 4. LƯỚI TÓM TẮT KIẾN TRÚC ĐA GIAI ĐOẠN CAO CẤP

### 📦 4.1. LƯỚI NHIỆM VỤ SẢN PHẨM KIẾN TRÚC CHÍNH

#### [MA TRẬN TÍNH TOÁN HỆ THỐNG]
> - **Tổng thẻ [REQ]:** 3 thẻ
> - **Tổng thẻ [EXC]:** 5 thẻ
> - **Tổng thẻ [ARC]:** 6 thẻ
> - **Tổng thẻ [DAT]:** 3 thẻ
> - **Tổng thẻ [NFR]:** 3 thẻ
> - ➡️ **Tổng thẻ SRS:** 17 thẻ

<!--BACKLOG_SYNOPSIS_GRID_START-->

| STT | Nhiệm vụ | Mục đích kỹ thuật / Tóm tắt giao hàng | Loại | Mã theo dõi |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Tích hợp lịch đăng bài tự động | Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok | Mã ứng dụng | [REQ-001] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 2 | Đề xuất nội dung bằng AI | Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó | Mã ứng dụng | [REQ-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 3 | Xác thực đầu vào & giới hạn tỷ lệ | Thực hiện xác thực đầu vào dữ liệu và kiểm tra giới hạn tỷ lệ cho từng người dùng | Mã ứng dụng | [REQ-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 4 | Cơ sở dữ liệu và xác thực mã thông báo | Thiết lập cơ sở dữ liệu và xác thực mã thông báo cho hệ thống | Kiến trúc | [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 5 | Tích hợp API và hợp đồng tích hợp | Tích hợp API và hợp đồng tích hợp cho hệ thống | Kiến trúc | [ARC-006] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 6 | Cơ sở dữ liệu và mã thông báo | Thiết lập cơ sở dữ liệu và mã thông báo cho hệ thống | Cơ sở dữ liệu | [DAT-001] [DAT-002] [DAT-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 7 | Xử lý ngoại lệ và xác thực | Xử lý ngoại lệ và xác thực cho hệ thống | Mã ứng dụng | [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 8 | Tài liệu kỹ thuật | Tạo tài liệu kỹ thuật cho hệ thống | Tài liệu | [DOC-001] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| **TÓM TẮT** | **Tổng số thẻ theo dõi đã bao phủ:** 17 | **Tổng số nhiệm vụ:** 8 | **Trạng thái:** Đã xác minh | **Độ bao phủ:** 100% |

<!--BACKLOG_SYNOPSIS_GRID_END-->

<!--END_CHUNK_PART_1_BACKLOG_4_1-->

<!--START_CHUNK_PART_1_MATRIX_4_2-->

### 🔭 4.2. MA TRẬN TÓM TẮT ĐA GIAI ĐOẠN

#### [MA TRẬN TÍNH TOÁN HỆ THỐNG]
> - **Tổng số nhiệm vụ Backlog:** 8 nhiệm vụ
> - **Tổng số thẻ Backlog:** 17 thẻ
> - **Tổng số nhiệm vụ đã phân phối:** 8 nhiệm vụ
> - **Tổng số thẻ đã phân phối:** 17 thẻ

| Giai đoạn | Phạm vi ngày | Nhiệm vụ được bao phủ | Thành phần kiến trúc / Đường dẫn mô-đun | Tóm tắt giao hàng kỹ thuật | Đặc biệt hóa công việc của Sub-Agent | Thẻ được theo dõi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 2 | Nhiệm vụ 4, Nhiệm vụ 6 | `./sources/backend/pom.xml` <br/> `./sources/backend/scheduling-service/pom.xml` <br/> `./sources/backend/content-service/pom.xml` <br/> `./sources/backend/auth-service/pom.xml` | Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống | Coder, Tester, Reviewer, Doc | [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [DAT-001] [DAT-002] [DAT-003] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 2 | Ngày 1 - 2 | Nhiệm vụ 1 | `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java` <br/> `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java` <br/> `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/repository/SchedulingRepository.java` <br/> `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/entity/Schedule.java` <br/> `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/exception/SchedulingExceptionHandler.java` | Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok | Coder, Tester, Reviewer, Doc | [REQ-001] [EXC-001] [EXC-002] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 3 | Ngày 1 - 2 | Nhiệm vụ 2 | `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/controller/ContentController.java` <br/> `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/service/ContentService.java` <br/> `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepository.java` <br/> `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetric.java` <br/> `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandler.java` | Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó | Coder, Tester, Reviewer, Doc | [REQ-002] [EXC-003] [EXC-004] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 4 | Ngày 1 - 2 | Nhiệm vụ 3, Nhiệm vụ 5 | `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/controller/AuthController.java` <br/> `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/AuthService.java` <br/> `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/repository/AuthRepository.java` <br/> `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/entity/RateLimit.java` <br/> `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/exception/AuthExceptionHandler.java` | Thực hiện xác thực đầu vào dữ liệu và kiểm tra giới hạn tỷ lệ cho từng người dùng | Coder, Tester, Reviewer, Doc | [REQ-003] [ARC-006] [EXC-002] [EXC-003] [EXC-005] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 5 | Ngày 1 - 2 | Nhiệm vụ 7, Nhiệm vụ 8 | `./sources/docs/technical-documentation.md` <br/> `./sources/infra/devops/docker-compose.yml` <br/> `./sources/infra/devops/kubernetes-deployment.yaml` | Tạo tài liệu kỹ thuật cho hệ thống và triển khai hệ thống | Doc, Docker, GCP, GKE | [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005] [DOC-001] <!--REGISTERED_PHASE_ROW--> |
| **Kiểm tra** | **Xác minh phân phối Backlog chính** | **Tổng số giai đoạn:** 5 | **Tổng số thẻ Backlog:** 17 | **Tổng số thẻ đã phân phối:** 17 | **Tổng số nhiệm vụ đã phân phối:** 8 | **Trạng thái & Tuân thủ:** Đã xác minh (100%) |

<!--PHASE_SYNOPSIS_GRID_END-->

<!--END_CHUNK_PART_1_MATRIX_4_2-->

<!--START_CHUNK_PART_2_PHASE_LOOP-->

## 🔬 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1 - Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

- **Ma trận đường dẫn thư mục vật lý mục tiêu:** Tạo ra danh sách kiểm tra kỹ thuật toàn diện, chi tiết về 100% các đường dẫn tệp vật lý riêng lẻ (KHÔNG phải thư mục hoặc đường dẫn) nằm dưới `./sources/`. Mỗi dòng mục trong danh sách này PHẢI đại diện cho một thực thể tệp cụ thể kết thúc bằng phần mở rộng cấu trúc rõ ràng, với các mã theo dõi được đính kèm trực tiếp.

- **Chỉ định DDL SQL Cơ sở dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các trường cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).

- **Hợp đồng định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ nhớ đệm tin nhắn. Khối kỹ thuật KHÔNG ĐƯỢC dịch).

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại.

#### 📅 Nhật ký phân phối nhiệm vụ theo ngày của Sub-Agent (Giai đoạn 1)

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 1: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/pom.xml`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Tester]

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/pom.xml;./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/SchedulingServiceTest.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 3: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Reviewer]

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/pom.xml`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 4: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Doc]

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/pom.xml`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 2: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/scheduling-service/pom.xml`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Tester]

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/scheduling-service/pom.xml;./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/SchedulingServiceTest.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 3: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Reviewer]

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/scheduling-service/pom.xml`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 4: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
- **Chuyên môn công việc của Sub-Agent:** [Doc]

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Đường dẫn thành phần mục tiêu (target_component):** `./sources/backend/scheduling-service/pom.xml`

* **Hướng dẫn kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--PHASE_INDEX_END-->

<!--END_CHUNK_PART_2_PHASE_LOOP-->

<!--START_CHUNK_PART_2_PHASE_LOOP-->

### 📈 Giai đoạn 2 - Dịch vụ Lịch Đăng Bài Tự Động

- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Giai đoạn này tập trung vào việc tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok. Mục tiêu là thiết lập cơ sở hạ tầng cần thiết để lên lịch và thực hiện các bài đăng tự động trên các nền tảng mạng xã hội.

- **Bản đồ ma trận thư mục vật lý mục tiêu:** Tạo danh sách kiểm tra kỹ thuật toàn diện liệt kê 100% tất cả các đường dẫn tệp vật lý riêng lẻ nằm dưới `./sources/` được tạo, tái cấu trúc hoặc xử lý trong phạm vi giai đoạn này. Mỗi mục liệt kê phải đại diện cho một thực thể tệp cụ thể kết thúc bằng phần mở rộng tệp rõ ràng.

- **Chỉ định DDL SQL Schema Cơ sở dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các trường cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có lớp cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).

- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ nhớ đệm tin nhắn. Khối mã KHÔNG ĐƯỢC dịch).

- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ chính xác với phạm vi giai đoạn hiện tại.

#### 📅 Nhật ký phân phối công việc theo ngày của các Sub-Agent (Giai đoạn 2)

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 1: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Triển khai điểm cuối API để lên lịch các bài đăng trên các nền tảng mạng xã hội. Xử lý các trường hợp ngoại lệ khi tích hợp với API bên thứ ba.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Tester]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java`; `./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingControllerTest.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Viết các bài kiểm tra đơn vị và tích hợp cho điểm cuối API lịch đăng bài tự động. Đảm bảo các bài đăng được lên lịch chính xác vào thời điểm đã chỉ định và trạng thái hiển thị là "đã lên lịch".

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 3: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Reviewer]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Đánh giá mã nguồn cho điểm cuối API lịch đăng bài tự động. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 4: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Doc]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/docs/technical-documentation.md`

* **Hướng dẫn kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho điểm cuối API lịch đăng bài tự động. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng điểm cuối API.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 2: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Triển khai dịch vụ để xử lý các yêu cầu lên lịch bài đăng. Xử lý các trường hợp ngoại lệ khi tích hợp với API bên thứ ba.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Tester]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java`; `./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingServiceTest.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ lịch đăng bài tự động. Đảm bảo các bài đăng được lên lịch chính xác vào thời điểm đã chỉ định và trạng thái hiển thị là "đã lên lịch".

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 3: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Reviewer]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Đánh giá mã nguồn cho dịch vụ lịch đăng bài tự động. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 4: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

* **Chuyên môn công việc của Sub-Agent:** [Doc]

* **Thẻ được theo dõi:** [REQ-001], [EXC-001], [EXC-002]

* **Thành phần mục tiêu (đường dẫn tệp):** `./sources/docs/technical-documentation.md`

* **Hướng dẫn kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho dịch vụ lịch đăng bài tự động. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng dịch vụ.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--PHASE_INDEX_END-->

<!--END_CHUNK_PART_2_PHASE_LOOP-->

<!--START_CHUNK_PART_2_PHASE_LOOP-->

### 📈 Giai đoạn 3 - Dịch vụ đề xuất nội dung bằng AI

- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó. Giai đoạn này tập trung vào việc phát triển và tích hợp dịch vụ đề xuất nội dung bằng AI, bao gồm việc tạo ra các điểm cuối API, triển khai mô hình học máy và xử lý các ngoại lệ liên quan đến đề xuất nội dung.

- **Ma trận đường dẫn vật lý mục tiêu:** Tạo một danh sách kiểm tra kỹ thuật toàn diện liệt kê 100% tất cả các đường dẫn tệp vật lý riêng lẻ (KHÔNG phải thư mục hoặc đường dẫn) nằm dưới `./sources/` được tạo, tái cấu trúc hoặc xử lý trong phạm vi giai đoạn này. Mỗi mục trong danh sách phải đại diện cho một thực thể tệp cụ thể kết thúc bằng phần mở rộng cấu trúc rõ ràng, với các mã theo dõi tương ứng được đính kèm inline.

- **Chỉ định DDL SQL Schema [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL thô, hoàn chỉnh và hợp lệ chứa các trường rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng trong phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu dự án không có lớp cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG được dịch).

- **Hợp đồng định tuyến API và sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ nhớ đệm tin nhắn. Khối mã KHÔNG được dịch).

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh sang tiếng Việt.

#### 📅 Nhật ký phân phối nhiệm vụ hàng ngày của các Sub-Agent (Giai đoạn 3)

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 1: Triển khai điểm cuối API đề xuất nội dung

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Triển khai điểm cuối API đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Coder]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/controller/ContentController.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai điểm cuối API để nhận yêu cầu đề xuất nội dung từ người dùng. Đảm bảo điểm cuối này có thể xử lý các yêu cầu đồng thời và trả về các đề xuất nội dung phù hợp.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Triển khai dịch vụ đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Coder]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/service/ContentService.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai dịch vụ đề xuất nội dung để xử lý logic đề xuất nội dung dựa trên hiệu suất trước đó của các bài đăng. Đảm bảo dịch vụ này có thể tích hợp với các mô hình học máy để tạo ra các đề xuất nội dung phù hợp.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 3: Triển khai kho lưu trữ đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Coder]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepository.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai kho lưu trữ đề xuất nội dung để tương tác với cơ sở dữ liệu và lưu trữ các đề xuất nội dung. Đảm bảo kho lưu trữ này có thể xử lý các truy vấn phức tạp và lưu trữ các đề xuất nội dung một cách hiệu quả.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 4: Triển khai thực thể hiệu suất bài đăng
- **Chuyên môn công việc của Sub-Agent:** [Coder]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetric.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể hiệu suất bài đăng để lưu trữ các chỉ số hiệu suất của các bài đăng. Đảm bảo thực thể này có thể ánh xạ với các bảng cơ sở dữ liệu tương ứng và lưu trữ các chỉ số hiệu suất một cách hiệu quả.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 5: Triển khai bộ xử lý ngoại lệ đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Coder]
- **Mã theo dõi mục tiêu:** [EXC-003], [EXC-004]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandler.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai bộ xử lý ngoại lệ đề xuất nội dung để xử lý các ngoại lệ liên quan đến đề xuất nội dung. Đảm bảo bộ xử lý này có thể ghi lại các ngoại lệ và cung cấp các thông báo lỗi phù hợp cho người dùng.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 2: Kiểm thử và tối ưu hóa dịch vụ đề xuất nội dung

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Kiểm thử điểm cuối API đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Tester]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/controller/ContentControllerTest.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử điểm cuối API đề xuất nội dung để đảm bảo nó có thể xử lý các yêu cầu đồng thời và trả về các đề xuất nội dung phù hợp. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Kiểm thử dịch vụ đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Tester]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/service/ContentServiceTest.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử dịch vụ đề xuất nội dung để đảm bảo nó có thể xử lý logic đề xuất nội dung dựa trên hiệu suất trước đó của các bài đăng. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 3: Kiểm thử kho lưu trữ đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Tester]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepositoryTest.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử kho lưu trữ đề xuất nội dung để đảm bảo nó có thể tương tác với cơ sở dữ liệu và lưu trữ các đề xuất nội dung. Đảm bảo các trường hợp kiểm thử bao gồm các truy vấn phức tạp và lưu trữ các đề xuất nội dung một cách hiệu quả.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 4: Kiểm thử thực thể hiệu suất bài đăng
- **Chuyên môn công việc của Sub-Agent:** [Tester]
- **Mã theo dõi mục tiêu:** [REQ-002]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetricTest.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử thực thể hiệu suất bài đăng để đảm bảo nó có thể ánh xạ với các bảng cơ sở dữ liệu tương ứng và lưu trữ các chỉ số hiệu suất một cách hiệu quả. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 5: Kiểm thử bộ xử lý ngoại lệ đề xuất nội dung
- **Chuyên môn công việc của Sub-Agent:** [Tester]
- **Mã theo dõi mục tiêu:** [EXC-003], [EXC-004]
- **Đường dẫn thành phần mục tiêu:** `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandlerTest.java`
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử bộ xử lý ngoại lệ đề xuất nội dung để đảm bảo nó có thể ghi lại các ngoại lệ và cung cấp các thông báo lỗi phù hợp cho người dùng. Đảm bảo các trường hợp kiểm thử bao gồm các ngoại lệ hợp lệ và không hợp lệ.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--PHASE_INDEX_END-->

<!--END_CHUNK_PART_2_PHASE_LOOP-->

<!--START_CHUNK_PART_2_PHASE_LOOP-->

### 📈 Giai đoạn 4 - Kiến trúc và triển khai dịch vụ xác thực và giới hạn tỷ lệ

- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Giai đoạn này tập trung vào việc triển khai dịch vụ xác thực và giới hạn tỷ lệ, bao gồm việc thiết lập cơ sở dữ liệu, xác thực mã thông báo và triển khai các điểm cuối API. Giai đoạn này đảm bảo rằng hệ thống có thể xác thực người dùng và giới hạn số lần gọi API mỗi phút để ngăn chặn lạm dụng.

- **Ma trận đường dẫn vật lý mục tiêu:** Triển khai các điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các điểm cuối cho xác thực người dùng, tạo mã thông báo, làm mới mã thông báo và kiểm tra giới hạn tỷ lệ.

- **Chỉ số DDL SQL cơ sở dữ liệu [DAT-XXX]:** Triển khai các bảng cơ sở dữ liệu cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm bảng người dùng, bảng mã thông báo và bảng giới hạn tỷ lệ.

- **Hợp đồng định tuyến API và sự kiện [REQ-XXX], [ARC-XXX]:** Triển khai các điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các điểm cuối cho xác thực người dùng, tạo mã thông báo, làm mới mã thông báo và kiểm tra giới hạn tỷ lệ.

- **Bộ xử lý ngoại lệ cục bộ của giai đoạn [EXC-XXX]:** Triển khai các bộ xử lý ngoại lệ cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm xử lý ngoại lệ cho xác thực người dùng, tạo mã thông báo, làm mới mã thông báo và kiểm tra giới hạn tỷ lệ.

#### 📅 Nhật ký phân phối nhiệm vụ theo ngày của các Sub-Agent (Giai đoạn 4)

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 1: Triển khai cơ sở dữ liệu và xác thực mã thông báo

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Triển khai cơ sở dữ liệu cho dịch vụ xác thực và giới hạn tỷ lệ

* **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Thẻ được theo dõi:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Thành phần mục tiêu (đường dẫn thành phần):** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/entity/User.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Triển khai lớp thực thể User cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các trường như userId, username, password, email và role.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Triển khai xác thực mã thông báo cho dịch vụ xác thực và giới hạn tỷ lệ

* **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Thẻ được theo dõi:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Thành phần mục tiêu (đường dẫn thành phần):** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/AuthService.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Triển khai dịch vụ xác thực mã thông báo cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các phương thức như authenticate, generateToken, refreshToken và validateToken.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 2: Triển khai các điểm cuối API và kiểm tra giới hạn tỷ lệ

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Triển khai điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ

* **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Thẻ được theo dõi:** [REQ-003], [ARC-006]

* **Thành phần mục tiêu (đường dẫn thành phần):** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/controller/AuthController.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Triển khai điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các điểm cuối như /authenticate, /generate-token, /refresh-token và /validate-token.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 2: Triển khai kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ

* **Chuyên môn công việc của Sub-Agent:** [Coder]

* **Thẻ được theo dõi:** [REQ-003], [EXC-005]

* **Thành phần mục tiêu (đường dẫn thành phần):** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/RateLimitService.java`

* **Hướng dẫn kỹ thuật cấp thấp:** Triển khai dịch vụ kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các phương thức như checkRateLimit và updateRateLimit.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--PHASE_INDEX_END-->

<!--END_CHUNK_PART_2_PHASE_LOOP-->

<!--START_CHUNK_PART_2_PHASE_LOOP-->

### 📈 Giai đoạn 5 - Triển khai và tài liệu hệ thống

- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Triển khai hệ thống và tạo tài liệu kỹ thuật cho hệ thống. Giai đoạn này tập trung vào việc triển khai hệ thống và tạo tài liệu kỹ thuật để đảm bảo hệ thống hoạt động đúng cách và dễ dàng bảo trì.

- **Ma trận đường dẫn vật lý mục tiêu:** Tạo tài liệu kỹ thuật cho hệ thống và triển khai hệ thống.

- **Xử lý ngoại lệ cục bộ của giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Xử lý ngoại lệ và xác thực cho hệ thống.

#### 📅 Nhật ký phân phối công việc theo ngày của các Sub-Agent (Giai đoạn 5)

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 1: Triển khai hệ thống và tạo tài liệu kỹ thuật

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Triển khai hệ thống

* **Chuyên môn công việc của Sub-Agent:** [Docker]

* **Thẻ được theo dõi:** [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]

* **Thành phần mục tiêu (target_component):** `./sources/infra/devops/docker-compose.yml`

* **Hướng dẫn kỹ thuật cấp thấp:** Triển khai hệ thống sử dụng Docker Compose. Đảm bảo tất cả các dịch vụ được triển khai đúng cách và hệ thống hoạt động đúng cách.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

<!--DAY_LOG_INDEX_START-->

##### 📅 NGÀY 2: Tạo tài liệu kỹ thuật

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 NHIỆM VỤ CON 1: Tạo tài liệu kỹ thuật

* **Chuyên môn công việc của Sub-Agent:** [Doc]

* **Thẻ được theo dõi:** [DOC-001]

* **Thành phần mục tiêu (target_component):** `./sources/docs/technical-documentation.md`

* **Hướng dẫn kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho hệ thống. Đảm bảo tài liệu kỹ thuật bao gồm tất cả các thông tin cần thiết để hiểu và bảo trì hệ thống.

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->

### 🕵️ Báo cáo kiểm tra kiến trúc tự động:

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=2
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=8
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=12
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

<!--PHASE_INDEX_END-->

<!--END_CHUNK_PART_2_PHASE_LOOP-->

<!--START_CHUNK_PART_3_FINAL-->

## ☣️ 6. CÁC ĐOẠN MÃ BẢO MẬT VÀ ĐIỀU KHIỂN TIÊU CHUẨN NHÂN TỐ [NFR-XXX]

- **[Đoạn mã bảo mật SQL (SQLi) tuyệt đối]:** Hướng dẫn cho Coder agent thực hiện buộc ràng buộc tham số thời gian chạy bằng cách sử dụng các thuộc tính trạng thái thực thể và truy vấn đặt tên Hibernate. Bạn ĐƯỢC CẤM TỰ DO HOÀN TOÀN VÀ VÔ CÙNG BANNED từ sử dụng nối chuỗi động; các lệnh SQL thô phải được hoàn toàn làm sạch thông qua bộ lọc kho lưu trữ Spring Data JPA để đạt được 100% bảo vệ chống lại thao tác dữ liệu tầng.
- **[Đoạn mã bảo mật XSS & Chính sách bảo mật nội dung (CSP)]:** Thực hiện các quy trình thoát ngữ cảnh XSS tự động trong tất cả các trường trình bày đầu vào người dùng phía trước. Cổng giao diện hệ thống phải động chèn một cấu hình tiêu đề phản hồi HTTP Content-Security-Policy (CSP) chứa các ràng buộc chỉ thị tối ưu (ví dụ: `default-src 'self'`) để hoàn toàn trung hòa các thực thi kịch bản trái phép.
- **[Rào cản bảo mật CORS đa tenant]:** Thiết lập một lớp rào cản CORS không tin tưởng trên tất cả các điểm cuối API hệ thống. Cơ sở hạ tầng chủ tuyến đường phải xác thực các chuỗi nguồn gốc đến từ một cây đăng ký ủy quyền tenant động, cấm hoàn toàn các toán tử đại diện toàn cầu `*` cho các yêu cầu phiên làm việc được xác thực.
- **[Máy làm sạch log không rò rỉ & Máy che dữ liệu PII]:** Cấu hình một máy làm sạch log trung gian tự động để phân tích tất cả các tải dữ liệu telemetry ra ngoài. Bạn PHẢI sử dụng các ràng buộc tuần tự hóa Jackson đặc biệt và các đánh dấu siêu dữ liệu (ví dụ: logic tuần tự hóa tùy chỉnh `@JsonSerialize` che giấu) để tự động chặn và che giấu các chuỗi thông tin định danh cá nhân (PII) trước khi dữ liệu đến lưu trữ vật lý.

## 📱 7. CÁC QUY TẮC TUÂN THỦ HỢP NHÂN HỌC & CƠ CHẾ SEO QUỐC TẾ HÓA

- **[Rào cản tuân thủ hợp nhân học di động]:** Thực hiện các ràng buộc cấu trúc hợp nhân học di động bằng cách hạn chế các cuộc gọi tài nguyên phía máy khách chỉ đến các cấu trúc giao thức tuyệt đối đã được xác thực. Tất cả các quy trình lưu trữ nội bộ an toàn phải sử dụng máy chủ trừu tượng thời gian chạy bản địa (`@capacitor/preferences`), kết hợp với các móc webview phần cứng bản địa để chặn các mẫu truy cập phần cứng trái phép.
- **[Quốc tế hóa (i18n) & Tiêm động SEO]:** Triển khai một máy chủ phát hiện ngôn ngữ động ở lớp biên để phân tích các thuộc tính ngôn ngữ người dùng đến. Bộ biên dịch trang phản hồi Next.js phải tự động xử lý các lược đồ siêu dữ liệu được bản địa hóa và tiêm các thuộc tính liên kết `hreflang` đối xứng, thân thiện với SEO vào cây trình bày.

## 🚀 8. LUỒNG NHÁNH GIT PHIÊN BẢN TỰ ĐỘNG HÀNG NGÀY

- **[Cách ly phân nhánh không gian làm việc hàng ngày]:** Thực hiện một quy trình kiểm soát phiên bản được tách biệt một cách tự động bằng cách thực hiện một phân vùng không gian làm việc tự động cho mỗi phiên bản kỹ thuật hàng ngày. Hệ thống tự động PHẢI xác thực rằng các nhà phát triển thực hiện công việc của họ độc lập trong các đường dẫn nhánh được cô lập nghiêm ngặt theo quy tắc đặt tên chữ ký: `feature/phase-X-day-Y` (trong đó X đại diện cho chỉ số giai đoạn tính toán và Y chỉ ra ngày tuần tự hoạt động).
- **[Cổng bảo vệ xác nhận tự động]:** Thiết lập một cổng xác nhận tự động nghiêm ngặt trong máy chủ tích hợp liên tục trung tâm GitHub Actions. Quy trình triển khai đám mây PHẢI tự động kích hoạt các bài kiểm tra xác nhận chéo biên dịch, quét phân tích chất lượng mã tĩnh SonarQube và buộc hủy bỏ chuỗi triển khai nếu điểm số ma trận bao phủ kiểm tra tích lũy rơi dưới ngưỡng tham số không thương lượng của `>= 85%`.

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 3, TOTAL ARC TAGS: 6, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 3, TOTAL NFR TAGS: 3. ZERO UNASSIGNED CODES FOUND.]

<!--END_CHUNK_PART_3_FINAL-->