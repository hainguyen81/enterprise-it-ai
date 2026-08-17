# Quản lý trung tâm và khóa học <!--PHASE_NAME_START-->Quản lý trung tâm và khóa học<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID bản thiết kế** | ARCH-20260817193854 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Quản lý trung tâm và khóa học<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc quản lý trung tâm và khóa học. Chúng ta sẽ xây dựng các chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm, xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học, và đăng ký khóa học cho học viên.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/17 19:38:54 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc quản lý trung tâm và khóa học. Chúng ta sẽ xây dựng các chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm, xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học, và đăng ký khóa học cho học viên.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/center/`
- `./sources/backend/course/`
- `./sources/backend/enrollment/`

## 3. Hướng dẫn chức năng của các chuyên gia con được chỉ định
*   **Coder**: Hoạt động như một Nhà phát triển ứng dụng cấp cao/Chủ tịch. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Trưởng/QC/QA cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con tác vụ liên quan đến phạm vi tích hợp hoặc kết thúc-to-end tổng thể nơi không có tệp mã cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh trình biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về việc đóng gói, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm.
- Hoàn thành 100% các chức năng xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học.
- Hoàn thành 100% các chức năng đăng ký khóa học cho học viên.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% các bộ kiểm thử chức năng và tích hợp.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc hàng ngày

### 🌤️ NGÀY 1: Xây dựng chức năng xem danh sách trung tâm, thêm, sửa, xóa trung tâm

#### 📝 NHIỆM VỤ CON 1.1: Xây dựng chức năng xem danh sách trung tâm
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/center/src/main/java/org/nlh4j/membership_hub/center/CenterService.java

* **TagID mục tiêu:** [REQ-004]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem danh sách trung tâm. Chức năng này sẽ trả về danh sách các trung tâm với các thông tin như tên, địa chỉ, mã số thuế, và thông tin liên hệ.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) UNIQUE NOT NULL,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
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
      "path": "/api/centers",
      "method": "GET",
      "response": {
        "centers": [
          {
            "center_id": "UUID",
            "name": "string",
            "address": "string",
            "tax_id": "string",
            "contact_phone": "string",
            "contact_email": "string"
          }
        ]
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(NoCentersFoundException.class)
public ResponseEntity<ErrorResponse> handleNoCentersFound(NoCentersFoundException ex) {
    ErrorResponse errorResponse = new ErrorResponse("No centers found", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.NOT_FOUND);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.2: Viết kiểm thử cho chức năng xem danh sách trung tâm
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/center/src/main/java/org/nlh4j/membership_hub/center/CenterService.java;./sources/backend/center/src/test/java/org/nlh4j/membership_hub/center/CenterTest.java

* **TagID mục tiêu:** [REQ-004]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem danh sách trung tâm. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 1.3: Tài liệu chức năng xem danh sách trung tâm
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/center.md

* **TagID mục tiêu:** [REQ-004]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem danh sách trung tâm. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 1.4: Xây dựng chức năng thêm, sửa, xóa trung tâm
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/center/src/main/java/org/nlh4j/membership_hub/center/CenterService.java

* **TagID mục tiêu:** [REQ-005]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng thêm, sửa, xóa trung tâm. Chức năng này sẽ cho phép quản trị viên thêm, sửa, hoặc xóa thông tin trung tâm.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) UNIQUE NOT NULL,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
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
      "path": "/api/centers",
      "method": "POST",
      "request": {
        "name": "string",
        "address": "string",
        "tax_id": "string",
        "contact_phone": "string",
        "contact_email": "string"
      },
      "response": {
        "center_id": "UUID",
        "status": "string"
      }
    },
    {
      "path": "/api/centers/{centerId}",
      "method": "PUT",
      "request": {
        "name": "string",
        "address": "string",
        "tax_id": "string",
        "contact_phone": "string",
        "contact_email": "string"
      },
      "response": {
        "center_id": "UUID",
        "status": "string"
      }
    },
    {
      "path": "/api/centers/{centerId}",
      "method": "DELETE",
      "response": {
        "center_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(DuplicateTaxIdException.class)
public ResponseEntity<ErrorResponse> handleDuplicateTaxId(DuplicateTaxIdException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Tax ID already exists", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.CONFLICT);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.5: Viết kiểm thử cho chức năng thêm, sửa, xóa trung tâm
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/center/src/main/java/org/nlh4j/membership_hub/center/CenterService.java;./sources/backend/center/src/test/java/org/nlh4j/membership_hub/center/CenterTest.java

* **TagID mục tiêu:** [REQ-005]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng thêm, sửa, xóa trung tâm. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 1.6: Tài liệu chức năng thêm, sửa, xóa trung tâm
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/center.md

* **TagID mục tiêu:** [REQ-005]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng thêm, sửa, xóa trung tâm. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 1.7: Xây dựng chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/center/src/main/java/org/nlh4j/membership_hub/center/CenterAdminService.java

* **TagID mục tiêu:** [REQ-006]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể. Chức năng này sẽ cho phép quản trị viên hệ thống gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE center_admins (
    center_admin_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    center_id UUID REFERENCES centers(center_id),
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
      "path": "/api/centers/{centerId}/admins",
      "method": "POST",
      "request": {
        "user_id": "UUID"
      },
      "response": {
        "center_admin_id": "UUID",
        "status": "string"
      }
    },
    {
      "path": "/api/centers/{centerId}/admins/{userId}",
      "method": "DELETE",
      "response": {
        "center_admin_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidCenterAdminException.class)
public ResponseEntity<ErrorResponse> handleInvalidCenterAdmin(InvalidCenterAdminException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid center admin", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.8: Viết kiểm thử cho chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/center/src/main/java/org/nlh4j/membership_hub/center/CenterAdminService.java;./sources/backend/center/src/test/java/org/nlh4j/membership_hub/center/CenterAdminTest.java

* **TagID mục tiêu:** [REQ-006]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 1.9: Tài liệu chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/center.md

* **TagID mục tiêu:** [REQ-006]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gán hoặc hủy gán người dùng làm quản trị viên trung tâm cho một trung tâm cụ thể. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

### 🌤️ NGÀY 2: Xây dựng chức năng xem danh sách khóa học, thêm, sửa, xóa khóa học, gán giáo viên cho khóa học

#### 📝 NHIỆM VỤ CON 2.1: Xây dựng chức năng xem danh sách khóa học
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/course/src/main/java/org/nlh4j/membership_hub/course/CourseService.java

* **TagID mục tiêu:** [REQ-007]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem danh sách khóa học. Chức năng này sẽ trả về danh sách các khóa học với các thông tin như tên, mô tả, ngày bắt đầu, ngày kết thúc, và giáo viên phụ trách.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID REFERENCES users(user_id),
    max_students INT DEFAULT 30,
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
      "path": "/api/courses",
      "method": "GET",
      "response": {
        "courses": [
          {
            "course_id": "UUID",
            "title": "string",
            "description": "string",
            "start_date": "date",
            "end_date": "date",
            "teacher_id": "UUID",
            "max_students": "integer"
          }
        ]
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(NoCoursesFoundException.class)
public ResponseEntity<ErrorResponse> handleNoCoursesFound(NoCoursesFoundException ex) {
    ErrorResponse errorResponse = new ErrorResponse("No courses found", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.NOT_FOUND);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.2: Viết kiểm thử cho chức năng xem danh sách khóa học
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/course/src/main/java/org/nlh4j/membership_hub/course/CourseService.java;./sources/backend/course/src/test/java/org/nlh4j/membership_hub/course/CourseTest.java

* **TagID mục tiêu:** [REQ-007]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem danh sách khóa học. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 2.3: Tài liệu chức năng xem danh sách khóa học
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/course.md

* **TagID mục tiêu:** [REQ-007]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem danh sách khóa học. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 2.4: Xây dựng chức năng thêm, sửa, xóa khóa học
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/course/src/main/java/org/nlh4j/membership_hub/course/CourseService.java

* **TagID mục tiêu:** [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng thêm, sửa, xóa khóa học. Chức năng này sẽ cho phép quản trị viên thêm, sửa, hoặc xóa thông tin khóa học.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID REFERENCES users(user_id),
    max_students INT DEFAULT 30,
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
      "path": "/api/courses",
      "method": "POST",
      "request": {
        "title": "string",
        "description": "string",
        "start_date": "date",
        "end_date": "date",
        "teacher_id": "UUID",
        "max_students": "integer"
      },
      "response": {
        "course_id": "UUID",
        "status": "string"
      }
    },
    {
      "path": "/api/courses/{courseId}",
      "method": "PUT",
      "request": {
        "title": "string",
        "description": "string",
        "start_date": "date",
        "end_date": "date",
        "teacher_id": "UUID",
        "max_students": "integer"
      },
      "response": {
        "course_id": "UUID",
        "status": "string"
      }
    },
    {
      "path": "/api/courses/{courseId}",
      "method": "DELETE",
      "response": {
        "course_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidCourseDateException.class)
public ResponseEntity<ErrorResponse> handleInvalidCourseDate(InvalidCourseDateException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid course date", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.5: Viết kiểm thử cho chức năng thêm, sửa, xóa khóa học
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/course/src/main/java/org/nlh4j/membership_hub/course/CourseService.java;./sources/backend/course/src/test/java/org/nlh4j/membership_hub/course/CourseTest.java

* **TagID mục tiêu:** [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng thêm, sửa, xóa khóa học. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 2.6: Tài liệu chức năng thêm, sửa, xóa khóa học
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/course.md

* **TagID mục tiêu:** [REQ-008]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng thêm, sửa, xóa khóa học. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 2.7: Xây dựng chức năng gán giáo viên cho khóa học
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/course/src/main/java/org/nlh4j/membership_hub/course/CourseTeacherService.java

* **TagID mục tiêu:** [REQ-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gán giáo viên cho khóa học. Chức năng này sẽ cho phép quản trị viên gán giáo viên cho khóa học.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE course_teachers (
    course_teacher_id UUID PRIMARY KEY,
    course_id UUID REFERENCES courses(course_id),
    teacher_id UUID REFERENCES users(user_id),
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
      "path": "/api/courses/{courseId}/teachers",
      "method": "POST",
      "request": {
        "teacher_id": "UUID"
      },
      "response": {
        "course_teacher_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidTeacherException.class)
public ResponseEntity<ErrorResponse> handleInvalidTeacher(InvalidTeacherException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid teacher", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.8: Viết kiểm thử cho chức năng gán giáo viên cho khóa học
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/course/src/main/java/org/nlh4j/membership_hub/course/CourseTeacherService.java;./sources/backend/course/src/test/java/org/nlh4j/membership_hub/course/CourseTeacherTest.java

* **TagID mục tiêu:** [REQ-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gán giáo viên cho khóa học. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 2.9: Tài liệu chức năng gán giáo viên cho khóa học
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/course.md

* **TagID mục tiêu:** [REQ-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gán giáo viên cho khóa học. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

### 🌤️ NGÀY 3: Xây dựng chức năng xem danh sách khóa học, đăng ký khóa học cho học viên

#### 📝 NHIỆM VỤ CON 3.1: Xây dựng chức năng xem danh sách khóa học
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentService.java

* **TagID mục tiêu:** [REQ-010]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem danh sách khóa học. Chức năng này sẽ trả về danh sách các khóa học mà học viên chưa đăng ký.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    course_id UUID REFERENCES courses(course_id),
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
      "path": "/api/enrollments/available-courses",
      "method": "GET",
      "response": {
        "courses": [
          {
            "course_id": "UUID",
            "title": "string",
            "description": "string",
            "start_date": "date",
            "end_date": "date",
            "teacher_id": "UUID",
            "max_students": "integer"
          }
        ]
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(NoAvailableCoursesException.class)
public ResponseEntity<ErrorResponse> handleNoAvailableCourses(NoAvailableCoursesException ex) {
    ErrorResponse errorResponse = new ErrorResponse("No available courses", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.NOT_FOUND);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 3.2: Viết kiểm thử cho chức năng xem danh sách khóa học
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentService.java;./sources/backend/enrollment/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentTest.java

* **TagID mục tiêu:** [REQ-010]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem danh sách khóa học. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 3.3: Tài liệu chức năng xem danh sách khóa học
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/enrollment.md

* **TagID mục tiêu:** [REQ-010]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem danh sách khóa học. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 3.4: Xây dựng chức năng đăng ký khóa học cho học viên
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentService.java

* **TagID mục tiêu:** [REQ-011]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đăng ký khóa học cho học viên. Chức năng này sẽ cho phép học viên đăng ký khóa học.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    course_id UUID REFERENCES courses(course_id),
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
      "path": "/api/enrollments",
      "method": "POST",
      "request": {
        "course_id": "UUID"
      },
      "response": {
        "enrollment_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidEnrollmentException.class)
public ResponseEntity<ErrorResponse> handleInvalidEnrollment(InvalidEnrollmentException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid enrollment", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 3.5: Viết kiểm thử cho chức năng đăng ký khóa học cho học viên
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/src/main/java/org/nlh4j/membership_hub/enrollment/EnrollmentService.java;./sources/backend/enrollment/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentTest.java

* **TagID mục tiêu:** [REQ-011]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đăng ký khóa học cho học viên. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 3.6: Tài liệu chức năng đăng ký khóa học cho học viên
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/enrollment.md

* **TagID mục tiêu:** [REQ-011]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đăng ký khóa học cho học viên. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.