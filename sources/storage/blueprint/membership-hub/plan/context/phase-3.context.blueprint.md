# Giai đoạn 3: <!--PHASE_NAME_START-->Triển khai điểm danh QR, quản lý thẻ hội viên, thông báo đa kênh và khuyến mãi<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã bản thiết kế** | ARCH-20260822094056 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai điểm danh QR, quản lý thẻ hội viên, thông báo đa kênh và khuyến mãi<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai các tính năng vận hành cốt lõi của hệ thống, bao gồm chức năng điểm danh quét mã QR với tính bất biến chống trùng lặp bản ghi, quản lý thẻ hội viên (hiển thị số ngày còn lại hiệu lực, gia hạn thẻ sau thanh toán), hệ thống thông báo đa kênh (push notification, tin nhắn nhóm Zalo) với cơ chế tự động thử lại khi gửi thất bại, quản lý khuyến mãi và thông báo hệ thống (CRUD với ngày hết hạn tùy chọn, tự động ẩn thông báo hết hạn), đảm bảo tất cả quy tắc nghiệp vụ liên quan đến tương tác của học viên và vận hành trung tâm được đáp ứng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/22 09:40:56 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào triển khai các tính năng vận hành cốt lõi của hệ thống membership-hub, bao gồm bốn nhóm dịch vụ vi mô chính: attendance-service (điểm danh QR với tính idempotent), membership-service (quản lý thẻ hội viên), notification-service (thông báo đa kênh với cơ chế retry), và promotion-service (khuyến mãi cùng thông báo hệ thống). Mục tiêu kỹ thuật cốt lõi bao gồm: đảm bảo tính bất biến của bản ghi điểm danh (một học viên chỉ có một bản ghi điểm danh duy nhất cho mỗi khóa học trong mỗi ngày), triển khai cơ chế tự động thử lại gửi thông báo tối đa 3 lần khi gửi thất bại, xây dựng giao diện frontend responsive cho các chức năng điểm danh, thẻ hội viên, thông báo và khuyến mãi, đồng thời đảm bảo tuân thủ nghiêm ngặt các ràng buộc RBAC, OWASP Top 10, và yêu cầu phi chức năng về hiệu năng, bảo mật và khả năng sẵn sàng.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục
Tất cả đường dẫn tệp đều bắt đầu với gốc kho lưu trữ `./sources/`, tuân thủ cấu trúc kiến trúc vi mô đã định nghĩa:
* **Hạ tầng backend vi mô Quarkus (dịch vụ đã được khởi tạo trong Giai đoạn 1):**
  * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java [REQ-012, EXC-001, EXC-002, REQ-013]
  * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceController.java [REQ-012, REQ-013, ARC-007]
  * ./sources/backend/attendance-service/src/main/resources/db/migration/V1_0_0__create_attendance_table.sql [DAT-006]
  * ./sources/backend/membership-service/src/main/java/org/nlh4j/membership_hub/membership/MembershipService.java [REQ-014, REQ-015]
  * ./sources/backend/membership-service/src/main/java/org/nlh4j/membership_hub/membership/MembershipController.java [REQ-014, REQ-015, ARC-009]
  * ./sources/backend/membership-service/src/main/resources/db/migration/V1_0_0__create_student_cards_table.sql [DAT-007]
  * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/NotificationService.java [REQ-016, EXC-003]
  * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/NotificationController.java [REQ-016, ARC-008]
  * ./sources/backend/notification-service/src/main/resources/db/migration/V1_0_0__create_notifications_table.sql [DAT-008]
  * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/PromotionService.java [REQ-017]
  * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/PromotionController.java [REQ-017]
  * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/announcement/AnnouncementService.java [REQ-018]
  * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/announcement/AnnouncementController.java [REQ-018]
  * ./sources/backend/promotion-service/src/main/resources/db/migration/V1_0_0__create_promotions_announcements_tables.sql [DAT-009]
* **Lớp frontend Next.js:**
  * ./sources/frontend/src/app/attendance/page.tsx [REQ-012, REQ-013]
  * ./sources/frontend/src/app/membership-card/page.tsx [REQ-014, REQ-015]
  * ./sources/frontend/src/app/notifications/page.tsx [REQ-016]
  * ./sources/frontend/src/app/promotions/page.tsx [REQ-017, REQ-018]
* **Tài liệu doanh nghiệp:**
  * ./sources/docs/attendance-service-api-spec.md [REQ-012, REQ-013, ARC-007]
  * ./sources/docs/membership-service-api-spec.md [REQ-014, REQ-015]
  * ./sources/docs/notification-service-api-spec.md [REQ-016, ARC-008]
  * ./sources/docs/promotion-service-api-spec.md [REQ-017, REQ-018]
* **Tệp kiểm thử:**
  * ./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceServiceTest.java [REQ-012, EXC-001, EXC-002, REQ-013]
  * ./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceControllerIntegrationTest.java [REQ-012, EXC-001, ARC-007]
  * ./sources/backend/membership-service/src/test/java/org/nlh4j/membership_hub/membership/MembershipServiceTest.java [REQ-014, REQ-015]
  * ./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/NotificationServiceTest.java [REQ-016, EXC-003]
  * ./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/PromotionServiceTest.java [REQ-017]
  * ./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/announcement/AnnouncementServiceTest.java [REQ-018]
  * ./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/NotificationControllerIntegrationTest.java [REQ-016, EXC-003]
  * ./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/PromotionControllerIntegrationTest.java [REQ-017]
  * ./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/announcement/AnnouncementControllerIntegrationTest.java [REQ-018]

## 3. Chỉ thị chức năng cho tác nhân phụ chuyên dụng
* **Coder**: Đóng vai trò là Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên cả backend services (attendance-service, membership-service, notification-service, promotion-service) và frontend/ứng dụng di động. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
* **Tester**: Đóng vai trò là Kiểm soát chất lượng (QC/QA) cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác thực hiệu năng. Bị cấm sửa mã nguồn sản xuất. Nếu mục tiêu nhiệm vụ liên quan đến phạm vi kiểm thử tích hợp hoặc end-to-end mà không có tệp mã ứng dụng cụ thể nào có thể bị giới hạn, bạn PHẢI xuất ra literal token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp dấu chấm phẩy.
* **Doc**: Hoạt động như là Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Đặc tả kỹ thuật toàn diện, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp kiến trúc đang hoạt động của dự án. Mỗi tệp tài liệu kỹ thuật được tạo PHẢI được liệt kê là thực thể đường dẫn tệp cụ thể có phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Chịu trách nhiệm xác minh trình biên dịch, cổng phân tích tĩnh và vá bảo vệ phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗi hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
Giai đoạn 3 được coi là hoàn thành khi đáp ứng đầy đủ các mốc định lượng sau:
1. Dịch vụ attendance-service được triển khai đầy đủ chức năng quét mã QR điểm danh với cơ chế idempotent, đảm bảo chỉ tạo một bản gị điểm danh duy nhất cho mỗi học viên/khóa học/ngày, xử lý yêu cầu trùng lặp trả về cờ DUPLICATE.
2. Dịch vụ membership-service được triển khai đầy đủ chức năng hiển thị số ngày còn lại thẻ hội viên và gia hạn thẻ sau thanh toán, tích hợp với bảng student_cards.
3. Dịch vụ notification-service được triển khai hệ thống thông báo đa kênh (push notification, tin nhắn Zalo) với cơ chế retry tự động tối đa 3 lần khi gửi thất bại, ghi nhật ký lỗi chi tiết.
4. Dịch vụ promotion-service được triển khai đầy đủ chức năng CRUD khuyến mãi và thông báo hệ thống với ngày hết hạn tùy chọn, tự động ẩn thông báo sau ngày hết hạn.
5. Giao diện frontend cho điểm danh, thẻ hội viên, thông báo và khuyến mãi được triển khai responsive, tích hợp đầy đủ với backend APIs, hỗ trợ đa ngôn ngữ.
6. Tất cả bộ kiểm thử đơn vị và tích hợp cho bốn dịch vụ vi mô đều vượt qua, độ bao phủ mã đạt >= 85%.
7. Tất cả thẻ theo dõi yêu cầu được phân phối cho giai đoạn 3 ([REQ-012] đến [REQ-018], [EXC-001], [EXC-002], [EXC-003]) được ánh xạ đầy đủ vào các nhiệm vụ kỹ thuật và tài liệu, không có thẻ nào bị thiếu.
8. Tài liệu API cho attendance, membership, notification và promotion được hoàn thiện đầy đủ, tuân thủ chuẩn OpenAPI 3.0.
9. Không có lỗ hổng bảo mật OWASP Top 10 được phát hiện trong mã nguồn giai đoạn 3, tất cả đầu vào người dùng được xác thực, truy vấn cơ sở dữ liệu sử dụng prepared statements.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC TỪNG NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Triển khai cốt lõi dịch vụ điểm danh và kiểm thử đơn vị<!--DAY_HEADER_END-->

#### 📝 Công việc con 1.1: Xây dựng logic nghiệp vụ cốt lõi dịch vụ điểm danh và migration cơ sở dữ liệu
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [EXC-001], [EXC-002], [REQ-013], [DAT-006]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ cốt lõi của dịch vụ điểm danh, bao gồm xác thực quan hệ học viên-khóa học (kiểm tra student_id có tồn tại trong bảng users và đã đăng ký khóa học trong bảng enrollments), triển khai cơ chế idempotent để đảm bảo chỉ tạo một bản ghi điểm danh duy nhất cho mỗi học viên/khóa học/ngày thông qua ràng buộc duy nhất unique_attendance_per_student_course_day, xử lý yêu cầu quét mã QR trùng lặp bằng cách kiểm tra sự tồn tại của bản ghi trước khi insert, ném ngoại lệ nghiệp vụ khi học viên chưa đăng ký khóa học hoặc khóa học không tồn tại. Đồng thời tạo script migration DDL SQL cho bảng attendance với đầy đủ ràng buộc khóa ngoại và ràng buộc duy nhất.

<!--START_DDL_MIGRATION-->
```sql
-- Tạo bảng điểm danh [DAT-006]
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_attendance_per_student_course_day UNIQUE (student_id, course_id, attendance_date)
);
```
<!--END_DDL_MIGRATION-->

#### 📝 Công việc con 1.2: Xây dựng endpoint REST cho dịch vụ điểm danh
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [ARC-007]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST POST /api/attendance/scan để nhận payload quét mã QR từ ứng dụng di động (studentId, courseId, qrToken), xác thực JWT Bearer Token, kiểm tra quyền RBAC (chỉ học viên có vai trò Student được phép quét mã), endpoint GET /api/attendance/course/{courseId}/date/{date} để truy xuất danh sách điểm danh của khóa học trong ngày được chỉ định (chỉ giáo viên phụ trách và quản trị viên có quyền xem). Áp dụng xác thực đầu vào request, chuẩn hóa phản hồi JSON theo hợp đồng API đã định nghĩa, xử lý ngoại lệ trả về mã lỗi 400 cho yêu cầu không hợp lệ và 404 cho khóa học không tồn tại.

<!--START_API_CONTRACT-->
```json
{
  "attendanceApi": {
    "basePath": "/api/attendance",
    "endpoints": [
      {
        "method": "POST",
        "path": "/scan",
        "description": "Record attendance via QR scan",
        "requestSchema": {
          "studentId": "uuid",
          "courseId": "uuid",
          "qrToken": "string"
        },
        "responseSchema": {
          "attendanceId": "uuid",
          "timestamp": "timestamp",
          "status": "RECORDED | DUPLICATE"
        },
        "auth": "Bearer JWT",
        "rbac": ["Student"]
      },
      {
        "method": "GET",
        "path": "/course/{courseId}/date/{date}",
        "description": "Get attendance list for course on specific date",
        "requestSchema": null,
        "responseSchema": {
          "type": "array",
          "items": {
            "attendanceId": "uuid",
            "studentId": "uuid",
            "studentName": "string",
            "timestamp": "timestamp",
            "status": "string"
          }
        },
        "auth": "Bearer JWT",
        "rbac": ["Teacher", "Center Admin", "System Admin"]
      }
    ]
  }
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
// EXC-001: Network & Connectivity Drops During QR Scan
// Ứng dụng di động lưu payload quét vào bộ nhớ cục bộ và tự động gửi lại khi kết nối khôi phục
// EXC-002: Duplicate Attendance Submission
// Hệ thống phát hiện trùng lặp dựa trên ràng buộc duy nhất (student_id, course_id, attendance_date)
// Trả về phản hồi thành công với cờ "already_recorded" và không tạo bản ghi bổ sung
```
<!--END_EXC_HANDLER-->

#### 📝 Công việc con 1.3: Viết kiểm thử đơn vị cho dịch vụ điểm danh
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [EXC-001], [EXC-002], [REQ-013]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị toàn diện cho AttendanceService sử dụng JUnit 5 và Mockito, bao gồm các kịch bản: quét mã QR hợp lệ tạo bản ghi điểm danh mới thành công, quét mã QR trùng lặp trong cùng ngày trả về cờ DUPLICATE và không tạo bản ghi mới, xử lý lỗi khi học viên không đăng ký khóa học (ném ngoại lệ EnrollmentNotFoundException), xử lý lỗi khi khóa học không tồn tại, xác minh cơ chế idempotent hoạt động chính xác qua kiểm tra số lượng bản ghi trong cơ sở dữ liệu. Đảm bảo độ bao phủ mã >= 90%.

#### 📝 Công việc con 1.4: Viết kiểm thử tích hợp cho endpoint điểm danh
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceControllerIntegrationTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [EXC-001], [ARC-007]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm thử tích hợp cho endpoint /api/attendance/scan sử dụng Testcontainers với PostgreSQL, mô phỏng payload quét mã QR từ ứng dụng di động với JWT token hợp lệ, xác minh phản hồi API chính xác (status RECORDED hoặc DUPLICATE), xác minh bản ghi điểm danh được lưu vào cơ sở dữ liệu với đúng student_id, course_id, attendance_date, xác minh xử lý yêu cầu trùng lặp hoạt động đúng (không tạo bản ghi mới). Kiểm tra xác thực JWT và phân quyền RBAC.

#### 📝 Công việc con 1.5: Soạn thảo tài liệu đặc tả API dịch vụ điểm danh
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/attendance-service-api-spec.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [ARC-007]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Soạn thảo tài liệu đặc tả API cho dịch vụ điểm danh theo chuẩn OpenAPI 3.0, bao gồm mô tả endpoint POST /api/attendance/scan và GET /api/attendance/course/{courseId}/date/{date}, schema request/response chi tiết, mã lỗi (400, 401, 403, 404), luồng xử lý điểm danh trùng lặp, tích hợp với luồng quét mã QR, yêu cầu xác thực JWT và phân quyền RBAC, kèm ví dụ payload thực tế và hướng dẫn tích hợp frontend.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Triển khai cốt lõi dịch vụ thẻ hội viên và thông báo<!--DAY_HEADER_END-->

#### 📝 Công việc con 2.1: Xây dựng logic nghiệp vụ cốt lõi dịch vụ thẻ hội viên và migration cơ sở dữ liệu
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/membership-service/src/main/java/org/nlh4j/membership_hub/membership/MembershipService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ quản lý thẻ hội viên, bao gồm tính toán số ngày còn lại hiệu lực (remaining_days = validity_days - số ngày đã sử dụng), xử lý yêu cầu gia hạn thẻ sau khi xác nhận thanh toán bằng cách cập nhật remaining_days và issue_date, đảm bảo remaining_days không bao giờ âm (CHECK constraint), tích hợp với bảng student_cards cơ sở dữ liệu. Đồng thời tạo script migration DDL SQL cho bảng student_cards với các ràng buộc kiểm tra tính hợp lệ của trường validity_days và remaining_days.

<!--START_DDL_MIGRATION-->
```sql
-- Tạo bảng thẻ hội viên [DAT-007]
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL UNIQUE REFERENCES users(user_id),
    issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
    validity_days INT NOT NULL CHECK (validity_days > 0),
    remaining_days INT NOT NULL CHECK (remaining_days >= 0)
);
```
<!--END_DDL_MIGRATION-->

#### 📝 Công việc con 2.2: Xây dựng endpoint REST cho dịch vụ thẻ hội viên
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/membership-service/src/main/java/org/nlh4j/membership_hub/membership/MembershipController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-014], [REQ-015], [ARC-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST GET /api/membership/card để lấy thông tin thẻ hội viên của học viên đang đăng nhập (cardId, issueDate, validityDays, remainingDays), endpoint POST /api/membership/renew để xử lý yêu cầu gia hạn thẻ với tham số renewalDays và paymentTransactionId, áp dụng xác thực JWT và kiểm tra quyền truy cập của học viên (chỉ học viên sở hữu thẻ mới được phép xem/gia hạn). Trả về phản hồi JSON với newRemainingDays và newExpiryDate sau khi gia hạn thành công.

#### 📝 Công việc con 2.3: Xây dựng logic nghiệp vụ cốt lõi dịch vụ thông báo và migration cơ sở dữ liệu
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/NotificationService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-016], [EXC-003], [DAT-008]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ hệ thống thông báo đa kênh, bao gồm xếp hàng thông báo đẩy (FCM/APNs) và tin nhắn nhóm Zalo, triển khai cơ chế retry tự động tối đa 3 lần khi gửi thất bại với khoảng cách tăng dần (exponential backoff), ghi nhật ký lỗi gửi thông báo chi tiết vào trường message của bảng notifications, tích hợp với bảng notifications cơ sở dữ liệu. Đồng thời tạo script migration DDL SQL cho bảng notifications với ràng buộc retry_count từ 0 đến 3.

<!--START_DDL_MIGRATION-->
```sql
-- Tạo bảng thông báo [DAT-008]
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NULL REFERENCES users(user_id),
    group_zalo VARCHAR(255) NULL,
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    retry_count INT NOT NULL DEFAULT 0 CHECK (retry_count BETWEEN 0 AND 3)
);
```
<!--END_DDL_MIGRATION-->

<!--START_EXC_HANDLER-->
```java
// EXC-003: Failed Notification Delivery
// Nếu thông báo đẩy không thể gửi đến thiết bị (token không hợp lệ), hệ thống ghi lại lỗi vào bảng notifications
// Tự động thử lại tối đa 3 lần với khoảng cách tăng dần, sau đó đánh dấu trạng thái "thất bại"
// và ghi nhật ký cho đội ngũ vận hành để xử lý thủ công
```
<!--END_EXC_HANDLER-->

#### 📝 Công việc con 2.4: Viết kiểm thử đơn vị cho dịch vụ thẻ hội viên
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/membership-service/src/test/java/org/nlh4j/membership_hub/membership/MembershipServiceTest.java;./sources/backend/membership-service/src/main/java/org/nlh4j/membership_hub/membership/MembershipService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị toàn diện cho MembershipService sử dụng JUnit 5 và Mockito, bao gồm các trường hợp: tính toán số ngày còn lại thẻ chính xác dựa trên issue_date và validity_days, xử lý yêu cầu gia hạn thẻ cập nhật remaining_days và issue_date đúng, xử lý lỗi khi renewalDays <= 0 (ném ngoại lệ IllegalArgumentException), xử lý lỗi khi paymentTransactionId không hợp lệ, đảm bảo remaining_days không bao giờ vượt quá giá trị tối đa cho phép. Đảm bảo độ bao phủ mã >= 90%.

#### 📝 Công việc con 2.5: Viết kiểm thử đơn vị cho dịch vụ thông báo
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/NotificationService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-016], [EXC-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị toàn diện cho NotificationService sử dụng JUnit 5 và Mockito, bao gồm các trường hợp: xếp hàng thông báo đẩy và Zalo thành công với đúng payload, xử lý retry tự động khi gửi thất bại (giả lập lỗi FCM/APNs), đánh dấu thông báo là thất bại sau 3 lần thử không thành công, ghi nhật ký lỗi gửi thông báo chi tiết, xác minh retry_count được tăng đúng sau mỗi lần thử. Đảm bảo độ bao phủ mã >= 90%.

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Triển khai dịch vụ khuyến mãi, thông báo hệ thống và giao diện frontend liên quan<!--DAY_HEADER_END-->

#### 📝 Công việc con 3.1: Xây dựng endpoint REST cho dịch vụ thông báo
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/NotificationController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-016], [ARC-008]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST POST /api/notifications/send để kích hoạt gửi thông báo đa kênh, nhận payload gồm userId (tùy chọn), groupZalo (tùy chọn), message, và danh sách channels (PUSH, ZALO), tích hợp với dịch vụ FCM/APNs và Zalo API, xử lý phân phối thông báo đến người dùng hoặc nhóm Zalo mục tiêu, trả về notificationId và status (QUEUED hoặc FAILED). Áp dụng xác thực JWT và kiểm soát quyền truy cập theo RBAC.

#### 📝 Công việc con 3.2: Xây dựng logic nghiệp vụ dịch vụ khuyến mãi và migration cơ sở dữ liệu
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/PromotionService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-017], [DAT-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ quản lý khuyến mãi, bao gồm CRUD khuyến mãi với kiểm tra tính hợp lệ của ngày bắt đầu/kết thúc (end_date >= start_date), lọc khuyến mãi đang hoạt động cho học viên dựa trên ngày hiện tại nằm trong khoảng start_date đến end_date, đảm bảo mã khuyến mãi (code) là duy nhất, tích hợp với bảng promotions cơ sở dữ liệu. Đồng thời tạo script migration DDL SQL cho bảng promotions với ràng buộc kiểm tra phần trăm giảm giá (1-100) và tính hợp lệ của ngày hiệu lực.

<!--START_DDL_MIGRATION-->
```sql
-- Tạo bảng khuyến mãi [DAT-009]
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL CHECK (discount_percent BETWEEN 1 AND 100),
    start_date DATE NULL,
    end_date DATE NULL,
    description TEXT NULL,
    CHECK (end_date IS NULL OR end_date >= start_date)
);
```
<!--END_DDL_MIGRATION-->

#### 📝 Công việc con 3.3: Xây dựng logic nghiệp vụ dịch vụ thông báo hệ thống và migration cơ sở dữ liệu
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/announcement/AnnouncementService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-018], [DAT-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ quản lý thông báo hệ thống, bao gồm CRUD thông báo với ngày hết hạn tùy chọn, tự động ẩn thông báo sau ngày hết hạn bằng cách lọc theo điều kiện end_date IS NULL OR end_date >= CURRENT_DATE, phát sóng thông báo toàn hệ thống, đảm bảo nội dung thông báo không vượt quá 2000 ký tự (CHECK constraint), tích hợp với bảng announcements cơ sở dữ liệu.

<!--START_DDL_MIGRATION-->
```sql
-- Tạo bảng thông báo hệ thống [DAT-009]
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL CHECK (LENGTH(content) <= 2000),
    start_date DATE NULL DEFAULT CURRENT_DATE,
    end_date DATE NULL,
    CHECK (end_date IS NULL OR end_date >= start_date)
);
```
<!--END_DDL_MIGRATION-->

#### 📝 Công việc con 3.4: Xây dựng giao diện frontend cho điểm danh và thẻ hội viên
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/app/attendance/page.tsx;./sources/frontend/src/app/membership-card/page.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [REQ-014], [REQ-015]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng giao diện trang điểm danh cho học viên với tích hợp camera quét mã QR sử dụng thư viện html5-qrcode, hiển thị trạng thái điểm danh (thành công, trùng lặp, lỗi) sau khi quét, tự động đồng bộ với backend khi kết nối mạng khôi phục. Xây dựng giao diện trang thẻ hội viên hiển thị số ngày còn lại hiệu lực, ngày phát hành, tổng số ngày hiệu lực, nút gia hạn thẻ với lựa chọn thời hạn gia hạn (30, 60, 90 ngày), tích hợp thanh toán giả lập. Đảm bảo giao diện responsive, hỗ trợ đa ngôn ngữ qua i18next, đồng bộ trạng thái với backend qua REST API.

#### 📝 Công việc con 3.5: Viết kiểm thử đơn vị cho dịch vụ khuyến mãi và thông báo hệ thống
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/PromotionServiceTest.java;./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/announcement/AnnouncementServiceTest.java;./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/PromotionService.java;./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/announcement/AnnouncementService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị toàn diện cho PromotionService và AnnouncementService sử dụng JUnit 5 và Mockito, bao gồm các trường hợp: tạo khuyến mãi với ngày hết hạn hợp lệ, lọc khuyến mãi đang hoạt động chính xác dựa trên ngày hiện tại, tự động ẩn thông báo sau ngày hết hạn, xử lý lỗi khi ngày kết thúc nhỏ hơn ngày bắt đầu (ném ngoại lệ IllegalArgumentException), xác minh mã khuyến mãi duy nhất, đảm bảo độ bao phủ mã >= 90%.

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->Hoàn thiện endpoint, giao diện frontend, kiểm thử tích hợp và tài liệu kỹ thuật<!--DAY_HEADER_END-->

#### 📝 Công việc con 4.1: Xây dựng endpoint REST cho dịch vụ khuyến mãi và thông báo hệ thống
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/PromotionController.java;./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/announcement/AnnouncementController.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST CRUD cho `/api/promotions` (GET, POST, PUT, DELETE) và `/api/announcements` (GET, POST, PUT, DELETE), áp dụng xác thực JWT và kiểm soát quyền truy cập theo RBAC (chỉ Center Admin/Manager mới có quyền tạo/sửa/xóa, tất cả người dùng đăng nhập có quyền xem). Thêm xác thực đầu vào request, chuẩn hóa phản hồi lỗi, đảm bảo endpoint GET tự động lọc các khuyến mãi/thông báo đã hết hạn.

<!--START_API_CONTRACT-->
```json
{
  "promotionApi": {
    "basePath": "/api/promotions",
    "endpoints": [
      {
        "method": "GET",
        "path": "/",
        "description": "List all active promotions",
        "auth": "Bearer JWT",
        "rbac": ["Student", "Teacher", "Center Admin", "System Admin"]
      },
      {
        "method": "POST",
        "path": "/",
        "description": "Create new promotion",
        "requestSchema": {
          "code": "string (required, unique)",
          "discountPercent": "integer (1-100)",
          "startDate": "date (optional)",
          "endDate": "date (optional)",
          "description": "text (optional)"
        },
        "auth": "Bearer JWT",
        "rbac": ["Center Admin", "Manager"]
      }
    ]
  },
  "announcementApi": {
    "basePath": "/api/announcements",
    "endpoints": [
      {
        "method": "GET",
        "path": "/",
        "description": "List all active announcements",
        "auth": "Bearer JWT",
        "rbac": ["Student", "Teacher", "Center Admin", "System Admin"]
      },
      {
        "method": "POST",
        "path": "/",
        "description": "Create new announcement",
        "requestSchema": {
          "title": "string (required, max 150 chars)",
          "content": "string (required, max 2000 chars)",
          "startDate": "date (optional)",
          "endDate": "date (optional)"
        },
        "auth": "Bearer JWT",
        "rbac": ["Center Admin", "Manager"]
      }
    ]
  }
}
```
<!--END_API_CONTRACT-->

#### 📝 Công việc con 4.2: Xây dựng giao diện frontend cho thông báo và khuyến mãi
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/app/notifications/page.tsx;./sources/frontend/src/app/promotions/page.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng giao diện trang thông báo hiển thị danh sách thông báo hệ thống và thông báo cá nhân, tích hợp hiển thị trạng thái đã gửi/thất bại với icon trạng thái, hỗ trợ đa ngôn ngữ. Xây dựng giao diện trang khuyến mãi hiển thị các khuyến mãi đang hoạt động cho học viên với thẻ thông tin mã giảm giá, phần trăm giảm, ngày hết hạn, điều kiện áp dụng. Đảm bảo giao diện responsive, tương thích di động, tích hợp với API endpoints tương ứng.

#### 📝 Công việc con 4.3: Viết kiểm thử tích hợp cho các endpoint dịch vụ thông báo, khuyến mãi và thông báo hệ thống
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/NotificationControllerIntegrationTest.java;./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/PromotionControllerIntegrationTest.java;./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/announcement/AnnouncementControllerIntegrationTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-016], [EXC-003], [REQ-017], [REQ-018]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử tích hợp cho tất cả endpoint của dịch vụ thông báo, khuyến mãi và thông báo hệ thống sử dụng Testcontainers với PostgreSQL, xác minh logic nghiệp vụ hoạt động đúng (CRUD operations, lọc theo ngày hết hạn), xác minh kiểm soát quyền RBAC hoạt động chính xác (phân biệt quyền Student, Center Admin, Manager, System Admin), xác minh cơ chế retry thông báo hoạt động đúng (giả lập lỗi gửi thất bại, kiểm tra retry_count tăng dần). Kiểm tra phản hồi lỗi chuẩn hóa cho các trường hợp không hợp lệ.

#### 📝 Công việc con 4.4: Rà soát chất lượng mã nguồn giai đoạn 3
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** Toàn bộ mã nguồn dịch vụ điểm danh, thẻ hội viên, thông báo, khuyến mãi và giao diện frontend liên quan trong giai đoạn 3
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [EXC-001], [EXC-002], [EXC-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát mã nguồn toàn bộ các thành phần được phát triển trong giai đoạn 3, kiểm tra tuân thủ tiêu chuẩn mã hóa doanh nghiệp, phát hiện lỗi logic (ví dụ: race condition trong điểm danh, thiếu xác thực đầu vào), điểm nghẽn hiệu năng (truy vấn cơ sở dữ liệu thiếu chỉ mục), đảm bảo không có lỗ hổng bảo mật (SQL injection, XSS, CSRF), đề xuất chiến lược sửa lỗi tối ưu, đảm bảo mã nguồn sẵn sàng cho tích hợp với các dịch vụ khác trong giai đoạn 4 và 5.

#### 📝 Công việc con 4.5: Soạn thảo tài liệu kỹ thuật cho các dịch vụ giai đoạn 3
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/notification-service-api-spec.md;./sources/docs/promotion-service-api-spec.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [EXC-001], [EXC-002], [EXC-003]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Soạn thảo tài liệu kỹ thuật chi tiết cho bốn dịch vụ vi mô của giai đoạn 3 theo chuẩn OpenAPI 3.0, bao gồm: đặc tả API đầy đủ cho attendance-service (điểm danh QR), membership-service (thẻ hội viên), notification-service (thông báo đa kênh), promotion-service (khuyến mãi và thông báo hệ thống). Mỗi tài liệu phải bao gồm: mô tả chức năng, phương thức HTTP, đường dẫn, schema request/response, mã lỗi, yêu cầu xác thực JWT, quyền RBAC, xử lý ngoại lệ (EXC-001, EXC-002, EXC-003), và ví dụ payload thực tế. Đảm bảo tài liệu phù hợp với tiêu chuẩn doanh nghiệp, dễ hiểu cho các đội phát triển các giai đoạn sau.