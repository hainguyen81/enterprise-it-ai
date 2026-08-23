# Giai đoạn 4: <!--PHASE_NAME_START-->Điều Phối Thông Báo Đa Kênh, Khuyến Mãi, Chatbot AI Và Trải Nghiệm Di Động Đa Ngôn Ngữ<!--PHASE_NAME_END-->

## 📊 Kiểm soát Tài liệu

| Hạng mục | Chi tiết |
| :--- | :--- |
| **ID Bản thiết kế** | ARCH-20260823050512 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Điều Phối Thông Báo Đa Kênh, Khuyến Mãi, Chatbot AI Và Trải Nghiệm Di Động Đa Ngôn Ngữ<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 4 bàn giao lớp giao tiếp và tương tác đa kênh của nền tảng membership-hub trên ba microservices mới và hai ứng dụng client. notification-service điều phối thông báo đa kênh FCM/APNs/Zalo cho các sự kiện phân công giáo viên, ghi danh học viên và announcement theo cơ chế persist-trước-fan-out, đăng ký device token sau login lưu trên Redis, kèm chính sách retry tối đa 3 lần với khoảng nghỉ luỹ thừa trước khi đánh dấu thất bại vĩnh viễn [REQ-016], [EXC-003], [REQ-021]. promotion-service cung cấp CRUD khuyến mãi với mã unique trả 409 khi trùng, discountPercent trong khoảng 1–100 và quy tắc endDate bỏ trống coi là khuyến mãi vĩnh viễn [REQ-017], cùng CRUD announcement tự động ẩn sau ngày hết hạn qua bộ lọc cửa sổ hiệu lực [REQ-018]. chatbot-service trả lời truy vấn về khóa học, giáo viên, trung tâm và trạng thái tài khoản kèm điểm confidence, tự động escalate lên nhân viên hỗ trợ khi độ tin cậy thấp và ghi toàn bộ hội thoại vào AuditLog [REQ-019]. mobile-app React Native render giao diện responsive theo vai trò Student/Teacher/Admin trên Android/iOS [REQ-020], đăng ký device token và xử lý deep-link push tới màn hình đích [REQ-021]. web-app Next.js phát hiện ngôn ngữ ưu tiên theo thứ tự preference đã lưu rồi fallback Accept-Language với mặc định 'vi', chuyển locale không cần reload trang [REQ-022], đồng thời SSR meta tags cùng bộ hreflang alternate links cho en/vi/es phục vụ crawler lập chỉ mục [REQ-023].<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/23 05:05:12 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 1. Phạm vi Vận hành Giai đoạn & Mục tiêu

Giai đoạn 4 bàn giao toàn bộ lớp giao tiếp và tương tác của nền tảng membership-hub, bao phủ trọn vẹn Task 18, Task 19, Task 20, Task 21, Task 22, Task 23, Task 24 và Task 25 của Master Backlog trên ba microservices backend mới (notification-service, promotion-service, chatbot-service) và hai ứng dụng client (web-app Next.js, mobile-app React Native).

Thứ nhất, notification-service kiến tạo pipeline điều phối thông báo đa kênh: NotificationOrchestrationService tiêu thụ các sự kiện nghiệp vụ từ topic `course.teacher.events` (teacher.assigned.v1 do course-service phát ở Giai đoạn 2), topic `enrollment.created` (do enrollment-service phát ở Giai đoạn 3) và topic `notification.dispatch`, persist bản ghi Notifications trước khi fan-out để bảo đảm không mất thông báo, rồi điều phối đồng thời tới kênh PUSH (FCM cho Android, APNs cho iOS) và kênh ZALO (đăng tin nhắn nhóm Zalo qua Zalo Open API) theo giá trị delivery_channels [REQ-016]. Device token được đăng ký ngay sau login qua POST /api/v1/devices/token, lưu ánh xạ userId–deviceToken trên Redis với TTL 7 ngày làm mới mỗi lần đăng nhập lại [REQ-021]. Khi kênh giao hàng thất bại (device token invalid, lỗi tạm thời mạng hoặc timeout), hệ thống ghi nhận thất bại kèm timestamp và lập lịch retry tối đa ba lần với khoảng nghỉ luỹ thừa trước khi đánh dấu thất bại vĩnh viễn kèm failure_reason [EXC-003].

Thứ hai, promotion-service cung cấp CRUD khuyến mãi GET/POST/PUT/DELETE /api/v1/promotions dành cho Center Admin và Manager: mã code unique trả 409 PROMO_CODE_DUPLICATED khi trùng, discountPercent bị ràng buộc trong khoảng 1–100, endDate bỏ trống được đánh dấu khuyến mãi vĩnh viễn và luôn hiển thị trong danh sách ưu đãi phía học viên [REQ-017]; song song, CRUD thông báo công khai /api/v1/announcements với title tối đa 150 ký tự, content tối đa 2000 ký tự, expiry tùy chọn và cơ chế tự động ẩn sau ngày hết hạn đã cấu hình nhờ bộ lọc cửa sổ hiệu lực tận dụng idx_announcements_visibility_window [REQ-018].

Thứ ba, chatbot-service công bố POST /api/v1/chatbot/query trả lời truy vấn tự nhiên về khóa học, giáo viên, trung tâm và trạng thái tài khoản kèm điểm confidence; khi độ tin cậy xuống dưới ngưỡng cấu hình trong SystemSettings, engine kích hoạt escalate chuyển phiên cho nhân viên hỗ trợ và ghi toàn bộ hội thoại vào AuditLog phục vụ truy vết [REQ-019].

Thứ tư, mobile-app React Native render điều hướng động theo roleId ngay sau đăng nhập với bộ màn hình riêng cho Student, Teacher và Admin trên cả Android lẫn iOS [REQ-020]; dịch vụ push xin quyền, lấy device token FCM/APNs, đăng ký lên backend và xử lý deep-link điều hướng sâu tới màn hình liên quan ở cả trạng thái cold-start lẫn background [REQ-021]. Cuối cùng, web-app Next.js vận hành middleware phát hiện ngôn ngữ theo thứ tự ưu tiên preference đã lưu → Accept-Language header → mặc định 'vi' với khả năng chuyển locale không cần reload trang [REQ-022], đồng thời component SEO SSR phát sinh thuộc tính html lang cùng bộ link rel='alternate' hreflang cho en/vi/es và meta tags bản địa hóa phục vụ crawler lập chỉ mục [REQ-023].

## 2. Phạm vi Kỹ thuật Được phép & Ranh giới Thư mục (Tệp, đường dẫn và Endpoint)

* **Ma trận thư mục Backend được phép:**
    * ./sources/backend/notification-service/pom.xml [ARC-000]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/service/NotificationOrchestrationService.java [REQ-016]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/api/NotificationDispatchResource.java [REQ-016]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/channel/FcmApnsPushAdapter.java [REQ-016]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/channel/ZaloGroupChannelAdapter.java [REQ-016]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/api/DeviceTokenResource.java [REQ-021]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/retry/DeliveryRetryScheduler.java [REQ-016], [EXC-003]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/exception/NotificationDeliveryException.java [EXC-003]
    * ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/exception/NotificationDeliveryExceptionMapper.java [EXC-003]
    * ./sources/backend/notification-service/src/main/resources/db/migration/V4__phase4_notification_delivery_tracking.sql [REQ-016], [EXC-003]
    * ./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/retry/DeliveryRetrySchedulerTest.java [REQ-016], [EXC-003]
    * ./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/channel/MultiChannelDispatchIT.java [REQ-016]
    * ./sources/backend/promotion-service/pom.xml [ARC-000]
    * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/api/PromotionResource.java [REQ-017]
    * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/service/PromotionService.java [REQ-017]
    * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/api/AnnouncementResource.java [REQ-018]
    * ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/service/AnnouncementExpiryFilter.java [REQ-018]
    * ./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/service/PromotionServiceTest.java [REQ-017]
    * ./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/api/AnnouncementExpiryIT.java [REQ-018]
    * ./sources/backend/chatbot-service/pom.xml [ARC-000]
    * ./sources/backend/chatbot-service/src/main/java/org/nlh4j/membership_hub/chatbot/api/ChatbotResource.java [REQ-019]
    * ./sources/backend/chatbot-service/src/main/java/org/nlh4j/membership_hub/chatbot/service/ChatbotEngineService.java [REQ-019]
    * ./sources/backend/chatbot-service/src/test/java/org/nlh4j/membership_hub/chatbot/service/ChatbotEscalationIT.java [REQ-019]
* **Ma trận thư mục Frontend được phép:**
    * ./sources/frontend/mobile-app/src/navigation/RoleBasedNavigator.tsx [REQ-020]
    * ./sources/frontend/mobile-app/src/screens/RoleDashboardScreen.tsx [REQ-020]
    * ./sources/frontend/mobile-app/src/services/PushNotificationService.ts [REQ-021]
    * ./sources/frontend/mobile-app/src/services/DeepLinkHandler.ts [REQ-021]
    * ./sources/frontend/web-app/src/middleware/localeDetection.ts [REQ-022]
    * ./sources/frontend/web-app/src/components/seo/HreflangHeadManager.tsx [REQ-023]
    * ./sources/frontend/mobile-app/__tests__/RoleBasedNavigator.test.tsx [REQ-020]
    * ./sources/frontend/mobile-app/__tests__/PushDeepLink.e2e.ts [REQ-021]
    * ./sources/frontend/web-app/__tests__/localeDetection.test.ts [REQ-022]
* **Ma trận thư mục Tài liệu được phép:**
    * ./sources/docs/api-notification-service-spec.md [REQ-016], [EXC-003]
    * ./sources/docs/api-promotion-service-spec.md [REQ-017], [REQ-018]
    * ./sources/docs/chatbot-integration-guide.md [REQ-019]
    * ./sources/docs/localization-seo-guide.md [REQ-022], [REQ-023]
    * ./sources/docs/mobile-push-deeplink-guide.md [REQ-021]
* **Mẫu định tuyến Endpoint được phép trong giai đoạn:**
    * POST /api/v1/notifications/dispatch — BEARER JWT, role=SYSTEM_ADMIN/CENTER_ADMIN/MANAGER [REQ-016]
    * POST /api/v1/devices/token — BEARER JWT, mọi vai trò đã xác thực [REQ-021]
    * GET/POST/PUT/DELETE /api/v1/promotions — ghi: CENTER_ADMIN/MANAGER; đọc: mọi vai trò đã xác thực, STUDENT tự lọc cửa sổ hiệu lực [REQ-017]
    * GET/POST/PUT/DELETE /api/v1/announcements — ghi: CENTER_ADMIN/MANAGER; đọc: mọi vai trò đã xác thực [REQ-018]
    * POST /api/v1/chatbot/query — BEARER JWT, mọi vai trò đã xác thực [REQ-019]
* **Mẫu định tuyến Sự kiện được phép trong giai đoạn:**
    * Consume: topic `course.teacher.events` (teacher.assigned.v1) — producer course-service, consumer notification-service, deduplicate theo eventId [REQ-016]
    * Consume: topic `enrollment.created` — producer enrollment-service, consumer notification-service, deduplicate theo eventId [REQ-016]
    * Consume: topic `notification.dispatch` — hàng đợi lệnh gửi thông báo nội bộ, consumer duy nhất notification-service [REQ-016]
    * Tích hợp ngoài: FCM HTTP v1 API, Apple APNs Provider API, Zalo Open Platform REST API [REQ-016], [REQ-021]
* **Ranh giới cấm xâm phạm:** mọi module và endpoint thuộc reporting-service cùng toàn bộ cây ./sources/infra/ được dành riêng cho Giai đoạn 5; Giai đoạn 4 nghiêm cấm phát sinh tệp ngoài ma trận trên và cấm tái tạo bất kỳ tệp nào đã tồn tại từ Giai đoạn 1 đến Giai đoạn 3 (descriptor cha, auth-service, db-migrations chuỗi trung tâm V1–V9, center-service, course-service, api-gateway, enrollment-service, attendance-service, card-service, manifest workspace frontend gốc).

* **INVARIANT KHUNG NỀN TẢNG BẮT BUỘC (PLATFORM SKELETON MANIFEST INVARIANTS)**:
    * Descriptor hạ tầng repository gốc `./sources/backend/pom.xml` và workspace frontend `./sources/frontend/package.json` cùng `./sources/frontend/tsconfig.json` đã được neo vĩnh viễn tại Giai đoạn 1 - NGÀY 1 theo token kiến trúc [ARC-000]; Giai đoạn 4 nghiêm cấm tái tạo hoặc ghi đè các descriptor nền móng này.
    * Với ba module dịch vụ mới gia nhập chuỗi microservices ở giai đoạn này (notification-service, promotion-service, chatbot-service), bắt buộc đăng ký descriptor module con độc lập `./sources/backend/<service-name>/pom.xml` kế thừa parent membership-hub-backend TRƯỚC khi phát hành bất kỳ thành phần mã nguồn ứng dụng nào của module đó; toàn bộ descriptor scaffolding sinh ra phải ánh xạ nghiêm ngặt vào token theo dõi kiến trúc [ARC-000].
    * Hai ứng dụng client web-app và mobile-app vận hành trên workspace chung đã khai báo workspaces tại `./sources/frontend/package.json`; Giai đoạn 4 chỉ bổ sung cây nguồn bên trong `./sources/frontend/web-app/` và `./sources/frontend/mobile-app/` mà không chỉnh sửa manifest gốc.

## 3. Chỉ đạo Chức năng Sub-Agent Chuyên trách

Theo ma trận phân công của Giai đoạn 4, các Sub-Agent được kích hoạt gồm Coder, Tester, Reviewer và Doc; Docker, GCP và GKE được dự phòng và chỉ kích hoạt từ Giai đoạn 5.

* **Coder**: Đóng vai trò Lập trình viên Ứng dụng Cấp cao/Principal. Chịu trách nhiệm hiện thực mã nguồn ứng dụng thuần túy: descriptor Maven module con cho notification-service, promotion-service và chatbot-service; pipeline điều phối đa kênh, adapter FCM/APNs/Zalo, scheduler retry và registry device token; CRUD khuyến mãi và thông báo công khai kèm bộ lọc hết hạn; engine chatbot và lộ trình escalate; navigator/dashboard/services của mobile-app; middleware locale và component SEO của web-app; chuỗi migration V4. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng DevOps.
* **Tester**: Đóng vai trò Trưởng QC/QA Principal. Chuyên về kỹ nghệ bộ kiểm thử, xác nhận và cổng chất lượng. Chịu trách nhiệm sinh JUnit unit test, integration test trên Testcontainers PostgreSQL/Kafka với WireMock mô phỏng FCM/APNs/Zalo, E2E automation cho luồng push deep-link và đo độ trễ đối chiếu [NFR-001]. Bị cấm sửa mã production. Khi phạm vi kiểm thử mang tính tích hợp tổng thể hoặc E2E không cô lập được một tệp production đơn lẻ, bắt buộc dùng định dạng cặp semicolon với token `INTEGRATION_SCOPE` đứng đầu (ví dụ: `INTEGRATION_SCOPE;./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/channel/MultiChannelDispatchIT.java`).
* **Doc**: Đóng vai trò Nhà văn Kỹ thuật Principal và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên biên soạn tài liệu đặc tả kỹ thuật, tham chiếu API, sơ đồ sự kiện và catalog hợp đồng phù hợp topology dự án. Mọi tệp tài liệu phải là đường dẫn tệp tường minh đuôi `.md` nằm trong kho lưu trữ tập trung `./sources/docs/`. Theo luật định giai đoạn, Doc phải được phân công tối thiểu một nhiệm vụ nền móng ngay NGÀY 1 để khởi tạo khung tài liệu markdown tham chiếu API notification-service tương thích stack Java/Quarkus/PostgreSQL/Redis/Kafka của ngữ cảnh này.
* **Reviewer**: Chịu trách nhiệm xác minh biên dịch, cổng phân tích tĩnh và vá phòng thủ. Chuyên kiểm toán chất lượng mã, phân tích race condition giữa orchestrator và scheduler, tính idempotent tiêu thụ sự kiện, khắc phục lỗ hổng bảo mật OWASP Top 10 (đặc biệt kiểm soát truy cập hỏng A01 trên quyền sở hữu device token và injection A03 trên đầu vào nội dung), gỡ blocker SonarQube trước khi merge; ký duyệt điều kiện mở khóa giữa các ngày làm việc.
* **Docker**: Chuyên container hóa, kỹ nghệ Dockerfile multi-stage, tối ưu dung lượng image và đẩy image đã kiểm chứng lên registry. Trong Giai đoạn 4 chưa được phân công nhiệm vụ cụ thể.
* **GCP**: Chuyên tự động hóa trên Google Cloud Platform: build/push image lên Artifact Registry và điều phối môi trường container trên Cloud Run. Trong Giai đoạn 4 chưa được phân công nhiệm vụ cụ thể.
* **GKE**: Chuyên điều phối container production trong Google Kubernetes Engine: manifest deployment, routing control, cấu hình HPA, Helm chart và triển khai workload microservices. Trong Giai đoạn 4 chưa được phân công nhiệm vụ cụ thể.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)

* 100% thẻ truy vết của giai đoạn ([REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]) được ánh xạ tường minh vào nhật ký ngày qua container `<!--START_TAGS-->` không gaps, không trùng lặp sai ngữ cảnh.
* `mvn -q verify` sạch trên ba descriptor module con mới (notification-service, promotion-service, chatbot-service); cây Maven không xung đột phiên bản với parent membership-hub-backend và Quarkus BOM 3.15.x.
* Pipeline điều phối: bản ghi Notifications được persist trước khi fan-out; cờ delivered chỉ bật true khi toàn bộ kênh mục tiêu xác nhận thành công; fan-out một phần giữ delivered=false nhường vòng retry kế tiếp; mỗi lần dispatch ghi audit log kèm userId và timestamp [REQ-016].
* Chính sách retry: đúng tối đa 3 lần thử với khoảng nghỉ luỹ thừa; sau lần thử thứ ba thất bại, bản ghi bị đánh dấu thất bại vĩnh viễn kèm failure_reason và không còn được quét lại; nhiều pod chạy song tranh chấp an toàn nhờ UPDATE điều kiện, không phát sinh dispatch kép [EXC-003].
* Device token: đăng ký ngay sau login, re-register khi token xoay vòng, ánh xạ lưu Redis TTL 7 ngày; userId suy nghiêm ngặt từ claim sub của JWT chống leo thang gán token chéo tài khoản theo OWASP A01; token sai định dạng trả 400 DEVICE_TOKEN_INVALID [REQ-021].
* Khuyến mãi: code trùng trả 409 PROMO_CODE_DUPLICATED với ràng buộc unique tầng DB làm lớp phòng vệ thứ hai; discountPercent ngoài 1–100 bị chặn; endDate bỏ trống đánh dấu perpetual=true và luôn nằm trong danh sách ưu đãi hiệu lực phía học viên [REQ-017].
* Thông báo công khai: title vượt 150 ký tự hoặc content vượt 2000 ký tự bị chặn ở tầng DTO; announcement quá hạn tự động biến mất khỏi mọi đường đọc công khai nhưng vẫn quản trị được bởi vai trò có quyền; announcement không có endDate luôn hiển thị [REQ-018].
* Chatbot: câu hỏi trong phạm vi trả answer kèm confidence ≥ ngưỡng và escalated=false; câu hỏi ngoài phạm vi trả escalated=true kèm thông điệp chuyển phiên nhân viên hỗ trợ; mọi lượt hội thoại ghi dòng AuditLog với userId, sessionId và timestamp [REQ-019].
* Mobile: navigator render đúng tập màn hình theo từng roleId, chặn route ngoài phạm vi vai trò trước khi render; push deep-link điều hướng đúng màn hình đích ở cả cold-start lẫn background, route không hợp lệ fallback an toàn về trang chủ không crash [REQ-020], [REQ-021].
* Web: thứ tự ưu tiên locale là stored preference → Accept-Language (xử lý q-value) → mặc định 'vi'; chuyển đổi locale không cần reload trang; mỗi page SSR phát sinh html lang khớp locale hiện hành cùng đủ ba link hreflang en/vi/es và x-default [REQ-022], [REQ-023].
* Độ bao phủ kiểm thử tự động ≥ 85% trên cả ba module backend và hai ứng dụng client; latency trung bình dispatch/devices-token/promotions/announcements/chatbot-query ≤ 200 ms trong profile đo hiệu năng đối chiếu [NFR-001].
* Tuân thủ OWASP Top 10: toàn bộ truy vấn đi qua prepared statement tham số hóa; nội dung description/content được làm sạch server-side chống XSS; không leak stack trace hay chi tiết SQL ra phản hồi lỗi; không ghi device token hay bearer token vào log.
* Năm tài liệu ./sources/docs/ hoàn chỉnh, liên kết chéo nhất quán với schema Giai đoạn 1 và hợp đồng API thực tế.
* Zero blocker SonarQube; mọi merge thực hiện qua pull request squash trên nhánh `features/development-phase-4-day-Y` theo quy trình phân nhánh hàng ngày.

## 5. Nhật ký Thực thi Kiến trúc Theo Ngày

### 🌤️ NGÀY 1:
<!--DAY_HEADER_START-->Xây Dựng Trọn Vẹn Notification Service Với Điều Phối Đa Kênh FCM APNs Zalo, Đăng Ký Device Token Và Cơ Chế Retry Tối Đa Ba Lần<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.1: Sinh descriptor module con notification-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module notification-service kế thừa parent membership-hub-backend mà không tái khai báo phiên bản dependency; đăng ký vào danh sách `<modules>` của descriptor cha sau card-service; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator, quarkus-flyway, quarkus-redis-client (lưu registry device token và khóa dedup eventId), quarkus-scheduler (job retry định kỳ), quarkus-smallrye-reactive-messaging-kafka (tiêu thụ course.teacher.events, enrollment.created, notification.dispatch) và firebase-admin 9.x phục vụ gửi FCM HTTP v1; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=notification-service phục vụ đóng gói image ở Giai đoạn 5; cấu hình quarkus.flyway.locations trỏ tới classpath:db/migration của chính module để chuỗi migration V4 chạy trong ngữ cảnh lịch sử Flyway riêng biệt, tránh va chạm phiên bản với chuỗi trung tâm V1–V9 của db-migrations; tinh chỉnh Agroal connection pool chịu tải fan-out đồng thời; bổ sung dependency test scope junit-jupiter, rest-assured, testcontainers-postgresql và testcontainers-kafka làm nền cho suite kiểm thử của Tester.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.2: Migration V4 theo dõi trạng thái giao hàng thông báo và index danh mục dùng chung

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/resources/db/migration/V4__phase4_notification_delivery_tracking.sql

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016], [EXC-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Sinh migration V4 bổ sung hạ tầng theo dõi giao hàng cho bảng notifications: cột delivery_channels VARCHAR(30) DEFAULT 'PUSH' kèm CHECK ràng buộc ba giá trị PUSH/ZALO/PUSH_AND_ZALO, cột last_attempt_at TIMESTAMP và failure_reason VARCHAR(500) phục vụ chẩn đoán thất bại vĩnh viễn [REQ-016]; cột retry_count đã tồn tại từ V1 (SMALLINT NOT NULL DEFAULT 0) nên chỉ bổ sung CHECK biên 0–3 thay vì khai báo lại cột gây lỗi duplicate-column; tạo index idx_notifications_retry_queue (delivered, retry_count, sent_at) phục vụ quét hàng đợi pending của scheduler với hiệu năng sub-second [EXC-003]; đồng thời cấp phát hai index danh mục dùng chung cho Giai đoạn 2 ngày làm việc kế tiếp: idx_promotions_active_lookup (code, start_date, end_date) và idx_announcements_visibility_window (start_date, end_date) chạy trên cùng schema chia sẻ; toàn bộ câu lệnh tuân thủ ANSI SQL, không dùng ENUM inline.

* **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [REQ-016], [EXC-003]:**

<!--START_DDL_MIGRATION-->
```sql
-- =====================================================================
-- Flyway Migration: V4__phase4_notification_delivery_tracking.sql
-- Scope: Phase 4 - notification delivery retry tracking and catalog indexes
-- =====================================================================

ALTER TABLE notifications ADD COLUMN delivery_channels VARCHAR(30) NOT NULL DEFAULT 'PUSH';
-- retry_count column originates from V1__create_roles_and_users_tables.sql
-- (SMALLINT NOT NULL DEFAULT 0); re-declaration intentionally omitted to
-- avoid a duplicate-column migration failure against the shared schema.
ALTER TABLE notifications ADD COLUMN last_attempt_at TIMESTAMP;
ALTER TABLE notifications ADD COLUMN failure_reason VARCHAR(500);

ALTER TABLE notifications ADD CONSTRAINT chk_notifications_delivery_channels
    CHECK (delivery_channels IN ('PUSH', 'ZALO', 'PUSH_AND_ZALO'));

ALTER TABLE notifications ADD CONSTRAINT chk_notifications_retry_bounds
    CHECK (retry_count BETWEEN 0 AND 3);

CREATE INDEX idx_notifications_retry_queue
    ON notifications (delivered, retry_count, sent_at);

CREATE INDEX idx_promotions_active_lookup
    ON promotions (code, start_date, end_date);

CREATE INDEX idx_announcements_visibility_window
    ON announcements (start_date, end_date);
```
<!--END_DDL_MIGRATION-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.3: Pipeline điều phối trung tâm NotificationOrchestrationService tiêu thụ sự kiện nghiệp vụ

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/service/NotificationOrchestrationService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng service điều phối trung tâm nhận yêu cầu dispatch từ ba nguồn: consumer @Incoming cho topic course.teacher.events (payload teacher.assigned.v1), consumer @Incoming cho topic enrollment.created và consumer @Incoming cho topic notification.dispatch [REQ-016]; trong một @Transactional, persist bản ghi Notifications (message, delivery_channels, user_id hoặc group_zalo nullable) TRƯỚC khi fan-out để bảo đảm không mất thông báo kể cả khi broker lỗi; sau commit, điều phối đồng thời qua Uni/CompletionStage tới adapter PUSH và ZALO theo giá trị delivery_channels; chỉ bật delivered=true khi toàn bộ kênh mục tiêu xác nhận thành công, fan-out một phần giữ delivered=false nhường scheduler retry ở NHIỆM VỤ CON 1.8; áp dụng khóa dedup eventId qua Redis SETNX với TTL 24 giờ chặn tiêu thụ kép khi Kafka phát lại ở chế độ at-least-once; tôn trọng partition key courseId bảo đảm thứ tự xử lý trong phạm vi từng khóa học; chuẩn hóa chuỗi tiếng Việt về dạng Unicode NFC trước khi đẩy kênh; ghi audit log mỗi lần dispatch kèm userId và timestamp mà không ghi device token hay bearer token vào log.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-016]:**

<!--START_API_CONTRACT-->
```json
{
  "consumedTopics": [
    { "topic": "course.teacher.events", "eventType": "teacher.assigned.v1", "producer": "course-service" },
    { "topic": "enrollment.created", "producer": "enrollment-service" },
    { "topic": "notification.dispatch", "producer": "internal services" }
  ],
  "deliveryChannels": ["PUSH", "ZALO", "PUSH_AND_ZALO"],
  "fanOutRule": "persist Notifications row BEFORE fan-out; delivered=true only when every targeted channel acknowledges; partial success keeps delivered=false for the retry scheduler",
  "idempotencyKey": "eventId via Redis SETNX TTL 24h",
  "partitionKey": "courseId"
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.4: REST endpoint POST /api/v1/notifications/dispatch

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/api/NotificationDispatchResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Công bố POST /api/v1/notifications/dispatch yêu cầu bearer JWT với @RolesAllowed({"SYSTEM_ADMIN","CENTER_ADMIN","MANAGER"}) phục vụ kịch bản admin tạo announcement hoặc kích hoạt thông báo thủ công [REQ-016]; DTO DispatchRequest ràng buộc Bean Validation: message bắt buộc tối đa 2000 ký tự, channels là tập con của enum PUSH/ZALO, userId nullable chỉ khi groupZalo có mặt иначе trả 400 NOTIF_VALIDATION_FAILED với mảng invalidFields liệt kê từng trường; ủy quyền cho NotificationOrchestrationService thực hiện bước persist rồi trả 202 kèm {notificationId, status:"QUEUED"} mà không chặn đồng bộ quá trình fan-out; áp dụng annotation OpenAPI @Operation/@ApiResponse phục vụ công bố hợp đồng; ghi audit log mỗi lần gọi kèm userId và timestamp.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-016]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "POST /api/v1/notifications/dispatch",
  "auth": "BEARER JWT | role=SYSTEM_ADMIN, CENTER_ADMIN, MANAGER",
  "request": {
    "userId": "uuid (nullable when broadcasting to Zalo group only)",
    "groupZalo": "string (optional target Zalo group id)",
    "message": "string (required, max 2000 chars)",
    "channels": ["PUSH", "ZALO"]
  },
  "response_202": {
    "notificationId": "uuid",
    "status": "QUEUED"
  },
  "error_400": {
    "errorCode": "NOTIF_VALIDATION_FAILED",
    "invalidFields": [
      { "field": "string", "rejectedValue": "string|null", "message": "string" }
    ]
  }
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.5: Adapter đẩy thông báo FCM/APNs

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/channel/FcmApnsPushAdapter.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai interface PushChannelAdapter với hai triển khai nội tuyến: FCM qua Firebase Admin SDK 9.x (HTTP v1 API) cho device token nền tảng ANDROID và APNs Provider API với chữ ký token .p8 cho nền tảng IOS [REQ-016]; đọc device token từ Redis hash device:token:{userId} do DeviceTokenResource duy trì; phân loại phản hồi lỗi: UNREGISTERED/INVALID_ARGUMENT liên quan token bị từ chối vĩnh viễn ném PermanentTokenInvalidException, còn UNAVAILABLE/INTERNAL/DEADLINE_EXCEEDED hoặc timeout ném TransientChannelDeliveryException để scheduler quyết định retry; chuẩn hóa payload gồm alert/title/sound kèm trường tùy chỉnh deepLink route và category cho từng nền tảng; thiết lập timeout 5 giây mỗi lần gọi kèm circuit breaker đơn giản chặn dồn 请求 khi nhà cung cấp suy giảm; không ghi log token thô.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.6: Adapter đăng bài nhóm Zalo

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/channel/ZaloGroupChannelAdapter.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Triển khai ZaloGroupChannelAdapter gọi Zalo Open Platform REST API đăng tin nhắn văn bản lên groupZalo được chỉ định cho thông báo, phân công khóa học và cảnh báo điểm danh [REQ-016]; quản lý access token ứng dụng trong Redis kèm cơ chế làm mới chủ động trước khi hết hạn tránh lỗi xác thực giữa chừng; ánh xạ mã lỗi HTTP của Zalo sang hai nhánh retryable/non-retryable: lỗi xác thực hoặc tham số bất hợp lệ ném PermanentTokenInvalidException, lỗi rate-limit/timeout/5xx ném TransientChannelDeliveryException; cắt gọn nội dung theo giới hạn ký tự của Zalo bảo toàn UTF-8 và dấu tiếng Việt; ghi audit log mỗi lần đăng bài kèm groupZalo và timestamp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.7: REST endpoint đăng ký device token POST /api/v1/devices/token

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/api/DeviceTokenResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-021]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Công bố POST /api/v1/devices/token nhận deviceToken và platform (enum ANDROID|IOS) ngay sau khi người dùng login trên Android/iOS [REQ-021]; suy ra userId nghiêm ngặt từ claim sub của bearer JWT và tuyệt đối không tin tưởng trường userId trong body nhằm chặn leo thang gán token chéo tài khoản theo OWASP A01; validate định dạng token theo nền tảng (độ dài và bảng ký tự heuristic) trả 400 DEVICE_TOKEN_INVALID khi sai; lưu ánh xạ userId–deviceToken vào Redis hash device:token:{userId} với trường theo platform, TTL 7 ngày được làm mới mỗi lần re-register để đồng bộ vòng đời refresh token; hỗ trợ re-register khi token xoay vòng bằng cách ghi đè trường tương ứng; trả 204 body rỗng khi thành công; ghi audit log đăng ký kèm userId, platform và timestamp.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-021]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "POST /api/v1/devices/token",
  "auth": "BEARER JWT (any authenticated role)",
  "request": {
    "userId": "uuid (informational only; authoritative identity resolved from JWT sub claim)",
    "deviceToken": "string (FCM or APNs token)",
    "platform": "ANDROID | IOS"
  },
  "storage": "Redis hash device:token:{userId}, field per platform, TTL 7 days renewed on re-register",
  "response_204": "empty body",
  "error_400": { "code": "DEVICE_TOKEN_INVALID" }
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.8: Lập lịch retry giao hàng tối đa 3 lần với khoảng nghỉ luỹ thừa

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/retry/DeliveryRetryScheduler.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016], [EXC-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng job @Scheduled định kỳ quét các bản ghi delivered=false còn retry_count nhỏ hơn 3 theo thứ tự sent_at tăng dần với LIMIT batch, tận dụng index idx_notifications_retry_queue [EXC-003]; trước khi thử lại, thực hiện UPDATE điều kiện kiểu tranh chấp: SET retry_count = retry_count + 1, last_attempt_at = now(), delivery_status = 'RETRYING' WHERE notification_id = ? AND delivered = false AND retry_count = <giá_trị_đã_quét> — số dòng ảnh hưởng bằng 1 nghĩa là pod thắng quyền xử lý, bảo đảm an toàn khi nhiều pod chạy song song không phát sinh dispatch kép [REQ-016]; tính khoảng nghỉ luỹ thừa theo retry_count (ví dụ 30 giây, 2 phút, 8 phút) đối chiếu last_attempt_at trước khi gọi lại adapter kênh thất bại; sau lần thử thứ ba vẫn thất bại thì đánh dấu delivery_status='FAILED' vĩnh viễn kèm failure_reason và loại khỏi vòng quét; lỗi permanent (token invalid) được loại ngay lập tức không tiêu tốn lượt retry; ghi audit log mỗi lần thử lại kèm notificationId và timestamp.

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "NotificationDeliveryExceptionMapper",
  "package": "org.nlh4j.membership_hub.notification.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.notification.exception.NotificationValidationException",
      "httpStatus": 400,
      "errorCode": "NOTIF_VALIDATION_FAILED",
      "bodySchema": {
        "errorCode": "NOTIF_VALIDATION_FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "Aggregate Bean Validation violations (message length cap 2000, channels enum subset, userId/groupZalo mutual exclusivity) into invalidFields; never expose internal channel errors"
    },
    {
      "handles": "org.nlh4j.membership_hub.notification.exception.TransientChannelDeliveryException",
      "httpStatus": null,
      "errorCode": "NOTIF_CHANNEL_TRANSIENT",
      "internalBehavior": "increment retry_count by one, schedule exponential backoff retry, keep delivery_status RETRYING while retry_count < 3",
      "rule": "Internal domain signal consumed by DeliveryRetryScheduler; never propagated as HTTP 5xx to clients"
    },
    {
      "handles": "org.nlh4j.membership_hub.notification.exception.PermanentTokenInvalidException",
      "httpStatus": null,
      "errorCode": "NOTIF_TOKEN_PERMANENT_INVALID",
      "internalBehavior": "no retry, record failure_reason, mark delivered=false terminally, prune stale device token from Redis registry, write warning audit entry",
      "rule": "Terminal classification for rejected device tokens and Zalo authentication failures"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.9: Hierarchy ngoại lệ giao hàng và mapper chuẩn hóa

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/exception/NotificationDeliveryException.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[EXC-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng hierarchy ngoại lệ bao gói lỗi FCM/APNs/Zalo kèm mã lỗi máy đọc: lớp cơ sở abstract NotificationDeliveryException mang trường errorCode, hai lớp con TransientChannelDeliveryException (NOTIF_CHANNEL_TRANSIENT) và PermanentTokenInvalidException (NOTIF_TOKEN_PERMANENT_INVALID) cùng NotificationValidationException tổng hợp vi phạm đầu vào [EXC-003]; triển khai @Provider ExceptionMapper<NotificationValidationException> trả error envelope thống nhất dạng ProblemDetail RFC 7807 với mảng invalidFields cho resource layer; hai nhánh transient/permanent là tín hiệu miền nội bộ để scheduler quyết định đường đi xử lý và không bao giờ được surface dưới dạng HTTP 5xx ra client; bảo đảm mapper không lộ stack trace hay chi tiết kết nối nhà cung cấp.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.10: Unit test scheduler retry giao hàng

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/retry/DeliveryRetryScheduler.java;./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/retry/DeliveryRetrySchedulerTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016], [EXC-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest với adapter FCM/Zalo được mock: kịch bản A lỗi transient ở lần 1 rồi thành công ở lần 2 xác nhận delivered=true, retry_count=2 và không phát sinh bản ghi trùng [REQ-016]; kịch bản B ba lần thử liên tiếp thất bại xác nhận đúng 3 lần tối đa rồi delivery_status='FAILED' vĩnh viễn kèm failure_reason và scheduler không còn quét lại [EXC-003]; kịch bản C lỗi permanent token invalid đánh dấu FAILED ngay với zero lượt retry; kịch bản D khoảng nghỉ luỹ thừa được tôn trọng — scheduler không gọi adapter trước mốc eligible kế tiếp; kịch bản E mô phỏng hai pod tranh chấp cùng dòng xác nhận chỉ một UPDATE điều kiện thắng quyền xử lý.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.11: Integration test điều phối đa kênh đầu-cuối

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/notification-service/src/test/java/org/nlh4j/membership_hub/notification/channel/MultiChannelDispatchIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khởi chạy @QuarkusIntegrationTest với PostgreSQL Testcontainers, Kafka Testcontainers và hai máy chủ WireMock mô phỏng FCM/APNs cùng Zalo API; chạy luồng end-to-end: phát sự kiện enrollment.created lên broker → xác nhận bản ghi Notifications được persist trước khi fan-out → cả hai kênh mock nhận request → delivered=true cùng dòng audit log được ghi đầy đủ [REQ-016]; kịch bản Zalo lỗi 5xx xác nhận delivered=false giữ trạng thái QUEUED/RETRYING cho vòng retry kế tiếp; phát lại cùng eventId xác nhận khóa dedup Redis chặn gửi kép được WireMock verification counting xác nhận; đo latency trung bình toàn trình giữ dưới 200 ms đối chiếu [NFR-001].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.12: Rà soát tính idempotent và an toàn luồng của orchestrator

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/notification-service/src/main/java/org/nlh4j/membership_hub/notification/service/NotificationOrchestrationService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016], [EXC-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Rà soát nguy cơ dispatch kép khi retry chồng chất, xác nhận transaction boundary persist-trước-fan-out không tồn tại trạng thái nửa vời và không sử dụng phân tán 2PC [REQ-016]; phát hiện và đề xuất fix race condition giữa scheduler và orchestrator trên cùng dòng notifications (kiểm tra cổng delivery_status và delivered ngăn hai luồng ghi đè); đối chiếu TTL khóa dedup Redis 24 giờ với retention offset Kafka bảo đảm cửa sổ che phủ at-least-once; kiểm tra chuẩn hóa encoding tiếng Việt Unicode NFC trong nội dung message trước khi đẩy kênh; đối chiếu OWASP A01: xác minh DeviceTokenResource suy userId từ claim sub chứ không tin body; xác minh log scrubbing không ghi device token, access token Zalo hay bearer token; lập danh sách remediation ưu tiên kèm diff cụ thể và chốt điều kiện mở khóa Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 1.13: Biên soạn đặc tả API notification-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-notification-service-spec.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-016], [EXC-003]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn khung tài liệu tham chiếu OpenAPI 3.0.3 cho POST /api/v1/notifications/dispatch và POST /api/v1/devices/token kèm schema request/response, ví dụ payload và lệnh curl [REQ-016]; mô tả chính sách retry tối đa 3 lần với bảng khoảng nghỉ luỹ thừa và ý nghĩa vòng đời trạng thái QUEUED → SENT/RETRYING → DELIVERED | FAILED [EXC-003]; liệt kê bảng mã lỗi NOTIF_VALIDATION_FAILED, NOTIF_CHANNEL_TRANSIENT, NOTIF_TOKEN_PERMANENT_INVALID, DEVICE_TOKEN_INVALID kèm điều kiện kích hoạt và hành vi hệ thống; bổ sung sơ đồ Mermaid tuần tự sự kiện nghiệp vụ → persist → fan-out đa kênh → retry branch; neo mọi mục vào thẻ truy vết tương ứng và chuẩn bị cấu trúc liên kết chéo cho chương promotion/chatbot sẽ bổ sung ở Ngày 2.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 2:
<!--DAY_HEADER_START-->Triển Khai CRUD Khuyến Mãi Quy Tắc Vĩnh Viễn, Thông Báo Công Kai Tự Ẩn Hết Hạn Và Tích Hợp Chatbot AI Chăm Sóc Khách Hàng<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.1: Sinh descriptor module con promotion-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/promotion-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module promotion-service kế thừa parent membership-hub-backend; đăng ký vào danh sách `<modules>` của descriptor cha sau notification-service; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache, quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator và quarkus-flyway; gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=promotion-service phục vụ đóng gói image ở Giai đoạn 5; cấu hình quarkus.flyway.locations trỏ classpath:db/migration của chính module với ngữ cảnh lịch sử Flyway riêng biệt; ghi chú rõ hai index danh mục idx_promotions_active_lookup và idx_announcements_visibility_window đã được cấp phát tập trung trong migration V4 của notification-service chạy trên cùng schema chia sẻ nên module này không phát sinh DDL bổ sung; bổ sung dependency test scope junit-jupiter, rest-assured và testcontainers-postgresql làm nền cho suite kiểm thử của Tester.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.2: REST CRUD khuyến mãi /api/v1/promotions

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/api/PromotionResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Công bố GET/POST/PUT/DELETE /api/v1/promotions: thao tác ghi giới hạn @RolesAllowed({"CENTER_ADMIN","MANAGER"}) theo ma trận RBAC (Manager được quản lý khuyến mãi dù bị chặn sửa khóa học), thao tác đọc mở cho mọi vai trò đã xác thực [REQ-017]; DTO PromotionRequest ràng buộc code @NotBlank @Size(max=50), discountPercent @Min(1) @Max(100), startDate/endDate tùy chọn, description tùy chọn; trả 409 PROMO_CODE_DUPLICATED khi code trùng và 404 PROMO_NOT_FOUND khi promoId thiếu; response bao gồm trường perpetual suy ra từ endDate == null; tham số sắp xếp đi qua whitelist cứng (code, discountPercent, startDate — ASC/DESC) chặn giá trị ngoài whitelist bằng 400 chống SQL injection; vai trò STUDENT đọc tự động lọc cửa sổ hiệu lực hiện hành; áp dụng annotation OpenAPI; ghi audit log mọi thao tác ghi kèm userId và timestamp.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-017]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    "GET /api/v1/promotions",
    "POST /api/v1/promotions",
    "PUT /api/v1/promotions/{promoId}",
    "DELETE /api/v1/promotions/{promoId}"
  ],
  "authWrite": "BEARER JWT | role=CENTER_ADMIN, MANAGER",
  "authRead": "BEARER JWT | any authenticated role (STUDENT auto-filtered to active window)",
  "create_request": {
    "code": "string (unique discount code, max 50)",
    "discountPercent": 10,
    "startDate": "2025-01-01 (optional)",
    "endDate": "2025-06-30 (optional, null means perpetual)",
    "description": "string (optional)"
  },
  "response_201": { "promoId": "uuid", "code": "TET2025", "discountPercent": 10, "perpetual": false },
  "error_409": { "code": "PROMO_CODE_DUPLICATED" },
  "error_404": { "code": "PROMO_NOT_FOUND" }
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.3: Logic nghiệp vụ khuyến mãi và truy vấn ưu đãi hiệu lực

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/service/PromotionService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng tầng service quản lý vòng đời promotion trong @Transactional: ràng buộc code unique ở cả mức ứng dụng (pre-check) và mức DB qua uq_promotions_code bắt ConstraintViolationException ánh xạ 409 làm lớp phòng vệ thứ hai chống race condition check-then-insert [REQ-017]; cung cấp truy vấn danh sách ưu đãi đang hiệu lực với vị từ ((start_date IS NULL OR start_date <= CURRENT_DATE) AND (end_date IS NULL OR end_date >= CURRENT_DATE)) tận dụng idx_promotions_active_lookup bảo đảm phản hồi sub-second; quy tắc vĩnh viễn: endDate bỏ trống bỏ qua ràng buộc biên kết thúc và luôn nằm trong kết quả; bổ sung thực thể Panache Promotion ánh xạ bảng promotions với tên cột snake_case khớp schema vật lý cùng PromotionRepository dùng prepared statement tham số hóa; mọi phép so sánh ngày thống nhất múi giờ UTC.

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-017]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "PromotionExceptionMapper",
  "package": "org.nlh4j.membership_hub.promotion.exception",
  "providers": [
    {
      "handles": "org.nlh4j.membership_hub.promotion.exception.PromoCodeDuplicatedException",
      "httpStatus": 409,
      "errorCode": "PROMO_CODE_DUPLICATED",
      "bodySchema": { "errorCode": "PROMO_CODE_DUPLICATED", "message": "Promotion code already exists", "code": "string" },
      "rule": "Application-level pre-check combined with uq_promotions_code unique constraint as second defensive layer against check-then-insert races"
    },
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 400,
      "errorCode": "PROMO_VALIDATION_FAILED",
      "bodySchema": {
        "errorCode": "PROMO_VALIDATION_FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "discountPercent must be between 1 and 100; code required max 50 chars; aggregate violations preserving DTO declaration order"
    },
    {
      "handles": "org.nlh4j.membership_hub.promotion.exception.PromoNotFoundException",
      "httpStatus": 404,
      "errorCode": "PROMO_NOT_FOUND",
      "bodySchema": { "errorCode": "PROMO_NOT_FOUND", "message": "Promotion does not exist" },
      "rule": "Validate existence before mutation; no partial updates"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.4: Sinh descriptor module con chatbot-service kế thừa parent Quarkus

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/chatbot-service/pom.xml

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[ARC-000]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khai báo module chatbot-service kế thừa parent membership-hub-backend; đăng ký vào danh sách `<modules>` của descriptor cha sau promotion-service; khai báo dependency quarkus-rest, quarkus-hibernate-orm-panache (truy vấn chỉ đọc mô hình Courses/Users/Centers), quarkus-jdbc-postgresql, quarkus-smallrye-jwt, quarkus-hibernate-validator và quarkus-redis-client (đếm rate limit theo user và ngữ cảnh phiên hội thoại); gắn quarkus-maven-plugin cho vòng đời dev/build/package; định nghĩa thuộc tính quarkus.container-image.name=chatbot-service phục vụ đóng gói image ở Giai đoạn 5; module không phát sinh migration riêng vì chỉ đọc dữ liệu hiện hữu và ghi AuditLog; bổ sung dependency test scope junit-jupiter, rest-assured và testcontainers-postgresql làm nền cho suite kiểm thử escalate của Tester.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.5: REST CRUD thông báo công khai /api/v1/announcements

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/api/AnnouncementResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Công bố GET/POST/PUT/DELETE /api/v1/announcements: thao tác ghi giới hạn @RolesAllowed({"CENTER_ADMIN","MANAGER"}), đọc mở cho mọi vai trò đã xác thực [REQ-018]; DTO AnnouncementRequest ràng buộc title @NotBlank @Size(max=150), content @NotBlank @Size(max=2000), startDate/endDate tùy chọn với CHECK endDate không sớm hơn startDate; hỗ trợ expiry tùy chọn; phát sóng toàn site cho mọi người dùng và tự động ẩn sau ngày hết hạn đã cấu hình nhờ AnnouncementExpiryFilter áp dụng trên mọi đường đọc; làm sạch đầu vào rich-text server-side bằng OWASP Java HTML Sanitizer với whitelist thẻ nghiêm ngặt trước khi persist chống XSS; trả 404 ANNOUNCEMENT_NOT_FOUND khi thiếu bản ghi; áp dụng annotation OpenAPI; ghi audit log mỗi thao tác ghi kèm userId và timestamp.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-018]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoints": [
    "GET /api/v1/announcements",
    "POST /api/v1/announcements",
    "PUT /api/v1/announcements/{announcementId}",
    "DELETE /api/v1/announcements/{announcementId}"
  ],
  "authWrite": "BEARER JWT | role=CENTER_ADMIN, MANAGER",
  "authRead": "BEARER JWT | any authenticated role",
  "create_request": {
    "title": "string (max 150 chars)",
    "content": "string (max 2000 chars)",
    "startDate": "2025-02-01 (optional)",
    "endDate": "2025-03-01 (optional expiry, auto-hidden after this date)"
  },
  "list_item": { "announcementId": "uuid", "title": "Scheduled maintenance", "endDate": "2025-03-01" },
  "visibilityRule": "expired announcements excluded from all public reads via visibility window filter; retained for privileged management"
}
```
<!--END_API_CONTRACT-->

* **Trình Xử lý Ngoại lệ Cục bộ của Giai đoạn [REQ-018]:**

<!--START_EXC_HANDLER-->
```json
{
  "mapperClass": "AnnouncementExceptionMapper",
  "package": "org.nlh4j.membership_hub.promotion.exception",
  "providers": [
    {
      "handles": "jakarta.validation.ConstraintViolationException",
      "httpStatus": 400,
      "errorCode": "ANNOUNCEMENT_VALIDATION_FAILED",
      "bodySchema": {
        "errorCode": "ANNOUNCEMENT_VALIDATION_FAILED",
        "invalidFields": [
          { "field": "string", "rejectedValue": "string|null", "message": "string" }
        ]
      },
      "rule": "title required max 150 chars; content required max 2000 chars; endDate must not precede startDate; violations aggregated into invalidFields"
    },
    {
      "handles": "org.nlh4j.membership_hub.promotion.exception.AnnouncementNotFoundException",
      "httpStatus": 404,
      "errorCode": "ANNOUNCEMENT_NOT_FOUND",
      "bodySchema": { "errorCode": "ANNOUNCEMENT_NOT_FOUND", "message": "Announcement does not exist" },
      "rule": "Validate existence before mutation; expired announcements remain manageable by privileged roles but hidden from public reads"
    }
  ]
}
```
<!--END_EXC_HANDLER-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.6: Bộ lọc tự ẩn announcement sau ngày hết hạn

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/service/AnnouncementExpiryFilter.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng component thuần chức năng sinh vị từ truy vấn cửa sổ hiệu lực: (start_date IS NULL OR start_date <= CURRENT_DATE) AND (end_date IS NULL OR end_date >= CURRENT_DATE) áp dụng nhất quán trên mọi đường đọc danh sách và chi tiết để announcement tự động biến mất sau ngày hết hạn mà không cần cron xóa dữ liệu [REQ-018]; announcement không có endDate luôn thỏa vị từ và hiển thị vĩnh viễn; tận dụng idx_announcements_visibility_window cho truy vấn cửa sổ; cung cấp API tách biệt giữa chế độ đọc công khai (áp filter) và chế độ quản trị của vai trò có quyền (bỏ filter) phục vụ kiểm tra nội dung quá hạn; thiết kế dạng hàm tinh khiết dễ unit test và tái sử dụng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.7: REST endpoint truy vấn chatbot POST /api/v1/chatbot/query

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/chatbot-service/src/main/java/org/nlh4j/membership_hub/chatbot/api/ChatbotResource.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Công bố POST /api/v1/chatbot/query yêu cầu bearer JWT cho mọi vai trò đã xác thực, nhận {sessionId UUID, message chuỗi tối đa 500 ký tự} [REQ-019]; ủy quyền ChatbotEngineService giải đáp rồi trả 200 kèm {answer, confidence, escalated}; áp dụng rate limit đơn giản qua Redis 30 request/phút/user trả 429 CHATBOT_RATE_LIMITED khi vượt; ghi toàn bộ hội thoại vào AuditLog với action=CHATBOT_QUERY, userId, sessionId, hash nội dung message (không lưu raw để hạn chế PII) và timestamp phục vụ truy vết; áp dụng annotation OpenAPI; validate đầu vào trả 400 CHATBOT_VALIDATION_FAILED với mảng invalidFields khi thiếu trường.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-019]:**

<!--START_API_CONTRACT-->
```json
{
  "endpoint": "POST /api/v1/chatbot/query",
  "auth": "BEARER JWT (any authenticated role)",
  "request": {
    "sessionId": "uuid",
    "message": "When does the Japanese course start?"
  },
  "response_200_high_confidence": {
    "answer": "The Japanese course starts on 2025-03-15 at District 1 center",
    "confidence": 0.92,
    "escalated": false
  },
  "response_200_low_confidence": {
    "answer": "Your question has been forwarded to human support",
    "confidence": 0.31,
    "escalated": true
  },
  "rateLimit": "30 requests/minute/user via Redis counter",
  "error_429": { "code": "CHATBOT_RATE_LIMITED" }
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.8: Engine chatbot đối chiếu intent và lộ trình escalate

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/chatbot-service/src/main/java/org/nlh4j/membership_hub/chatbot/service/ChatbotEngineService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng engine đối chiếu intent với bốn miền dữ liệu whitelist: khóa học (title, lịch start/end, sức chứa qua truy vấn tham số hóa trên courses), giáo viên (join users trên teacher_id), trung tâm (name/address/contact trên centers) và trạng thái tài khoản (thẻ hội viên, ghi danh của chính caller suy từ claim sub JWT) [REQ-019]; tính điểm confidence từ cường độ khớp intent cộng số lượng thực thể phân giải thành công; ngưỡng escalate đọc từ system_settings key chatbot.confidence.threshold mặc định 0.60; khi confidence xuống dưới ngưỡng, đặt escalated=true, điều phối thông báo chuyển phiên tới hàng đợi nhân viên hỗ trợ (CENTER_ADMIN/MANAGER của trung tâm liên quan hoặc SYSTEM_ADMIN dự phòng) qua NotificationOrchestrationService và trả thông điệp đã chuyển tiếp cho người dùng; mọi lượt hội thoại đều ghi AuditLog; nghiêm cấm nối chuỗi đầu vào người dùng vào câu lệnh SQL/JPQL.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.9: Unit test nghiệp vụ khuyến mãi

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/promotion-service/src/main/java/org/nlh4j/membership_hub/promotion/service/PromotionService.java;./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/service/PromotionServiceTest.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết @QuarkusTest bao phủ [REQ-017]: tạo promotion code trùng sinh PromoCodeDuplicatedException kỳ vọng 409; biên discountPercent giá trị 1 và 100 được chấp nhận, 0 và 101 bị từ chối với đúng số violation; hành vi khuyến mãi vĩnh viễn khi endDate null được đánh dấu perpetual=true và xuất hiện trong danh sách hiệu lực bất kể ngày hiện hành; bộ lọc ưu đãi hiệu lực trả đúng tập kết quả với ngày biên start_date=end_date=CURRENT_DATE vẫn hiển thị; cập nhật code sang giá trị đã tồn tại bị chặn; caller STUDENT/TEACHER gọi thao tác ghi bị chặn 403.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.10: Integration test tự ẩn announcement hết hạn

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/promotion-service/src/test/java/org/nlh4j/membership_hub/promotion/api/AnnouncementExpiryIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khởi chạy @QuarkusIntegrationTest với PostgreSQL Testcontainers; seed bốn nhóm dữ liệu: announcement quá hạn (end_date < hôm nay), còn hạn, tương lai (start_date > hôm nay) và không có endDate; gọi GET /api/v1/announcements với vai trò STUDENT xác nhận bản ghi quá hạn và tương lai không xuất hiện trong phản hồi còn bản ghi không endDate luôn hiển thị [REQ-018]; gọi với vai trò CENTER_ADMIN xác nhận chế độ quản trị nhìn thấy toàn bộ kể cả quá hạn; kiểm tra biên end_date trùng đúng CURRENT_DATE vẫn hiển thị; xác minh thao tác ghi từ vai trò không có quyền trả 403 và title/content vượt giới hạn trả 400 với danh sách trường lỗi.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.11: Integration test escalate chatbot

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/backend/chatbot-service/src/test/java/org/nlh4j/membership_hub/chatbot/service/ChatbotEscalationIT.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Khởi chạy @QuarkusIntegrationTest với PostgreSQL Testcontainers; seed khóa học mẫu "Tiếng Nhật N5" với ngày bắt đầu biết trước; gửi câu hỏi trong phạm vi xác nhận phản hồi chứa đáp án đúng, confidence ≥ ngưỡng và escalated=false [REQ-019]; gửi câu hỏi ngoài phạm vi/gibberish xác nhận escalated=true kèm thông điệp chuyển phiên nhân viên hỗ trợ và thông báo escalate được điều phối vào hàng đợi notification; xác minh AuditLog ghi đủ dòng cho cả hai lượt hội thoại với cùng sessionId liên kết; burst vượt 30 request/phút xác nhận 429 CHATBOT_RATE_LIMITED.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.12: Rà soát biên validate, chống XSS và hiệu năng truy vấn danh mục

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/backend/promotion-service/src/main/java/com/../nlh4j_placeholder_removed/PromotionService.java

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Kiểm tra chặt chẽ giới hạn title 150 ký tự và content 2000 ký tự được thực thi server-side chứ không chỉ client-side, cùng chuẩn hóa đầu vào chống XSS bằng OWASP Java HTML Sanitizer trước khi persist vì nội dung được render trên web-app và mobile-app [REQ-018]; xác minh race condition check-then-insert trên promo code được che phủ bởi ràng buộc unique uq_promotions_code ở tầng DB [REQ-017]; phân tích kế hoạch truy vấn EXPLAIN cho vị từ cửa sổ hiệu lực bảo đảm sử dụng idx_promotions_active_lookup và idx_announcements_visibility_window, đề xuất bổ sung index nếu phát hiện full-table scan; chuẩn hóa mọi nhánh lỗi trả ProblemDetail RFC 7807 không leak stack trace hay chi tiết SQL; lập danh sách remediation kèm diff cụ thể và chốt điều kiện mở khóa Ngày 3.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.13: Biên soạn đặc tả API promotion-service

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/api-promotion-service-spec.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn tài liệu tham chiếu CRUD promotions và announcements kèm ví dụ payload request/response, lệnh curl và ma trận quyền từng endpoint [REQ-017], [REQ-018]; diễn giải quy tắc khuyến mãi vĩnh viễn khi endDate bỏ trống với trường perpetual trong phản hồi; mô tả cơ chế tự ẩn announcement sau ngày hết hạn qua bộ lọc cửa sổ hiệu lực và sự khác biệt giữa chế độ đọc công khai với chế độ quản trị; liệt kê bảng mã lỗi PROMO_CODE_DUPLICATED, PROMO_VALIDATION_FAILED, PROMO_NOT_FOUND, ANNOUNCEMENT_VALIDATION_FAILED, ANNOUNCEMENT_NOT_FOUND kèm điều kiện kích hoạt; neo mọi mục vào thẻ truy vết tương ứng và liên kết chéo với từ điển dữ liệu bảng PROMOTIONS/ANNOUNCEMENTS từ Giai đoạn 1.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 2.14: Biên soạn hướng dẫn tích hợp chatbot

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/chatbot-integration-guide.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Mô tả hợp đồng POST /api/v1/chatbot/query với schema request/response cho hai nhánh confidence cao/thấp [REQ-019]; tài liệu hóa cơ chế cấu hình ngưỡng confidence qua system_settings key chatbot.confidence.threshold và quy trình thay đổi ngưỡng an toàn; vẽ sơ đồ Mermaid tuần tự luồng escalate: truy vấn → chấm điểm → dưới ngưỡng → điều phối thông báo chuyển phiên → phản hồi escalated=true; diễn giải ngữ nghĩa ghi AuditLog cho từng lượt hội thoại gồm userId, sessionId, hash message và timestamp; bổ sung bảng giới hạn rate limit 30 request/phút/user và mã lỗi 429 CHATBOT_RATE_LIMITED.

<!--END_ATOMIC_SUB_TASK_NODE-->

### 🌤️ NGÀY 3:
<!--DAY_HEADER_START-->Hoàn Thiện Giao Diện Di Động Theo Vai Trò, Push Notification Deep Link, Phát Hiện Ngôn Ngữ Ưu Tiên Và SEO Đa Ngôn Ngữ En Vi Es<!--DAY_HEADER_END-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.1: Điều hướng đa vai trò React Native RoleBasedNavigator

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/mobile-app/src/navigation/RoleBasedNavigator.tsx

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-020]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng navigator động trên react-navigation 6.x đọc roleId ngay sau đăng nhập từ Zustand auth slice (hydrate từ @capacitor/preferences) và render bộ stack tương ứng: Student nhận tab Duyệt khóa/Thẻ hội viên/Quét QR/Thông báo, Teacher nhận stack Lịch dạy chỉ đọc/Khóa học/Thông báo, nhóm Admin (SYSTEM_ADMIN/CENTER_ADMIN/MANAGER) nhận stack Trung tâm/Khóa học/Ghi danh/Thông báo/Thông cáo [REQ-020]; chặn truy cập màn hình ngoài phạm vi vai trò ngay tại tầng điều hướng trước khi render bằng navigation guard redirect về trang chủ vai trò; tích hợp cấu hình linking prefix phục vụ deep-link từ push; bảo đảm bố cục responsive nhất quán trên Android và iOS với SafeAreaProvider.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.2: Màn hình dashboard phản chiếu chức năng web theo vai trò

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/mobile-app/src/screens/RoleDashboardScreen.tsx

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-020]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Hiện thực màn hình chủ phân nhánh theo vai trò phản chiếu đầy đủ chức năng web: Student thấy widget thẻ hội viên gọi GET /api/v1/cards/me hiển thị daysRemaining đếm ngược kèm CTA gia hạn và lối tắt duyệt khóa học; Teacher thấy danh sách buổi dạy hôm nay ở chế độ chỉ đọc từ API khóa học; Admin thấy lối tắt điều hành trung tâm và thông cáo mới [REQ-020]; lấy dữ liệu qua TanStack Query hooks với staleTime hợp lý, axios instance gắn bearer token tự động từ interceptor đọc @capacitor/preferences; bố cục flex/useWindowDimension thích ứng kích thước màn hình; nhãn accessibility bản địa hóa qua bộ i18n dùng chung.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.3: Dịch vụ đăng ký push và nhận thông báo foreground/background

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/mobile-app/src/services/PushNotificationService.ts

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-021]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng dịch vụ xin quyền notification ở lần đăng nhập đầu, lấy device token qua @react-native-firebase/messaging cho Android (FCM) và cầu nối APNs cho iOS, rồi gọi POST /api/v1/devices/token với platform tương ứng ngay sau login [REQ-021]; đăng ký listener onTokenRefresh để re-register tự động khi token xoay vòng; lắng nghe push ở chế độ foreground hiển thị banner in-app và tăng badge, chế độ background/quit qua background handler phân loại category ATTENDANCE_CONFIRMED/ANNOUNCEMENT_NEW/REMINDER; lưu payload cuối cùng vào bộ nhớ tạm cho DeepLinkHandler tiêu thụ; xử lý an toàn kịch bản từ chối quyền với fallback graceful không crash.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.4: Xử lý deep-link từ payload push

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/mobile-app/src/services/DeepLinkHandler.ts

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-021]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Phân giải route đính kèm payload push hỗ trợ cả scheme membershiphub:// và https universal link, ánh xạ bảng route: /courses/{id} → CourseDetail, /cards → MembershipCard, /attendance/{id} → AttendanceResult, /announcements/{id} → AnnouncementDetail [REQ-021]; validate routeAgainst whitelist theo vai trò hiện hành chặn deep-link injection, route không hợp lệ hoặc ngoài phạm vi vai trò fallback an toàn về trang chủ vai trò kèm telemetry log; xử lý cold-start bằng cách capture initial notification trước khi navigator sẵn sàng và xếp hàng đến khi navigationRef mount; xử lý chuyển tiếp từ background điều hướng trực tiếp qua navigationRef; tuyệt đối không eval chuỗi route thô.

* **Hợp đồng Định tuyến API và Sự kiện [REQ-021]:**

<!--START_API_CONTRACT-->
```json
{
  "pushPayloadSchema": {
    "title": "string",
    "body": "string",
    "category": "ATTENDANCE_CONFIRMED | ANNOUNCEMENT_NEW | REMINDER",
    "deepLink": "membershiphub://courses/{courseId} | https://app.membership-hub.vn/vi/courses/{courseId}"
  },
  "deepLinkRouteTable": {
    "/courses/{courseId}": "CourseDetailScreen",
    "/cards": "MembershipCardScreen",
    "/attendance/{attendanceId}": "AttendanceResultScreen",
    "/announcements/{announcementId}": "AnnouncementDetailScreen"
  },
  "fallbackRule": "unknown or role-forbidden route resolves to role home screen without crash"
}
```
<!--END_API_CONTRACT-->

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.5: Middleware phát hiện ngôn ngữ ưu tiên Next.js

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/web-app/src/middleware/localeDetection.ts

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-022]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng Next.js middleware chạy tại edge với matcher loại trừ _next/static và tài nguyên tĩnh: đọc preference ngôn ngữ đã lưu từ cookie NEXT_LOCALE (được đồng bộ từ @capacitor/preferences trên hybrid), fallback phân giải Accept-Language header với sắp xếp q-value giao với tập locale kích hoạt ['en','vi','es'], mặc định cuối cùng là 'vi' [REQ-022]; rewrite route sang tiền tố /{locale}{pathname} tương ứng và set cookie detection để duy trì lựa chọn; phối hợp next-intl bảo đảm chuyển đổi locale không cần reload trang ở mức khả thi; middleware phải thuần chức năng, không tác dụng phụ ngoài rewrite/cookie.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.6: Quản lý hreflang và thẻ lang SSR

##### Sub-Agent được phân công: Coder

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/web-app/src/components/seo/HreflangHeadManager.tsx

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-023]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Xây dựng server component gắn vào root layout phát sinh trên từng page: thuộc tính html lang khớp locale hiện hành, bộ ba link rel='alternate' hrefLang cho en/vi/es trỏ tới URL tuyệt đối của cùng pathname theo từng locale cùng link x-default trỏ về locale mặc định được phát hiện [REQ-023]; sinh language-specific meta title và description từ bộ từ điển i18n tương ứng, kèm openGraph.locale và canonical URL phục vụ crawler lập chỉ mục; bảo đảm render xảy ra ở SSR (không phụ thuộc effect client-side) để HTML source chứa đầy đủ thẻ khi crawler fetch; component nhận props pathname/locale thuần túy dễ test.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.7: Unit test điều hướng vai trò

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/mobile-app/src/navigation/RoleBasedNavigator.tsx;./sources/frontend/mobile-app/__tests__/RoleBasedNavigator.test.tsx

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-020]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết React Testing Library suite render navigator với từng roleId mock và xác nhận tập màn hình đúng phạm vi vai trò: Student nhận đúng bốn tab nghiệp vụ tự phục vụ, Teacher nhận stack chỉ đọc không chứa hành động ghi, Admin nhận đầy đủ stack điều hành [REQ-020]; khẳng định Student điều hướng sâu tới route /admin/centers bị guard chặn và redirect về trang chủ Student; xác minh hydrate roleId từ Zustand store và fallback về màn hình đăng nhập khi chưa xác thực; snapshot ổn định giữa các lần render.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.8: E2E test push deep-link cold-start và background

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** INTEGRATION_SCOPE;./sources/frontend/mobile-app/__tests__/PushDeepLink.e2e.ts

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-021]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Dựng E2E profile mô phỏng push chứa deep-link ở cả hai trạng thái: cold-start với initial notification chứa /courses/{id} xác nhận ứng dụng sau khi mount điều hướng tới đúng CourseDetailScreen, và background tap xác nhận điều hướng trực tiếp qua navigationRef [REQ-021]; kịch bản deep-link không hợp lệ hoặc ngoài whitelist vai trò xác nhận fallback về trang chủ không crash; kịch bản chưa đăng nhập nhận deep-link xác nhận chuyển hướng login rồi resume route đích sau xác thực; đo thời gian từ tap notification đến màn hình đích ghi nhận baseline hiệu năng.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.9: Unit test thứ tự ưu tiên ngôn ngữ

##### Sub-Agent được phân công: Tester

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/web-app/src/middleware/localeDetection.ts;./sources/frontend/web-app/__tests__/localeDetection.test.ts

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-022]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Viết Vitest/Jest suite kiểm tra thứ tự ưu tiên: cookie NEXT_LOCALE có mặt thì thắng mọi header; không có cookie thì phân giải Accept-Language với q-value ('es;q=0.9,en;q=0.8' chọn es); locale không hỗ trợ (ví dụ 'fr') bị bỏ qua rơi xuống ứng viên kế tiếp; không khớp gì thì mặc định 'vi'; xác minh rewrite path đúng dạng /{locale}{pathname} và cookie được set; xác minh việc nạp đúng bundle en/vi/es với khóa dịch tương ứng tồn tại [REQ-022].

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.10: Rà soát bảo mật deep-link và trải nghiệm ngoại tuyến

##### Sub-Agent được phân công: Reviewer

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/frontend/mobile-app/src/services/DeepLinkHandler.ts

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Rà soát nguy cơ deep-link injection và xác thực route whitelist được thực thi kép ở cả client handler lẫn navigation guard theo vai trò [REQ-021]; kiểm tra cấu hình universal links (assetlinks.json/applinks) được tham chiếu đúng trong tài liệu; đánh giá khả năng đáp ứng UI khi mất kết nối mạng cho dashboard và màn hình thẻ, đề xuất bổ sung caching ngoại tuyến stale-while-revalidate cho màn hình còn thiếu [REQ-020]; xác minh refresh token, ngôn ngữ ưu tiên và device token lưu qua @capacitor/preferences thay vì localStorage của WebView; đối chiếu interceptor nút back vật lý Android đồng bộ hành vi pop của navigator; lập danh sách remediation kèm diff cụ thể.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.11: Biên soạn hướng dẫn bản địa hóa và SEO

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/localization-seo-guide.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-022], [REQ-023]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Biên soạn hướng dẫn vận hành ba ngôn ngữ en/vi/es gồm quy trình externalize chuỗi UI (trích xuất → từ điển → review), tài liệu hóa thứ tự fallback locale stored preference → Accept-Language → 'vi' kèm ví dụ q-value [REQ-022]; xây dựng checklist QA hreflang: assertion view-source cho bộ ba link alternate và x-default, xác minh html lang khớp locale, kiểm tra Google Search Console international targeting, ánh xạ og:locale theo từng ngôn ngữ [REQ-023]; ghi chú giới hạn kỹ thuật của việc chuyển locale không reload trang và quy trình bổ sung locale mới trong tương lai.

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

#### 📝 NHIỆM VỤ CON 3.12: Biên soạn hướng dẫn push và deep-link di động

##### Sub-Agent được phân công: Doc

##### Thành phần Đích & Yêu cầu Kỹ thuật:

* **Đường dẫn Đích:** ./sources/docs/mobile-push-deeplink-guide.md

* **Thẻ Truy vết Tag Tokens:** <!--START_TAGS-->[REQ-021]<!--END_TAGS-->

* **Chỉ dẫn Nhiệm vụ Kỹ thuật Cấp thấp:** Tài liệu hóa luồng đăng ký device token sau login với sơ đồ Mermaid tuần tự: login → xin quyền → lấy token FCM/APNs → POST /api/v1/devices/token → Redis registry [REQ-021]; mô tả cấu trúc payload push cho FCM và APNs gồm title/body/category/deepLink kèm bảng ánh xạ category → deep-link route → màn hình đích; xây dựng ma trận hành vi cold-start/background/quit và quy tắc fallback route không hợp lệ; bổ sung phần troubleshoot token invalid, token xoay vòng và từ chối quyền notification; neo mọi mục vào thẻ truy vết [REQ-021] và liên kết chéo với đặc tả API notification-service từ Ngày 1.

<!--END_ATOMIC_SUB_TASK_NODE-->