# Giai đoạn 3: <!--PHASE_NAME_START-->Triển khai dịch vụ điểm danh QR và quản lý thẻ hội viên<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản thảo** | ARCH-20260817042313 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai dịch vụ điểm danh QR và quản lý thẻ hội viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai dịch vụ điểm danh QR có tính bất biến (idempotent) để đảm bảo mỗi học viên chỉ có một bản ghi điểm danh mỗi ngày cho mỗi khóa học, xây dựng dịch vụ quản lý thẻ hội viên với chức năng hiển thị ngày còn lại và gia hạn thẻ sau khi thanh toán thành công, xử lý các ngoại lệ liên quan đến kết nối mạng và gửi thông báo, đảm bảo tính toàn vẹn dữ liệu điểm danh và trải nghiệm người dùng liền mạch.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/08/17 04:23:13 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào việc triển khai hai microservice cốt lõi cho hệ thống điểm danh và quản lý thẻ hội viên:
1. **attendance-service**: Triển khai API quét mã QR điểm danh với tính bất biến (idempotent), đảm bảo mỗi học viên chỉ được ghi nhận điểm danh một lần duy nhất mỗi ngày cho mỗi khóa học. Xử lý các ngoại lệ về kết nối mạng (lưu hàng đợi Redis và thử lại tự động) và điểm danh trùng lặp (trả về trạng thái DUPLICATE).
2. **card-service**: Triển khai API quản lý thẻ hội viên, bao gồm hiển thị thông tin thẻ (tổng ngày hiệu lực, ngày còn lại, ngày hết hạn) và gia hạn thẻ sau khi xác nhận thanh toán thành công. Tích hợp kiểm tra tính hợp lệ của giao dịch thanh toán và kích hoạt thông báo xác nhận.
3. **Tài liệu hóa**: Viết tài liệu hợp đồng API REST chi tiết cho cả hai service, đảm bảo tuân thủ chuẩn OpenAPI 3.0.
4. **Kiểm thử**: Thực hiện kiểm thử đơn vị và tích hợp đầy đủ, đảm bảo độ phủ mã >= 90% và không có lỗi bảo mật cơ bản.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Dịch vụ Backend:**
  * `./sources/backend/attendance-service/` [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
  * `./sources/backend/card-service/` [REQ-014], [REQ-015], [DAT-007]
- **Tài liệu Kiến trúc:**
  * `./sources/docs/architecture/attendance-service-api.md` [ARC-010], [REQ-012], [REQ-013]
  * `./sources/docs/architecture/card-service-api.md` [ARC-010], [REQ-014], [REQ-015]
- **Điểm cuối API (REST):**
  * `POST /api/v1/attendance/scan` [REQ-012]
  * `GET /api/v1/attendance/student/{studentId}` [REQ-012]
  * `GET /api/v1/cards/student/{studentId}` [REQ-014]
  * `POST /api/v1/cards/{cardId}/renew` [REQ-015]
- **Chủ đề Sự kiện (Message Broker):**
  * `attendance.recorded` [REQ-012], [REQ-013]
  * `attendance.duplicate` [REQ-013], [EXC-002]
  * `card.renewed` [REQ-015]

## 3. Chỉ thị chức năng chuyên biệt cho Đại lý phụ
* **Coder**: Làm việc như Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên 2 dịch vụ backend `attendance-service` và `card-service`. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
* **Tester**: Làm việc như Kiểm soát chất lượng/QA chính. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo kiểm thử đơn vị, kiểm thử tích hợp và kịch bản xác thực hiệu suất. Bị cấm sửa đổi mã nguồn sản xuất. Nếu phạm vi tác vụ mục tiêu là tích hợp/E2E không có tệp mã nguồn cụ thể, phải xuất ra token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp đường dẫn phân tách bằng dấu chấm phẩy.
* **Doc**: Hoạt động như Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên biên soạn tài liệu Thông số kỹ thuật, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp công nghệ đang hoạt động của dự án. Mọi tệp tài liệu kỹ thuật được tạo phải có đuôi `.md` và nằm strictly trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Chịu trách nhiệm xác minh biên dịch, kiểm soát phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗi bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.

## 4. Định nghĩa Hoàn thành của Giai đoạn (DoD)
1. Tất cả công việc của giai đoạn 3 đã được triển khai và kiểm thử thành công.
2. 100% thẻ theo dõi [REQ-012] đến [REQ-015], [EXC-001], [EXC-002] được ánh xạ và bao phủ đầy đủ.
3. Độ phủ mã đạt >= 90% cho các lớp service và controller của `attendance-service` và `card-service`.
4. Tất cả endpoint API hoạt động đúng theo hợp đồng đã định nghĩa, bao gồm logic điểm danh bất biến hoạt động chính xác.
5. Luồng gia hạn thẻ hoạt động đúng, bao gồm kiểm tra tính hợp lệ của giao dịch thanh toán, cập nhật ngày hết hạn và gửi thông báo xác nhận.
6. Tất cả sự kiện message broker được kích hoạt đúng khi có thay đổi nghiệp vụ (điểm danh thành công, điểm danh trùng lặp, gia hạn thẻ).
7. Tài liệu hợp đồng API cho `attendance-service` và `card-service` được hoàn thiện đầy đủ, chính xác, tuân thủ chuẩn OpenAPI 3.0.
8. Không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) được phát hiện trong quá trình code review, tuân thủ đầy đủ OWASP Top 10 [NFR-003].
9. Tất cả unit test và integration test đều vượt qua, đáp ứng ngưỡng độ phủ mã yêu cầu.

## 5. Nhật ký thực thi kiến trúc theo từng ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->Triển khai dịch vụ điểm danh QR và logic bất biến điểm danh<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai logic cốt lõi của dịch vụ điểm danh QR
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceController.java`; `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java`; `./sources/backend/attendance-service/src/main/resources/db/migration/V2__add_attendance_unique_constraint.sql`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai endpoint `POST /api/v1/attendance/scan` để xử lý yêu cầu quét mã QR điểm danh: nhận payload chứa mã QR khóa học và ID học viên, xác thực học viên đã đăng ký khóa học tương ứng với mã QR, tạo bản ghi điểm danh với thời gian hiện tại. Triển khai logic kiểm tra trùng lặp điểm danh dựa trên ràng buộc duy nhất (student_id, course_id, attendance_date) để đảm bảo chỉ tạo một bản ghi điểm danh mỗi ngày cho mỗi học viên và khóa học. Triển khai xử lý yêu cầu thử lại khi lỗi kết nối mạng, đảm bảo điểm danh được ghi nhận đúng một lần sau khi kết nối được khôi phục.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:**
```sql
-- Thêm ràng buộc duy nhất cho bảng điểm danh để đảm bảo tính bất biến (mỗi học viên chỉ điểm danh 1 lần/ngày/khóa học) [DAT-006], [REQ-013]
ALTER TABLE attendance
ADD CONSTRAINT uk_student_course_date UNIQUE (student_id, course_id, attendance_date);
```
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
```json
{
  "services": [
    {
      "serviceName": "attendance-service",
      "version": "v1",
      "endpoints": [
        {
          "method": "POST",
          "path": "/api/v1/attendance/scan",
          "tags": ["REQ-012"],
          "request": {
            "schema": {
              "type": "object",
              "required": ["qrCode", "studentId"],
              "properties": {
                "qrCode": {"type": "string", "description": "Mã QR của khóa học"},
                "studentId": {"type": "uuid", "description": "ID học viên quét mã"}
              }
            }
          },
          "response": {
            "schema": {
              "type": "object",
              "properties": {
                "attendanceId": {"type": "uuid"},
                "status": {"type": "string", "enum": ["RECORDED", "DUPLICATE"]},
                "message": {"type": "string"}
              }
            }
          }
        },
        {
          "method": "GET",
          "path": "/api/v1/attendance/student/{studentId}",
          "tags": ["REQ-012"],
          "response": {
            "schema": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "attendanceId": {"type": "uuid"},
                  "courseId": {"type": "uuid"},
                  "courseName": {"type": "string"},
                  "attendanceDate": {"type": "date"},
                  "timestamp": {"type": "timestamp"},
                  "status": {"type": "string"}
                }
              }
            }
          }
        }
      ],
      "events": [
        {
          "topic": "attendance.recorded",
          "tags": ["REQ-012", "REQ-013"],
          "payload": {
            "attendanceId": {"type": "uuid"},
            "studentId": {"type": "uuid"},
            "courseId": {"type": "uuid"},
            "attendanceDate": {"type": "date"},
            "timestamp": {"type": "timestamp"}
          }
        },
        {
          "topic": "attendance.duplicate",
          "tags": ["REQ-013", "EXC-002"],
          "payload": {
            "studentId": {"type": "uuid"},
            "courseId": {"type": "uuid"},
            "attendanceDate": {"type": "date"}
          }
        }
      ]
    }
  ]
}
```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ [EXC-001] (lỗi kết nối mạng) bằng cách lưu tạm yêu cầu điểm danh vào hàng đợi Redis khi không thể kết nối cơ sở dữ liệu, tự động xử lý hàng đợi khi kết nối được khôi phục. Triển khai xử lý ngoại lệ [EXC-002] (điểm danh trùng lặp) bằng cách bắt lỗi vi phạm ràng buộc duy nhất, trả về trạng thái `DUPLICATE` và thông báo "Bạn đã điểm danh cho khóa học này trong ngày hôm nay".

#### 📝 Phụ công việc 2: Viết unit test cho dịch vụ điểm danh
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java;./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/AttendanceServiceTest.java`; `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceController.java;./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/AttendanceControllerTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: quét mã QR thành công và tạo bản ghi điểm danh, quét mã QR trùng lặp trong cùng ngày trả về trạng thái DUPLICATE, quét mã QR khi học viên chưa đăng ký khóa học trả về lỗi 403 Forbidden, quét mã QR không hợp lệ trả về lỗi 400 Bad Request, xử lý yêu cầu khi kết nối mạng bị gián đoạn và thử lại sau khi khôi phục. Đảm bảo độ phủ mã ít nhất 90% cho các lớp xử lý điểm danh.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 3: Kiểm tra chất lượng mã nguồn dịch vụ điểm danh
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002], [NFR-001]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn attendance-service, kiểm tra logic kiểm tra trùng lặp điểm danh hoạt động đúng, đảm bảo không có lỗi logic trong xử lý mã QR và xác thực quan hệ học viên-khóa học, kiểm tra hiệu suất truy vấn cơ sở dữ liệu đảm bảo độ trễ API trung bình dưới 200ms [NFR-001], kiểm tra không có lỗi bảo mật cơ bản (SQL injection, XSS). Đề xuất và thực hiện sửa lỗi nếu có.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->Triển khai quản lý thẻ hội viên và gia hạn thẻ<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai logic cốt lõi của dịch vụ quản lý thẻ hội viên
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/card-service/src/main/java/com/membershiphub/card/CardController.java`; `./sources/backend/card-service/src/main/java/com/membershiphub/card/CardService.java`; `./sources/backend/card-service/src/main/resources/db/migration/V2__add_card_check_constraints.sql`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai endpoint `GET /api/v1/cards/student/{studentId}` để trả về thông tin thẻ hội viên của học viên: tổng ngày hiệu lực, ngày đã sử dụng, ngày còn lại, ngày hết hạn. Triển khai endpoint `POST /api/v1/cards/{cardId}/renew` để gia hạn thẻ: nhận số ngày gia hạn và ID giao dịch thanh toán thành công, cập nhật ngày hết hạn của thẻ, tính toán lại số ngày còn lại, kích hoạt sự kiện `card.renewed` để gửi thông báo xác nhận cho học viên. Triển khai logic kiểm tra tính hợp lệ của giao dịch thanh toán trước khi cập nhật thẻ.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:**
```sql
-- Thêm ràng buộc CHECK cho bảng thẻ hội viên để đảm bảo ngày còn lại không âm và không vượt quá tổng ngày hiệu lực [DAT-007], [REQ-014]
ALTER TABLE student_cards
ADD CONSTRAINT chk_remaining_days CHECK (remaining_days >= 0 AND remaining_days <= validity_days);
```
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
```json
{
  "services": [
    {
      "serviceName": "card-service",
      "version": "v1",
      "endpoints": [
        {
          "method": "GET",
          "path": "/api/v1/cards/student/{studentId}",
          "tags": ["REQ-014"],
          "response": {
            "schema": {
              "type": "object",
              "properties": {
                "cardId": {"type": "uuid"},
                "studentId": {"type": "uuid"},
                "issueDate": {"type": "date"},
                "validityDays": {"type": "integer"},
                "remainingDays": {"type": "integer"},
                "expiryDate": {"type": "date"}
              }
            }
          }
        },
        {
          "method": "POST",
          "path": "/api/v1/cards/{cardId}/renew",
          "tags": ["REQ-015"],
          "request": {
            "schema": {
              "type": "object",
              "required": ["renewalDays", "paymentId"],
              "properties": {
                "renewalDays": {"type": "integer", "description": "Số ngày gia hạn"},
                "paymentId": {"type": "uuid", "description": "ID giao dịch thanh toán thành công"}
              }
            }
          },
          "response": {
            "schema": {
              "type": "object",
              "properties": {
                "cardId": {"type": "uuid"},
                "newExpiryDate": {"type": "date"},
                "remainingDays": {"type": "integer"}
              }
            }
          }
        }
      ],
      "events": [
        {
          "topic": "card.renewed",
          "tags": ["REQ-015"],
          "payload": {
            "cardId": {"type": "uuid"},
            "studentId": {"type": "uuid"},
            "newExpiryDate": {"type": "date"},
            "renewalDays": {"type": "integer"}
          }
        }
      ]
    }
  ]
}
```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ khi giao dịch thanh toán không hợp lệ, trả về mã lỗi 402 Payment Required với thông báo "Giao dịch thanh toán không hợp lệ hoặc đã hết hạn". Triển khai xử lý ngoại lệ khi thẻ hội viên không tồn tại, trả về mã lỗi 404 Not Found.

#### 📝 Phụ công việc 2: Viết unit và integration test cho dịch vụ quản lý thẻ
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/card-service/src/main/java/com/membershiphub/card/CardService.java;./sources/backend/card-service/src/test/java/com/membershiphub/card/CardServiceTest.java`; `INTEGRATION_SCOPE;./sources/backend/card-service/src/test/java/com/membershiphub/card/CardIntegrationTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: lấy thông tin thẻ hội viên thành công, gia hạn thẻ thành công với số ngày hợp lệ, gia hạn thẻ thất bại với giao dịch thanh toán không hợp lệ, gia hạn thẻ thất bại khi thẻ không tồn tại. Viết integration test cho luồng gia hạn thẻ: gửi yêu cầu gia hạn -> kiểm tra thông tin thẻ được cập nhật -> kiểm tra sự kiện `card.renewed` được kích hoạt -> kiểm tra thông báo được gửi cho học viên. Đảm bảo độ phủ mã ít nhất 90% cho các lớp xử lý thẻ hội viên.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 3: Viết tài liệu hợp đồng API cho dịch vụ điểm danh và quản lý thẻ
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/attendance-service-api.md`; `./sources/docs/architecture/card-service-api.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-012], [REQ-013], [REQ-014], [REQ-015]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho attendance-service và card-service, bao gồm phương thức HTTP, đường dẫn, schema request/response, mã lỗi, ví dụ sử dụng. Mô tả logic kiểm tra trùng lặp điểm danh, quy tắc tính ngày còn lại của thẻ hội viên, quy trình gia hạn thẻ và tích hợp thanh toán.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 4: Kiểm tra cuối cùng và xác nhận hoàn thành giai đoạn 3
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/`; `./sources/backend/card-service/`; `./sources/docs/architecture/attendance-service-api.md`; `./sources/docs/architecture/card-service-api.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [REQ-014], [REQ-015], [EXC-001], [EXC-002], [DAT-006], [DAT-007], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra cuối cùng toàn bộ sản phẩm của giai đoạn 3, đảm bảo tất cả các yêu cầu và thẻ theo dõi đã được triển khai đầy đủ: logic điểm danh bất biến hoạt động đúng, chức năng hiển thị và gia hạn thẻ hoạt động chính xác, các ngoại lệ được xử lý đúng, tài liệu API đầy đủ và chính xác, không có lỗi còn tồn tại, xác nhận giai đoạn sẵn sàng cho giai đoạn tiếp theo.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.