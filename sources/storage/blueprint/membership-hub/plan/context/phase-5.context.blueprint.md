# [Giai đoạn] 5: <!--PHASE_NAME_START-->Tích hợp các tính năng ứng dụng di động và cơ sở hạ tầng DevOps<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID bản thiết kế** | ARCH-20260817193854 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Tích hợp các tính năng ứng dụng di động và cơ sở hạ tầng DevOps<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc tích hợp các tính năng ứng dụng di động bao gồm giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.), gửi thông báo đẩy cho người dùng trên thiết bị di động, phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha). Ngoài ra, xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/17 19:38:54 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc tích hợp các tính năng ứng dụng di động bao gồm giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.), gửi thông báo đẩy cho người dùng trên thiết bị di động, phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha). Ngoài ra, xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/frontend/`
- `./sources/backend/report/`
- `./sources/backend/exception/`
- `./sources/backend/architecture/`
- `./sources/infra/`

## 3. Hướng dẫn chức năng của các chuyên gia con được chỉ định
*   **Coder**: Hoạt động như một Nhà phát triển ứng dụng cấp cao/Chủ tịch. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Trưởng/QC/QA cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con tác vụ liên quan đến phạm vi tích hợp hoặc kết thúc-to-end tổng thể nơi không có tệp mã cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh trình biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về việc đóng gói, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các tính năng ứng dụng di động bao gồm giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.), gửi thông báo đẩy cho người dùng trên thiết bị di động, phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha).
- Hoàn thành 100% cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% các bộ kiểm thử chức năng và tích hợp.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc hàng ngày

### 🌤️ [Ngày] 1: Tích hợp các tính năng ứng dụng di động và cơ sở hạ tầng DevOps

#### 📝 [Nhiệm vụ con] 1.1: Xây dựng giao diện người dùng phù hợp với vai trò của người dùng
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/src/components/UserDashboard.js

* **TagID mục tiêu:** [REQ-020]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.).

#### 📝 [Nhiệm vụ con] 1.2: Viết kiểm thử cho giao diện người dùng phù hợp với vai trò của người dùng
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/src/components/UserDashboard.js;./sources/frontend/src/tests/UserDashboard.test.js

* **TagID mục tiêu:** [REQ-020]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.).

#### 📝 [Nhiệm vụ con] 1.3: Tài liệu giao diện người dùng phù hợp với vai trò của người dùng
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/frontend.md

* **TagID mục tiêu:** [REQ-020]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu giao diện người dùng phù hợp với vai trò của người dùng (Học viên, Giáo viên, Quản trị viên, v.v.).

#### 📝 [Nhiệm vụ con] 1.4: Xây dựng chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notification/src/main/java/org/nlh4j/membership_hub/notification/PushNotificationService.java

* **TagID mục tiêu:** [REQ-021]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động.

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/push-notifications",
      "method": "POST",
      "request": {
        "user_id": "UUID",
        "title": "string",
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
@ExceptionHandler(PushNotificationException.class)
public ResponseEntity<ErrorResponse> handlePushNotification(PushNotificationException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Push notification failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
}
```
<!--END_EXC_HANDLER-->

#### 📝 [Nhiệm vụ con] 1.5: Viết kiểm thử cho chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notification/src/main/java/org/nlh4j/membership_hub/notification/PushNotificationService.java;./sources/backend/notification/src/test/java/org/nlh4j/membership_hub/notification/PushNotificationTest.java

* **TagID mục tiêu:** [REQ-021]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động.

#### 📝 [Nhiệm vụ con] 1.6: Tài liệu chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/notification.md

* **TagID mục tiêu:** [REQ-021]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gửi thông báo đẩy cho người dùng trên thiết bị di động.

#### 📝 [Nhiệm vụ con] 1.7: Xây dựng chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/src/utils/LocaleDetector.js

* **TagID mục tiêu:** [REQ-022] [REQ-023]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha).

#### 📝 [Nhiệm vụ con] 1.8: Viết kiểm thử cho chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/src/utils/LocaleDetector.js;./sources/frontend/src/tests/LocaleDetector.test.js

* **TagID mục tiêu:** [REQ-022] [REQ-023]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha).

#### 📝 [Nhiệm vụ con] 1.9: Tài liệu chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/frontend.md

* **TagID mục tiêu:** [REQ-022] [REQ-023]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng phát hiện ngôn ngữ mặc định và hỗ trợ SEO cho nhiều ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha).

#### 📝 [Nhiệm vụ con] 1.10: Xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes
##### Chuyên gia con được chỉ định: Docker, GCP, GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/docker/Dockerfile;./sources/infra/terraform/main.tf;./sources/infra/k8s/deployment.yaml

* **TagID mục tiêu:** [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

#### 📝 [Nhiệm vụ con] 1.11: Viết kiểm thử cho cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/infra/tests/integration_test.go

* **TagID mục tiêu:** [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

#### 📝 [Nhiệm vụ con] 1.12: Tài liệu cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/infra.md

* **TagID mục tiêu:** [NFR-001] [NFR-002] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu cơ sở hạ tầng DevOps bao gồm các tập lệnh Docker, thiết lập môi trường đám mây thông qua Terraform và các biểu mẫu điều phối cụm Kubernetes.

### 🌤️ [Ngày] 2: Xây dựng chức năng tạo báo cáo điểm danh hàng ngày và bảng điều khiển tổng quan cho quản trị viên trung tâm

#### 📝 [Nhiệm vụ con] 2.1: Xây dựng chức năng tạo báo cáo điểm danh hàng ngày
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/report/src/main/java/org/nlh4j/membership_hub/report/AttendanceReportService.java

* **TagID mục tiêu:** [REQ-024]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng tạo báo cáo điểm danh hàng ngày.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE attendance_reports (
    report_id UUID PRIMARY KEY,
    center_id UUID REFERENCES centers(center_id),
    report_date DATE NOT NULL,
    report_data JSONB NOT NULL,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/attendance-reports",
      "method": "POST",
      "request": {
        "center_id": "UUID",
        "report_date": "date"
      },
      "response": {
        "report_id": "UUID",
        "status": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(AttendanceReportGenerationException.class)
public ResponseEntity<ErrorResponse> handleAttendanceReportGeneration(AttendanceReportGenerationException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Attendance report generation failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
}
```
<!--END_EXC_HANDLER-->

#### 📝 [Nhiệm vụ con] 2.2: Viết kiểm thử cho chức năng tạo báo cáo điểm danh hàng ngày
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/report/src/main/java/org/nlh4j/membership_hub/report/AttendanceReportService.java;./sources/backend/report/src/test/java/org/nlh4j/membership_hub/report/AttendanceReportTest.java

* **TagID mục tiêu:** [REQ-024]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng tạo báo cáo điểm danh hàng ngày.

#### 📝 [Nhiệm vụ con] 2.3: Tài liệu chức năng tạo báo cáo điểm danh hàng ngày
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/report.md

* **TagID mục tiêu:** [REQ-024]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng tạo báo cáo điểm danh hàng ngày.

#### 📝 [Nhiệm vụ con] 2.4: Xây dựng bảng điều khiển tổng quan cho quản trị viên trung tâm
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/report/src/main/java/org/nlh4j/membership_hub/report/DashboardService.java

* **TagID mục tiêu:** [REQ-025]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng bảng điều khiển tổng quan cho quản trị viên trung tâm.

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/dashboard",
      "method": "GET",
      "request": {
        "center_id": "UUID"
      },
      "response": {
        "total_students": "integer",
        "active_courses": "integer",
        "upcoming_sessions": "integer"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(DashboardDataException.class)
public ResponseEntity<ErrorResponse> handleDashboardData(DashboardDataException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Dashboard data retrieval failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
}
```
<!--END_EXC_HANDLER-->

#### 📝 [Nhiệm vụ con] 2.5: Viết kiểm thử cho bảng điều khiển tổng quan cho quản trị viên trung tâm
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/report/src/main/java/org/nlh4j/membership_hub/report/DashboardService.java;./sources/backend/report/src/test/java/org/nlh4j/membership_hub/report/DashboardTest.java

* **TagID mục tiêu:** [REQ-025]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho bảng điều khiển tổng quan cho quản trị viên trung tâm.

#### 📝 [Nhiệm vụ con] 2.6: Tài liệu bảng điều khiển tổng quan cho quản trị viên trung tâm
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/report.md

* **TagID mục tiêu:** [REQ-025]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu bảng điều khiển tổng quan cho quản trị viên trung tâm.

#### 📝 [Nhiệm vụ con] 2.7: Xây dựng chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/exception/src/main/java/org/nlh4j/membership_hub/exception/ExceptionHandler.java

* **TagID mục tiêu:** [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố.

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(NetworkException.class)
public ResponseEntity<ErrorResponse> handleNetworkException(NetworkException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Network error", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.SERVICE_UNAVAILABLE);
}

@ExceptionHandler(DuplicateAttendanceException.class)
public ResponseEntity<ErrorResponse> handleDuplicateAttendance(DuplicateAttendanceException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Duplicate attendance", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.CONFLICT);
}

@ExceptionHandler(NotificationDeliveryException.class)
public ResponseEntity<ErrorResponse> handleNotificationDelivery(NotificationDeliveryException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Notification delivery failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
}

@ExceptionHandler(InvalidInputException.class)
public ResponseEntity<ErrorResponse> handleInvalidInput(InvalidInputException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Invalid input", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
}

@ExceptionHandler(SystemRecoveryException.class)
public ResponseEntity<ErrorResponse> handleSystemRecovery(SystemRecoveryException ex) {
    ErrorResponse errorResponse = new ErrorResponse("System recovery failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
}
```
<!--END_EXC_HANDLER-->

#### 📝 [Nhiệm vụ con] 2.8: Viết kiểm thử cho chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/exception/src/main/java/org/nlh4j/membership_hub/exception/ExceptionHandler.java;./sources/backend/exception/src/test/java/org/nlh4j/membership_hub/exception/ExceptionHandlerTest.java

* **TagID mục tiêu:** [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố.

#### 📝 [Nhiệm vụ con] 2.9: Tài liệu chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/exception.md

* **TagID mục tiêu:** [EXC-001] [EXC-002] [EXC-003] [EXC-004] [EXC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xử lý ngoại lệ khi mạng bị gián đoạn, điểm danh trùng lặp, thông báo không được gửi, đầu vào không hợp lệ, phục hồi hệ thống sau sự cố.

#### 📝 [Nhiệm vụ con] 2.10: Xây dựng cơ sở dữ liệu và xác thực mã thông báo cho hệ thống
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/architecture/src/main/java/org/nlh4j/membership_hub/architecture/DatabaseService.java

* **TagID mục tiêu:** [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng cơ sở dữ liệu và xác thực mã thông báo cho hệ thống.

<!--START_DDL_MIGRATION-->
```sql
CREATE TABLE system_tokens (
    token_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    token_type VARCHAR(50) NOT NULL,
    token_value TEXT NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
<!--END_DDL_MIGRATION-->

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    {
      "path": "/api/tokens",
      "method": "POST",
      "request": {
        "user_id": "UUID",
        "token_type": "string",
        "expires_at": "timestamp"
      },
      "response": {
        "token_id": "UUID",
        "token_value": "string"
      }
    }
  ]
}
```
<!--END_API_CONTRACT-->

<!--START_EXC_HANDLER-->
```java
@ExceptionHandler(TokenValidationException.class)
public ResponseEntity<ErrorResponse> handleTokenValidation(TokenValidationException ex) {
    ErrorResponse errorResponse = new ErrorResponse("Token validation failed", ex.getMessage());
    return new ResponseEntity<>(errorResponse, HttpStatus.UNAUTHORIZED);
}
```
<!--END_EXC_HANDLER-->

#### 📝 [Nhiệm vụ con] 2.11: Viết kiểm thử cho cơ sở dữ liệu và xác thực mã thông báo cho hệ thống
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/architecture/src/main/java/org/nlh4j/membership_hub/architecture/DatabaseService.java;./sources/backend/architecture/src/test/java/org/nlh4j/membership_hub/architecture/DatabaseTest.java

* **TagID mục tiêu:** [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho cơ sở dữ liệu và xác thực mã thông báo cho hệ thống.

#### 📝 [Nhiệm vụ con] 2.12: Tài liệu cơ sở dữ liệu và xác thực mã thông báo cho hệ thống
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/architecture.md

* **TagID mục tiêu:** [ARC-001] [ARC-002] [ARC-003] [ARC-004] [ARC-005] [ARC-006] [ARC-007] [ARC-008] [ARC-009]

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu cơ sở dữ liệu và xác thực mã thông báo cho hệ thống.