## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕI

### 1.1. MÔ HÌNH KIẾN TRÚC CỐT LÕI & CÁC BOUNDARY

- Kiến trúc microservices phân tách rõ ràng: Auth, User, Center, Course, Attendance, Notification, Promotion, Report.
- Mô hình CQRS: các lệnh (Command) ghi dữ liệu, truy vấn (Query) đọc dữ liệu, sử dụng Event Store để lưu trữ sự kiện.
- Reactive core: Quarkus với Mutiny, xử lý bất đồng bộ, giảm độ trễ, hỗ trợ streaming.
- Event‑driven: Kafka chủ đạo cho các sự kiện quan trọng (attendance, enrollment, promotion), Redis cho cache và session.
- API Gateway: Quarkus RESTEasy, bảo vệ bằng JWT, rate‑limit, CORS.
- GKE orchestrator: Deploy microservices, auto‑scale, HPA, liveness/readiness probes.
- CI/CD: GitHub Actions, Docker multi‑stage, Helm charts, GCP Artifact Registry.

### 1.2. CÁC ĐỘI CHUỘT DỮ LIỆU & HỆ THỐNG CƠ BẢN

- Ingestion gateway: Firebase Auth + OAuth2, chuyển đổi thành JWT, lưu vào PostgreSQL.
- Topic topology: `attendance.events`, `enrollment.events`, `notification.events`, `promotion.events`.
- Fan‑out: Kafka → Firebase Cloud Messaging, Zalo API, email service.
- Cross‑channel: RESTful CRUD, gRPC cho internal microservice, gRPC‑JSON transcoding.
- Data replication: PostgreSQL read replicas cho báo cáo, read‑only replicas cho frontend.
- Cache layer: Redis, TTL 5 phút cho dữ liệu read‑heavy (course list, center list).

## 📁 2. CỤC THỂ CÔNG NGHỆ & THƯ VIỆN HỆ THỐNG

- **Backend Infrastructure Core Stack**  
  - Java 17, Quarkus 3.6.0, Hibernate ORM 6.2, Flyway 9.22, PostgreSQL 15, Redis 7, Kafka 3.6, Firebase Admin SDK 9.1, Google Cloud SDK 420, Docker 24, Helm 3.12, GCP Artifact Registry, GKE 1.28.  
- **Frontend & Cross‑Platform UI Mobile Stack**  
  - Next.js 13.4, React 18, TypeScript 5.0, Tailwind CSS 3.3, React Query 4.29, React Native 0.73, Expo SDK 49, TypeScript 5.0, React Navigation 6, Firebase SDK 10.0, Zalo SDK 1.0.  

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. QUY TẮC BẢO VỆ & THUẬT NGHIỆP DOANH NGHIỆP

- **Địa chỉ repository**: Tất cả các file bắt đầu bằng `./sources/`.  
- **Dynamic Directory Prefixing**:  
  - Backend: `./sources/backend/<service-name>/` (ví dụ: `./sources/backend/auth/`).  
  - Frontend: `./sources/frontend/` (ví dụ: `./sources/frontend/web/`).  
  - DevOps: `./sources/infra/`.  
  - Docs: `./sources/docs/`.  
- **Java Package Standard**: `org.nlh4j.saas.membershiphub`.  
- **Tester Target Path Syntax**: `<source_component>;<test_suite_file>` (cả hai bắt đầu bằng `./sources/`).  
- **OWASP Top‑10 Mitigations**: Prepared statements, CSRF tokens, CSP headers, rate limiting, input validation.  
- **GDPR/CCPA Compliance**: Data export JSON, deletion on request, consent flags.  
- **Backup & DR**: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24h, GKE cluster backup vùng khác.  
- **Performance & Availability**: 200 ms avg API, 99.9 % uptime, HPA, read replicas, auto‑failover.  
- **Security**: TLS 1.3, AES‑256 at rest, JWT 15 min, refresh 7 days.  
- **Multi‑Language**: Externalized strings, locale switching, SEO hreflang.

# BẢNG NGHIỆP ĐỀ TOÀN CẦU: membership-hub

## 4.1. BẢNG NGHIỆP ĐỀ TOÀN CẦU MASTER PRODUCT BACKLOG

<!--START_BACKLOG_SYNOPSIS_GRID-->

| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | REQ-001 | Triển khai endpoint đăng ký người dùng | Application Code | [REQ-001] |
| 2 | REQ-002 | Triển khai endpoint đăng nhập xã hội | Application Code | [REQ-002] |
| 3 | REQ-003 | Triển khai endpoint phân quyền người dùng | Application Code | [REQ-003] |
| 4 | REQ-004 | Triển khai endpoint danh sách trung tâm | Application Code | [REQ-004] |
| 5 | REQ-005 | Triển khai endpoint CRUD trung tâm | Application Code | [REQ-005] |
| 6 | REQ-006 | Triển khai endpoint gán/huỷ quản trị trung tâm | Application Code | [REQ-006] |
| 7 | REQ-007 | Triển khai endpoint danh sách khóa học | Application Code | [REQ-007] |
| 8 | REQ-008 | Triển khai endpoint CRUD khóa học | Application Code | [REQ-008] |
| 9 | REQ-009 | Triển khai endpoint gán/huỷ giáo viên cho khóa học | Application Code | [REQ-009] |
| 10 | REQ-010 | Triển khai endpoint duyệt khóa học | Application Code | [REQ-010] |
| 11 | REQ-011 | Triển khai endpoint đăng ký học viên | Application Code | [REQ-011] |
| 12 | REQ-012 | Triển khai endpoint quét mã QR điểm danh | Application Code | [REQ-012] |
| 13 | REQ-013 | Triển khai logic idempotent điểm danh | Application Code | [REQ-013] |
| 14 | REQ-014 | Triển khai endpoint hiển thị thẻ hội viên | Application Code | [REQ-014] |
| 15 | REQ-015 | Triển khai endpoint gia hạn thẻ hội viên | Application Code | [REQ-015] |
| 16 | REQ-016 | Triển khai logic gửi thông báo | Application Code | [REQ-016] |
| 17 | REQ-017 | Triển khai endpoint CRUD khuyến mãi | Application Code | [REQ-017] |
| 18 | REQ-018 | Triển khai endpoint CRUD thông báo | Application Code | [REQ-018] |
| 19 | REQ-019 | Triển khai endpoint tích hợp chatbot AI | Application Code | [REQ-019] |
| 20 | REQ-020 | Triển khai giao diện người dùng di động | Application Code | [REQ-020] |
| 21 | REQ-021 | Triển khai logic push notification | Application Code | [REQ-021] |
| 22 | REQ-022 | Triển khai logic phát hiện ngôn ngữ | Application Code | [REQ-022] |
| 23 | REQ-023 | Triển khai logic SEO đa ngôn ngữ | Application Code | [REQ-023] |
| 24 | REQ-024 | Triển khai endpoint báo cáo điểm danh | Application Code | [REQ-024] |
| 25 | EXC-001 | Xử lý mất kết nối trong quét QR | Application Code | [EXC-001] |
| 26 | EXC-002 | Xử lý trùng lặp điểm danh | Application Code | [EXC-002] |
| 27 | EXC-003 | Xử lý thất bại gửi thông báo | Application Code | [EXC-003] |
| 28 | EXC-004 | Xử lý lỗi xác thực đầu vào | Application Code | [EXC-004] |
| 29 | EXC-005 | Xử lý phục hồi sau sự cố | Application Code | [EXC-005] |
| 30 | DAT-001 | Định nghĩa bảng Users | Enterprise Documentation | [DAT-001] |
| 31 | DAT-002 | Định nghĩa bảng Roles | Enterprise Documentation | [DAT-002] |
| 32 | DAT-003 | Định nghĩa bảng Centers | Enterprise Documentation | [DAT-003] |
| 33 | DAT-004 | Định nghĩa bảng Courses | Enterprise Documentation | [DAT-004] |
| 34 | DAT-005 | Định nghĩa bảng Enrollments | Enterprise Documentation | [DAT-005] |
| 35 | DAT-006 | Định nghĩa bảng Attendance | Enterprise Documentation | [DAT-006] |
| 36 | DAT-007 | Định nghĩa bảng StudentCards | Enterprise Documentation | [DAT-007] |
| 37 | DAT-008 | Định nghĩa bảng Notifications | Enterprise Documentation | [DAT-008] |
| 38 | DAT-009 | Định nghĩa bảng Promotions | Enterprise Documentation | [DAT-009] |
| 39 | DAT-010 | Định nghĩa bảng Announcements | Enterprise Documentation | [DAT-010] |
| 40 | DAT-011 | Định nghĩa bảng SystemSettings | Enterprise Documentation | [DAT-011] |
| 41 | ARC-001 | Mô tả vai trò System Admin | Enterprise Documentation | [ARC-001] |
| 42 | ARC-002 | Mô tả vai trò Center Admin | Enterprise Documentation | [ARC-002] |
| 43 | ARC-003 | Mô tả vai trò Manager | Enterprise Documentation | [ARC-003] |
| 44 | ARC-004 | Mô tả vai trò Teacher | Enterprise Documentation | [ARC-004] |
| 45 | ARC-005 | Mô tả vai trò Student | Enterprise Documentation | [ARC-005] |
| 46 | ARC-006 | Mô tả luồng xác thực | Enterprise Documentation | [ARC-006] |
| 47 | ARC-007 | Mô tả luồng điểm danh QR | Enterprise Documentation | [ARC-007] |
| 48 | ARC-008 | Mô tả luồng thông báo | Enterprise Documentation | [ARC-008] |
| 49 | ARC-009 | Mô tả luồng tích hợp mobile backend | Enterprise Documentation | [ARC-009] |
| 50 | ARC-010 | Mô tả công nghệ & hạ tầng | Enterprise Documentation | [ARC-010] |
| 51 | NFR-001 | Định nghĩa hiệu suất hệ thống | Enterprise Documentation | [NFR-001] |
| 52 | NFR-002 | Định nghĩa độ sẵn sàng | Enterprise Documentation | [NFR-002] |
| 53 | NFR-003 | Định nghĩa bảo mật | Enterprise Documentation | [NFR-003] |
| 54 | NFR-004 | Định nghĩa khả năng mở rộng & sẵn sàng | Enterprise Documentation | [NFR-004] |
| 55 | NFR-005 | Định nghĩa kích thước image Docker | Enterprise Documentation | [NFR-005] |
| 56 | NFR-006 | Định nghĩa ghi log & audit | Enterprise Documentation | [NFR-006] |
| 57 | NFR-007 | Định nghĩa hỗ trợ đa ngôn ngữ | Enterprise Documentation | [NFR-007] |
| 58 | NFR-008 | Định nghĩa tuân thủ GDPR/CCPA | Enterprise Documentation | [NFR-008] |
| 59 | NFR-009 | Định nghĩa sao lưu & khôi phục | Enterprise Documentation | [NFR-009] |
| **SUMMARY** | **Tổng Công Việc Hệ Thống** | **TOTAL:** 59 | **STATUS:** Verified | **COVERAGE:** 100% |

<!--END_BACKLOG_SYNOPSIS_GRID-->

## 4.2. BẢNG NGHIỆP ĐỀ TOÀN CẦU SYNOPSIS GRID

| Task ID | Phase |
| :--- | :--- |
| REQ-001 | 1 |
| REQ-002 | 1 |
| REQ-003 | 1 |
| REQ-004 | 1 |
| REQ-005 | 1 |
| REQ-006 | 1 |
| REQ-007 | 1 |
| REQ-008 | 1 |
| REQ-009 | 1 |
| REQ-010 | 1 |
| REQ-011 | 1 |
| REQ-012 | 1 |
| REQ-013 | 2 |
| REQ-014 | 2 |
| REQ-015 | 2 |
| REQ-016 | 2 |
| REQ-017 | 2 |
| REQ-018 | 2 |
| REQ-019 | 2 |
| REQ-020 | 2 |
| REQ-021 | 2 |
| REQ-022 | 2 |
| REQ-023 | 2 |
| REQ-024 | 2 |
| EXC-001 | 3 |
| EXC-002 | 3 |
| EXC-003 | 3 |
| EXC-004 | 3 |
| EXC-005 | 3 |
| DAT-001 | 3 |
| DAT-002 | 3 |
| DAT-003 | 3 |
| DAT-004 | 3 |
| DAT-005 | 3 |
| DAT-006 | 3 |
| DAT-007 | 4 |
| DAT-008 | 4 |
| DAT-009 | 4 |
| DAT-010 | 4 |
| DAT-011 | 4 |
| ARC-001 | 4 |
| ARC-002 | 4 |
| ARC-003 | 4 |
| ARC-004 | 4 |
| ARC-005 | 4 |
| ARC-006 | 4 |
| ARC-007 | 4 |
| ARC-008 | 4 |
| ARC-009 | 4 |
| ARC-010 | 4 |
| NFR-001 | 5 |
| NFR-002 | 5 |
| NFR-003 | 5 |
| NFR-004 | 5 |
| NFR-005 | 5 |
| NFR-006 | 5 |
| NFR-007 | 5 |
| NFR-008 | 5 |
| NFR-009 | 5 |

## 5. LỊCH LÀM VIỆC NGÀY

### Giai đoạn 1: Đặc tả Kiến trúc Chi tiết

- **DAY 1:**
  - **REQ-001**: Coder, ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/RegisterController.java, [REQ-001]
  - **REQ-002**: Coder, ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/SocialAuthController.java, [REQ-002]
  - **REQ-003**: Coder, ./sources/backend/user-service/src/main/java/com/membershiphub/user/RoleController.java, [REQ-003]
  - **REQ-004**: Coder, ./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterController.java, [REQ-004]
  - **REQ-005**: Coder, ./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterController.java, [REQ-005]
  - **REQ-006**: Coder, ./sources/backend/user-service/src/main/java/com/membershiphub/user/CenterAdminController.java, [REQ-006]
- **DAY 2:**
  - **REQ-007**: Coder, ./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java, [REQ-007]
  - **REQ-008**: Coder, ./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java, [REQ-008]
  - **REQ-009**: Coder, ./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseTeacherController.java, [REQ-009]
  - **REQ-010**: Coder, ./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java, [REQ-010]
  - **REQ-011**: Coder, ./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentController.java, [REQ-011]
  - **REQ-012**: Coder, ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceController.java, [REQ-012]

### Giai đoạn 2: Đặc tả Kiến trúc Chi tiết

- **DAY 1:**
  - **REQ-013**: Coder, ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java, [REQ-013]
  - **REQ-014**: Coder, ./sources/backend/card-service/src/main/java/com/membershiphub/card/CardController.java, [REQ-014]
  - **REQ-015**: Coder, ./sources/backend/card-service/src/main/java/com/membershiphub/card/CardController.java, [REQ-015]
  - **REQ-016**: Coder, ./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationService.java, [REQ-016]
  - **REQ-017**: Coder, ./sources/backend/promotion-service/src/main/java/com/membershiphub/promotion/PromotionController.java, [REQ-017]
  - **REQ-018**: Coder, ./sources/backend/announcement-service/src/main/java/com/membershiphub/announcement/AnnouncementController.java, [REQ-018]
- **DAY 2:**
  - **REQ-019**: Coder, ./sources/backend/chatbot-service/src/main/java/com/membershiphub/chatbot/ChatbotController.java, [REQ-019]
  - **REQ-020**: Coder, ./sources/frontend/mobile-app/src/components/RoleBasedNavigation.vue, [REQ-020]
  - **REQ-021**: Coder, ./sources/backend/notification-service/src/main/java/com/membershiphub/notification/PushNotificationService.java, [REQ-021]
  - **REQ-022**: Coder, ./sources/backend/i18n-service/src/main/java/com/membershiphub/i18n/LocaleService.java, [REQ-022]
  - **REQ-023**: Coder, ./sources/frontend/web-app/src/components/SeoMeta.vue, [REQ-023]
  - **REQ-024**: Coder, ./sources/backend/report-service/src/main/java/com/membershiphub/report/AttendanceReportService.java, [REQ-024]

### Giai đoạn 3: Đặc tả Kiến trúc Chi tiết

- **DAY 1:**
  - **EXC-001**: Coder, ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/RetryHandler.java, [EXC-001]
  - **EXC-002**: Coder, ./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java, [EXC-002]
  - **EXC-003**: Coder, ./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationRetryService.java, [EXC-003]
  - **EXC-004**: Coder, ./sources/backend/auth-service/src/main/java/com/membershiphub/auth/ValidationException.java, [EXC-004]
  - **EXC-005**: Coder, ./sources/backend/report-service/src/main/java/com/membershiphub/report/RecoveryService.java, [EXC-005]
  - **DAT-001**: Doc, ./sources/docs/db-schema/Users.sql, [DAT-001]
  - **DAT-002**: Doc, ./sources/docs/db-schema/Roles.sql, [DAT-002]
- **DAY 2:**
  - **DAT-003**: Doc, ./sources/docs/db-schema/Centers.sql, [DAT-003]
  - **DAT-004**: Doc, ./sources/docs/db-schema/Courses.sql, [DAT-004]
  - **DAT-005**: Doc, ./sources/docs/db-schema/Enrollments.sql, [DAT-005]
  - **DAT-006**: Doc, ./sources/docs/db-schema/Attendance.sql, [DAT-006]
  - **DAT-007**: Doc, ./sources/docs/db-schema/StudentCards.sql, [DAT-007]
  - **DAT-008**: Doc, ./sources/docs/db-schema/Notifications.sql, [DAT-008]
  - **DAT-009**: Doc, ./sources/docs/db-schema/Promotions.sql, [DAT-009]

### Giai đoạn 4: Đặc tả Kiến trúc Chi tiết

- **DAY 1:**
  - **DAT-010**: Doc, ./sources/docs/db-schema/Announcements.sql, [DAT-010]
  - **DAT-011**: Doc, ./sources/docs/db-schema/SystemSettings.sql, [DAT-011]
  - **ARC-001**: Doc, ./sources/docs/architecture/roles.md, [ARC-001]
  - **ARC-002**: Doc, ./sources/docs/architecture/roles.md, [ARC-002]
  - **ARC-003**: Doc, ./sources/docs/architecture/roles.md, [ARC-003]
  - **ARC-004**: Doc, ./sources/docs/architecture/roles.md, [ARC-004]
  - **ARC-005**: Doc, ./sources/docs/architecture/roles.md, [ARC-005]
  - **ARC-006**: Doc, ./sources/docs/architecture/auth-flow.md, [ARC-006]
- **DAY 2:**
  - **ARC-007**: Doc, ./sources/docs/architecture/attendance-flow.md, [ARC-007]
  - **ARC-008**: Doc, ./sources/docs/architecture/notification-flow.md, [ARC-008]
  - **ARC-009**: Doc, ./sources/docs/architecture/mobile-integration.md, [ARC-009]
  - **ARC-010**: Doc, ./sources/docs/architecture/tech-stack.md, [ARC-010]
  - **NFR-001**: Doc, ./sources/docs/requirements/performance.md, [NFR-001]
  - **NFR-002**: Doc, ./sources/docs/requirements/availability.md, [NFR-002]
  - **NFR-003**: Doc, ./sources/docs/requirements/security.md, [NFR-003]
  - **NFR-004**: Doc, ./sources/docs/requirements/scalability.md, [NFR-004]

### Giai đoạn 5: Đặc tả Kiến trúc Chi tiết

- **DAY 1:**
  - **NFR-005**: Doc, ./sources/docs/requirements/docker-image-size.md, [NFR-005]
  - **NFR-006**: Doc, ./sources/docs/requirements/logging.md, [NFR-006]
  - **NFR-007**: Doc, ./sources/docs/requirements/multilanguage.md, [NFR-007]
  - **NFR-008**: Doc, ./sources/docs/requirements/gdpr.md, [NFR-008]
  - **NFR-009**: Doc, ./sources/docs/requirements/backup.md, [NFR-009]