# Giai đoạn 2: <!--PHASE_NAME_START-->Triển khai quản lý khóa học và đăng ký học viên<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản thảo** | ARCH-20260817042313 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai quản lý khóa học và đăng ký học viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai các dịch vụ quản lý khóa học và đăng ký học viên, bao gồm API quản lý khóa học (CRUD), phân công giáo viên, duyệt khóa học và đăng ký khóa học cho học viên với kiểm tra xung đột lịch học, đảm bảo tích hợp liền mạch với các service đã triển khai ở giai đoạn trước và tuân thủ các yêu cầu phi chức năng về hiệu suất, bảo mật.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/08/17 04:23:13 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 2 tập trung triển khai 2 microservice cốt lõi của hệ thống membership-hub là `course-service` (quản lý khóa học) và `enrollment-service` (quản lý đăng ký học viên), bao gồm các mục tiêu kỹ thuật sau:
1. Triển khai API CRUD đầy đủ cho quản lý khóa học: xem danh sách khóa học, tạo mới, cập nhật, xóa khóa học, tích hợp logic kiểm tra xung đột lịch học giáo viên để tránh gán giáo viên cho nhiều khóa học trùng thời gian.
2. Triển khai API phân công giáo viên vào khóa học và thu hồi phân công, tích hợp cơ chế gửi thông báo tự động cho giáo viên khi được phân công.
3. Triển khai API duyệt khóa học cho học viên, hiển thị danh sách khóa học chưa đăng ký kèm thông tin sức chứa và lịch học, đảm bảo học viên chỉ xem được khóa học chưa đăng ký của chính mình (tuân thủ RBAC).
4. Triển khai API đăng ký khóa học cho học viên, tích hợp logic tự động tạo tài khoản học viên nếu chưa tồn tại, kiểm tra trùng lặp đăng ký và sức chứa khóa học, kích hoạt thông báo tự động cho học viên và nhóm Zalo của trung tâm sau khi đăng ký thành công.
5. Viết tài liệu hợp đồng API REST chi tiết cho 2 service, đảm bảo tuân thủ chuẩn hóa hợp đồng API và tích hợp liền mạch với các service đã triển khai ở giai đoạn 1 (`user-service`, `center-service`).
6. Thực hiện kiểm thử đơn vị và tích hợp đầy đủ cho tất cả chức năng, đảm bảo độ phủ mã >= 90%, không có lỗi bảo mật cơ bản.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Dịch vụ Backend:**
  * `./sources/backend/course-service/` [REQ-007], [REQ-008], [REQ-009]
  * `./sources/backend/enrollment-service/` [REQ-010], [REQ-011]
- **Tài liệu:**
  * `./sources/docs/architecture/` [ARC-010], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]
- **Điểm cuối API (REST):**
  * `GET /api/v1/courses` [REQ-007]
  * `POST /api/v1/courses` [REQ-008]
  * `PUT /api/v1/courses/{courseId}` [REQ-008]
  * `DELETE /api/v1/courses/{courseId}` [REQ-008]
  * `POST /api/v1/courses/{courseId}/teachers` [REQ-009]
  * `DELETE /api/v1/courses/{courseId}/teachers/{teacherId}` [REQ-009]
  * `GET /api/v1/courses/available` [REQ-010]
  * `POST /api/v1/courses/{courseId}/enroll` [REQ-011]
- **Chủ đề sự kiện (Message Broker):**
  * `course.created` [REQ-008]
  * `course.updated` [REQ-008]
  * `teacher.assigned` [REQ-009]
  * `student.enrolled` [REQ-011]

## 3. Chỉ thị chức năng chuyên biệt cho Đại lý phụ
*   **Coder**: Làm việc như Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên cả 2 dịch vụ backend `course-service` và `enrollment-service`. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
*   **Tester**: Làm việc như Kiểm soát chất lượng/QA chính. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo kiểm thử đơn vị, kiểm thử tích hợp và kịch bản xác thực hiệu suất. Bị cấm sửa đổi mã nguồn sản xuất. Nếu phạm vi tác vụ mục tiêu là tích hợp/E2E không có tệp mã nguồn cụ thể, phải xuất ra token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp đường dẫn phân tách bằng dấu chấm phẩy.
*   **Doc**: Hoạt động như Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên biên soạn tài liệu Thông số kỹ thuật, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp công nghệ đang hoạt động của dự án. Mọi tệp tài liệu kỹ thuật được tạo phải có đuôi `.md` và nằm strictly trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Chịu trách nhiệm xác minh biên dịch, kiểm soát phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗi bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên strictly về containerization, kỹ thuật Dockerfile đa giai đoạn, tối ưu gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trên Google Cloud Platform. Chịu trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container một cách native trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Chịu trách nhiệm xây dựng manifest triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc microservice vào cụm GKE đang hoạt động.

## 4. Định nghĩa Hoàn thành của Giai đoạn (DoD)
1. Tất cả công việc của giai đoạn 2 đã được triển khai và kiểm thử thành công.
2. 100% thẻ theo dõi [REQ-007] đến [REQ-011] được ánh xạ và bao phủ đầy đủ.
3. Độ phủ mã đạt >= 90% cho các lớp service và controller của `course-service` và `enrollment-service`.
4. Tất cả endpoint API hoạt động đúng theo hợp đồng đã định nghĩa, bao gồm logic kiểm tra xung đột lịch học giáo viên hoạt động chính xác.
5. Luồng đăng ký khóa học hoạt động đúng, bao gồm tự động tạo tài khoản học viên nếu chưa tồn tại, kiểm tra sức chứa khóa học, ngăn chặn đăng ký trùng lặp.
6. Tất cả sự kiện message broker được kích hoạt đúng khi có thay đổi nghiệp vụ (tạo khóa học, phân công giáo viên, đăng ký học viên).
7. Tài liệu hợp đồng API cho `course-service` và `enrollment-service` được hoàn thiện đầy đủ, chính xác, tuân thủ chuẩn OpenAPI 3.0.
8. Không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) được phát hiện trong quá trình code review, tuân thủ đầy đủ OWASP Top 10 [NFR-003].
9. Tất cả unit test và integration test đều vượt qua, đáp ứng ngưỡng độ phủ mã yêu cầu.

## 5. Nhật ký thực thi kiến trúc theo từng ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->Triển khai API quản lý khóa học và phân công giáo viên<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai API CRUD quản lý khóa học
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java`; `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API CRUD đầy đủ cho quản lý khóa học:
  - `GET /api/v1/courses`: Lấy danh sách tất cả khóa học, kèm thông tin lịch học, giáo viên được phân công, sức chứa hiện tại. Sử dụng JOIN truy vấn giữa bảng `courses` và `users` để lấy tên giáo viên, áp dụng phân trang nếu số lượng khóa học lớn.
  - `POST /api/v1/courses`: Tạo khóa học mới, yêu cầu đầu vào bao gồm `title`, `startDate`, `endDate`, `teacherId`, `maxStudents` (tùy chọn, mặc định 30). Triển khai logic kiểm tra xung đột lịch học: truy vấn các khóa học hiện tại của `teacherId` trong khoảng thời gian `[startDate, endDate]` mới, nếu có bất kỳ khóa học nào giao nhau, trả về lỗi 409 Conflict với thông báo "Giáo viên đã được phân công cho khóa học khác trong khoảng thời gian này".
  - `PUT /api/v1/courses/{courseId}`: Cập nhật thông tin khóa học, nếu thay đổi `teacherId`, `startDate` hoặc `endDate` thì thực hiện kiểm tra xung đột lịch học tương tự như khi tạo mới.
  - `DELETE /api/v1/courses/{courseId}`: Xóa khóa học, kiểm tra không có học viên nào đã đăng ký khóa học trước khi xóa, nếu có học viên đăng ký thì trả về lỗi 400 Bad Request với thông báo "Không thể xóa khóa học đã có học viên đăng ký".
  Đảm bảo tất cả truy vấn cơ sở dữ liệu sử dụng prepared statements để ngăn chặn SQL injection [NFR-003], áp dụng xác thực đầu vào cho tất cả các trường request body, thực thi kiểm tra quyền RBAC (chỉ System Admin và Center Admin được phép thực hiện các thao tác CRUD khóa học).

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "courseService": {
      "basePath": "/api/v1",
      "endpoints": [
        {
          "method": "GET",
          "path": "/courses",
          "tags": ["REQ-007"],
          "summary": "Lấy danh sách khóa học với lịch học và thông tin giáo viên",
          "response": {
            "schema": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "courseId": {"type": "uuid"},
                  "title": {"type": "string", "maxLength": 150},
                  "description": {"type": "string"},
                  "startDate": {"type": "date"},
                  "endDate": {"type": "date"},
                  "teacherId": {"type": "uuid"},
                  "teacherName": {"type": "string"},
                  "maxStudents": {"type": "integer"},
                  "currentEnrollments": {"type": "integer"}
                }
              }
            }
          }
        },
        {
          "method": "POST",
          "path": "/courses",
          "tags": ["REQ-008"],
          "summary": "Tạo khóa học mới với kiểm tra xung đột lịch học",
          "request": {
            "schema": {
              "type": "object",
              "required": ["title", "startDate", "endDate", "teacherId"],
              "properties": {
                "title": {"type": "string", "maxLength": 150},
                "description": {"type": "string"},
                "startDate": {"type": "date"},
                "endDate": {"type": "date"},
                "teacherId": {"type": "uuid"},
                "maxStudents": {"type": "integer", "default": 30}
              }
            }
          }
        },
        {
          "method": "PUT",
          "path": "/courses/{courseId}",
          "tags": ["REQ-008"],
          "summary": "Cập nhật thông tin khóa học"
        },
        {
          "method": "DELETE",
          "path": "/courses/{courseId}",
          "tags": ["REQ-008"],
          "summary": "Xóa khóa học"
        },
        {
          "method": "POST",
          "path": "/courses/{courseId}/teachers",
          "tags": ["REQ-009"],
          "summary": "Phân công giáo viên vào khóa học",
          "request": {
            "schema": {
              "type": "object",
              "required": ["teacherId"],
              "properties": {
                "teacherId": {"type": "uuid"}
              }
            }
          }
        },
        {
          "method": "DELETE",
          "path": "/courses/{courseId}/teachers/{teacherId}",
          "tags": ["REQ-009"],
          "summary": "Thu hồi phân công giáo viên"
        }
      ],
      "events": [
        {
          "topic": "course.created",
          "tags": ["REQ-008"],
          "payload": {
            "courseId": {"type": "uuid"},
            "title": {"type": "string"},
            "startDate": {"type": "date"},
            "endDate": {"type": "date"},
            "teacherId": {"type": "uuid"}
          }
        },
        {
          "topic": "course.updated",
          "tags": ["REQ-008"],
          "payload": {
            "courseId": {"type": "uuid"},
            "updatedFields": {"type": "object"}
          }
        },
        {
          "topic": "teacher.assigned",
          "tags": ["REQ-009"],
          "payload": {
            "courseId": {"type": "uuid"},
            "teacherId": {"type": "uuid"},
            "assignedAt": {"type": "timestamp"}
          }
        }
      ]
    }
  }
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho tác vụ này.

#### 📝 Phụ công việc 2: Triển khai API phân công giáo viên vào khóa học
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/course-service/src/main/java/com/membershiphub/course/TeacherAssignmentController.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-009]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai 2 endpoint phân công giáo viên:
  - `POST /api/v1/courses/{courseId}/teachers`: Gán giáo viên vào khóa học, kiểm tra quyền của người thực hiện (chỉ System Admin được phép phân công), kiểm tra giáo viên có tồn tại và có vai trò Teacher không, sau đó lưu liên kết giáo viên - khóa học. Kích hoạt sự kiện `teacher.assigned` để hệ thống gửi thông báo cho giáo viên.
  - `DELETE /api/v1/courses/{courseId}/teachers/{teacherId}`: Thu hồi phân công giáo viên khỏi khóa học, kiểm tra quyền của người thực hiện, xóa liên kết giáo viên - khóa học.
  Đảm bảo tất cả thao tác được ghi log audit với timestamp, user ID thực hiện thao tác, chi tiết hành động (gán/thu hồi phân công) [NFR-006].

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "endpoints": [
      {
        "method": "POST",
        "path": "/api/v1/courses/{courseId}/teachers",
        "tags": ["REQ-009"],
        "request": {
          "schema": {
            "type": "object",
            "required": ["teacherId"],
            "properties": {
              "teacherId": {"type": "uuid"}
            }
          }
        },
        "response": {
          "schema": {
            "type": "object",
            "properties": {
              "courseId": {"type": "uuid"},
              "teacherId": {"type": "uuid"},
              "assignedAt": {"type": "timestamp"}
            }
          }
        }
      },
      {
        "method": "DELETE",
        "path": "/api/v1/courses/{courseId}/teachers/{teacherId}",
        "tags": ["REQ-009"],
        "response": {"statusCode": 204}
      }
    ],
    "events": [
      {
        "topic": "teacher.assigned",
        "tags": ["REQ-009"],
        "payload": {
          "courseId": {"type": "uuid"},
          "teacherId": {"type": "uuid"},
          "assignedAt": {"type": "timestamp"}
        }
      }
    ]
  }
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho tác vụ này.

#### 📝 Phụ công việc 3: Viết unit test cho dịch vụ quản lý khóa học
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseServiceTest.java`; `./sources/backend/course-service/src/test/java/com/membershiphub/course/TeacherAssignmentTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test đầy đủ cho các lớp service của `course-service`, bao gồm các trường hợp:
  - Tạo khóa học thành công với dữ liệu hợp lệ.
  - Tạo khóa học thất bại do giáo viên bị trùng lịch, trả về mã lỗi 409.
  - Cập nhật khóa học thành công, cập nhật thất bại do trùng lịch khi thay đổi giáo viên/thời gian.
  - Xóa khóa học thành công khi không có học viên đăng ký, xóa thất bại khi có học viên đăng ký.
  - Phân công giáo viên thành công, thu hồi phân công thành công.
  - Kiểm tra logic kiểm tra xung đột lịch học hoạt động đúng với các trường hợp giao nhau thời gian khác nhau.
  Đảm bảo độ phủ mã >= 90% cho tất cả các lớp service, sử dụng mock cho các phụ thuộc ngoài (repository, message broker).

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 4: Kiểm tra chất lượng mã nguồn dịch vụ khóa học
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/course-service/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review toàn bộ mã nguồn của `course-service`, bao gồm controller, service, repository, model. Kiểm tra các điểm sau:
  - Logic kiểm tra xung đột lịch học hoạt động chính xác, không có lỗi logic trong điều kiện truy vấn.
  - Tất cả truy vấn cơ sở dữ liệu sử dụng prepared statements, không có lỗ hổng SQL injection.
  - Xác thực đầu vào đầy đủ cho tất cả các endpoint, không có lỗ hổng XSS khi hiển thị dữ liệu đầu ra.
  - Logic phân quyền RBAC được thực thi đúng trên tất cả các endpoint, chỉ người dùng có quyền mới có thể thực hiện thao tác.
  - Độ phủ mã đạt ngưỡng yêu cầu >= 90%, không có code smell, tuân thủ chuẩn mã hóa Quarkus và Java 21.
  Đề xuất và thực hiện sửa lỗi tất cả các vấn đề phát hiện, đảm bảo không có lỗi bảo mật cơ bản [NFR-003].

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 5: Viết tài liệu hợp đồng API dịch vụ khóa học
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/course-service-api.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hợp đồng API REST chi tiết cho `course-service`, bao gồm:
  - Danh sách tất cả endpoint với phương thức HTTP, đường dẫn, mô tả chức năng.
  - Schema request body và response body cho từng endpoint, bao gồm kiểu dữ liệu, trường bắt buộc, trường tùy chọn, giới hạn độ dài.
  - Danh sách mã lỗi có thể trả về, mô tả nguyên nhân và cách xử lý.
  - Ví dụ sử dụng cho từng endpoint (curl command, response mẫu).
  - Mô tả logic kiểm tra xung đột lịch học, cách xử lý khi có trùng lịch.
  - Mô tả các sự kiện message broker được kích hoạt bởi service, bao gồm tên topic, schema payload, điều kiện kích hoạt.
  Đảm bảo tài liệu đầy đủ, chính xác, phù hợp với triển khai thực tế, tuân thủ chuẩn tài liệu API OpenAPI 3.0.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->Triển khai duyệt khóa học và đăng ký học viên<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai API duyệt khóa học cho học viên
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/CourseBrowseController.java`; `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-010]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `GET /api/v1/courses/available` để trả về danh sách khóa học chưa đăng ký của học viên đang đăng nhập. Logic thực hiện:
  1. Lấy `studentId` từ JWT token của người dùng đăng nhập, không cho phép truyền `studentId` từ request parameter để tránh truy cập dữ liệu của học viên khác (tuân thủ RBAC).
  2. Truy vấn danh sách tất cả khóa học đang hoạt động (chưa hết hạn), loại bỏ các khóa học mà học viên đã có bản ghi ghi danh trong bảng `enrollments`.
  3. Đối với mỗi khóa học, tính số chỗ trống còn lại = `maxStudents` - số lượng học viên đã đăng ký (`currentEnrollments`).
  4. Trả về danh sách khóa học kèm thông tin `courseId`, `title`, `startDate`, `endDate`, `maxStudents`, `currentEnrollments`.
  Đảm bảo truy vấn sử dụng prepared statements, tối ưu hiệu suất với index trên bảng `enrollments` (student_id, course_id) [NFR-001].

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "endpoints": [
      {
        "method": "GET",
        "path": "/api/v1/courses/available",
        "tags": ["REQ-010"],
        "description": "Lấy danh sách khóa học chưa đăng ký của học viên",
        "response": {
          "schema": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "courseId": {"type": "uuid"},
                "title": {"type": "string", "maxLength": 150},
                "startDate": {"type": "date"},
                "endDate": {"type": "date"},
                "maxStudents": {"type": "integer"},
                "currentEnrollments": {"type": "integer"}
              }
            }
          }
        }
      }
    ]
  }
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho tác vụ này.

#### 📝 Phụ công việc 2: Triển khai API đăng ký khóa học học viên
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentController.java`; `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-011]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `POST /api/v1/courses/{courseId}/enroll` để đăng ký khóa học cho học viên. Logic thực hiện:
  1. Lấy `studentId` từ JWT token, kiểm tra học viên đã đăng ký khóa học này chưa (truy vấn bảng `enrollments` với điều kiện `student_id` và `course_id`, nếu đã tồn tại thì trả về lỗi 409 Conflict với thông báo "Bạn đã đăng ký khóa học này").
  2. Kiểm tra khóa học còn chỗ trống không: so sánh `currentEnrollments` với `maxStudents`, nếu đã đủ thì trả về lỗi 409 Conflict với thông báo "Khóa học đã đủ số lượng học viên".
  3. Nếu học viên chưa có tài khoản cục bộ trong bảng `users` (trường hợp học viên đăng ký qua OAuth2 nhưng chưa có bản ghi cục bộ), tự động tạo tài khoản mới với vai trò 'Student', thông tin email và full_name lấy từ thông tin JWT token.
  4. Tạo bản ghi ghi danh mới trong bảng `enrollments` với `enrollment_date` là thời gian hiện tại.
  5. Kích hoạt sự kiện `student.enrolled` với payload chứa `enrollmentId`, `studentId`, `courseId`, `enrollmentDate` để hệ thống thông báo gửi thông báo cho học viên và nhóm Zalo của trung tâm.
  Đảm bảo toàn bộ quá trình thực hiện trong transaction để đảm bảo tính toàn vẹn dữ liệu, xử lý race condition khi nhiều học viên đăng ký cùng lúc bằng cách khóa bản ghi khóa học khi kiểm tra sức chứa.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "endpoints": [
      {
        "method": "POST",
        "path": "/api/v1/courses/{courseId}/enroll",
        "tags": ["REQ-011"],
        "request": {
          "schema": {
            "type": "object",
            "required": ["studentId"],
            "properties": {
              "studentId": {"type": "uuid"}
            }
          }
        },
        "response": {
          "schema": {
            "type": "object",
            "properties": {
              "enrollmentId": {"type": "uuid"},
              "studentId": {"type": "uuid"},
              "courseId": {"type": "uuid"},
              "enrollmentDate": {"type": "timestamp"}
            }
          }
        }
      }
    ],
    "events": [
      {
        "topic": "student.enrolled",
        "tags": ["REQ-011"],
        "payload": {
          "enrollmentId": {"type": "uuid"},
          "studentId": {"type": "uuid"},
          "courseId": {"type": "uuid"},
          "enrollmentDate": {"type": "timestamp"}
        }
      }
    ]
  }
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho tác vụ này.

#### 📝 Phụ công việc 3: Viết unit và integration test cho dịch vụ đăng ký khóa học
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollment-service/src/test/java/com/membershiphub/enrollment/EnrollmentServiceTest.java`; `./sources/backend/enrollment-service/src/test/java/com/membershiphub/enrollment/EnrollmentIntegrationTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test và integration test đầy đủ cho các chức năng của `enrollment-service`:
  **Unit test:**
  - Kiểm tra API duyệt khóa học trả về đúng danh sách khóa học chưa đăng ký, loại bỏ đúng các khóa học đã đăng ký.
  - Kiểm tra đăng ký khóa học thành công tạo bản ghi ghi danh đúng.
  - Kiểm tra đăng ký thất bại khi khóa học đã hết chỗ, trả về mã lỗi 409.
  - Kiểm tra đăng ký thất bại khi đã đăng ký trước đó, trả về mã lỗi 409.
  - Kiểm tra tự động tạo tài khoản học viên mới thành công khi học viên chưa có tài khoản cục bộ.
  **Integration test:**
  - Luồng đăng ký khóa học đầy đủ: học viên đăng nhập -> duyệt khóa học chưa đăng ký -> đăng ký khóa học -> kiểm tra bản ghi ghi danh được tạo đúng -> kiểm tra sự kiện `student.enrolled` được kích hoạt -> kiểm tra thông báo được gửi cho học viên và nhóm Zalo.
  - Kiểm tra các trường hợp lỗi: đăng ký khóa học đã hết chỗ, đăng ký khóa học đã đăng ký trước đó, truy cập API duyệt khóa học của học viên khác bị từ chối (403 Forbidden).
  Đảm bảo độ phủ mã >= 90% cho tất cả các lớp service và controller của `enrollment-service`.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 4: Kiểm tra chất lượng mã nguồn dịch vụ đăng ký
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollment-service/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-010], [REQ-011], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review toàn bộ mã nguồn của `enrollment-service`, bao gồm controller, service, repository, model. Kiểm tra các điểm sau:
  - Logic kiểm tra trùng lặp đăng ký hoạt động chính xác, không có lỗi cho phép đăng ký trùng.
  - Logic kiểm tra sức chứa khóa học hoạt động đúng, xử lý race condition khi nhiều học viên đăng ký cùng lúc.
  - Logic tự động tạo tài khoản học viên hoạt động đúng, không tạo tài khoản trùng lặp.
  - Tất cả truy vấn cơ sở dữ liệu sử dụng prepared statements, không có lỗ hổng SQL injection.
  - Xác thực đầu vào đầy đủ, không có lỗ hổng XSS.
  - Logic phân quyền RBAC được thực thi đúng, học viên chỉ có thể đăng ký khóa học cho chính mình, không thể đăng ký cho học viên khác.
  - Độ phủ mã đạt ngưỡng yêu cầu >= 90%, tuân thủ chuẩn mã hóa Quarkus và Java 21.
  Đề xuất và thực hiện sửa lỗi tất cả các vấn đề phát hiện, đảm bảo không có lỗi bảo mật cơ bản [NFR-003].

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 5: Viết tài liệu hợp đồng API dịch vụ đăng ký
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/enrollment-service-api.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-010], [REQ-011]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hợp đồng API REST chi tiết cho `enrollment-service`, bao gồm:
  - Danh sách tất cả endpoint với phương thức HTTP, đường dẫn, mô tả chức năng.
  - Schema request body và response body cho từng endpoint, bao gồm kiểu dữ liệu, trường bắt buộc, trường tùy chọn, giới hạn độ dài.
  - Danh sách mã lỗi có thể trả về, mô tả nguyên nhân và cách xử lý (ví dụ: lỗi đăng ký trùng lặp, lỗi khóa học hết chỗ).
  - Ví dụ sử dụng cho từng endpoint (curl command, response mẫu).
  - Mô tả logic tự động tạo tài khoản học viên, luồng thông báo sau khi đăng ký thành công.
  - Mô tả sự kiện message broker `student.enrolled` được kích hoạt bởi service, bao gồm tên topic, schema payload, điều kiện kích hoạt.
  Đảm bảo tài liệu đầy đủ, chính xác, phù hợp với triển khai thực tế, tuân thủ chuẩn tài liệu API OpenAPI 3.0.

* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.