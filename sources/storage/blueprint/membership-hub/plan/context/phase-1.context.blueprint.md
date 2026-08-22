# Giai đoạn 1: <!--PHASE_NAME_START-->Khởi tạo cấu trúc dự án và nền tảng hạ tầng cơ sở<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã bản thiết kế** | ARCH-20260822094056 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Khởi tạo cấu trúc dự án và nền tảng hạ tầng cơ sở<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai toàn bộ cấu trúc dự án nền tảng cho kiến trúc vi mô backend Quarkus và frontend Next.js, khởi tạo toàn bộ schema cơ sở dữ liệu PostgreSQL với 9 bảng nghiệp vụ chính, triển khai lớp xác thực RBAC và OAuth2 cốt lõi, cùng các chức năng quản lý người dùng và trung tâm đầu tiên, đảm bảo mọi service có môi trường phát triển ổn định, sẵn sàng cho các giai đoạn phát triển chức năng tiếp theo<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/22 09:40:56 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 1 tập trung vào việc thiết lập nền tảng cốt lõi cho toàn bộ hệ thống membership-hub, bao gồm 4 trụ cột chính:
1. Khởi tạo cấu trúc dự án vi mô backend Quarkus với 10 service con độc lập và cấu trúc dự án frontend Next.js theo chuẩn App Router, đảm bảo môi trường phát triển ổn định cho toàn bộ hệ thống.
2. Khởi tạo toàn bộ schema cơ sở dữ liệu PostgreSQL với 9 bảng nghiệp vụ chính, các ràng buộc toàn vẹn khóa chính/khóa ngoại, ràng buộc CHECK và chỉ mục tối ưu, đáp ứng yêu cầu lưu trữ dữ liệu nghiệp vụ.
3. Triển khai lớp xác thực RBAC và OAuth2 cốt lõi với cơ chế JWT token (access token 15 phút, refresh token 7 ngày), bộ lọc xác thực toàn cục và trình xử lý ngoại lệ chuẩn hóa, đảm bảo bảo mực truy cập hệ thống.
4. Triển khai các chức năng nghiệp vụ cốt lõi đầu tiên: quản lý người dùng (đăng ký email/mật khẩu, xác thực mạng xã hội, phân quyền vai trò) và quản lý trung tâm (xem danh sách, CRUD, phân quyền quản trị trung tâm), tuân thủ ma trận RBAC đã định nghĩa và các yêu cầu bảo mật OWASP Top 10.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục
Tất cả đường dẫn tệp đều bắt đầu với gốc kho lưu trữ `./sources/`, tuân thủ cấu trúc kiến trúc vi mô đã định nghĩa:
* **Hạ tầng backend vi mô Quarkus:**
  * ./sources/backend/pom.xml [ARC-000]
  * ./sources/backend/auth-service/pom.xml [ARC-000]
  * ./sources/backend/center-service/pom.xml [ARC-000]
  * ./sources/backend/course-service/pom.xml [ARC-000]
  * ./sources/backend/enrollment-service/pom.xml [ARC-000]
  * ./sources/backend/attendance-service/pom.xml [ARC-000]
  * ./sources/backend/membership-service/pom.xml [ARC-000]
  * ./sources/backend/notification-service/pom.xml [ARC-000]
  * ./sources/backend/promotion-service/pom.xml [ARC-000]
  * ./sources/backend/report-service/pom.xml [ARC-000]
  * ./sources/backend/ai-chatbot-service/pom.xml [ARC-000]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/entity/Role.java [DAT-002, ARC-001]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/entity/User.java [DAT-001, ARC-001]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/repository/UserRepository.java [DAT-001, ARC-001]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/repository/RoleRepository.java [DAT-002, ARC-001]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/AuthService.java [REQ-001, REQ-002, ARC-006]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/controller/AuthController.java [REQ-001, REQ-002, ARC-006]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/OAuth2Service.java [REQ-002, ARC-006]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/RoleManagementService.java [REQ-003, ARC-001, ARC-002, ARC-003, ARC-004, ARC-005]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/filter/RbacFilter.java [ARC-001, ARC-002, ARC-003, ARC-004, ARC-005, NFR-003]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/util/JwtUtil.java [ARC-006, NFR-003]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/exception/GlobalExceptionHandler.java [EXC-004]
  * ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/entity/Center.java [DAT-003, ARC-002]
  * ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/repository/CenterRepository.java [DAT-003, ARC-002]
  * ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/service/CenterService.java [REQ-004, REQ-005, ARC-002]
  * ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/controller/CenterController.java [REQ-004, REQ-005, ARC-002]
  * ./sources/backend/auth-service/src/main/resources/db/migration/V1__init_schema.sql [DAT-001, DAT-002, DAT-003, DAT-004, DAT-005, DAT-006, DAT-007, DAT-008, DAT-009]
* **Lớp frontend Next.js:**
  * ./sources/frontend/package.json [ARC-000]
  * ./sources/frontend/tsconfig.json [ARC-000]
* **Tài liệu doanh nghiệp:**
  * ./sources/docs/architecture-overview.md [ARC-000]
  * ./sources/docs/api-contracts-auth.md [ARC-000]
  * ./sources/docs/api-contracts-center.md [ARC-000]
  * ./sources/docs/database-schema.md [ARC-000]
  * ./sources/docs/security-spec.md [ARC-006, NFR-003]
* **Tệp kiểm thử:**
  * ./sources/backend/auth-service/src/test/java/com/hub/auth/BuildValidationTest.java [ARC-000]
  * ./sources/backend/auth-service/src/test/java/com/hub/auth/DbMigrationTest.java [DAT-001, DAT-002, DAT-003, DAT-004, DAT-005, DAT-006, DAT-007, DAT-008, DAT-009]
  * ./sources/backend/auth-service/src/test/java/com/hub/auth/AuthServiceTest.java [REQ-001, EXC-004]
  * ./sources/backend/auth-service/src/test/java/com/hub/auth/OAuth2ServiceTest.java [REQ-002, REQ-003]
  * ./sources/backend/auth-service/src/test/java/com/hub/auth/RbacFilterTest.java [ARC-001, ARC-002, ARC-003, ARC-004, ARC-005]
  * ./sources/backend/center-service/src/test/java/com/hub/center/CenterServiceTest.java [REQ-004, REQ-005, REQ-006]
  * ./sources/backend/auth-service/src/test/java/com/hub/auth/IntegrationAuthCenterTest.java [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]

## 3. Chỉ thị chức năng cho tác nhân phụ chuyên dụng
* **Coder**: Đóng vai trò là Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên cả backend services và frontend/ứng dụng di động. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
* **Tester**: Đóng vai trò là Kiểm soát chất lượng (QC/QA) cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác thực hiệu năng. Bị cấm sửa mã nguồn sản xuất. Nếu mục tiêu nhiệm vụ liên quan đến phạm vi kiểm thử tích hợp hoặc end-to-end mà không có tệp mã ứng dụng cụ thể nào có thể bị giới hạn, bạn PHẢI xuất ra literal token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp dấu chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Hoạt động như là Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Đặc tả kỹ thuật toàn diện, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp kiến trúc đang hoạt động của dự án. Mỗi tệp tài liệu kỹ thuật được tạo PHẢI được liệt kê là thực thể đường dẫn tệp cụ thể có phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Chịu trách nhiệm xác minh trình biên dịch, cổng phân tích tĩnh và vá bảo vệ phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
* **Docker**: Chuyên nghiệp nghiêm ngặt về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
* **GCP**: Chuyên nghiệp về tự động hóa đám mây trong Google Cloud Platform. Chịu trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container một cách tự nhiên trên Google Cloud Run.
* **GKE**: Chuyên nghiệp về điều phối container sản xuất bên trong Google Kubernetes Engine. Chịu trách nhiệm xây dựng manifest triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc dịch vụ vi mô vào cụm GKE đang hoạt động.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
Giai đoạn 1 được coi là hoàn thành khi đáp ứng đầy đủ các mốc định lượng sau:
1. Toàn bộ cấu trúc dự án backend vi mô Quarkus (10 service con) và frontend Next.js được khởi tạo thành công, không có lỗi biên dịch, tất cả phụ thuộc được tải đúng.
2. Toàn bộ schema cơ sở dữ liệu PostgreSQL với 9 bảng nghiệp vụ được tạo thành công qua script migration, tất cả ràng buộc toàn vẹn hoạt động đúng, không có lỗi khi chạy migration trên môi trường PostgreSQL 16.
3. Lớp xác thực RBAC và OAuth2 được triển khai hoàn chỉnh, hỗ trợ đăng ký email/mật khẩu, đăng nhập mạng xã hội (Firebase, Google, Facebook), cấp JWT token với thời hạn đúng quy định (access 15 phút, refresh 7 ngày), bộ lọc xác thực toàn cục hoạt động đúng với tất cả endpoint.
4. Các chức năng quản lý người dùng cơ bản (đăng ký, xác thực xã hội, phân quyền vai trò) và quản lý trung tâm (xem danh sách, CRUD, phân quyền quản trị trung tâm) được triển khai và hoạt động đúng theo yêu cầu nghiệp vụ, tuân thủ ma trận RBAC.
5. Tất cả bộ kiểm thử đơn vị cho các chức năng cốt lõi của giai đoạn đều vượt qua, độ bao phủ mã đạt >= 85%, không có lỗi nghiêm trọng trong kiểm thử tích hợp auth-center.
6. Tất cả thẻ theo dõi yêu cầu được phân phối cho giai đoạn 1 ([ARC-000], [DAT-001] đến [DAT-009], [ARC-001] đến [ARC-005], [REQ-001] đến [REQ-006], [EXC-004]) được ánh xạ đầy đủ vào các nhiệm vụ kỹ thuật và tài liệu, không có thẻ nào bị thiếu.
7. Không có lỗ hổng bảo mật OWASP Top 10 được phát hiện trong mã nguồn các service auth và center, tất cả đầu vào người dùng được xác thực, truy vấn cơ sở dữ liệu sử dụng prepared statements.
8. Tất cả tài liệu kỹ thuật (hợp đồng API, đặc tả bảo mật, schema cơ sở dữ liệu) được hoàn thiện và cập nhật đầy đủ, tuân thủ chuẩn tài liệu doanh nghiệp.

## 5. Nhật ký thực hiện kiến trúc từng ngày

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Khởi tạo cấu trúc dự án nền tảng<!--DAY_HEADER_END-->
#### 📝 Công việc con 1.1: Tạo cấu trúc dự án backend vi mô Quarkus
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/pom.xml
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tệp pom.xml gốc cho dự án backend vi mô Quarkus, cấu hình 10 module service con (auth, center, course, enrollment, attendance, membership, notification, promotion, report, ai-chatbot), thiết lập các phụ thuộc chung cho Quarkus 3.15, JWT 0.12, PostgreSQL 16 driver, OAuth2, bcrypt, và các thư viện bổ trợ cần thiết, đảm bảo cấu hình build thành công cho tất cả module, tuân thủ cấu trúc Maven đa module chuẩn doanh nghiệp.
#### 📝 Công việc con 1.2: Tạo cấu trúc dự án frontend Next.js
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/package.json
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tệp package.json cho dự án frontend Next.js 14, cấu hình các phụ thuộc cốt lõi (React 18, Redux Toolkit, Axios 1.6, i18next 23.7, Tailwind CSS 3.4), khởi tạo tệp tsconfig.json cho TypeScript, đảm bảo cấu hình build và chạy môi trường phát triển thành công, tuân thủ cấu trúc dự án Next.js App Router chuẩn.
#### 📝 Công việc con 1.3: Khởi tạo cấu trúc thư mục tài liệu doanh nghiệp
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/architecture-overview.md
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo cấu trúc thư mục tài liệu doanh nghiệp, khởi tạo các tệp mẫu cho bản vẽ kiến trúc tổng thể, hợp đồng API, hướng dẫn vận hành, đảm bảo cấu trúc tài liệu tuân thủ chuẩn doanh nghiệp, dễ dàng mở rộng cho các giai đoạn sau, bao gồm mục lục chuẩn và mẫu nội dung cho từng loại tài liệu.
#### 📝 Công việc con 1.4: Xác thực cấu trúc dự án build thành công
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/pom.xml;./sources/backend/auth-service/src/test/java/com/hub/auth/BuildValidationTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện build tất cả module backend và dự án frontend, xác nhận không có lỗi biên dịch, tất cả phụ thuộc được tải đúng, ghi nhận kết quả kiểm thực vào báo cáo, báo cáo lỗi nếu có bất kỳ lỗi build nào.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Khởi tạo schema cơ sở dữ liệu và thực thể RBAC cơ bản<!--DAY_HEADER_END-->
#### 📝 Công việc con 2.1: Tạo script DDL khởi tạo toàn bộ bảng nghiệp vụ
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/resources/db/migration/V1__init_schema.sql
* **Thẻ truy xuất:** <!--START_TAGS-->[DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết script DDL ANSI compliant khởi tạo toàn bộ 9 bảng nghiệp vụ (roles, users, centers, courses, enrollments, attendance, student_cards, notifications, promotions, announcements, system_settings), định nghĩa rõ ràng kiểu dữ liệu, ràng buộc khóa chính/khóa ngoại, ràng buộc CHECK cho các trường kiểm tra, đảm bảo script chạy thành công trên PostgreSQL 16, tuân thủ các ràng buộc đã định nghĩa trong từ điển dữ liệu.
<!--START_DDL_MIGRATION-->
```sql
-- Tạo bảng vai trò người dùng [DAT-001], [DAT-002]
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

-- Tạo bảng người dùng [DAT-001]
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL REFERENCES roles(role_id),
    provider VARCHAR(20) NOT NULL DEFAULT 'local' CHECK (provider IN ('local', 'firebase', 'google', 'facebook')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tạo bảng trung tâm [DAT-003]
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE CHECK (tax_id ~ '^[0-9]{10,13}$'),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255) CHECK (contact_email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Tạo bảng khóa học [DAT-004]
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30,
    CHECK (end_date > start_date)
);

-- Tạo bảng ghi danh [DAT-005]
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)
);

-- Tạo bảng điểm danh [DAT-006]
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id, attendance_date)
);

-- Tạo bảng thẻ hội viên [DAT-007]
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL UNIQUE REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);

-- Tạo bảng thông báo [DAT-008]
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(255),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

-- Tạo bảng khuyến mãi [DAT-009]
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL CHECK (discount_percent BETWEEN 1 AND 100),
    start_date DATE,
    end_date DATE,
    description TEXT,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Tạo bảng thông báo hệ thống [DAT-009]
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Tạo bảng cài đặt hệ thống [DAT-009]
CREATE TABLE system_settings (
    setting_key VARCHAR(50) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description VARCHAR(200)
);
```
<!--END_DDL_MIGRATION-->
#### 📝 Công việc con 2.2: Triển khai thực thể Role và User trong service auth
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/entity/Role.java
* **Thẻ truy xuất:** <!--START_TAGS-->[DAT-001], [DAT-002], [ARC-001]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho bảng roles và users, ánh xạ chính xác các trường dữ liệu, thiết lập quan hệ nhiều-người dùng thuộc một vai trò giữa User và Role (sử dụng `@ManyToOne` và `@JoinColumn`), đảm bảo ánh xạ khớp với schema cơ sở dữ liệu đã định nghĩa, tuân thủ các ràng buộc NOT NULL và UNIQUE, thêm các annotation validation (`@NotNull`, `@Size`, `@Email`) cho các trường dữ liệu.
#### 📝 Công việc con 2.3: Xác thực migration cơ sở dữ liệu thành công
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/resources/db/migration/V1__init_schema.sql;./sources/backend/auth-service/src/test/java/com/hub/auth/DbMigrationTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Chạy script migration trên cơ sở dữ liệu PostgreSQL cục bộ, xác nhận tất cả các bảng được tạo đúng, các ràng buộc khóa chính/khóa ngoại hoạt động, không có lỗi khi chạy script, viết test tự động hóa để xác minh migration thành công trên môi trường CI/CD.
#### 📝 Công việc con 2.4: Cập nhật tài liệu schema cơ sở dữ liệu
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/database-schema.md
* **Thẻ truy xuất:** <!--START_TAGS-->[DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cập nhật tệp tài liệu schema cơ sở dữ liệu với mô tả chi tiết từng bảng, trường dữ liệu, kiểu dữ liệu, ràng buộc, mối quan hệ giữa các bảng, kèm sơ đồ ERD đã được cung cấp trong yêu cầu, đảm bảo tài liệu dễ hiểu cho các đội phát triển sau.

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Triển khai chức năng đăng ký và xác thực người dùng cơ bản<!--DAY_HEADER_END-->
#### 📝 Công việc con 3.1: Triển khai logic đăng ký email/mật khẩu trong AuthService
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/AuthService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [EXC-004]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic đăng ký người dùng bằng email/mật khẩu, bao gồm xác thực đầu vào (định dạng email hợp lệ, độ mạnh mật khẩu tối thiểu 8 ký tự bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt), mã hóa mật khẩu bằng bcrypt với cost factor 12, tạo bản ghi người dùng với vai trò mặc định là Student, xử lý lỗi xác thực theo yêu cầu [EXC-004] trả về danh sách chi tiết lỗi cho từng trường không hợp lệ, đảm bảo không tạo bản ghi người dùng nếu xác thực thất bại.
#### 📝 Công việc con 3.2: Triển khai endpoint đăng ký và đăng nhập trong AuthController
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/controller/AuthController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [ARC-006]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST cho đăng ký (POST /api/auth/register), đăng nhập (POST /api/auth/login), cấp access token (hết hạn 15 phút) và refresh token (hết hạn 7 ngày) theo chuẩn JWT, trả về phản hồi JSON theo hợp đồng API đã định nghĩa, áp dụng xác thực đầu vào và chuẩn hóa lỗi, đảm bảo endpoint công khai không yêu cầu xác thực JWT.
<!--START_API_CONTRACT-->
```json
// Endpoint xác thực
POST /api/auth/register
Request Body: {
  "email": "string",
  "password": "string",
  "fullName": "string"
}
Response 200: {
  "accessToken": "string",
  "refreshToken": "string",
  "expiresIn": 900,
  "user": { "userId": "uuid", "role": "string" }
}
Response 400: { "error": "VALIDATION_ERROR", "details": ["Email không hợp lệ", "Mật khẩu phải có ít nhất 8 ký tự"] }

POST /api/auth/login
Request Body: {
  "email": "string",
  "password": "string"
}
Response 200: {
  "accessToken": "string",
  "refreshToken": "string",
  "expiresIn": 900,
  "user": { "userId": "uuid", "role": "string" }
}
Response 401: { "error": "INVALID_CREDENTIALS", "message": "Email hoặc mật khẩu không đúng" }

POST /api/auth/refresh
Request Body: { "refreshToken": "string" }
Response 200: { "accessToken": "string", "expiresIn": 900 }
Response 401: { "error": "INVALID_REFRESH_TOKEN", "message": "Refresh token không hợp lệ hoặc đã hết hạn" }
```
<!--END_API_CONTRACT-->
#### 📝 Công việc con 3.3: Viết unit test cho chức năng đăng ký và xác thực
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/AuthService.java;./sources/backend/auth-service/src/test/java/com/hub/auth/AuthServiceTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [EXC-004]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test đầy đủ cho logic đăng ký, bao gồm trường hợp thành công, lỗi xác thực đầu vào (email không hợp lệ, mật khẩu yếu, họ tên trống), trùng lặp email, xác nhận mật khẩu bcrypt được tạo đúng, bản ghi người dùng được lưu chính xác vào cơ sở dữ liệu, đảm bảo độ bao phủ mã >= 90%.
#### 📝 Công việc con 3.4: Rà soát mã nguồn chức năng xác thực
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/AuthService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [EXC-004], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát mã nguồn chức năng đăng ký và xác thực, kiểm tra tuân thủ chuẩn bảo mật mật khẩu bcrypt, không có lỗ hổng SQL injection (sử dụng prepared statements), xác thực đầu vào đầy đủ, xử lý ngoại lệ chính xác, đề xuất cải tiến nếu có.

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->Triển khai xác thực mạng xã hội và phân quyền người dùng<!--DAY_HEADER_END-->
#### 📝 Công việc con 4.1: Tích hợp OAuth2 Firebase/Google/Facebook vào AuthService
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/OAuth2Service.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-002], [ARC-006]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic tích hợp OAuth2 với các nhà cung cấp Firebase, Google, Facebook, xử lý mã xác thực từ nhà cung cấp, trao đổi lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ (nếu email đã tồn tại thì cập nhật thông tin provider, nếu không thì tạo mới với vai trò Student), cấp JWT token sau khi xác thực thành công, xử lý lỗi từ nhà cung cấp OAuth2 (từ chối truy cập, mã xác thực không hợp lệ).
#### 📝 Công việc con 4.2: Triển khai logic gán/thay đổi vai trò người dùng
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/RoleManagementService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic gán, thay đổi, hủy gán vai trò người dùng, đảm bảo quyền truy cập được áp dụng ngay lập tức sau khi thay đổi vai trò (xóa cache Redis phiên người dùng nếu có), kiểm tra quyền của người thực hiện thao tác phân quyền (chỉ System Admin được phép thay đổi vai trò), tuân thủ ma trận RBAC đã định nghĩa, ghi log hành động thay đổi vai trò theo yêu cầu NFR-006.
#### 📝 Công việc con 4.3: Viết unit test cho xác thực mạng xã hội và phân quyền
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/OAuth2Service.java;./sources/backend/auth-service/src/test/java/com/hub/auth/OAuth2ServiceTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-002], [REQ-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test cho luồng xác thực mạng xã hội (giả lập phản hồi từ nhà cung cấp OAuth2), xác nhận bản ghi người dùng được tạo/cập nhật đúng, JWT token được cấp chính xác; viết test cho logic phân quyền, xác nhận vai trò người dùng được cập nhật đúng trong cơ sở dữ liệu, kiểm tra quyền truy cập được áp dụng ngay sau thay đổi, đảm bảo độ bao phủ mã >= 90%.
#### 📝 Công việc con 4.4: Rà soát logic phân quyền và xác thực mạng xã hội
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/OAuth2Service.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-002], [REQ-003], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát logic tích hợp OAuth2 và phân quyền người dùng, kiểm tra không có lỗ hổng bảo mật (lộ thông tin người dùng, phân quyền sai vai trò, lỗi chuyển hướng OAuth2 không hợp lệ), xác nhận tuân thủ yêu cầu OAuth2 và RBAC, đề xuất cải tiến nếu có.

### 🌤️ NGÀY 5: <!--DAY_HEADER_START-->Triển khai chức năng quản lý trung tâm cơ bản<!--DAY_HEADER_END-->
#### 📝 Công việc con 5.1: Triển khai thực thể Center và repository tương ứng
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/entity/Center.java
* **Thẻ truy xuất:** <!--START_TAGS-->[DAT-003], [ARC-002]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho bảng centers, ánh xạ chính xác các trường dữ liệu, thiết lập các ràng buộc ánh xạ khớp với schema cơ sở dữ liệu (bao gồm ràng buộc unique cho taxId, ràng buộc định dạng email và regex cho taxId), triển khai repository cho thực thể Center với các phương thức truy vấn cơ bản (tìm theo ID, tìm tất cả, lưu, xóa, tìm theo taxId).
#### 📝 Công việc con 5.2: Triển khai logic nghiệp vụ quản lý trung tâm
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/service/CenterService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-004], [REQ-005], [ARC-002]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic nghiệp vụ cho các chức năng xem danh sách trung tâm, thêm/sửa/xóa trung tâm, kiểm tra trùng lặp mã số thuế khi tạo mới hoặc cập nhật trung tâm (nếu taxId đã tồn tại thì ném ngoại lệ DuplicateTaxIdException), đảm bảo chỉ System Admin có quyền thực hiện các thao tác quản lý (kiểm tra quyền RBAC trước khi thực hiện thao tác), ghi log hành động quản lý trung tâm theo yêu cầu NFR-006.
#### 📝 Công việc con 5.3: Triển khai endpoint quản lý trung tâm
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/controller/CenterController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-004], [REQ-005], [ARC-002]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST: GET /api/centers (lấy danh sách tất cả trung tâm, công khai cho người dùng đã xác thực), POST /api/centers (tạo trung tâm mới, chỉ System Admin), PUT /api/centers/{centerId} (cập nhật trung tâm, chỉ System Admin), DELETE /api/centers/{centerId} (xóa trung tâm, chỉ System Admin), áp dụng xác thực JWT và kiểm tra quyền RBAC, trả về phản hồi JSON theo hợp đồng API đã định nghĩa, xử lý lỗi trùng taxId với mã lỗi 409 Conflict.
<!--START_API_CONTRACT-->
```json
// Endpoint quản lý trung tâm
GET /api/centers
Response 200: [
  { "centerId": "uuid", "name": "string", "address": "string", "taxId": "string", "contactPhone": "string", "contactEmail": "string" }
]

POST /api/centers
Request Body: { "name": "string", "address": "string", "taxId": "string", "contactPhone": "string", "contactEmail": "string" }
Response 201: { "centerId": "uuid" }
Response 409: { "error": "DUPLICATE_TAX_ID", "message": "Mã số thuế đã tồn tại" }

PUT /api/centers/{centerId}
Request Body: { "name": "string", "address": "string", "taxId": "string", "contactPhone": "string", "contactEmail": "string" }
Response 200: { "centerId": "uuid" }

DELETE /api/centers/{centerId}
Response 204: No Content

POST /api/centers/{centerId}/admins
Request Body: { "userId": "uuid" }
Response 200: { "message": "Phân quyền quản trị trung tâm thành công" }
```
<!--END_API_CONTRACT-->
#### 📝 Công việc con 5.4: Viết unit test cho chức năng quản lý trung tâm
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/center-service/src/main/java/org/nlh4j/membership_hub/center/service/CenterService.java;./sources/backend/center-service/src/test/java/com/hub/center/CenterServiceTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test đầy đủ cho các chức năng quản lý trung tâm, bao gồm trường hợp thành công, lỗi trùng mã số thuế, truy cập trái phép khi không có quyền System Admin, xác nhận dữ liệu trả về đúng định dạng, đảm bảo độ bao phủ mã >= 90%.

### 🌤️ NGÀY 6: <!--DAY_HEADER_START-->Triển khai lớp bảo mật RBAC và bộ lọc xác thực JWT<!--DAY_HEADER_END-->
#### 📝 Công việc con 6.1: Triển khai công cụ tạo và xác thực JWT token
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/util/JwtUtil.java
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai công cụ tạo access token (hết hạn 15 phút) và refresh token (hết hạn 7 ngày), xác thực token, kiểm tra thời hạn token, sử dụng thuật toán mã hóa HS256 với khóa bí mật được lưu trong biến môi trường, đảm bảo token không thể bị giả mạo, tuân thủ yêu cầu thời hạn token của NFR-003, thêm phương thức trích xuất thông tin người dùng và vai trò từ token.
#### 📝 Công việc con 6.2: Triển khai bộ lọc xác thực RBAC cho tất cả endpoint
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/filter/RbacFilter.java
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai bộ lọc JWT và RBAC toàn cục cho tất cả service vi mô, kiểm tra tính hợp lệ của access token trên mỗi yêu cầu (trích xuất token từ header Authorization, xác thực chữ ký và thời hạn), xác thực quyền truy cập của người dùng dựa trên vai trò và tài nguyên được yêu cầu, trả về lỗi 401 Unauthorized nếu token không hợp lệ/hết hạn, 403 Forbidden nếu người dùng không có quyền truy cập, tuân thủ ma trận RBAC đã định nghĩa, tích hợp với tất cả các endpoint của service auth và center.
#### 📝 Công việc con 6.3: Viết unit test cho bộ lọc RBAC
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/filter/RbacFilter.java;./sources/backend/auth-service/src/test/java/com/hub/auth/RbacFilterTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test cho bộ lọc RBAC, kiểm tra các trường hợp: token hợp lệ có quyền truy cập, token hết hạn, token không hợp lệ, người dùng có quyền truy cập, người dùng không có quyền truy cập, xác nhận phản hồi lỗi đúng định dạng và mã trạng thái HTTP, đảm bảo độ bao phủ mã >= 90%.
#### 📝 Công việc con 6.4: Cập nhật tài liệu đặc tả bảo mật và luồng xác thực
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/security-spec.md
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cập nhật tài liệu đặc tả bảo mật với mô tả chi tiết luồng xác thực, cấu trúc JWT token, chính sách phân quyền RBAC, các yêu cầu bảo mật tuân thủ OWASP Top 10 và NFR-003, bao gồm các biện pháp chống SQL injection, XSS, CSRF, mã hóa dữ liệu truyền và lưu trữ.

### 🌤️ NGÀY 7: <!--DAY_HEADER_START-->Xử lý ngoại lệ, kiểm thử tích hợp và hoàn thiện tài liệu giai đoạn<!--DAY_HEADER_END-->
#### 📝 Công việc con 7.1: Triển khai trình xử lý ngoại lệ toàn cục
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/exception/GlobalExceptionHandler.java
* **Thẻ truy xuất:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai trình xử lý ngoại lệ toàn cục cho tất cả service, chuẩn hóa cấu trúc phản hồi lỗi (mã lỗi, thông báo chi tiết, timestamp), xử lý các ngoại lệ nghiệp vụ (lỗi xác thực, lỗi phân quyền, lỗi trùng dữ liệu) và ngoại lệ hệ thống, ghi log lỗi theo yêu cầu [NFR-006] với đầy đủ thông tin ngữ cảnh, trả về mã trạng thái HTTP phù hợp, xử lý ngoại lệ [EXC-004] trả về danh sách chi tiết lỗi cho từng trường không hợp lệ.
<!--START_EXC_HANDLER-->
```java
// Trình xử lý ngoại lệ toàn cục cho ngoại lệ xác thực đầu vào [EXC-004]
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(MethodArgumentNotValidException ex) {
        List<String> details = ex.getBindingResult().getFieldErrors().stream()
                .map(error -> error.getField() + ": " + error.getDefaultMessage())
                .collect(Collectors.toList());
        ErrorResponse error = new ErrorResponse("VALIDATION_ERROR", "Dữ liệu đầu vào không hợp lệ", details, LocalDateTime.now());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }
}
```
<!--END_EXC_HANDLER-->
#### 📝 Công việc con 7.2: Thực hiện kiểm thử tích hợp giữa service auth và center
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/com/hub/auth/IntegrationAuthCenterTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện kiểm thử tích hợp toàn bộ luồng nghiệp vụ: đăng ký người dùng -> đăng nhập -> lấy JWT token -> truy cập danh sách trung tâm -> tạo trung tâm mới -> phân quyền Center Admin -> xác nhận quyền truy cập của Center Admin hoạt động đúng, không có lỗi trong toàn bộ luồng, sử dụng cơ sở dữ liệu thử nghiệm H2 và Testcontainers để mô phỏng môi trường production.
#### 📝 Công việc con 7.3: Rà soát toàn bộ mã nguồn giai đoạn
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/auth-service/src/main/java/org/nlh4j/membership_hub/auth/service/AuthService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-000], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [EXC-004]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát toàn bộ mã nguồn được tạo trong giai đoạn 1, kiểm tra tuân thủ chuẩn mã hóa doanh nghiệp, không có lỗ hổng bảo mật, hiệu năng đáp ứng yêu cầu NFR-001, đề xuất các cải tiến về cấu trúc mã và tối ưu hóa, đảm bảo không có code smell và lỗi SonarQube.
#### 📝 Công việc con 7.4: Hoàn thiện tài liệu giai đoạn 1
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/api-contracts-auth.md
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-000], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Hoàn thiện tài liệu hợp đồng API cho tất cả endpoint của service auth và center, cập nhật tài liệu kiến trúc tổng thể với cấu trúc dự án đã được khởi tạo, đảm bảo tài liệu đầy đủ, chính xác, dễ hiểu cho các đội phát triển các giai đoạn sau, bao gồm mô tả endpoint, schema request/response, mã lỗi, yêu cầu xác thực, quyền RBAC, ví dụ sử dụng thực tế.