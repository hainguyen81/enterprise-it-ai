# Giai đoạn 4: Quản lý thông báo, khuyến mãi, thông báo và tích hợp chatbot AI <!--PHASE_NAME_START-->Quản lý thông báo, khuyến mãi, thông báo và tích hợp chatbot AI<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID bản thiết kế** | ARCH-20260817193854 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Quản lý thông báo, khuyến mãi, thông báo và tích hợp chatbot AI<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc quản lý thông báo, khuyến mãi, thông báo và tích hợp chatbot AI. Chúng ta sẽ xây dựng các chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm. Xây dựng chức năng tạo, sửa, xóa khuyến mãi. Xây dựng chức năng tạo, sửa, xóa thông báo. Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/17 19:38:54 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc quản lý thông báo, khuyến mãi, thông báo và tích hợp chatbot AI. Chúng ta sẽ xây dựng các chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm. Xây dựng chức năng tạo, sửa, xóa khuyến mãi. Xây dựng chức năng tạo, sửa, xóa thông báo. Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/notification/`
- `./sources/backend/promotion/`
- `./sources/backend/announcement/`
- `./sources/backend/chatbot/`

## 3. Hướng dẫn chức năng của các chuyên gia con được chỉ định
*   **Coder**: Hoạt động như một Nhà phát triển ứng dụng cấp cao/Chủ tịch. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Trưởng/QC/QA cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con tác vụ liên quan đến phạm vi tích hợp hoặc kết thúc-to-end tổng thể nơi không có tệp mã cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh trình biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về việc đóng gói, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm.
- Hoàn thành 100% các chức năng tạo, sửa, xóa khuyến mãi.
- Hoàn thành 100% các chức năng tạo, sửa, xóa thông báo.
- Hoàn thành 100% các chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% các bộ kiểm thử chức năng và tích hợp.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc hàng ngày

### 🌤️ NGÀY 1: Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm

#### 📝 NHIỆM VỤ CON 1.1: Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notification/src/main/java/org/nlh4j/membership_hub/notification/NotificationService.java

* **TagID mục tiêu:** [REQ-016]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm. Chức năng này sẽ cho phép quản trị viên tạo và gửi thông báo đến các nhóm người dùng khác nhau.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(50),
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/notifications",
      "method": "POST",
      "request": {
        "user_id": "UUID",
        "group_zalo": "string",
        "message": "string"
      },
      "response": {
        "notification_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(NotificationDeliveryException.class)
public ResponseEntity<ErrorResponse> handleNotificationDelivery(NotificationDeliveryException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Notification delivery failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.2: Viết kiểm thử cho chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notification/src/main/java/org/nlh4j/membership_hub/notification/NotificationService.java;./sources/backend/notification/src/test/java/org/nlh4j/membership_hub/notification/NotificationTest.java

* **TagID mục tiêu:** [REQ-016]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 1.3: Tài liệu chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/notification.md

* **TagID mục tiêu:** [REQ-016]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo, gửi thông báo cho học viên, giáo viên, trung tâm. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 1.4: Xây dựng chức năng tạo, sửa, xóa khuyến mãi
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotion/src/main/java/org/nlh4j/membership_hub/promotion/PromotionService.java

* **TagID mục tiêu:** [REQ-017]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo, sửa, xóa khuyến mãi. Chức năng này sẽ cho phép quản trị viên tạo, sửa và xóa các chương trình khuyến mãi.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(30) UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/promotions",
      "method": "POST",
      "request": {
        "code": "string",
        "discount_percent": "integer",
        "start_date": "date",
        "end_date": "date",
        "description": "string"
      },
      "response": {
        "promo_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(InvalidPromoCodeException.class)
public ResponseEntity<ErrorResponse> handleInvalidPromoCode(InvalidPromoCodeException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid promo code", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 1.5: Viết kiểm thử cho chức năng tạo, sửa, xóa khuyến mãi
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotion/src/main/java/org/nlh4j/membership_hub/promotion/PromotionService.java;./sources/backend/promotion/src/test/java/org/nlh4j/membership_hub/promotion/PromotionTest.java

* **TagID mục tiêu:** [REQ-017]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo, sửa, xóa khuyến mãi. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 1.6: Tài liệu chức năng tạo, sửa, xóa khuyến mãi
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/promotion.md

* **TagID mục tiêu:** [REQ-017]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo, sửa, xóa khuyến mãi. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

### 🌤️ NGÀY 2: Xây dựng chức năng tạo, sửa, xóa thông báo và tích hợp chatbot AI

#### 📝 NHIỆM VỤ CON 2.1: Xây dựng chức năng tạo, sửa, xóa thông báo
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcement/src/main/java/org/nlh4j/membership_hub/announcement/AnnouncementService.java

* **TagID mục tiêu:** [REQ-018]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo, sửa, xóa thông báo. Chức năng này sẽ cho phép quản trị viên tạo, sửa và xóa các thông báo.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/announcements",
      "method": "POST",
      "request": {
        "title": "string",
        "content": "string",
        "start_date": "date",
        "end_date": "date"
      },
      "response": {
        "announcement_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(AnnouncementValidationException.class)
public ResponseEntity<ErrorResponse> handleAnnouncementValidation(AnnouncementValidationException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Announcement validation failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.2: Viết kiểm thử cho chức năng tạo, sửa, xóa thông báo
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcement/src/main/java/org/nlh4j/membership_hub/announcement/AnnouncementService.java;./sources/backend/announcement/src/test/java/org/nlh4j/membership_hub/announcement/AnnouncementTest.java

* **TagID mục tiêu:** [REQ-018]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo, sửa, xóa thông báo. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 2.3: Tài liệu chức năng tạo, sửa, xóa thông báo
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/announcement.md

* **TagID mục tiêu:** [REQ-018]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo, sửa, xóa thông báo. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.

#### 📝 NHIỆM VỤ CON 2.4: Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/chatbot/src/main/java/org/nlh4j/membership_hub/chatbot/ChatbotService.java

* **TagID mục tiêu:** [REQ-019]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp. Chức năng này sẽ cho phép người dùng tương tác với chatbot để nhận câu trả lời cho các câu hỏi thường gặp.

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/chatbot",
      "method": "POST",
      "request": {
        "question": "string"
      },
      "response": {
        "answer": "string",
        "confidence": "float"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(ChatbotProcessingException.class)
public ResponseEntity<ErrorResponse> handleChatbotProcessing(ChatbotProcessingException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Chatbot processing failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
}
```
<!--END_EXC_HANDLER-->

#### 📝 NHIỆM VỤ CON 2.5: Viết kiểm thử cho chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/chatbot/src/main/java/org/nlh4j/membership_hub/chatbot/ChatbotService.java;./sources/backend/chatbot/src/test/java/org/nlh4j/membership_hub/chatbot/ChatbotTest.java

* **TagID mục tiêu:** [REQ-019]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp. Kiểm thử sẽ bao gồm các trường hợp thành công và thất bại, kiểm tra tính hợp lệ của dữ liệu đầu vào và dữ liệu trả về.

#### 📝 NHIỆM VỤ CON 2.6: Tài liệu chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/chatbot.md

* **TagID mục tiêu:** [REQ-019]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tích hợp chatbot AI để trả lời các câu hỏi thường gặp. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường dữ liệu, và các trường hợp sử dụng.