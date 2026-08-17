# Giai đoạn 1: <!--PHASE_NAME_START-->Triển khai nền tảng quản lý người dùng, trung tâm và xác thực cốt lõi<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản thảo** | ARCH-20260817042313 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai nền tảng quản lý người dùng, trung tâm và xác thực cốt lõi<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai các module quản lý người dùng và trung tâm cốt lõi, hệ thống phân quyền RBAC, luồng xác thực OAuth2/JWT, schema cơ sở dữ liệu cho các thực thể cốt lõi, cùng tài liệu kiến trúc hệ thống nền tảng, tạo điều kiện cho việc triển khai các module chức năng khác trong các giai đoạn sau.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/08/17 04:23:13 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Triển khai nền tảng kiến trúc cốt lõi cho hệ thống membership-hub, bao gồm:
- Thiết lập schema cơ sở dữ liệu PostgreSQL đầy đủ cho tất cả thực thể cốt lõi (users, roles, centers, courses, enrollments, attendance, student_cards, notifications, promotions, announcements, system_settings) với các ràng buộc toàn vẹn dữ liệu và index tối ưu.
- Triển khai hệ thống xác thực người dùng hỗ trợ đăng ký email/mật khẩu và OAuth2 (Firebase, Google, Facebook) với JWT access token (15 phút) và refresh token (7 ngày).
- Triển khai hệ thống phân quyền RBAC với 5 vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student) và các quy tắc kiểm soát truy cập tương ứng.
- Triển khai API quản lý người dùng (đăng ký, đăng nhập, phân quyền) và quản lý trung tâm (CRUD, phân quyền quản trị trung tâm).
- Viết tài liệu kiến trúc tổng quan, hợp đồng API REST, sự kiện và hướng dẫn vận hành.
- Đảm bảo tuân thủ các yêu cầu phi chức năng về bảo mật (OWASP Top 10, mã hóa dữ liệu), hiệu suất (độ trễ API < 200ms) và logging/audit.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Backend Services:**
  * `./sources/backend/user-service/` [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001], [ARC-001], [ARC-006]
  * `./sources/backend/center-service/` [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]
- **Documentation:**
  * `./sources/docs/architecture/` [ARC-010], [DAT-ALL (1 to 11)], [ARC-001 to ARC-009]

- **API Endpoints (REST):**
  * `POST /api/v1/auth/register` [REQ-001]
  * `POST /api/v1/auth/login` [REQ-001]
  * `POST /api/v1/auth/oauth/{provider}` [REQ-002]
  * `PUT /api/v1/users/{userId}/role` [REQ-003]
  * `GET /api/v1/centers` [REQ-004]
  * `POST /api/v1/centers` [REQ-005]
  * `PUT /api/v1/centers/{centerId}` [REQ-005]
  * `DELETE /api/v1/centers/{centerId}` [REQ-005]
  * `POST /api/v1/centers/{centerId}/admins` [REQ-006]
  * `DELETE /api/v1/centers/{centerId}/admins/{userId}` [REQ-006]

- **Event Topics:**
  * `user.registered` [ARC-006]
  * `user.role.updated` [ARC-006]
  * `center.created` [ARC-007]
  * `center.admin.assigned` [ARC-007]

## 3. Chỉ thị chức năng chuyên biệt cho Đại lý phụ
- **Coder**: Thực hiện triển khai mã nguồn ứng dụng backend cho các service user-service và center-service, bao gồm logic xác thực, phân quyền RBAC, và các API CRUD. Bị cấm viết test suite hoặc infrastructure manifests.
- **Tester**: Chuyên về kỹ thuật test suite, validation và quality gates. Chịu trách nhiệm tạo unit test, integration test và performance validation scripts. Bị cấm sửa đổi mã nguồn production. Nếu phạm vi tích hợp không có file cụ thể, sử dụng token `INTEGRATION_SCOPE`.
- **Doc**: Làm việc như Principal Technical Writer và Enterprise Systems Architect. Chuyên biên soạn tài liệu Technical Specification, schema references, system blueprints. Mọi file tài liệu phải có đuôi `.md` và nằm trong `./sources/docs/`.
- **Reviewer**: Chịu trách nhiệm kiểm tra biên dịch, phân tích tĩnh, vá lỗi bảo mật OWASP và đảm bảo quality gate SonarQube.
- **Docker**: Chuyên về containerization, multi-stage Dockerfile và đẩy hình ảnh lên registry.
- **GCP**: Chuyên về tự động hóa đám mây GCP, quản lý artifact registry.
- **GKE**: Chuyên về orchestration container trên GKE, deployment manifests, HPA.

## 4. Định nghĩa Hoàn thành của Giai đoạn (DoD)
- Tất cả công việc giai đoạn 1 đã được triển khai và kiểm tra thành công.
- Tất cả thẻ theo dõi [REQ-001] đến [REQ-006], [EXC-004], [DAT-001] đến [DAT-011], [ARC-001] đến [ARC-010] đã được ánh xạ và bao phủ 100%.
- Độ phủ mã đạt >= 90% cho các lớp service và controller.
- Tất cả API endpoints hoạt động đúng theo hợp đồng đã định nghĩa.
- Hệ thống phân quyền RBAC hoạt động chính xác cho tất cả 5 vai trò.
- Luồng xác thực OAuth2/JWT hoạt động đúng với thời hạn token đã định.
- Tất cả ngoại lệ nghiệp vụ được xử lý đúng theo đặc tả.
- Tài liệu kiến trúc, API contracts và hướng dẫn vận hành được hoàn thiện đầy đủ.
- Không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) được phát hiện trong quá trình code review.
- Hình ảnh Docker được build thành công với kích thước < 500MB.

## 5. Nhật ký thực thi kiến trúc theo từng ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->Thiết lập cấu trúc dự án, schema cơ sở dữ liệu và xác thực cốt lõi<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Thiết lập cấu trúc dự án microservice và schema cơ sở dữ liệu cốt lõi
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/main/resources/db/migration/V1__init_core_schema.sql`; `./sources/backend/center-service/src/main/resources/db/migration/V1__init_core_schema.sql`; `./sources/docs/architecture/database-schema.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo cấu trúc thư mục microservice cho user-service và center-service theo chuẩn Quarkus, triển khai script migration Flyway cho tất cả các bảng cốt lõi (users, roles, centers, courses, enrollments, attendance, student_cards, notifications, promotions, announcements, system_settings) với cấu trúc cột, khóa chính/khóa ngoại, ràng buộc CHECK và index như đã định nghĩa trong đặc tả DDL của giai đoạn. Viết tài liệu mô tả schema cơ sở dữ liệu với sơ đồ ERD và giải thích các ràng buộc toàn vẹn dữ liệu.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:**
```sql
-- Tạo bảng vai trò người dùng [DAT-001]
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
    tax_id VARCHAR(13) NOT NULL UNIQUE CHECK (LENGTH(tax_id) BETWEEN 10 AND 13 AND tax_id NOT LIKE '%[^0-9]%'),
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
    teacher_id UUID REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
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
    code VARCHAR(50) UNIQUE,
    discount_percent SMALLINT NOT NULL CHECK (discount_percent BETWEEN 0 AND 100),
    start_date DATE,
    end_date DATE,
    description TEXT
);

-- Tạo bảng thông báo hệ thống [DAT-009]
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Tạo bảng cài đặt hệ thống [DAT-011]
CREATE TABLE system_settings (
    setting_key VARCHAR(50) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description VARCHAR(255)
);

-- Tạo index cho các truy vấn thường dùng [DAT-ALL]
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role_id ON users(role_id);
CREATE INDEX idx_centers_tax_id ON centers(tax_id);
CREATE INDEX idx_courses_teacher_id ON courses(teacher_id);
CREATE INDEX idx_enrollments_student_id ON enrollments(student_id);
CREATE INDEX idx_enrollments_course_id ON enrollments(course_id);
CREATE INDEX idx_attendance_student_course_date ON attendance(student_id, course_id, attendance_date);
CREATE INDEX idx_notifications_user_id ON notifications(user_id);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 2: Cấu hình RBAC và tích hợp xác thực JWT/OAuth2 cơ bản
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/main/java/com/membershiphub/auth/JwtAuthFilter.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/auth/OAuth2Handler.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/auth/RbacEnforcer.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai bộ lọc xác thực JWT để xác thực token trên mọi yêu cầu API, tích hợp OAuth2 với Firebase, Google, Facebook, cấu hình cơ chế refresh token với thời hạn 7 ngày, triển khai logic phân quyền dựa trên vai trò người dùng (RBAC) với các quy tắc: System Admin có toàn quyền trên tất cả trung tâm, Center Admin chỉ quản lý trung tâm của mình, Manager có thể tạo thông báo, quản lý học viên, xem danh sách khóa học, Teacher chỉ xem khóa học và lịch dạy của mình, Student chỉ duyệt khóa học và xem thẻ hội viên cá nhân.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  1. `POST /api/v1/auth/register` [REQ-001]: Đăng ký người dùng mới với email/mật khẩu, trả về JWT access token và refresh token. Request body: `{email, password, fullName}`. Response 201: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  2. `POST /api/v1/auth/login` [REQ-001]: Đăng nhập với email/mật khẩu, trả về JWT token. Request body: `{email, password}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  3. `POST /api/v1/auth/oauth/{provider}` [REQ-002]: Xác thực OAuth2 với nhà cung cấp (firebase/google/facebook). Request body: `{oauthCode}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  4. `PUT /api/v1/users/{userId}/role` [REQ-003]: Cập nhật vai trò người dùng. Request body: `{roleId}`. Response 200: `{userId, roleId, roleName}`.
  5. `GET /api/v1/centers` [REQ-004]: Lấy danh sách tất cả trung tâm. Response 200: `[{centerId, name, address, taxId, contactPhone, contactEmail}]`.
  6. `POST /api/v1/centers` [REQ-005]: Tạo trung tâm mới. Request body: `{name, address, taxId, contactPhone, contactEmail}`. Response 201: `{centerId, ...}`.
  7. `PUT /api/v1/centers/{centerId}` [REQ-005]: Cập nhật thông tin trung tâm. Request body: `{name, address, contactPhone, contactEmail}`. Response 200: `{centerId, ...}`.
  8. `DELETE /api/v1/centers/{centerId}` [REQ-005]: Xóa trung tâm. Response 204 No Content.
  9. `POST /api/v1/centers/{centerId}/admins` [REQ-006]: Gán quyền quản trị viên cho trung tâm. Request body: `{userId}`. Response 200: `{userId, centerId, role: 'CENTER_ADMIN'}`.
  10. `DELETE /api/v1/centers/{centerId}/admins/{userId}` [REQ-006]: Thu hồi quyền quản trị viên trung tâm. Response 204 No Content.

  **Hợp đồng sự kiện (Message Broker):**
  - `user.registered` [ARC-006]: Kích hoạt khi người dùng đăng ký thành công, payload: `{userId, email, role, provider}`.
  - `user.role.updated` [ARC-006]: Kích hoạt khi vai trò người dùng thay đổi, payload: `{userId, oldRole, newRole, updatedBy}`.
  - `center.created` [ARC-007]: Kích hoạt khi trung tâm mới được tạo, payload: `{centerId, name, taxId, createdBy}`.
  - `center.admin.assigned` [ARC-007]: Kích hoạt khi quản trị viên trung tâm được gán/thu hồi, payload: `{userId, centerId, action: 'ASSIGN'|'UNASSIGN', assignedBy}`.

* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 3: Viết tài liệu kiến trúc tổng quan hệ thống
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/system-overview.md`; `./sources/docs/architecture/auth-flow.md`; `./sources/docs/architecture/rbac-matrix.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [ARC-001], [ARC-006], [ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu kiến trúc tổng quan hệ thống mô tả kiến trúc microservice, luồng dữ liệu chính (xác thực, điểm danh QR, thông báo), ma trận RBAC chi tiết cho 5 vai trò người dùng, tích hợp các dịch vụ bên thứ ba (Firebase Authentication, FCM/APNs, Zalo API, Redis caching). Viết tài liệu mô tả luồng xác thực OAuth2/JWT, luồng xử lý điểm danh QR idempotent, luồng gửi thông báo đa kênh.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->Triển khai chức năng đăng ký, xác thực người dùng và xác thực mạng xã hội<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai logic đăng ký và đăng nhập người dùng
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserService.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserDTO.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserController.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-001], [EXC-004]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai logic đăng ký người dùng với email/mật khẩu, xác thực đầu vào (định dạng email hợp lệ, mật khẩu có ít nhất 8 ký tự bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt), mã hóa mật khẩu bằng bcrypt, tạo bản ghi người dùng mặc định với vai trò Student, trả về JWT token sau khi đăng ký thành công. Triển khai logic đăng nhập với email/mật khẩu, xác thực thông tin và cấp token.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  1. `POST /api/v1/auth/register` [REQ-001]: Đăng ký người dùng mới với email/mật khẩu, trả về JWT access token và refresh token. Request body: `{email, password, fullName}`. Response 201: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  2. `POST /api/v1/auth/login` [REQ-001]: Đăng nhập với email/mật khẩu, trả về JWT token. Request body: `{email, password}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.

  **Hợp đồng sự kiện (Message Broker):**
  - `user.registered` [ARC-006]: Kích hoạt khi người dùng đăng ký thành công, payload: `{userId, email, role, provider}`.

* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:**
  1. [EXC-004] Lỗi xác thực đầu vào: Khi người dùng gửi form đăng ký/đăng nhập với dữ liệu không hợp lệ (email sai định dạng, mật khẩu yếu, thiếu trường bắt buộc), hệ thống trả về mã lỗi 400 Bad Request với thông báo chi tiết từng trường lỗi, ví dụ: `{"errors": [{"field": "email", "message": "Định dạng email không hợp lệ"}, {"field": "password", "message": "Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường và số"}]}`. Áp dụng cho tất cả các endpoint đăng ký và đăng nhập [REQ-001], [REQ-002].

#### 📝 Phụ công việc 2: Triển khai xác thực người dùng qua mạng xã hội
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/main/java/com/membershiphub/auth/OAuth2Service.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tích hợp OAuth2 với Firebase, Google, Facebook, xử lý mã xác thực từ nhà cung cấp, lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ, cấp JWT token sau khi xác thực thành công. Lưu trữ thông tin nhà cung cấp xác thực vào trường provider của bảng users.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  3. `POST /api/v1/auth/oauth/{provider}` [REQ-002]: Xác thực OAuth2 với nhà cung cấp (firebase/google/facebook). Request body: `{oauthCode}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.

  **Hợp đồng sự kiện (Message Broker):**
  - `user.registered` [ARC-006]: Kích hoạt khi người dùng đăng ký thành công, payload: `{userId, email, role, provider}`.

* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:**
  4. Lỗi xác thực OAuth2 thất bại: Khi mã xác thực từ nhà cung cấp OAuth2 không hợp lệ hoặc đã hết hạn, hệ thống trả về mã lỗi 401 Unauthorized với thông báo "Mã xác thực không hợp lệ hoặc đã hết hạn" [REQ-002].

#### 📝 Phụ công việc 3: Viết unit test cho chức năng xác thực người dùng
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/main/java/com/membershiphub/auth/AuthService.java;./sources/backend/user-service/src/test/java/com/membershiphub/auth/AuthServiceTest.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserService.java;./sources/backend/user-service/src/test/java/com/membershiphub/user/UserServiceTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-001], [REQ-002], [EXC-004]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: đăng ký thành công với email/mật khẩu hợp lệ, đăng ký thất bại với email đã tồn tại, đăng nhập thành công với thông tin hợp lệ, đăng nhập thất bại với mật khẩu sai, xác thực OAuth2 thành công với Google/Facebook, xác thực thất bại với mã không hợp lệ. Đảm bảo độ phủ mã ít nhất 90% cho các lớp xử lý xác thực.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 3: <!--DAY_HEADER_START-->Triển khai API quản lý vai trò người dùng và quản lý trung tâm cơ bản<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai API quản lý vai trò người dùng
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/main/java/com/membershiphub/user/RoleController.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/user/RoleService.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-003], [ARC-001], [ARC-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `PUT /api/v1/users/{userId}/role` để cập nhật vai trò người dùng, kiểm tra quyền của người thực hiện thao tác (chỉ System Admin được phép thay đổi vai trò), cập nhật cột role_id trong bảng users, áp dụng quyền truy cập mới ngay lập tức.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  4. `PUT /api/v1/users/{userId}/role` [REQ-003]: Cập nhật vai trò người dùng. Request body: `{roleId}`. Response 200: `{userId, roleId, roleName}`.

  **Hợp đồng sự kiện (Message Broker):**
  - `user.role.updated` [ARC-006]: Kích hoạt khi vai trò người dùng thay đổi, payload: `{userId, oldRole, newRole, updatedBy}`.

* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:**
  3. Lỗi phân quyền không hợp lệ: Khi người dùng không có quyền thực hiện thao tác (ví dụ: người dùng thường cố gắng xóa trung tâm), hệ thống trả về mã lỗi 403 Forbidden với thông báo "Bạn không có quyền thực hiện thao tác này" [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005].

#### 📝 Phụ công việc 2: Triển khai API quản lý trung tâm (CRUD)
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterController.java`; `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterService.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-004], [REQ-005], [ARC-002]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai các API CRUD cho trung tâm: `GET /api/v1/centers` (lấy danh sách trung tâm với địa chỉ, mã số thuế, thông tin liên hệ quản trị), `POST /api/v1/centers` (tạo trung tâm mới), `PUT /api/v1/centers/{centerId}` (cập nhật thông tin trung tâm), `DELETE /api/v1/centers/{centerId}` (xóa trung tâm). Kiểm tra tính duy nhất của mã số thuế khi tạo hoặc cập nhật trung tâm.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  5. `GET /api/v1/centers` [REQ-004]: Lấy danh sách tất cả trung tâm. Response 200: `[{centerId, name, address, taxId, contactPhone, contactEmail}]`.
  6. `POST /api/v1/centers` [REQ-005]: Tạo trung tâm mới. Request body: `{name, address, taxId, contactPhone, contactEmail}`. Response 201: `{centerId, ...}`.
  7. `PUT /api/v1/centers/{centerId}` [REQ-005]: Cập nhật thông tin trung tâm. Request body: `{name, address, contactPhone, contactEmail}`. Response 200: `{centerId, ...}`.
  8. `DELETE /api/v1/centers/{centerId}` [REQ-005]: Xóa trung tâm. Response 204 No Content.

  **Hợp đồng sự kiện (Message Broker):**
  - `center.created` [ARC-007]: Kích hoạt khi trung tâm mới được tạo, payload: `{centerId, name, taxId, createdBy}`.
  - `center.updated` [ARC-007]: Kích hoạt khi thông tin trung tâm thay đổi, payload: `{centerId, updatedFields}`.

* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:**
  2. Lỗi trùng lặp mã số thuế trung tâm: Khi tạo hoặc cập nhật trung tâm với mã số thuế đã tồn tại, hệ thống trả về mã lỗi 409 Conflict với thông báo "Mã số thuế đã được sử dụng bởi trung tâm khác" [REQ-005].

#### 📝 Phụ công việc 3: Viết unit test cho API quản lý vai trò và trung tâm
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/main/java/com/membershiphub/user/RoleController.java;./sources/backend/user-service/src/test/java/com/membershiphub/user/RoleControllerTest.java`; `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterController.java;./sources/backend/center-service/src/test/java/com/membershiphub/center/CenterControllerTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-003], [REQ-004], [REQ-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test và integration test cho các endpoint quản lý vai trò và trung tâm, bao gồm các trường hợp thành công, lỗi phân quyền, lỗi trùng lặp mã số thuế, lỗi không tìm thấy tài nguyên. Đảm bảo độ phủ mã ít nhất 90% cho các lớp controller và service tương ứng.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 4: <!--DAY_HEADER_START-->Triển khai phân quyền quản trị trung tâm và tích hợp xác thực toàn hệ thống<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai API phân quyền quản trị trung tâm
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterAdminController.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-006], [ARC-002]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `POST /api/v1/centers/{centerId}/admins` để gán quyền quản trị viên cho trung tâm cho người dùng được chọn, cập nhật vai trò người dùng thành 'CENTER_ADMIN' và lưu liên kết trung tâm. Triển khai API `DELETE /api/v1/centers/{centerId}/admins/{userId}` để thu hồi quyền quản trị viên, đặt lại vai trò người dùng về 'Student' và xóa liên kết trung tâm.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  9. `POST /api/v1/centers/{centerId}/admins` [REQ-006]: Gán quyền quản trị viên cho trung tâm. Request body: `{userId}`. Response 200: `{userId, centerId, role: 'CENTER_ADMIN'}`.
  10. `DELETE /api/v1/centers/{centerId}/admins/{userId}` [REQ-006]: Thu hồi quyền quản trị viên trung tâm. Response 204 No Content.

  **Hợp đồng sự kiện (Message Broker):**
  - `center.admin.assigned` [ARC-007]: Kích hoạt khi quản trị viên trung tâm được gán/thu hồi, payload: `{userId, centerId, action: 'ASSIGN'|'UNASSIGN', assignedBy}`.

* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:**
  3. Lỗi phân quyền không hợp lệ: Khi người dùng không có quyền thực hiện thao tác (ví dụ: người dùng thường cố gắng xóa trung tâm), hệ thống trả về mã lỗi 403 Forbidden với thông báo "Bạn không có quyền thực hiện thao tác này" [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005].

#### 📝 Phụ công việc 2: Tích hợp và kiểm tra luồng xác thực toàn hệ thống
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/src/test/java/com/membershiphub/auth/AuthIntegrationTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-006], [REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra tích hợp toàn bộ luồng xác thực: đăng ký người dùng mới -> đăng nhập với email/mật khẩu -> đăng nhập với OAuth2 Google/Facebook -> sử dụng JWT token truy cập các endpoint được bảo vệ -> kiểm tra refresh token hoạt động đúng khi access token hết hạn. Kiểm tra logic phân quyền RBAC hoạt động đúng với từng vai trò người dùng.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Xử lý lỗi khi JWT token không hợp lệ hoặc hết hạn, trả về mã lỗi 401 Unauthorized với thông báo "Token xác thực không hợp lệ hoặc đã hết hạn".

#### 📝 Phụ công việc 3: Xây dựng Dockerfile đa giai đoạn cho service backend
##### Đại lý phụ được giao: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/Dockerfile`; `./sources/backend/center-service/Dockerfile`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Xây dựng Dockerfile đa giai đoạn cho user-service và center-service, sử dụng base image JDK 21 slim, tối ưu kích thước hình ảnh dưới 200MB, cấu hình biến môi trường cho kết nối cơ sở dữ liệu, cổng ứng dụng và cấu hình xác thực.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 5: <!--DAY_HEADER_START-->Viết integration test và kiểm tra chất lượng mã nguồn<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Viết integration test cho luồng chức năng người dùng và trung tâm
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `INTEGRATION_SCOPE;./sources/backend/user-service/src/test/java/com/membershiphub/user/UserIntegrationTest.java`; `INTEGRATION_SCOPE;./sources/backend/center-service/src/test/java/com/membershiphub/center/CenterIntegrationTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết integration test cho các luồng: đăng ký người dùng -> đăng nhập -> cập nhật vai trò -> gán quyền quản trị trung tâm -> quản lý thông tin trung tâm. Kiểm tra tính toàn vẹn dữ liệu, ràng buộc khóa ngoại, logic phân quyền hoạt động đúng. Đảm bảo độ phủ tích hợp ít nhất 85%.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 2: Kiểm tra chất lượng mã và sửa lỗi
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/`; `./sources/backend/center-service/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [EXC-004], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho tất cả các mã nguồn của user-service và center-service, phát hiện lỗi cú pháp, lỗi logic, điểm nghẽn hiệu suất, vi phạm chuẩn mã hóa, đề xuất và thực hiện sửa lỗi. Đảm bảo mã nguồn tuân thủ chuẩn Quarkus và Java 21, không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) [NFR-003].

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 6: <!--DAY_HEADER_START-->Viết tài liệu kiến trúc và hợp đồng hệ thống<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Viết tài liệu hợp đồng API REST và sự kiện
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/api-contracts.md`; `./sources/docs/architecture/event-contracts.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho tất cả các endpoint của user-service và center-service, bao gồm phương thức HTTP, đường dẫn, schema request/response, mã lỗi, ví dụ sử dụng. Viết tài liệu hợp đồng sự kiện cho các topic message broker, bao gồm tên topic, schema payload, mô tả sự kiện.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  1. `POST /api/v1/auth/register` [REQ-001]: Đăng ký người dùng mới với email/mật khẩu, trả về JWT access token và refresh token. Request body: `{email, password, fullName}`. Response 201: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  2. `POST /api/v1/auth/login` [REQ-001]: Đăng nhập với email/mật khẩu, trả về JWT token. Request body: `{email, password}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  3. `POST /api/v1/auth/oauth/{provider}` [REQ-002]: Xác thực OAuth2 với nhà cung cấp (firebase/google/facebook). Request body: `{oauthCode}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  4. `PUT /api/v1/users/{userId}/role` [REQ-003]: Cập nhật vai trò người dùng. Request body: `{roleId}`. Response 200: `{userId, roleId, roleName}`.
  5. `GET /api/v1/centers` [REQ-004]: Lấy danh sách tất cả trung tâm. Response 200: `[{centerId, name, address, taxId, contactPhone, contactEmail}]`.
  6. `POST /api/v1/centers` [REQ-005]: Tạo trung tâm mới. Request body: `{name, address, taxId, contactPhone, contactEmail}`. Response 201: `{centerId, ...}`.
  7. `PUT /api/v1/centers/{centerId}` [REQ-005]: Cập nhật thông tin trung tâm. Request body: `{name, address, contactPhone, contactEmail}`. Response 200: `{centerId, ...}`.
  8. `DELETE /api/v1/centers/{centerId}` [REQ-005]: Xóa trung tâm. Response 204 No Content.
  9. `POST /api/v1/centers/{centerId}/admins` [REQ-006]: Gán quyền quản trị viên cho trung tâm. Request body: `{userId}`. Response 200: `{userId, centerId, role: 'CENTER_ADMIN'}`.
  10. `DELETE /api/v1/centers/{centerId}/admins/{userId}` [REQ-006]: Thu hồi quyền quản trị viên trung tâm. Response 204 No Content.

  **Hợp đồng sự kiện (Message Broker):**
  - `user.registered` [ARC-006]: Kích hoạt khi người dùng đăng ký thành công, payload: `{userId, email, role, provider}`.
  - `user.role.updated` [ARC-006]: Kích hoạt khi vai trò người dùng thay đổi, payload: `{userId, oldRole, newRole, updatedBy}`.
  - `center.created` [ARC-007]: Kích hoạt khi trung tâm mới được tạo, payload: `{centerId, name, taxId, createdBy}`.
  - `center.admin.assigned` [ARC-007]: Kích hoạt khi quản trị viên trung tâm được gán/thu hồi, payload: `{userId, centerId, action: 'ASSIGN'|'UNASSIGN', assignedBy}`.

* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 2: Viết tài liệu hướng dẫn vận hành và tuân thủ
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/operational-guide.md`; `./sources/docs/architecture/compliance.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [NFR-006], [NFR-008]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn vận hành các service backend, bao gồm cách khởi chạy, cấu hình môi trường, giám sát, xử lý sự cố. Viết tài liệu tuân thủ RBAC, OWASP Top 10, GDPR/CCPA liên quan đến module quản lý người dùng và trung tâm, bao gồm quy trình xóa dữ liệu người dùng khi có yêu cầu, quy trình xuất dữ liệu người dùng dưới dạng JSON.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 7: <!--DAY_HEADER_START-->Kiểm tra cuối cùng, tối ưu và đóng gói sản phẩm giai đoạn<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Kiểm tra bảo mật và tối ưu hiệu suất
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/user-service/`; `./sources/backend/center-service/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra bảo mật toàn diện cho các service: kiểm tra lỗi SQL injection, XSS, CSRF, kiểm tra cấu hình mã hóa mật khẩu bcrypt, kiểm tra cơ chế hết hạn JWT token, kiểm tra logic phân quyền RBAC không có lỗ hổng. Tối ưu truy vấn cơ sở dữ liệu, đảm bảo độ trễ API trung bình dưới 200ms [NFR-001]. Kiểm tra cấu hình logging ghi lại tất cả hành động người dùng (thay đổi vai trò, quản lý trung tâm) với timestamp, user ID và chi tiết hành động, đảm bảo log được lưu trữ 1 năm [NFR-006].

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 2: Hoàn thiện tài liệu và đẩy hình ảnh Docker
##### Đại lý phụ được giao: Doc, Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/`; `./sources/backend/user-service/Dockerfile`; `./sources/backend/center-service/Dockerfile`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [NFR-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Hoàn thiện tất cả tài liệu kiến trúc, đảm bảo tài liệu đầy đủ, chính xác, phù hợp với triển khai thực tế. Xây dựng và đẩy hình ảnh Docker cho user-service và center-service lên registry mục tiêu, đảm bảo kích thước hình ảnh dưới 500MB [NFR-005].

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 3: Kiểm tra cuối cùng và xác nhận hoàn thành giai đoạn
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** Toàn bộ mã nguồn và tài liệu của giai đoạn 1
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [EXC-004], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra cuối cùng toàn bộ sản phẩm của giai đoạn 1, đảm bảo tất cả các yêu cầu và thẻ theo dõi đã được triển khai đầy đủ, không có lỗi còn tồn tại, xác nhận giai đoạn sẵn sàng cho giai đoạn tiếp theo.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]