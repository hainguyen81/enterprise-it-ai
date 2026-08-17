# Giai đoạn 1: Thiết lập cơ sở hạ tầng lõi và xác thực

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID bản thiết kế** | ARCH-20260817193854 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Thiết lập cơ sở hạ tầng lõi và xác thực<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc thiết lập cơ sở hạ tầng lõi và xác thực cho hệ thống. Chúng ta sẽ xây dựng các chức năng đăng ký người dùng, xác thực qua email và mật khẩu, đăng nhập qua Firebase, Google, Facebook, và quản lý vai trò người dùng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/17 19:38:54 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc thiết lập cơ sở hạ tầng lõi và xác thực cho hệ thống. Chúng ta sẽ xây dựng các chức năng đăng ký người dùng, xác thực qua email và mật khẩu, đăng nhập qua Firebase, Google, Facebook, và quản lý vai trò người dùng.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/auth/`
- `./sources/backend/user/`

## 3. Hướng dẫn chức năng của các chuyên gia con được chỉ định
*   **Coder**: Hoạt động như một Nhà phát triển ứng dụng cấp cao/Chủ tịch. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Trưởng/QC/QA cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con tác vụ liên quan đến phạm vi tích hợp hoặc kết thúc-to-end tổng thể nơi không có tệp mã cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh trình biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về việc đóng gói, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các chức năng đăng ký người dùng, xác thực qua email và mật khẩu, đăng nhập qua Firebase, Google, Facebook.
- Hoàn thành 100% các chức năng quản lý vai trò người dùng.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% các bộ kiểm thử chức năng và tích hợp.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc hàng ngày

### 🌤️ NGÀY 1: Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu

#### 📝 NHIỆM VỤ CON 1.1: Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/auth/src/main/java/org/nlh4j/membership_hub/auth/AuthService.java

* **TagID mục tiêu:** [REQ-001]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đăng ký người dùng với xác thực email và mật khẩu. Chức năng này sẽ kiểm tra tính hợp lệ của email và mật khẩu, mã hóa mật khẩu trước khi lưu vào cơ sở dữ liệu, và trả về một JWT token sau khi đăng ký thành công.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT REFERENCES roles(role_id),
    provider VARCHAR(20) DEFAULT 'local',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/auth/register",
      "method": "POST",
      "request": {
        "email": "string",
        "password": "string",
        "full_name": "string"
      },
      "response": {
        "user_id": "UUID",
        "token": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(DuplicateEmailException.class)
public ResponseEntity<ErrorResponse> handleDuplicateEmail(DuplicateEmailException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Email already exists", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.CONFLICT);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.2: Viết kiểm thử cho chức năng đăng ký người dùng
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/auth/src/main/java/org/nlh4j/membership_hub/auth/AuthService.java;./sources/backend/auth/src/test/java/org/nlh4j/membership_hub/auth/AuthTest.java

* **TagID mục tiêu:** [REQ-001]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đăng ký người dùng với xác thực email và mật khẩu. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của email và mật khẩu, và kiểm tra tính duy nhất của email.

#### 📝 NHIỆM VỤ CON 1.3: Tài liệu chức năng đăng ký người dùng
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/auth.md

* **TagID mục tiêu:** [REQ-001]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đăng ký người dùng với xác thực email và mật khẩu. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

### 🌤️ NGÀY 2: Xây dựng chức năng đăng nhập qua Firebase, Google, Facebook

#### 📝 NHIỆM VỤ CON 2.1: Xây dựng chức năng đăng nhập qua Firebase, Google, Facebook
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/auth/src/main/java/org/nlh4j/membership_hub/auth/SocialAuthService.java

* **TagID mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đăng nhập qua Firebase, Google, Facebook. Chức năng này sẽ xử lý mã token từ các nhà cung cấp xã hội, xác thực thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ, và phát hành một JWT token.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE social_accounts (
    social_id VARCHAR(255) PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    provider VARCHAR(20) NOT NULL,
    provider_user_id VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/auth/social-login",
      "method": "POST",
      "request": {
        "provider": "string",
        "token": "string"
      },
      "response": {
        "user_id": "UUID",
        "token": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidSocialTokenException.class)
public ResponseEntity<ErrorResponse> handleInvalidSocialToken(InvalidSocialTokenException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid social token", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.UNAUTHORIZED);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.2: Viết kiểm thử cho chức năng đăng nhập qua Firebase, Google, Facebook
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/auth/src/main/java/org/nlh4j/membership_hub/auth/SocialAuthService.java;./sources/backend/auth/src/test/java/org/nlh4j/membership_hub/auth/SocialAuthTest.java

* **TagID mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đăng nhập qua Firebase, Google, Facebook. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của mã token, và kiểm tra tính duy nhất của tài khoản xã hội.

#### 📝 NHIỆM VỤ CON 2.3: Tài liệu chức năng đăng nhập qua Firebase, Google, Facebook
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/auth.md

* **TagID mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đăng nhập qua Firebase, Google, Facebook. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

### 🌤️ NGÀY 3: Xây dựng chức năng gán và thay đổi vai trò người dùng

#### 📝 NHIỆM VỤ CON 3.1: Xây dựng chức năng gán và thay đổi vai trò người dùng
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/user/src/main/java/org/nlh4j/membership_hub/user/UserRoleService.java

* **TagID mục tiêu:** [REQ-003]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gán và thay đổi vai trò người dùng. Chức năng này sẽ cho phép quản trị viên gán hoặc thay đổi vai trò của người dùng (System Admin, Center Admin, Manager, Teacher, Student).

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    description VARCHAR(200)
);

INSERT INTO roles (role_id, name, description) VALUES
(1, 'System Admin', 'Global super-user'),
(2, 'Center Admin', 'Center-level manager'),
(3, 'Manager', 'Sub-admin with limited rights'),
(4, 'Teacher', 'Read-only course schedule'),
(5, 'Student', 'Course browsing, enrollment, card view');
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/users/{userId}/role",
      "method": "PUT",
      "request": {
        "role_id": "integer"
      },
      "response": {
        "user_id": "UUID",
        "role_id": "integer"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidRoleException.class)
public ResponseEntity<ErrorResponse> handleInvalidRole(InvalidRoleException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid role", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 3.2: Viết kiểm thử cho chức năng gán và thay đổi vai trò người dùng
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/user/src/main/java/org/nlh4j/membership_hub/user/UserRoleService.java;./sources/backend/user/src/test/java/org/nlh4j/membership_hub/user/UserRoleTest.java

* **TagID mục tiêu:** [REQ-003]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gán và thay đổi vai trò người dùng. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của vai trò, và kiểm tra quyền truy cập của người dùng sau khi thay đổi vai trò.

#### 📝 NHIỆM VỤ CON 3.3: Tài liệu chức năng gán và thay đổi vai trò người dùng
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/user.md

* **TagID mục tiêu:** [REQ-003]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gán và thay đổi vai trò người dùng. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.