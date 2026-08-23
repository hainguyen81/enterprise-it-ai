# Giai đoạn 3: <!--PHASE_NAME_START-->Dịch Vụ Ghi Danh, Điểm Danh QR Và Thẻ Hội Viên Kỹ Thuật Số<!--PHASE_NAME_END-->

## 📊 Kiểm soát Tài liệu

| Hạng mục | Chi tiết |
| :--- | :--- |
| **ID Bản thiết kế** | ARCH-20260823050512 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Dịch Vụ Ghi Danh, Điểm Danh QR Và Thẻ Hội Viên Kỹ Thuật Số<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 3 bàn giao chuỗi nghiệp vụ học viên end-to-end trên ba microservices mới của nền tảng membership-hub. enrollment-service cung cấp duyệt khóa học loại trừ mọi khóa đã có bản ghi ghi danh kèm số chỗ còn trống [REQ-010] và đăng ký khóa học trong một transaction nguyên tử tự cấp tài khoản vai trò 'Student' khi thiếu, đồng thời phát sự kiện enrollment.created tới notification-service để đẩy thông báo tới mobile app học viên và nhóm Zalo của trung tâm [REQ-011]. attendance-service tiếp nhận payload quét QR (studentId, courseId, clientTimestamp) tại POST /api/v1/attendance/scan với chính sách phát lại FIFO các scan tồn đọng sau khi mất kết nối mạng [REQ-012], [EXC-001], cùng ràng buộc idempotent (studentId, courseId, attendanceDate) trả success kèm cờ duplicate cho mọi lần quét trùng [REQ-013], [EXC-002]. card-service suy ra totalValidityDays, daysUsed, daysRemaining từ thực thể StudentCard để hiển thị thẻ hội viên kỹ thuật số [REQ-014] và thực thi gia hạn theo kỳ 30 ngày ngay sau khi payment service xác nhận sự kiện payment.confirmed thành công [REQ-015]. Chất lượng được bảo chứng bởi bộ JUnit unit test, integration test trên Testcontainers PostgreSQL/Kafka và bộ đặc tả API cập nhật cho cả ba dịch vụ.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/23 05:05:12 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 1. Phạm vi Vận hành Giai đoạn & Mục tiêu

Giai đoạn 3 bàn giao chuỗi nghiệp vụ học viên end-to-end của nền tảng membership-hub trên ba microservices mới, bao phủ trọn vẹn Task 12, Task 13, Task 14, Task 15, Task 16 và Task 17 của Master Backlog.

Thứ nhất, enrollment-service vận hành vòng đời ghi danh: endpoint GET /api/v1/enrollments/browse trả danh sách khóa học loại trừ hoàn toàn mọi khóa đã có bản ghi Enrollment của studentId kèm availableSeats = maxStudents − số chỗ đã chiếm, sắp xếp theo startDate và phân trang với index idx_enrollments_student_lookup bảo đảm độ trễ đọc sub-second [REQ-010]; endpoint POST /api/v1/enrollments/register chạy trong một transaction nguyên tử — khóa bi quan chống race condition giành chỗ cuối cùng, tự cấp tài khoản vai trò 'Student' qua auth-service khi studentId chưa tồn tại, ghi hàng enrollment_outbox trong cùng transaction và phát sự kiện enrollment.created tới notification-service để đẩy push notification tới mobile app học viên cùng đăng tin nhóm Zalo của trung tâm; khóa đầy trả 409 ENR-409-CAPACITY với rollback sạch không để lại dữ liệu mồ côi [REQ-011].

Thứ hai, attendance-service tiếp nhận quét QR: POST /api/v1/attendance/scan nhận {studentId, courseId, clientTimestamp}, xác thực quan hệ student–course qua bản ghi Enrollments, suy ra attendanceDate từ clientTimestamp theo UTC và ghi bản ghi Attendance [REQ-012]; ứng dụng di động hàng đợi cục bộ các scan khi mất mạng và phát lại sau reconnect, attendance-service tiếp nhận bó tồn đọng xử lý FIFO theo clientTimestamp gốc mà không phạt request đến trễ [EXC-001]; ràng buộc unique (student_id, course_id, attendance_date) đóng vai trò cổng idempotent duy nhất ở tầng lưu trữ — mọi lần quét trùng cùng ngày trả 200 với status='DUPLICATE', duplicate=true, mã nghiệp vụ ATT-DUP-001 ('already recorded') mà không phát sinh thêm bản ghi [REQ-013], [EXC-002].

Thứ ba, card-service quản lý thẻ hội viên kỹ thuật số: GET /api/v1/cards/me suy ra totalValidityDays, daysUsed (kẹp biên [0, validityDays]) và daysRemaining từ thực thể StudentCard theo phép toán ngày thống nhất UTC [REQ-014]; POST /api/v1/cards/renew chỉ mở rộng validityDays theo kỳ chọn (ví dụ 30 ngày) sau khi PaymentConfirmationConsumer tiêu thụ sự kiện payment.confirmed với khóa idempotent theo paymentReferenceId chống cộng dồn ngày hiệu lực, kèm notification xác nhận gia hạn tới học viên; payment chưa xác nhận trả 409 PAYMENT-PENDING giữ nguyên dữ liệu thẻ [REQ-015].

Chất lượng được bảo chứng bởi JUnit unit test, integration test trên Testcontainers PostgreSQL/Kafka đo độ trễ dưới 200 ms đối chiếu [NFR-001]; tài liệu được đóng gói qua ba tham chiếu API enrollment/attendance/card cập nhật đầy đủ hợp đồng, mã lỗi và sơ đồ sự kiện.

## 2. Phạm vi Kỹ thuật Được phép & Ranh giới Thư mục (Tệp, đường dẫn và Endpoint)

* **Ma trận thư mục Backend được phép:**
    * ./sources/backend/enrollment-service/pom.xml [ARC-000]
    * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/*.java
    * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/dto/*.java
    * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/event/*.java
    * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/exception/*.java
    * ./sources/backend/enrollment-service/src/main/resources/db/migration/V3__enrollment_browse_outbox.sql [REQ-010], [REQ-011]
    * ./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/*.java
    * ./sources/backend/attendance-service/pom.xml [ARC-000]
    * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/*.java
    * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/dto/*.java
    * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/retry/*.java
    * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/exception/*.java
    * ./sources/backend/attendance-service/src/main/resources/db/migration/V4__attendance_unique_idempotency.sql [REQ-013], [EXC-002]
    * ./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/*.java
    * ./sources/backend/card-service/pom.xml [ARC-000]
    * ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/*.java
    * ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/dto/*.java
    * ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/exception/*.java
    * ./sources/backend/card-service/src/main/resources/db/migration/V5__card_validity_support.sql [REQ-014]
    * ./sources/backend/card-service/src/test/java/org/nlh4j/membership_hub/card/*.java
* **Ma trận thư mục Tài liệu được phép:**
    * ./sources/docs/api-enrollment-service.md [REQ-010], [REQ-011]
    * ./sources/docs/api-attendance-service.md [REQ-012], [REQ-013], [EXC-001], [EXC-002]
    * ./sources/docs/api-card-service.md [REQ-014], [REQ-015]
* **Mẫu định tuyến Endpoint được phép trong giai đoạn:**
    * GET /api/v1/enrollments/browse — BEARER JWT, role=STUDENT [REQ-010]
    * POST /api/v1/enrollments/register — BEARER JWT tùy chọn, cho phép kịch bản học viên chưa có tài khoản tự cấp vai trò 'Student' [REQ-011]
    * POST /api/v1/attendance/scan — BEARER JWT, role=STUDENT [REQ-012], [REQ-013]
    * GET /api/v1/cards/me — BEARER JWT, role=STUDENT [REQ-014]
    * POST /api/v1/cards/renew — BEARER JWT, role=STUDENT [REQ-015]
* **Mẫu định tuyến Sự kiện được phép trong giai đoạn:**
    * Publish: topic `enrollment.created` — producer enrollment-service, consumer notification-service, delivery at-least-once, deduplicate theo eventId [REQ-011]
    * Consume: topic `payment.confirmed` — producer payment-service, consumer card-service, delivery at-least-once, khóa idempotent theo paymentReferenceId, dead-letter topic `payment.confirmed.dlq` [REQ-015]
* **Ranh giới cấm xâm phạm:** mọi module và endpoint thuộc notification-service, promotion-service, chatbot-service, reporting-service cùng toàn bộ cây ./sources/infra/ và ./sources/frontend/ được dành riêng cho các giai đoạn 4 đến 5; Giai đoạn 3 nghiêm cấm phát sinh tệp ngoài ma trận trên và cấm tái tạo bất kỳ tệp nào đã tồn tại từ Giai đoạn 1 và Giai đoạn 2 (descriptor cha, auth-service, db-migrations chuỗi V1–V9, center-service, course-service, api-gateway, workspace frontend).

* **INVARIANT KHUNG NỀN TẢNG BẮT BUỘC (PLATFORM SKELETON MANIFEST INVARIANTS)**:
    * Descriptor hạ tầng repository gốc `./sources/backend/pom.xml` và workspace frontend `./sources/frontend/package.json` cùng `./sources/frontend/tsconfig.json` đã được neo vĩnh viễn tại Giai đoạn 1 - NGÀY 1 theo token kiến trúc [ARC-000]; Giai đoạn 3 nghiêm cấm tái tạo hoặc ghi đè các descriptor nền móng này.
    * Với ba module dịch vụ mới gia nhập chuỗi microservices ở giai đoạn này (enrollment-service, attendance-service, card-service), bắt buộc đăng ký descriptor module con độc lập `./sources/backend/<service-name>/pom.xml` kế thừa parent membership-hub-backend TRƯỚC khi phát hành bất kỳ thành phần mã nguồn ứng dụng nào của module đó; toàn bộ descriptor scaffolding sinh ra phải ánh xạ nghiêm ngặt vào token theo dõi kiến trúc [ARC-000].

## 3. Chỉ đạo Chức năng Sub-Agent Chuyên trách

Theo ma trận phân công của Giai đoạn 3, các Sub-Agent được kích hoạt gồm Coder, Tester, Reviewer và Doc; Docker, GCP và GKE được dự phòng và chỉ kích hoạt từ Giai đoạn 5.

* **Coder**: Đóng vai trò Lập trình viên Ứng dụng Cấp cao/Principal. Chịu trách nhiệm hiện thực mã nguồn ứng dụng thuần túy: descriptor Maven module con cho enrollment-service, attendance-service và card-service; thực thể/repository/service/resource của ba dịch vụ nghiệp vụ; bộ xuất bản sự kiện transactional outbox; chính sách replay ngoại tuyến FIFO; consumer xác nhận thanh toán; chuỗi migration V3/V4/V5. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng DevOps.
* **Tester**: Đóng vai trò Trưởng QC/QA Principal. Chuyên về kỹ nghệ bộ kiểm thử, xác nhận và cổng chất lượng. Chịu trách nhiệm sinh JUnit unit test, integration test trên Testcontainers PostgreSQL và Kafka, kịch bản đo độ trễ đối chiếu [NFR-001]. Bị cấm sửa mã production. Khi phạm vi kiểm thử mang tính tích hợp tổng thể hoặc E2E không cô lập được một tệp production đơn lẻ, bắt buộc dùng định dạng cặp semicolon với token `INTEGRATION_SCOPE` đứng đầu (ví dụ: `INTEGRATION_SCOPE;./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentRegistrationTransactionIT.java`).
* **Doc**: Đóng vai trò Nhà văn Kỹ thuật Principal và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên biên soạn tài liệu đặc tả kỹ thuật, tham chiếu API, sơ đồ sự kiện và catalog hợp đồng phù hợp topology dự án. Mọi tệp tài liệu phải là đường dẫn tệp tường minh đuôi `.md` nằm trong kho lưu trữ tập trung `./sources/docs/`. Theo luật định giai đoạn, Doc phải được phân công tối thiểu một nhiệm vụ nền móng ngay NGÀY 1 để khởi tạo khung tài liệu markdown tham chiếu API enrollment-service tương thích stack Java/Quarkus/PostgreSQL của ngữ cảnh này.
* **Reviewer**: Chịu trách nhiệm xác minh biên dịch, cổng phân tích tĩnh và vá phòng thủ. Chuyên kiểm toán chất lượng mã, phân tích race condition và tính idempotent, khắc phục lỗ hổng bảo mật OWASP Top 10 (đặc biệt kiểm soát truy cập hỏng A01 và injection A03), gỡ blocker SonarQube trước khi merge; ký duyệt điều kiện mở khóa giữa các ngày làm việc.
* **Docker**: Chuyên container hóa, kỹ nghệ Dockerfile multi-stage, tối ưu dung lượng image và đẩy image đã kiểm chứng lên registry. Trong Giai đoạn 3 chưa được phân công nhiệm vụ cụ thể.
* **GCP**: Chuyên tự động hóa trên Google Cloud Platform: build/push image lên Artifact Registry và điều phối môi trường container trên Cloud Run. Trong Giai đoạn 3 chưa được phân công nhiệm vụ cụ thể.
* **GKE**: Chuyên điều phối container production trong Google Kubernetes Engine: manifest deployment, routing control, cấu hình HPA, Helm chart và triển khai workload microservices. Trong Giai đoạn 3 chưa được phân công nhiệm vụ cụ thể.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)

* 100% thẻ truy vết của giai đoạn ([REQ-010], [REQ-011], [REQ-012], [EXC-001], [REQ-013], [EXC-002], [REQ-014], [REQ-015]) được ánh xạ tường minh vào nhật ký ngày qua container `<!--START_TAGS-->` không gaps, không trùng lặp sai ngữ cảnh.
* `mvn -q verify` sạch trên ba descriptor module con mới (enrollment-service, attendance-service, card-service); cây Maven không xung đột phiên bản với parent membership-hub-backend và Quarkus BOM 3.15.x.
* GET /api/v1/enrollments/browse loại trừ đúng mọi khóa đã có bản ghi Enrollment của studentId, trả availableSeats chính xác gồm biên capacity=0, kế hoạch truy vấn sử dụng idx_enrollments_student_lookup, độ trễ đọc sub-second ở 10.000 dòng dữ liệu mẫu [REQ-010].
* POST /api/v1/enrollments/register: tài khoản 'Student' tự cấp + bản ghi Enrollments + hàng enrollment_outbox tạo trong cùng một transaction; khóa đầy trả 409 ENR-409-CAPACITY rollback sạch; hai request đồng thời giành chỗ cuối cùng chỉ đúng một thành công nhờ khóa bi quan; sự kiện enrollment.created phát sau commit với chế độ at-least-once và deduplicate theo eventId [REQ-011].
* POST /api/v1/attendance/scan: quan hệ student–course không tồn tại trả 409 ATT-VAL-409; attendanceDate suy đúng từ clientTimestamp kể cả múi giờ khác UTC; bó scan ngoại tuyến phát lại sau reconnect xử lý FIFO theo clientTimestamp gốc không phạt request đến trễ [REQ-012], [EXC-001].
* Tính idempotent: hai lần quét cùng student/course/ngày tạo đúng một hàng Attendance; request trùng trả 200 duplicate=true ATT-DUP-001 'already recorded' không phát sinh bản ghi mới; không tồn tại mẫu check-then-insert TOCTOU, cổng idempotent dựa hoàn toàn vào ràng buộc unique tầng DB [REQ-013], [EXC-002].
* GET /api/v1/cards/me: daysUsed kẹp biên [0, validityDays], daysRemaining không bao giờ âm, phép toán ngày thống nhất UTC; thẻ chưa cấp trả 404 CARD-NOT-FOUND [REQ-014].
* POST /api/v1/cards/renew: validityDays chỉ mở rộng sau khi payment.confirmed được xác nhận; paymentReferenceId trùng lặp không cộng dồn ngày hiệu lực; payment chưa xác nhận trả 409 PAYMENT-PENDING giữ nguyên dữ liệu thẻ; notification xác nhận gia hạn được điều phối thành công [REQ-015].
* Độ bao phủ kiểm thử tự động ≥ 85% trên cả ba module; latency trung bình browse/scan/cards-me ≤ 200 ms trong profile đo hiệu năng đối chiếu [NFR-001].
* Tuân thủ OWASP Top 10: toàn bộ truy vấn đi qua prepared statement tham số hóa; sắp xếp/lọc động đi qua whitelist cứng tên cột; không leak stack trace hay chi tiết SQL ra phản hồi lỗi; studentId trên cards/me suy từ claim sub của JWT chống leo thang dữ liệu chéo tài khoản.
* Ba tài liệu ./sources/docs/ hoàn chỉnh, liên kết chéo nhất quán với schema Giai đoạn 1 và hợp đồng API thực tế.
* Zero blocker SonarQube; mọi merge thực hiện qua pull request squash trên nhánh `features/development-phase-3-day-Y` theo quy trình phân nhánh hàng ngày.

## 5. Nhật ký Thực thi Kiến trúc Theo Ngày

### 🌤️ NGÀY 1:
<!--DAY_HEADER_START-->Khởi Tạo Enrollment Service Với Bộ Lọc Duyệt Khóa Học, Giao Dịch Ghi Danh Nguyên Tử Và Outbox Thông Báo<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.1: Sinh descriptor module con enrollment-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/enrollment-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module enrollment-service kế thừa parent membership-hub-backend mà không tái khai báo phiên bản dependency; đăng ký module này vào danh sách `<modules>` của descriptor cha theo thứ tự phụ thuộc sau api-gateway; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator, quarkus-flyway và quarkus-smallrye-reactive-messaging-kafka phục vụ xuất bản sự kiện enrollment.created qua transactional outbox; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=enrollment-service phục vụ đóng gói image ở Giai đoạn 5; cấu hình quarkus.flyway.locations trỏ tới classpath:db/migration của chính module để chuỗi migration V3 chạy trong ngữ cảnh lịch sử Flyway riêng biệt, tránh xung đột với chuỗi V1–V9 toàn cục của db-migrations; bổ sung dependency test scope junit-jupiter, rest-assured, testcontainers-postgresql và testcontainers-kafka làm nền cho suite kiểm thử của Tester.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.2: Repository duyệt khóa học loại trừ bản ghi ghi danh và migration outbox

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentRepository.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai EnrollmentRepository dựa trên PanacheRepository với truy vấn duyệt khóa học dùng LEFT JOIN enrollments trên điều kiện student_id = :studentId để loại trừ hoàn toàn mọi khóa đã có bản ghi ghi danh của học viên [REQ-010]; tính availableSeats = maxStudents − COUNT(enrollments) và chỉ trả về các khóa còn chỗ trống lớn hơn 0; sắp xếp kết quả theo start_date tăng dần với phân trang page/size mặc định 20; bổ sung record DTO CourseAvailabilityDto trong gói dto với các trường courseId, title, startDate, endDate, teacherName, maxStudents, availableSeats phục vụ serialization JSON thống nhất; chạy migration V3__enrollment_browse_outbox.sql tạo composite index idx_enrollments_student_lookup (student_id, course_id) và idx_courses_schedule_window (start_date, end_date, teacher_id) cùng bảng enrollment_outbox phục vụ mẫu transactional outbox; cung cấp phương thức đếm tổng số dòng phục vụ totalPages; nghiêm cấm nối chuỗi đầu vào người dùng vào câu lệnh SQL/JPQL native, mọi tham số đi qua positional parameter `?1` hoặc named parameter `:param` chống SQL injection.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [REQ-010], [REQ-011]:**

<!--START_DDL_MIGRATION-->
```sql
-- V3__enrollment_browse_outbox.sql (enrollment-service)
CREATE INDEX idx_enrollments_student_lookup
    ON enrollments (student_id, course_id);

CREATE INDEX idx_courses_schedule_window
    ON courses (start_date, end_date, teacher_id);

CREATE TABLE enrollment_outbox (
    outbox_id uuid PRIMARY KEY,
    aggregate_id uuid NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    payload TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP NULL,
    CONSTRAINT chk_enrollment_outbox_event_type
        CHECK (event_type IN ('ENROLLMENT_CREATED'))
);

CREATE INDEX idx_enrollment_outbox_pending
    ON enrollment_outbox (published_at, outbox_id);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.3: Endpoint REST duyệt khóa học GET /api/v1/enrollments/browse

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentBrowseResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng EnrollmentBrowseResource exposing GET /api/v1/enrollments/browse với tham số studentId bắt buộc kiểu UUID, page mặc định 0 và size mặc định 20 chặn trần 100 chống abuse; yêu cầu bearer JWT hợp lệ cho vai trò STUDENT, ủy quyền chi tiết do RoleAuthorizationFilter tại api-gateway thực thi theo ma trận RBAC; trả payload chuẩn gồm mảng courses (CourseAvailabilityDto), totalElements và page hiện hành; áp dụng annotation OpenAPI @Operation/@ApiResponse phục vụ công bố hợp đồng; tham số sắp xếp đi qua whitelist cứng (startDate, title — ASC/DESC) chặn mọi giá trị ngoài whitelist bằng HTTP 400 chống SQL injection; ghi log truy cập kèm userId và timestamp phục vụ audit theo chuẩn [NFR-006] mà không ghi bearer token hay PII nhạy cảm.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-010]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "/api/v1/enrollments/browse",
  "method": "GET",
  "auth": "bearer JWT, role=STUDENT",
  "queryParams": {
    "studentId": "uuid (required)",
    "page": "int (default 0)",
    "size": "int (default 20, cap 100)"
  },
  "response_200": {
    "courses": [
      {
        "courseId": "uuid",
        "title": "string",
        "startDate": "YYYY-MM-DD",
        "endDate": "YYYY-MM-DD",
        "teacherName": "string",
        "maxStudents": 30,
        "availableSeats": 12
      }
    ],
    "totalElements": 42,
    "page": 0
  },
  "error_400": { "code": "SORT_FIELD_NOT_ALLOWED" }
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.4: Service đăng ký ghi danh giao dịch nguyên tử với khóa bi quan

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentRegistrationResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cài đặt POST /api/v1/enrollments/register chạy trong đúng một @Transactional: khóa bi quan SELECT ... FOR UPDATE trên dòng courses tương ứng để chặn race condition khi hai request đồng thời giành chỗ cuối cùng; kiểm tra capacity còn trống rồi chèn bản ghi Enrollments với ràng buộc unique (student_id, course_id) làm lớp phòng vệ thứ hai; nếu studentId null thì gọi nội bộ auth-service tự động cấp tài khoản vai trò 'Student' từ fullName/email trước khi ghi danh và đặt cờ autoCreatedAccount=true [REQ-011]; ghi hàng enrollment_outbox trong cùng transaction phục vụ xuất bản sự kiện; rollback toàn bộ khi bất kỳ bước nào thất bại không để lại dữ liệu mồ côi; trả 201 kèm enrollmentId/studentId/courseId/enrollmentDate/notificationTargets; trả 409 ENR-409-CAPACITY khi khóa đã đầy và 409 ENR-409-DUPLICATE khi cặp student–course đã tồn tại; validate courseId tồn tại trả 404 COURSE_NOT_FOUND khi thiếu; validate đầu vào ở tầng DTO với danh sách từng trường không hợp lệ khi vi phạm.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-011]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "/api/v1/enrollments/register",
  "method": "POST",
  "request": {
    "studentId": "uuid | null",
    "fullName": "string (required when studentId is null)",
    "email": "string (required when studentId is null)",
    "courseId": "uuid (required)"
  },
  "response_201": {
    "enrollmentId": "uuid",
    "studentId": "uuid",
    "courseId": "uuid",
    "enrollmentDate": "YYYY-MM-DDTHH:mm:ssZ",
    "autoCreatedAccount": true,
    "notificationTargets": ["MOBILE_PUSH", "ZALO_GROUP"]
  },
  "error_409_capacity": {
    "errorCode": "ENR-409-CAPACITY",
    "message": "Course has reached maxStudents capacity"
  },
  "error_409_duplicate": {
    "errorCode": "ENR-409-DUPLICATE",
    "message": "Student already enrolled in this course"
  },
  "error_404": { "code": "COURSE_NOT_FOUND" }
}
```
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-011]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "EnrollmentExceptionMapper",
  "package": "org.nlh4j.membership_hub.enrollment.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.enrollment.exception.CourseCapacityExceededException",
      "httpStatus": 409,
      "errorCode": "ENR-409-CAPACITY",
      "bodySchema": {
        "errorCode": "ENR-409-CAPACITY",
        "message": "Course has reached maxStudents capacity",
        "courseId": "uuid"
      },
      "rule": "Pessimistic lock SELECT FOR UPDATE on courses row before capacity check; rollback cleanly without orphan records"
    },
    {
      "handles": "org.nlh4j.membership_hub.enrollment.exception.DuplicateEnrollmentException",
      "httpStatus": 409,
      "errorCode": "ENR-409-DUPLICATE",
      "bodySchema": {
        "errorCode": "ENR-409-DUPLICATE",
        "message": "Student already enrolled in this course"
      },
      "rule": "Unique constraint (student_id, course_id) acts as second defensive layer against check-then-insert races"
    },
    {
      "handles": "org.nlh4j.membership_hub.enrollment.exception.CourseNotFoundException",
      "httpStatus": 404,
      "errorCode": "COURSE_NOT_FOUND",
      "bodySchema": { "errorCode": "COURSE_NOT_FOUND", "message": "Course does not exist" },
      "rule": "Validate courseId existence before mutating; no partial mutations"
    },
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 400,
      "errorCode": "ENR-VALIDATION-FAILED",
      "bodySchema": {
        "errorCode": "ENR-VALIDATION-FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "Aggregate every Bean Validation violation into invalidFields preserving DTO declaration order; never expose stack traces or SQL fragments"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.5: Xuất bản sự kiện thông báo ghi danh qua transactional outbox

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/event/EnrollmentNotificationPublisher.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cài đặt mẫu transactional outbox: worker poll định kỳ quét các hàng enrollment_outbox có published_at IS NULL theo thứ tự created_at tăng dần tận dụng index idx_enrollment_outbox_pending; đẩy sự kiện vào topic enrollment.created với payload {eventId, enrollmentId, studentId, courseId, centerZaloGroup, occurredAt} qua SmallRye Reactive Messaging với serialization JSON thống nhất mà notification-service sẽ tiêu thụ ở Giai đoạn 4; bảo đảm chế độ at-least-once, eventId sinh ổn định theo cặp (enrollmentId, thao tác) để phát lặp không tạo thông báo nhân bản; partition key theo courseId bảo đảm thứ tự xử lý trong phạm vi từng khóa học; cập nhật published_at sau khi điều phối thành công và giữ hàng pending khi broker lỗi tạm thời; không đưa PII nhạy cảm ngoài studentId/courseId vào payload sự kiện; ghi audit log mỗi lần phát sự kiện kèm eventId phục vụ truy vết.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-011]:**

<!--START_API_CONTRACT-->
```json
{
  "topic": "enrollment.created",
  "deliveryMode": "at-least-once (transactional outbox)",
  "payload": {
    "eventId": "uuid",
    "enrollmentId": "uuid",
    "studentId": "uuid",
    "courseId": "uuid",
    "centerZaloGroup": "string",
    "occurredAt": "YYYY-MM-DDTHH:mm:ssZ"
  },
  "partitionKey": "courseId",
  "consumer": "notification-service"
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.6: Unit test bộ lọc duyệt khóa học

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentBrowseResource.java;./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentBrowseResourceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-010]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest bao phủ bộ lọc duyệt khóa học [REQ-010]: seed nhiều khóa học và bản ghi ghi danh mẫu rồi xác minh phản hồi loại trừ đúng mọi khóa đã có Enrollment của studentId; availableSeats tính chính sát theo maxStudents bao gồm biên capacity=0 (khóa đầy bị loại khỏi danh sách); xác minh phân trang page/size, thứ tự startDate tăng dần và cấu trúc CourseAvailabilityDto trả về đúng kiểu ISO-8601; tham số sort ngoài whitelist trả 400 SORT_FIELD_NOT_ALLOWED; caller chưa mang bearer JWT bị chặn 401; đo latency trung bình GET /api/v1/enrollments/browse giữ dưới 200 ms đối chiếu [NFR-001].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.7: Kiểm thử tích hợp giao dịch đăng ký khóa học

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentRegistrationTransactionIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khởi chạy @QuarkusIntegrationTest với PostgreSQL Testcontainers và Kafka Testcontainers; xác minh kịch bản học viên mới: tài khoản vai trò 'Student' tự cấp + bản ghi Enrollments + hàng enrollment_outbox được tạo trong cùng một transaction [REQ-011]; kịch bản khóa đầy trả 409 ENR-409-CAPACITY và rollback sạch không để lại dữ liệu mồ côi; kịch bản ghi danh trùng cặp student–course trả 409 ENR-409-DUPLICATE nhờ ràng buộc unique; mô phỏng hai request đồng thời giành chỗ cuối cùng xác minh chỉ đúng một request thành công nhờ khóa bi quan SELECT FOR UPDATE; xác minh sự kiện enrollment.created được đẩy ra broker sau commit với payload đầy đủ và consumer deduplicate theo eventId khi phát lặp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.8: Rà soát chất lượng và chiến lược tối ưu enrollment-service

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Phân tích race condition khi hai request đăng ký đồng thời giành chỗ cuối cùng của khóa, xác nhận khóa bi quan SELECT ... FOR UPDATE đã áp dụng đúng và ràng buộc unique (student_id, course_id) làm lớp phòng vệ thứ hai; rà soát chống N+1 query trong luồng duyệt khóa bằng fetch join hoặc batch loading [REQ-010]; chuẩn hóa DTO và bảo đảm mọi nhánh lỗi trả ProblemDetail RFC 7807 không leak stack trace hay chi tiết SQL [REQ-011]; kiểm soát truy cập hỏng OWASP A01: xác minh endpoint register không cho phép caller gán vai trò khác STUDENT khi tự cấp tài khoản; đối chiếu OWASP A03 injection: xác minh không tồn tại đường nối chuỗi trong repository; lập danh sách remediation ưu tiên kèm chủ sở hữu fix và chốt điều kiện mở khóa Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.9: Khởi tạo khung tài liệu tham chiếu API enrollment-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-enrollment-service.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn khung tài liệu tham chiếu API enrollment-service: bảng endpoint GET /api/v1/enrollments/browse và POST /api/v1/enrollments/register kèm schema request/response đầy đủ, tham số phân trang, mã lỗi 409 ENR-409-CAPACITY, 409 ENR-409-DUPLICATE, 404 COURSE_NOT_FOUND và 400 ENR-VALIDATION-FAILED; ví dụ payload mẫu và lệnh curl cho từng endpoint; sơ đồ Mermaid tuần tự luồng outbox → notification-service minh họa cơ chế at-least-once; định nghĩa hợp đồng sự kiện enrollment.created với payload, partition key courseId và chính sách deduplicate theo eventId; neo mọi mục vào thẻ truy vết [REQ-010], [REQ-011] và chuẩn bị cấu trúc liên kết chéo cho chương attendance sẽ bổ sung ở Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 2:
<!--DAY_HEADER_START-->Vận Hành Attendance Service Với Quét Điểm Danh QR, Replay Ngoại Tuyến FIFO Và Cổng Idempotent Tuyệt Đối<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.1: Sinh descriptor module con attendance-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/attendance-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module attendance-service kế thừa parent membership-hub-backend; đăng ký vào danh sách `<modules>` của descriptor cha sau enrollment-service; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator và quarkus-flyway phục vụ bootstrap schema riêng của dịch vụ; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=attendance-service phục vụ đóng gói image ở Giai đoạn 5; cấu hình quarkus.flyway.locations trỏ tới classpath:db/migration của chính module để chuỗi migration V4 chạy trong ngữ cảnh lịch sử Flyway riêng biệt; tinh chỉnh Agroal connection pool với kích thước pool chịu được burst replay đồng thời; bổ sung dependency test scope junit-jupiter, rest-assured và testcontainers-postgresql làm nền cho suite kiểm thử idempotency của Tester.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.2: Thực thể Attendance và migration cổng idempotent

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/Attendance.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-013], [EXC-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai thực thể Panache Attendance ánh xạ chính xác bảng attendance đã migrate ở Giai đoạn 1: attendanceId UUID PK, studentId UUID FK users, courseId UUID FK courses, attendanceDate DATE NOT NULL, recordedAt TIMESTAMP DEFAULT now() với tên cột snake_case khớp schema vật lý qua @Column; chạy migration V4__attendance_unique_idempotency.sql bổ sung ràng buộc uq_attendance_student_course_date UNIQUE (student_id, course_id, attendance_date) làm cổng idempotent duy nhất ở tầng lưu trữ [REQ-013] cùng index idx_attendance_course_date (course_id, attendance_date) phục vụ báo cáo điểm danh theo trung tâm; bổ sung AttendanceRepository với phương thức findByStudentCourseDate dùng prepared statement tham số hóa phục vụ tra cứu bản ghi hiện hữu khi trả phản hồi duplicate; nghiêm cấm nối chuỗi đầu vào vào câu lệnh SQL, mọi tham số đi qua positional/named parameter.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [REQ-013], [EXC-002]:**

<!--START_DDL_MIGRATION-->
```sql
-- V4__attendance_unique_idempotency.sql (attendance-service)
ALTER TABLE attendance
    ADD CONSTRAINT uq_attendance_student_course_date
    UNIQUE (student_id, course_id, attendance_date);

CREATE INDEX idx_attendance_course_date
    ON attendance (course_id, attendance_date);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.3: Endpoint quét điểm danh POST /api/v1/attendance/scan

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceScanResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-012], [EXC-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cài đặt POST /api/v1/attendance/scan nhận payload {studentId, courseId, clientTimestamp} với Bean Validation chặn thiếu trường bắt buộc trả 400 kèm danh sách từng trường lỗi; xác thực quan hệ student–course thông qua kiểm tra bản ghi Enrollments trước khi ghi, quan hệ không tồn tại trả 409 ATT-VAL-409 [REQ-012]; suy ra attendanceDate từ clientTimestamp theo múi giờ UTC thống nhất và ghi bản ghi Attendance kèm recordedAt timestamp máy chủ; chấp nhận các scan tồn đọng được mobile app phát lại sau khi reconnect theo thứ tự FIFO clientTimestamp tăng dần mà không phạt request đến trễ — bản ghi vẫn được tạo đúng một lần nhờ cổng idempotent ở tầng lưu trữ [EXC-001]; yêu cầu bearer JWT vai trò STUDENT; áp dụng annotation OpenAPI phục vụ công bố hợp đồng; ghi audit log mỗi lần scan kèm userId và timestamp phục vụ truy vết.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-012]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "/api/v1/attendance/scan",
  "method": "POST",
  "auth": "bearer JWT, role=STUDENT",
  "request": {
    "studentId": "uuid (required)",
    "courseId": "uuid (required)",
    "clientTimestamp": "ISO-8601 (required)"
  },
  "response_200_recorded": {
    "attendanceId": "uuid",
    "status": "RECORDED",
    "duplicate": false,
    "attendanceDate": "YYYY-MM-DD"
  },
  "error_409": {
    "errorCode": "ATT-VAL-409",
    "message": "Student-course enrollment relation not found"
  },
  "error_400": {
    "errorCode": "ATT-VALIDATION-FAILED",
    "invalidFields": [
      { "field": "string", "rejectedValue": "string|null", "message": "string" }
    ]
  }
}
```
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-012], [EXC-001]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "AttendanceValidationMapper",
  "package": "org.nlh4j.membership_hub.attendance.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.attendance.exception.EnrollmentRelationNotFoundException",
      "httpStatus": 409,
      "errorCode": "ATT-VAL-409",
      "bodySchema": {
        "errorCode": "ATT-VAL-409",
        "message": "Student-course enrollment relation not found"
      },
      "rule": "Validate enrollment existence before inserting attendance; late offline replays are accepted without penalty as long as the relation exists"
    },
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 400,
      "errorCode": "ATT-VALIDATION-FAILED",
      "bodySchema": {
        "errorCode": "ATT-VALIDATION-FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "Aggregate every Bean Validation violation into invalidFields preserving DTO declaration order; never expose stack traces or SQL fragments"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.4: Service idempotent bắt vi phạm ràng buộc duy nhất

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-013], [EXC-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Áp dụng ràng buộc unique (student_id, course_id, attendance_date) tại tầng PostgreSQL làm cổng idempotent duy nhất thay vì mẫu check-then-insert dễ lỗi TOCTOU [REQ-013]; khi INSERT va chạm ràng buộc, bắt ConstraintViolationException và ánh xạ qua DuplicateAttendanceMapper sang phản hồi 200 với status='DUPLICATE', duplicate=true, businessCode='ATT-DUP-001', message='already recorded' kèm attendanceId của bản ghi hiện hữu tra cứu qua repository mà không phát sinh hàng mới [EXC-002]; bảo đảm hai lần quét cách nhau dưới một phút trong cùng ngày trả kết quả nhất quán; ghi audit log sự kiện duplicate kèm userId và timestamp phục vụ truy vết; mapper không lộ chi tiết SQL hay stack trace ra phản hồi.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-013]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "/api/v1/attendance/scan",
  "method": "POST",
  "idempotencyRule": "UNIQUE (student_id, course_id, attendance_date)",
  "response_200_duplicate": {
    "attendanceId": "uuid (existing record reference)",
    "status": "DUPLICATE",
    "duplicate": true,
    "businessCode": "ATT-DUP-001",
    "message": "already recorded"
  }
}
```
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-002]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "DuplicateAttendanceMapper",
  "package": "org.nlh4j.membership_hub.attendance.exception",
  "providers": [
    {
      "handles": "org.hibernate.exception.ConstraintViolationException on uq_attendance_student_course_date",
      "httpStatus": 200,
      "errorCode": "ATT-DUP-001",
      "bodySchema": {
        "attendanceId": "uuid (existing record reference)",
        "status": "DUPLICATE",
        "duplicate": true,
        "businessCode": "ATT-DUP-001",
        "message": "already recorded"
      },
      "rule": "Unique constraint is the sole idempotency gate instead of check-then-insert; duplicate submissions return success with duplicate flag, no extra rows; every duplicate writes an audit entry with userId and timestamp; never leak SQL details"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.5: Chính sách tái xử lý scan ngoại tuyến sau ngắt kết nối

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/retry/OfflineReplayPolicy.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[EXC-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cài đặt hàng đợi nội bộ tiếp nhận bó scan được mobile app gửi lại sau reconnect; xử lý nghiêm ngặt FIFO theo clientTimestamp tăng dần bảo đảm scan có mốc sớm hơn luôn được ghi trước [EXC-001]; từng phần tử vẫn đi qua cổng idempotent nên các bản sao lặp trong bó replay tự động hội tụ về một bản ghi duy nhất mà không phát sinh lỗi phía client; giới hạn kích thước bó tối đa mỗi phiên replay chống abuse; ghi audit log mỗi phiên replay kèm userId, số lượng phần tử, số bản ghi trùng bị bỏ qua và timestamp để phục vụ giám sát phục hồi hậu outage; cấu hình timeout và backoff khi dịch vụ downstream quá tải bảo đảm phiên replay không làm nghẽn connection pool.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.6: Unit test xác thực quan hệ student–course

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceScanResource.java;./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceScanResourceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-012]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest xác minh [REQ-012]: quan hệ student–course hợp lệ ghi bản ghi Attendance thành công trả 200 status='RECORDED' duplicate=false; quan hệ không tồn tại trả 409 ATT-VAL-409; attendanceDate được suy đúng từ clientTimestamp kể cả trường hợp múi giờ khác UTC; payload thiếu studentId/courseId/clientTimestamp trả 400 với danh sách từng trường lỗi; caller chưa mang bearer JWT bị chặn 401; đo latency trung bình POST /api/v1/attendance/scan giữ dưới 200 ms đối chiếu [NFR-001].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.7: Kiểm thử tích hợp tính idempotent điểm danh

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceIdempotencyIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-013], [EXC-002], [EXC-001]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Dùng PostgreSQL Testcontainers; gửi song song hai request quét cùng student/course/ngày cách nhau dưới một phút, assert đúng một hàng Attendance được tạo và request thứ hai trả 200 duplicate=true businessCode='ATT-DUP-001' [REQ-013], [EXC-002]; mô phỏng replay bó 5 scan ngoại tuyến sau outage với clientTimestamp xen kẽ asserting thứ tự xử lý FIFO và zero bản ghi trùng lặp [EXC-001]; xác minh audit log ghi đủ sự kiện duplicate và phiên replay kèm userId/timestamp; xác minh phản hồi duplicate không lộ chi tiết SQL hay stack trace.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.8: Rà soát đồng thời và ràng buộc idempotent attendance-service

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-013], [EXC-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Phân tích đường đua giữa INSERT và vi phạm unique để xác nhận không tồn tại mẫu check-then-insert dễ lỗi TOCTOU và cổng idempotent dựa hoàn toàn vào ràng buộc DB [REQ-013]; đánh giá cấu hình Agroal connection pool và timeout khi xử lý burst replay đồng thời; kiểm tra ánh xạ ConstraintViolationException không lộ chi tiết SQL ra ngoài phản hồi [EXC-002]; rà soát việc suy diễn attendanceDate từ clientTimestamp có thống nhất múi giờ UTC trên toàn pipeline; đối chiếu OWASP A03 injection: xác minh không tồn tại đường nối chuỗi trong repository; lập danh sách remediation ưu tiên kèm diff cụ thể và chốt điều kiện mở khóa Ngày 3.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.9: Biên soạn đặc tả API attendance-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-attendance-service.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tài liệu hóa endpoint POST /api/v1/attendance/scan với semantics idempotent: bảng schema request/response cho hai trạng thái RECORDED và DUPLICATE [REQ-012], [REQ-013]; mô tả chính sách retry ngoại tuyến của mobile app và thứ tự FIFO replay kèm ví dụ bó scan tồn đọng sau outage [EXC-001]; liệt kê bảng mã lỗi ATT-VAL-409 và ATT-DUP-001 ('already recorded') kèm điều kiện kích hoạt và hành vi hệ thống [EXC-002]; bổ sung sơ đồ Mermaid tuần tự quét QR → validate enrollment → insert → duplicate branch; neo mọi mục vào thẻ truy vết tương ứng và liên kết chéo với từ điển dữ liệu bảng ATTENDANCE từ Giai đoạn 1.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 3:
<!--DAY_HEADER_START-->Hoàn Thiện Card Service Với Truy Vấn Ngày Hiệu Lực Thẻ Hội Viên Và Luồng Gia Hạn Sau Xác Nhận Thanh Toán<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.1: Sinh descriptor module con card-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/card-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module card-service kế thừa parent membership-hub-backend; đăng ký vào danh sách `<modules>` của descriptor cha sau attendance-service; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator, quarkus-flyway và quarkus-smallrye-reactive-messaging-kafka phục vụ tiêu thụ sự kiện payment.confirmed; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=card-service phục vụ đóng gói image ở Giai đoạn 5; cấu hình quarkus.flyway.locations trỏ tới classpath:db/migration của chính module để chuỗi migration V5 chạy trong ngữ cảnh lịch sử Flyway riêng biệt; bổ sung dependency test scope junit-jupiter, rest-assured, testcontainers-postgresql và testcontainers-kafka làm nền cho suite kiểm thử luồng gia hạn của Tester.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.2: Máy tính ngày hiệu lực thẻ và migration hỗ trợ truy vấn

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/CardValidityCalculator.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai CardValidityCalculator thuần chức năng suy ra ba chỉ số từ thực thể StudentCard: totalValidityDays lấy trực tiếp từ cột validity_days, daysUsed = CURRENT_DATE − issue_date được kẹp biên trong khoảng [0, validityDays], daysRemaining = validityDays − daysUsed bảo đảm không bao giờ âm [REQ-014]; chuẩn hóa mọi phép toán ngày theo múi giờ UTC thống nhất tránh lệch múi giờ làm sai số liệu; xử lý biên issueDate trùng ngày hiện hành trả daysUsed=0; bổ sung thực thể Panache StudentCard ánh xạ bảng student_cards với tên cột snake_case khớp schema vật lý; chạy migration V5__card_validity_support.sql tạo index idx_student_cards_student_lookup (student_id, issue_date) bảo đảm truy vấn thẻ phản hồi sub-second.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [REQ-014]:**

<!--START_DDL_MIGRATION-->
```sql
-- V5__card_validity_support.sql (card-service)
CREATE INDEX idx_student_cards_student_lookup
    ON student_cards (student_id, issue_date);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.3: Endpoint truy vấn thẻ hội viên GET /api/v1/cards/me

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/CardQueryResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cài đặt GET /api/v1/cards/me yêu cầu bearer JWT và suy ra studentId từ claim sub của token thay vì tham số đường dẫn chống leo thang dữ liệu chéo tài khoản theo OWASP A01; gọi CardValidityCalculator tính ba chỉ số totalValidityDays/daysUsed/daysRemaining phục vụ render thẻ hội viên kỹ thuật số kèm đếm ngày hiệu lực còn lại [REQ-014]; trả 404 CARD-NOT-FOUND khi học viên chưa được cấp thẻ; tận dụng index idx_student_cards_student_lookup bảo đảm phản hồi sub-second; áp dụng annotation OpenAPI phục vụ công bố hợp đồng; ghi audit log truy vấn kèm userId và timestamp phục vụ truy vết.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-014]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "/api/v1/cards/me",
  "method": "GET",
  "auth": "Bearer JWT (role Student)",
  "response_200": {
    "cardId": "uuid",
    "issueDate": "YYYY-MM-DD",
    "totalValidityDays": 90,
    "daysUsed": 34,
    "daysRemaining": 56
  },
  "error_404": {
    "errorCode": "CARD-NOT-FOUND",
    "message": "No membership card issued for this student"
  }
}
```
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-014]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "CardQueryExceptionMapper",
  "package": "org.nlh4j.membership_hub.card.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.card.exception.CardNotFoundException",
      "httpStatus": 404,
      "errorCode": "CARD-NOT-FOUND",
      "bodySchema": {
        "errorCode": "CARD-NOT-FOUND",
        "message": "No membership card issued for this student"
      },
      "rule": "Resolve studentId from JWT sub claim only; never trust path or query parameters to prevent cross-account data escalation"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.4: Endpoint gia hạn thẻ POST /api/v1/cards/renew

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/CardRenewalResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-015]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Cài đặt POST /api/v1/cards/renew nhận {renewalPeriodDays, paymentReferenceId} với renewalPeriodDays ví dụ 30 và phải lớn hơn 0; chỉ mở rộng validityDays/ngày kết thúc của StudentCards sau khi PaymentConfirmationConsumer xác nhận sự kiện payment.confirmed từ payment service tương ứng paymentReferenceId [REQ-015]; trong một @Transaction cập nhật thẻ và điều phối notification xác nhận gia hạn tới học viên; từ chối gia hạn khi paymentReferenceId chưa được xác nhận bằng 409 PAYMENT-PENDING mà không làm thay đổi dữ liệu thẻ; validate thẻ tồn tại trả 404 CARD-NOT-FOUND khi thiếu; yêu cầu bearer JWT vai trò STUDENT; ghi audit log mỗi lần gia hạn kèm userId, paymentReferenceId và timestamp.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-015]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "/api/v1/cards/renew",
  "method": "POST",
  "auth": "Bearer JWT (role Student)",
  "request": {
    "renewalPeriodDays": 30,
    "paymentReferenceId": "string (required)"
  },
  "response_200": {
    "cardId": "uuid",
    "validityDaysBefore": 90,
    "validityDaysAfter": 120,
    "extendedUntil": "YYYY-MM-DD",
    "confirmationNotificationSent": true
  },
  "error_409": {
    "errorCode": "PAYMENT-PENDING",
    "message": "Payment reference not confirmed yet"
  },
  "error_404": { "code": "CARD-NOT-FOUND" }
}
```
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-015]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "CardRenewalExceptionMapper",
  "package": "org.nlh4j.membership_hub.card.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.card.exception.PaymentPendingException",
      "httpStatus": 409,
      "errorCode": "PAYMENT-PENDING",
      "bodySchema": {
        "errorCode": "PAYMENT-PENDING",
        "message": "Payment reference not confirmed yet",
        "paymentReferenceId": "string"
      },
      "rule": "Reject renewal without mutating card data when payment.confirmed has not been received for the given paymentReferenceId"
    },
    {
      "handles": "org.nlh4j.membership_hub.card.exception.CardNotFoundException",
      "httpStatus": 404,
      "errorCode": "CARD-NOT-FOUND",
      "bodySchema": { "errorCode": "CARD-NOT-FOUND", "message": "No membership card issued for this student" },
      "rule": "Validate card existence before mutating; no partial mutations"
    },
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 400,
      "errorCode": "CARD-RENEWAL-VALIDATION-FAILED",
      "bodySchema": {
        "errorCode": "CARD-RENEWAL-VALIDATION-FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "renewalPeriodDays must be greater than 0; aggregate violations into invalidFields preserving DTO declaration order"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.5: Consumer xác nhận thanh toán cho luồng gia hạn thẻ

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/PaymentConfirmationConsumer.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-015]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tiêu thụ topic payment.confirmed với chế độ at-least-once qua SmallRye Reactive Messaging; áp dụng khóa idempotent theo paymentReferenceId lưu trạng thái đã xử lý để chống cộng dồn validityDays khi sự kiện được phát lại [REQ-015]; khi xử lý thành công thì đánh dấu paymentReferenceId đã xác nhận sẵn sàng cho luồng renew và điều phối notification xác nhận; đẩy payload sai schema hoặc thiếu trường bắt buộc vào dead-letter topic payment.confirmed.dlq để phân tích hậu kiểm; cấu hình groupId card-service-renewal và chiến lược ack thủ công sau khi persist thành công; ghi audit log mỗi lần tiêu thụ kèm paymentReferenceId và timestamp phục vụ truy vết.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-015]:**

<!--START_API_CONTRACT-->
```json
{
  "topic": "payment.confirmed",
  "groupId": "card-service-renewal",
  "deliveryMode": "at-least-once",
  "idempotencyKey": "paymentReferenceId",
  "deadLetterTopic": "payment.confirmed.dlq",
  "payload": {
    "eventId": "uuid",
    "paymentReferenceId": "string",
    "studentId": "uuid",
    "amountConfirmed": "decimal",
    "occurredAt": "YYYY-MM-DDTHH:mm:ssZ"
  },
  "onSuccess": ["mark paymentReferenceId confirmed", "enable card validity extension", "dispatch renewal confirmation notification"]
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.6: Bộ test đơn vị máy tính ngày hiệu lực thẻ

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/CardValidityCalculator.java;./sources/backend/card-service/src/test/java/org/nlh4j/membership_hub/card/CardValidityCalculatorTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết JUnit 5 parametrized xác minh [REQ-014]: daysUsed được kẹp biên tại 0 khi issueDate trùng ngày hiện hành và tại validityDays khi thẻ hết hạn; daysRemaining không bao giờ âm và về đúng 0 khi hết hạn; mọi phép trừ ngày thống nhất múi giờ UTC kể cả case vượt ranh giới tháng/năm nhuận; phủ case validityDays=1 biên tối thiểu; xác minh bất biến toán học totalValidityDays = daysUsed + daysRemaining luôn được bảo toàn trên mọi tổ hợp đầu vào.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.7: Kiểm thử tích hợp luồng gia hạn thẻ

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/card-service/src/test/java/org/nlh4j/membership_hub/card/CardRenewalFlowIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-015]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Mô phỏng toàn trình [REQ-015]: POST /api/v1/cards/renew trước khi thanh toán trả 409 PAYMENT-PENDING và dữ liệu thẻ bất biến; phát sự kiện payment.confirmed lên Kafka Testcontainers → consumer xác nhận → gọi renew lần hai thành công với validityDays tăng đúng 30 ngày và notification xác nhận được điều phối; phát lại cùng sự kiện payment.confirmed với paymentReferenceId trùng lặp chứng minh tính idempotent không cộng dồn ngày hiệu lực; kịch bản thẻ không tồn tại trả 404 CARD-NOT-FOUND; kịch bản renewalPeriodDays=0 hoặc âm trả 400 với danh sách trường lỗi; xác minh audit log ghi đủ chuỗi sự kiện gia hạn kèm userId và timestamp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.8: Rà soát phép toán ngày và tính idempotent gia hạn card-service

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/card-service/src/main/java/org/nlh4j/membership_hub/card/CardValidityCalculator.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Rà soát phép trừ ngày theo UTC để loại trừ lỗi lệch múi giờ làm sai daysUsed/daysRemaining, xác minh không sử dụng LocalDate.now() không tham số múi giờ ở bất kỳ đâu trong pipeline [REQ-014]; kiểm tra consumer chống cộng dồn validityDays khi sự kiện payment.confirmed được phát lại và xác minh khóa idempotent theo paymentReferenceId hoạt động đúng dưới tải đồng thời [REQ-015]; rà soát transaction boundary giữa xác nhận payment và mở rộng thẻ bảo đảm không có trạng thái nửa vời; đối chiếu OWASP A01: xác minh studentId trên cards/me và renew suy từ claim sub của JWT; chuẩn hóa thông điệp lỗi không leak chi tiết nội bộ; đề xuất bản fix kèm diff cụ thể.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.9: Biên soạn đặc tả API card-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-card-service.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tài liệu hóa GET /api/v1/cards/me với quy tắc suy ra totalValidityDays/daysUsed/daysRemaining kèm ví dụ payload và quy tắc kẹp biên [REQ-014]; mô tả luồng POST /api/v1/cards/renew phụ thuộc xác nhận payment.confirmed với sơ đồ Mermaid tuần tự renew → payment.confirmed → extend → notification [REQ-015]; liệt kê bảng mã lỗi CARD-NOT-FOUND, PAYMENT-PENDING và CARD-RENEWAL-VALIDATION-FAILED kèm điều kiện kích hoạt; bổ sung hợp đồng sự kiện payment.confirmed với chính sách at-least-once, khóa idempotent paymentReferenceId và dead-letter topic payment.confirmed.dlq; neo mọi mục vào thẻ truy vết tương ứng và liên kết chéo với từ điển dữ liệu bảng STUDENT_CARDS từ Giai đoạn 1.

<!--END_ATOMIC_SUB_TASK_NODE-->