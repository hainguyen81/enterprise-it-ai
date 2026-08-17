# Giai đoạn 4: <!--PHASE_NAME_START-->Triển khai hệ thống thông báo đa kênh, quản lý khuyến mãi, tích hợp chatbot AI và báo cáo phân tích<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản thảo** | ARCH-20260817042313 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai hệ thống thông báo đa kênh, quản lý khuyến mãi, tích hợp chatbot AI và báo cáo phân tích<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai hoàn chỉnh các tính năng giao tiếp đa kênh (thông báo đẩy di động, tin nhắn nhóm Zalo), quản lý khuyến mãi và thông báo hệ thống, tích hợp chatbot AI hỗ trợ khách hàng, giao diện di động vai trò tương ứng, bản địa hóa/SEO đa ngôn ngữ và các báo cáo phân tích cốt lõi, hoàn thiện tất cả các yêu cầu chức năng người dùng cuối của hệ thống membership-hub, đảm bảo tích hợp liền mạch giữa các microservice và giao diện người dùng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/08/17 04:23:13 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn

Giai đoạn 4 tập trung vào việc triển khai hoàn chỉnh các tính năng giao tiếp đa kênh và báo cáo phân tích cho hệ thống membership-hub, bao gồm 10 công việc chính từ Công việc 16 đến Công việc 25. Các mục tiêu kiến trúc cốt lõi bao gồm:

1. **Hệ thống thông báo đa kênh**: Triển khai dịch vụ `notification-service` hỗ trợ tạo và quản lý thông báo hệ thống (announcements) với ngày hết hạn tùy chọn, tự động ẩn thông báo hết hạn, tích hợp gửi thông báo đẩy qua FCM/APNs và tin nhắn nhóm Zalo với cơ chế thử lại tối đa 3 lần khi gửi thất bại [REQ-016], [REQ-018], [EXC-003].
2. **Quản lý khuyến mãi**: Triển khai dịch vụ `promotion-service` hỗ trợ CRUD khuyến mãi (giảm giá, ưu đãi) với mã khuyến mãi duy nhất, phần trăm giảm giá từ 0-100%, ngày bắt đầu/kết thúc, tự động ẩn khuyến mãi hết hạn [REQ-017].
3. **Tích hợp chatbot AI**: Tích hợp dịch vụ chatbot AI bên thứ ba vào `chatbot-service`, xử lý truy vấn người dùng về khóa học, giáo viên, trung tâm, tình trạng tài khoản, chuyển tiếp cho hỗ trợ con người khi độ tin cậy dưới 70% [REQ-019].
4. **Bản địa hóa và SEO đa ngôn ngữ**: Triển khai phát hiện ngôn ngữ mặc định (ưu tiên cài đặt người dùng, sau đó là header Accept-Language, mặc định Tiếng Việt), cấu hình thẻ meta ngôn ngữ và thuộc tính hreflang cho Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha, đảm bảo chuyển đổi ngôn ngữ không cần tải lại trang [REQ-022], [REQ-023], [NFR-007].
5. **Giao diện di động đa vai trò**: Triển khai ứng dụng di động React Native với giao diện đáp ứng cho từng vai trò (Student, Teacher, Admin), tích hợp FCM/APNs cho thông báo đẩy, chức năng quét mã QR điểm danh [REQ-020], [REQ-021].
6. **Báo cáo và phân tích**: Triển khai `report-service` tạo báo cáo điểm danh hàng ngày định dạng CSV và dashboard tổng hợp ghi danh (tổng học viên, khóa học đang hoạt động, buổi học sắp tới 7 ngày), xử lý khôi phục dữ liệu điểm danh sau sự cố hệ thống [REQ-024], [REQ-025], [EXC-005].
7. **Tài liệu hóa**: Viết tài liệu hợp đồng API chi tiết cho tất cả các service mới, hướng dẫn tích hợp chatbot, bản địa hóa/SEO, hướng dẫn sử dụng ứng dụng di động và tài liệu tích hợp tổng thể.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục

### Dịch vụ Backend
- `./sources/backend/notification-service/` [REQ-016], [EXC-003], [ARC-008]
- `./sources/backend/promotion-service/` [REQ-017], [REQ-018]
- `./sources/backend/report-service/` [REQ-024], [REQ-025], [EXC-005]
- `./sources/backend/chatbot-service/` [REQ-019]

### Ứng dụng di động và Frontend
- `./sources/frontend/mobile-app/` [REQ-020], [REQ-021], [REQ-022], [REQ-023]
- `./sources/frontend/web/src/` [REQ-022], [REQ-023], [REQ-019]

### Tài liệu Kiến trúc
- `./sources/docs/architecture/notification-service-api.md` [ARC-010]
- `./sources/docs/architecture/promotion-service-api.md` [ARC-010]
- `./sources/docs/architecture/report-service-api.md` [ARC-010]
- `./sources/docs/architecture/chatbot-integration.md` [ARC-010]
- `./sources/docs/architecture/localization-seo-guide.md` [ARC-010]
- `./sources/docs/architecture/mobile-app-guide.md` [ARC-010]
- `./sources/docs/architecture/integration-guide.md` [ARC-010]

### Điểm cuối API và Sự kiện
- **notification-service**: `POST /api/v1/notifications/announcements`, `GET /api/v1/notifications/announcements`, `POST /api/v1/notifications/send`, `DELETE /api/v1/notifications/announcements/{announcementId}`
- **promotion-service**: `POST /api/v1/promotions`, `GET /api/v1/promotions/active`, `DELETE /api/v1/promotions/{promoId}`
- **chatbot-service**: `POST /api/v1/chatbot/query`
- **report-service**: `GET /api/v1/reports/attendance/daily`, `GET /api/v1/reports/dashboard/enrollment`
- **Chủ đề sự kiện**: `announcement.created`, `promotion.created`, `notification.sent`, `report.generated`, `card.renewed`, `attendance.recorded`, `attendance.duplicate`

## 3. Chỉ thị chức năng chuyên biệt cho Đại lý phụ

*   **Coder**: Làm việc như Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên các dịch vụ backend `notification-service`, `promotion-service`, `report-service`, `chatbot-service` và ứng dụng di động `mobile-app`. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
*   **Tester**: Làm việc như Kiểm soát chất lượng/QA chính. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo kiểm thử đơn vị, kiểm thử tích hợp và kịch bản xác thực hiệu suất. Bị cấm sửa đổi mã nguồn sản xuất. Nếu phạm vi tác vụ mục tiêu là tích hợp/E2E không có tệp mã nguồn cụ thể, phải xuất ra token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp đường dẫn phân tách bằng dấu chấm phẩy.
*   **Doc**: Hoạt động như Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên biên soạn tài liệu Thông số kỹ thuật, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp công nghệ đang hoạt động của dự án. Mọi tệp tài liệu kỹ thuật được tạo phải có đuôi `.md` và nằm strictly trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Chịu trách nhiệm xác minh biên dịch, kiểm soát phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗi bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về containerization, multi-stage Dockerfile engineering, package optimization, và pushing verified application image assets.
*   **GCP**: Chuyên về cloud automation trong Google Cloud Platform, xây dựng và push images lên Google Cloud Artifact Registry (GCR), orchestrate container environments trên Google Cloud Run.
*   **GKE**: Chuyên về production container orchestration trong Google Kubernetes Engine, xây dựng Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, và deploy microservices workloads vào active GKE clusters.

## 4. Định nghĩa Hoàn thành của Giai đoạn (DoD)

1. Tất cả 10 công việc của giai đoạn 4 (Công việc 16-25) đã được triển khai và kiểm thử thành công.
2. 100% thẻ theo dõi [REQ-016] đến [REQ-025], [EXC-003], [EXC-005] được ánh xạ và bao phủ đầy đủ.
3. Độ phủ mã đạt >= 90% cho các lớp service và controller của `notification-service`, `promotion-service`, `report-service`, `chatbot-service`; đạt >= 80% cho ứng dụng di động `mobile-app`.
4. Tất cả endpoint API hoạt động đúng theo hợp đồng đã định nghĩa, bao gồm logic thông báo đa kênh, quản lý khuyến mãi, chatbot AI, báo cáo CSV và dashboard.
5. Cơ chế thử lại thông báo thất bại hoạt động đúng (tối đa 3 lần với khoảng cách tăng dần), trạng thái `delivered` được cập nhật chính xác.
6. Chatbot AI chuyển tiếp truy vấn cho hỗ trợ con người khi độ tin cậy dưới 70%.
7. Báo cáo điểm danh CSV được tạo đúng định dạng với các cột StudentName, CourseName, AttendanceDate, Status; dashboard trả về đúng tổng hợp.
8. Bản địa hóa đa ngôn ngữ hoạt động đúng cho Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha; SEO tags (hreflang, html lang) được cấu hình đúng.
9. Không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) được phát hiện trong quá trình code review, tuân thủ đầy đủ OWASP Top 10 [NFR-003].
10. Tất cả tài liệu API, hướng dẫn tích hợp và hướng dẫn sử dụng được hoàn thiện đầy đủ và chính xác.

## 5. Nhật ký thực thi kiến trúc theo từng ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->Triển khai dịch vụ thông báo và quản lý khuyến mãi cơ bản<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai API quản lý thông báo và khuyến mãi
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationController.java`; `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationService.java`; `./sources/backend/promotion-service/src/main/java/com/membershiphub/promotion/PromotionController.java`; `./sources/backend/promotion-service/src/main/java/com/membershiphub/promotion/PromotionService.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [EXC-003], [DAT-008], [DAT-009]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API CRUD cho quản lý thông báo (announcements): `POST /api/v1/notifications/announcements` (tạo thông báo mới với tiêu đề, nội dung, ngày hết hạn tùy chọn, nhóm Zalo mục tiêu), `GET /api/v1/notifications/announcements` (lấy danh sách thông báo còn hiệu lực), `DELETE /api/v1/notifications/announcements/{announcementId}` (xóa thông báo). Triển khai logic tự động ẩn thông báo sau ngày hết hạn nếu được cấu hình. Triển khai API CRUD cho quản lý khuyến mãi (promotions): `POST /api/v1/promotions` (tạo khuyến mãi mới với mã duy nhất, phần trăm giảm giá 0-100%, ngày bắt đầu/kết thúc), `GET /api/v1/promotions/active` (lấy danh sách khuyến mãi còn hiệu lực), `DELETE /api/v1/promotions/{promoId}` (xóa khuyến mãi). Triển khai logic tự động ẩn khuyến mãi sau ngày hết hạn. Triển khai logic gửi thông báo đẩy qua FCM/APNs và tin nhắn đến nhóm Zalo được chỉ định. Triển khai xử lý ngoại lệ [EXC-003] với cơ chế thử lại tối đa 3 lần khi gửi thông báo thất bại, lưu lỗi vào bảng notifications với trạng thái delivered = false.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:**
```sql
-- Thêm ràng buộc CHECK cho phần trăm giảm giá khuyến mãi [REQ-017]
ALTER TABLE promotions ADD CONSTRAINT chk_discount_percent CHECK (discount_percent BETWEEN 0 AND 100);

-- Tạo index cho bảng điểm danh để tối ưu truy vấn báo cáo [REQ-024], [NFR-001]
CREATE INDEX idx_attendance_student_course_date ON attendance (student_id, course_id, attendance_date);

-- Tạo index cho bảng ghi danh để tối ưu truy vấn dashboard [REQ-025], [NFR-001]
CREATE INDEX idx_enrollments_course_student ON enrollments (course_id, student_id);

-- Tạo index cho bảng khóa học để tối ưu truy vấn khóa học sắp tới [REQ-025], [NFR-001]
CREATE INDEX idx_courses_dates ON courses (start_date, end_date);

-- Tạo index cho bảng thông báo để tối ưu truy vấn thông báo chưa gửi [REQ-016], [NFR-001]
CREATE INDEX idx_notifications_delivered_sent ON notifications (delivered, sent_at);
```
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
```json
{
  "services": [
    {
      "serviceName": "notification-service",
      "version": "v1",
      "endpoints": [
        {
          "method": "POST",
          "path": "/api/v1/notifications/announcements",
          "tags": ["REQ-018"],
          "request": {
            "schema": {
              "type": "object",
              "required": ["title", "content"],
              "properties": {
                "title": {"type": "string", "maxLength": 150},
                "content": {"type": "string", "maxLength": 2000},
                "expiryDate": {"type": "date", "optional": true},
                "targetZaloGroup": {"type": "string", "optional": true}
              }
            }
          },
          "response": {
            "schema": {
              "type": "object",
              "properties": {
                "announcementId": {"type": "uuid"},
                "createdAt": {"type": "timestamp"}
              }
            }
          }
        },
        {
          "method": "GET",
          "path": "/api/v1/notifications/announcements",
          "tags": ["REQ-018"],
          "response": {
            "schema": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "announcementId": {"type": "uuid"},
                  "title": {"type": "string"},
                  "content": {"type": "string"},
                  "startDate": {"type": "date"},
                  "endDate": {"type": "date", "optional": true}
                }
              }
            }
          }
        },
        {
          "method": "POST",
          "path": "/api/v1/notifications/send",
          "tags": ["REQ-016"],
          "request": {
            "schema": {
              "type": "object",
              "required": ["message", "targetType"],
              "properties": {
                "message": {"type": "string", "maxLength": 1000},
                "targetType": {"type": "string", "enum": ["USER", "ZALO_GROUP", "COURSE"]},
                "targetId": {"type": "uuid", "optional": true}
              }
            }
          },
          "response": {"statusCode": 202}
        }
      ],
      "events": [
        {
          "topic": "notification.sent",
          "tags": ["REQ-016"],
          "payload": {
            "notificationId": {"type": "uuid"},
            "targetType": {"type": "string"},
            "targetId": {"type": "uuid", "optional": true},
            "sentAt": {"type": "timestamp"}
          }
        }
      ]
    },
    {
      "serviceName": "promotion-service",
      "version": "v1",
      "endpoints": [
        {
          "method": "POST",
          "path": "/api/v1/promotions",
          "tags": ["REQ-017"],
          "request": {
            "schema": {
              "type": "object",
              "required": ["code", "discountPercent", "startDate"],
              "properties": {
                "code": {"type": "string", "unique": true, "maxLength": 50},
                "discountPercent": {"type": "integer", "minimum": 0, "maximum": 100},
                "startDate": {"type": "date"},
                "endDate": {"type": "date", "optional": true},
                "description": {"type": "string", "maxLength": 500, "optional": true}
              }
            }
          },
          "response": {
            "schema": {
              "type": "object",
              "properties": {
                "promoId": {"type": "uuid"},
                "createdAt": {"type": "timestamp"}
              }
            }
          }
        },
        {
          "method": "GET",
          "path": "/api/v1/promotions/active",
          "tags": ["REQ-017"],
          "response": {
            "schema": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "promoId": {"type": "uuid"},
                  "code": {"type": "string"},
                  "discountPercent": {"type": "integer"},
                  "endDate": {"type": "date", "optional": true},
                  "description": {"type": "string", "optional": true}
                }
              }
            }
          }
        }
      ],
      "events": [
        {
          "topic": "promotion.created",
          "tags": ["REQ-017"],
          "payload": {
            "promoId": {"type": "uuid"},
            "code": {"type": "string"},
            "discountPercent": {"type": "integer"},
            "startDate": {"type": "date"},
            "endDate": {"type": "date", "optional": true}
          }
        }
      ]
    }
  ]
}
```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ [EXC-003] trả về mã lỗi 500 Internal Server Error với thông báo "Gửi thông báo thất bại, hệ thống sẽ thử lại sau" khi lần thử đầu tiên thất bại, lên lịch thử lại tự động. Nếu thất bại sau 3 lần thử, ghi log lỗi chi tiết và gửi cảnh báo cho quản trị viên.

#### 📝 Phụ công việc 2: Viết unit test cho dịch vụ thông báo và khuyến mãi
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationService.java;./sources/backend/notification-service/src/test/java/com/membershiphub/notification/NotificationServiceTest.java`; `./sources/backend/promotion-service/src/main/java/com/membershiphub/promotion/PromotionService.java;./sources/backend/promotion-service/src/test/java/com/membershiphub/promotion/PromotionServiceTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [EXC-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: tạo thông báo thành công, lấy danh sách thông báo còn hiệu lực (lọc bỏ thông báo đã hết hạn), xóa thông báo thành công, tạo khuyến mãi thành công, lấy danh sách khuyến mãi còn hiệu lực, xử lý lỗi gửi thông báo thất bại với cơ chế thử lại 3 lần, kiểm tra trạng thái delivered được cập nhật đúng sau khi thử lại thất bại. Đảm bảo độ phủ mã ít nhất 90% cho các lớp service tương ứng.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 3: Kiểm tra chất lượng mã nguồn dịch vụ thông báo và khuyến mãi
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notification-service/`; `./sources/backend/promotion-service/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [EXC-003], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn notification-service và promotion-service, kiểm tra logic gửi thông báo đa kênh hoạt động đúng, logic tự động ẩn thông báo/khuyến mãi hết hạn hoạt động chính xác, cơ chế thử lại khi gửi thông báo thất bại hoạt động đúng, đảm bảo không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) [NFR-003], tuân thủ chuẩn mã hóa Quarkus/Java 21. Đề xuất và thực hiện sửa lỗi nếu có.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 4: Viết tài liệu hợp đồng API cho dịch vụ thông báo và khuyến mãi
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/notification-service-api.md`; `./sources/docs/architecture/promotion-service-api.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-016], [REQ-017], [REQ-018]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho notification-service và promotion-service, bao gồm tất cả endpoint quản lý thông báo, quản lý khuyến mãi, schema request/response, mã lỗi, ví dụ sử dụng. Mô tả luồng gửi thông báo đa kênh (push, Zalo) và cơ chế thử lại khi gửi thất bại, quy tắc tự động ẩn thông báo/khuyến mãi hết hạn.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->Triển khai tích hợp chatbot AI và bản địa hóa/SEO đa ngôn ngữ<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Tích hợp chatbot AI và triển khai bản địa hóa/SEO
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/chatbot-service/src/main/java/com/membershiphub/chatbot/ChatbotController.java`; `./sources/backend/chatbot-service/src/main/java/com/membershiphub/chatbot/ChatbotService.java`; `./sources/frontend/web/src/components/ChatbotWidget.tsx`; `./sources/frontend/web/src/hooks/useLocale.ts`; `./sources/frontend/web/src/app/[locale]/layout.tsx`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-019], [REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tích hợp dịch vụ chatbot AI bên thứ ba, triển khai endpoint `POST /api/v1/chatbot/query` để xử lý truy vấn người dùng về khóa học, giáo viên, trung tâm, tình trạng tài khoản. Triển khai logic chuyển tiếp truy vấn cho hỗ trợ con người khi độ tin cậy của câu trả lời chatbot dưới 70%. Triển khai logic phát hiện ngôn ngữ ưu tiên: ưu tiên ngôn ngữ đã lưu trong cài đặt người dùng, sau đó là header `Accept-Language` của trình duyệt, mặc định là Tiếng Việt. Triển khai cấu hình SEO đa ngôn ngữ: thẻ `<html lang="...">` chính xác cho mỗi ngôn ngữ, thuộc tính `hreflang` cho các phiên bản ngôn ngữ (en, vi, es), thẻ meta ngôn ngữ cho mỗi trang. Đảm bảo chuyển đổi ngôn ngữ không cần tải lại trang [NFR-007].
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
```json
{
  "endpoints": [
    {
      "method": "POST",
      "path": "/api/v1/chatbot/query",
      "tags": ["REQ-019"],
      "request": {
        "schema": {
          "type": "object",
          "required": ["query"],
          "properties": {
            "query": {"type": "string", "maxLength": 500},
            "context": {"type": "object", "optional": true}
          }
        }
      },
      "response": {
        "schema": {
          "type": "object",
          "properties": {
            "answer": {"type": "string"},
            "confidence": {"type": "float"},
            "escalateToHuman": {"type": "boolean"}
          }
        }
      }
    }
  ]
}
```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho tác vụ này.

#### 📝 Phụ công việc 2: Viết unit test cho chatbot và bản địa hóa/SEO
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/chatbot-service/src/main/java/com/membershiphub/chatbot/ChatbotService.java;./sources/backend/chatbot-service/src/test/java/com/membershiphub/chatbot/ChatbotServiceTest.java`; `./sources/frontend/web/src/test/components/ChatbotWidget.test.tsx`; `./sources/frontend/web/src/test/hooks/useLocale.test.ts`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-019], [REQ-022], [REQ-023]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho chatbot: xử lý truy vấn thành công trả về câu trả lời liên quan, chuyển tiếp cho hỗ trợ con người khi độ tin cậy dưới 70%, xử lý truy vấn không hợp lệ. Viết unit test cho logic phát hiện ngôn ngữ: ưu tiên ngôn ngữ đã lưu, sau đó là Accept-Language, mặc định là Tiếng Việt, chuyển đổi ngôn ngữ không cần tải lại trang. Viết test cho cấu hình SEO: kiểm tra thẻ `hreflang` và thẻ `<html lang="...">` được tạo đúng cho 3 ngôn ngữ (en, vi, es). Đảm bảo độ phủ mã ít nhất 85% cho các thành phần liên quan.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 3: Kiểm tra chất lượng mã nguồn chatbot và bản địa hóa
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/chatbot-service/`; `./sources/frontend/web/src/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-019], [REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho chatbot service và các thành phần frontend liên quan đến bản địa hóa/SEO, kiểm tra logic xử lý truy vấn chatbot hoạt động đúng, logic chuyển tiếp cho hỗ trợ con người hoạt động chính xác khi độ tin cậy thấp, logic phát hiện ngôn ngữ hoạt động đúng, cấu hình SEO đầy đủ cho 3 ngôn ngữ, không có lỗi bảo mật (XSS khi hiển thị nội dung chatbot), tuân thủ yêu cầu đa ngôn ngữ [NFR-007]. Đề xuất và thực hiện sửa lỗi nếu có.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 4: Viết tài liệu tích hợp chatbot và hướng dẫn bản địa hóa/SEO
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/chatbot-integration.md`; `./sources/docs/architecture/localization-seo-guide.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-019], [REQ-022], [REQ-023]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn tích hợp chatbot AI, bao gồm cấu hình API key, xử lý truy vấn, logic chuyển tiếp cho hỗ trợ con người, xử lý lỗi. Viết tài liệu hướng dẫn bản địa hóa và SEO, bao gồm cách thêm ngôn ngữ mới, cấu hình hreflang, quản lý chuỗi văn bản đa ngôn ngữ, kiểm tra cấu hình SEO cho từng ngôn ngữ.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.

### 🌤️ Ngày 3: <!--DAY_HEADER_START-->Triển khai giao diện di động vai trò và thông báo đẩy<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai giao diện di động vai trò và tích hợp thông báo đẩy
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend/mobile-app/src/screens/StudentDashboard.tsx`; `./sources/frontend/mobile-app/src/screens/TeacherDashboard.tsx`; `./sources/frontend/mobile-app/src/screens/AdminDashboard.tsx`; `./sources/frontend/mobile-app/src/services/NotificationService.ts`; `./sources/frontend/mobile-app/src/components/AttendanceScanner.tsx`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai giao diện người dùng đáp ứng cho từng vai trò trên ứng dụng di động:
  * Student: màn hình duyệt khóa học, đăng ký khóa học, xem thẻ hội viên (ngày còn lại), quét mã QR điểm danh, xem lịch sử điểm danh.
  * Teacher: màn hình xem danh sách khóa học được phân công, danh sách học viên, lịch dạy, điểm danh học viên.
  * Admin: màn hình quản lý trung tâm, quản lý khóa học, quản lý người dùng, tạo thông báo, xem báo cáo.
  Tích hợp FCM/APNs: xử lý đăng ký token thiết bị khi người dùng đăng nhập, nhận và hiển thị thông báo đẩy cho xác nhận điểm danh, thông báo mới, nhắc nhở khóa học. Đảm bảo giao diện hoạt động mượt mà trên cả Android và iOS, đồng bộ chức năng với phiên bản web.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Coder không thực hiện viết hợp đồng API cho tác vụ này.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho tác vụ này.

#### 📝 Phụ công việc 2: Viết unit và integration test cho ứng dụng di động
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend/mobile-app/src/test/screens/StudentDashboard.test.tsx;./sources/frontend/mobile-app/src/test/screens/TeacherDashboard.test.tsx`; `./sources/frontend/mobile-app/src/test/services/NotificationService.test.ts`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các thành phần giao diện di động: kiểm tra menu điều hướng hiển thị đúng theo vai trò người dùng, các màn hình chức năng hoạt động đúng (duyệt khóa học, xem thẻ hội viên, quét mã QR điểm danh). Viết integration test cho luồng thông báo đẩy: đăng ký token thiết bị thành công, nhận thông báo đẩy khi có sự kiện mới, hiển thị thông báo đúng trên giao diện. Kiểm tra giao diện hoạt động đúng trên các kích thước màn hình khác nhau. Đảm bảo độ phủ mã ít nhất 80% cho các thành phần di động.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 3: Kiểm tra chất lượng mã nguồn ứng dụng di động
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend/mobile-app/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-020], [REQ-021], [NFR-007]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn ứng dụng di động, kiểm tra giao diện đáp ứng hoạt động đúng trên Android và iOS, logic hiển thị theo vai trò người dùng chính xác, tích hợp thông báo đẩy hoạt động đúng, tuân thủ yêu cầu đa ngôn ngữ [NFR-007], không có lỗi hiệu suất (tiêu tốn nhiều tài nguyên, phản hồi chậm). Kiểm tra logic quét mã QR điểm danh tích hợp với backend hoạt động đúng. Đề xuất và thực hiện sửa lỗi nếu có.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 4: Viết tài liệu hướng dẫn sử dụng ứng dụng di động
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/mobile-app-guide.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-020], [REQ-021]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn sử dụng ứng dụng di động cho từng vai trò người dùng (Student, Teacher, Admin), bao gồm hướng dẫn đăng ký, đăng nhập, sử dụng các chức năng chính (duyệt khóa học, điểm danh, xem thẻ hội viên, nhận thông báo). Viết hướng dẫn cài đặt ứng dụng trên Android và iOS, cấu hình thông báo đẩy.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.

### 🌤️ Ngày 4: <!--DAY_HEADER_START-->Triển khai dịch vụ báo cáo và hoàn thiện tích hợp giai đoạn<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Triển khai API báo cáo điểm danh và dashboard ghi danh
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/report-service/src/main/java/com/membershiphub/report/ReportController.java`; `./sources/backend/report-service/src/main/java/com/membershiphub/report/ReportService.java`; `./sources/backend/report-service/src/main/java/com/membershiphub/report/AttendanceCsvExporter.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-024], [REQ-025], [EXC-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `GET /api/v1/reports/attendance/daily` để tạo báo cáo điểm danh hàng ngày cho trung tâm định dạng CSV, bao gồm các cột: StudentName, CourseName, AttendanceDate, Status (Present/Absent/Late). Triển khai API `GET /api/v1/reports/dashboard/enrollment` để trả về dữ liệu tổng hợp cho dashboard: tổng số học viên đã đăng ký, số khóa học đang hoạt động, số buổi học sắp tới trong 7 ngày tiếp theo. Triển khai logic xử lý hàng đợi điểm danh chờ sau sự cố hệ thống [EXC-005]: xử lý các yêu cầu điểm danh đang lưu trong hàng đợi Redis theo thứ tự FIFO, đồng bộ với cơ sở dữ liệu chính, gửi thông báo cho người dùng về các sự kiện đã được xử lý.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:**
```sql
-- Thêm ràng buộc CHECK cho phần trăm giảm giá khuyến mãi [REQ-017]
ALTER TABLE promotions ADD CONSTRAINT chk_discount_percent CHECK (discount_percent BETWEEN 0 AND 100);

-- Tạo index cho bảng điểm danh để tối ưu truy vấn báo cáo [REQ-024], [NFR-001]
CREATE INDEX idx_attendance_student_course_date ON attendance (student_id, course_id, attendance_date);

-- Tạo index cho bảng ghi danh để tối ưu truy vấn dashboard [REQ-025], [NFR-001]
CREATE INDEX idx_enrollments_course_student ON enrollments (course_id, student_id);

-- Tạo index cho bảng khóa học để tối ưu truy vấn khóa học sắp tới [REQ-025], [NFR-001]
CREATE INDEX idx_courses_dates ON courses (start_date, end_date);

-- Tạo index cho bảng thông báo để tối ưu truy vấn thông báo chưa gửi [REQ-016], [NFR-001]
CREATE INDEX idx_notifications_delivered_sent ON notifications (delivered, sent_at);
```
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
```json
{
  "services": [
    {
      "serviceName": "report-service",
      "version": "v1",
      "endpoints": [
        {
          "method": "GET",
          "path": "/api/v1/reports/attendance/daily",
          "tags": ["REQ-024"],
          "parameters": [
            {"name": "centerId", "in": "query", "required": true, "type": "uuid"},
            {"name": "date", "in": "query", "required": true, "type": "date"}
          ],
          "response": {
            "contentType": "text/csv",
            "schema": {
              "columns": ["StudentName", "CourseName", "AttendanceDate", "Status"]
            }
          }
        },
        {
          "method": "GET",
          "path": "/api/v1/reports/dashboard/enrollment",
          "tags": ["REQ-025"],
          "parameters": [
            {"name": "centerId", "in": "query", "required": true, "type": "uuid"}
          ],
          "response": {
            "schema": {
              "type": "object",
              "properties": {
                "totalStudents": {"type": "integer"},
                "activeCourses": {"type": "integer"},
                "upcomingSessions": {"type": "integer"}
              }
            }
          }
        }
      ],
      "events": [
        {
          "topic": "report.generated",
          "tags": ["REQ-024", "REQ-025"],
          "payload": {
            "reportType": {"type": "string", "enum": ["ATTENDANCE_DAILY", "ENROLLMENT_DASHBOARD"]},
            "generatedAt": {"type": "timestamp"},
            "requestedBy": {"type": "uuid"}
          }
        }
      ]
    }
  ]
}
```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ [EXC-005] trả về mã lỗi 503 Service Unavailable với thông báo "Hệ thống đang khôi phục sau sự cố, vui lòng thử lại sau" nếu hàng đợi điểm danh chưa được xử lý xong. Sau khi xử lý xong, gửi thông báo cho người dùng về các sự kiện đã được xử lý.

#### 📝 Phụ công việc 2: Viết unit và integration test cho dịch vụ báo cáo
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/report-service/src/main/java/com/membershiphub/report/ReportService.java;./sources/backend/report-service/src/test/java/com/membershiphub/report/ReportServiceTest.java`; `INTEGRATION_SCOPE;./sources/backend/report-service/src/test/java/com/membershiphub/report/ReportIntegrationTest.java`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-024], [REQ-025], [EXC-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: tạo báo cáo điểm danh CSV thành công với dữ liệu chính xác, lấy dữ liệu dashboard thành công với các giá trị tổng hợp đúng, xử lý hàng đợi điểm danh chờ sau sự cố theo thứ tự FIFO, đồng bộ dữ liệu chính xác. Viết integration test cho luồng tạo báo cáo: gửi yêu cầu với centerId và date hợp lệ -> kiểm tra file CSV được tạo đúng định dạng, dữ liệu chính xác. Kiểm tra các trường hợp lỗi: centerId không tồn tại, date không hợp lệ. Đảm bảo độ phủ mã ít nhất 85% cho các lớp service.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 3: Kiểm tra chất lượng mã nguồn dịch vụ báo cáo
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/report-service/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[REQ-024], [REQ-025], [EXC-005], [NFR-001]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn report-service, kiểm tra logic tạo báo cáo CSV hoạt động đúng, logic tổng hợp dữ liệu dashboard chính xác, logic xử lý hàng đợi sau sự cố hoạt động đúng theo thứ tự FIFO, tối ưu truy vấn cơ sở dữ liệu để đảm bảo độ trễ API trung bình dưới 200ms [NFR-001], không có lỗi bảo mật (SQL injection, XSS). Đề xuất và thực hiện sửa lỗi nếu có.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.

#### 📝 Phụ công việc 4: Hoàn thiện tài liệu và xác nhận tích hợp giai đoạn
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/architecture/report-service-api.md`; `./sources/docs/architecture/system-overview.md`; `./sources/docs/architecture/integration-guide.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho report-service, bao gồm endpoint tạo báo cáo điểm danh và dashboard ghi danh, schema request/response, mã lỗi, ví dụ sử dụng, định dạng file CSV. Cập nhật tài liệu kiến trúc tổng quan hệ thống với tất cả các dịch vụ mới được triển khai trong giai đoạn 4. Viết tài liệu hướng dẫn tích hợp giữa các microservice (notification, promotion, chatbot, report) và giao diện người dùng (web, mobile).
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.