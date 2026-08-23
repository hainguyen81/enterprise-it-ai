# Giai đoạn 2: <!--PHASE_NAME_START-->Triển khai quản lý khóa học và đăng ký học viên<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã bản thiết kế** | ARCH-20260822094056 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai quản lý khóa học và đăng ký học viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai toàn bộ chức năng quản lý khóa học (xem danh sách, CRUD với kiểm tra xung đột lịch giáo viên/địa điểm, phân công giáo viên) và chức năng đăng ký khóa học cho học viên (duyệt khóa học chưa đăng ký, xử lý đăng ký tự động tạo tài khoản Student nếu cần, gửi thông báo tự động), đảm bảo tính toàn vẹn dữ liệu và trải nghiệm người dùng mượt mà<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/22 09:40:56 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 2 tập trung vào triển khai hai nhóm chức năng nghiệp vụ cốt lõi của hệ thống membership-hub:
1. **Quản lý khóa học**: Xây dựng dịch vụ vi mô course-service với đầy đủ chức năng CRUD, kiểm tra xung đột lịch giáo viên/địa điểm, phân công giáo viên vào khóa học, và giao diện frontend hiển thị danh sách khóa học responsive.
2. **Đăng ký khóa học**: Xây dựng dịch vụ vi mô enrollment-service xử lý đăng ký khóa học cho học viên, tự động tạo tài khoản Student nếu chưa tồn tại, gửi thông báo tự động, và giao diện frontend cho học viên duyệt và đăng ký khóa học.
Tất cả chức năng tuân thủ ma trận RBAC đã định nghĩa, đảm bảo tính toàn vẹn dữ liệu với các ràng buộc khóa ngoại và duy nhất, và tích hợp sẵn sàng với các dịch vụ khác trong hệ thống vi mô.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục
Tất cả đường dẫn tệp đều bắt đầu với gốc kho lưu trữ `./sources/`, tuân thủ cấu trúc kiến trúc vi mô đã định nghĩa:
* **Hạ tầng backend vi mô Quarkus (dịch vụ đã được khởi tạo trong Giai đoạn 1):**
  * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/model/Course.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/repository/CourseRepository.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/service/CourseService.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/exception/ScheduleConflictException.java [REQ-008]
  * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/model/Enrollment.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/repository/EnrollmentRepository.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/service/EnrollmentService.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/controller/EnrollmentController.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/exception/EnrollmentException.java [REQ-011]
* **Lớp frontend Next.js:**
  * ./sources/frontend/src/app/courses/page.tsx [REQ-007], [REQ-010]
  * ./sources/frontend/src/app/courses/[id]/page.tsx [REQ-007], [REQ-008], [REQ-009]
  * ./sources/frontend/src/app/enrollments/page.tsx [REQ-010], [REQ-011]
  * ./sources/frontend/src/components/CourseCard.tsx [REQ-007], [REQ-010]
  * ./sources/frontend/src/components/EnrollmentForm.tsx [REQ-011]
* **Tài liệu doanh nghiệp:**
  * ./sources/docs/api/course-management-api.md [REQ-007], [REQ-008], [REQ-009]
  * ./sources/docs/api/enrollment-api.md [REQ-010], [REQ-011]
* **Tệp kiểm thử:**
  * ./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/CourseServiceTest.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/CourseControllerIT.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentServiceTest.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentControllerIT.java [REQ-010], [REQ-011]

## 3. Chỉ thị chức năng cho tác nhân phụ chuyên dụng
* **Coder**: Đóng vai trò là Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên cả backend services (course-service, enrollment-service) và frontend/ứng dụng di động. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
* **Tester**: Đóng vai trò là Kiểm soát chất lượng (QC/QA) cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác thực hiệu năng. Bị cấm sửa mã nguồn sản xuất. Nếu mục tiêu nhiệm vụ liên quan đến phạm vi kiểm thử tích hợp hoặc end-to-end mà không có tệp mã ứng dụng cụ thể nào có thể bị giới hạn, bạn PHẢI xuất ra literal token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp dấu chấm phẩy.
* **Doc**: Hoạt động như là Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Đặc tả kỹ thuật toàn diện, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp kiến trúc đang hoạt động của dự án. Mỗi tệp tài liệu kỹ thuật được tạo PHẢI được liệt kê là thực thể đường dẫn tệp cụ thể có phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Chịu trách nhiệm xác minh trình biên dịch, cổng phân tích tĩnh và vá bảo vệ phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗi hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
Giai đoạn 2 được coi là hoàn thành khi đáp ứng đầy đủ các mốc định lượng sau:
1. Dịch vụ course-service được triển khai đầy đủ chức năng CRUD khóa học, kiểm tra xung đột lịch giáo viên/địa điểm, phân công giáo viên, tất cả endpoint REST hoạt động đúng theo hợp đồng API đã định nghĩa.
2. Dịch vụ enrollment-service được triển khai đầy đủ chức năng duyệt khóa học chưa đăng ký, xử lý đăng ký khóa học, tự động tạo tài khoản Student nếu cần, gửi thông báo tự động.
3. Giao diện frontend cho danh sách khóa học và đăng ký khóa học được triển khai responsive, tích hợp đầy đủ với backend APIs, hỗ trợ đa ngôn ngữ.
4. Tất cả bộ kiểm thử đơn vị và tích hợp cho course-service và enrollment-service đều vượt qua, độ bao phủ mã đạt >= 85%.
5. Tất cả thẻ theo dõi yêu cầu được phân phối cho giai đoạn 2 ([REQ-007] đến [REQ-011]) được ánh xạ đầy đủ vào các nhiệm vụ kỹ thuật và tài liệu, không có thẻ nào bị thiếu.
6. Tài liệu API cho course-management và enrollment được hoàn thiện đầy đủ, tuân thủ chuẩn OpenAPI 3.0.
7. Không có lỗ hổng bảo mật OWASP Top 10 được phát hiện trong mã nguồn course-service và enrollment-service, tất cả đầu vào người dùng được xác thực, truy vấn cơ sở dữ liệu sử dụng prepared statements.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC TỪNG NGÀY

### 🌤️ NGÀY 1
<!--DAY_HEADER_START-->Triển khai logic cốt lõi dịch vụ khóa học và giao diện danh sách khóa học frontend<!--DAY_HEADER_END-->

#### 📝 Công việc con 1.1: Xây dựng thực thể và kho lưu trữ khóa học
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/model/Course.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho khóa học, ánh xạ đến bảng PostgreSQL COURSES (DAT-004), định nghĩa đầy đủ các trường: courseId (UUID, khóa chính), title (varchar 150, không null), description (text, tùy chọn), startDate (date, không null), endDate (date, không null), teacherId (UUID, khóa ngoại đến Users.userId), maxStudents (int, mặc định 30), createdAt và updatedAt (timestamp, không null, mặc định now()). Thêm ràng buộc duy nhất trên trường title để tránh trùng tên khóa học. Sử dụng các annotation validation (@NotNull, @Size, @PastOrPresent) cho các trường dữ liệu.

#### 📝 Công việc con 1.2: Xây dựng logic nghiệp vụ cốt lõi của dịch vụ khóa học
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/service/CourseService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các phương thức nghiệp vụ: lấy danh sách tất cả khóa học đang hoạt động, lấy chi tiết khóa học theo ID, tạo mới khóa học với xác thực các trường bắt buộc, cập nhật thông tin khóa học, xóa khóa học. Thêm logic kiểm tra xung đột lịch giáo viên: trước khi phân công giáo viên hoặc tạo/cập nhật khóa học, kiểm tra xem giáo viên có khóa học khác trùng khoảng thời gian (startDate đến endDate) hay không, nếu có thì ném ngoại lệ ScheduleConflictException. Đảm bảo chỉ System Admin và Center Admin có quyền thực hiện các thao tác quản lý.

#### 📝 Công việc con 1.3: Xây dựng controller và endpoint REST cho quản lý khóa học
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/controller/CourseController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST: GET /api/courses (lấy danh sách khóa học), GET /api/courses/{id} (lấy chi tiết), POST /api/courses (tạo mới), PUT /api/courses/{id} (cập nhật), DELETE /api/courses/{id} (xóa), POST /api/courses/{id}/assign-teacher (phân công giáo viên). Áp dụng xác thực JWT Bearer Token, kiểm tra quyền RBAC (chỉ System Admin và Center Admin được phép chỉnh sửa/xóa khóa học, tất cả người dùng đã xác thực được phép xem). Thêm xác thực đầu vào request và phản hồi lỗi chuẩn hóa theo hợp đồng API đã định nghĩa.

<!--START_API_CONTRACT-->
```json
{
  "courseApi": {
    "basePath": "/api/courses",
    "endpoints": [
      {
        "method": "GET",
        "path": "/",
        "description": "List all active courses",
        "requestSchema": null,
        "responseSchema": {
          "type": "array",
          "items": {
            "courseId": "uuid",
            "title": "string (max 150 chars, not null)",
            "description": "string (optional, max 2000 chars)",
            "startDate": "date (YYYY-MM-DD, not null)",
            "endDate": "date (YYYY-MM-DD, not null)",
            "teacherId": "uuid (not null)",
            "teacherName": "string",
            "maxStudents": "integer (default 30)",
            "enrolledCount": "integer"
          }
        },
        "auth": "Bearer JWT",
        "rbac": ["Student", "Teacher", "Center Admin", "System Admin"]
      },
      {
        "method": "POST",
        "path": "/",
        "description": "Create new course",
        "requestSchema": {
          "title": "string (required, max 150 chars)",
          "description": "string (optional, max 2000 chars)",
          "startDate": "date (required, YYYY-MM-DD)",
          "endDate": "date (required, YYYY-MM-DD)",
          "teacherId": "uuid (required)",
          "maxStudents": "integer (optional, default 30)"
        },
        "responseSchema": {
          "courseId": "uuid",
          "title": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid"
        },
        "auth": "Bearer JWT",
        "rbac": ["System Admin", "Center Admin"]
      },
      {
        "method": "PUT",
        "path": "/{courseId}",
        "description": "Update existing course",
        "requestSchema": {
          "title": "string (optional, max 150 chars)",
          "description": "string (optional, max 2000 chars)",
          "startDate": "date (optional, YYYY-MM-DD)",
          "endDate": "date (optional, YYYY-MM-DD)",
          "maxStudents": "integer (optional)"
        },
        "responseSchema": {
          "courseId": "uuid",
          "title": "string",
          "startDate": "date",
          "endDate": "date",
          "teacherId": "uuid"
        },
        "auth": "Bearer JWT",
        "rbac": ["System Admin", "Center Admin"]
      },
      {
        "method": "DELETE",
        "path": "/{courseId}",
        "description": "Delete course",
        "requestSchema": null,
        "responseSchema": null,
        "auth": "Bearer JWT",
        "rbac": ["System Admin"]
      },
      {
        "method": "POST",
        "path": "/{courseId}/assign-teacher",
        "description": "Assign teacher to course",
        "requestSchema": {
          "teacherId": "uuid (required)"
        },
        "responseSchema": {
          "success": "boolean",
          "message": "string"
        },
        "auth": "Bearer JWT",
        "rbac": ["System Admin"]
      }
    ]
  }
}
```
<!--END_API_CONTRACT-->

#### 📝 Công việc con 1.4: Xây dựng trang danh sách khóa học frontend
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/app/courses/page.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai trang danh sách khóa học responsive, tích hợp với API /api/courses để hiển thị danh sách khóa học với đầy đủ thông tin: tiêu đề, lịch học, giáo viên phụ trách, số lượng học viên đã đăng ký. Thêm chức năng lọc theo trung tâm, tìm kiếm theo tên khóa học, sắp xếp theo ngày bắt đầu. Đảm bảo giao diện phù hợp với cả web và di động, tích hợp với hệ thống i18n để hỗ trợ đa ngôn ngữ.

#### 📝 Công việc con 1.5: Viết bài kiểm tra đơn vị cho logic nghiệp vụ khóa học
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/service/CourseService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra đơn vị toàn diện cho tất cả các phương thức trong CourseService, bao gồm: thao tác CRUD khóa học, logic kiểm tra xung đột lịch giáo viên, xác thực các trường đầu vào, xử lý các trường hợp biên (khóa học không tồn tại, giáo viên không hợp lệ, ngày bắt đầu sau ngày kết thúc). Đảm bảo độ bao phủ mã ít nhất 90%, sử dụng JUnit 5 và Mockito.

#### 📝 Công việc con 1.6: Viết bài kiểm tra tích hợp cho endpoint quản lý khóa học
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/backend/course-service/src/test/java/org/nlh4j/membership_hub/course/CourseControllerIT.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra tích hợp cho tất cả các endpoint trong CourseController, kiểm tra xác thực JWT, kiểm tra quyền RBAC (phân biệt quyền của Student, Teacher, Center Admin, System Admin), xác thực phản hồi request/response, xử lý lỗi (khóa học không tồn tại, xung đột lịch, thiếu quyền truy cập). Sử dụng cơ sở dữ liệu thử nghiệm H2 và Testcontainers để chạy kiểm tra.

#### 📝 Công việc con 1.7: Viết tài liệu đặc tả API quản lý khóa học
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/api/course-management-api.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết tài liệu đặc tả API đầy đủ cho tất cả các endpoint quản lý khóa học, bao gồm: mô tả chức năng, phương thức HTTP, đường dẫn, schema request/response, mã lỗi, yêu cầu xác thực, quyền RBAC, và ví dụ payload thực tế. Đảm bảo tài liệu phù hợp với tiêu chuẩn OpenAPI 3.0.

#### 📝 Công việc con 1.8: Rà soát mã nguồn dịch vụ khóa học
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/service/CourseService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát mã nguồn toàn bộ dịch vụ khóa học, kiểm tra tuân thủ tiêu chuẩn mã hóa doanh nghiệp, phát hiện lỗi logic, điểm nghẽn hiệu năng, đảm bảo không có lỗ hổng bảo mật (SQL injection, XSS), đề xuất chiến lược sửa lỗi tối ưu. Đảm bảo mã nguồn sẵn sàng cho tích hợp với các dịch vụ khác.

### 🌤️ NGÀY 2
<!--DAY_HEADER_START-->Triển khai logic nghiệp vụ đăng ký khóa học và giao diện liên quan frontend<!--DAY_HEADER_END-->

#### 📝 Công việc con 2.1: Xây dựng thực thể và kho lưu trữ ghi danh
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/model/Enrollment.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho ghi danh, ánh xạ đến bảng PostgreSQL ENROLLMENTS (DAT-005), định nghĩa các trường: enrollmentId (UUID, khóa chính), studentId (UUID, khóa ngoại đến Users.userId, không null), courseId (UUID, khóa ngoại đến Courses.courseId, không null), enrollmentDate (timestamp, mặc định now()). Thêm ràng buộc duy nhất trên cặp (studentId, courseId) để ngăn đăng ký trùng lặp, thêm chỉ mục trên courseId để tối ưu truy vấn danh sách học viên của khóa học.

#### 📝 Công việc con 2.2: Xây dựng logic nghiệp vụ cốt lõi của dịch vụ ghi danh
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/service/EnrollmentService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các phương thức nghiệp vụ: lấy danh sách khóa học chưa đăng ký của học viên (loại trừ các khóa học đã có bản ghi ghi danh), xử lý yêu cầu đăng ký khóa học, tự động tạo tài khoản Student với vai trò 'Student' nếu học viên chưa có tài khoản cục bộ, xác thực số lượng học viên tối đa của khóa học trước khi đăng ký, kích hoạt gửi thông báo đăng ký thành công cho học viên và nhóm Zalo của trung tâm. Đảm bảo chỉ học viên có vai trò Student được phép đăng ký khóa học.

#### 📝 Công việc con 2.3: Xây dựng controller và endpoint REST cho đăng ký khóa học
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/controller/EnrollmentController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST: GET /api/courses/available (lấy danh sách khóa học chưa đăng ký của học viên hiện tại), POST /api/enrollments (xử lý đăng ký khóa học). Áp dụng xác thực JWT Bearer Token, kiểm tra quyền RBAC (chỉ học viên có vai trò Student được phép đăng ký khóa học, tất cả người dùng đã xác thực được phép xem danh sách khóa học có sẵn). Thêm xác thực đầu vào request và phản hồi lỗi chuẩn hóa cho trường hợp khóa học đã đủ sĩ số hoặc học viên đã đăng ký trước đó.

<!--START_API_CONTRACT-->
```json
{
  "enrollmentApi": {
    "basePath": "/api/enrollments",
    "endpoints": [
      {
        "method": "GET",
        "path": "/available",
        "description": "List available courses for current student (exclude already enrolled)",
        "requestSchema": null,
        "responseSchema": {
          "type": "array",
          "items": {
            "courseId": "uuid",
            "title": "string",
            "startDate": "date",
            "endDate": "date",
            "teacherName": "string",
            "maxStudents": "integer",
            "availableSlots": "integer"
          }
        },
        "auth": "Bearer JWT",
        "rbac": ["Student"]
      },
      {
        "method": "POST",
        "path": "/",
        "description": "Enroll student in course",
        "requestSchema": {
          "courseId": "uuid (required)"
        },
        "responseSchema": {
          "enrollmentId": "uuid",
          "courseId": "uuid",
          "enrollmentDate": "timestamp (ISO 8601)",
          "status": "string (success | failed)"
        },
        "auth": "Bearer JWT",
        "rbac": ["Student"]
      }
    ]
  }
}
```
<!--END_API_CONTRACT-->

#### 📝 Công việc con 2.4: Xây dựng giao diện đăng ký khóa học frontend
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/app/enrollments/page.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai trang đăng ký khóa học responsive cho học viên, hiển thị danh sách khóa học chưa đăng ký lấy từ endpoint /api/courses/available, tích hợp form đăng ký với xác thực đầu vào, hiển thị thông báo thành công/lỗi sau khi đăng ký, đồng bộ trạng thái đăng ký với backend. Đảm bảo giao diện thân thiện với người dùng di động, tích hợp với hệ thống i18n để hỗ trợ đa ngôn ngữ.

#### 📝 Công việc con 2.5: Viết bài kiểm tra đơn vị cho logic nghiệp vụ ghi danh
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/service/EnrollmentService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra đơn vị toàn diện cho tất cả các phương thức trong EnrollmentService, bao gồm: lấy danh sách khóa học có sẵn, xử lý đăng ký khóa học, tự động tạo tài khoản Student, ngăn chặn đăng ký trùng lặp, xác thực số lượng học viên tối đa. Đảm bảo độ bao phủ mã ít nhất 90%, bao gồm các trường hợp biên (học viên không tồn tại, khóa học không tồn tại, khóa học đã đủ sĩ số).

#### 📝 Công việc con 2.6: Viết bài kiểm tra tích hợp cho endpoint đăng ký khóa học
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/backend/enrollment-service/src/test/java/org/nlh4j/membership_hub/enrollment/EnrollmentControllerIT.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra tích hợp cho tất cả các endpoint trong EnrollmentController, kiểm tra xác thực JWT, kiểm tra quyền RBAC, xác thực phản hồi request/response, xử lý lỗi (khóa học không tồn tại, đã đủ sĩ số, đã đăng ký trước đó, thiếu quyền truy cập). Sử dụng cơ sở dữ liệu thử nghiệm H2 và Testcontainers để chạy kiểm tra.

#### 📝 Công việc con 2.7: Rà soát mã nguồn dịch vụ khóa học và ghi danh
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/course-service/src/main/java/org/nlh4j/membership_hub/course/service/CourseService.java;./sources/backend/enrollment-service/src/main/java/org/nlh4j/membership_hub/enrollment/service/EnrollmentService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát mã nguồn toàn bộ dịch vụ khóa học và ghi danh, kiểm tra tuân thủ tiêu chuẩn mã hóa doanh nghiệp, phát hiện lỗi logic, điểm nghẽn hiệu năng, đảm bảo không có lỗ hổng bảo mật (injection SQL, xác thực đầu vào không đầy đủ), tối ưu hiệu năng truy vấn cơ sở dữ liệu, sửa các lỗi và điểm nghẽn được phát hiện, đảm bảo mã nguồn sẵn sàng cho tích hợp với các dịch vụ khác.

#### 📝 Công việc con 2.8: Viết tài liệu đặc tả API đăng ký khóa học
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/api/enrollment-api.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết tài liệu đặc tả API đầy đủ cho tất cả các endpoint đăng ký khóa học, bao gồm: mô tả chức năng, phương thức HTTP, đường dẫn, schema request/response, mã lỗi, yêu cầu xác thực, quyền RBAC, và ví dụ payload thực tế. Đảm bảo tài liệu phù hợp với tiêu chuẩn OpenAPI 3.0.