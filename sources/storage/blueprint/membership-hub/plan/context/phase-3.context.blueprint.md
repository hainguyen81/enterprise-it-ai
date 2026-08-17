# Quản lý điểm danh và thẻ thành viên <!--PHASE_NAME_START-->Quản lý điểm danh và thẻ thành viên<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID bản thiết kế** | ARCH-20260817193854 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Quản lý điểm danh và thẻ thành viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc quản lý điểm danh và thẻ thành viên. Chúng ta sẽ xây dựng các chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh, xem thông tin thẻ thành viên, và gia hạn thẻ thành viên.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/17 19:38:54 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc quản lý điểm danh và thẻ thành viên. Chúng ta sẽ xây dựng các chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh, xem thông tin thẻ thành viên, và gia hạn thẻ thành viên.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/attendance/`
- `./sources/backend/studentcard/`

## 3. Hướng dẫn chức năng của các chuyên gia con được chỉ định
*   **Coder**: Hoạt động như một Nhà phát triển ứng dụng cấp cao/Chủ tịch. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Trưởng/QC/QA cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con tác vụ liên quan đến phạm vi tích hợp hoặc kết thúc-to-end tổng thể nơi không có tệp mã cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh trình biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về việc đóng gói, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các chức năng quét mã QR để điểm danh.
- Hoàn thành 100% các chức năng đảm bảo tính idempotency cho điểm danh.
- Hoàn thành 100% các chức năng xem thông tin thẻ thành viên.
- Hoàn thành 100% các chức năng gia hạn thẻ thành viên.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% các bộ kiểm thử chức năng và tích hợp.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc hàng ngày

### 🌤️ NGÀY 1: Xây dựng chức năng quét mã QR để điểm danh

#### 📝 NHIỆM VỤ CON 1.1: Xây dựng chức năng quét mã QR để điểm danh
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java

* **TagID mục tiêu:** [REQ-012]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng quét mã QR để điểm danh. Chức năng này sẽ cho phép học viên quét mã QR để điểm danh cho các khóa học.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    course_id UUID REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
      "path": "/api/attendance",
      "method": "POST",
      "request": {
        "student_id": "UUID",
        "course_id": "UUID",
        "attendance_date": "date"
      },
      "response": {
        "attendance_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(DuplicateAttendanceException.class)
public ResponseEntity<ErrorResponse> handleDuplicateAttendance(DuplicateAttendanceException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Duplicate attendance", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.CONFLICT);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.2: Viết kiểm thử cho chức năng quét mã QR để điểm danh
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java;./sources/backend/attendance/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceTest.java

* **TagID mục tiêu:** [REQ-012]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng quét mã QR để điểm danh. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 1.3: Tài liệu chức năng quét mã QR để điểm danh
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/attendance.md

* **TagID mục tiêu:** [REQ-012]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng quét mã QR để điểm danh. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 1.4: Xây dựng chức năng đảm bảo tính idempotency cho điểm danh
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java

* **TagID mục tiêu:** [REQ-013]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đảm bảo tính idempotency cho điểm danh. Chức năng này sẽ đảm bảo rằng mỗi học viên chỉ có một bản ghi điểm danh cho mỗi khóa học trong một ngày.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    course_id UUID REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id, attendance_date)
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/attendance",
      "method": "POST",
      "request": {
        "student_id": "UUID",
        "course_id": "UUID",
        "attendance_date": "date"
      },
      "response": {
        "attendance_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(DuplicateAttendanceException.class)
public ResponseEntity<ErrorResponse> handleDuplicateAttendance(DuplicateAttendanceException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Duplicate attendance", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.CONFLICT);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.5: Viết kiểm thử cho chức năng đảm bảo tính idempotency cho điểm danh
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java;./sources/backend/attendance/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceTest.java

* **TagID mục tiêu:** [REQ-013]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đảm bảo tính idempotency cho điểm danh. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 1.6: Tài liệu chức năng đảm bảo tính idempotency cho điểm danh
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/attendance.md

* **TagID mục tiêu:** [REQ-013]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đảm bảo tính idempotency cho điểm danh. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

### 🌤️ NGÀY 2: Xây dựng chức năng xem thông tin thẻ thành viên, gia hạn thẻ thành viên

#### 📝 NHIỆM VỤ CON 2.1: Xây dựng chức năng xem thông tin thẻ thành viên
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java

* **TagID mục tiêu:** [REQ-014]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem thông tin thẻ thành viên. Chức năng này sẽ cho phép học viên xem thông tin thẻ thành viên, bao gồm ngày phát hành, ngày hết hạn, và số ngày còn lại.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
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
      "path": "/api/student-cards/{studentId}",
      "method": "GET",
      "response": {
        "card_id": "UUID",
        "issue_date": "date",
        "validity_days": "integer",
        "remaining_days": "integer"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(NoStudentCardFoundException.class)
public ResponseEntity<ErrorResponse> handleNoStudentCardFound(NoStudentCardFoundException ex) {
    ErrorResponse errorResponse = new ErrorResponse("No student card found", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.NOT_FOUND);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.2: Viết kiểm thử cho chức năng xem thông tin thẻ thành viên
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java;./sources/backend/studentcard/src/test/java/org/nlh4j/membership_hub/studentcard/StudentCardTest.java

* **TagID mục tiêu:** [REQ-014]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem thông tin thẻ thành viên. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 2.3: Tài liệu chức năng xem thông tin thẻ thành viên
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/studentcard.md

* **TagID mục tiêu:** [REQ-014]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem thông tin thẻ thành viên. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 2.4: Xây dựng chức năng gia hạn thẻ thành viên
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java

* **TagID mục tiêu:** [REQ-015]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gia hạn thẻ thành viên. Chức năng này sẽ cho phép học viên gia hạn thẻ thành viên bằng cách thêm số ngày vào ngày hết hạn hiện tại.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
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
      "path": "/api/student-cards/{studentId}/renew",
      "method": "POST",
      "request": {
        "renewal_days": "integer"
      },
      "response": {
        "card_id": "UUID",
        "remaining_days": "integer",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidRenewalDaysException.class)
public ResponseEntity<ErrorResponse> handleInvalidRenewalDays(InvalidRenewalDaysException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid renewal days", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.5: Viết kiểm thử cho chức năng gia hạn thẻ thành viên
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java;./sources/backend/studentcard/src/test/java/org/nlh4j/membership_hub/studentcard/StudentCardTest.java

* **TagID mục tiêu:** [REQ-015]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gia hạn thẻ thành viên. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 2.6: Tài liệu chức năng gia hạn thẻ thành viên
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/studentcard.md

* **TagID mục tiêu:** [REQ-015]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gia hạn thẻ thành viên. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.