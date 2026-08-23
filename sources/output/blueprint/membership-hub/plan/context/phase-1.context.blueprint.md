# Giai đoạn 1: <!--PHASE_NAME_START-->Khởi Tạo Khung Dự Án, Lược Đồ Dữ Liệu Hợp Nhất Và Dịch Vụ Xác Thực<!--PHASE_NAME_END-->

## 📊 Kiểm soát Tài liệu

| Hạng mục | Chi tiết |
| :--- | :--- |
| **ID Bản thiết kế** | ARCH-20260823050512 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Khởi Tạo Khung Dự Án, Lược Đồ Dữ Liệu Hợp Nhất Và Dịch Vụ Xác Thực<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Hoàn tất nền móng hạ tầng của nền tảng membership-hub: sinh descriptor build gốc Maven multi-module cùng descriptor module con auth-service và db-migrations theo mô hình microservices Java 21/Quarkus 3.15, đồng thời khởi tạo workspace frontend Next.js/React Native với TypeScript strict mode [ARC-000]; thực thi chuỗi Flyway migration V1→V9 tạo đủ 11 bảng lõi với khóa ngoại, unique constraint và index truy vấn sub-second [DAT-001] đến [DAT-011]; triển khai endpoint POST /api/v1/auth/register hash bcrypt cost 12 cấp JWT RS256 15 phút kèm refresh token 7 ngày với cơ chế liệt kê từng trường không hợp lệ khi validation thất bại [REQ-001], [EXC-004]; tích hợp đăng nhập mạng xã hội OAuth2 Firebase/Google/Facebook [REQ-002]; xây dựng API gán/thay đổi vai trò người dùng kèm audit log append-only [REQ-003]. Tester bàn giao JUnit suite auth, integration test migration CSDL và profile E2E đăng ký; Doc bàn giao blueprint kiến trúc tổng thể và đặc tả tham chiếu API auth-service.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/23 05:05:12 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 1. Phạm vi Vận hành Giai đoạn & Mục tiêu

Giai đoạn 1 thiết lập nền móng hạ tầng của nền tảng membership-hub trên ba trụ cột song song, bao phủ trọn vẹn Task 1, Task 2, Task 3, Task 4, Task 5 và Task 28 của Master Backlog.

Thứ nhất, khởi tạo khung dự án multi-module: descriptor build gốc `./sources/backend/pom.xml` neo Quarkus BOM 3.15.x với dependencyManagement tập trung, hai descriptor module con `auth-service` và `db-migrations`, cùng workspace frontend `./sources/frontend/package.json` và `./sources/frontend/tsconfig.json` strict mode làm nền chung cho web-app và mobile-app [ARC-000].

Thứ hai, thực thi chuỗi Flyway migration V1→V9 tạo đủ 11 bảng lõi (Roles, Users, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, SystemSettings) với khóa ngoại, unique constraint, CHECK constraint và index tối ưu truy vấn sub-second [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]. Cổng idempotent UNIQUE (student_id, course_id, attendance_date) trên bảng Attendance được neo ngay từ tầng schema làm nền cho tính bất biến điểm danh ở các giai đoạn sau.

Thứ ba, xây dựng tầng xác thực auth-service: endpoint POST /api/v1/auth/register hash bcrypt cost 12 cấp JWT RS256 15 phút kèm refresh token 7 ngày, kèm cơ chế liệt kê từng trường không hợp lệ khi validation thất bại [REQ-001], [EXC-004]; đăng nhập mạng xã hội OAuth2 Firebase/Google/Facebook [REQ-002]; API gán/thay đổi vai trò chỉ dành cho System Admin kèm audit log append-only [REQ-003]. Chất lượng được bảo chứng bởi JUnit suite auth, integration test migration trên Testcontainers PostgreSQL và profile E2E vòng đời xác thực; tài liệu được đóng gói qua blueprint kiến trúc, hai từ điển dữ liệu và đặc tả tham chiếu API auth-service.

## 2. Phạm vi Kỹ thuật Được phép & Ranh giới Thư mục (Tệp, đường dẫn và Endpoint)

* **Ma trận thư mục Backend được phép:**
    * ./sources/backend/pom.xml [ARC-000]
    * ./sources/backend/auth-service/pom.xml [ARC-000]
    * ./sources/backend/db-migrations/pom.xml [ARC-000]
    * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/dto/*.java
    * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/*.java
    * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/security/*.java
    * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/resource/*.java
    * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/exception/*.java
    * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/oauth/*.java
    * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/audit/*.java
    * ./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/*.java
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V1__create_roles_and_users_tables.sql [DAT-002], [DAT-001]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V2__create_centers_table.sql [DAT-003]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V3__create_courses_table.sql [DAT-004]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V4__create_enrollments_table.sql [DAT-005]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V5__create_attendance_table.sql [DAT-006]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V6__create_student_cards_table.sql [DAT-007]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V7__create_notifications_table.sql [DAT-008]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V8__create_promotions_and_announcements_tables.sql [DAT-009], [DAT-010]
    * ./sources/backend/db-migrations/src/main/resources/db/migration/V9__create_system_settings_table.sql [DAT-011]
    * ./sources/backend/db-migrations/src/test/java/org/nlh4j/membership_hub/db/*.java
* **Ma trận thư mục Frontend được phép:**
    * ./sources/frontend/package.json [ARC-000]
    * ./sources/frontend/tsconfig.json [ARC-000]
* **Ma trận thư mục Tài liệu được phép:**
    * ./sources/docs/architecture-blueprint.md [ARC-000]
    * ./sources/docs/data-dictionary-core-tables.md [DAT-001], [DAT-002], [DAT-003], [DAT-004]
    * ./sources/docs/data-dictionary-operational-tables.md [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]
    * ./sources/docs/api-auth-service-reference.md [REQ-001], [EXC-004], [REQ-002], [REQ-003]
* **Mẫu định tuyến Endpoint được phép trong giai đoạn:**
    * POST /api/v1/auth/register — PUBLIC [REQ-001], [EXC-004]
    * POST /api/v1/auth/oauth2/{provider} — PUBLIC, provider ∈ {firebase, google, facebook} [REQ-002]
    * PUT /api/v1/admin/users/{userId}/role — BEARER JWT, role=SYSTEM_ADMIN [REQ-003]
* **Ranh giới cấm xâm phạm:** mọi module và endpoint thuộc center-service, course-service, enrollment-service, attendance-service, card-service, notification-service, promotion-service, chatbot-service, reporting-service, api-gateway cùng toàn bộ cây ./sources/infra/ được dành riêng cho các giai đoạn 2 đến 5; Giai đoạn 1 nghiêm cấm phát sinh tệp ngoài ma trận trên.

* **INVARIANT KHUNG NỀN TẢNG BẮT BUỘC (PLATFORM SKELETON MANIFEST INVARIANTS)**:
    * Khi khởi tạo vòng đời vận hành (bên trong NGÀY 1 của Giai đoạn 1), hệ thống bắt buộc khai báo descriptor hạ tầng repository trước khi phát hành bất kỳ thành phần mã nguồn ứng dụng nào.
    * Với topology microservices backend, bắt buộc neo đường dẫn descriptor cha `./sources/backend/pom.xml` và các manifest module con độc lập `./sources/backend/<service-name>/pom.xml`.
    * Với lớp giao diện frontend đang kích hoạt, bắt buộc đăng ký cấu hình `./sources/frontend/package.json` và `./sources/frontend/tsconfig.json`. Toàn bộ tài sản scaffolding sinh ra phải ánh xạ nghiêm ngặt vào token theo dõi kiến trúc [ARC-000].

## 3. Chỉ đạo Chức năng Sub-Agent Chuyên trách

Theo ma trận phân công của Giai đoạn 1, các Sub-Agent được kích hoạt gồm Coder, Tester, Reviewer và Doc; Docker, GCP và GKE được dự phòng và chỉ kích hoạt từ Giai đoạn 5.

* **Coder**: Đóng vai trò Lập trình viên Ứng dụng Cấp cao/Principal. Chịu trách nhiệm hiện thực mã nguồn ứng dụng thuần túy trên cả dịch vụ backend lẫn client frontend/mobile: descriptor Maven multi-module, chuỗi migration Flyway, DTO/service/resource/security/audit của auth-service và cấu hình workspace frontend. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng DevOps.
* **Tester**: Đóng vai trò Trưởng QC/QA Principal. Chuyên về kỹ nghệ bộ kiểm thử, xác nhận và cổng chất lượng. Chịu trách nhiệm sinh JUnit, integration test trên Testcontainers PostgreSQL, E2E automation và kịch bản đo hiệu năng cho luồng xác thực. Bị cấm sửa mã production. Khi phạm vi kiểm thử mang tính tích hợp tổng thể hoặc E2E không cô lập được một tệp production đơn lẻ, bắt buộc dùng định dạng cặp semicolon với token `INTEGRATION_SCOPE` đứng đầu (ví dụ: `INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/AuthLifecycleE2EIT.java`).
* **Doc**: Đóng vai trò Nhà văn Kỹ thuật Principal và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên biên soạn tài liệu đặc tả kỹ thuật, từ điển dữ liệu, blueprint kiến trúc và danh mục doanh nghiệp phù hợp topology dự án. Mọi tệp tài liệu phải là đường dẫn tệp tường minh đuôi `.md` nằm trong kho lưu trữ tập trung `./sources/docs/`. Theo luật định giai đoạn, Doc phải được phân công tối thiểu một nhiệm vụ nền móng ngay NGÀY 1 để khởi tạo khung tài liệu markdown, sơ đồ lược đồ dữ liệu và catalog kiến trúc tương thích stack Java/Quarkus/PostgreSQL của ngữ cảnh này.
* **Reviewer**: Chịu trách nhiệm xác minh biên dịch, cổng phân tích tĩnh và vá phòng thủ. Chuyên kiểm toán chất lượng mã, xử lý lỗi compile, khắc phục lỗ hổng bảo mật OWASP Top 10 và gỡ blocker SonarQube trước khi merge; ký duyệt điều kiện mở khóa giữa các ngày làm việc.
* **Docker**: Chuyên container hóa, kỹ nghệ Dockerfile multi-stage, tối ưu dung lượng image và đẩy image đã kiểm chứng lên registry. Trong Giai đoạn 1 chưa được phân công nhiệm vụ cụ thể.
* **GCP**: Chuyên tự động hóa trên Google Cloud Platform: build/push image lên Artifact Registry và điều phối môi trường container trên Cloud Run. Trong Giai đoạn 1 chưa được phân công nhiệm vụ cụ thể.
* **GKE**: Chuyên điều phối container production trong Google Kubernetes Engine: manifest deployment, routing control, cấu hình HPA, Helm chart và triển khai workload microservices. Trong Giai đoạn 1 chưa được phân công nhiệm vụ cụ thể.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)

* 100% thẻ truy vết của giai đoạn ([ARC-000], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [EXC-004]) được ánh xạ tường minh vào nhật ký ngày qua container `<!--START_TAGS-->` không gaps.
* `mvn -q verify` sạch trên descriptor cha và hai module con; workspace frontend pass `tsc --noEmit` ở chế độ strict; cây Maven không xung đột phiên bản.
* Chuỗi Flyway V1→V9 chạy sạch trên PostgreSQL 16 Testcontainers; information_schema xác nhận đủ 11 bảng lõi và đúng 5 dòng seed roles.
* Endpoint POST /api/v1/auth/register trả 201 với accessToken RS256 exp=900s và refreshToken TTL=604800s; bcrypt cost 12 khớp cột CHAR(60); phản hồi 400 trả mảng invalidFields liệt kê từng trường; phản hồi 409 trả EMAIL_ALREADY_EXISTS [REQ-001], [EXC-004].
* OAuth2 ba provider firebase/google/facebook exchange thành công với cờ isNewUser chính xác; authorization code bị từ chối trả 401 OAUTH2_CODE_EXCHANGE_FAILED [REQ-002].
* Role assignment chỉ chấp nhận caller SYSTEM_ADMIN; mỗi thay đổi phát sinh đúng một dòng audit append-only action=USER_ROLE_CHANGED kèm timestamp và userId [REQ-003].
* Độ bao phủ kiểm thử tự động ≥ 85%; latency trung bình register ≤ 200 ms trong profile E2E đối chiếu ràng buộc [NFR-001].
* Tuân thủ OWASP Top 10: không log password/hash/token ở bất kỳ tầng nào; toàn bộ truy vấn đi qua prepared statement; thông điệp lỗi không dò được sự tồn tại tài khoản.
* Bốn tài liệu ./sources/docs/ hoàn chỉnh, liên kết chéo nhất quán với schema và hợp đồng API thực tế.
* Zero blocker SonarQube; mọi merge thực hiện qua pull request squash theo quy trình phân nhánh hàng ngày.

## 5. Nhật ký Thực thi Kiến trúc Theo Ngày

<!--START_DAY_LOG_INDEX-->

### 🌤️ NGÀY 1:
<!--DAY_HEADER_START-->Khởi Tạo Khung Dự Án Backend Multi-Module Và Workspace Frontend TypeScript Strict Mode<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.1: Sinh descriptor build gốc Maven cho chuỗi dịch vụ Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo packaging=pom với groupId org.nlh4j, artifactId membership-hub-backend, version 1.0.0-SNAPSHOT; import Quarkus BOM 3.15.x vào dependencyManagement tập trung để khóa phiên bản toàn chuỗi dịch vụ; cố định maven-compiler-plugin ở release Java 21 với encoding UTF-8; liệt kê hai module con auth-service và db-migrations theo thứ tự phụ thuộc; thiết lập hai profile dev và production kiểm soát biến cấu hình môi trường thống nhất (quarkus.profile, datasource host, redis endpoint) không chứa secret hardcode; khai báo pluginManagement dùng chung cho quarkus-maven-plugin, surefire và failsafe bảo đảm mọi module con kế thừa vòng đời build đồng nhất. Nghiêm cấm khai báo trùng phiên bản dependency ở module con gây xung đột cây Maven.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.2: Sinh descriptor module con auth-service

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Kế thừa parent membership-hub-backend mà không tái khai báo phiên bản; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-redis-client, quarkus-hibernate-validator cùng quarkus-flyway phục vụ bootstrap schema; gắn quarkus-maven-plugin cho các goal dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=auth-service phục vụ đóng gói image ở giai đoạn DevOps; bổ sung dependency test scope junit-jupiter, rest-assured và testcontainers-postgresql làm nền cho suite kiểm thử của Tester ở các ngày tiếp theo.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.3: Sinh descriptor module con db-migrations

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Thiết lập module chuyên chứa tài nguyên Flyway: dependency flyway-core và org.postgresql:postgresql driver scope runtime; cấu hình maven-resources-plugin giữ nguyên thư mục db/migration khi copy tài nguyên để tên file V{n}__{description}.sql không bị biến đổi; đóng gói toàn bộ chuỗi migration vào artifact triển khai chung để auth-service và các dịch vụ ở giai đoạn sau tham chiếu cùng một nguồn schema duy nhất; cấm phát sinh mã Java trong module này ngoài lớp bootstrap tối thiểu.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.4: Khởi tạo manifest workspace frontend Next.js/React Native

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/package.json

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo scripts dev/build/lint/start chuẩn npm workspaces; khai báo dependencies next 14.2.x, react 18.3.x, react-dom, react-native 0.75.x, expo SDK 51, typescript 5.5.x; devDependencies eslint, prettier, tailwindcss 3.4.x; cấu hình workspaces trỏ tới hai ứng dụng con web-app và mobile-app làm nền chung cho các giai đoạn giao diện phía sau; đặt private:true chặn publish nhầm lên registry; ghim engines node >= 20 bảo đảm tương thích build CI GitHub Actions.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.5: Cấu hình biên dịch TypeScript strict mode

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/tsconfig.json

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Bật strict:true, noUncheckedIndexedAccess, exactOptionalPropertyTypes, noImplicitOverride; ánh xạ path alias @/* về src/* phục vụ import tuyệt đối; chọn target ES2022, lib DOM+ES2022, moduleResolution bundler, jsx preserve để tương thích đồng thời Next.js SSR và React Native Metro bundler; bật skipLibCheck giảm nhiễu kiểu từ thư viện bên thứ ba; cấu hình include phủ src và exclude node_modules/dist/.next.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.6: Kiểm chứng bootstrap context dịch vụ xác thực

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/BootstrapContextIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusIntegrationTest khởi động auth-service từ descriptor vừa sinh; xác minh application context tải thành công, health probe /q/health trả UP cho cả liveness và readiness; chạy `mvn -q dependency:tree` khẳng định cây Maven không xung đột phiên bản giữa Quarkus BOM và dependency của module con; fail build ngay nếu bootstrap lỗi hoặc xuất hiện convergence warning; ghi kết quả smoke nền móng vào báo cáo kiểm thử làm điều kiện mở khóa Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.7: Kiểm toán chất lượng descriptor build

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Rà soát dependencyManagement tránh phiên bản trùng lặp hoặc xung đột plugin; chuẩn hóa thứ tự khai báo module theo chiều phụ thuộc db-migrations trước auth-service; đối chiếu encoding UTF-8 và release 21 trên compiler; kiểm tra profile dev/production không chứa credential hardcode; lập danh sách remediation ưu tiên kèm chủ sở hữu fix và chốt điều kiện mở khóa giai đoạn xây dựng lược đồ dữ liệu ở Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.8: Biên soạn bản phác thảo blueprint kiến trúc tổng thể

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/architecture-blueprint.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn khung blueprint kiến trúc tổng thể: topology microservices hiện hành (auth-service, db-migrations) và lộ trình 10 dịch vụ mục tiêu; sơ đồ phụ thuộc Maven parent–child; chiến lược profile dev/production; quy ước gói org.nlh4j.membership_hub.*; ma trận stack công nghệ Java 21 LTS/Quarkus 3.15.x/PostgreSQL 16.x/Redis 7.2.x/Kafka 3.7.x; đánh dấu mục lục các phần sẽ bổ sung ở giai đoạn sau (RBAC gateway, enrollment, notification đa kênh, reporting); neo mọi mục vào thẻ truy vết [ARC-000] và chuẩn bị cấu trúc liên kết chéo cho từ điển dữ liệu cũng như đặc tả API auth-service.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 2:
<!--DAY_HEADER_START-->Xây Dựng Lược Đồ Dữ Liệu Hạt Nhân Roles, Users, Centers, Courses Với Ràng Buộc Và Index Tối Ưu<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.1: Migration V1 — bảng Roles và Users kèm seed 5 vai trò

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V1__create_roles_and_users_tables.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-002], [DAT-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo extension pgcrypto phục vụ gen_random_uuid(); dựng bảng roles (role_id SMALLINT PK, name VARCHAR(30) UNIQUE NOT NULL, description VARCHAR(200)) và seed đúng 5 vai trò SYSTEM_ADMIN/CENTER_ADMIN/MANAGER/TEACHER/STUDENT; dựng bảng users với email VARCHAR(255) UNIQUE NOT NULL, password_hash CHAR(60) NOT NULL dành cho bcrypt, full_name VARCHAR(100) NOT NULL, role_id SMALLINT FK về roles, provider VARCHAR(20) DEFAULT 'local' kèm CHECK IN ('local','firebase','google','facebook'), created_at/updated_at TIMESTAMP DEFAULT now(); thêm index idx_users_role_id và idx_users_provider phục vụ lọc vai trò và nguồn xác thực; tuân thủ ANSI SQL nghiêm cấm ENUM inline, thay bằng VARCHAR + CHECK.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-002], [DAT-001]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.2: Migration V2 — bảng Centers ràng buộc taxId số học duy nhất

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V2__create_centers_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo bảng centers với center_id UUID PK DEFAULT gen_random_uuid(), name VARCHAR(100) NOT NULL, address VARCHAR(255) NOT NULL, tax_id VARCHAR(13) NOT NULL UNIQUE kèm CHECK regex ^[0-9]{10,13}$ ép định dạng số 10–13 chữ số, contact_phone VARCHAR(30) nullable, contact_email VARCHAR(255) nullable áp dụng CHECK pattern email khi có giá trị; đặt tên ràng buộc tường minh pk_centers/uq_centers_tax_id/ck_centers_tax_id_digits/ck_centers_contact_email để tầng ứng dụng ở Giai đoạn 2 ánh xạ chính xác lỗi 409 TAX_ID_CONFLICT.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-003]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.3: Migration V3 — bảng Courses với khóa ngoại giáo viên và index lịch

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V3__create_courses_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo bảng courses với course_id UUID PK DEFAULT gen_random_uuid(), title VARCHAR(150) NOT NULL, description TEXT nullable, start_date/end_date DATE NOT NULL kèm CHECK end_date >= start_date, teacher_id UUID FK về users(user_id) cho phép NULL, max_students INTEGER NOT NULL DEFAULT 30 kèm CHECK > 0; tạo index idx_courses_teacher_id và idx_courses_start_date phục vụ tra cứu lịch dạy và lưới khóa học đạt độ trễ sub-second ở Giai đoạn 2.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-004]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.4: Integration test chuỗi migration hạt nhân V1–V3 trên Testcontainers

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/db-migrations/src/test/java/org/nlh4j/membership_hub/db/CoreSchemaMigrationIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-001], [DAT-002], [DAT-003], [DAT-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Dùng Testcontainers PostgreSQL 16 khởi động container sạch rồi chạy Flyway migrate qua module db-migrations; assert bảng roles chứa đúng 5 dòng seed; chèn user hợp lệ với bcrypt hash 60 ký tự thành công; chèn email trùng bị từ chối bởi uq_users_email; tax_id 9 chữ số bị ck_centers_tax_id_digits chặn còn tax_id 10–13 chữ số được chấp nhận; khóa học với end_date sớm hơn start_date bị ck_courses_date_range chặn; đo thời gian migrate toàn chuỗi làm baseline CI và fail pipeline nếu vượt ngưỡng 5 giây.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-001], [DAT-002], [DAT-003], [DAT-004]:**

<!--START_DDL_MIGRATION-->
```sql
-- Verified chain executed by CoreSchemaMigrationIT (V1 -> V3)
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.5: Rà soát ràng buộc ANSI và index lược đồ hạt nhân

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V1__create_roles_and_users_tables.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-001], [DAT-002], [DAT-003], [DAT-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Kiểm tra tuân thủ ANSI SQL: cấm ENUM inline, thay bằng VARCHAR + CHECK; độ kín khóa ngoại users.role_id→roles.role_id và courses.teacher_id→users.user_id; xác nhận unique constraint email/tax_id đặt tên tường minh phục vụ ánh xạ lỗi nghiệp vụ; đánh giá index phục vụ truy vấn danh sách Giai đoạn 2; rà soát an toàn rollback migration và khả năng replay trên môi trường sạch; đề xuất chỉnh sửa trước khi cho phép merge lên nhánh tích hợp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.6: Biên soạn từ điển dữ liệu bốn bảng hạt nhân

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/data-dictionary-core-tables.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-001], [DAT-002], [DAT-003], [DAT-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Mô tả từng cột, kiểu dữ liệu, ràng buộc và giá trị mặc định của 4 bảng hạt nhân ROLES/USERS/CENTERS/COURSES; vẽ sơ đồ quan hệ ROLES ||--o{ USERS và USERS ||--o{ COURSES bằng Mermaid; kèm ví dụ giá trị mẫu và ghi chú ảnh hưởng tới API quản trị trung tâm/khóa học ở Giai đoạn 2; liệt kê từng index kèm mục đích tối ưu truy vấn và ghi chú chính sách bcrypt 60 ký tự cho cột password_hash.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 3:
<!--DAY_HEADER_START-->Hoàn Thiện Chuỗi Migration 11 Bảng Lõi Gồm Enrollments, Attendance Idempotent, StudentCards, Notifications, Promotions, Announcements, SystemSettings<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.1: Migration V4 — bảng Enrollments chặn ghi danh trùng

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V4__create_enrollments_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-005]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo enrollments với enrollment_id UUID PK DEFAULT gen_random_uuid(), student_id UUID NOT NULL FK users(user_id), course_id UUID NOT NULL FK courses(course_id), enrollment_date TIMESTAMP NOT NULL DEFAULT now(); ràng buộc UNIQUE (student_id, course_id) chặn ghi danh trùng cùng khóa; index hai chiều idx_enrollments_student_id và idx_enrollments_course_id phục vụ duyệt khóa học loại trừ các khóa đã có bản ghi và đếm chỗ còn trống ở Giai đoạn 3.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-005]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.2: Migration V5 — bảng Attendance với cổng idempotent ba cột

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V5__create_attendance_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-006]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo attendance với cổng idempotent UNIQUE (student_id, course_id, attendance_date) bảo đảm một dòng duy nhất mỗi học viên/khóa/ngày; recorded_at TIMESTAMP NOT NULL DEFAULT now() tách biệt attendance_date DATE được suy từ clientTimestamp của thiết bị; index composite idx_attendance_course_date (course_id, attendance_date) phục vụ báo cáo điểm danh theo trung tâm và khoảng ngày ở Giai đoạn 5; đây là nền móng schema cho cơ chế trả success kèm cờ duplicate không phát sinh bản ghi mới.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-006]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.3: Migration V6 — bảng StudentCards một thẻ mỗi học viên

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V6__create_student_cards_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-007]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo student_cards với card_id UUID PK, student_id UUID NOT NULL FK users kèm UNIQUE(student_id) bảo đảm một thẻ mỗi học viên, issue_date DATE NOT NULL, validity_days INTEGER NOT NULL CHECK > 0, remaining_days INTEGER NOT NULL DEFAULT 0 do tầng ứng dụng suy ra từ issue_date cộng validityDays theo UTC; index idx_student_cards_student_id phục vụ truy vấn GET /api/v1/cards/me sub-second ở Giai đoạn 3.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-007]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.4: Migration V7 — bảng Notifications với vòng đời trạng thái giao hàng

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V7__create_notifications_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-008]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo notifications với delivery_status VARCHAR(20) NOT NULL DEFAULT 'PENDING' kèm CHECK IN ('PENDING','SENT','RETRYING','FAILED') mô hình hóa vòng đời giao hàng; retry_count SMALLINT NOT NULL DEFAULT 0 kèm CHECK <= 3 tương ứng cơ chế thử lại tối đa ba lần trước khi đánh dấu FAILED; delivered BOOLEAN NOT NULL DEFAULT FALSE; group_zalo VARCHAR(100) nullable cho kênh nhóm Zalo; index idx_notifications_user_id và idx_notifications_status phục vụ quét hàng đợi retry ở Giai đoạn 4.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-008]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.5: Migration V8 — bảng Promotions và Announcements

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V8__create_promotions_and_announcements_tables.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-009], [DAT-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo promotions (code VARCHAR(50) NOT NULL UNIQUE, discount_percent SMALLINT NOT NULL CHECK BETWEEN 1 AND 100, start_date/end_date DATE nullable với end_date NULL nghĩa là khuyến mãi vĩnh viễn, CHECK end_date >= start_date khi có giá trị) và announcements (title VARCHAR(150) NOT NULL, content VARCHAR(2000) NOT NULL, start_date/end_date nullable kèm CHECK khoảng ngày hợp lệ); index idx_announcements_end_date phục vụ tự động ẩn announcement sau ngày hết hạn đã cấu hình ở Giai đoạn 4.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-009], [DAT-010]:**

<!--START_DDL_MIGRATION-->
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
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.6: Migration V9 — bảng SystemSettings key-value

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V9__create_system_settings_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tạo system_settings dạng key-value với setting_key VARCHAR(100) NOT NULL PK, setting_value TEXT NOT NULL, description VARCHAR(255) nullable; làm nơi lưu locale mặc định hệ thống, danh sách locale kích hoạt en/vi/es và tham số SEO hreflang cho giai đoạn bản địa hóa; cấu hình origin CORS theo trung tâm cũng đăng ký tập trung tại đây theo quy ước key cors.allowed.origin.<centerId> phục vụ rào chắn đa tenant.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-011]:**

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE system_settings (
    setting_key    VARCHAR(100)  NOT NULL,
    setting_value  TEXT          NOT NULL,
    description    VARCHAR(255),
    CONSTRAINT pk_system_settings PRIMARY KEY (setting_key)
);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.7: Integration test chuỗi migration đầy đủ V1–V9

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/db-migrations/src/test/java/org/nlh4j/membership_hub/db/FullMigrationChainIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Chạy toàn bộ chuỗi V1→V9 trên Testcontainers PostgreSQL sạch; assert chèn attendance trùng cùng (student, course, date) bị uq_attendance_idempotent từ chối; retry_count vượt 3 bị ck_notifications_retry_cap chặn; discount_percent ngoài 1–100 bị ck_promotions_discount_range chặn; promotion không end_date được chấp nhận như khuyến mãi vĩnh viễn; xác minh information_schema trả về đúng 11 bảng lõi tồn tại sau migrate và không có orphan reference giữa các khóa ngoại.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]:**

<!--START_DDL_MIGRATION-->
```sql
-- Verified chain executed by FullMigrationChainIT (V4 -> V9)
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

CREATE TABLE system_settings (
    setting_key    VARCHAR(100)  NOT NULL,
    setting_value  TEXT          NOT NULL,
    description    VARCHAR(255),
    CONSTRAINT pk_system_settings PRIMARY KEY (setting_key)
);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.8: Kiểm toán đồ thị khóa ngoại toàn cục và ký merge

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/db-migrations/src/main/resources/db/migration/V5__create_attendance_table.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xác minh thứ tự phụ thuộc FK V1→V9 không tạo orphan reference khi migrate tuần tự trên môi trường sạch; xác nhận cổng idempotent UNIQUE đúng ba cột (student_id, course_id, attendance_date) không thừa thiếu cột nào; rà soát CHECK constraint không che khuất lỗi nghiệp vụ cần surface lên tầng ứng dụng; duyệt và ký merge toàn bộ chuỗi migration làm điều kiện mở khóa tầng ứng dụng auth-service ở Ngày 4.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.9: Cập nhật từ điển dữ liệu bảy bảng vận hành

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/data-dictionary-operational-tables.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Bổ sung mô tả cột/ràng buộc của 7 bảng vận hành ENROLLMENTS/ATTENDANCE/STUDENT_CARDS/NOTIFICATIONS/PROMOTIONS/ANNOUNCEMENTS/SYSTEM_SETTINGS; diễn giải vòng đời trạng thái notification PENDING→SENT/RETRYING/FAILED và cơ chế idempotent của attendance kèm ví dụ truy vấn minh họa; cập nhật sơ đồ Mermaid quan hệ USERS ||--o{ ENROLLMENTS, COURSES ||--o{ ENROLLMENTS, USERS ||--o| STUDENT_CARDS và ghi chú ý nghĩa end_date NULL của promotions.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 4:
<!--DAY_HEADER_START-->Triển Khai Endpoint Đăng Ký Người Dùng Hash Bcrypt Cấp JWT Và Bộ Xử Lý Ngoại Lệ Xác Thực Đầu Vào<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.1: DTO đăng ký kèm ràng buộc Bean Validation

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/dto/RegisterRequest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001], [EXC-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Định nghĩa record RegisterRequest với @Email @NotBlank @Size(max=255) cho email, @NotBlank @Pattern(regexp chính sách mạnh: tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ số, một ký tự đặc biệt) cho password, @NotBlank @Size(max=100) cho fullName, @AssertTrue(message yêu cầu đồng ý điều khoản) cho acceptedTerms; gắn message tiếng Anh máy đọc cho từng ràng buộc để GlobalExceptionMapper ánh xạ sang mảng invalidFields đúng từng trường; cấm đặt annotation validation ở tầng controller thay vì DTO để bảo đảm một nguồn chân lý duy nhất.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.2: Dịch vụ đăng ký người dùng hash bcrypt transactional

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/UserRegistrationService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai @Transactional UserRegistrationService: kiểm tra email unique qua repository dùng prepared statement và ném EmailAlreadyExistsException khi trùng; hash BCrypt cost 12 bảo đảm chuỗi hash đúng 60 ký tự khớp cột CHAR(60); persist Users với roleId mặc định STUDENT (id 5) hoặc TEACHER (id 4) khi request mang inviteToken hợp lệ; cập nhật updated_at tự động; trả về thực thể Users đã tạo cho tầng resource phát hành token; mọi truy vấn đi qua tham số hóa chống SQL injection.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.3: Bộ phát hành JWT RS256 và refresh token Redis

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/security/JwtTokenIssuer.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Phát hành access token RS256 hết hạn 900 giây chứa claims sub (userId), role, iss, iat, exp; refresh token opaque UUID có TTL 7 ngày (604800 giây) lưu Redis với key refresh:<userId>:<tokenId> phục vụ xoay vòng và thu hồi tức thời; ký bằng private key nạp từ cấu hình môi trường qua MicroProfile Config, nghiêm cấm hardcode trong mã nguồn; không đưa passwordHash hay PII nhạy cảm vào payload JWT theo khung OWASP; cung cấp hàm verify cho filter OIDC downstream ở Giai đoạn 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.4: REST endpoint POST /api/v1/auth/register

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/resource/AuthResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** JAX-RS resource POST /api/v1/auth/register nhận body RegisterRequest qua @Valid kích hoạt Bean Validation, điều phối UserRegistrationService rồi JwtTokenIssuer; trả 201 kèm TokenResponse (userId, email, fullName, role, accessToken, refreshToken, tokenType=Bearer); ánh xạ ConstraintViolationException sang 400 AUTH_VALIDATION_FAILED và EmailAlreadyExistsException sang 409 EMAIL_ALREADY_EXISTS; endpoint công khai không yêu cầu bearer; ghi log truy cập tuyệt đối không bao gồm password hay hash.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-001]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.5: GlobalExceptionMapper hợp nhất vi phạm xác thực đầu vào

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/exception/GlobalExceptionMapper.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** @Provider ExceptionMapper<ConstraintViolationException> gom từng violation thành bộ {field, rejectedValue, message} bảo toàn thứ tự khai báo DTO, trả 400 với errorCode=AUTH_VALIDATION_FAILED và mảng invalidFields liệt kê từng trường không hợp lệ đúng tiêu chí chấp nhận [EXC-004]; bổ sung mapper cho EmailAlreadyExistsException trả 409 với thông điệp chung chống dò tài khoản; cấm leak stack trace hay chi tiết SQL ra phản hồi; thông điệp lỗi hướng dẫn người dùng chỉnh sửa từng trường trước khi gửi lại biểu mẫu.

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "GlobalExceptionMapper",
  "package": "org.nlh4j.membership_hub.auth.exception",
  "providers": [
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 400,
      "errorCode": "AUTH_VALIDATION_FAILED",
      "bodySchema": {
        "errorCode": "AUTH_VALIDATION_FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "Aggregate every Bean Validation violation into invalidFields preserving DTO declaration order; never expose stack traces or SQL fragments"
    },
    {
      "handles": "org.nlh4j.membership_hub.auth.exception.EmailAlreadyExistsException",
      "httpStatus": 409,
      "errorCode": "EMAIL_ALREADY_EXISTS",
      "bodySchema": {
        "errorCode": "EMAIL_ALREADY_EXISTS",
        "message": "A user with this email already exists"
      },
      "rule": "Return fixed generic message to prevent account enumeration; keep constant response time"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.6: Unit test dịch vụ đăng ký và chính sách mật khẩu

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/UserRegistrationService.java;./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/UserRegistrationServiceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001], [EXC-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** @QuarkusTest: assert hash bcrypt khác plaintext và verifier xác thực thành công với mật khẩu gốc; email trùng sinh EmailAlreadyExistsException ánh xạ 409; mật khẩu thiếu chữ hoa/chữ số/ký tự đặc biệt và email sai định dạng sinh đúng số violation tương ứng từng trường; acceptedTerms=false và fullName vượt 100 ký tự bị chặn; xác minh phản hồi 400 chứa mảng invalidFields đầy đủ đúng schema hợp đồng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.7: Rà soát bảo mật luồng đăng ký theo OWASP

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/resource/AuthResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001], [EXC-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Kiểm chứng BCrypt cost >= 12, thời hạn access 900 giây/refresh 604800 giây khớp hợp đồng; bảo đảm không log password, hash hay token ở bất kỳ tầng nào; thông điệp 409 không dò được sự tồn tại email qua timing attack (thời gian phản hồi ổn định giữa email tồn tại và không tồn tại); rà soát placeholder rate limiting tại gateway cho endpoint public; phê duyệt merge endpoint đăng ký sau khi SonarQube không còn blocker.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 4.8: Đặc tả tham chiếu API đăng ký

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-auth-service-reference.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001], [EXC-004]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Ghi hợp đồng POST /api/v1/auth/register: schema yêu cầu bắt buộc từng trường, phản hồi 201/400/409, bảng mã lỗi AUTH_VALIDATION_FAILED và EMAIL_ALREADY_EXISTS, ví dụ curl kèm payload mẫu; mô tả chính sách mật khẩu (tối thiểu 8 ký tự, chữ hoa, chữ số, ký tự đặc biệt) và cách UI hiển thị danh sách trường không hợp lệ trả về từ mảng invalidFields để người dùng chỉnh sửa trực tiếp.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 5:
<!--DAY_HEADER_START-->Tích Hợp Đăng Nhập Mạng Xã Hội OAuth2 Firebase Google Facebook Kèm Trao Đổi Token An Toàn<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.1: Dịch vụ trao đổi mã OAuth2 upsert người dùng

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/OAuth2LoginService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Nhận authorizationCode và redirectUri từ client, gọi token endpoint của provider tương ứng để exchange access token rồi lấy userinfo; upsert Users theo email trong một @Transaction: email chưa tồn tại thì tạo mới với provider tương ứng và role STUDENT, đã tồn tại thì cập nhật cột provider nếu khác mà không nhân bản dòng; sau commit phát hành JWT phiên qua JwtTokenIssuer; mọi lỗi exchange gói vào OAuth2CodeExchangeFailedException ánh xạ 401; toàn bộ HTTP outbound dùng timeout cấu hình và không log token trung gian.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.2: Adapter nhà cung cấp danh tính Firebase/Google/Facebook

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/oauth/SocialProviderAdapter.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Định nghĩa interface SocialProviderAdapter với phương thức exchange(authorizationCode, redirectUri) trả UserProfile(email, fullName, provider); triển khai ba bean FirebaseTokenVerifier, GoogleIdTokenVerifier, FacebookGraphClient chọn động theo tham số đường dẫn; xác thực chữ ký token, audience/client-id và expiry trước khi chấp nhận danh tính; chuẩn hóa trường họ tên về tối đa 100 ký tự khớp cột users.full_name; ném UnsupportedProviderException cho giá trị provider ngoài whitelist.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.3: REST endpoint POST /api/v1/auth/oauth2/{provider}

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/resource/OAuthResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** POST /api/v1/auth/oauth2/{provider} giới hạn provider IN (firebase, google, facebook), giá trị khác trả 400 OAUTH2_PROVIDER_UNSUPPORTED; trả 200 TokenResponse kèm cờ isNewUser phản ánh việc tạo bản ghi Users mới; exchange thất bại trả 401 OAUTH2_CODE_EXCHANGE_FAILED với thông điệp chung không tiết lộ nguyên nhân chi tiết; endpoint công khai; log chỉ ghi provider và kết quả, tuyệt đối không ghi authorizationCode hay token trung gian.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-002]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-002]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "GlobalExceptionMapper",
  "package": "org.nlh4j.membership_hub.auth.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.auth.oauth.OAuth2CodeExchangeFailedException",
      "httpStatus": 401,
      "errorCode": "OAUTH2_CODE_EXCHANGE_FAILED",
      "bodySchema": {
        "errorCode": "OAUTH2_CODE_EXCHANGE_FAILED",
        "message": "Provider rejected the authorization code"
      },
      "rule": "Generic message only; authorizationCode and intermediate tokens are banned from logs and response bodies"
    },
    {
      "handles": "org.nlh4j.membership_hub.auth.oauth.UnsupportedProviderException",
      "httpStatus": 400,
      "errorCode": "OAUTH2_PROVIDER_UNSUPPORTED",
      "bodySchema": {
        "errorCode": "OAUTH2_PROVIDER_UNSUPPORTED",
        "message": "Provider must be one of: firebase, google, facebook"
      },
      "rule": "Reject unknown path parameter before invoking any provider adapter"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.4: Unit test dịch vụ OAuth2 với mock adapter

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/OAuth2LoginService.java;./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/OAuth2LoginServiceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Mock adapter: mã hợp lệ → upsert và cấp JWT với claims đúng; mã hết hạn/sai chữ ký → OAuth2CodeExchangeFailedException ánh xạ 401; email đã tồn tại với provider khác → cập nhật provider, không nhân bản dòng Users; xác minh isNewUser=true chỉ lần đầu tạo bản ghi; kiểm tra transaction rollback khi userinfo thiếu email bắt buộc và không để lại bản ghi mồ côi.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.5: Integration test luồng OAuth2 đầu-cuối với stub provider

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/OAuth2FlowIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** @QuarkusIntegrationTest với stub provider server (WireMock) giả lập token endpoint Google/Firebase/Facebook: lần đầu gọi trả isNewUser=true và dòng Users mới xuất hiện trong PostgreSQL Testcontainers; lần sau cùng email trả isNewUser=false; giải mã access token xác nhận claims role=STUDENT và exp−iat=900s; xác minh refresh token được lưu Redis với TTL 604800 giây và có thể thu hồi.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.6: Rà soát an ninh trao đổi token chống CSRF

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/OAuth2LoginService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xác thực state/nonce chống CSRF trên luồng popup→callback; kiểm tra audience/client-id khớp cấu hình môi trường và clock skew cho phép ±60 giây; bảo đảm không ghi log authorizationCode, access token trung gian hay refresh token; rà soát whitelist redirectUri chặn open redirect; phê duyệt merge luồng OAuth2 sau khi cổng phân tích tĩnh xanh.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 5.7: Bổ sung chương OAuth2 vào tham chiếu API

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-auth-service-reference.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cập nhật chương OAuth2: bảng ba provider firebase/google/facebook, schema yêu cầu authorizationCode/redirectUri, phản hồi 200 kèm cờ isNewUser, mã lỗi 401 OAUTH2_CODE_EXCHANGE_FAILED và 400 OAUTH2_PROVIDER_UNSUPPORTED; bổ sung sơ đồ sequence popup→callback→exchange→JWT phát hành bằng Mermaid và ghi chú chính sách bảo mật state/nonce.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 6:
<!--DAY_HEADER_START-->Xây Dựng Phân Quyền Vai Trò Kèm Audit Log Append-Only Và Đóng Gói Bàn Giao Giai Đoạn<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 6.1: Dịch vụ gán/thay đổi vai trò vô hiệu hóa cache phiên

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/RoleAssignmentService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cập nhật users.role_id trong @Transaction sau khi xác minh caller mang claim role=SYSTEM_ADMIN; vô hiệu hóa cache phiên Redis của target user (key sessions:<userId>) để ma trận quyền áp dụng tức thời không cần đăng nhập lại; ném RoleAssignmentForbiddenException khi thiếu quyền và UserNotFoundException khi targetUserId không tồn tại; ghi nhận previousRoleId/newRoleId phục vụ phản hồi và audit; validate roleId trong khoảng 1–5 trước khi mutate.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 6.2: Bộ ghi audit log append-only thay đổi vai trò

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/audit/AuditLogRecorder.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Ghi append-only mỗi thay đổi vai trò gồm actorUserId, targetUserId, oldRoleId, newRoleId, action=USER_ROLE_CHANGED, reason tùy chọn và timestamp UTC; sử dụng repository audit riêng không expose update/delete ở bất kỳ tầng nào; bảo đảm ghi audit trong cùng transaction với thay đổi role để không xảy ra trạng thái lệch; định dạng dòng log chuẩn hóa phục vụ sink Cloud Logging retention 1 năm ở Giai đoạn 5.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 6.3: REST endpoint PUT /api/v1/admin/users/{userId}/role

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/resource/AdminRoleResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** PUT /api/v1/admin/users/{userId}/role với @RolesAllowed("SYSTEM_ADMIN"); nhận RoleAssignmentRequest(roleId, reason optional); trả 200 kèm userId, previousRoleId, newRoleId, permissionsAppliedAt, auditLogId; 403 ROLE_ASSIGNMENT_FORBIDDEN khi caller thiếu quyền, 404 USER_NOT_FOUND khi userId không tồn tại, 400 khi roleId ngoài khoảng hợp lệ; bearer JWT bắt buộc trên toàn endpoint.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-003]:**

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-003]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "GlobalExceptionMapper",
  "package": "org.nlh4j.membership_hub.auth.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.auth.service.RoleAssignmentForbiddenException",
      "httpStatus": 403,
      "errorCode": "ROLE_ASSIGNMENT_FORBIDDEN",
      "bodySchema": {
        "errorCode": "ROLE_ASSIGNMENT_FORBIDDEN",
        "message": "Caller lacks SYSTEM_ADMIN privilege"
      },
      "rule": "Enforced by @RolesAllowed at resource layer and re-checked inside service transaction; every denial writes an audit entry"
    },
    {
      "handles": "org.nlh4j.membership_hub.auth.exception.UserNotFoundException",
      "httpStatus": 404,
      "errorCode": "USER_NOT_FOUND",
      "bodySchema": {
        "errorCode": "USER_NOT_FOUND",
        "message": "Target user does not exist"
      },
      "rule": "Validate targetUserId existence before mutating role_id; no partial updates"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 6.4: Unit test dịch vụ phân quyền và dòng audit

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/RoleAssignmentService.java;./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/RoleAssignmentServiceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Assert gán hợp lệ cập nhật role_id và trả previousRoleId/newRoleId đúng; caller thường (STUDENT/TEACHER/MANAGER/CENTER_ADMIN) bị chặn RoleAssignmentForbiddenException ánh xạ 403; roleId không tồn tại ném lỗi nghiệp vụ 400; mỗi thao tác phát sinh đúng một dòng audit append-only với action=USER_ROLE_CHANGED và timestamp tăng dần; cache phiên target user bị invalidate sau đổi vai trò.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 6.5: Profile E2E vòng lifecycle xác thực đầu-cuối

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/org/nlh4j/membership_hub/auth/AuthLifecycleE2EIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Kịch bản E2E đầu-cuối trên PostgreSQL Testcontainers: đăng ký local → đăng nhập OAuth2 stub → admin đổi vai trò STUDENT→CENTER_ADMIN → gọi lại API bằng token mới xác nhận quyền có hiệu lực ngay không cần đăng nhập lại; đo latency trung bình register qua 100 lần gọi giữ dưới 200 ms làm gate hiệu năng đối chiếu [NFR-001]; xác minh audit log ghi đủ ba sự kiện với timestamp tăng dần và không có bản ghi mồ côi sau rollback.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 6.6: Rà soát tổng kết chất lượng và ký duyệt bàn giao

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/resource/AdminRoleResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-003], [ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Duyệt toàn bộ diff giai đoạn: descriptor build gốc và hai module con, chuỗi 9 migration, bộ endpoint auth (register/OAuth2/role); đối chiếu 100% tag traceability [ARC-000], [DAT-001] đến [DAT-011], [REQ-001], [REQ-002], [REQ-003], [EXC-004] với nhật ký ngày; chuẩn coding Quarkus và OWASP Top 10 không còn finding mức cao; ký duyệt bàn giao sang Giai đoạn 2 kèm danh sách nợ kỹ thuật được chấp nhận.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 6.7: Hoàn thiện blueprint và tham chiếu API giai đoạn 1

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/architecture-blueprint.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000], [REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cập nhật trạng thái bàn giao: 11 bảng lõi đã migrate qua chuỗi V1–V9, auth-service hoàn chỉnh đăng ký/OAuth2/phân quyền kèm audit log append-only; liên kết chéo data dictionary core/operational và api-auth-service-reference.md; liệt kê hạng mục mở cho Giai đoạn 2 (center-service, course-service, RBAC gateway, công bố hợp đồng OpenAPI); bổ sung sơ đồ topology cập nhật phản chiếu đúng cấu trúc module đã build.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->