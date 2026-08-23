# Giai đoạn 5: <!--PHASE_NAME_START-->Hạ Tầng DevOps, Dịch Vụ Báo Cáo Và Bàn Giao Production<!--PHASE_NAME_END-->

## 📊 Kiểm soát Tài liệu

| Hạng mục | Chi tiết |
| :--- | :--- |
| **ID Bản thiết kế** | ARCH-20260823050512 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Hạ Tầng DevOps, Dịch Vụ Báo Cáo Và Bàn Giao Production<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 5 hoàn thiện chuỗi bàn giao production của nền tảng membership-hub trên ba trụ cột kỹ thuật. Thứ nhất, reporting-service cung cấp xuất báo cáo điểm danh CSV theo trung tâm và khoảng ngày với bốn cột StudentName, CourseName, AttendanceDate, Status qua GET /api/v1/reports/attendance/csv [REQ-024], cơ chế phát lại FIFO cho các bản ghi quét QR tồn đọng hậu outage kèm thông báo phục hồi tới người dùng bị ảnh hưởng [EXC-005], và bảng điều khiển real-time totalStudents, activeCourses, upcomingSessions đọc qua PostgreSQL read replica để cách ly workload báo cáo khỏi OLTP [REQ-025]. Thứ hai, chốt nền tảng công nghệ chuẩn Java/Quarkus, PostgreSQL, Redis session caching, FCM/APNs, Zalo API, GitHub Actions [ARC-010] và cung cấp hạ tầng DevOps hoàn chỉnh: Dockerfile multi-stage base image dưới 200MB và final image dưới 500MB [NFR-005], Terraform provisioning VPC/IAM/Storage trên GCP, manifests GKE với HPA kích hoạt khi CPU vượt 70% hoặc latency vượt 300ms [NFR-004], failover liên cluster đạt uptime 99.9% [NFR-002], TLS 1.3/AES-256 kèm mitigations OWASP Top 10 [NFR-003], backup PITR 24h đa region [NFR-009], audit log lưu trữ 1 năm [NFR-006], workflow GDPR/CCPA export/deletion và consent management [NFR-008], cổng hiệu năng p95 200ms [NFR-001] và hỗ trợ đa ngôn ngữ en/vi/es [NFR-007]. Thứ ba, đóng gói bộ tài liệu doanh nghiệp gồm blueprint kiến trúc tổng thể, hợp đồng OpenAPI tham chiếu hợp nhất, hướng dẫn vận hành bản địa hóa vi/en/es và quy trình audit log cùng quản lý consent [NFR-006], [NFR-007], [NFR-008], kết thúc bằng kiểm toán sẵn sàng production GO/NO-GO đối chiếu toàn bộ ràng buộc phi chức năng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/23 05:05:12 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 1. Phạm vi Vận hành Giai đoạn & Mục tiêu

Giai đoạn 5 bàn giao trọn vẹn Task 26, Task 27, Task 31, Task 32 và Task 33 của Master Backlog, đóng vai trò giai đoạn cuối cùng của vòng đời kiến trúc membership-hub trên ba trụ cột: dịch vụ báo cáo, hạ tầng DevOps production và khối tài liệu doanh nghiệp.

Thứ nhất, reporting-service kiến tạo lớp phân tích và báo cáo: AttendanceReportController exposing GET /api/v1/reports/attendance/csv nhận tham số centerId, fromDate, toDate, xác thực bearer JWT kèm phạm vi tenant trước khi truy vấn, stream phản hồi text/csv charset=UTF-8 với bốn cột StudentName, CourseName, AttendanceDate, Status đúng thứ tự [REQ-024]; AttendanceCsvReportService sinh dòng CSV từ tập hợp Attendance join Users và Courses theo chuẩn escape RFC 4180 với streaming fetch size chống OOM trên tập dữ liệu lớn; OutageReplayService thực thi hàng đợi phát lại FIFO cho các bản ghi quét QR tồn đọng hậu outage dựa trên timestamp gốc, áp dụng idempotency qua ràng buộc unique (studentId, courseId, attendanceDate), khóa phân tán Redis chặn hai phiên replay song song, và sau khi hoàn tất đẩy thông báo "sự kiện đã phục hồi" tới người dùng liên quan [EXC-005]; DashboardSummaryController exposing GET /api/v1/reports/dashboard/summary trả ba thẻ chỉ số totalStudents, activeCourses, upcomingSessions (7 ngày tới) định tuyến toàn bộ truy vấn tổng hợp qua datasource read-only trỏ tới PostgreSQL read replica để cách ly workload báo cáo khỏi OLTP [REQ-025].

Thứ hai, giai đoạn chốt nền tảng công nghệ production [ARC-010] và cung cấp hạ tầng DevOps end-to-end: Dockerfile multi-stage ép base image nhỏ hơn 200 MB và final image nhỏ hơn 500 MB [NFR-005]; Terraform provisioning VPC regional, IAM least privilege với Workload Identity, Cloud Storage phân tầng backup/audit-log, Cloud SQL PostgreSQL 16 HA kèm read replica chuyên dụng và backup PITR 24h đa region [NFR-009]; manifests GKE regional cluster trải 3 zone bảo đảm failover tự động uptime 99.9% [NFR-002], HPA scale theo CPU vượt 70% hoặc custom metric latency p95 vượt 300 ms [NFR-004]; ingress ManagedCertificate ép minimum TLS 1.3 tại load balancer, mã hóa Secret bằng Cloud KMS AES-256, NetworkPolicy mặc định deny-all [NFR-003]; Log Sink thu audit log vào bucket retention locked 365 ngày phục vụ lưu trữ truy vết 1 năm [NFR-006]; pipeline CI/CD GitHub Actions tích hợp cổng chất lượng SonarQube, Trivy scan, terraform plan/apply có bước phê duyệt thủ công và gate hiệu năng chặn promote nếu p95 vượt 200 ms [NFR-001]; PrivacyComplianceController thực thi workflow GDPR/CCPA export dữ liệu cá nhân dạng JSON, xóa vĩnh viễn theo yêu cầu và quản lý đồng ý truyền thông marketing [NFR-008].

Thứ ba, khối tài liệu doanh nghiệp được hoàn thiện gồm blueprint kiến trúc tổng thể phản chiếu topology 10 microservices đã triển khai, hợp đồng OpenAPI tham chiếu hợp nhất toàn bộ dịch vụ, hướng dẫn vận hành bản địa hóa vi/en/es đáp ứng externalize chuỗi UI và chuyển locale không reload trang [NFR-007], quy trình audit log cùng quản lý consent GDPR/CCPA [NFR-006], [NFR-008], khép lại bằng kiểm toán sẵn sàng production GO/NO-GO đối chiếu từng ràng buộc phi chức năng từ [NFR-001] đến [NFR-009].

## 2. Phạm vi Kỹ thuật Được phép & Ranh giới Thư mục (Tệp, đường dẫn và Endpoint)

* **Ma trận thư mục Backend được phép:**
    * ./sources/backend/reporting-service/pom.xml [ARC-000]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/api/AttendanceReportController.java [REQ-024]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/service/AttendanceCsvReportService.java [REQ-024]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/service/OutageReplayService.java [EXC-005], [REQ-024]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/api/DashboardSummaryController.java [REQ-025]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/repository/DashboardAggregationRepository.java [REQ-025], [NFR-004]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/cache/DashboardCacheService.java [REQ-025], [ARC-010]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/exception/ReportingExceptionMapper.java [EXC-005]
    * ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/privacy/PrivacyComplianceController.java [NFR-008], [NFR-006]
    * ./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/service/AttendanceCsvReportServiceTest.java [REQ-024]
    * ./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/OutageReplayIntegrationTest.java [EXC-005]
    * ./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/repository/DashboardAggregationRepositoryTest.java [REQ-025]
    * ./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/DashboardPerformanceIntegrationTest.java [NFR-001], [REQ-025]
    * ./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/PrivacyComplianceIntegrationTest.java [NFR-008]
* **Ma trận thư mục Hạ tầng DevOps được phép:**
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
* **Ma trận thư mục Tài liệu được phép:**
    * ./sources/docs/api-reporting-service.md [REQ-024], [REQ-025]
    * ./sources/docs/runbook-reporting-deployment.md [REQ-024], [REQ-025]
    * ./sources/docs/architecture-blueprint.md [ARC-010], [NFR-002]
    * ./sources/docs/openapi-reference.md [ARC-010]
    * ./sources/docs/localization-operations-guide.md [NFR-007]
    * ./sources/docs/compliance-audit-consent-guide.md [NFR-006], [NFR-008]
    * ./sources/docs/production-readiness-review.md [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
* **Mẫu định tuyến Endpoint được phép trong giai đoạn:**
    * GET /api/v1/reports/attendance/csv — BEARER JWT, role=SYSTEM_ADMIN (toàn bộ trung tâm) / CENTER_ADMIN (trong phạm vi managed_center_id) [REQ-024]
    * GET /api/v1/reports/dashboard/summary — BEARER JWT, role=SYSTEM_ADMIN / CENTER_ADMIN [REQ-025]
    * POST /api/v1/reports/outage/replay — BEARER JWT, role=SYSTEM_ADMIN / CENTER_ADMIN [EXC-005]
    * GET /api/v1/privacy/export — BEARER JWT, mọi vai trò đã xác thực (danh tính suy từ claim sub) [NFR-008]
    * DELETE /api/v1/privacy/data — BEARER JWT, mọi vai trò đã xác thực (danh tính suy từ claim sub) [NFR-008]
    * PUT /api/v1/privacy/consent — BEARER JWT, mọi vai trò đã xác thực (danh tính suy từ claim sub) [NFR-008]
* **Ranh giới cấm xâm phạm:** Giai đoạn 5 nghiêm cấm tái tạo bất kỳ tệp nào đã tồn tại từ Giai đoạn 1 đến Giai đoạn 4 (descriptor cha, workspace frontend gốc, auth-service, db-migrations chuỗi trung tâm V1–V9, center-service, course-service, api-gateway, enrollment-service, attendance-service, card-service, notification-service, promotion-service, chatbot-service); nghiêm cấm phát sinh migration DDL mới vì lược đồ đã đóng băng ở trạng thái 11 bảng lõi cộng các cột theo dõi giao hàng của Giai đoạn 4; reporting-service chỉ tiêu thụ schema hiện hữu ở chế độ đọc/tổng hợp.

* **INVARIANT KHUNG NỀN TẢNG BẮT BUỘC (PLATFORM SKELETON MANIFEST INVARIANTS)**:
    * Descriptor hạ tầng repository gốc `./sources/backend/pom.xml` và workspace frontend `./sources/frontend/package.json` cùng `./sources/frontend/tsconfig.json` đã được neo vĩnh viễn tại Giai đoạn 1 - NGÀY 1 theo token kiến trúc [ARC-000]; Giai đoạn 5 nghiêm cấm tái tạo hoặc ghi đè các descriptor nền móng này.
    * Module reporting-service gia nhập chuỗi microservices ở giai đoạn này bắt buộc đăng ký descriptor module con độc lập `./sources/backend/reporting-service/pom.xml` kế thừa parent membership-hub-backend TRƯỚC khi phát hành bất kỳ thành phần mã nguồn ứng dụng nào của module; toàn bộ descriptor scaffolding sinh ra phải ánh xạ nghiêm ngặt vào token theo dõi kiến trúc [ARC-000].
    * Hai ứng dụng client web-app và mobile-app không phát sinh thay đổi nguồn mới trong Giai đoạn 5; mọi chỉnh sửa giao diện liên quan báo cáo/dashboard được giới hạn ở mức cấu hình tiêu thụ endpoint reporting qua axios interceptor hiện hữu.

## 3. Chỉ đạo Chức năng Sub-Agent Chuyên trách

Theo ma trận phân công của Giai đoạn 5, toàn bộ bảy Sub-Agent được kích hoạt đồng thời: Coder, Tester, Reviewer, Doc, Docker, GCP và GKE.

* **Coder**: Đóng vai trò Lập trình viên Ứng dụng Cấp cao/Principal. Chịu trách nhiệm hiện thực mã nguồn ứng dụng thuần túy của reporting-service: descriptor Maven module con; controller xuất CSV, service sinh luồng RFC 4180, service phát lại FIFO hậu outage, controller dashboard, repository tổng hợp trên read replica, service cache Redis và controller tuân thủ GDPR/CCPA. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng DevOps.
* **Tester**: Đóng vai trò Trưởng QC/QA Principal. Chuyên về kỹ nghệ bộ kiểm thử, xác nhận và cổng chất lượng. Chịu trách nhiệm sinh JUnit unit test, integration test trên Testcontainers PostgreSQL/Redis, profile đo hiệu năng Gatling mô phỏng 10.000 người dùng đồng thời đối chiếu [NFR-001] và kiểm thử vòng đời GDPR/CCPA. Bị cấm sửa mã production. Khi phạm vi kiểm thử mang tính tích hợp tổng thể hoặc E2E không cô lập được một tệp production đơn lẻ, bắt buộc dùng định dạng cặp semicolon với token `INTEGRATION_SCOPE` đứng đầu (ví dụ: `INTEGRATION_SCOPE;./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/OutageReplayIntegrationTest.java`).
* **Doc**: Đóng vai trò Nhà văn Kỹ thuật Principal và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên biên soạn tài liệu đặc tả kỹ thuật, tham chiếu API, runbook triển khai, blueprint kiến trúc và catalog hợp đồng phù hợp topology dự án. Mọi tệp tài liệu phải là đường dẫn tệp tường minh đuôi `.md` nằm trong kho lưu trữ tập trung `./sources/docs/`. Theo luật định giai đoạn, Doc phải được phân công tối thiểu một nhiệm vụ nền móng ngay NGÀY 1 để khởi tạo khung tài liệu markdown tham chiếu API reporting-service tương thích stack Java/Quarkus/PostgreSQL/Redis của ngữ cảnh này.
* **Reviewer**: Chịu trách nhiệm xác minh biên dịch, cổng phân tích tĩnh và vá phòng thủ. Chuyên kiểm toán chất lượng mã reporting-service, phân tích race condition giữa các phiên replay, nhất quán replica–cache, kiểm toán bảo mật IaC theo OWASP Top 10 (đặc biệt least privilege IAM A01 và injection A03), gỡ blocker SonarQube trước khi merge; ký duyệt điều kiện mở khóa giữa các ngày làm việc và phát hành verdict GO/NO-GO cuối giai đoạn.
* **Docker**: Chuyên container hóa, kỹ nghệ Dockerfile multi-stage, tối ưu dung lượng image dưới ngân sách 200 MB base/500 MB final, kịch bản build-push song song kèm Trivy scan và đẩy image đã kiểm chứng lên Artifact Registry.
* **GCP**: Chuyên tự động hóa trên Google Cloud Platform: Terraform provisioning VPC/IAM/Storage/Cloud SQL/backup/audit sink, build-push image lên Artifact Registry khu vực asia-southeast1 và điều phối pipeline CI/CD GitHub Actions với Workload Identity.
* **GKE**: Chuyên điều phối container production trong Google Kubernetes Engine: manifest cụm regional failover, deployment/service cho 10 microservices, cấu hình HPA theo CPU và custom metric latency, ingress TLS 1.3 với ManagedCertificate và triển khai workload vào cụm GKE active.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)

* 100% thẻ truy vết của giai đoạn ([REQ-024], [EXC-005], [REQ-025], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]) được ánh xạ tường minh vào nhật ký ngày qua container `<!--START_TAGS-->` không gaps, không trùng lặp sai ngữ cảnh.
* `mvn -q verify` sạch trên descriptor module con reporting-service; cây Maven không xung đột phiên bản với parent membership-hub-backend và Quarkus BOM 3.15.x; hai datasource (primary + replica) khởi tạo thành công trong profile dev và test.
* Xuất CSV: đúng bốn cột StudentName, CourseName, AttendanceDate, Status theo thứ tự; escape dấu phẩy, ngoặc kép và ngắt dòng theo RFC 4180; charset UTF-8 bảo toàn dấu tiếng Việt; streaming fetch size tránh OOM; mọi truy vấn xuất ghi audit log kèm userId và timestamp [REQ-024].
* Phát lại hậu outage: xử lý FIFO tuyệt đối theo timestamp gốc; idempotent nhờ ràng buộc unique (studentId, courseId, attendanceDate) không nhân bản dòng Attendance; khóa phân tán Redis chặn phiên song song trả 409 REPORTING_REPLAY_LOCK_CONFLICT; hàng đợi rỗng trả 204 REPORTING_REPLAY_QUEUE_EMPTY; thông báo phục hồi được queue cho đúng số người dùng bị ảnh hưởng [EXC-005].
* Dashboard: ba chỉ số totalStudents, activeCourses, upcomingSessions chính xác; toàn bộ truy vấn tổng hợp thực thi trên read replica; Redis cache TTL 60 giây scope theo centerId với fallback truy vấn trực tiếp khi Redis unavailable; p95 latency ≤ 200 ms ở mức 10.000 người dùng đồng thời [REQ-025], [NFR-001], [NFR-004].
* Container: base image nhỏ hơn 200 MB, final image nhỏ hơn 500 MB, user non-root, JVM container-aware flags; Trivy scan chặn pipeline ở mức CRITICAL [NFR-005].
* Hạ tầng GCP: IAM least privilege gắn Workload Identity, bucket chặn public access, tfsec/checkov pass bắt buộc trước terraform apply [NFR-003]; Cloud SQL PostgreSQL 16 HA regional kèm read replica chuyên dụng [NFR-004]; backup hằng ngày 02:00 UTC với PITR cửa sổ 24 giờ và cross-region replication [NFR-009]; audit log sink retention locked 365 ngày [NFR-006].
* Hạ tầng GKE: regional cluster trải 3 zone với failover tự động đạt uptime mục tiêu 99.9% [NFR-002]; HPA minReplicas 2/maxReplicas 20 kích hoạt CPU vượt 70% hoặc latency p95 vượt 300 ms với stabilizationWindow 300 giây [NFR-004]; ingress ép minimum TLS 1.3, Secret mã hóa Cloud KMS AES-256, NetworkPolicy mặc định deny-all [NFR-003].
* GDPR/CCPA: export trả đủ trường dữ liệu cá nhân dạng JSON hợp lệ; deletion xóa triệt để trên mọi bảng liên quan và thu hồi refresh token; consent cập nhật có hiệu lực tức thời; mọi thao tác ghi audit log kèm userId và timestamp; danh tính suy nghiêm ngặt từ claim sub chống leo thang chéo tài khoản theo OWASP A01 [NFR-008].
* Pipeline CI/CD: chuỗi build → unit test → SonarQube quality gate → Trivy scan → build/push image → terraform plan/apply có approval thủ công → kubectl apply qua Workload Identity; gate hiệu năng chặn promote production nếu Gatling p95 vượt 200 ms [NFR-001], [ARC-010].
* Bảy tài liệu ./sources/docs/ hoàn chỉnh, liên kết chéo nhất quán với schema Giai đoạn 1, hợp đồng OpenAPI thực tế và hướng dẫn bản địa hóa vi/en/es [NFR-006], [NFR-007], [NFR-008].
* Độ bao phủ kiểm thử tự động ≥ 85% trên module reporting-service; zero blocker SonarQube; verdict GO/NO-GO được phát hành kèm danh sách hành động khắc phục nếu NO-GO; mọi merge thực hiện qua pull request squash trên nhánh `features/development-phase-5-day-Y` theo quy trình phân nhánh hàng ngày.

## 5. Nhật ký Thực thi Kiến trúc Theo Ngày

### 🌤️ NGÀY 1:
<!--DAY_HEADER_START-->Xây Dựng Lõi Reporting Service Với Xuất CSV Điểm Danh, Phát Lại FIFO Hậu Outage Và Endpoint Tóm Tắt Dashboard Real Time<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.1: Sinh descriptor module con reporting-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module reporting-service kế thừa parent membership-hub-backend mà không tái khai báo phiên bản dependency; đăng ký vào danh sách `<modules>` của descriptor cha sau chatbot-service; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator, quarkus-redis-client (khóa phân tán replay và cache dashboard), quarkus-scheduler (worker quét hàng đợi tồn đọng định kỳ) và quarkus-agroal; cấu hình hai datasource: datasource mặc định trỏ primary PostgreSQL và named datasource `replica` trỏ read replica phục vụ toàn bộ truy vấn tổng hợp báo cáo; thiết lập quarkus.flyway.migrate-at-start=false vì lược đồ đã được sở hữu tập trung bởi chuỗi db-migrations V1–V9 cộng migration V4 của Giai đoạn 4, module này chỉ tiêu thụ schema hiện hữu; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=reporting-service phục vụ đóng gói image ở NGÀY 2; tinh chỉnh Agroal connection pool riêng biệt cho mỗi datasource chịu tải streaming CSV và tổng hợp dashboard; bổ sung dependency test scope junit-jupiter, rest-assured, testcontainers-postgresql và testcontainers-redis làm nền cho suite kiểm thử của Tester.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.2: Controller xuất báo cáo CSV điểm danh theo trung tâm và khoảng ngày

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/api/AttendanceReportController.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-024]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai AttendanceReportController exposing GET /api/v1/reports/attendance/csv nhận tham số centerId (UUID bắt buộc), fromDate và toDate (định dạng yyyy-MM-dd, ràng buộc toDate không sớm hơn fromDate) [REQ-024]; yêu cầu bearer JWT với @RolesAllowed({"SYSTEM_ADMIN","CENTER_ADMIN"}); với vai trò CENTER_ADMIN, đối chiếu centerId trên đường dẫn với managed_center_id trong claim phiên và trả 403 TENANT_SCOPE_VIOLATION khi truy cập trung tâm khác nhằm cô lập ranh giới tenant theo OWASP A01; ủy quyền AttendanceCsvReportService sinh luồng và trả phản hồi StreamingOutput với Content-Type text/csv; charset=UTF-8 cùng header Content-Disposition attachment kèm tên tệp chứa centerId và khoảng ngày; validate đầu vào qua Bean Validation trả 400 REPORT_VALIDATION_FAILED với mảng invalidFields liệt kê từng trường không hợp lệ; mọi tham số đi qua prepared statement tham số hóa, nghiêm cấm nối chuỗi đầu vào vào câu lệnh SQL; ghi audit log mỗi truy vấn xuất kèm userId, centerId, khoảng ngày và timestamp phục vụ truy vết [NFR-006].

* **Hợp đồng Định tuyến API và Sự kiện [REQ-024]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "GET /api/v1/reports/attendance/csv",
  "auth": "BEARER JWT | role=SYSTEM_ADMIN (all centers), CENTER_ADMIN (own managed_center_id)",
  "queryParameters": {
    "centerId": "uuid (required)",
    "fromDate": "yyyy-MM-dd (required, inclusive)",
    "toDate": "yyyy-MM-dd (required, inclusive)"
  },
  "response_200": {
    "contentType": "text/csv; charset=UTF-8",
    "headerRow": ["StudentName", "CourseName", "AttendanceDate", "Status"],
    "transferMode": "chunked streaming, JDBC fetch-size 1000"
  },
  "error_400": {
    "errorCode": "REPORT_VALIDATION_FAILED",
    "invalidFields": [
      { "field": "toDate", "rejectedValue": "2024-01-01", "message": "toDate must not precede fromDate" }
    ]
  },
  "error_403": { "errorCode": "TENANT_SCOPE_VIOLATION", "message": "Center Admin cannot export reports outside managed_center_id" }
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.3: Service sinh luồng CSV chuẩn RFC 4180 chống OOM

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/service/AttendanceCsvReportService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-024]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng AttendanceCsvReportService sinh dòng CSV từ truy vấn join attendance, users và courses lọc theo center_id thông qua khóa học thuộc trung tâm và khoảng [fromDate, toDate] bao biên; ghi dòng tiêu đề cố định StudentName,CourseName,AttendanceDate,Status rồi các dòng dữ liệu theo đúng thứ tự bốn cột [REQ-024]; escape dấu ngoặc kép bằng cách nhân đôi, bao trường bằng ngoặc kép khi chứa dấu phẩy, ngoặc kép hoặc ngắt dòng theo chuẩn RFC 4180; ánh xạ trạng thái Present khi tồn tại bản ghi Attendance khớp và Absent cho học viên đang ghi danh nhưng thiếu bản ghi trong buổi đã diễn ra; sử dụng streaming ResultSet với fetch size 1000 ghi trực tiếp vào OutputStream của phản hồi để tránh nạp toàn bộ tập kết quả vào heap khi xuất dữ liệu điểm danh lớn của một trung tâm; chuẩn hóa mọi phép so sánh ngày theo múi giờ UTC; tận dụng idx_attendance_course_date bảo đảm độ trễ đọc sub-second; không ghi PII thô vào log ứng dụng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.4: Service phát lại FIFO các scan tồn đọng hậu outage

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/service/OutageReplayService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[EXC-005], [REQ-024]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai OutageReplayService xử lý hàng đợi phát lại các bản ghi quét QR tồn đọng khi hệ thống khôi phục sau outage: đọc tuần tự theo timestamp gốc tăng dần bảo đảm thứ tự FIFO tuyệt đối [EXC-005]; từng bản ghi được ghi vào bảng attendance trong transaction riêng với cơ chế idempotent dựa hoàn toàn vào ràng buộc unique (student_id, course_id, attendance_date) — bản sao trùng bị bỏ qua an toàn mà không phát sinh lỗi phía client; trước khi bắt đầu phiên, chiếm khóa phân tán Redis qua SETNX key replay:lock với TTL 300 giây, thất bại chiếm khóa ném ReplayLockConflictException ánh xạ HTTP 409 REPORTING_REPLAY_LOCK_CONFLICT chặn hai phiên replay chạy song song; hàng đợi rỗng trả HTTP 204 REPORTING_REPLAY_QUEUE_EMPTY và giải phóng khóa ngay; sau khi phiên hoàn tất, đếm số sự kiện đã phát lại và số người dùng duy nhất bị ảnh hưởng rồi điều phối thông báo "sự kiện đã phục hồi" tới topic notification.dispatch để notification-service đẩy push tới từng người dùng; ghi audit log toàn bộ phiên replay kèm userId kích hoạt, số lượng phần tử, số bản ghi trùng bỏ qua và timestamp.

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-005]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "ReportingExceptionMapper",
  "package": "org.nlh4j.membership_hub.reporting.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.reporting.exception.ReplayLockConflictException",
      "httpStatus": 409,
      "errorCode": "REPORTING_REPLAY_LOCK_CONFLICT",
      "bodySchema": { "errorCode": "REPORTING_REPLAY_LOCK_CONFLICT", "message": "Another replay session currently holds the distributed lock" },
      "rule": "Redis SETNX lock replay:lock with TTL 300s; concurrent POST /api/v1/reports/outage/replay rejected without mutating queue state"
    },
    {
      "handles": "org.nlh4j.membership_hub.reporting.exception.ReplayQueueEmptyException",
      "httpStatus": 204,
      "errorCode": "REPORTING_REPLAY_QUEUE_EMPTY",
      "bodySchema": null,
      "rule": "Pending scan backlog exhausted; return 204 empty body, release distributed lock immediately, skip recovery notification dispatch"
    },
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 400,
      "errorCode": "REPORT_VALIDATION_FAILED",
      "bodySchema": {
        "errorCode": "REPORT_VALIDATION_FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "Aggregate Bean Validation violations (centerId required UUID, fromDate/toDate ISO-8601, toDate >= fromDate) preserving DTO declaration order; never expose internal SQL details"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

* **Hợp đồng Định tuyến API và Sự kiện [EXC-005]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "POST /api/v1/reports/outage/replay",
  "auth": "BEARER JWT | role=SYSTEM_ADMIN, CENTER_ADMIN",
  "processingOrder": "strict FIFO by original clientTimestamp ascending",
  "idempotencyRule": "UNIQUE (student_id, course_id, attendance_date) absorbs duplicates silently",
  "response_202": {
    "replayedEvents": 17,
    "notifiedUsers": 9,
    "status": "REPLAY_COMPLETED_FIFO"
  },
  "response_204": { "status": "REPORTING_REPLAY_QUEUE_EMPTY" },
  "response_409": { "errorCode": "REPORTING_REPLAY_LOCK_CONFLICT", "message": "Another replay session holds the distributed lock" },
  "sideEffect": "publish recovery notifications to topic notification.dispatch for each affected user"
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.5: Controller tóm tắt dashboard real-time định tuyến read replica

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/api/DashboardSummaryController.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-025]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Exposing GET /api/v1/reports/dashboard/summary nhận tham số centerId bắt buộc, yêu cầu bearer JWT với @RolesAllowed({"SYSTEM_ADMIN","CENTER_ADMIN"}) kèm kiểm tra phạm vi tenant tương tự endpoint CSV [REQ-025]; trả payload ba thẻ chỉ số: totalStudents (số học viên duy nhất đang ghi danh các khóa của trung tâm), activeCourses (các khóa có end_date lớn hơn hoặc bằng CURRENT_DATE) và upcomingSessions (danh sách buổi học trong 7 ngày tới kèm courseId, title, sessionDate); định tuyến toàn bộ truy vấn tổng hợp qua named datasource `replica` trỏ tới PostgreSQL read replica để cách ly hoàn toàn workload báo cáo khỏi cụm ghi OLTP; ủy quyền đọc qua DashboardCacheService để hưởng lợi ích cache Redis với fallback truy vấn trực tiếp; trả kèm generatedAt timestamp ISO-8601 phục vụ hiển thị độ tươi dữ liệu; áp dụng annotation OpenAPI @Operation/@ApiResponse; ghi audit log mỗi lần gọi kèm userId và timestamp.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-025]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "GET /api/v1/reports/dashboard/summary",
  "auth": "BEARER JWT | role=SYSTEM_ADMIN (all centers), CENTER_ADMIN (own managed_center_id)",
  "queryParameters": { "centerId": "uuid (required)" },
  "datasourceRouting": "all aggregation queries execute on named read-only datasource 'replica' (PostgreSQL read replica)",
  "response_200": {
    "totalStudents": 1250,
    "activeCourses": 42,
    "upcomingSessions": [
      { "courseId": "uuid", "title": "string", "sessionDate": "yyyy-MM-dd" }
    ],
    "generatedAt": "2026-08-23T05:05:12Z"
  },
  "error_403": { "errorCode": "TENANT_SCOPE_VIOLATION" }
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.6: Unit test service sinh CSV

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/service/AttendanceCsvReportService.java;./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/service/AttendanceCsvReportServiceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-024]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết JUnit 5 kiểm tra AttendanceCsvReportService: xác thực dòng tiêu đề và thứ tự bốn cột StudentName, CourseName, AttendanceDate, Status không đổi [REQ-024]; escape ký tự đặc biệt theo RFC 4180 với tên khóa học chứa dấu phẩy, ngoặc kép và ngắt dòng tiếng Việt; xử lý tập kết quả rỗng chỉ trả dòng tiêu đề; từ chối khoảng ngày đảo chiều với ngoại lệ validation tương ứng; xác minh ánh xạ trạng thái Present/Absent đúng nghiệp vụ với học viên ghi danh thiếu bản ghi điểm danh; đo độ bao phủ branch tối thiểu 85% trên service.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.7: Integration test phát lại FIFO hậu outage

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/OutageReplayIntegrationTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[EXC-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khởi chạy @QuarkusIntegrationTest với PostgreSQL Testcontainers và Redis Testcontainers; seed 50 bản ghi scan tồn đọng với timestamp xen kẽ không tuần tự; kích hoạt POST /api/v1/reports/outage/replay và khẳng định xử lý đúng thứ tự FIFO theo timestamp gốc tăng dần, không phát sinh dòng Attendance trùng nhờ ràng buộc unique, và thông báo phục hồi được queue thành công cho đúng số người dùng duy nhất [EXC-005]; kịch bản thứ hai gọi replay song song khi khóa còn hiệu lực xác nhận trả 409 REPORTING_REPLAY_LOCK_CONFLICT và trạng thái hàng đợi bất biến; kịch bản hàng đợi rỗng xác nhận trả 204 REPORTING_REPLAY_QUEUE_EMPTY và khóa được giải phóng ngay cho lần gọi kế tiếp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.8: Rà soát chất lượng lõi reporting-service

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/api/AttendanceReportController.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-024], [REQ-025]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Rà soát toàn diện lõi reporting-service: xác minh mọi truy vấn đi qua prepared statement tham số hóa chống SQL injection theo OWASP A03 [REQ-024]; kiểm tra enforcement phạm vi tenant trên cả hai endpoint CSV và dashboard, đảm bảo CENTER_ADMIN không đọc chéo trung tâm [REQ-025]; phân tích hồ sơ bộ nhớ streaming CSV qua profiling heap xác nhận fetch size 1000 giữ ổn định trên tập dữ liệu triệu dòng; rà soát race condition giữa các phiên replay trên khóa Redis (xác minh TTL đủ dài so với thời gian xử lý tối đa và kịch bản hết hạn giữa chừng được xử lý an toàn); đối chiếu mọi nhánh lỗi trả ProblemDetail RFC 7807 không leak stack trace hay chi tiết SQL; xác minh log scrubbing không ghi PII hay token; lập danh sách remediation ưu tiên kèm diff cụ thể và chốt điều kiện mở khóa NGÀY 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.9: Khởi tạo khung tài liệu tham chiếu API reporting-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-reporting-service.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-024], [REQ-025]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn khung tài liệu tham chiếu OpenAPI 3.0.3 cho reporting-service: mô tả ba endpoint GET /api/v1/reports/attendance/csv, GET /api/v1/reports/dashboard/summary và POST /api/v1/reports/outage/replay kèm schema request/response, bảng tham số truy vấn, ví dụ payload và lệnh curl thực tế [REQ-024], [REQ-025]; xây dựng bảng mã lỗi REPORT_VALIDATION_FAILED, TENANT_SCOPE_VIOLATION, REPORTING_REPLAY_LOCK_CONFLICT, REPORTING_REPLAY_QUEUE_EMPTY kèm điều kiện kích hoạt và hành vi hệ thống; bổ sung sơ đồ Mermaid tuần tự luồng replay hậu outage: kích hoạt → chiếm khóa Redis → FIFO xử lý → idempotent absorb → thông báo phục hồi; neo mọi mục vào thẻ truy vết tương ứng và chuẩn bị cấu trúc liên kết chéo cho runbook triển khai (NGÀY 2) và tài liệu OpenAPI hợp nhất (NGÀY 5).

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 2:
<!--DAY_HEADER_START-->Tối Ưu Lớp Đọc Bản Sao PostgreSQL, Caching Redis Dashboard Và Đóng Gói Container Reporting Service<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.1: Repository tổng hợp dashboard trên read replica

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/repository/DashboardAggregationRepository.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-025], [NFR-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai DashboardAggregationRepository gắn annotation @ReadOnlyDataSource định tuyến toàn bộ truy vấn qua named datasource `replica` trỏ tới PostgreSQL read replica nhằm cách ly workload báo cáo khỏi OLTP [NFR-004]; viết ba truy vấn tổng hợp tham số hóa: COUNT DISTINCT student_id từ enrollments join courses lọc theo center scope cho totalStudents, COUNT khóa học có end_date >= CURRENT_DATE cho activeCourses, và SELECT các buổi học trong cửa sổ 7 ngày tới cho upcomingSessions; tận dụng các index hiện hữu idx_enrollments_course_id, idx_courses_start_date và idx_attendance_course_date bảo đảm đọc sub-second ngay cả khi các dịch vụ Quarkus scale ngang qua HPA [REQ-025]; nghiêm cấm thao tác ghi trên datasource này; chuẩn hóa múi giờ UTC cho mọi phép so sánh ngày; trả về DTO bất biến phục vụ serialization.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.2: Service cache Redis dashboard với fallback read replica

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/cache/DashboardCacheService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-025], [ARC-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng DashboardCacheService dùng Quarkus Redis Client trên Redis 7.2.x với cache-key scope theo centerId dạng dashboard:summary:{centerId}, TTL 60 giây cân bằng độ tươi dữ liệu và giảm tải read replica [REQ-025], [ARC-010]; đăng ký listener vô hiệu hóa chủ động khi tiêu thụ sự kiện enrollment.created và attendance mới qua Kafka để cache không stale quá một chu kỳ TTL; serialize payload JSON bằng Jackson với cấu hình kiểu tường minh; triển khai fallback truy vấn trực tiếp read replica khi Redis unavailable hoặc timeout, bảo đảm dashboard không bao giờ mất khả năng phục vụ; đặt header Cache-Control private, max-age=60 và ETag weak validator hash của payload phục vụ client-side revalidation; không cache dữ liệu PII ngoài các chỉ số tổng hợp; ghi metric hit/miss ratio phục vụ giám sát hiệu quả cache.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-025]:**

<!--START_API_CONTRACT-->
```json
{
  "component": "DashboardCacheService",
  "cacheKeyPattern": "dashboard:summary:{centerId}",
  "ttlSeconds": 60,
  "invalidationTriggers": [
    { "topic": "enrollment.created", "action": "evict dashboard:summary:* of affected centerId" },
    { "topic": "attendance.events", "action": "evict dashboard:summary:* of affected centerId" }
  ],
  "responseHeaders": {
    "Cache-Control": "private, max-age=60",
    "ETag": "W/\"<sha256-of-payload>\""
  },
  "fallbackRule": "on Redis unavailable or timeout, query read replica directly and serve without caching; dashboard availability is never degraded by cache layer"
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.3: Unit test repository tổng hợp trên Testcontainers

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/repository/DashboardAggregationRepository.java;./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/repository/DashboardAggregationRepositoryTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-025]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết JUnit 5 với PostgreSQL Testcontainers: seed dataset mẫu nhiều trung tâm gồm học viên, khóa học đang diễn ra, khóa đã kết thúc và buổi học trong/t ngoài cửa sổ 7 ngày; xác thực số liệu totalStudents, activeCourses, upcomingSessions khớp kỳ vọng toán học cho từng centerId [REQ-025]; kiểm tra biên khóa học có end_date trùng đúng CURRENT_DATE vẫn tính là active; xác nhận phiên bản truy vấn thực thi trên datasource replica thay vì primary bằng cách intercept connection metadata; xác minh truy vấn từ chối tham số centerId null với ngoại lệ validation rõ ràng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.4: Kiểm thử hiệu năng dashboard p95 với Gatling

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/DashboardPerformanceIntegrationTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-001], [REQ-025]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** INTEGRATION_SCOPE dựng profile đo hiệu năng bằng Gatling mô phỏng 10.000 người dùng đồng thời gọi GET /api/v1/reports/dashboard/summary với phân bố centerId thực tế; thất bại pipeline nếu p95 latency vượt 200 ms theo ràng buộc [NFR-001]; ghi nhận throughput, tỷ lệ lỗi và utilization của connection pool làm baseline định cỡ HPA cho Giai đoạn hạ tầng [REQ-025]; chạy thêm kịch bản cold-cache (xóa Redis trước khi load) và warm-cache để đối chiếu tác động của TTL 60 giây; xuất báo cáo kết quả dạng HTML artifact đính kèm hồ sơ hiệu năng phục vụ kiểm toán GO/NO-GO ở NGÀY 5.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.5: Rà soát nhất quán replica–cache và hiệu quả truy vấn

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/repository/DashboardAggregationRepository.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-025], [NFR-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Rà soát DashboardAggregationRepository và DashboardCacheService: đánh giá rủi ro stale-read giữa primary và replica trong cửa sổ replication lag và xác nhận ngưỡng chấp nhận được cho dashboard tổng hợp [REQ-025]; kiểm tra rò rỉ kết nối pool khi fallback Redis xảy ra dồn dập, đề xuất circuit breaker ngăn domino; phát hiện sai lệch cache sau invalidate do race giữa listener Kafka và TTL expiry, đề xuất chiến lược evict-then-populate nguyên tử; phân tích kế hoạch truy vấn EXPLAIN cho cả ba truy vấn tổng hợp bảo đảm sử dụng index hiện hữu, thiết kế bản vá tối ưu nếu phát hiện full-table scan [NFR-004]; ghi nhận quyết định kiến trúc và chốt điều kiện mở khóa NGÀY 3.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.6: Dockerfile multi-stage reporting-service dưới ngân sách kích thước

##### Sub-Agent được phân công: Docker

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/docker/reporting-service.Dockerfile

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-005], [ARC-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết multi-stage Dockerfile cho reporting-service: stage build dùng maven:3.9-eclipse-temurin-21 với cache layer cho thư mục ~/.m2 qua BuildKit mount, stage runtime dùng eclipse-temurin-21-jre-alpine chỉ sao chép fast-jar output của Quarkus; ép kích thước base image nhỏ hơn 200 MB và image cuối nhỏ hơn 500 MB theo ràng buộc [NFR-005]; bật JVM container-aware flags (-XX:MaxRAMPercentage=75.0, -XX:+UseSerialGC cho profile nhỏ) và chạy dưới user non-root uid 1001; khai báo HEALTHCHECK gọi readiness probe nội bộ; loại bỏ build tool và source khỏi stage cuối để thu nhỏ bề mặt tấn công theo OWASP attack surface minimization trên nền stack [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.7: Runbook triển khai reporting-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/runbook-reporting-deployment.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-024], [REQ-025]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Soạn runbook triển khai reporting-service: trình tự build image qua reporting-service.Dockerfile, push lên Artifact Registry, apply manifests GKE, verify health check endpoint CSV và dashboard bằng bộ curl mẫu kèm kỳ vọng phản hồi, quy trình rollback nhanh về revision trước đó qua kubectl rollout undo; kèm checklist hậu triển khai xác minh [REQ-024] và [REQ-025] hoạt động end-to-end (xuất CSV mẫu một trung tâm, đối chiếu ba chỉ số dashboard với truy vấn SQL thủ công trên replica); bổ sung phần troubleshoot lỗi thường gặp: khóa replay conflict, cache stale, replica lag vượt ngưỡng và hướng dẫn escalation; neo mọi mục vào thẻ truy vết tương ứng và liên kết chéo với api-reporting-service.md từ NGÀY 1.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 3:
<!--DAY_HEADER_START-->Cung Cấp Hạ Tầng GCP Bằng Terraform Và Biên Soạn Manifests Điều Phối GKE Với HPA Tự Động Mở Rộng<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.1: Terraform VPC production multi-zone

##### Sub-Agent được phân công: GCP

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/terraform/vpc-main.tf

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-010], [NFR-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khởi tạo vpc-main.tf cấp VPC production cho membership-hub: subnet regional asia-southeast1 với dải CIDR riêng biệt cho node và pod, firewall rule chỉ mở cổng 443 (HTTPS ingress) và 6443 (Kubernetes API) từ dải IP được phép, Cloud NAT với egress IP tĩnh cho outbound traffic của node, bật Private Google Access cho node truy cập API Google qua đường nội bộ; thiết kế topology multi-zone làm nền cho failover tự động đạt uptime mục tiêu 99.9% [NFR-002] trên nền stack đã chốt [ARC-010]; khai báo outputs chuẩn hóa subnet-id và network-id cho các module Terraform kế tiếp; cấm gán IP public trực tiếp cho bất kỳ tài nguyên compute nào.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.2: Terraform IAM least privilege và Cloud Storage phân tầng

##### Sub-Agent được phân công: GCP

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/terraform/iam-storage.tf

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-010], [NFR-003], [NFR-006]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo iam-storage.tf: service account tối thiểu quyền (least privilege) cho từng nhóm workload GKE gắn Workload Identity thay vì tải key JSON, giảm bề mặt tấn công credential theo OWASP A01 [NFR-003]; bucket Cloud Storage phân tầng: bucket backup chứa snapshot cơ sở dữ liệu và bucket audit-log chứa dòng sự kiện kiểm toán, cả hai bật object versioning, uniform bucket-level access và public access prevention bắt buộc; gắn IAM Conditions theo thuộc tính resource giới hạn phạm vi truy cập; bucket audit-log được thiết kế làm kho chứa đích cho Log Sink phục vụ lưu trữ truy vết 1 năm [NFR-006]; mã hóa at-rest mặc định AES-256 do Google quản lý trên toàn bộ bucket [NFR-003]; khai báo outputs cho module backup-pitr.tf và audit-log-sink.tf ở NGÀY 4 trên nền stack [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.3: Terraform Cloud SQL PostgreSQL HA và read replica báo cáo

##### Sub-Agent được phân công: GCP

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/terraform/postgresql.tf

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-004], [REQ-025]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Provision postgresql.tf: Cloud SQL PostgreSQL 16 chế độ HA regional với automatic failover trong cùng region, instance read replica chuyên dụng tiếp nhận toàn bộ workload báo cáo và dashboard của reporting-service để cách ly khỏi OLTP [NFR-004]; bật flag pg_stat_statements phục vụ tuning truy vấn, cấu hình max_connections phối hợp connection pooler phía ứng dụng (Agroal) tránh cạn kiệt slot; thiết lập private IP peering với VPC đã tạo ở vpc-main.tf, nghiêm cấm public IP; khai báo database membership_hub và user ứng dụng với đặc quyền tối thiểu không sở hữu quyền DDL trên schema production; tham số hóa maintenance window ngoài giờ cao điểm; outputs connection-name và replica-connection-name cho cấu hình datasource của reporting-service [REQ-025].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.4: Manifest cụm GKE regional failover

##### Sub-Agent được phân công: GKE

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/gke/cluster.yaml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn cluster.yaml: GKE regional cluster trải 3 zone của region asia-southeast1 bảo đảm failover tự động khi một zone suy giảm, duy trì uptime mục tiêu 99.9% [NFR-002]; bật private nodes với dải CIDR riêng, Workload Identity bắt buộc cho mọi namespace, Network Policy enabled ở mức dataplane VPC-native; release channel REGULAR để nhận bản vá bảo mật định kỳ, maintenance window cấu hình ngoài giờ cao điểm Việt Nam; bật shielded nodes với secure boot và integrity monitoring; khai báo node pool tách biệt cho workload báo cáo với taint chuyên dụng tránh tranh chấp tài nguyên với dịch vụ OLTP.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.5: Manifests Deployment/Service cho 10 microservices

##### Sub-Agent được phân công: GKE

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/gke/deployments.yaml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Sinh deployments.yaml cho 10 microservices membership-hub (auth-service, center-service, course-service, enrollment-service, attendance-service, card-service, notification-service, promotion-service, chatbot-service, reporting-service): probes liveness/readiness/startup với ngưỡng phù hợp từng dịch vụ (reporting-service readiness gọi health endpoint nội bộ), resource requests/limits chuẩn hóa theo baseline đo hiệu năng NGÀY 2, topologySpreadConstraints chống tập trung pod trên một zone hoặc node, image pull từ Artifact Registry khu vực asia-southeast1 với imagePullPolicy IfNotPresent và tag digest bất biến trên nền stack [ARC-010]; khai báo Service ClusterIP cho giao tiếp nội bộ và biến môi trường kết nối Redis/Kafka/PostgreSQL inject từ Secret mã hóa KMS; reporting-service nhận thêm biến cấu hình named datasource replica trỏ connection-name của read replica.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.6: Manifests HPA tự động mở rộng theo CPU và latency

##### Sub-Agent được phân công: GKE

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/gke/hpa.yaml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Thiết kế hpa.yaml: HorizontalPodAutoscaler v2 áp dụng cho toàn bộ deployment dịch vụ với hai chỉ báo scale — resource CPU targetAverageUtilization 70% và custom metric http_request_duration_p95 vượt 300 ms lấy từ Prometheus Adapter [NFR-004]; minReplicas 2 bảo đảm HA tối thiểu, maxReplicas 20 chặn trần chi phí; behavior.scaleDown stabilizationWindow 300 giây chống flapping khi lưu lượng dao động, scaleUp policy tăng nhanh tối đa 4 pod/30 giây hấp thụ burst điểm danh giờ cao điểm; ghi chú ràng buộc tương thích: mọi deployment phải khai báo resource requests để HPA tính toán chính xác.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.7: Kiểm toán bảo mật IaC theo OWASP Top 10

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/terraform/iam-storage.tf

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-003], [ARC-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Kiểm toán bảo mật IaC theo OWASP Top 10: rà soát iam-storage.tf và vpc-main.tf về nguyên tắc least privilege IAM (không role chứa wildcard `*` trên action hoặc resource), xác minh public access prevention bật cứng trên mọi bucket, cấm hardcode credential hoặc secret trong biến plaintext (bắt buộc tham chiếu Secret Manager/KMS), xác minh firewall không mở cổng quản trị rộng rãi; bắt buộc tfsec/checkov pass với zero finding mức HIGH trước khi terraform apply được phép chạy trong pipeline [NFR-003]; đối chiếu cấu hình Workload Identity loại trừ rủi ro key leakage; thiết kế bản vá cho mọi phát hiện mức HIGH kèm diff cụ thể và chốt điều kiện mở khóa NGÀY 4 trên nền stack [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 4:
<!--DAY_HEADER_START-->Củng Cố Bảo Mật TLS AES, Backup PITR Đa Vùng, Audit Log, Pipeline CI CD Và Tuân Thủ GDPR CCPA<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.1: Ingress TLS 1.3 và mã hóa Secret bằng Cloud KMS

##### Sub-Agent được phân công: GKE

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/gke/ingress-tls.yaml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai ingress-tls.yaml: ManagedCertificate do Google quản lý cho domain production, ép minimum TLS version 1.3 tại load balancer bảo vệ toàn bộ dữ liệu truyền theo ràng buộc [NFR-003]; khai báo SSLPolicy với profile MODERN và min TLS 1.3, từ chối handshake phiên bản thấp hơn; mã hóa Kubernetes Secret chứa biến môi trường nhạy cảm (chuỗi kết nối database, credential Redis/Kafka) bằng Cloud KMS với khóa đối xứng AES-256 gắn EnforceConfigAsData; định nghĩa NetworkPolicy mặc định deny-all cho namespace membership-hub rồi whitelist từng luồng service-to-service cần thiết (reporting-service → replica Postgres, notification-service → FCM/Zalo egress), thu nhỏ bề mặt lateral movement.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.2: Terraform backup PITR đa vùng

##### Sub-Agent được phân công: GCP

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/terraform/backup-pitr.tf

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-009]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo backup-pitr.tf: lịch full backup PostgreSQL hằng ngày lúc 02:00 UTC qua backup schedule của Cloud SQL, bật point-in-time recovery với cửa sổ 24 giờ cho phép khôi phục về bất kỳ mốc thời gian nào trong ngày [NFR-009]; cấu hình cross-region replication sao chép backup sang region thứ hai làm bản sao DR cho cụm GKE đáp ứng yêu cầu backup cụm sang region riêng biệt; định nghĩa chính sách retention backup đầy đủ 30 ngày và WAL archive theo cửa sổ PITR; thiết lập cảnh báo qua Cloud Monitoring khi job backup thất bại hoặc replication lag vượt ngưỡng; tham chiếu bucket backup từ iam-storage.tf làm đích lưu trữ; outputs phục vụ runbook khôi phục thảm họa.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.3: Terraform audit log sink retention 1 năm

##### Sub-Agent được phân công: GCP

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/terraform/audit-log-sink.tf

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-006]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Thiết lập audit-log-sink.tf: Log Sink thu Admin Activity logs và Data Access logs của toàn bộ project chuyển vào bucket audit-log chuyên dụng với retention policy locked 365 ngày đáp ứng lưu trữ truy vết 1 năm [NFR-006]; exporter phụ sang BigQuery dataset partition theo ngày phục vụ truy vấn điều tra hành động người dùng (thay đổi vai trò, bản ghi điểm danh, gửi thông báo, thao tác GDPR) kèm timestamp, userId và chi tiết hành động; khóa xóa bucket qua retention lock ngăn tampering dòng kiểm toán; cấp quyền reader riêng biệt cho vai trò điều tra bảo mật theo nguyên tắc least privilege; outputs tên dataset và bucket cho tài liệu compliance ở NGÀY 5.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.4: Kịch bản build-push image lên Artifact Registry

##### Sub-Agent được phân công: Docker

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/docker/build-push.sh

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-005], [ARC-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết build-push.sh build song song 10 image microservices từ các Dockerfile multi-stage hiện hữu: gắn tag semantic theo phiên bản git commit kèm digest bất biến, chạy Trivy scan trên mỗi image và chặn pipeline ở mức CRITICAL vulnerability, xác minh ràng buộc kích thước base nhỏ hơn 200 MB và final nhỏ hơn 500 MB bằng docker image inspect trước khi cho phép push [NFR-005]; đẩy lên Artifact Registry khu vực asia-southeast1 với retry 3 lần khi lỗi mạng tạm thời; xuất manifest danh sách image-digest phục vụ traceability triển khai và rollback; script phải idempotent — chạy lại không tạo tag trùng lặp và thoát sạch với exit code chuẩn hóa cho pipeline CI/CD [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.5: Controller tuân thủ GDPR/CCPA export, deletion và consent

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/reporting-service/src/main/java/org/nlh4j/membership_hub/reporting/privacy/PrivacyComplianceController.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-008], [NFR-006]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai PrivacyComplianceController với danh tính chủ thể dữ liệu suy nghiêm ngặt từ claim sub của bearer JWT, tuyệt đối không tin tưởng trường userId trong body nhằm chặn leo thang export/xóa chéo tài khoản theo OWASP A01 [NFR-008]; GET /api/v1/privacy/export tổng hợp và xuất toàn bộ dữ liệu cá nhân của người dùng dạng JSON hợp lệ gồm hồ sơ, ghi danh, điểm danh, thẻ hội viên, thông báo và trạng thái consent; DELETE /api/v1/privacy/data thực thi right to erasure xóa vĩnh viễn trên mọi bảng liên quan trong một transaction phân tán logic theo thứ tự khóa ngoại và vô hiệu hóa refresh token phiên; PUT /api/v1/privacy/consent cập nhật trạng thái đồng ý truyền thông marketing theo kênh với hiệu lực tức thời; mọi thao tác đều ghi audit log kèm userId, hành động và timestamp phục vụ lưu trữ truy vết [NFR-006]; validate đầu vào trả 400 PRIVACY_VALIDATION_FAILED với mảng invalidFields; caller yêu cầu thao tác trên userId khác mà không mang vai trò SYSTEM_ADMIN bị chặn 403 PRIVACY_IDENTITY_MISMATCH.

* **Hợp đồng Định tuyến API và Sự kiện [NFR-008]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "method": "GET",
      "path": "/api/v1/privacy/export",
      "auth": "BEARER JWT (subject resolved from sub claim; SYSTEM_ADMIN may pass ?userId=)",
      "response_200": {
        "format": "application/json",
        "scope": ["profile", "enrollments", "attendance", "membershipCard", "notifications", "consents"]
      }
    },
    {
      "method": "DELETE",
      "path": "/api/v1/privacy/data",
      "auth": "BEARER JWT (subject resolved from sub claim)",
      "response_204": {},
      "sideEffect": "permanent erasure across related tables in FK-safe order + refresh token revocation + audit entry"
    },
    {
      "method": "PUT",
      "path": "/api/v1/privacy/consent",
      "auth": "BEARER JWT (subject resolved from sub claim)",
      "request": { "marketingConsent": true, "channel": "PUSH | EMAIL | ZALO" },
      "response_200": { "userId": "uuid", "marketingConsent": true, "effectiveAt": "2026-08-23T05:05:12Z" }
    }
  ],
  "error_400": { "errorCode": "PRIVACY_VALIDATION_FAILED", "invalidFields": [] },
  "error_403": { "errorCode": "PRIVACY_IDENTITY_MISMATCH", "message": "Caller identity does not match target data subject" }
}
```
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [NFR-008]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "PrivacyExceptionMapper",
  "package": "org.nlh4j.membership_hub.reporting.privacy",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.reporting.privacy.PrivacyValidationException",
      "httpStatus": 400,
      "errorCode": "PRIVACY_VALIDATION_FAILED",
      "bodySchema": {
        "errorCode": "PRIVACY_VALIDATION_FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "Aggregate Bean Validation violations (channel enum subset PUSH/EMAIL/ZALO, marketingConsent boolean required) into invalidFields; never expose internal storage errors"
    },
    {
      "handles": "org.nlh4j.membership_hub.reporting.privacy.PrivacyIdentityMismatchException",
      "httpStatus": 403,
      "errorCode": "PRIVACY_IDENTITY_MISMATCH",
      "bodySchema": { "errorCode": "PRIVACY_IDENTITY_MISMATCH", "message": "Caller identity does not match target data subject" },
      "rule": "Triggered when JWT sub claim differs from requested userId and caller lacks SYSTEM_ADMIN role; blocks cross-account export/erasure per OWASP A01 broken access control"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.6: Integration test vòng đời GDPR export/deletion/consent

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/reporting-service/src/test/java/org/nlh4j/membership_hub/reporting/PrivacyComplianceIntegrationTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** INTEGRATION_SCOPE khởi chạy @QuarkusIntegrationTest với PostgreSQL Testcontainers và Redis Testcontainers kiểm thử vòng đời GDPR/CCPA đầy đủ: export trả đủ trường dữ liệu cá nhân dạng JSON hợp lệ khớp schema khai báo cho học viên có dữ liệu đa bảng [NFR-008]; deletion xóa triệt để bản ghi trên mọi bảng liên quan (users, enrollments, attendance, student_cards, notifications, consents) xác nhận bằng truy vấn đếm sau xóa và thu hồi refresh token khiến phiên cũ không còn dùng được; consent cập nhật có hiệu lực tức thời trong phản hồi kế tiếp và được audit log ghi nhận đầy đủ kèm timestamp; kịch bản caller cố export userId khác xác nhận 403 PRIVACY_IDENTITY_MISMATCH; kịch bản payload consent sai kênh xác nhận 400 với mảng invalidFields.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.7: Pipeline CI/CD GitHub Actions với cổng chất lượng và hiệu năng

##### Sub-Agent được phân công: GCP

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/infra/cicd/github-actions-deploy.yaml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-010], [NFR-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Dựng github-actions-deploy.yaml với chuỗi job tuần tự: checkout và build backend `mvn -q verify` cùng frontend `next build`; chạy unit/integration suite với độ bao phủ ≥ 85% chặn merge khi vi phạm; phân tích tĩnh SonarQube với quality gate chặn mọi blocker/critical mới phát sinh; Trivy scan image chặn mức CRITICAL; build/push image qua build-push.sh lên Artifact Registry; terraform plan bắt buộc đính kèm output rồi terraform apply sau bước approval thủ công qua GitHub Environment protection; kubectl apply manifests GKE qua Workload Identity federation không dùng key JSON; kèm gate hiệu năng cuối cùng chặn promote production nếu kết quả Gatling cho thấy p95 latency vượt 200 ms theo [NFR-001] trên nền pipeline [ARC-010]; khai báo concurrency group ngăn deploy song song va chạm và retention artifact 30 ngày phục vụ điều tra.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 5:
<!--DAY_HEADER_START-->Hoàn Thiện Bộ Tài Liệu Doanh Nghiệp, Hướng Dẫn Bản Địa Hóa Và Kiểm Toán Sẵn Sàng Production<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.1: Hoàn thiện blueprint kiến trúc tổng thể

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/architecture-blueprint.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-010], [NFR-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Hoàn thiện architecture-blueprint.md thành bản đóng gói cuối cùng: sơ đồ topology 10 microservices với luồng dữ liệu OAuth2/JWT qua api-gateway, điểm danh QR idempotent qua ràng buộc unique ba cột, điều phối thông báo đa kênh FCM/APNs/Zalo qua Kafka topics, mô hình RBAC 5 vai trò với phạm vi tenant managed_center_id, kiến trúc CQRS đọc báo cáo qua read replica và cache Redis; bổ sung chương hạ tầng production phản chiếu Terraform/GKE đã provision: HPA theo CPU 70%/latency 300 ms, failover liên zone đạt uptime 99.9% [NFR-002], TLS 1.3/AES-256, backup PITR đa region và audit sink 1 năm; cập nhật trạng thái bàn giao toàn bộ 5 giai đoạn với ma trận tag traceability 100%; liệt kê quyết định kiến trúc trọng yếu (ADR) kèm lý do lựa chọn trên nền stack đã chốt [ARC-010].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.2: Tổng hợp tài liệu tham chiếu OpenAPI hợp nhất

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/openapi-reference.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tổng hợp openapi-reference.md hợp nhất hợp đồng OpenAPI 3.1 của toàn bộ 10 dịch vụ (auth, center, course, enrollment, attendance, card, notification, promotion, chatbot, reporting) kèm ví dụ request/response thực tế cho từng endpoint, sơ đồ mã lỗi chuẩn hóa thống nhất (AUTH_VALIDATION_FAILED, TAX_ID_CONFLICT, SCHEDULE_CONFLICT, ATT-DUP-001, PROMO_CODE_DUPLICATED, CHATBOT_RATE_LIMITED, REPORTING_REPLAY_LOCK_CONFLICT, PRIVACY_IDENTITY_MISMATCH...) và hướng dẫn xác thực bearer token qua api-gateway với vòng đời access 15 phút/refresh 7 ngày [ARC-010]; bổ sung bảng phân bổ endpoint theo vai trò RBAC và ma trận topic Kafka producer/consumer làm phụ lục tham chiếu chéo cho đội tích hợp bên thứ ba.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.3: Hướng dẫn vận hành bản địa hóa vi/en/es

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/localization-operations-guide.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-007]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn localization-operations-guide.md hoàn chỉnh: quy trình externalize UI strings ba bước (trích xuất khóa → cập nhật từ điển en/vi/es → review ngôn ngữ học) bảo đảm không còn chuỗi hardcode trong nguồn [NFR-007]; thủ tục bổ sung locale mới trong tương lai gồm cập nhật middleware localeDetection, bộ hreflang và cấu hình next-intl; checklist kiểm thử hreflang và meta SSR cho crawler (assertion view-source bộ ba link alternate cùng x-default, xác minh html lang khớp locale, kiểm tra Google Search Console international targeting); vận hành cơ chế fallback stored preference → Accept-Language với xử lý q-value → mặc định 'vi'; ghi chú giới hạn kỹ thuật của chuyển locale không reload trang và quy trình QA đa ngôn ngữ trước mỗi release.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.4: Quy trình audit log và quản lý consent GDPR/CCPA

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/compliance-audit-consent-guide.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-006], [NFR-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Soạn compliance-audit-consent-guide.md: quy trình ghi audit log thống nhất (timestamp, userId, chi tiết hành động) với lưu trữ 1 năm qua Log Sink retention locked 365 ngày và đường dẫn truy vấn điều tra trên BigQuery [NFR-006]; luồng xử lý yêu cầu xóa/xuất dữ liệu cá nhân GDPR/CCPA từ tiếp nhận → xác minh danh tính → thực thi qua PrivacyComplianceController → xác nhận hoàn tất với SLA nội bộ, kèm mẫu biểu xác minh danh tính và biểu mẫu từ chối hợp lệ [NFR-008]; ma trận quản lý consent marketing cho từng kênh truyền thông (PUSH, EMAIL, ZALO) với quy tắc hiệu lực tức thời và cơ chế thu hồi; hướng dẫn phản hồi sự cố rò rỉ dữ liệu kèm checklist thông báo theo nghĩa vụ pháp lý; neo mọi mục vào thẻ truy vết tương ứng và liên kết chéo với api-reporting-service.md.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.5: Kiểm toán sẵn sàng production GO/NO-GO

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/production-readiness-review.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Thực hiện kiểm toán sẵn sàng production cuối cùng đối chiếu từng ràng buộc với bằng chứng đo lường thực tế: p95 latency 200 ms và index sub-second cho 10.000 người dùng đồng thời đối chiếu báo cáo Gatling NGÀY 2 [NFR-001]; uptime 99.9% failover liên zone qua cấu hình cluster regional [NFR-002]; TLS 1.3/AES-256 và mitigations OWASP Top 10 đối chiếu kết quả tfsec/checkov và ingress policy [NFR-003]; HPA CPU 70%/latency 300 ms cùng read replica cách ly [NFR-004]; kích thước image 200 MB base/500 MB final đối chiếu manifest build-push [NFR-005]; audit log retention 1 năm đối chiếu cấu hình sink [NFR-006]; đa ngôn ngữ en/vi/es đối chiếu checklist bản địa hóa [NFR-007]; GDPR/CCPA export/deletion/consent đối chiếu integration test NGÀY 4 [NFR-008]; backup PITR 24h đa region đối chiếu cấu hình backup-pitr.tf [NFR-009]; phát hành verdict GO/NO-GO kèm danh sách hành động khắc phục ưu tiên nếu NO-GO và chữ ký phê duyệt của hội đồng quản trị kỹ thuật.

<!--END_ATOMIC_SUB_TASK_NODE-->