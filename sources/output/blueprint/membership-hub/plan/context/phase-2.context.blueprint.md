# Giai đoạn 2: <!--PHASE_NAME_START-->Dịch Vụ Trung Tâm, Khóa Học Và Thực Thi RBAC Qua API Gateway<!--PHASE_NAME_END-->

## 📊 Kiểm soát Tài liệu

| Hạng mục | Chi tiết |
| :--- | :--- |
| **ID Bản thiết kế** | ARCH-20260823050512 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Dịch Vụ Trung Tâm, Khóa Học Và Thực Thi RBAC Qua API Gateway<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 2 kiến tạo toàn bộ tầng nghiệp vụ quản trị đa trung tâm của nền tảng membership-hub trên nền Quarkus. center-service cung cấp API danh sách trung tâm phân trang với index truy vấn sub-second [REQ-004], CRUD trung tâm validate taxId numeric 10–13 chữ số và trả 409 Conflict khi trùng [REQ-005], cùng cơ chế gán/hủy Center Admin ghi phạm vi quản lý managed_center_id và cô lập tenant theo trung tâm [REQ-006], [ARC-002]. course-service vận hành lưới khóa học CourseID, Title, StartDate, EndDate, TeacherName [REQ-007], CRUD khóa học chặn xung đột lịch trên cùng teacherId với maxStudents mặc định 30 [REQ-008], và phân công giáo viên phát sự kiện teacher.assigned.v1 sang notification-service [REQ-009], [ARC-008]. Toàn bộ endpoint được bảo vệ bởi bộ filter/interceptor RBAC 5 vai trò (System Admin, Center Admin, Manager, Teacher, Student) thống nhất qua api-gateway [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], đồng thời công bố hợp đồng OpenAPI chuẩn hóa bốn luồng tích hợp liên dịch vụ: xác thực OAuth2/JWT, điểm danh QR idempotent, điều phối thông báo đa kênh và tích hợp mobile bearer token [ARC-006], [ARC-007], [ARC-008], [ARC-009]. Tester bàn giao JUnit phân quyền RBAC, integration test xung đột lịch và E2E đa vai trò; Doc bàn giao tài liệu tham chiếu API center/course và sơ đồ topology RBAC.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/23 05:05:12 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 1. Phạm vi Vận hành Giai đoạn & Mục tiêu

Giai đoạn 2 kiến tạo toàn bộ tầng nghiệp vụ quản trị đa trung tâm của nền tảng membership-hub, bao phủ trọn vẹn Task 6, Task 7, Task 8, Task 9, Task 10, Task 11, Task 29 và Task 30 của Master Backlog trên ba trụ cột kiến trúc song song.

Thứ nhất, center-service vận hành danh mục trung tâm: endpoint GET /api/v1/centers trả bảng trung tâm (Name, Address, TaxID, AdminContact) phân trang cho mọi vai trò đã xác thực với index idx_centers_name bảo đảm độ trễ đọc sub-second [REQ-004]; CRUD trung tâm dành cho System Admin validate taxId numeric 10–13 chữ số với ràng buộc unique, trả 409 TAX_ID_CONFLICT khi trùng và persist contactPhone/contactEmail đúng định dạng chuẩn [REQ-005]; cơ chế gán/hủy Center Admin set role và ghi center ID vào cột managed_center_id phục vụ cô lập tenant, mọi thay đổi ghi audit log kèm timestamp và userId [REQ-006], [ARC-002].

Thứ hai, course-service vận hành danh mục khóa học: lưới GET /api/v1/courses trả CourseID, Title, StartDate, EndDate, TeacherName (join Users) [REQ-007]; CRUD khóa học kiểm tra giao thoa khoảng startDate–endDate trên cùng teacherId trước khi persist, trả 422 SCHEDULE_CONFLICT kèm conflictingCourseId, maxStudents mặc định 30 [REQ-008]; phân công giáo viên phát sự kiện teacher.assigned.v1 lên topic course.teacher.events để notification-service queue push notification tới mobile app của giáo viên [REQ-009], [ARC-008].

Thứ ba, api-gateway thực thi bảo mật và hợp đồng tích hợp: bộ filter/interceptor RoleAuthorizationFilter đối chiếu claim vai trò trong JWT với ma trận quyền 5 vai trò — System Admin toàn quyền toàn cầu [ARC-001], Center Admin bị cô lập trong phạm vi managed_center_id [ARC-002], Manager không được sửa khóa học hoặc chỉ định giáo viên [ARC-003], Teacher chỉ đọc lịch dạy [ARC-004], Student giới hạn nghiệp vụ tự phục vụ [ARC-005] — chặn 403 ngay tại cổng gateway trước khi route tới service nghiệp vụ; đồng thời công bố hợp đồng OpenAPI chuẩn hóa bốn luồng tích hợp liên dịch vụ: xác thực OAuth2/JWT với access token 15 phút và refresh token 7 ngày [ARC-006], điểm danh QR idempotent [ARC-007], điều phối thông báo đa kênh FCM/APNs/Zalo [ARC-008], và tích hợp mobile bearer token với caching ngoại tuyến [ARC-009]. Chất lượng được bảo chứng bởi JUnit phân quyền RBAC, integration test xung đột lịch trên Testcontainers PostgreSQL và profile E2E đa vai trò; tài liệu được đóng gói qua tham chiếu API center/course, blueprint topology RBAC và tài liệu hợp đồng tích hợp OpenAPI.

## 2. Phạm vi Kỹ thuật Được phép & Ranh giới Thư mục (Tệp, đường dẫn và Endpoint)

* **Ma trận thư mục Backend được phép:**
    * ./sources/backend/center-service/pom.xml [ARC-000]
    * ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/*.java
    * ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/dto/*.java
    * ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/exception/*.java
    * ./sources/backend/center-service/src/main/resources/db/migration/V2__center_performance_indexes.sql [REQ-004]
    * ./sources/backend/center-service/src/main/resources/db/migration/V3__center_admin_scope.sql [REQ-006], [ARC-002]
    * ./sources/backend/center-service/src/test/java/org/nlh4j/membership_hub/center/*.java
    * ./sources/backend/course-service/pom.xml [ARC-000]
    * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/*.java
    * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/dto/*.java
    * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/event/*.java
    * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/exception/*.java
    * ./sources/backend/course-service/src/main/resources/db/migration/V2__course_schedule_indexes.sql [REQ-007], [REQ-008]
    * ./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/*.java
    * ./sources/backend/api-gateway/pom.xml [ARC-000]
    * ./sources/backend/api-gateway/src/main/java/org/nlh4j/membership_hub/gateway/rbac/*.java
    * ./sources/backend/api-gateway/src/main/resources/openapi/*.yaml
    * ./sources/backend/api-gateway/src/test/java/org/nlh4j/membership_hub/gateway/rbac/*.java
* **Ma trận thư mục Tài liệu được phép:**
    * ./sources/docs/api-center-service-reference.md [REQ-004], [REQ-005], [REQ-006]
    * ./sources/docs/api-course-service-reference.md [REQ-007], [REQ-008], [REQ-009]
    * ./sources/docs/rbac-topology-blueprint.md [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    * ./sources/docs/integration-contracts-openapi.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]
    * ./sources/docs/center-service-review-day1.md [REQ-004], [REQ-005]
    * ./sources/docs/course-service-review-conflict-detection.md [REQ-008]
    * ./sources/docs/phase2-final-review-report.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]
* **Mẫu định tuyến Endpoint được phép trong giai đoạn:**
    * GET /api/v1/centers — BEARER JWT, mọi vai trò đã xác thực [REQ-004]
    * POST /api/v1/centers — BEARER JWT, role=SYSTEM_ADMIN [REQ-005]
    * PUT /api/v1/centers/{centerId} — BEARER JWT, role=SYSTEM_ADMIN [REQ-005]
    * DELETE /api/v1/centers/{centerId} — BEARER JWT, role=SYSTEM_ADMIN [REQ-005]
    * POST /api/v1/centers/{centerId}/admins — BEARER JWT, role=SYSTEM_ADMIN [REQ-006]
    * DELETE /api/v1/centers/{centerId}/admins/{userId} — BEARER JWT, role=SYSTEM_ADMIN [REQ-006]
    * GET /api/v1/courses — BEARER JWT, mọi vai trò đã xác thực [REQ-007]
    * POST /api/v1/courses — BEARER JWT, role ∈ {SYSTEM_ADMIN, CENTER_ADMIN} [REQ-008]
    * PUT /api/v1/courses/{courseId} — BEARER JWT, role ∈ {SYSTEM_ADMIN, CENTER_ADMIN} [REQ-008]
    * DELETE /api/v1/courses/{courseId} — BEARER JWT, role ∈ {SYSTEM_ADMIN, CENTER_ADMIN} [REQ-008]
    * POST /api/v1/courses/{courseId}/teacher — BEARER JWT, role=SYSTEM_ADMIN, side-effect phát sự kiện teacher.assigned.v1 [REQ-009], [ARC-008]
    * DELETE /api/v1/courses/{courseId}/teacher — BEARER JWT, role=SYSTEM_ADMIN [REQ-009]
* **Ranh giới cấm xâm phạm:** mọi module và endpoint thuộc enrollment-service, attendance-service, card-service, notification-service, promotion-service, chatbot-service, reporting-service cùng toàn bộ cây ./sources/infra/ và ./sources/frontend/ được dành riêng cho các giai đoạn 3 đến 5; Giai đoạn 2 nghiêm cấm phát sinh tệp ngoài ma trận trên và cấm tái tạo bất kỳ tệp nào đã tồn tại từ Giai đoạn 1 (descriptor cha, auth-service, db-migrations, workspace frontend).

* **INVARIANT KHUNG NỀN TẢNG BẮT BUỘC (PLATFORM SKELETON MANIFEST INVARIANTS)**:
    * Descriptor hạ tầng repository gốc `./sources/backend/pom.xml` và workspace frontend `./sources/frontend/package.json` cùng `./sources/frontend/tsconfig.json` đã được neo vĩnh viễn tại Giai đoạn 1 - NGÀY 1 theo token kiến trúc [ARC-000]; Giai đoạn 2 nghiêm cấm tái tạo hoặc ghi đè các descriptor nền móng này.
    * Với ba module dịch vụ mới gia nhập chuỗi microservices ở giai đoạn này (center-service, course-service, api-gateway), bắt buộc đăng ký descriptor module con độc lập `./sources/backend/<service-name>/pom.xml` kế thừa parent membership-hub-backend TRƯỚC khi phát hành bất kỳ thành phần mã nguồn ứng dụng nào của module đó; toàn bộ descriptor scaffolding sinh ra phải ánh xạ nghiêm ngặt vào token theo dõi kiến trúc [ARC-000].

## 3. Chỉ đạo Chức năng Sub-Agent Chuyên trách

Theo ma trận phân công của Giai đoạn 2, các Sub-Agent được kích hoạt gồm Coder, Tester, Reviewer và Doc; Docker, GCP và GKE được dự phòng và chỉ kích hoạt từ Giai đoạn 5.

* **Coder**: Đóng vai trò Lập trình viên Ứng dụng Cấp cao/Principal. Chịu trách nhiệm hiện thực mã nguồn ứng dụng thuần túy: descriptor Maven module con cho center-service, course-service và api-gateway; thực thể/repository/service/resource của hai dịch vụ nghiệp vụ; bộ lọc RBAC và hợp đồng sự kiện Kafka; công bố spec OpenAPI YAML. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng DevOps.
* **Tester**: Đóng vai trò Trưởng QC/QA Principal. Chuyên về kỹ nghệ bộ kiểm thử, xác nhận và cổng chất lượng. Chịu trách nhiệm sinh JUnit unit test, integration test trên Testcontainers PostgreSQL, E2E automation đa vai trò qua api-gateway và kịch bản đo hiệu năng phân trang. Bị cấm sửa mã production. Khi phạm vi kiểm thử mang tính tích hợp tổng thể hoặc E2E không cô lập được một tệp production đơn lẻ, bắt buộc dùng định dạng cặp semicolon với token `INTEGRATION_SCOPE` đứng đầu (ví dụ: `INTEGRATION_SCOPE;./sources/backend/api-gateway/src/test/java/org/nlh4j/membership_hub/gateway/rbac/RbacMatrixIT.java`).
* **Doc**: Đóng vai trò Nhà văn Kỹ thuật Principal và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên biên soạn tài liệu đặc tả kỹ thuật, tham chiếu API, blueprint topology RBAC và catalog hợp đồng tích hợp phù hợp topology dự án. Mọi tệp tài liệu phải là đường dẫn tệp tường minh đuôi `.md` nằm trong kho lưu trữ tập trung `./sources/docs/`. Theo luật định giai đoạn, Doc phải được phân công tối thiểu một nhiệm vụ nền móng ngay NGÀY 1 để khởi tạo khung tài liệu markdown tham chiếu API center-service tương thích stack Java/Quarkus/PostgreSQL của ngữ cảnh này.
* **Reviewer**: Chịu trách nhiệm xác minh biên dịch, cổng phân tích tĩnh và vá phòng thủ. Chuyên kiểm toán chất lượng mã, xử lý lỗi compile, khắc phục lỗ hổng bảo mật OWASP Top 10 (đặc biệt kiểm soát truy cập hỏng A01 và injection A03), gỡ blocker SonarQube trước khi merge; ký duyệt điều kiện mở khóa giữa các ngày làm việc.
* **Docker**: Chuyên container hóa, kỹ nghệ Dockerfile multi-stage, tối ưu dung lượng image và đẩy image đã kiểm chứng lên registry. Trong Giai đoạn 2 chưa được phân công nhiệm vụ cụ thể.
* **GCP**: Chuyên tự động hóa trên Google Cloud Platform: build/push image lên Artifact Registry và điều phối môi trường container trên Cloud Run. Trong Giai đoạn 2 chưa được phân công nhiệm vụ cụ thể.
* **GKE**: Chuyên điều phối container production trong Google Kubernetes Engine: manifest deployment, routing control, cấu hình HPA, Helm chart và triển khai workload microservices. Trong Giai đoạn 2 chưa được phân công nhiệm vụ cụ thể.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)

* 100% thẻ truy vết của giai đoạn ([REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009]) được ánh xạ tường minh vào nhật ký ngày qua container `<!--START_TAGS-->` không gaps, không trùng lặp sai ngữ cảnh.
* `mvn -q verify` sạch trên ba descriptor module con mới (center-service, course-service, api-gateway); cây Maven không xung đột phiên bản với parent membership-hub-backend và Quarkus BOM 3.15.x.
* GET /api/v1/centers trả payload phân trang chuẩn (content, page, size, totalElements, totalPages) với kế hoạch truy vấn sử dụng idx_centers_name, độ trễ đọc sub-second ở 10.000 dòng dữ liệu mẫu [REQ-004].
* CRUD trung tâm: tạo/cập nhật với taxId trùng trả 409 TAX_ID_CONFLICT và rollback nguyên vẹn không để lại bản ghi mồ côi; taxId sai định dạng 10–13 chữ số hoặc contactEmail sai mẫu trả 422 kèm danh sách từng trường không hợp lệ [REQ-005].
* Gán Center Admin set role và ghi managed_center_id; hủy gán đảo ngược hoàn toàn; Center Admin truy cập trung tâm khác phạm vi bị chặn 403; mọi thao tác gán/hủy phát sinh đúng một dòng audit log kèm timestamp và userId [REQ-006], [ARC-002].
* GET /api/v1/courses trả lưới đủ 5 cột CourseID, Title, StartDate, EndDate, TeacherName; teacherName trả null an toàn khi teacherId chưa phân công [REQ-007].
* CRUD khóa học: khoảng ngày giao thoa trên cùng teacherId trả 422 SCHEDULE_CONFLICT kèm conflictingCourseId; cập nhật không tự xung đột với chính nó; hai giáo viên khác nhau cùng khung giờ được chấp nhận; maxStudents mặc định 30 khi thiếu trường đầu vào [REQ-008].
* Phân công giáo viên phát sự kiện teacher.assigned.v1 lên topic course.teacher.events với payload đầy đủ (eventId, courseId, teacherId, assignedBy, occurredAt), consumer deduplicate theo eventId; unassign gỡ ánh xạ và dừng luồng thông báo [REQ-009], [ARC-008].
* RoleAuthorizationFilter chặn 403 RBAC_ACCESS_DENIED cho mọi vi phạm ma trận 5 vai trò và 403 TENANT_SCOPE_VIOLATION cho Center Admin vượt phạm vi managed_center_id, thực thi ngay tại gateway trước khi route downstream [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005].
* Hai spec OpenAPI 3.0.3 được công bố tại api-gateway: auth-integration-contract.yaml bao phủ register/login/oauth2/refresh với securityScheme bearer JWT [ARC-006]; integration-contracts.yaml bao phủ attendance scan idempotent [ARC-007], notification dispatch đa kênh retry 3 lần [ARC-008] và mobile session bearer với ETag/Cache-Control [ARC-009].
* Độ bao phủ kiểm thử tự động ≥ 85% trên cả ba module; latency trung bình GET /api/v1/centers và GET /api/v1/courses ≤ 200 ms trong profile đo hiệu năng đối chiếu ràng buộc [NFR-001].
* Tuân thủ OWASP Top 10: toàn bộ truy vấn đi qua prepared statement với tham số hóa; sắp xếp/lọc động đi qua whitelist cứng tên cột; không leak stack trace hay chi tiết SQL ra phản hồi lỗi; thông điệp lỗi chuẩn hóa không dò được dữ liệu chéo tenant.
* Bảy tài liệu ./sources/docs/ hoàn chỉnh, liên kết chéo nhất quán với schema Giai đoạn 1 và hợp đồng API thực tế.
* Zero blocker SonarQube; mọi merge thực hiện qua pull request squash trên nhánh `features/development-phase-2-day-Y` theo quy trình phân nhánh hàng ngày.

## 5. Nhật ký Thực thi Kiến trúc Theo Ngày

<!--START_DAY_LOG_INDEX-->

### 🌤️ NGÀY 1:
<!--DAY_HEADER_START-->Khởi Tạo Center Service Với Thực Thể Trung Tâm, Danh Sách Phân Trang Và CRUD Ràng Buộc TaxId<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.1: Sinh descriptor module con center-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/center-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module center-service kế thừa parent membership-hub-backend mà không tái khai báo phiên bản dependency; đăng ký module này vào danh sách `<modules>` của descriptor cha theo thứ tự phụ thuộc sau db-migrations; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator và quarkus-flyway phục vụ bootstrap schema riêng của dịch vụ; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=center-service phục vụ đóng gói image ở Giai đoạn 5; bổ sung dependency test scope junit-jupiter, rest-assured và testcontainers-postgresql làm nền cho suite kiểm thử của Tester; cấu hình quarkus.flyway.locations trỏ tới classpath:db/migration của chính module để chuỗi migration V2/V3 của center-service chạy trong ngữ cảnh lịch sử Flyway riêng biệt, tránh xung đột phiên bản với chuỗi V1–V9 toàn cục của db-migrations.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.2: Thực thể JPA Center và DTO phản hồi chuẩn hóa

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/Center.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai thực thể Panache Center ánh xạ chính xác bảng centers đã migrate ở Giai đoạn 1: centerId UUID PK, name VARCHAR(100) NOT NULL, address VARCHAR(255) NOT NULL, taxId VARCHAR(13) NOT NULL UNIQUE, contactPhone VARCHAR(30) nullable, contactEmail VARCHAR(255) nullable; đặt tên cột snake_case khớp schema vật lý qua @Column; bổ sung record DTO CenterResponse trong gói dto với các trường centerId, name, address, taxId, contactPhone, contactEmail phục vụ serialization JSON thống nhất và chuẩn hóa hợp đồng trả về; bổ sung record DTO CenterRequest với ràng buộc Bean Validation @NotBlank @Size(max=100) cho name, @NotBlank @Size(max=255) cho address, @NotBlank @Pattern(regexp="^[0-9]{10,13}$") cho taxId, @Email cho contactEmail — đặt toàn bộ annotation validation ở tầng DTO theo nguyên tắc một nguồn chân lý duy nhất, cấm đặt ở tầng controller; serializer che một phần contactEmail/contactPhone cho vai trò không đủ thẩm định theo ma trận RBAC [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] chống rò rỉ PII.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.3: Repository truy vấn phân trang kèm migration index hiệu năng

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/CenterRepository.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai CenterRepository dựa trên PanacheRepository với truy vấn phân trang sắp xếp theo name tăng dần, tận dụng index idx_centers_name bảo đảm độ trễ đọc sub-second; cung cấp phương thức findByTaxId dùng prepared statement tham số hóa chống SQL injection phục vụ kiểm tra trùng lặp trước khi persist; cung cấp phương thức đếm tổng số dòng phục vụ totalPages; chạy migration V2__center_performance_indexes.sql tạo index hiệu năng cho danh sách trung tâm; nghiêm cấm nối chuỗi đầu vào người dùng vào câu lệnh SQL/JPQL native, mọi tham số đi qua positional parameter `?1` hoặc named parameter `:param`.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [REQ-004]:**

<!--START_DDL_MIGRATION-->
```sql
-- V2__center_performance_indexes.sql (center-service)
-- Performance index supporting paginated center listing ordered by name [REQ-004]
CREATE INDEX IF NOT EXISTS idx_centers_name ON centers (name);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.4: Endpoint REST danh sách trung tâm GET /api/v1/centers

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/CenterResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng CenterResource exposing GET /api/v1/centers với tham số truy vấn page (mặc định 0) và size (mặc định 20, chặn trần 100 chống abuse); yêu cầu bearer JWT hợp lệ cho mọi vai trò đã xác thực, ủy quyền chi tiết do RoleAuthorizationFilter tại api-gateway thực thi; trả payload phân trang chuẩn gồm content (danh sách CenterResponse), page, size, totalElements, totalPages; áp dụng annotation OpenAPI @Operation/@ApiResponse phục vụ công bố hợp đồng ở Ngày 5; ghi log truy cập kèm userId và timestamp phục vụ audit theo chuẩn [NFR-006] mà không ghi bearer token.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-004]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.5: Service CRUD trung tâm với validate taxId duy nhất

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/CenterService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai CenterService @Transactional với các thao tác create/update/delete: validate taxId theo mẫu numeric 10–13 chữ số ở tầng DTO, kiểm tra trùng lặp qua findByTaxId trước khi persist và ném TaxIdConflictException ánh xạ HTTP 409 khi trùng; validate định dạng contactEmail theo pattern RFC 5322 và contactPhone cho phép +, chữ số, khoảng trắng, gạch nối, ngoặc đơn; giới hạn quyền ghi cho SYSTEM_ADMIN qua kiểm tra claim vai trò trong JWT, các vai trò khác ném RbacAssignmentDeniedException ánh xạ 403; thao tác update loại trừ chính dòng đang sửa khỏi kiểm tra trùng taxId; thao tác delete xác minh centerId tồn tại trước khi xóa, trả 404 CENTER_NOT_FOUND khi thiếu; toàn bộ persist chạy trong cùng một transaction bảo đảm rollback nguyên vẹn không để lại bản ghi mồ côi khi xung đột; bổ sung ràng buộc unique uq_centers_tax_id ở tầng DB làm lớp phòng vệ thứ hai chống race condition check-then-insert.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-005]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-005]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "CenterExceptionMapper",
  "package": "org.nlh4j.membership_hub.center.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.center.exception.TaxIdConflictException",
      "httpStatus": 409,
      "errorCode": "TAX_ID_CONFLICT",
      "bodySchema": {
        "errorCode": "TAX_ID_CONFLICT",
        "message": "A center with this taxId already exists",
        "conflictingTaxId": "string"
      },
      "rule": "Block persist inside the same transaction; rollback cleanly without orphan records; message names the conflicting taxId value so the admin can correct the form"
    },
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 422,
      "errorCode": "CENTER_VALIDATION_FAILED",
      "bodySchema": {
        "errorCode": "CENTER_VALIDATION_FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "Aggregate every Bean Validation violation into invalidFields preserving DTO declaration order; never expose stack traces or SQL fragments"
    },
    {
      "handles": "org.nlh4j.membership_hub.center.exception.CenterNotFoundException",
      "httpStatus": 404,
      "errorCode": "CENTER_NOT_FOUND",
      "bodySchema": {
        "errorCode": "CENTER_NOT_FOUND",
        "message": "Center does not exist"
      },
      "rule": "Validate centerId existence before update or delete; no partial mutations"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.6: JUnit suite nghiệp vụ trung tâm

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/CenterService.java;./sources/backend/center-service/src/test/java/org/nlh4j/membership_hub/center/CenterServiceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest bao phủ: phân trang danh sách trung tâm với page/size mặc định và tham số tùy chỉnh, xác minh cấu trúc payload content/totalElements/totalPages; tạo trung tâm thành công trả 201 với centerId UUID; từ chối taxId trùng với kỳ vọng 409 TAX_ID_CONFLICT kèm conflictingTaxId; từ chối taxId 9 chữ số và 14 chữ số với 422 liệt kê đúng trường taxId; từ chối contactEmail sai định dạng; cập nhật trung tâm không tự xung đột với chính nó khi giữ nguyên taxId; xóa trung tâm tồn tại trả 204 và xóa centerId không tồn tại trả 404 CENTER_NOT_FOUND; caller không phải SYSTEM_ADMIN gọi endpoint ghi bị chặn 403; sử dụng Testcontainers PostgreSQL bảo đảm độ bao phủ nhánh validation đầy đủ và đo latency trung bình GET /api/v1/centers giữ dưới 200 ms đối chiếu [NFR-001].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.7: Rà soát chất lượng tầng center-service

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/center-service-review-day1.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Kiểm tra chất lượng code center-service: rò rỉ race condition khi check-then-insert taxId (xác nhận ràng buộc unique uq_centers_tax_id ở tầng DB đã làm lớp phòng vệ thứ hai và mapper bắt ConstraintViolationException ánh xạ đúng 409), hiệu quả kế hoạch truy vấn phân trang qua EXPLAIN xác nhận sử dụng idx_centers_name, tuân thủ chuẩn đặt tên Quarkus và quy ước gói org.nlh4j.membership_hub.center.*, chuẩn hóa thông báo lỗi không leak chi tiết SQL; kiểm soát truy cập hỏng OWASP A01: xác minh mọi endpoint ghi yêu cầu claim SYSTEM_ADMIN và không có đường bypass; ghi nhận phát hiện, phương án sửa kèm chủ sở hữu fix vào báo cáo review và chốt điều kiện mở khóa Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.8: Tài liệu tham chiếu API center-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-center-service-reference.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn tài liệu tham chiếu API center-service: bảng endpoint GET/POST/PUT/DELETE /api/v1/centers kèm schema request/response đầy đủ, tham số phân trang page/size, mã lỗi 409 TAX_ID_CONFLICT, 422 CENTER_VALIDATION_FAILED và 404 CENTER_NOT_FOUND; ví dụ payload mẫu và lệnh curl cho từng endpoint; ma trận quyền truy cập từng endpoint phân biệt System Admin (đọc/ghi/xóa) và các vai trò còn lại (chỉ đọc); ghi chú chính sách validate taxId numeric 10–13 chữ số và định dạng contactPhone/contactEmail; neo mọi mục vào thẻ truy vết [REQ-004], [REQ-005] và chuẩn bị cấu trúc liên kết chéo cho chương phân quyền Center Admin sẽ bổ sung ở Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 2:
<!--DAY_HEADER_START-->Phân Quyền Quản Trị Trung Tâm Theo Tenant Và Khởi Tạo Lưới Khóa Học<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.1: Sinh descriptor module con course-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module course-service kế thừa parent membership-hub-backend; đăng ký vào danh sách `<modules>` của descriptor cha sau center-service; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator, quarkus-flyway và quarkus-smallrye-reactive-messaging-kafka phục vụ phát sự kiện teacher.assigned.v1 ở Ngày 4; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=course-service; cấu hình quarkus.flyway.locations trỏ tới classpath:db/migration của chính module cho chuỗi migration V2__course_schedule_indexes.sql chạy trong ngữ cảnh lịch sử Flyway riêng biệt; bổ sung dependency test scope junit-jupiter, rest-assured, testcontainers-postgresql và testcontainers-kafka làm nền cho suite kiểm thử xung đột lịch và sự kiện.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.2: Migration phạm vi tenant và resource gán/hủy Center Admin

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/CenterAdminAssignmentResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-006], [ARC-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai CenterAdminAssignmentResource với hai endpoint: POST /api/v1/centers/{centerId}/admins nhận {userId} — cập nhật users.role_id sang CENTER_ADMIN (id 2) và ghi managed_center_id trong cùng một @Transaction, chỉ caller SYSTEM_ADMIN được phép, mọi thay đổi ghi audit log append-only kèm actorUserId, targetUserId, centerId, action=CENTER_ADMIN_ASSIGNED và timestamp UTC; DELETE /api/v1/centers/{centerId}/admins/{userId} đảo ngược hoàn toàn thao tác gán — khôi phục role trước đó và xóa managed_center_id, ghi audit action=CENTER_ADMIN_UNASSIGNED; chạy migration V3__center_admin_scope.sql bổ sung cột managed_center_id trên users kèm index phục vụ đối chiếu phạm vi tenant; ném RbacAssignmentDeniedException (403) khi caller thiếu quyền và AssignmentTargetInvalidException (409) khi hủy gán user không đang giữ vai trò Center Admin tại trung tâm chỉ định hoặc gán user đã quản lý trung tâm khác; xác minh centerId tồn tại trước khi mutate, trả 404 CENTER_NOT_FOUND khi thiếu; toàn bộ truy vấn đi qua prepared statement tham số hóa.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [REQ-006], [ARC-002]:**

<!--START_DDL_MIGRATION-->
```sql
-- V3__center_admin_scope.sql (center-service)
-- Tenant scope column mapping Center Admin delegation to a specific center [REQ-006], [ARC-002]
ALTER TABLE users ADD COLUMN managed_center_id UUID REFERENCES centers (center_id);
CREATE INDEX IF NOT EXISTS idx_users_managed_center_id ON users (managed_center_id);
```
<!--END_DDL_MIGRATION-->

* **Hợp đồng Định tuyến API và Sự kiện [REQ-006]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-006], [ARC-002]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "CenterAdminAssignmentExceptionMapper",
  "package": "org.nlh4j.membership_hub.center.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.center.exception.RbacAssignmentDeniedException",
      "httpStatus": 403,
      "errorCode": "RBAC_ASSIGNMENT_DENIED",
      "bodySchema": {
        "errorCode": "RBAC_ASSIGNMENT_DENIED",
        "message": "Only SYSTEM_ADMIN may assign or unassign Center Admin"
      },
      "rule": "Enforced at api-gateway filter and re-checked inside service transaction; every denial writes an audit entry with actorUserId and timestamp"
    },
    {
      "handles": "org.nlh4j.membership_hub.center.exception.AssignmentTargetInvalidException",
      "httpStatus": 409,
      "errorCode": "ASSIGNMENT_TARGET_INVALID",
      "bodySchema": {
        "errorCode": "ASSIGNMENT_TARGET_INVALID",
        "message": "Target user is not an active Center Admin of this center or already manages another center"
      },
      "rule": "Validate current role state and managed_center_id before mutating; no partial updates; unassign of a non-assigned user is rejected"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.3: Kiểm định tích hợp cô lập tenant Center Admin

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/center-service/src/test/java/org/nlh4j/membership_hub/center/CenterAdminIsolationIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-006], [ARC-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Dựng @QuarkusIntegrationTest trên Testcontainers PostgreSQL xác minh: gán Center Admin thành công cập nhật role_id và managed_center_id trong cùng transaction; Center Admin chỉ thao tác dữ liệu trong trung tâm được gán, mọi truy cập tài nguyên thuộc trung tâm khác trả 403 TENANT_SCOPE_VIOLATION; unassign khôi phục trạng thái ban đầu của user (role và managed_center_id về giá trị trước gán); hủy gán user không đang giữ vai trò Center Admin tại trung tâm chỉ định trả 409 ASSIGNMENT_TARGET_INVALID; caller không phải SYSTEM_ADMIN bị chặn 403 RBAC_ASSIGNMENT_DENIED; audit log ghi đủ bản ghi gán/hủy kèm timestamp và userId với action=CENTER_ADMIN_ASSIGNED/CENTER_ADMIN_UNASSIGNED; xác minh không có bản ghi mồ côi sau rollback khi gán thất bại giữa chừng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.4: Thực thể Course và endpoint lưới khóa học GET /api/v1/courses

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/CourseResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-007]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khởi tạo tầng đọc course-service: thực thể Panache Course ánh xạ bảng courses (courseId UUID PK, title VARCHAR(150), description TEXT, startDate/endDate DATE, teacherId UUID FK users, maxStudents INTEGER DEFAULT 30); triển khai CourseResource exposing GET /api/v1/courses trả lưới CourseID, Title, StartDate, EndDate, TeacherName qua LEFT JOIN users lấy full_name của giáo viên, teacherName trả null an toàn khi teacherId chưa được phân công; hỗ trợ phân trang page/size với tham số sắp xếp đi qua whitelist cứng (title, startDate, endDate — ASC/DESC) chặn mọi giá trị ngoài whitelist bằng HTTP 400 chống SQL injection; bổ sung DTO CourseResponse và CourseRequest phục vụ các nghiệp vụ CRUD ở Ngày 3; yêu cầu bearer JWT cho mọi vai trò đã xác thực; áp dụng annotation OpenAPI phục vụ công bố hợp đồng.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-007]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.5: Unit test lưới khóa học

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/CourseResource.java;./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/CourseResourceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-007]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest xác minh cấu trúc lưới khóa học: phản hồi đủ 5 cột CourseID, Title, StartDate, EndDate, TeacherName đúng kiểu dữ liệu ISO-8601; join teacherName trả null an toàn khi teacherId chưa được phân công và trả đúng full_name khi đã gán; phân trang ổn định với tập dữ liệu lớn (seed 500 dòng mẫu) và tham số sắp xếp hợp lệ qua whitelist; tham số sort ngoài whitelist trả 400; caller chưa mang bearer JWT bị chặn 401; đo latency trung bình GET /api/v1/courses giữ dưới 200 ms đối chiếu [NFR-001].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.6: Cập nhật tài liệu phân quyền trung tâm và draft tài liệu khóa học

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-course-service-reference.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-006], [REQ-007]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Bổ sung vào api-center-service-reference.md các endpoint POST/DELETE /api/v1/centers/{centerId}/admins kèm sơ đồ phạm vi tenant managed_center_id, bảng mã lỗi 403 RBAC_ASSIGNMENT_DENIED và 409 ASSIGNMENT_TARGET_INVALID, quy trình audit log gán/hủy; khởi tạo draft api-course-service-reference.md với hợp đồng GET /api/v1/courses, cấu trúc lưới hiển thị 5 cột, quy tắc whitelist sắp xếp và ghi chú teacherName nullable; vẽ sơ đồ Mermaid quan hệ USERS ||--o{ COURSES qua teacher_id và USERS ||--o{ CENTERS qua managed_center_id phản chiếu đúng schema sau migration V3; neo mọi mục vào thẻ truy vết [REQ-006], [REQ-007].

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 3:
<!--DAY_HEADER_START-->CRUD Khóa Học Chống Xung Đột Lịch Và Tối Ưu Truy Vấn Phát Hiện Giao Thoa<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.1: CourseService chặn xung đột lịch giáo viên

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/CourseService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai CourseService @Transactional với create/update/delete khóa học: trước khi persist, truy vấn mọi khóa học của teacherId có khoảng [startDate, endDate] giao thoa theo điều kiện start_date <= :endDate AND end_date >= :startDate; nếu phát hiện chồng lấn ném ScheduleConflictException ánh xạ HTTP 422 kèm conflictingCourseId để admin điều chỉnh lịch hoặc đổi giáo viên; validate endDate >= startDate ở tầng DTO, vi phạm trả 422 DATE_RANGE_INVALID liệt kê từng trường không hợp lệ; áp dụng maxStudents mặc định 30 khi thiếu trường đầu vào và chặn giá trị <= 0; giới hạn quyền ghi cho SYSTEM_ADMIN và CENTER_ADMIN qua kiểm tra claim vai trò, các vai trò khác ném RbacAccessDeniedException ánh xạ 403; thao tác update loại trừ chính khóa đang sửa khỏi kiểm tra giao thoa; toàn bộ persist chạy trong cùng transaction bảo đảm rollback nguyên vẹn; mọi truy vấn đi qua prepared statement tham số hóa chống SQL injection.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-008]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-008]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "CourseExceptionMapper",
  "package": "org.nlh4j.membership_hub.course.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.course.exception.ScheduleConflictException",
      "httpStatus": 422,
      "errorCode": "SCHEDULE_CONFLICT",
      "bodySchema": {
        "errorCode": "SCHEDULE_CONFLICT",
        "message": "Teacher already scheduled for an overlapping course",
        "conflictingCourseId": "uuid"
      },
      "rule": "Overlap check runs before persist using parameterized query on idx_courses_teacher_dates; rollback cleanly on conflict without orphan records"
    },
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 422,
      "errorCode": "DATE_RANGE_INVALID",
      "bodySchema": {
        "errorCode": "DATE_RANGE_INVALID",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "endDate earlier than startDate or missing required fields return per-field invalidFields list preserving DTO declaration order"
    },
    {
      "handles": "org.nlh4j.membership_hub.course.exception.CourseNotFoundException",
      "httpStatus": 404,
      "errorCode": "COURSE_NOT_FOUND",
      "bodySchema": {
        "errorCode": "COURSE_NOT_FOUND",
        "message": "Course does not exist"
      },
      "rule": "Validate courseId existence before update or delete; no partial mutations"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.2: Repository phát hiện giao thoa và migration index khóa học

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/CourseRepository.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Bổ sung vào CourseRepository truy vấn overlap findOverlappingCourses(teacherId, startDate, endDate) dùng prepared statement với điều kiện start_date <= :endDate AND end_date >= :startDate AND teacher_id = :teacherId, loại trừ courseId đang cập nhật qua tham số excludeCourseId; chạy migration V2__course_schedule_indexes.sql tạo idx_courses_title phục vụ lưới danh sách và tìm kiếm tiêu đề, cùng composite index idx_courses_teacher_dates (teacher_id, start_date, end_date) bảo đảm kiểm tra xung đột và lưới danh sách đạt độ trễ sub-second; cung cấp phương thức đếm tổng số dòng phục vụ phân trang; nghiêm cấm nối chuỗi đầu vào vào câu lệnh SQL, mọi tham số đi qua positional/named parameter.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [REQ-007], [REQ-008]:**

<!--START_DDL_MIGRATION-->
```sql
-- V2__course_schedule_indexes.sql (course-service)
-- Index supporting course listing grid and title search [REQ-007]
CREATE INDEX IF NOT EXISTS idx_courses_title ON courses (title);
-- Composite index accelerating teacher schedule overlap detection [REQ-008]
CREATE INDEX IF NOT EXISTS idx_courses_teacher_dates ON courses (teacher_id, start_date, end_date);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.3: Kiểm định tích hợp xung đột lịch

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/CourseScheduleConflictIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Dựng @QuarkusIntegrationTest trên Testcontainers PostgreSQL với nhiều kịch bản biên: chèn khóa học chồng lấn hoàn toàn cùng giáo viên trả 422 SCHEDULE_CONFLICT kèm conflictingCourseId đúng; khoảng chạm biên (endDate của khóa A trùng startDate của khóa B) xử lý đúng nghiệp vụ giao thoa bao gồm; cập nhật khóa học không tự xung đột với chính nó khi giữ nguyên khoảng ngày; hai giáo viên khác nhau cùng khung giờ được chấp nhận; khóa học không có giáo viên (teacherId null) bỏ qua kiểm tra giao thoa; maxStudents thiếu trường đầu vào mặc định 30 và giá trị 0 hoặc âm bị chặn 422; endDate sớm hơn startDate trả 422 DATE_RANGE_INVALID; caller MANAGER/TEACHER/STUDENT gọi endpoint ghi bị chặn 403; xác minh rollback sạch không để lại bản ghi mồ côi khi xung đột xảy ra giữa chừng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.4: Rà soát hiệu quả phát hiện xung đột lịch

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/course-service-review-conflict-detection.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Phân tích kế hoạch truy vấn overlap qua EXPLAIN bảo đảm sử dụng composite index idx_courses_teacher_dates thay vì sequential scan; rà soát race condition khi hai request tạo khóa học đồng thời trên cùng giáo viên — đề xuất khóa biên SELECT ... FOR UPDATE trên dòng tham chiếu hoặc mức cô lập transaction REPEATABLE READ phù hợp, ghi nhận quyết định kiến trúc; kiểm tra điều kiện giao thoa bao gồm đúng hai biên (start_date <= :endDate AND end_date >= :startDate) không lệch off-by-one; chuẩn hóa thông báo lỗi xung đột trả về client kèm conflictingCourseId mà không leak chi tiết SQL; đối chiếu OWASP A03 injection: xác minh không tồn tại đường nối chuỗi trong repository; lập danh sách remediation ưu tiên và chốt điều kiện mở khóa Ngày 4.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.5: Hoàn thiện tài liệu tham chiếu API course-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-course-service-reference.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cập nhật api-course-service-reference.md với hợp đồng CRUD khóa học đầy đủ POST/PUT/DELETE /api/v1/courses: schema request/response, mã lỗi 422 SCHEDULE_CONFLICT kèm ví dụ payload xung đột chứa conflictingCourseId, 422 DATE_RANGE_INVALID, 404 COURSE_NOT_FOUND; ghi chú ma trận quyền SYSTEM_ADMIN/CENTER_ADMIN được ghi và các vai trò còn lại chỉ đọc; mô tả quy tắc maxStudents mặc định 30, điều kiện giao thoa bao gồm hai biên và hành vi bỏ qua kiểm tra khi teacherId null; bổ sung ví dụ curl cho kịch bản xung đột và kịch bản thành công; neo mọi mục vào thẻ truy vết [REQ-007], [REQ-008] và liên kết chéo với từ điển dữ liệu bảng COURSES từ Giai đoạn 1.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 4:
<!--DAY_HEADER_START-->Phân Công Giáo Viên Phát Sự Kiện Đa Kênh Và Bộ Lọc RBAC Năm Vai Trò Tại API Gateway<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.1: Sinh descriptor module con api-gateway kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/api-gateway/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module api-gateway kế thừa parent membership-hub-backend; đăng ký vào danh sách `<modules>` của descriptor cha sau course-service; khai báo dependency quarkus-rest, quarkus-smallrye-jwt, quarkus-oidc phục vụ giải mã và kiểm chứng JWT tại cổng, quarkus-hibernate-validator và quarkus-smallrye-openapi phục vụ phục vụ spec OpenAPI tĩnh; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=api-gateway; cấu hình mp.jwt.verify.publickey.location trỏ tới public key RS256 phát hành bởi auth-service ở Giai đoạn 1 qua biến môi trường không chứa secret hardcode; bổ sung dependency test scope junit-jupiter, rest-assured và testcontainers làm nền cho suite kiểm thử ma trận RBAC và E2E hợp đồng tích hợp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.2: Endpoint phân công giáo viên vào khóa học

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/TeacherAssignmentResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-009]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai TeacherAssignmentResource với hai endpoint: POST /api/v1/courses/{courseId}/teacher nhận {teacherId} — ghi ánh xạ course–teacher (cập nhật courses.teacher_id) trong @Transaction, chỉ SYSTEM_ADMIN được thao tác, caller khác ném RbacAccessDeniedException ánh xạ 403; xác minh teacherId tồn tại và mang vai trò TEACHER trước khi gán, trả 404 USER_NOT_FOUND khi thiếu; sau khi gán thành công phát sự kiện teacher.assigned.v1 lên topic course.teacher.events để notification-service queue push notification tới mobile app của giáo viên được chỉ định; DELETE /api/v1/courses/{courseId}/teacher gỡ ánh xạ (set teacher_id NULL) và dừng luồng thông báo liên quan, ghi audit log cả hai thao tác kèm timestamp và userId; xác minh courseId tồn tại trước khi mutate trả 404 COURSE_NOT_FOUND khi thiếu; toàn bộ truy vấn đi qua prepared statement.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-009]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.3: Hợp đồng sự kiện teacher.assigned.v1 phát lên Kafka

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/event/TeacherAssignedEvent.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-009], [ARC-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Định nghĩa record TeacherAssignedEvent với các trường eventId (UUID duy nhất mỗi lần phát), courseId, teacherId, assignedBy (userId của caller), occurredAt (timestamp ISO-8601 UTC); cấu hình Kafka emitter qua SmallRye Reactive Messaging phát lên topic course.teacher.events với serialization JSON thống nhất mà notification-service sẽ tiêu thụ ở Giai đoạn 4; bảo đảm chế độ at-least-once và consumer deduplicate theo eventId — eventId được sinh ổn định theo cặp (courseId, teacherId, thao tác) để phát lặp không tạo thông báo nhân bản; cấu hình partition key theo courseId bảo đảm thứ tự xử lý trong phạm vi từng khóa học; không đưa PII nhạy cảm vào payload sự kiện; ghi audit log mỗi lần phát sự kiện kèm eventId phục vụ truy vết.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-009], [ARC-008]:**

<!--START_API_CONTRACT-->
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
  "partitionKey": "courseId",
  "consumer": "notification-service"
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.4: Bộ lọc RBAC 5 vai trò tại api-gateway

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/api-gateway/src/main/java/org/nlh4j/membership_hub/gateway/rbac/RoleAuthorizationFilter.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai RoleAuthorizationFilter (ContainerRequestFilter @Priority ưu tiên chạy trước routing) cùng hai lớp hỗ trợ RoleScope (enum ma trận quyền) và TenantScopeContext (CDI request-scoped lưu managed_center_id giải mã từ JWT): giải mã và kiểm chứng chữ ký JWT RS256, đối chiếu claim vai trò với ma trận quyền 5 vai trò — System Admin toàn quyền mọi trung tâm gồm đọc/ghi/xóa trung tâm, gán/hủy Center Admin, CRUD khóa học và phân công giáo viên [ARC-001]; Center Admin giới hạn trong phạm vi managed_center_id, được CRUD khóa học nhưng không gán/hủy Center Admin hay phân công giáo viên [ARC-002]; Manager bị chặn course.write, course.delete và teacher.assign nhưng được đọc danh sách [ARC-003]; Teacher chỉ đọc lịch dạy các khóa được phân công [ARC-004]; Student chỉ duyệt danh sách công khai [ARC-005]; với request trỏ tới tài nguyên trung tâm cụ thể, filter đối chiếu centerId trên đường dẫn với managed_center_id trong TenantScopeContext và ném TenantScopeViolationException khi vượt phạm vi; chặn 403 ngay tại gateway trước khi route tới service nghiệp vụ; mọi lần từ chối ghi audit log kèm userId, đường dẫn và timestamp; filter không tự thực hiện truy vấn database, toàn bộ phạm vi tenant suy từ claim JWT để giữ độ trễ gateway tối thiểu.

* **Hợp đồng Định tuyến API và Sự kiện [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "GatewayExceptionMapper",
  "package": "org.nlh4j.membership_hub.gateway.rbac",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.gateway.rbac.RbacAccessDeniedException",
      "httpStatus": 403,
      "errorCode": "RBAC_ACCESS_DENIED",
      "bodySchema": {
        "errorCode": "RBAC_ACCESS_DENIED",
        "message": "Role claim does not permit this operation"
      },
      "rule": "RoleAuthorizationFilter compares JWT role claim against the 5-role matrix and blocks at the gateway before downstream routing; every denial writes an audit entry"
    },
    {
      "handles": "org.nlh4j.membership_hub.gateway.rbac.TenantScopeViolationException",
      "httpStatus": 403,
      "errorCode": "TENANT_SCOPE_VIOLATION",
      "bodySchema": {
        "errorCode": "TENANT_SCOPE_VIOLATION",
        "message": "Resource centerId is outside the caller managed_center_id scope"
      },
      "rule": "Filter compares path centerId against TenantScopeContext managed_center_id and blocks immediately; no cross-center data leakage"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.5: Unit test phân công giáo viên và sự kiện Kafka

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/TeacherAssignmentResource.java;./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/TeacherAssignmentTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-009], [ARC-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest với InMemoryConnector cho Kafka: gán giáo viên thành công cập nhật courses.teacher_id và phát sự kiện teacher.assigned.v1 với payload đầy đủ eventId/courseId/teacherId/assignedBy/occurredAt; unassign gỡ ánh xạ (teacher_id về NULL) và không phát sự kiện gán; từ chối thao tác từ vai trò CENTER_ADMIN/MANAGER/TEACHER/STUDENT với 403; teacherId không tồn tại hoặc không mang vai trò TEACHER trả 404 USER_NOT_FOUND; courseId không tồn tại trả 404 COURSE_NOT_FOUND; xác minh tính idempotent của eventId khi phát lặp cùng cặp (courseId, teacherId) không tạo thông báo nhân bản; xác minh partition key theo courseId được gắn đúng vào bản ghi Kafka.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.6: Unit test ma trận RBAC 5 vai trò

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/api-gateway/src/main/java/org/nlh4j/membership_hub/gateway/rbac/RoleAuthorizationFilter.java;./sources/backend/api-gateway/src/test/java/org/nlh4j/membership_hub/gateway/rbac/RoleAuthorizationFilterTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest phủ ma trận 5 vai trò × nhóm endpoint: System Admin pass toàn bộ endpoint quản trị trung tâm, gán/hủy Center Admin, CRUD khóa học và phân công giáo viên [ARC-001]; Center Admin pass đọc/ghi/xóa khóa học trong trung tâm sở tại và fail 403 TENANT_SCOPE_VIOLATION khi trỏ tới trung tâm khác managed_center_id, bị chặn khi tự gán/hủy Center Admin [ARC-002]; Manager pass endpoint đọc nhưng bị chặn 403 RBAC_ACCESS_DENIED khi gọi course.write, course.delete và teacher.assign [ARC-003]; Teacher bị chặn mọi thao tác ghi, chỉ pass đọc khóa học được phân công [ARC-004]; Student chỉ pass endpoint đọc công khai, bị chặn mọi endpoint quản trị [ARC-005]; JWT thiếu claim role hoặc mang chữ ký sai bị chặn 401 trước khi vào ma trận; xác minh mỗi lần từ chối ghi đúng một dòng audit log kèm userId và đường dẫn.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.7: Blueprint topology RBAC

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/rbac-topology-blueprint.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn blueprint RBAC: sơ đồ Mermaid luồng JWT qua api-gateway (client → Ingress TLS → RoleAuthorizationFilter → downstream service), bảng ma trận quyền đầy đủ 5 vai trò × nhóm tài nguyên (centers, centerAdminAssignment, courses, teacherAssignment), quy tắc phạm vi tenant theo managed_center_id kèm ví dụ request hợp lệ và vi phạm, cơ chế audit log thay đổi vai trò và phân công kèm timestamp/userId, hướng dẫn mở rộng vai trò mới trong tương lai (thêm dòng ma trận và seed roles); mô tả vị trí thực thi kép gateway filter + kiểm chứng lại tại từng dịch vụ theo nguyên tắc defense-in-depth; neo mọi mục vào thẻ truy vết [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] và liên kết chéo với api-center-service-reference.md cùng api-course-service-reference.md.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 5:
<!--DAY_HEADER_START-->Công Bố Hợp Đồng OpenAPI Bốn Luồng Tích Hợp Liên Dịch Vụ Và Kiểm Định E2E Đa Vai Trò<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.1: Hợp đồng OpenAPI xác thực OAuth2/JWT

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/api-gateway/src/main/resources/openapi/auth-integration-contract.yaml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Công bố spec OpenAPI 3.0.3 cho luồng xác thực liên dịch vụ: POST /api/v1/auth/register, POST /api/v1/auth/login, POST /api/v1/auth/oauth2/{provider} với enum provider firebase/google/facebook, POST /api/v1/auth/refresh; định nghĩa securityScheme bearerAuth kiểu http scheme bearer bearerFormat JWT với access token RS256 hết hạn 15 phút (900 giây) và refresh token opaque TTL 7 ngày (604800 giây); chuẩn hóa schema lỗi xác thực (401 OAUTH2_CODE_EXCHANGE_FAILED, 400 AUTH_VALIDATION_FAILED, 409 EMAIL_ALREADY_EXISTS) cho toàn bộ consumer liên dịch vụ tham chiếu; spec phải pass kiểm tra lint swagger-cli validate và được neo làm nguồn tham chiếu chính thức cho tài liệu integration-contracts-openapi.md.

* **Hợp đồng Định tuyến API và Sự kiện [ARC-006]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.2: Hợp đồng OpenAPI điểm danh QR, thông báo đa kênh và mobile bearer

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/api-gateway/src/main/resources/openapi/integration-contracts.yaml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Công bố spec OpenAPI 3.0.3 hợp nhất ba luồng còn lại: POST /api/v1/attendance/scan với semantic idempotency key (studentId, courseId, attendanceDate) và phản hồi 200 mang cờ duplicate already_recorded cho lần quét trùng cùng ngày [ARC-007]; POST /api/v1/notifications/dispatch điều phối đa kênh FCM/APNs/Zalo trả 202 QUEUED kèm chính sách retry tối đa 3 lần trước khi đánh dấu failed [ARC-008]; GET /api/v1/mobile/session hợp đồng mobile bearer token với header ETag và Cache-Control phục vụ caching ngoại tuyến khi mất kết nối [ARC-009]; định nghĩa securityScheme bearerAuth dùng chung; spec phải pass swagger-cli validate và nhất quán schema với chuỗi migration notifications (delivery_status, retry_count <= 3) đã neo ở Giai đoạn 1.

* **Hợp đồng Định tuyến API và Sự kiện [ARC-007], [ARC-008], [ARC-009]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.3: Kiểm định E2E ma trận RBAC và hợp đồng tích hợp

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/api-gateway/src/test/java/org/nlh4j/membership_hub/gateway/rbac/RbacMatrixIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Dựng @QuarkusIntegrationTest profile E2E chạy qua api-gateway với Testcontainers PostgreSQL và Kafka: xác thực OAuth2/JWT cấp access token 15 phút và refresh token 7 ngày, giải mã xác nhận claims role và exp−iat=900s [ARC-006]; gọi POST /api/v1/attendance/scan hai lần cùng student/course/ngày nhận lần đầu RECORDED và lần hai duplicate=true already_recorded không phát sinh bản ghi mới, đối chiếu ràng buộc uq_attendance_idempotent [ARC-007]; kích hoạt POST /api/v1/notifications/dispatch và xác minh hàng đợi retry tối đa 3 lần khi device token invalid trước khi đánh dấu failed [ARC-008]; gọi GET /api/v1/mobile/session xác minh phản hồi mang header ETag và Cache-Control phục vụ offline cache [ARC-009]; toàn bộ kịch bản chạy lặp lại dưới 5 vai trò RBAC (System Admin, Center Admin, Manager, Teacher, Student) để xác minh rào chắn phân quyền đầu-cuối: mỗi vai trò chỉ pass đúng nhóm endpoint của ma trận và mọi vi phạm bị chặn 403 tại gateway; đo latency trung bình các luồng giữ dưới 200 ms đối chiếu [NFR-001].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.4: Báo cáo rà soát cuối giai đoạn 2

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/phase2-final-review-report.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tổng hợp rà soát cuối giai đoạn: tính nhất quán giữa hai spec OpenAPI công bố (auth-integration-contract.yaml, integration-contracts.yaml) và implementation thực tế của center-service/course-service — đối chiếu từng path, schema và mã lỗi; độ bao phủ test ma trận RBAC 5 vai trò qua báo cáo JaCoCo xác nhận ≥ 85%; kiểm toán bảo mật OWASP Top 10 trên toàn bộ diff giai đoạn (A01 broken access control qua ma trận RBAC, A03 injection qua prepared statement và whitelist sắp xếp, A05 misconfiguration qua cấu hình JWT); phát hiện nợ kỹ thuật và kế hoạch khắc phục trước khi bước vào Giai đoạn 3 (enrollment-service, attendance-service, card-service); ký duyệt bàn giao kèm verdict GO/NO-GO và danh sách hành động khắc phục nếu NO-GO.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.5: Tài liệu hợp đồng tích hợp OpenAPI

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/integration-contracts-openapi.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn tài liệu tham chiếu bốn luồng tích hợp: sơ đồ sequence Mermaid OAuth2/JWT với vòng đời access token 15 phút và refresh token 7 ngày kèm cơ chế xoay vòng [ARC-006]; hợp đồng attendance idempotent và ngữ nghĩa cờ duplicate already_recorded đối chiếu ràng buộc unique (studentId, courseId, attendanceDate) [ARC-007]; ma trận kênh thông báo FCM/APNs/Zalo kèm chính sách retry tối đa 3 lần và các trạng thái QUEUED/DELIVERED/FAILED [ARC-008]; quy ước mobile bearer offline caching qua header ETag và Cache-Control kèm ví dụ phản hồi [ARC-009]; đính kèm đường dẫn tới hai file YAML trong api-gateway làm nguồn tham chiếu chính thức, bảng mã lỗi chuẩn hóa và hướng dẫn consumer mới tích hợp vào hợp đồng; neo mọi mục vào thẻ truy vết tương ứng và liên kết chéo với rbac-topology-blueprint.md.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->