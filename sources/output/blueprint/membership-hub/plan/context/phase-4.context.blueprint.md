# Giai đoạn 4: <!--PHASE_NAME_START-->Tích hợp Chatbot AI, Hoàn thiện Giao diện Di động và Báo cáo Phân tích<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã bản thiết kế** | ARCH-20260822094056 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Tích hợp Chatbot AI, Hoàn thiện Giao diện Di động và Báo cáo Phân tích<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai tích hợp chatbot AI hỗ trợ trả lời câu hỏi thường gặp và leo thang hỗ trợ khi độ tin cậy thấp, xây dựng giao diện responsive cho ứng dụng di động với phân quyền theo vai trò, tích hợp thông báo đẩy FCM/APNs, triển khai phát hiện ngôn ngữ mặc định và SEO đa ngôn ngữ (hreflang, thẻ meta), xây dựng chức năng xuất báo cáo điểm danh CSV và bảng điều khiển tóm tắt ghi danh realtime. Giai đoạn này tập trung vào hoàn thiện trải nghiệm người dùng và khả năng phân tích dữ liệu.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/22 09:40:56 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 4 tập trung vào việc triển khai các tính năng nâng cao và giao diện người dùng cuối cho hệ thống membership-hub. Các mục tiêu kỹ thuật cốt lõi bao gồm: (1) Tích hợp chatbot AI với khả năng trả lời câu hỏi thường gặp về khóa học, giáo viên, trung tâm và trạng thái tài khoản, đồng thời leo thang hỗ trợ khi độ tin cậy thấp; (2) Xây dựng giao diện người dùng responsive cho ứng dụng di động với phân quyền theo vai trò (Student, Teacher, Admin), đồng bộ chức năng với phiên bản web; (3) Tích hợp thông báo đẩy FCM/APNs cho ứng dụng di động, quản lý token thiết bị và xử lý nhận thông báo; (4) Triển khai phát hiện ngôn ngữ mặc định từ cookie và Accept-Language header, hỗ trợ chuyển đổi ngôn ngữ không cần tải lại trang; (5) Triển khai SEO đa ngôn ngữ với thẻ meta và hreflang cho 3 ngôn ngữ (Anh, Việt, Tây Ban Nha); (6) Xây dựng chức năng xuất báo cáo điểm danh CSV cho quản trị viên với cơ chế xử lý FIFO cho điểm danh đang chờ sau sự cố hệ thống; (7) Xây dựng bảng điều khiển tóm tắt ghi danh realtime hiển thị tổng số học viên, khóa học đang hoạt động và buổi học sắp tới (7 ngày tới). Giai đoạn này đảm bảo tuân thủ nghiêm ngặt các ràng buộc RBAC, OWASP Top 10, và yêu cầu phi chức năng về hiệu năng, bảo mật và khả năng sẵn sàng.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục
Tất cả đường dẫn tệp đều bắt đầu với gốc kho lưu trữ `./sources/`, tuân thủ cấu trúc kiến trúc vi mô đã định nghĩa:
* **Hạ tầng backend vi mô Quarkus:**
  * ./sources/backend/ai-chatbot-service/pom.xml [ARC-000]
  * ./sources/backend/ai-chatbot-service/src/main/java/org/nlh4j/membership_hub/ai/ChatbotService.java [REQ-019]
  * ./sources/backend/ai-chatbot-service/src/main/java/org/nlh4j/membership_hub/ai/ChatbotController.java [REQ-019]
  * ./sources/backend/ai-chatbot-service/src/test/java/org/nlh4j/membership_hub/ai/ChatbotServiceTest.java [REQ-019]
  * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceReportService.java [REQ-024, EXC-005]
  * ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/ReportController.java [REQ-024]
  * ./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceReportIntegrationTest.java [REQ-024, EXC-005]
* **Lớp frontend Next.js:**
  * ./sources/frontend/package.json [ARC-000]
  * ./sources/frontend/tsconfig.json [ARC-000]
  * ./sources/frontend/src/app/[locale]/layout.tsx [REQ-022, REQ-023]
  * ./sources/frontend/src/app/[locale]/page.tsx [REQ-022, REQ-023]
  * ./sources/frontend/src/components/mobile/MobileDashboard.tsx [REQ-020]
  * ./sources/frontend/src/components/chat/ChatWidget.tsx [REQ-019]
  * ./sources/frontend/src/hooks/usePushNotifications.ts [REQ-021]
  * ./sources/frontend/src/lib/seo.ts [REQ-023]
  * ./sources/frontend/src/components/dashboard/EnrollmentDashboard.tsx [REQ-025]
  * ./sources/frontend/src/e2e/mobile-ui.spec.ts [REQ-020, REQ-021]
  * ./sources/frontend/src/e2e/dashboard-chatbot.spec.ts [REQ-025, REQ-019]
* **Tài liệu doanh nghiệp:**
  * ./sources/docs/ai-chatbot-api-spec.md [REQ-019]
  * ./sources/docs/report-api-spec.md [REQ-024]
  * ./sources/docs/mobile-ui-spec.md [REQ-020, REQ-022, REQ-023]
  * ./sources/docs/phase4-technical-spec.md [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]

## 3. Chỉ thị chức năng cho tác nhân phụ chuyên dụng
* **Coder**: Đóng vai trò là Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên cả backend services (ai-chatbot-service, attendance-service) và frontend/ứng dụng di động. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
* **Tester**: Đóng vai trò là Kiểm soát chất lượng (QC/QA) cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác thực hiệu năng. Bị cấm sửa mã nguồn sản xuất. Nếu mục tiêu nhiệm vụ liên quan đến phạm vi kiểm thử tích hợp hoặc end-to-end mà không có tệp mã ứng dụng cụ thể nào có thể bị giới hạn, bạn PHẢI xuất ra literal token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp dấu chấm phẩy.
* **Doc**: Hoạt động như là Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Đặc tả kỹ thuật toàn diện, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp kiến trúc đang hoạt động của dự án. Mỗi tệp tài liệu kỹ thuật được tạo PHẢI được liệt kê là thực thể đường dẫn tệp cụ thể có phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Chịu trách nhiệm xác minh trình biên dịch, cổng phân tích tĩnh và vá bảo vệ phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗi hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
Giai đoạn 4 được coi là hoàn thành khi đáp ứng đầy đủ các mốc định lượng sau:
1. Dịch vụ ai-chatbot-service được triển khai đầy đủ chức năng xử lý câu hỏi thường gặp và leo thang hỗ trợ khi độ tin cậy thấp, tích hợp với frontend qua endpoint REST.
2. Dịch vụ attendance-service được triển khai chức năng xuất báo cáo điểm danh CSV với cơ chế xử lý FIFO cho điểm danh đang chờ sau sự cố hệ thống (EXC-005).
3. Giao diện frontend responsive cho ứng dụng di động được triển khai đầy đủ với phân quyền theo vai trò, đồng bộ chức năng với phiên bản web.
4. Tích hợp thông báo đẩy FCM/APNs hoạt động đúng, quản lý token thiết bị và xử lý nhận thông báo trên ứng dụng di động.
5. Phát hiện ngôn ngữ mặc định hoạt động đúng với fallback Accept-Language, hỗ trợ chuyển đổi ngôn ngữ không cần tải lại trang.
6. SEO đa ngôn ngữ được triển khai với thẻ meta và hreflang cho 3 ngôn ngữ (Anh, Việt, Tây Ban Nha).
7. Bảng điều khiển tóm tắt ghi danh realtime hiển thị chính xác tổng số học viên, khóa học đang hoạt động và buổi học sắp tới (7 ngày tới).
8. Tất cả bộ kiểm thử đơn vị, tích hợp và E2E cho các thành phần giai đoạn 4 đều vượt qua, độ bao phủ mã đạt >= 85%.
9. Tất cả thẻ theo dõi yêu cầu được phân phối cho giai đoạn 4 ([REQ-019] đến [REQ-025], [EXC-005]) được ánh xạ đầy đủ vào các nhiệm vụ kỹ thuật và tài liệu, không có thẻ nào bị thiếu.

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC TỪNG NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Triển khai nền tảng backend cho chatbot AI và dịch vụ báo cáo điểm danh<!--DAY_HEADER_END-->

#### 📝 Công việc con 1.1: Khởi tạo module ai-chatbot-service
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/ai-chatbot-service/pom.xml
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo cấu trúc dự án Maven cho service vi mô ai-chatbot-service với các phụ thuộc Quarkus, RESTEasy Reactive, và thư viện xử lý ngôn ngữ tự nhiên. Định nghĩa module trong pom.xml gốc, đảm bảo cấu hình build thành công và tích hợp với hệ thống quản lý phụ thuộc tập trung.

#### 📝 Công việc con 1.2: Triển khai ChatbotService và ChatbotController
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/ai-chatbot-service/src/main/java/org/nlh4j/membership_hub/ai/ChatbotService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai lớp ChatbotService với logic xử lý câu hỏi thường gặp về khóa học, giáo viên, trung tâm và trạng thái tài khoản. Tích hợp mô hình NLP để phân loại ý định và trích xuất thực thể. Triển khai ChatbotController với endpoint POST /api/chatbot/message, xác thực JWT, và cơ chế leo thang hỗ trợ khi độ tin cậy thấp. Đảm bảo phản hồi JSON bao gồm các trường response, confidence, escalate và suggestedActions theo hợp đồng API đã định nghĩa.

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "POST /api/chatbot/message",
  "request": {
    "message": "string",
    "sessionId": "uuid",
    "context": {
      "userId": "uuid",
      "role": "string"
    }
  },
  "response": {
    "response": "string",
    "confidence": 0.95,
    "escalate": false,
    "suggestedActions": ["string"]
  }
}
```
<!--END_API_CONTRACT-->

#### 📝 Công việc con 1.3: Viết unit test cho ChatbotService
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/ai-chatbot-service/src/test/java/org/nlh4j/membership_hub/ai/ChatbotServiceTest.java;./sources/backend/ai-chatbot-service/src/main/java/org/nlh4j/membership_hub/ai/ChatbotService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test cho ChatbotService bao gồm các kịch bản: câu hỏi thường gặp được trả lời chính xác, leo thang hỗ trợ khi độ tin cậy thấp, xử lý ngữ cảnh người dùng. Sử dụng JUnit 5 và Mockito để giả lập các phụ thuộc ngoại vi, đảm bảo độ bao phủ mã >= 90%.

#### 📝 Công việc con 1.4: Viết tài liệu API cho chatbot
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/ai-chatbot-api-spec.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật chi tiết cho API chatbot theo chuẩn OpenAPI 3.0, bao gồm endpoint POST /api/chatbot/message, schema request/response đầy đủ, mã lỗi, ví dụ sử dụng, và hướng dẫn tích hợp frontend. Đảm bảo tài liệu phù hợp với tiêu chuẩn doanh nghiệp.

#### 📝 Công việc con 1.5: Triển khai AttendanceReportService cho xuất CSV
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/attendance-service/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceReportService.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-024], [EXC-005]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai lớp AttendanceReportService với phương thức generateAttendanceReport(centerId, startDate, endDate) trả về định dạng CSV. Bao gồm logic truy vấn dữ liệu điểm danh từ bảng attendance, xử lý FIFO cho các bản ghi đang chờ sau sự cố hệ thống, và gửi thông báo phục hồi cho người dùng. Đảm bảo CSV có các cột StudentName, CourseName, AttendanceDate, Status theo đúng định dạng yêu cầu.

<!--START_EXC_HANDLER-->
```java
// EXC-005: System Recovery After Outage
// Khi dịch vụ khôi phục, xử lý điểm danh đang chờ theo FIFO
public void processPendingAttendanceAfterRecovery() {
    List<Attendance> pendingAttendances = attendanceRepository.findPendingAfterOutage();
    for (Attendance attendance : pendingAttendances) {
        processAttendance(attendance);
        notificationService.sendRecoveryNotification(attendance.getStudentId(), attendance.getAttendanceDate());
    }
}
```
<!--END_EXC_HANDLER-->

#### 📝 Công việc con 1.6: Viết integration test cho dịch vụ báo cáo
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/backend/attendance-service/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceReportIntegrationTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-024], [EXC-005]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết integration test cho AttendanceReportService sử dụng Testcontainers với PostgreSQL. Kiểm tra: tạo báo cáo CSV chính xác với đúng định dạng cột, xử lý điểm danh trùng lặp, và kịch bản phục hồi sau sự cố hệ thống (EXC-005) với hàng đợi FIFO. Đảm bảo độ bao phủ mã >= 85%.

#### 📝 Công việc con 1.7: Viết tài liệu API cho báo cáo
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/report-api-spec.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-024]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho API báo cáo điểm danh theo chuẩn OpenAPI 3.0, bao gồm endpoint GET /api/reports/attendance/csv, tham số query (centerId, startDate, endDate), định dạng CSV, và ví dụ sử dụng. Đảm bảo tài liệu rõ ràng cho đội ngũ frontend và quản trị viên.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Triển khai giao diện người dùng di động, thông báo đẩy và tối ưu SEO đa ngôn ngữ<!--DAY_HEADER_END-->

#### 📝 Công việc con 2.1: Triển khai giao diện responsive cho ứng dụng di động
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/components/mobile/MobileDashboard.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-020]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng thành phần MobileDashboard responsive sử dụng Tailwind CSS, hiển thị menu điều hướng và màn hình phù hợp với vai trò người dùng (Student, Teacher, Admin). Đảm bảo đồng bộ chức năng với phiên bản web, hỗ trợ đa ngôn ngữ qua i18next, và tương thích với Capacitor để đóng gói ứng dụng di động hybrid.

#### 📝 Công việc con 2.2: Tích hợp thông báo đẩy FCM/APNs
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/hooks/usePushNotifications.ts
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-021]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai hook usePushNotifications để đăng ký token thiết bị với FCM/APNs, xử lý nhận thông báo, và hiển thị thông báo trong ứng dụng. Tích hợp với Firebase Cloud Messaging cho Android và Apple Push Notification service cho iOS. Đảm bảo xử lý các trường hợp: quyền thông báo bị từ chối, token hết hạn, và hiển thị thông báo khi ứng dụng ở foreground/background.

#### 📝 Công việc con 2.3: Triển khai phát hiện ngôn ngữ mặc định và định tuyến i18n
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/app/[locale]/layout.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-022]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai middleware phát hiện ngôn ngữ ưu tiên từ cookie đã lưu, sau đó fallback sang header Accept-Language. Cấu hình định tuyến Next.js với tham số [locale] để hỗ trợ đa ngôn ngữ mà không cần tải lại trang. Đảm bảo lưu trữ cài đặt ngôn ngữ vào cookie hoặc localStorage để duy trì trải nghiệm người dùng giữa các phiên.

#### 📝 Công việc con 2.4: Triển khai SEO đa ngôn ngữ với hreflang và thẻ meta
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/lib/seo.ts
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-023]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tiện ích SEO động để tạo thẻ meta ngôn ngữ cụ thể, thuộc tính hreflang cho 3 ngôn ngữ (Anh, Việt, Tây Ban Nha), và đảm bảo mỗi trang có thẻ `<html lang='xx'>` chính xác. Tích hợp với Next.js Metadata API để inject động các thẻ meta, hreflang links, và canonical URLs. Đảm bảo công cụ tìm kiếm có thể nhận diện đúng phiên bản ngôn ngữ của từng trang.

#### 📝 Công việc con 2.5: Viết E2E test cho giao diện di động và thông báo đẩy
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/frontend/src/e2e/mobile-ui.spec.ts
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết end-to-end test sử dụng Playwright hoặc Cypress để kiểm tra: giao diện responsive hiển thị đúng trên thiết bị di động (viewport sizes: 375px, 768px, 1024px), menu điều hướng theo vai trò hoạt động chính xác, và thông báo đẩy được nhận và hiển thị đúng. Mô phỏng các kịch bản: đăng nhập với vai trò khác nhau, nhận thông báo khi ứng dụng ở foreground và background.

#### 📝 Công việc con 2.6: Viết tài liệu kỹ thuật cho giao diện di động và SEO
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/mobile-ui-spec.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-020], [REQ-022], [REQ-023]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật chi tiết cho giao diện người dùng di động responsive, tích hợp thông báo đẩy, phát hiện ngôn ngữ và cấu hình SEO đa ngôn ngữ. Bao gồm hướng dẫn cấu hình, ví dụ code, bảng tra cứu vai trò người dùng, và quy trình kiểm thử đa ngôn ngữ. Đảm bảo tài liệu phù hợp với tiêu chuẩn doanh nghiệp.

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Triển khai dashboard tóm tắt ghi danh, tích hợp chatbot vào frontend và kiểm tra cuối cùng<!--DAY_HEADER_END-->

#### 📝 Công việc con 3.1: Triển khai EnrollmentDashboard component
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/components/dashboard/EnrollmentDashboard.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-025]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng thành phần EnrollmentDashboard hiển thị real-time các thẻ: tổng số học viên, số khóa học đang hoạt động, và các buổi học sắp tới (7 ngày tới). Tích hợp với API GET /api/dashboard/enrollment-summary và cập nhật tự động mỗi 5 phút. Sử dụng React Query hoặc SWR để caching và tự động refetch, đảm bảo hiển thị skeleton loading state trong khi chờ dữ liệu.

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "GET /api/dashboard/enrollment-summary",
  "response": {
    "totalStudents": 100,
    "activeCourses": 5,
    "upcomingSessions": 12
  }
}
```
<!--END_API_CONTRACT-->

#### 📝 Công việc con 3.2: Tích hợp ChatbotWidget vào frontend
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/frontend/src/components/chat/ChatWidget.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng thành phần ChatWidget có thể đóng/mở, tích hợp với endpoint POST /api/chatbot/message, quản lý trạng thái sessionId, và hiển thị gợi ý hành động khi chatbot leo thang hỗ trợ. Đảm bảo widget hoạt động trên tất cả các trang, lắng nghe sự kiện click để mở/đóng, và lưu trữ lịch sử trò chuyện trong session.

#### 📝 Công việc con 3.3: Viết integration test cho dashboard và chatbot
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/frontend/src/e2e/dashboard-chatbot.spec.ts
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-025], [REQ-019]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết integration test kiểm tra: dashboard hiển thị đúng số liệu từ API, chatbot phản hồi chính xác các câu hỏi thường gặp, và leo thang hỗ trợ hoạt động khi độ tin cậy thấp. Sử dụng Playwright với mock API responses, kiểm tra các trường hợp: câu hỏi về khóa học, giáo viên, trung tâm, và trạng thái tài khoản.

#### 📝 Công việc con 3.4: Rà soát mã và tối ưu hóa các thành phần giai đoạn 4
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/ai-chatbot-service/src/main/java/org/nlh4j/membership_hub/ai/ChatbotService.java;./sources/frontend/src/components/mobile/MobileDashboard.tsx
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát mã toàn bộ các thành phần backend và frontend của giai đoạn 4. Kiểm tra chất lượng mã, phát hiện bottleneck hiệu năng (ví dụ: truy vấn N+1 trong dashboard, thiếu indexing cho báo cáo), đảm bảo tuân thủ OWASP Top 10 (chống XSS trong chatbot response, chống injection trong báo cáo), và đề xuất chiến lược sửa chữa cụ thể. Tối ưu hóa truy vấn cơ sở dữ liệu cho dịch vụ báo cáo và cơ chế phục hồi sau sự cố (EXC-005).

#### 📝 Công việc con 3.5: Hoàn thiện tài liệu kỹ thuật giai đoạn 4
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/phase4-technical-spec.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tổng hợp và hoàn thiện tài liệu kỹ thuật toàn diện cho giai đoạn 4, bao gồm: đặc tả API chatbot, báo cáo và dashboard; hướng dẫn tích hợp thông báo đẩy; cấu hình SEO đa ngôn ngữ; và quy trình xử lý phục hồi sau sự cố (EXC-005). Bao gồm sơ đồ kiến trúc, luồng dữ liệu, bảng tra cứu endpoint, và hướng dẫn triển khai cho đội ngũ vận hành. Đảm bảo tài liệu phù hợp với tiêu chuẩn doanh nghiệp.