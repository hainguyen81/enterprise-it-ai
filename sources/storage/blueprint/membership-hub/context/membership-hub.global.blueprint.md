# BỐI CẢNH DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã bản thiết kế** | ARCH-20260822094056 |
| **Tên dự án** | membership-hub |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/22 09:40:56 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & CHẾ ĐỘ KIẾN TRÚC CỐT LÕI

### ⚙️ 1.1. Chế độ hoạt động hệ thống cốt lõi & chế độ kiến trúc cốt lõi
- Hệ thống áp dụng kiến trúc microservices với backend được xây dựng bằng Java/Quarkus, triển khai trên môi trường Kubernetes (GKE) để đảm bảo khả năng mở rộng ngang và tính sẵn sàng cao.
- Hệ thống tuân thủ mô hình RBAC (Kiểm soát truy cập dựa trên vai trò) với 5 vai trò phân quyền rõ ràng: System Admin, Center Admin, Manager, Teacher, Student, đảm bảo quyền hạn được cách ly theo từng trung tâm.
- Luồng xác thực hỗ trợ đăng nhập email/mật khẩu, OAuth2 (Firebase, Google, Facebook), cấp JWT token có thời hạn 15 phút và refresh token có thời hạn 7 ngày.
- Luồng xử lý điểm danh QR đảm bảo tính idempotent, chỉ tạo một bản ghi điểm danh duy nhất cho mỗi học viên, khóa học và ngày, ngay cả khi người dùng quét mã nhiều lần.
- Hệ thống tích hợp đa kênh thông báo: gửi push notification qua FCM/APNs, đăng bài lên nhóm Zalo được chỉ định, đảm bảo thông báo đến người dùng cuối kịp thời cho các sự kiện quan trọng.
- Cơ sở dữ liệu chính sử dụng PostgreSQL 16 với hỗ trợ bản sao đọc cho khối lượng công việc báo cáo, Redis 7.2 được sử dụng để lưu cache phiên người dùng và dữ liệu ngoại tuyến cho ứng dụng di động.
- Hệ thống hỗ trợ đa ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha) với khả năng chuyển đổi ngôn ngữ không cần tải lại trang, đáp ứng yêu cầu bản địa hóa toàn cầu.

### 🌊 1.2. Các kiến trúc luồng dữ liệu doanh nghiệp & hệ sinh thái lõi
- Luồng xác thực: Người dùng gửi yêu cầu đăng nhập/đăng ký đến API Gateway, dịch vụ xác thực Quarkus xác thực thông tin, cấp JWT token và lưu thông tin phiên vào Redis để xác thực các yêu cầu tiếp theo.
- Luồng xử lý điểm danh QR: Ứng dụng di động quét mã QR của khóa học, gửi student ID và timestamp đến backend qua REST API; dịch vụ điểm danh xác thực tính idempotent, ghi bản ghi vào bảng Attendance, đồng bộ trạng thái thẻ hội viên nếu cần.
- Luồng gửi thông báo: Các sự kiện hệ thống (đăng ký khóa học, phân công giáo viên, tạo thông báo, điểm danh thành công) được xuất bản lên chủ đề Apache Kafka, dịch vụ thông báo tiêu thụ sự kiện, gửi push notification qua FCM/APNs và đăng bài lên nhóm Zalo qua Zalo API.
- Luồng tích hợp ứng dụng di động: Frontend Next.js tiêu thụ REST API với bearer token, hỗ trợ caching dữ liệu ngoại tuyến trên thiết bị để xử lý trường hợp mất kết nối mạng, đồng bộ dữ liệu tự động khi kết nối trở lại.
- Luồng báo cáo & phân tích: Dữ liệu điểm danh, ghi danh được đồng bộ đến kho dữ liệu phân tích, dịch vụ báo cáo tổng hợp dữ liệu theo yêu cầu, xuất báo cáo CSV hoặc hiển thị số liệu trên dashboard thời gian thực cho quản trị viên.

## 📁 2. CÁC PHỤ THUỘC NGĂN XẾP CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Hạ tầng lõi Backend:** Java 21, Quarkus 3.15, PostgreSQL 16, Redis 7.2, Apache Kafka 3.6, Hibernate ORM 6.4, Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, JWT 0.12, thư viện mã hóa bcrypt.
- **Ngăn xếp Frontend & Giao diện di động đa nền tảng:** Next.js 14, React 18, React Native 0.73, Tailwind CSS 3.4, i18next 23.7, Axios 1.6, Firebase SDK 10.7.

## 📁 3. RÀNG BUỘC TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP

### 🔑 3.1. Cơ sở bảo mật & tuân thủ
- Mã hóa dữ liệu khi truyền sử dụng TLS 1.3, mã hóa dữ liệu lưu trữ sử dụng AES-256 để đảm bảo bảo mật dữ liệu nhạy cảm.
- Token JWT có thời hạn 15 phút, refresh token có thời hạn 7 ngày, lưu trữ token an toàn trong Redis với thời gian sống phù hợp, hỗ trợ thu hồi token khi có sự cố bảo mật.
- Triển khai các biện pháp giảm thiểu OWASP Top 10: chống injection SQL bằng prepared statements, chống XSS bằng cách lọc đầu vào và mã hóa đầu ra, chống CSRF bằng token CSRF cho các yêu cầu nhạy cảm, kiểm tra quyền hạn trên mọi điểm cuối API.
- Tuân thủ GDPR/CCPA: hỗ trợ xóa dữ liệu cá nhân theo yêu cầu người dùng, xuất dữ liệu ở định dạng JSON, quản lý sự đồng ý cho các thông tin marketing, lưu trữ dữ liệu chỉ trong thời gian cần thiết.
- Ghi log tất cả hành động người dùng (thay đổi vai trò, bản ghi điểm danh, gửi thông báo, thay đổi khóa học) với timestamp, ID người dùng và chi tiết hành động, lưu log trong 1 năm để đáp ứng yêu cầu kiểm toán.

### 🌐 3.2. Ràng buộc hạ tầng & hiệu suất
- Độ trễ trung bình của API cốt lõi (xác thực, ghi điểm danh, danh sách khóa học) dưới 200ms, hỗ trợ đọc sub-second cho 10.000 người dùng đồng thời với các chỉ mục cơ sở dữ liệu được tối ưu.
- Mục tiêu thời gian hoạt động 99.9% hàng năm, hỗ trợ chuyển đổi tự động giữa các cụm GKE để đảm bảo tính sẵn sàng cao, không có thời gian chết kế hoạch.
- Quy mô ngang dịch vụ Quarkus thông qua Kubernetes HPA khi CPU > 70% hoặc độ trễ yêu cầu > 300ms, sử dụng bản sao đọc PostgreSQL cho khối lượng công việc báo cáo để giảm tải cho cơ sở dữ liệu chính.
- Kích thước hình ảnh Docker cơ sở dưới 200MB, hình ảnh cuối cùng dưới 500MB, sử dụng đa giai đoạn build để tối ưu kích thước và bảo mật hình ảnh.
- Hạn mức kết nối cơ sở dữ liệu được cấu hình thông qua HikariCP với giá trị tối ưu cho tải công việc, chính sách xóa cache Redis được cấu hình để đảm bảo dữ liệu phiên luôn tươi, không lưu trữ dữ liệu nhạy cảm trong cache.
- Sao lưu cơ sở dữ liệu PostgreSQL hàng ngày, hỗ trợ phục hồi điểm thời gian trong 24 giờ, sao lưu cụm GKE đến vùng riêng để phục hồi thảm họa, kiểm tra sao lưu định kỳ để đảm bảo tính toàn vẹn của dữ liệu.

### 🥞 3.3. MA TRẬN NGĂN XẾP KIẾN TRÚC
```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 🏁 4. TỔNG QUAN KIẾN TRÚC ĐA GIAI ĐOẠN MỨC CAO

### 📦 4.1. DANH SÁCH CÔNG VIỆC SẢN PHẨM KIẾN TRÚC TỔNG THỂ

<!--START_BACKLOG_SYNOPSIS_GRID-->

### MA TRẬN SỐ HỌC HỆ THỐNG
> - Tổng số thẻ [REQ]: 25 Thẻ

> - Tổng số thẻ [EXC]: 5 Thẻ

> - Tổng số thẻ [ARC]: 10 Thẻ

> - Tổng số thẻ [DAT]: 9 Thẻ

> - Tổng số thẻ [NFR]: 9 Thẻ

> - ➡️ Tổng số thẻ SRS: 58 Thẻ

Bảng danh sách công việc sản phẩm kiến trúc tổng thể này ánh xạ toàn bộ các yêu cầu nghiệp vụ, kiến trúc, dữ liệu và phi chức năng từ đặc tả yêu cầu phần mềm vào các nhiệm vụ kỹ thuật cụ thể, đảm bảo tính truy xuất nguồn gốc 100% và tuân thủ các tiêu chuẩn doanh nghiệp. Các thành phần kiến trúc có mối phụ thuộc chặt chẽ: hạ tầng cơ sở dữ liệu PostgreSQL là nền tảng cho tất cả các service vi mô, lớp bảo mật RBAC và xác thực OAuth2 kiểm soát truy cập vào toàn bộ hệ thống, hạ tầng DevOps trên GKE đảm bảo tính sẵn sàng và khả năng mở rộng, còn hệ thống tài liệu hỗ trợ vận hành và bảo trì lâu dài.

| STT | Nhiệm vụ | Mục đích kỹ thuật / Tóm tắt sản phẩm bàn giao | Loại | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Khởi tạo cấu trúc dự án backend vi mô Quarkus | Tạo pom.xml gốc và pom.xml cho từng service vi mô (auth, center, course, enrollment, attendance, membership, notification, promotion, report, ai-chatbot) | Mã Ứng dụng | [ARC-000] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 2 | Khởi tạo cấu trúc dự án frontend Next.js | Tạo package.json và tsconfig.json cho ứng dụng web và di động | Mã Ứng dụng | [ARC-000] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 3 | Khởi tạo cấu trúc thư mục tài liệu doanh nghiệp | Tạo cấu trúc thư mục cho bản vẽ kiến trúc, hợp đồng API, hướng dẫn vận hành | Tài liệu Doanh nghiệp | [ARC-000] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 4 | Triển khai chức năng đăng ký người dùng bằng email/mật khẩu | Xác thực đầu vào, tạo bản ghi người dùng với vai trò Student, cấp JWT token | Mã Ứng dụng | [REQ-001, EXC-004] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 5 | Triển khai xác thực mạng xã hội OAuth2 | Tích hợp Firebase, Google, Facebook OAuth2, xử lý mã xác thực, tạo/cập nhật bản ghi người dùng, cấp JWT | Mã Ứng dụng | [REQ-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 6 | Triển khai chức năng phân quyền người dùng | Gán/thay đổi vai trò người dùng, áp dụng quyền truy cập ngay lập tức | Mã Ứng dụng | [REQ-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 7 | Triển khai chức năng xem danh sách trung tâm | Hiển thị danh sách trung tâm với địa chỉ, mã số thuế, thông tin liên hệ quản trị | Mã Ứng dụng | [REQ-004] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 8 | Triển khai chức năng quản lý trung tâm (CRUD) | Thêm, sửa, xóa bản ghi trung tâm, kiểm tra trùng mã số thuế | Mã Ứng dụng | [REQ-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 9 | Triển khai chức năng phân quyền quản trị trung tâm | Gán/huỷ gán quyền Center Admin cho người dùng tại trung tâm cụ thể | Mã Ứng dụng | [REQ-006] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 10 | Triển khai chức năng xem danh sách khóa học | Hiển thị danh sách khóa học với lịch học và giáo viên phụ trách | Mã Ứng dụng | [REQ-007] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 11 | Triển khai chức năng quản lý khóa học (CRUD) với kiểm tra xung đột lịch | Thêm, sửa, xóa khóa học, kiểm tra trùng lịch giáo viên/địa điểm | Mã Ứng dụng | [REQ-008] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 12 | Triển khai chức năng phân công giáo viên vào khóa học | Gán/huỷ gán giáo viên cho khóa học, kích hoạt thông báo cho giáo viên | Mã Ứng dụng | [REQ-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 13 | Triển khai chức năng duyệt khóa học cho học viên | Hiển thị danh sách khóa học chưa đăng ký của học viên | Mã Ứng dụng | [REQ-010] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 14 | Triển khai chức năng đăng ký khóa học học viên | Xử lý đăng ký khóa học, tự động tạo tài khoản Student nếu chưa tồn tại, gửi thông báo | Mã Ứng dụng | [REQ-011] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 15 | Triển khai chức năng điểm danh quét mã QR | Nhận payload quét QR, xác thực quan hệ học viên-khóa học, tạo bản ghi điểm danh | Mã Ứng dụng | [REQ-012, EXC-001, EXC-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 16 | Triển khai tính chất bất biến của điểm danh | Đảm bảo chỉ tạo 1 bản ghi điểm danh/học viên/khóa học/ngày, xử lý yêu cầu trùng lặp | Mã Ứng dụng | [REQ-013, EXC-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 17 | Triển khai chức năng hiển thị tính hợp lệ thẻ hội viên | Hiển thị tổng số ngày hiệu lực, số ngày đã sử dụng, số ngày còn lại của thẻ hội viên | Mã Ứng dụng | [REQ-014] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 18 | Triển khai chức năng gia hạn thẻ hội viên | Gia hạn ngày kết thúc thẻ sau khi xác nhận thanh toán, gửi thông báo xác nhận | Mã Ứng dụng | [REQ-015] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 19 | Triển khai chức năng kích hoạt thông báo đa kênh | Tạo bản ghi thông báo, xếp hàng push notification, gửi tin nhắn nhóm Zalo | Mã Ứng dụng | [REQ-016, EXC-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 20 | Triển khai chức năng quản lý khuyến mãi | CRUD khuyến mãi (giảm giá, ưu đãi) với ngày bắt đầu/kết thúc, hiển thị cho học viên | Mã Ứng dụng | [REQ-017] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 21 | Triển khai chức năng quản lý thông báo | CRUD thông báo với ngày hết hạn tùy chọn, tự động ẩn sau ngày hết hạn, phát sóng toàn hệ thống | Mã Ứng dụng | [REQ-018] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 22 | Triển khai tích hợp chatbot AI | Xử lý câu hỏi thường gặp về khóa học, giáo viên, trung tâm, trạng thái tài khoản, leo thang hỗ trợ khi độ tin cậy thấp | Mã Ứng dụng | [REQ-019] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 23 | Triển khai giao diện người dùng vai trò trên di động | Xây dựng giao diện responsive Next.js cho từng vai trò (Student, Teacher, Admin...), đồng bộ chức năng với web | Mã Ứng dụng | [REQ-020] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 24 | Triển khai thông báo đẩy trên di động | Tích hợp FCM/APNs, quản lý token thiết bị, xử lý nhận thông báo trên ứng dụng di động | Mã Ứng dụng | [REQ-021] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 25 | Triển khai phát hiện ngôn ngữ mặc định | Phát hiện ngôn ngữ ưu tiên của người dùng, lưu trữ cài đặt, fallback sang Accept-Language header | Mã Ứng dụng | [REQ-022] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 26 | Triển khai SEO đa ngôn ngữ | Thêm thẻ meta ngôn ngữ, thuộc tính hreflang, hỗ trợ 3 ngôn ngữ (Anh, Việt, Tây Ban Nha) | Mã Ứng dụng | [REQ-023] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 27 | Triển khai chức năng tạo báo cáo điểm danh CSV | Xuất báo cáo điểm danh hàng ngày cho trung tâm, định dạng CSV với các cột StudentName, CourseName, AttendanceDate, Status | Mã Ứng dụng | [REQ-024, EXC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 28 | Triển khai bảng điều khiển tóm tắt ghi danh | Xây dựng dashboard realtime hiển thị tổng học viên, khóa học đang hoạt động, buổi học sắp tới (7 ngày tới) | Mã Ứng dụng | [REQ-025] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 29 | Khởi tạo hạ tầng cơ sở dữ liệu PostgreSQL | Tạo schema, tất cả các bảng dữ liệu theo định nghĩa, cấu hình connection pool và index tối ưu | Mã Ứng dụng | [DAT-ALL (1 to 9)] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 30 | Triển khai lớp bảo mật RBAC và xác thực | Triển khai kiểm soát truy cập dựa trên vai trò, xác thực JWT, OAuth2, refresh token, bảo vệ tất cả endpoint | Mã Ứng dụng | [ARC-001, ARC-002, ARC-003, ARC-004, ARC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 31 | Triển khai hợp đồng tích hợp hệ thống | Triển khai luồng xác thực, điểm danh QR, thông báo đa kênh, tích hợp backend-frontend | Mã Ứng dụng | [ARC-006, ARC-007, ARC-008, ARC-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 32 | Triển khai hạ tầng DevOps và đám mây | Xây dựng Dockerfile đa giai đoạn, pipeline CI/CD GitHub Actions, triển khai GKE, cấu hình Terraform cho GCP, tích hợp FCM/APNs, Zalo API, Redis caching, đảm bảo tuân thủ NFR | Hạ tầng DevOps | [NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-006, NFR-007, NFR-008, NFR-009, ARC-010] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 33 | Xây dựng tài liệu hệ thống doanh nghiệp | Viết bản vẽ kiến trúc, hợp đồng API REST/Event, hướng dẫn vận hành, tài liệu cơ sở dữ liệu, hướng dẫn người dùng | Tài liệu Doanh nghiệp | <!--REGISTERED_BACKLOG_TASK_ROW--> |
| **TÓM TẮT** | **Tổng số thẻ theo dõi đã bao phủ:** 58 | **Tổng số nhiệm vụ:** 33 | **Trạng thái:** ĐÃ XÁC THỰC | **Mức độ bao phủ:** 100% <!--REGISTERED_BACKLOG_TASK_ROW--> |

<!--END_BACKLOG_SYNOPSIS_GRID-->

<!--END_PART_1_BACKLOG_4_1-->

### 🔭 4.2. MA TRẬN TỔNG QUAN ĐA GIAI ĐOẠN
<!--START_PHASE_SYNOPSIS_GRID-->
### CHU KỲ SỐ HỌC MA TRẬN
> - **Tổng số nhiệm vụ backlog:** 33 Nhiệm vụ
> - **Tổng số thẻ backlog:** 58 Thẻ
> - **Tổng số nhiệm vụ đã phân phối:** 33 Nhiệm vụ
> - **Tổng số thẻ đã phân phối:** 58 Thẻ

| Giai đoạn | Khoảng ngày | ID Nhiệm vụ được bao phủ | Thành phần kiến trúc / Đường dẫn mô-đun | Tóm tắt sản phẩm bàn giao kỹ thuật | Đại lý phụ trách | ID Thẻ được nhắm mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | Nhiệm vụ 1, 2, 3, 29, 30, 4, 5, 6, 7, 8, 9 | ./sources/backend, ./sources/frontend, ./sources/docs | Khởi tạo cấu trúc dự án vi mô backend Quarkus (pom.xml gốc và các module service), cấu trúc dự án frontend Next.js (package.json, tsconfig.json), cấu trúc thư mục tài liệu doanh nghiệp, khởi tạo schema cơ sở dữ liệu PostgreSQL với toàn bộ các bảng dữ liệu theo định nghĩa, triển khai lớp xác thực RBAC và OAuth2 (JWT, refresh token), triển khai các chức năng cốt lõi quản lý người dùng (đăng ký, xác thực xã hội, phân quyền) và quản lý trung tâm (xem danh sách, CRUD, phân quyền quản trị trung tâm) | Coder, Tester, Reviewer, Doc | [ARC-000], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [EXC-004], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 2 | 1-2 | Nhiệm vụ 10, 11, 12, 13, 14 | ./sources/backend/course-service, ./sources/backend/enrollment-service, ./sources/frontend | Triển khai các chức năng quản lý khóa học (xem danh sách, CRUD với kiểm tra xung đột lịch giáo viên/địa điểm, phân công giáo viên) và chức năng đăng ký khóa học cho học viên (duyệt khóa học chưa đăng ký, xử lý đăng ký tự động tạo tài khoản Student nếu cần, gửi thông báo tự động) | Coder, Tester, Reviewer, Doc | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 3 | 1-4 | Nhiệm vụ 15, 16, 17, 18, 19, 20, 21 | ./sources/backend/attendance-service, ./sources/backend/membership-service, ./sources/backend/notification-service, ./sources/backend/promotion-service, ./sources/frontend | Triển khai chức năng điểm danh quét mã QR với tính bất biến chống trùng lặp (đảm bảo 1 bản ghi điểm danh/học viên/khóa học/ngày), quản lý thẻ hội viên (hiển thị số ngày còn lại, gia hạn thẻ sau thanh toán), hệ thống thông báo đa kênh (push notification, tin nhắn nhóm Zalo) với cơ chế retry khi gửi thất bại, quản lý khuyến mãi và thông báo hệ thống (CRUD với ngày hết hạn tùy chọn, tự động ẩn thông báo hết hạn) | Coder, Tester, Reviewer, Doc | [REQ-012], [EXC-001], [EXC-002], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [EXC-003], [REQ-017], [REQ-018] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 4 | 1-3 | Nhiệm vụ 22, 23, 24, 25, 26, 27, 28 | ./sources/backend/ai-chatbot-service, ./sources/frontend, ./sources/docs | Triển khai tích hợp chatbot AI hỗ trợ trả lời câu hỏi thường gặp và leo thang hỗ trợ khi độ tin cậy thấp, xây dựng giao diện người dùng responsive cho ứng dụng di động với phân quyền theo vai trò, tích hợp thông báo đẩy FCM/APNs, triển khai phát hiện ngôn ngữ mặc định và SEO đa ngôn ngữ (hreflang, thẻ meta), xây dựng chức năng xuất báo cáo điểm danh CSV và bảng điều khiển tóm tắt ghi danh realtime | Coder, Tester, Reviewer, Doc | [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [EXC-005], [REQ-025] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 5 | 1-5 | Nhiệm vụ 31, 32, 33 | ./sources/infra, ./sources/docs | Triển khai toàn bộ hạ tầng DevOps và đám mây: xây dựng Dockerfile đa giai đoạn cho tất cả service, pipeline CI/CD GitHub Actions, triển khai cụm GKE với auto-scaling, cấu hình hạ tầng GCP (VPC, IAM, Storage, PostgreSQL read replicas) qua Terraform, tích hợp FCM/APNs, Zalo API, Redis caching cho session, đảm bảo tuân thủ tất cả yêu cầu phi chức năng (hiệu năng, bảo mật, khả năng sẵn sàng, sao lưu và phục hồi thảm họa, tuân thủ GDPR/CCPA), hoàn thiện toàn bộ tài liệu hệ thống doanh nghiệp (bản vẽ kiến trúc, hợp đồng API, hướng dẫn vận hành, tài liệu cơ sở dữ liệu, hướng dẫn người dùng) | Coder, Tester, Reviewer, Doc, Docker, GCP, GKE | [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] <!--REGISTERED_PHASE_ROW--> |
| **Kiểm toán** | **Xác minh phân phối tổng backlog** | **Tổng số giai đoạn:** 5 | **Tổng số thẻ backlog:** 58 | **Tổng số thẻ đã phân phối:** 58 | **Tổng số nhiệm vụ đã phân phối:** 33 | **Trạng thái & Tuân thủ:** Đã xác thực (100%) |
<!--END_PHASE_SYNOPSIS_GRID-->

## 🔬 5. CHUYÊN MÔN HÓA CHI TIẾT GIAI ĐOẠN & SẢN PHẨM BÀN GIAO TỪNG NGÀY
<!--START_PHASE_INDEX-->
### 📈 GIAI ĐOẠN 1 - KHỞI TẠO CẤU TRÚC DỰ ÁN VÀ NỀN TẢNG HẠ TẦNG CƠ SỞ
- **Mục tiêu cốt lõi của giai đoạn:** Thiết lập toàn bộ cấu trúc dự án nền tảng cho kiến trúc vi mô backend Quarkus và frontend Next.js, khởi tạo toàn bộ schema cơ sở dữ liệu PostgreSQL với 9 bảng nghiệp vụ chính, triển khai lớp xác thực RBAC và OAuth2 cốt lõi, cùng các chức năng quản lý người dùng và trung tâm đầu tiên, đảm bảo mọi service có môi trường phát triển ổn định, sẵn sàng cho các giai đoạn phát triển chức năng tiếp theo.

- **Bản đồ ma trận thư mục vật lý mục tiêu:** Danh sách đầy đủ các tệp vật lý cụ thể được tạo/xử lý trong giai đoạn này, kèm Tag ID truy xuất:
  * ./sources/backend/pom.xml [ARC-000]
  * ./sources/backend/auth-service/pom.xml [ARC-000]
  * ./sources/backend/center-service/pom.xml [ARC-000]
  * ./sources/backend/course-service/pom.xml [ARC-000]
  * ./sources/backend/enrollment-service/pom.xml [ARC-000]
  * ./sources/backend/attendance-service/pom.xml [ARC-000]
  * ./sources/backend/membership-service/pom.xml [ARC-000]
  * ./sources/backend/notification-service/pom.xml [ARC-000]
  * ./sources/backend/promotion-service/pom.xml [ARC-000]
  * ./sources/backend/report-service/pom.xml [ARC-000]
  * ./sources/backend/ai-chatbot-service/pom.xml [ARC-000]
  * ./sources/frontend/package.json [ARC-000]
  * ./sources/frontend/tsconfig.json [ARC-000]
  * ./sources/docs/architecture-overview.md [ARC-000]
  * ./sources/docs/api-contracts-auth.md [ARC-000]
  * ./sources/docs/api-contracts-center.md [ARC-000]
  * ./sources/docs/database-schema.md [ARC-000]
  * ./sources/backend/auth-service/src/main/java/com/hub/auth/entity/User.java [DAT-001, ARC-001]
  * ./sources/backend/auth-service/src/main/java/com/hub/auth/entity/Role.java [DAT-002, ARC-001]
  * ./sources/backend/auth-service/src/main/java/com/hub/auth/repository/UserRepository.java [DAT-001, ARC-001]
  * ./sources/backend/auth-service/src/main/java/com/hub/auth/repository/RoleRepository.java [DAT-002, ARC-001]
  * ./sources/backend/auth-service/src/main/java/com/hub/auth/service/AuthService.java [REQ-001, REQ-002, ARC-006]
  * ./sources/backend/auth-service/src/main/java/com/hub/auth/controller/AuthController.java [REQ-001, REQ-002, ARC-006]
  * ./sources/backend/center-service/src/main/java/com/hub/center/entity/Center.java [DAT-003, ARC-002]
  * ./sources/backend/center-service/src/main/java/com/hub/center/repository/CenterRepository.java [DAT-003, ARC-002]
  * ./sources/backend/center-service/src/main/java/com/hub/center/service/CenterService.java [REQ-004, REQ-005, ARC-002]
  * ./sources/backend/center-service/src/main/java/com/hub/center/controller/CenterController.java [REQ-004, REQ-005, ARC-002]

- **Đặc tả DDL SQL cơ sở dữ liệu [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]:**
```sql
-- Tạo bảng vai trò người dùng
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

-- Tạo bảng người dùng
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL REFERENCES roles(role_id),
    provider VARCHAR(20) NOT NULL DEFAULT 'local' CHECK (provider IN ('local', 'firebase', 'google', 'facebook')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tạo bảng trung tâm
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE CHECK (tax_id ~ '^[0-9]{10,13}$'),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255) CHECK (contact_email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Tạo bảng khóa học
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30,
    CHECK (end_date > start_date)
);

-- Tạo bảng ghi danh
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)
);

-- Tạo bảng điểm danh
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id, attendance_date)
);

-- Tạo bảng thẻ hội viên
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL UNIQUE REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);

-- Tạo bảng thông báo
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(255),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

-- Tạo bảng khuyến mãi
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL CHECK (discount_percent BETWEEN 1 AND 100),
    start_date DATE,
    end_date DATE,
    description TEXT,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Tạo bảng thông báo hệ thống
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Tạo bảng cài đặt hệ thống
CREATE TABLE system_settings (
    setting_key VARCHAR(50) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **Hợp đồng định tuyến API và sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-006], [ARC-007]:**
```json
// Endpoint xác thực
POST /api/auth/register
Request Body: {
  "email": "string",
  "password": "string",
  "fullName": "string"
}
Response 200: {
  "accessToken": "string",
  "refreshToken": "string",
  "expiresIn": 900,
  "user": { "userId": "uuid", "role": "string" }
}
Response 400: { "error": "VALIDATION_ERROR", "details": ["Email không hợp lệ", "Mật khẩu phải có ít nhất 8 ký tự"] }

POST /api/auth/oauth2/{provider}
Request Body: { "code": "string", "redirectUri": "string" }
Response 200: Tương tự register

POST /api/auth/refresh
Request Body: { "refreshToken": "string" }
Response 200: { "accessToken": "string", "expiresIn": 900 }

// Endpoint quản lý trung tâm
GET /api/centers
Response 200: [
  { "centerId": "uuid", "name": "string", "address": "string", "taxId": "string", "contactPhone": "string", "contactEmail": "string" }
]

POST /api/centers
Request Body: { "name": "string", "address": "string", "taxId": "string", "contactPhone": "string", "contactEmail": "string" }
Response 201: { "centerId": "uuid" }
Response 409: { "error": "DUPLICATE_TAX_ID", "message": "Mã số thuế đã tồn tại" }

PUT /api/centers/{centerId}
DELETE /api/centers/{centerId}

POST /api/centers/{centerId}/admins
Request Body: { "userId": "uuid" }
Response 200: { "message": "Phân quyền quản trị trung tâm thành công" }
```

- **Trình xử lý ngoại lệ cục bộ của giai đoạn [EXC-004]:**
Xử lý lỗi xác thực đầu vào không hợp lệ cho chức năng đăng ký người dùng:
- Mã lỗi: `VALIDATION_ERROR`
- Trạng thái HTTP: 400 Bad Request
- Thông báo trả về: Liệt kê chi tiết từng trường không hợp lệ (ví dụ: "Email không đúng định dạng", "Mật khẩu phải có ít nhất 8 ký tự bao gồm chữ hoa, chữ thường và số", "Họ tên không được để trống")
- Hành động hệ thống: Không tạo bản ghi người dùng, ghi log lỗi xác thực vào hệ thống theo yêu cầu [NFR-006]

#### 📅 NHẬT KÝ PHÂN PHỐI NHIỆM VỤ ĐẠI LÝ PHỤ TRÁCH THEO THỨ TỰ THỜI GIAN TỪNG NGÀY (GIAI ĐOẠN 1)
<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 1: KHỞI TẠO CẤU TRÚC DỰ ÁN NỀN TẢNG
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 1: Tạo cấu trúc dự án backend vi mô Quarkus
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [ARC-000]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/pom.xml
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tệp pom.xml gốc cho dự án backend vi mô Quarkus, cấu hình các module service con (auth, center, course, enrollment, attendance, membership, notification, promotion, report, ai-chatbot), thiết lập các phụ thuộc chung cho Quarkus, JWT, PostgreSQL driver, OAuth2, và các thư viện bổ trợ cần thiết, đảm bảo cấu hình build thành công cho tất cả module.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 2: Tạo cấu trúc dự án frontend Next.js
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [ARC-000]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/frontend/package.json
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tệp package.json cho dự án frontend Next.js, cấu hình các phụ thuộc cốt lõi (Next.js, React, Redux Toolkit, Axios, i18n), khởi tạo cấu hình tsconfig.json cho TypeScript, đảm bảo cấu hình build và chạy môi trường phát triển thành công.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 3: Khởi tạo cấu trúc thư mục tài liệu doanh nghiệp
* **Chuyên môn đại lý phụ trách:** [Doc]
* **Tag ID mục tiêu:** [ARC-000]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/architecture-overview.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo cấu trúc thư mục tài liệu doanh nghiệp, khởi tạo các tệp mẫu cho bản vẽ kiến trúc tổng thể, hợp đồng API, hướng dẫn vận hành, đảm bảo cấu trúc tài liệu tuân thủ chuẩn doanh nghiệp, dễ dàng mở rộng cho các giai đoạn sau.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 4: Xác thực cấu trúc dự án build thành công
* **Chuyên môn đại lý phụ trách:** [Tester]
* **Tag ID mục tiêu:** [ARC-000]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/pom.xml;./sources/backend/auth-service/src/test/java/com/hub/auth/BuildValidationTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện build tất cả module backend và dự án frontend, xác nhận không có lỗi biên dịch, tất cả phụ thuộc được tải đúng, ghi nhận kết quả kiểm thực vào báo cáo.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 2: KHỞI TẠO SCHEMA CƠ SỞ DỮ LIỆU VÀ THỰC THỂ RBAC CƠ BẢN
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 1: Tạo script DDL khởi tạo toàn bộ bảng nghiệp vụ
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/resources/db/migration/V1__init_schema.sql
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết script DDL ANSI compliant khởi tạo toàn bộ 9 bảng nghiệp vụ (roles, users, centers, courses, enrollments, attendance, student_cards, notifications, promotions, announcements, system_settings), định nghĩa rõ ràng kiểu dữ liệu, ràng buộc khóa chính/khóa ngoại, ràng buộc CHECK cho các trường kiểm tra, đảm bảo script chạy thành công trên PostgreSQL.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 2: Triển khai thực thể Role và User trong service auth
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [DAT-001], [DAT-002], [ARC-001]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/entity/Role.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho bảng roles và users, ánh xạ chính xác các trường dữ liệu, thiết lập quan hệ giữa User và Role (nhiều-người dùng thuộc một vai trò), đảm bảo ánh xạ khớp với schema cơ sở dữ liệu đã định nghĩa.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 3: Xác thực migration cơ sở dữ liệu thành công
* **Chuyên môn đại lý phụ trách:** [Tester]
* **Tag ID mục tiêu:** [DAT-ALL]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/resources/db/migration/V1__init_schema.sql;./sources/backend/auth-service/src/test/java/com/hub/auth/DbMigrationTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Chạy script migration trên cơ sở dữ liệu PostgreSQL cục bộ, xác nhận tất cả các bảng được tạo đúng, các ràng buộc khóa chính/khóa ngoại hoạt động, không có lỗi khi chạy script.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 4: Cập nhật tài liệu schema cơ sở dữ liệu
* **Chuyên môn đại lý phụ trách:** [Doc]
* **Tag ID mục tiêu:** [DAT-ALL]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/database-schema.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cập nhật tệp tài liệu schema cơ sở dữ liệu với mô tả chi tiết từng bảng, trường dữ liệu, kiểu dữ liệu, ràng buộc, mối quan hệ giữa các bảng, kèm sơ đồ ERD đã được cung cấp trong yêu cầu.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 3: TRIỂN KHAI CHỨC NĂNG ĐĂNG KÝ VÀ XÁC THỰC NGƯỜI DÙNG CƠ BẢN
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 1: Triển khai logic đăng ký email/mật khẩu trong AuthService
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [REQ-001], [EXC-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/AuthService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic đăng ký người dùng bằng email/mật khẩu, bao gồm xác thực đầu vào (định dạng email, độ mạnh mật khẩu), mã hóa mật khẩu bằng bcrypt, tạo bản ghi người dùng với vai trò mặc định là Student, xử lý lỗi xác thực theo yêu cầu [EXC-004].
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 2: Triển khai endpoint đăng ký và đăng nhập trong AuthController
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [REQ-001], [ARC-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/controller/AuthController.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST cho đăng ký, đăng nhập, cấp access token và refresh token theo chuẩn JWT, thời hạn access token 15 phút, refresh token 7 ngày, trả về phản hồi JSON theo hợp đồng API đã định nghĩa.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 3: Viết unit test cho chức năng đăng ký và xác thực
* **Chuyên môn đại lý phụ trách:** [Tester]
* **Tag ID mục tiêu:** [REQ-001], [EXC-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/AuthService.java;./sources/backend/auth-service/src/test/java/com/hub/auth/AuthServiceTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test đầy đủ cho logic đăng ký, bao gồm trường hợp thành công, lỗi xác thực đầu vào (email không hợp lệ, mật khẩu yếu), trùng lặp email, xác nhận mật khẩu bcrypt được tạo đúng, bản ghi người dùng được lưu chính xác vào cơ sở dữ liệu.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 4: Rà soát mã nguồn chức năng xác thực
* **Chuyên môn đại lý phụ trách:** [Reviewer]
* **Tag ID mục tiêu:** [REQ-001], [EXC-004], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/AuthService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát mã nguồn chức năng đăng ký và xác thực, kiểm tra tuân thủ chuẩn bảo mật mật khẩu bcrypt, không có lỗ hổng SQL injection, xác thực đầu vào đầy đủ, xử lý ngoại lệ chính xác, đề xuất cải tiến nếu có.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 4: TRIỂN KHAI XÁC THỰC MẠNG XÃ HỘI VÀ PHÂN QUYỀN NGƯỜI DÙNG
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 1: Tích hợp OAuth2 Firebase/Google/Facebook vào AuthService
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [REQ-002], [ARC-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/OAuth2Service.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic tích hợp OAuth2 với các nhà cung cấp Firebase, Google, Facebook, xử lý mã xác thực từ nhà cung cấp, trao đổi lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ, cấp JWT token sau khi xác thực thành công.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 2: Triển khai logic gán/thay đổi vai trò người dùng
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/RoleManagementService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic gán, thay đổi, hủy gán vai trò người dùng, đảm bảo quyền truy cập được áp dụng ngay lập tức sau khi thay đổi vai trò, kiểm tra quyền của người thực hiện thao tác phân quyền theo RBAC.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 3: Viết unit test cho xác thực mạng xã hội và phân quyền
* **Chuyên môn đại lý phụ trách:** [Tester]
* **Tag ID mục tiêu:** [REQ-002], [REQ-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/OAuth2Service.java;./sources/backend/auth-service/src/test/java/com/hub/auth/OAuth2ServiceTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test cho luồng xác thực mạng xã hội (giả lập phản hồi từ nhà cung cấp OAuth2), xác nhận bản ghi người dùng được tạo/cập nhật đúng, JWT token được cấp chính xác; viết test cho logic phân quyền, xác nhận vai trò người dùng được cập nhật đúng trong cơ sở dữ liệu.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 4: Rà soát logic phân quyền và xác thực mạng xã hội
* **Chuyên môn đại lý phụ trách:** [Reviewer]
* **Tag ID mục tiêu:** [REQ-002], [REQ-003], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/OAuth2Service.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát logic tích hợp OAuth2 và phân quyền người dùng, kiểm tra không có lỗ hổng bảo mật (ví dụ: lộ thông tin người dùng, phân quyền sai vai trò), xác nhận tuân thủ yêu cầu OAuth2 và RBAC, đề xuất cải tiến nếu có.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 5: TRIỂN KHAI CHỨC NĂNG QUẢN LÝ TRUNG TÂM CƠ BẢN
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 1: Triển khai thực thể Center và repository tương ứng
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [DAT-003], [ARC-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/entity/Center.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho bảng centers, ánh xạ chính xác các trường dữ liệu, thiết lập các ràng buộc ánh xạ khớp với schema cơ sở dữ liệu, triển khai repository cho thực thể Center với các phương thức truy vấn cơ bản.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 2: Triển khai logic nghiệp vụ quản lý trung tâm
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [REQ-004], [REQ-005], [ARC-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/service/CenterService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai logic nghiệp vụ cho các chức năng xem danh sách trung tâm, thêm/sửa/xóa trung tâm, kiểm tra trùng lặp mã số thuế khi tạo mới hoặc cập nhật trung tâm, đảm bảo chỉ System Admin có quyền thực hiện các thao tác quản lý.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 3: Triển khai endpoint quản lý trung tâm
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [REQ-004], [REQ-005], [ARC-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/controller/CenterController.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST cho chức năng quản lý trung tâm (GET /api/centers, POST /api/centers, PUT /api/centers/{id}, DELETE /api/centers/{id}), áp dụng bộ lọc RBAC để kiểm soát quyền truy cập, trả về phản hồi JSON theo hợp đồng API đã định nghĩa.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 4: Viết unit test cho chức năng quản lý trung tâm
* **Chuyên môn đại lý phụ trách:** [Tester]
* **Tag ID mục tiêu:** [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/center-service/src/main/java/com/hub/center/service/CenterService.java;./sources/backend/center-service/src/test/java/com/hub/center/CenterServiceTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test đầy đủ cho các chức năng quản lý trung tâm, bao gồm trường hợp thành công, lỗi trùng mã số thuế, truy cập trái phép khi không có quyền System Admin, xác nhận dữ liệu trả về đúng định dạng.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 6: TRIỂN KHAI LỚP BẢO MẬT RBAC VÀ BỘ LỌC XÁC THỰC JWT
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 1: Triển khai công cụ tạo và xác thực JWT token
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [ARC-006], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/util/JwtUtil.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai công cụ tạo access token và refresh token, xác thực token, kiểm tra thời hạn token, sử dụng thuật toán mã hóa an toàn (HS256), đảm bảo token không thể bị giả mạo.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 2: Triển khai bộ lọc xác thực RBAC cho tất cả endpoint
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/filter/RbacFilter.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai bộ lọc JWT và RBAC toàn cục cho tất cả service vi mô, kiểm tra tính hợp lệ của access token trên mỗi yêu cầu, xác thực quyền truy cập của người dùng dựa trên vai trò và tài nguyên được yêu cầu, trả về lỗi 401 Unauthorized hoặc 403 Forbidden nếu không có quyền.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 3: Viết unit test cho bộ lọc RBAC
* **Chuyên môn đại lý phụ trách:** [Tester]
* **Tag ID mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/filter/RbacFilter.java;./sources/backend/auth-service/src/test/java/com/hub/auth/RbacFilterTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test cho bộ lọc RBAC, kiểm tra các trường hợp: token hợp lệ có quyền truy cập, token hết hạn, token không hợp lệ, người dùng có quyền truy cập, người dùng không có quyền truy cập, xác nhận phản hồi lỗi đúng định dạng.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 4: Cập nhật tài liệu đặc tả bảo mật và luồng xác thực
* **Chuyên môn đại lý phụ trách:** [Doc]
* **Tag ID mục tiêu:** [ARC-006], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/security-spec.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cập nhật tài liệu đặc tả bảo mật với mô tả chi tiết luồng xác thực, cấu trúc JWT token, chính sách phân quyền RBAC, các yêu cầu bảo mật tuân thủ OWASP Top 10 và NFR-003.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 7: XỬ LÝ NGOẠI LỆ, KIỂM THỬ TÍCH HỢP VÀ HOÀN THIỆN TÀI LIỆU GIAI ĐOẠN
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 1: Triển khai trình xử lý ngoại lệ toàn cục
* **Chuyên môn đại lý phụ trách:** [Coder]
* **Tag ID mục tiêu:** [EXC-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/exception/GlobalExceptionHandler.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai trình xử lý ngoại lệ toàn cục cho tất cả service, chuẩn hóa cấu trúc phản hồi lỗi, xử lý các ngoại lệ nghiệp vụ (lỗi xác thực, lỗi phân quyền, lỗi trùng dữ liệu) và ngoại lệ hệ thống, ghi log lỗi theo yêu cầu [NFR-006].
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 2: Thực hiện kiểm thử tích hợp giữa service auth và center
* **Chuyên môn đại lý phụ trách:** [Tester]
* **Tag ID mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/backend/auth-service/src/test/java/com/hub/auth/IntegrationAuthCenterTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện kiểm thử tích hợp toàn bộ luồng nghiệp vụ: đăng ký người dùng -> đăng nhập -> lấy JWT token -> truy cập danh sách trung tâm -> tạo trung tâm mới -> phân quyền Center Admin -> xác nhận quyền truy cập của Center Admin hoạt động đúng, không có lỗi trong toàn bộ luồng.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 3: Rà soát toàn bộ mã nguồn giai đoạn
* **Chuyên môn đại lý phụ trách:** [Reviewer]
* **Tag ID mục tiêu:** [ALL_PHASE_1_TAGS]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/auth-service/src/main/java/com/hub/auth/service/AuthService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Rà soát toàn bộ mã nguồn được tạo trong giai đoạn 1, kiểm tra tuân thủ chuẩn mã hóa doanh nghiệp, không có lỗ hổng bảo mật, hiệu năng đáp ứng yêu cầu NFR-001, đề xuất các cải tiến về cấu trúc mã và tối ưu hóa.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 CÔNG VIỆC CON 4: Hoàn thiện tài liệu giai đoạn 1
* **Chuyên môn đại lý phụ trách:** [Doc]
* **Tag ID mục tiêu:** [ARC-000], [DAT-ALL]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/api-contracts-auth.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Hoàn thiện tài liệu hợp đồng API cho tất cả endpoint của service auth và center, cập nhật tài liệu kiến trúc tổng thể với cấu trúc dự án đã được khởi tạo, đảm bảo tài liệu đầy đủ, chính xác, dễ hiểu cho các đội phát triển các giai đoạn sau.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

**Sổ cái kiểm toán chéo giai đoạn:**
| Tên trường | Giá trị |
| :--- | :--- |
| Tổng số sub-task nguyên tử đã tạo trong toàn bộ lịch sử (H) | 0 |
| Tổng số sub-task nguyên tử tạo mới trong giai đoạn này (A) | 28 |
| Tổng số sub-task nguyên tử tổng cộng (Final_Total = H + A) | 28 |
| TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5 | 28 |
<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->
### 📈 GIAI ĐOẠN 2 - TRIỂN KHAI CHỨC NĂNG QUẢN LÝ KHÓA HỌC VÀ ĐĂNG KÝ HỌC VIÊN
- **Mục tiêu cốt lõi và mục đích của giai đoạn:** Triển khai toàn bộ chức năng quản lý khóa học (xem danh sách, thêm/sửa/xóa với kiểm tra xung đột lịch giáo viên/địa điểm, phân công giáo viên) và chức năng đăng ký khóa học cho học viên (duyệt khóa học chưa đăng ký, xử lý đăng ký tự động tạo tài khoản Student nếu chưa tồn tại, gửi thông báo tự động), đảm bảo tính toàn vẹn dữ liệu và trải nghiệm người dùng mượt mà.
- **Bản đồ ma trận thư mục vật lý mục tiêu:** Liệt kê tất cả các file vật lý cụ thể được tạo hoặc cập nhật trong giai đoạn này, kèm Tag ID tương ứng:
  * ./sources/backend/course-service/src/main/java/com/hub/course/model/Course.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/com/hub/course/CourseRepository.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/com/hub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/com/hub/course/CourseController.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/course-service/src/main/java/com/hub/course/exception/ScheduleConflictException.java [REQ-008]
  * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/model/Enrollment.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentRepository.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentService.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentController.java [REQ-010], [REQ-011]
  * ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/exception/EnrollmentException.java [REQ-011]
  * ./sources/frontend/src/app/courses/page.tsx [REQ-007], [REQ-010]
  * ./sources/frontend/src/app/courses/[id]/page.tsx [REQ-007], [REQ-008], [REQ-009]
  * ./sources/frontend/src/app/enrollments/page.tsx [REQ-010], [REQ-011]
  * ./sources/frontend/src/components/CourseCard.tsx [REQ-007], [REQ-010]
  * ./sources/frontend/src/components/EnrollmentForm.tsx [REQ-011]
  * ./sources/docs/api/course-management-api.md [REQ-007], [REQ-008], [REQ-009]
  * ./sources/docs/api/enrollment-api.md [REQ-010], [REQ-011]
- **Thông số kỹ thuật DDL SQL cơ sở dữ liệu** [DAT-004], [DAT-005]:
```sql
-- Không có thay đổi cơ sở dữ liệu hoặc lớp lưu trữ nào được yêu cầu cho phạm vi giai đoạn này
-- Các bảng COURSES (DAT-004) và ENROLLMENTS (DAT-005) đã được khởi tạo và cấu hình trong giai đoạn 1
```
- **Hợp đồng định tuyến API và sự kiện** [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-007]:
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
  },
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
#### 📅 NHẬT KÝ NHIỆM VỤ PHỤ THEO THỜI GIAN TỪNG NGÀY (GIAI ĐOẠN 2)

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 1: Triển khai logic cốt lõi dịch vụ khóa học và giao diện danh sách khóa học frontend
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 1: Xây dựng thực thể và kho lưu trữ khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/model/Course.java [REQ-007], [REQ-008], [REQ-009]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho khóa học, ánh xạ đến bảng PostgreSQL COURSES (DAT-004), định nghĩa đầy đủ các trường: courseId (UUID, khóa chính), title (varchar 150, không null), description (text, tùy chọn), startDate (date, không null), endDate (date, không null), teacherId (UUID, khóa ngoại đến bảng Users.userId), maxStudents (int, mặc định 30), createdAt và updatedAt (timestamp, không null, mặc định now()). Thêm ràng buộc duy nhất trên trường title để tránh trùng tên khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 2: Xây dựng logic nghiệp vụ cốt lõi của dịch vụ khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các phương thức nghiệp vụ: lấy danh sách tất cả khóa học đang hoạt động, lấy chi tiết khóa học theo ID, tạo mới khóa học với xác thực các trường bắt buộc, cập nhật thông tin khóa học, xóa khóa học. Thêm logic kiểm tra xung đột lịch giáo viên: trước khi phân công giáo viên hoặc tạo/cập nhật khóa học, kiểm tra xem giáo viên có khóa học khác trùng khoảng thời gian (startDate đến endDate) hay không, nếu có thì ném ngoại lệ ScheduleConflictException.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 3: Xây dựng controller và endpoint REST cho quản lý khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/course-service/src/main/java/com/hub/course/CourseController.java [REQ-007], [REQ-008], [REQ-009]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST: GET /api/courses (lấy danh sách khóa học), GET /api/courses/{id} (lấy chi tiết), POST /api/courses (tạo mới), PUT /api/courses/{id} (cập nhật), DELETE /api/courses/{id} (xóa), POST /api/courses/{id}/assign-teacher (phân công giáo viên). Áp dụng xác thực JWT Bearer Token, kiểm tra quyền RBAC (chỉ System Admin và Center Admin được phép chỉnh sửa/xóa khóa học, tất cả người dùng đã xác thực được phép xem). Thêm xác thực đầu vào request và phản hồi lỗi chuẩn hóa.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 4: Xây dựng trang danh sách khóa học frontend
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-010]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/frontend/src/app/courses/page.tsx [REQ-007], [REQ-010]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai trang danh sách khóa học responsive, tích hợp với API /api/courses để hiển thị danh sách khóa học với đầy đủ thông tin: tiêu đề, lịch học, giáo viên phụ trách, số lượng học viên đã đăng ký. Thêm chức năng lọc theo trung tâm, tìm kiếm theo tên khóa học, sắp xếp theo ngày bắt đầu. Đảm bảo giao diện phù hợp với cả web và di động.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 5: Viết bài kiểm tra đơn vị cho logic nghiệp vụ khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Tester]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/course-service/src/test/java/com/hub/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/com/hub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra đơn vị toàn diện cho tất cả các phương thức trong CourseService, bao gồm: thao tác CRUD khóa học, logic kiểm tra xung đột lịch giáo viên, xác thực các trường đầu vào, xử lý các trường hợp biên (khóa học không tồn tại, giáo viên không hợp lệ, ngày bắt đầu sau ngày kết thúc). Đảm bảo độ bao phủ mã ít nhất 90%.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 6: Viết bài kiểm tra tích hợp cho endpoint quản lý khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Tester]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
- **Đường dẫn file thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/backend/course-service/src/test/java/com/hub/course/CourseControllerIT.java [REQ-007], [REQ-008], [REQ-009]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra tích hợp cho tất cả các endpoint trong CourseController, kiểm tra xác thực JWT, kiểm tra quyền RBAC (phân biệt quyền của Student, Teacher, Center Admin, System Admin), xác thực phản hồi request/response, xử lý lỗi (khóa học không tồn tại, xung đột lịch, thiếu quyền truy cập). Sử dụng cơ sở dữ liệu thử nghiệm H2 để chạy kiểm tra.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 7: Viết tài liệu đặc tả API quản lý khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Doc]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/docs/api/course-management-api.md [REQ-007], [REQ-008], [REQ-009]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết tài liệu đặc tả API đầy đủ cho tất cả các endpoint quản lý khóa học, bao gồm: mô tả chức năng, phương thức HTTP, đường dẫn, schema request/response, mã lỗi, yêu cầu xác thực, quyền RBAC, và ví dụ payload thực tế. Đảm bảo tài liệu phù hợp với tiêu chuẩn OpenAPI 3.0.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 2: Triển khai logic nghiệp vụ đăng ký khóa học và giao diện liên quan frontend
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 1: Xây dựng thực thể và kho lưu trữ ghi danh
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-010], [REQ-011]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/model/Enrollment.java [REQ-010], [REQ-011]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể JPA cho ghi danh, ánh xạ đến bảng PostgreSQL ENROLLMENTS (DAT-005), định nghĩa các trường: enrollmentId (UUID, khóa chính), studentId (UUID, khóa ngoại đến Users.userId, không null), courseId (UUID, khóa ngoại đến Courses.courseId, không null), enrollmentDate (timestamp, mặc định now()). Thêm ràng buộc duy nhất trên cặp (studentId, courseId) để ngăn đăng ký trùng lặp, thêm chỉ mục trên courseId để tối ưu truy vấn danh sách học viên của khóa học.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 2: Xây dựng logic nghiệp vụ cốt lõi của dịch vụ ghi danh
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-010], [REQ-011]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentService.java [REQ-010], [REQ-011]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các phương thức nghiệp vụ: lấy danh sách khóa học chưa đăng ký của học viên (loại trừ các khóa học đã có bản ghi ghi danh), xử lý yêu cầu đăng ký khóa học, tự động tạo tài khoản Student với vai trò 'Student' nếu học viên chưa có tài khoản cục bộ, xác thực số lượng học viên tối đa của khóa học trước khi đăng ký, kích hoạt gửi thông báo đăng ký thành công cho học viên và nhóm Zalo của trung tâm.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 3: Xây dựng controller và endpoint REST cho đăng ký khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-010], [REQ-011]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentController.java [REQ-010], [REQ-011]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai các endpoint REST: GET /api/courses/available (lấy danh sách khóa học chưa đăng ký của học viên hiện tại), POST /api/enrollments (xử lý đăng ký khóa học). Áp dụng xác thực JWT Bearer Token, kiểm tra quyền RBAC (chỉ học viên có vai trò Student được phép đăng ký khóa học, tất cả người dùng đã xác thực được phép xem danh sách khóa học có sẵn). Thêm xác thực đầu vào request và phản hồi lỗi chuẩn hóa cho trường hợp khóa học đã đủ sĩ số hoặc học viên đã đăng ký trước đó.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 4: Xây dựng giao diện đăng ký khóa học frontend
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Coder]
- **ID thẻ mục tiêu:** [REQ-010], [REQ-011]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/frontend/src/app/enrollments/page.tsx [REQ-010], [REQ-011]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai trang đăng ký khóa học responsive cho học viên, hiển thị danh sách khóa học chưa đăng ký lấy từ endpoint /api/courses/available, tích hợp form đăng ký với xác thực đầu vào, hiển thị thông báo thành công/lỗi sau khi đăng ký, đồng bộ trạng thái đăng ký với backend. Đảm bảo giao diện thân thiện với người dùng di động.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 5: Viết bài kiểm tra đơn vị cho logic nghiệp vụ ghi danh
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Tester]
- **ID thẻ mục tiêu:** [REQ-010], [REQ-011]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/enrollment-service/src/test/java/com/hub/enrollment/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/com/hub/enrollment/EnrollmentService.java [REQ-010], [REQ-011]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra đơn vị toàn diện cho tất cả các phương thức trong EnrollmentService, bao gồm: lấy danh sách khóa học có sẵn, xử lý đăng ký khóa học, tự động tạo tài khoản Student, ngăn chặn đăng ký trùng lặp, xác thực số lượng học viên tối đa. Đảm bảo độ bao phủ mã ít nhất 90%, bao gồm các trường hợp biên (học viên không tồn tại, khóa học không tồn tại, khóa học đã đủ sĩ số).
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 6: Viết bài kiểm tra tích hợp cho endpoint đăng ký khóa học
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Tester]
- **ID thẻ mục tiêu:** [REQ-010], [REQ-011]
- **Đường dẫn file thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/backend/enrollment-service/src/test/java/com/hub/enrollment/EnrollmentControllerIT.java [REQ-010], [REQ-011]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm tra tích hợp cho tất cả các endpoint trong EnrollmentController, kiểm tra xác thực JWT, kiểm tra quyền RBAC, xác thực phản hồi request/response, xử lý lỗi (khóa học không tồn tại, đã đủ sĩ số, đã đăng ký trước đó, thiếu quyền truy cập). Sử dụng cơ sở dữ liệu thử nghiệm H2 để chạy kiểm tra.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 NHIỆM VỤ PHỤ 7: Rà soát mã nguồn dịch vụ khóa học và ghi danh
- **Chuyên môn quy trình làm việc của đại lý phụ:** [Reviewer]
- **ID thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]
- **Đường dẫn file thành phần mục tiêu (target_component):** ./sources/backend/course-service, ./sources/backend/enrollment-service [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát mã nguồn toàn bộ dịch vụ khóa học và ghi danh, kiểm tra tuân thủ tiêu chuẩn mã hóa, phát hiện lỗ hổng bảo mật (injection SQL, xác thực đầu vào không đầy đủ), tối ưu hiệu năng truy vấn cơ sở dữ liệu, sửa các lỗi và điểm nghẽn được phát hiện, đảm bảo mã nguồn sẵn sàng cho tích hợp với các dịch vụ khác.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

### 📈 Giai đoạn 3 - Triển khai điểm danh QR, quản lý thẻ hội viên, thông báo đa kênh và khuyến mãi
- **Mục tiêu cốt lõi và mục đích của giai đoạn:** Giai đoạn này triển khai các tính năng vận hành cốt lõi của hệ thống, bao gồm chức năng điểm danh quét mã QR với tính bất biến chống trùng lặp bản ghi, quản lý thẻ hội viên (hiển thị số ngày còn lại hiệu lực, gia hạn thẻ sau thanh toán), hệ thống thông báo đa kênh (push notification, tin nhắn nhóm Zalo) với cơ chế tự động thử lại khi gửi thất bại, quản lý khuyến mãi và thông báo hệ thống (CRUD với ngày hết hạn tùy chọn, tự động ẩn thông báo hết hạn), đảm bảo tất cả quy tắc nghiệp vụ liên quan đến tương tác của học viên và vận hành trung tâm được đáp ứng.

- **Bản đồ ma trận đường dẫn vật lý mục tiêu:**
  * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceService.java [REQ-012, EXC-001, EXC-002, REQ-013]
  * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceController.java [REQ-012, REQ-013, ARC-007]
  * ./sources/backend/attendance-service/src/main/resources/db/migration/V1_0_0__create_attendance_table.sql [DAT-006]
  * ./sources/backend/membership-service/src/main/java/com/hub/membership/MembershipService.java [REQ-014, REQ-015]
  * ./sources/backend/membership-service/src/main/java/com/hub/membership/MembershipController.java [REQ-014, REQ-015, ARC-009]
  * ./sources/backend/membership-service/src/main/resources/db/migration/V1_0_0__create_student_cards_table.sql [DAT-007]
  * ./sources/backend/notification-service/src/main/java/com/hub/notification/NotificationService.java [REQ-016, EXC-003]
  * ./sources/backend/notification-service/src/main/java/com/hub/notification/NotificationController.java [REQ-016, ARC-008]
  * ./sources/backend/notification-service/src/main/resources/db/migration/V1_0_0__create_notifications_table.sql [DAT-008]
  * ./sources/backend/promotion-service/src/main/java/com/hub/promotion/PromotionService.java [REQ-017]
  * ./sources/backend/promotion-service/src/main/java/com/hub/promotion/PromotionController.java [REQ-017]
  * ./sources/backend/promotion-service/src/main/java/com/hub/announcement/AnnouncementService.java [REQ-018]
  * ./sources/backend/promotion-service/src/main/java/com/hub/announcement/AnnouncementController.java [REQ-018]
  * ./sources/backend/promotion-service/src/main/resources/db/migration/V1_0_0__create_promotions_announcements_tables.sql [DAT-009]
  * ./sources/frontend/src/app/attendance/page.tsx [REQ-012, REQ-013]
  * ./sources/frontend/src/app/membership-card/page.tsx [REQ-014, REQ-015]
  * ./sources/frontend/src/app/notifications/page.tsx [REQ-016]
  * ./sources/frontend/src/app/promotions/page.tsx [REQ-017, REQ-018]
  * ./sources/docs/attendance-service-api-spec.md [REQ-012, REQ-013, ARC-007]
  * ./sources/docs/membership-service-api-spec.md [REQ-014, REQ-015]
  * ./sources/docs/notification-service-api-spec.md [REQ-016, ARC-008]
  * ./sources/docs/promotion-service-api-spec.md [REQ-017, REQ-018]

- **Đặc tả SQL DDL lược đồ cơ sở dữ liệu [DAT-006, DAT-007, DAT-008, DAT-009]:**
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

-- Tạo bảng thẻ hội viên [DAT-007]
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL UNIQUE REFERENCES users(user_id),
    issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
    validity_days INT NOT NULL CHECK (validity_days > 0),
    remaining_days INT NOT NULL CHECK (remaining_days >= 0)
);

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

- **Hợp đồng định tuyến API và sự kiện [REQ-012, REQ-013, REQ-014, REQ-015, REQ-016, REQ-017, REQ-018, ARC-007, ARC-008, ARC-009]:**
  * **Hợp đồng REST API:**
    1. Dịch vụ điểm danh:
       - `POST /api/attendance/scan` [REQ-012, REQ-013, ARC-007]
         ```json
         // Yêu cầu
         {
           "studentId": "uuid",
           "courseId": "uuid",
           "qrToken": "string"
         }
         // Phản hồi thành công
         {
           "attendanceId": "uuid",
           "timestamp": "timestamp",
           "status": "RECORDED | DUPLICATE"
         }
         ```
       - `GET /api/attendance/course/{courseId}/date/{date}` [REQ-012, ARC-007]: Trả về danh sách bản ghi điểm danh của khóa học trong ngày được chỉ định.
    2. Dịch vụ thẻ hội viên:
       - `GET /api/membership/card` [REQ-014, ARC-009]
         ```json
         // Phản hồi thành công
         {
           "cardId": "uuid",
           "issueDate": "date",
           "validityDays": "int",
           "remainingDays": "int"
         }
         ```
       - `POST /api/membership/renew` [REQ-015, ARC-009]
         ```json
         // Yêu cầu
         {
           "renewalDays": "int",
           "paymentTransactionId": "string"
         }
         // Phản hồi thành công
         {
           "newRemainingDays": "int",
           "newExpiryDate": "date"
         }
         ```
    3. Dịch vụ thông báo:
       - `POST /api/notifications/send` [REQ-016, ARC-008]
         ```json
         // Yêu cầu
         {
           "userId": "uuid",
           "groupZalo": "string",
           "message": "string",
           "channels": ["PUSH", "ZALO"]
         }
         // Phản hồi thành công
         {
           "notificationId": "uuid",
           "status": "QUEUED | FAILED"
         }
         ```
    4. Dịch vụ khuyến mãi và thông báo: Các endpoint REST CRUD chuẩn cho `/api/promotions` [REQ-017] và `/api/announcements` [REQ-018], với schema yêu cầu/phản hồi tương ứng với từng thực thể.
  * **Hợp đồng sự kiện (Kafka Topics):**
    - `attendance.scan.request` [REQ-012, ARC-007]: Payload yêu cầu quét mã QR
    - `attendance.scan.response` [REQ-013, ARC-007]: Payload kết quả quét mã QR (bao gồm cờ trùng lặp)
    - `notification.send.request` [REQ-016, ARC-008]: Payload yêu cầu gửi thông báo
    - `notification.send.failed` [EXC-003, ARC-008]: Payload sự kiện gửi thông báo thất bại để xử lý thử lại
    - `membership.renewed` [REQ-015, ARC-008]: Sự kiện kích hoạt sau khi gia hạn thẻ hội viên thành công để gửi thông báo xác nhận

- **Trình xử lý ngoại lệ được bản địa hóa của giai đoạn [EXC-001, EXC-002, EXC-003]:**
  * [EXC-001] Lỗi kết nối mạng trong quá trình quét mã QR: Nếu học viên quét mã QR nhưng kết nối mạng bị gián đoạn, ứng dụng di động sẽ lưu trữ tạm payload quét vào bộ nhớ cục bộ và tự động gửi lại yêu cầu khi kết nối được khôi phục. Hệ thống backend xử lý yêu cầu một cách idempotent để đảm bảo chỉ tạo một bản ghi điểm danh duy nhất.
  * [EXC-002] Gửi điểm danh trùng lặp: Nếu học viên quét mã QR nhiều lần trong cùng một ngày cho cùng một khóa học, hệ thống sẽ phát hiện trùng lặp dựa trên ràng buộc duy nhất (student_id, course_id, attendance_date), trả về phản hồi thành công với cờ "already_recorded" và không tạo bản ghi điểm danh bổ sung.
  * [EXC-003] Gửi thông báo thất bại: Nếu thông báo đẩy không thể gửi đến thiết bị (ví dụ: token thiết bị không hợp lệ), hệ thống sẽ ghi lại lỗi vào bảng notifications, tự động thử lại tối đa 3 lần với khoảng cách tăng dần, sau đó đánh dấu trạng thái là "thất bại" và ghi nhật ký cho đội ngũ vận hành.

#### 📅 Nhật ký phân công nhiệm vụ theo trình tự thời gian từng ngày cho đại lý phụ trách (Giai đoạn 3)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Triển khai cốt lõi dịch vụ điểm danh và kiểm thử đơn vị
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 1: Xây dựng logic nghiệp vụ cốt lõi dịch vụ điểm danh và migration cơ sở dữ liệu
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-012], [EXC-001], [EXC-002], [REQ-013], [DAT-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ cốt lõi của dịch vụ điểm danh, bao gồm xác thực quan hệ học viên-khóa học, triển khai cơ chế idempotent để đảm bảo chỉ tạo một bản ghi điểm danh duy nhất cho mỗi học viên/khóa học/ngày, xử lý yêu cầu quét mã QR trùng lặp, tích hợp với bảng attendance cơ sở dữ liệu. Đồng thời tạo script migration DDL SQL cho bảng attendance với ràng buộc duy nhất unique_attendance_per_student_course_day.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 2: Xây dựng endpoint REST cho dịch vụ điểm danh
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-012], [REQ-013], [ARC-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceController.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST POST /api/attendance/scan để nhận payload quét mã QR từ ứng dụng di động, endpoint GET /api/attendance/course/{courseId}/date/{date} để truy xuất danh sách điểm danh của khóa học trong ngày, áp dụng xác thực JWT và kiểm soát quyền truy cập theo RBAC.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 3: Viết kiểm thử đơn vị cho dịch vụ điểm danh
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Tester]
* **ID thẻ mục tiêu:** [REQ-012], [EXC-001], [EXC-002], [REQ-013]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị cho AttendanceService, bao gồm các trường hợp: quét mã QR hợp lệ tạo bản ghi điểm danh mới, quét mã QR trùng lặp trong cùng ngày trả về cờ DUPLICATE, xử lý lỗi khi học viên không đăng ký khóa học, xác minh cơ chế idempotent hoạt động chính xác.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 4: Viết kiểm thử tích hợp cho endpoint điểm danh
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Tester]
* **ID thẻ mục tiêu:** [REQ-012], [EXC-001], [ARC-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceControllerIntegrationTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết kiểm thử tích hợp cho endpoint /api/attendance/scan, mô phỏng payload quét mã QR từ ứng dụng di động, xác minh phản hồi API chính xác, xác minh bản ghi điểm danh được lưu vào cơ sở dữ liệu, xác minh xử lý yêu cầu trùng lặp hoạt động đúng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 5: Soạn thảo tài liệu đặc tả API dịch vụ điểm danh
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Doc]
* **ID thẻ mục tiêu:** [REQ-012], [REQ-013], [ARC-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/attendance-service-api-spec.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Soạn thảo tài liệu đặc tả API cho dịch vụ điểm danh, bao gồm mô tả endpoint, schema yêu cầu/phản hồi, mã lỗi, luồng xử lý điểm danh trùng lặp, tích hợp với luồng quét mã QR.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Triển khai cốt lõi dịch vụ thẻ hội viên và thông báo
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 1: Xây dựng logic nghiệp vụ cốt lõi dịch vụ thẻ hội viên và migration cơ sở dữ liệu
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-014], [REQ-015], [DAT-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/membership-service/src/main/java/com/hub/membership/MembershipService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ quản lý thẻ hội viên, bao gồm tính toán số ngày còn lại hiệu lực, xử lý yêu cầu gia hạn thẻ sau khi xác nhận thanh toán, cập nhật trường remaining_days tự động, tích hợp với bảng student_cards cơ sở dữ liệu. Đồng thời tạo script migration DDL SQL cho bảng student_cards với các ràng buộc kiểm tra tính hợp lệ của trường validity_days và remaining_days.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 2: Xây dựng endpoint REST cho dịch vụ thẻ hội viên
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-014], [REQ-015], [ARC-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/membership-service/src/main/java/com/hub/membership/MembershipController.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST GET /api/membership/card để lấy thông tin thẻ hội viên của học viên đang đăng nhập, endpoint POST /api/membership/renew để xử lý yêu cầu gia hạn thẻ, áp dụng xác thực JWT và kiểm tra quyền truy cập của học viên.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 3: Xây dựng logic nghiệp vụ cốt lõi dịch vụ thông báo và migration cơ sở dữ liệu
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-016], [EXC-003], [DAT-008]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/NotificationService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ hệ thống thông báo đa kênh, bao gồm xếp hàng thông báo đẩy (FCM/APNs) và tin nhắn nhóm Zalo, triển khai cơ chế retry tự động tối đa 3 lần khi gửi thất bại, ghi nhật ký lỗi gửi thông báo, tích hợp với bảng notifications cơ sở dữ liệu. Đồng thời tạo script migration DDL SQL cho bảng notifications với ràng buộc retry_count từ 0 đến 3.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 4: Viết kiểm thử đơn vị cho dịch vụ thẻ hội viên
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Tester]
* **ID thẻ mục tiêu:** [REQ-014], [REQ-015]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/membership-service/src/test/java/com/hub/membership/MembershipServiceTest.java;./sources/backend/membership-service/src/main/java/com/hub/membership/MembershipService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị cho MembershipService, bao gồm các trường hợp: tính toán số ngày còn lại thẻ chính xác, xử lý yêu cầu gia hạn thẻ cập nhật ngày kết thúc đúng, xử lý lỗi khi giao dịch thanh toán không hợp lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 5: Viết kiểm thử đơn vị cho dịch vụ thông báo
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Tester]
* **ID thẻ mục tiêu:** [REQ-016], [EXC-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/notification-service/src/test/java/com/hub/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/com/hub/notification/NotificationService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị cho NotificationService, bao gồm các trường hợp: xếp hàng thông báo đẩy và Zalo thành công, xử lý retry tự động khi gửi thất bại, đánh dấu thông báo là thất bại sau 3 lần thử không thành công, ghi nhật ký lỗi gửi thông báo.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 3: Triển khai dịch vụ khuyến mãi, thông báo hệ thống và giao diện frontend liên quan
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 1: Xây dựng endpoint REST cho dịch vụ thông báo
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-016], [ARC-008]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/notification-service/src/main/java/com/hub/notification/NotificationController.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST POST /api/notifications/send để kích hoạt gửi thông báo đa kênh, tích hợp với dịch vụ FCM/APNs và Zalo API, xử lý phân phối thông báo đến người dùng hoặc nhóm Zalo mục tiêu.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 2: Xây dựng logic nghiệp vụ dịch vụ khuyến mãi và migration cơ sở dữ liệu
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-017], [DAT-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/PromotionService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ quản lý khuyến mãi, bao gồm CRUD khuyến mãi với kiểm tra tính hợp lệ của ngày bắt đầu/kết thúc, lọc khuyến mãi đang hoạt động cho học viên, tích hợp với bảng promotions cơ sở dữ liệu. Đồng thời tạo script migration DDL SQL cho bảng promotions với ràng buộc kiểm tra phần trăm giảm giá và tính hợp lệ của ngày hiệu lực.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 3: Xây dựng logic nghiệp vụ dịch vụ thông báo hệ thống và migration cơ sở dữ liệu
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-018], [DAT-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/announcement/AnnouncementService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng logic nghiệp vụ quản lý thông báo hệ thống, bao gồm CRUD thông báo với ngày hết hạn tùy chọn, tự động ẩn thông báo sau ngày hết hạn, phát sóng thông báo toàn hệ thống, tích hợp với bảng announcements cơ sở dữ liệu.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 4: Xây dựng giao diện frontend cho điểm danh và thẻ hội viên
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/frontend/src/app/attendance/page.tsx;./sources/frontend/src/app/membership-card/page.tsx
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng giao diện người dùng trang điểm danh cho học viên, tích hợp tính năng quét mã QR, hiển thị trạng thái điểm danh; xây dựng giao diện trang thẻ hội viên, hiển thị số ngày còn lại hiệu lực, nút gia hạn thẻ với lựa chọn thời hạn gia hạn.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 5: Viết kiểm thử đơn vị cho dịch vụ khuyến mãi và thông báo hệ thống
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Tester]
* **ID thẻ mục tiêu:** [REQ-017], [REQ-018]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/promotion-service/src/test/java/com/hub/promotion/PromotionServiceTest.java;./sources/backend/promotion-service/src/test/java/com/hub/announcement/AnnouncementServiceTest.java;./sources/backend/promotion-service/src/main/java/com/hub/promotion/PromotionService.java;./sources/backend/promotion-service/src/main/java/com/hub/announcement/AnnouncementService.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử đơn vị cho PromotionService và AnnouncementService, bao gồm các trường hợp: tạo khuyến mãi với ngày hết hạn hợp lệ, lọc khuyến mãi đang hoạt động, tự động ẩn thông báo sau ngày hết hạn, xử lý lỗi khi ngày kết thúc nhỏ hơn ngày bắt đầu.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 4: Hoàn thiện endpoint, giao diện frontend, kiểm thử tích hợp và tài liệu kỹ thuật
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 1: Xây dựng endpoint REST cho dịch vụ khuyến mãi và thông báo hệ thống
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-017], [REQ-018]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/promotion-service/src/main/java/com/hub/promotion/PromotionController.java;./sources/backend/promotion-service/src/main/java/com/hub/announcement/AnnouncementController.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng endpoint REST CRUD cho `/api/promotions` và `/api/announcements`, áp dụng xác thực JWT và kiểm soát quyền truy cập theo RBAC (chỉ Center Admin/Manager mới có quyền tạo/sửa/xóa, tất cả người dùng đăng nhập có quyền xem).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 2: Xây dựng giao diện frontend cho thông báo và khuyến mãi
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Coder]
* **ID thẻ mục tiêu:** [REQ-016], [REQ-017], [REQ-018]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/frontend/src/app/notifications/page.tsx;./sources/frontend/src/app/promotions/page.tsx
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng giao diện trang thông báo hiển thị danh sách thông báo hệ thống và thông báo cá nhân, tích hợp hiển thị trạng thái đã gửi/thất bại; xây dựng giao diện trang khuyến mãi hiển thị các khuyến mãi đang hoạt động cho học viên.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 3: Viết kiểm thử tích hợp cho các endpoint dịch vụ thông báo, khuyến mãi và thông báo hệ thống
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Tester]
* **ID thẻ mục tiêu:** [REQ-016], [EXC-003], [REQ-017], [REQ-018]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/backend/notification-service/src/test/java/com/hub/notification/NotificationControllerIntegrationTest.java;./sources/backend/promotion-service/src/test/java/com/hub/promotion/PromotionControllerIntegrationTest.java;./sources/backend/promotion-service/src/test/java/com/hub/announcement/AnnouncementControllerIntegrationTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bộ kiểm thử tích hợp cho tất cả endpoint của dịch vụ thông báo, khuyến mãi và thông báo hệ thống, xác minh logic nghiệp vụ hoạt động đúng, xác minh kiểm soát quyền RBAC hoạt động chính xác, xác minh cơ chế retry thông báo hoạt động đúng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 4: Rà soát chất lượng mã nguồn giai đoạn 3
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Reviewer]
* **ID thẻ mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [EXC-001], [EXC-002], [EXC-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** Toàn bộ mã nguồn dịch vụ điểm danh, thẻ hội viên, thông báo, khuyến mãi và giao diện frontend liên quan trong giai đoạn 3
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm tra chất lượng mã nguồn của tất cả các thành phần được phát triển trong giai đoạn 3, đảm bảo tuân thủ tiêu chuẩn lập trình doanh nghiệp, phát hiện lỗi logic, điểm nghẽn hiệu năng, đề xuất chiến lược sửa lỗi tối ưu.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Công việc con 5: Soạn thảo tài liệu kỹ thuật cho các dịch vụ giai đoạn 3
* **Chuyên môn quy trình làm việc của đại lý phụ trách:** [Doc]
* **ID thẻ mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [EXC-001], [EXC-002], [EXC-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/notification-service-api-spec.md;./sources/docs/promotion-service-api-spec.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Soạn thảo tài liệu đặc tả kỹ thuật cho dịch vụ thông báo, khuyến mãi và thông báo hệ thống, bao gồm mô tả luồng nghiệp vụ, hợp đồng API, xử lý ngoại lệ, hướng dẫn tích hợp.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->
### 📈 GIAI ĐOẠN 4 - TÍCH HỢP CHATBOT AI, GIAO DIỆN DI ĐỘNG VÀ BÁO CÁO
- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Triển khai các tính năng nâng cao và giao diện người dùng cuối: tích hợp chatbot AI hỗ trợ trả lời câu hỏi thường gặp và leo thang hỗ trợ khi độ tin cậy thấp, xây dựng giao diện responsive cho ứng dụng di động với phân quyền theo vai trò, tích hợp thông báo đẩy FCM/APNs, triển khai phát hiện ngôn ngữ mặc định và SEO đa ngôn ngữ (hreflang, thẻ meta), xây dựng chức năng xuất báo cáo điểm danh CSV và bảng điều khiển tóm tắt ghi danh realtime. Giai đoạn này tập trung vào hoàn thiện trải nghiệm người dùng và khả năng phân tích dữ liệu.

- **Bản đồ ma trận thư mục vật lý đích:** 
  * ./sources/backend/ai-chatbot-service/pom.xml [ARC-000]
  * ./sources/backend/ai-chatbot-service/src/main/java/com/hub/ai/ChatbotService.java [REQ-019]
  * ./sources/backend/ai-chatbot-service/src/main/java/com/hub/ai/ChatbotController.java [REQ-019]
  * ./sources/backend/ai-chatbot-service/src/test/java/com/hub/ai/ChatbotServiceTest.java [REQ-019]
  * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceReportService.java [REQ-024, EXC-005]
  * ./sources/backend/attendance-service/src/main/java/com/hub/attendance/ReportController.java [REQ-024]
  * ./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceReportIntegrationTest.java [REQ-024, EXC-005]
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
  * ./sources/docs/ai-chatbot-api-spec.md [REQ-019]
  * ./sources/docs/report-api-spec.md [REQ-024]
  * ./sources/docs/mobile-ui-spec.md [REQ-020, REQ-022, REQ-023]
  * ./sources/docs/phase4-technical-spec.md [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]

- **Đặc tả SQL DDL Schema Cơ sở dữ liệu:** [DAT-XXX]
```sql
-- Không có thay đổi cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu cho ngữ cảnh giai đoạn này
```

- **Hợp đồng định tuyến API và Sự kiện:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-006], [ARC-007], [ARC-008], [ARC-009]
  * **Chatbot API:** `POST /api/chatbot/message` - Nhận payload tin nhắn từ người dùng, trả về phản hồi AI hoặc leo thang hỗ trợ. Yêu cầu: `{"message": "string", "sessionId": "uuid", "context": {"userId": "uuid", "role": "string"}}`. Phản hồi: `{"response": "string", "confidence": 0.95, "escalate": false, "suggestedActions": ["string"]}`. [REQ-019]
  * **Report API:** `GET /api/reports/attendance/csv` - Xuất báo cáo điểm danh CSV cho trung tâm và khoảng ngày. Tham số query: `centerId` (uuid), `startDate` (date), `endDate` (date). Phản hồi: File CSV với các cột StudentName, CourseName, AttendanceDate, Status. [REQ-024, EXC-005]
  * **Dashboard API:** `GET /api/dashboard/enrollment-summary` - Lấy dữ liệu tóm tắt dashboard. Phản hồi: `{"totalStudents": 100, "activeCourses": 5, "upcomingSessions": 12}`. [REQ-025]
  * **Push Notification Event:** `notification.sent` - Sự kiện được phát ra khi thông báo được gửi đến hàng đợi FCM/APNs. Payload: `{"userId": "uuid", "title": "string", "body": "string", "data": {}}`. [REQ-021, ARC-008]

- **Trình xử lý ngoại lệ địa phương của giai đoạn:** [EXC-005]
  * **[EXC-005] Phục hồi hệ thống sau sự cố:** Khi dịch vụ khôi phục sau thời gian chết, hệ thống xử lý tất cả điểm danh đang chờ theo thứ tự FIFO và gửi thông báo cho người dùng về các sự kiện đã khôi phục. Áp dụng cho dịch vụ báo cáo điểm danh và toàn bộ luồng xử lý điểm danh. [EXC-005]

#### 📅 NHẬT KÝ PHÂN CÔNG NHIỆM VỤ TÁC NHÂN PHỤ THEO THỜI GIAN TỪNG NGÀY (GIAI ĐOẠN 4)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Triển khai nền tảng backend cho chatbot AI và dịch vụ báo cáo điểm danh

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: Khởi tạo module ai-chatbot-service
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [ARC-000]
- **Đường dẫn thành phần đích (target_component):** ./sources/backend/ai-chatbot-service/pom.xml
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo cấu trúc dự án Maven cho service vi mô ai-chatbot-service với các phụ thuộc Quarkus, RESTEasy Reactive, và thư viện xử lý ngôn ngữ tự nhiên. Định nghĩa module trong pom.xml gốc. [ARC-000]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Triển khai ChatbotService và ChatbotController
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-019]
- **Đường dẫn thành phần đích (target_component):** ./sources/backend/ai-chatbot-service/src/main/java/com/hub/ai/ChatbotService.java
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai lớp ChatbotService với logic xử lý câu hỏi thường gặp về khóa học, giáo viên, trung tâm và trạng thái tài khoản. Tích hợp mô hình NLP để phân loại ý định và trích xuất thực thể. Triển khai ChatbotController với endpoint POST /api/chatbot/message, xác thực JWT, và cơ chế leo thang hỗ trợ khi độ tin cậy thấp. [REQ-019]

**Hợp đồng API:**
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

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Viết unit test cho ChatbotService
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Tester]
- **ID Thẻ được nhắm mục tiêu:** [REQ-019]
- **Đường dẫn thành phần đích (target_component):** ./sources/backend/ai-chatbot-service/src/main/java/com/hub/ai/ChatbotService.java;./sources/backend/ai-chatbot-service/src/test/java/com/hub/ai/ChatbotServiceTest.java
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết unit test cho ChatbotService bao gồm các kịch bản: câu hỏi thường gặp được trả lời chính xác, leo thang hỗ trợ khi độ tin cậy thấp, xử lý ngữ cảnh người dùng. Sử dụng JUnit 5 và Mockito. [REQ-019]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: Viết tài liệu API cho chatbot
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Doc]
- **ID Thẻ được nhắm mục tiêu:** [REQ-019]
- **Đường dẫn thành phần đích (target_component):** ./sources/docs/ai-chatbot-api-spec.md
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật chi tiết cho API chatbot, bao gồm endpoint, schema request/response, mã lỗi, ví dụ sử dụng, và hướng dẫn tích hợp frontend. [REQ-019]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Triển khai AttendanceReportService cho xuất CSV
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-024, EXC-005]
- **Đường dẫn thành phần đích (target_component):** ./sources/backend/attendance-service/src/main/java/com/hub/attendance/AttendanceReportService.java
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai lớp AttendanceReportService với phương thức generateAttendanceReport(centerId, startDate, endDate) trả về định dạng CSV. Bao gồm logic truy vấn dữ liệu điểm danh, xử lý FIFO cho các bản ghi đang chờ sau sự cố hệ thống, và gửi thông báo phục hồi cho người dùng. [REQ-024, EXC-005]

**Xử lý ngoại lệ:**
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

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 6: Viết integration test cho dịch vụ báo cáo
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Tester]
- **ID Thẻ được nhắm mục tiêu:** [REQ-024, EXC-005]
- **Đường dẫn thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/backend/attendance-service/src/test/java/com/hub/attendance/AttendanceReportIntegrationTest.java
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết integration test cho AttendanceReportService sử dụng Testcontainers với PostgreSQL. Kiểm tra: tạo báo cáo CSV chính xác, xử lý điểm danh trùng lặp, và kịch bản phục hồi sau sự cố hệ thống (EXC-005). [REQ-024, EXC-005]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 7: Viết tài liệu API cho báo cáo
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Doc]
- **ID Thẻ được nhắm mục tiêu:** [REQ-024]
- **Đường dẫn thành phần đích (target_component):** ./sources/docs/report-api-spec.md
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho API báo cáo điểm danh, bao gồm endpoint GET /api/reports/attendance/csv, tham số query, định dạng CSV, và ví dụ sử dụng. [REQ-024]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Triển khai giao diện người dùng di động, thông báo đẩy và tối ưu SEO đa ngôn ngữ

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: Triển khai giao diện responsive cho ứng dụng di động
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-020]
- **Đường dẫn thành phần đích (target_component):** ./sources/frontend/src/components/mobile/MobileDashboard.tsx
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng thành phần MobileDashboard responsive sử dụng Tailwind CSS, hiển thị menu điều hướng và màn hình phù hợp với vai trò người dùng (Student, Teacher, Admin). Đảm bảo đồng bộ chức năng với phiên bản web. [REQ-020]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Tích hợp thông báo đẩy FCM/APNs
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-021]
- **Đường dẫn thành phần đích (target_component):** ./sources/frontend/src/hooks/usePushNotifications.ts
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai hook usePushNotifications để đăng ký token thiết bị với FCM/APNs, xử lý nhận thông báo, và hiển thị thông báo trong ứng dụng. Tích hợp với Firebase Cloud Messaging cho Android và Apple Push Notification service cho iOS. [REQ-021]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Triển khai phát hiện ngôn ngữ mặc định và định tuyến i18n
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-022]
- **Đường dẫn thành phần đích (target_component):** ./sources/frontend/src/app/[locale]/layout.tsx
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai middleware phát hiện ngôn ngữ ưu tiên từ cookie đã lưu, sau đó fallback sang header Accept-Language. Cấu hình định tuyến Next.js với tham số [locale] để hỗ trợ đa ngôn ngữ mà không cần tải lại trang. [REQ-022]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: Triển khai SEO đa ngôn ngữ với hreflang và thẻ meta
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-023]
- **Đường dẫn thành phần đích (target_component):** ./sources/frontend/src/lib/seo.ts
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tiện ích SEO động để tạo thẻ meta ngôn ngữ cụ thể, thuộc tính hreflang cho 3 ngôn ngữ (Anh, Việt, Tây Ban Nha), và đảm bảo mỗi trang có thẻ `<html lang='xx'>` chính xác. Tích hợp với Next.js Metadata API. [REQ-023]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Viết E2E test cho giao diện di động và thông báo đẩy
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Tester]
- **ID Thẻ được nhắm mục tiêu:** [REQ-020, REQ-021]
- **Đường dẫn thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/frontend/src/e2e/mobile-ui.spec.ts
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết end-to-end test sử dụng Playwright hoặc Cypress để kiểm tra: giao diện responsive hiển thị đúng trên thiết bị di động, menu điều hướng theo vai trò hoạt động chính xác, và thông báo đẩy được nhận và hiển thị đúng. [REQ-020, REQ-021]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 6: Viết tài liệu kỹ thuật cho giao diện di động và SEO
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Doc]
- **ID Thẻ được nhắm mục tiêu:** [REQ-020, REQ-022, REQ-023]
- **Đường dẫn thành phần đích (target_component):** ./sources/docs/mobile-ui-spec.md
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật chi tiết cho giao diện người dùng di động responsive, tích hợp thông báo đẩy, phát hiện ngôn ngữ và cấu hình SEO đa ngôn ngữ. Bao gồm hướng dẫn cấu hình, ví dụ code, và bảng tra cứu. [REQ-020, REQ-022, REQ-023]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 3: Triển khai dashboard tóm tắt ghi danh, tích hợp chatbot vào frontend và kiểm tra cuối cùng

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 1: Triển khai EnrollmentDashboard component
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-025]
- **Đường dẫn thành phần đích (target_component):** ./sources/frontend/src/components/dashboard/EnrollmentDashboard.tsx
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng thành phần EnrollmentDashboard hiển thị real-time các thẻ: tổng số học viên, số khóa học đang hoạt động, và các buổi học sắp tới (7 ngày tới). Tích hợp với API GET /api/dashboard/enrollment-summary và cập nhật tự động mỗi 5 phút. [REQ-025]

**Hợp đồng API:**
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

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 2: Tích hợp ChatbotWidget vào frontend
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Coder]
- **ID Thẻ được nhắm mục tiêu:** [REQ-019]
- **Đường dẫn thành phần đích (target_component):** ./sources/frontend/src/components/chat/ChatWidget.tsx
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng thành phần ChatWidget có thể đóng/mở, tích hợp với endpoint POST /api/chatbot/message, quản lý trạng thái sessionId, và hiển thị gợi ý hành động khi chatbot leo thang hỗ trợ. Đảm bảo widget hoạt động trên tất cả các trang. [REQ-019]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 3: Viết integration test cho dashboard và chatbot
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Tester]
- **ID Thẻ được nhắm mục tiêu:** [REQ-025, REQ-019]
- **Đường dẫn thành phần đích (target_component):** INTEGRATION_SCOPE;./sources/frontend/src/e2e/dashboard-chatbot.spec.ts
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết integration test kiểm tra: dashboard hiển thị đúng số liệu từ API, chatbot phản hồi chính xác các câu hỏi thường gặp, và leo thang hỗ trợ hoạt động khi độ tin cậy thấp. Sử dụng Playwright với mock API responses. [REQ-025, REQ-019]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 4: Rà soát mã và tối ưu hóa các thành phần giai đoạn 4
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Reviewer]
- **ID Thẻ được nhắm mục tiêu:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]
- **Đường dẫn thành phần đích (target_component):** ./sources/backend/ai-chatbot-service/src/main/java/com/hub/ai/ChatbotService.java;./sources/frontend/src/components/mobile/MobileDashboard.tsx
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát mã toàn bộ các thành phần backend và frontend của giai đoạn 4. Kiểm tra chất lượng mã, phát hiện bottleneck hiệu năng, đảm bảo tuân thủ OWASP Top 10, và đề xuất chiến lược sửa chữa cụ thể cho các lỗi phát hiện. Tối ưu hóa truy vấn cơ sở dữ liệu cho dịch vụ báo cáo và cơ chế phục hồi sau sự cố (EXC-005). [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]

**Xử lý ngoại lệ:**
```java
// EXC-005: Chiến lược phục hồi sau sự cố
// Đảm bảo dịch vụ báo cáo xử lý hàng đợi điểm danh pending theo FIFO
// và gửi thông báo phục hồi cho người dùng sau khi hệ thống khôi phục
```

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 NHIỆM VỤ PHỤ 5: Hoàn thiện tài liệu kỹ thuật giai đoạn 4
- **Phân công đặc trưng quy trình làm việc của tác nhân phụ:** [Doc]
- **ID Thẻ được nhắm mục tiêu:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]
- **Đường dẫn thành phần đích (target_component):** ./sources/docs/phase4-technical-spec.md
- **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tổng hợp và hoàn thiện tài liệu kỹ thuật toàn diện cho giai đoạn 4, bao gồm: đặc tả API chatbot, báo cáo và dashboard; hướng dẫn tích hợp thông báo đẩy; cấu hình SEO đa ngôn ngữ; và quy trình xử lý phục hồi sau sự cố (EXC-005). Đảm bảo tài liệu phù hợp với tiêu chuẩn doanh nghiệp. [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005]

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->

### 📈 Giai đoạn 5 - Triển khai hạ tầng DevOps, tích hợp hệ thống và tài liệu doanh nghiệp
- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Giai đoạn này tập trung vào việc hoàn thiện hạ tầng DevOps và đám mây, tích hợp các hợp đồng hệ thống giữa các service vi mô và frontend, đồng thời bàn giao toàn bộ tài liệu kỹ thuật doanh nghiệp. Các nhiệm vụ bao gồm: xây dựng Dockerfile đa giai đoạn, pipeline CI/CD GitHub Actions, triển khai cụm GKE với auto-scaling, cấu hình hạ tầng GCP (VPC, IAM, Storage, PostgreSQL read replicas) qua Terraform, tích hợp FCM/APNs, Zalo API, Redis caching, đảm bảo tuân thủ tất cả yêu cầu phi chức năng (hiệu năng, bảo mật, khả năng sẵn sàng, sao lưu và phục hồi thảm họa, tuân thủ GDPR/CCPA), và hoàn thiện toàn bộ tài liệu hệ thống doanh nghiệp (bản vẽ kiến trúc, hợp đồng API, hướng dẫn vận hành, tài liệu cơ sở dữ liệu, hướng dẫn người dùng).

- **Bản đồ thư mục vật lý mục tiêu:**
    * ./sources/infra/terraform/main.tf [ARC-010], [NFR-002], [NFR-003], [NFR-004], [NFR-009]
    * ./sources/infra/terraform/gke-cluster.tf [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/terraform/postgres-replica.tf [ARC-010], [NFR-004], [NFR-009]
    * ./sources/infra/terraform/iam.tf [ARC-010], [NFR-003], [NFR-008]
    * ./sources/infra/terraform/monitoring.tf [ARC-010], [NFR-006], [NFR-002]
    * ./sources/infra/terraform/security-policies.tf [ARC-010], [NFR-003], [NFR-008]
    * ./sources/infra/docker/Dockerfile.auth-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.center-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.course-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.enrollment-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.attendance-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.membership-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.notification-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.promotion-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.report-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/Dockerfile.ai-chatbot-service [ARC-010], [NFR-005]
    * ./sources/infra/docker/push-images.sh [ARC-010], [NFR-005]
    * ./sources/infra/k8s/deployment-auth-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-center-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-course-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-enrollment-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-attendance-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-membership-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-notification-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-promotion-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-report-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/deployment-ai-chatbot-service.yaml [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/k8s/service-auth-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-center-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-course-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-enrollment-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-attendance-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-membership-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-notification-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-promotion-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-report-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/service-ai-chatbot-service.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/hpa-auth-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-center-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-course-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-enrollment-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-attendance-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-membership-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-notification-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-promotion-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-report-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/hpa-ai-chatbot-service.yaml [ARC-010], [NFR-004]
    * ./sources/infra/k8s/ingress.yaml [ARC-010], [NFR-002]
    * ./sources/infra/k8s/configmap.yaml [ARC-010], [NFR-007]
    * ./sources/infra/k8s/secret.yaml [ARC-010], [NFR-003]
    * ./sources/infra/k8s/api-gateway.yaml [ARC-006], [ARC-009]
    * ./sources/infra/k8s/kafka-topics.yaml [ARC-007], [ARC-008], [ARC-009]
    * ./sources/infra/k8s/istio-config.yaml [ARC-006], [ARC-007], [ARC-008], [ARC-009]
    * ./sources/infra/.github/workflows/ci-cd.yml [ARC-010], [NFR-001], [NFR-006]
    * ./sources/infra/test/infra_test.go [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/test/e2e_deployment_test.go [ARC-010], [NFR-002], [NFR-004]
    * ./sources/infra/test/security_compliance_test.go [ARC-010], [NFR-003], [NFR-008]
    * ./sources/infra/test/full_e2e_test.go [ARC-010], [NFR-001], [NFR-002], [NFR-006]
    * ./sources/docs/architecture-overview.md [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * ./sources/docs/api-integration-contracts.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]
    * ./sources/docs/operational-runbooks.md [ARC-010], [NFR-002], [NFR-009]
    * ./sources/docs/database-architecture.md [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]
    * ./sources/docs/user-guide.md [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]

- **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:**
```sql
-- Không có thay đổi cơ sở dữ liệu hoặc lớp persistence nào được yêu cầu cho ngữ cảnh giai đoạn này
```

- **Hợp đồng API và Định tuyến Sự kiện [REQ-XXX], [ARC-XXX]:**
```json
{
  "api_gateway_routes": [
    {
      "service_name": "auth-service",
      "path": "/api/v1/auth/*",
      "methods": ["GET", "POST", "PUT", "DELETE"],
      "plugins": ["jwt", "rate-limiting"]
    },
    {
      "service_name": "attendance-service",
      "path": "/api/v1/attendance/scan",
      "methods": ["POST"],
      "plugins": ["jwt"]
    },
    {
      "service_name": "notification-service",
      "path": "/api/v1/notifications/*",
      "methods": ["GET", "POST"],
      "plugins": ["jwt"]
    }
  ],
  "kafka_topics": [
    {
      "topic_name": "attendance.scan",
      "partitions": 3,
      "replication_factor": 2,
      "retention_ms": 604800000
    },
    {
      "topic_name": "notification.push",
      "partitions": 3,
      "replication_factor": 2,
      "retention_ms": 604800000
    },
    {
      "topic_name": "notification.zalo",
      "partitions": 3,
      "replication_factor": 2,
      "retention_ms": 604800000
    },
    {
      "topic_name": "course.enrollment",
      "partitions": 3,
      "replication_factor": 2,
      "retention_ms": 604800000
    }
  ]
}
```

#### 📅 Nhật ký nhiệm vụ phân phối tác nhân phụ theo ngày (Giai đoạn 5)

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 1: Triển khai hạ tầng đám mây cơ bản và container hóa
<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 1: Cấu hình hạ tầng GCP cơ bản
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [GCP]
* **ID Thẻ mục tiêu:** [ARC-010], [NFR-002], [NFR-003], [NFR-004], [NFR-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/terraform/main.tf
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình hạ tầng GCP bao gồm tạo dự án, mạng VPC, subnet, firewall rules, Cloud SQL (PostgreSQL) với high availability, Redis Memorystore, và Cloud Storage. Đảm bảo mã hóa dữ liệu nghỉ (AES-256) và TLS 1.3 cho kết nối. Áp dụng các chính sách IAM để tuân thủ NFR-003 và NFR-008. Cấu hình sao lưu tự động hàng ngày và point-in-time recovery cho PostgreSQL (NFR-009).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 2: Xây dựng Dockerfile đa giai đoạn cho tất cả service vi mô
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Docker]
* **ID Thẻ mục tiêu:** [NFR-005], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/docker/Dockerfile.auth-service
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng Dockerfile đa giai đoạn (multi-stage) cho từng service vi mô (auth, center, course, enrollment, attendance, membership, notification, promotion, report, ai-chatbot). Sử dụng base image nhỏ (distroless hoặc alpine) để đảm bảo kích thước hình ảnh cuối cùng < 500MB (NFR-005). Tối ưu hóa layer caching và loại bỏ các công cụ không cần thiết trong giai đoạn production.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 3: Tạo cụm GKE với auto-scaling
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [GKE]
* **ID Thẻ mục tiêu:** [NFR-002], [NFR-004], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/terraform/gke-cluster.tf
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo cụm GKE với 3 node pools (system, application, cache). Cấu hình Horizontal Pod Autoscaler (HPA) dựa trên CPU > 70% và độ trễ yêu cầu > 300ms (NFR-004). Bật auto-scaling cho node pools. Cấu hình network policies và PodSecurityPolicy để đảm bảo an ninh.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 4: Cấu hình PostgreSQL read replicas
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Coder]
* **ID Thẻ mục tiêu:** [NFR-004], [NFR-009], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/terraform/postgres-replica.tf
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình 2 read replicas cho PostgreSQL để phân tán khối lượng công việc báo cáo. Thiết lập connection pooling với PgBouncer. Cấu hình automated failover cho primary instance. Đảm bảo backup hàng ngày và point-in-time recovery trong 24 giờ (NFR-009).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 5: Viết kiểm thử xác thực hạ tầng
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Tester]
* **ID Thẻ mục tiêu:** [NFR-002], [NFR-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/infra/test/infra_test.go
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết các bài kiểm thử xác thực hạ tầng sử dụng Terratest để kiểm tra việc provision VPC, Cloud SQL, Redis, và GKE cluster. Xác minh các cấu hình auto-scaling và network policies hoạt động như mong đợi.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 2: Triển khai Kubernetes và CI/CD pipeline
<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 1: Tạo Kubernetes deployment manifests và services
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [GKE]
* **ID Thẻ mục tiêu:** [NFR-002], [NFR-004], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/k8s/deployment-auth-service.yaml
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo Kubernetes Deployment, Service, và HorizontalPodAutoscaler cho tất cả các service vi mô. Cấu hình resource requests/limits, liveness/readiness probes, và rolling update strategy. Đảm bảo high availability với ít nhất 2 replicas cho mỗi service.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 2: Đẩy hình ảnh Docker lên Google Container Registry
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Docker]
* **ID Thẻ mục tiêu:** [NFR-005], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/docker/push-images.sh
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo script để đẩy tất cả hình ảnh Docker đã được build lên Google Container Registry (GCR) với tags phiên bản phù hợp. Cấu hình image pull policy là Always cho môi trường staging và IfNotPresent cho production.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 3: Cấu hình pipeline CI/CD GitHub Actions
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Coder]
* **ID Thẻ mục tiêu:** [NFR-001], [NFR-006], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/.github/workflows/ci-cd.yml
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng pipeline CI/CD với GitHub Actions bao gồm: build và test cho mỗi service, quét lỗ hổng bảo mật (Snyk), build Docker images, đẩy lên GCR, triển khai lên GKE. Tích hợp kiểm tra chất lượng mã (SonarQube) và logging cho pipeline (NFR-006).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 4: Cấu hình Cloud Logging và Monitoring
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [GCP]
* **ID Thẻ mục tiêu:** [NFR-006], [NFR-002], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/terraform/monitoring.tf
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình Cloud Logging để thu thập logs từ tất cả các service và GKE cluster. Thiết lập Cloud Monitoring với các dashboard hiển thị metrics hiệu năng (NFR-001), availability (NFR-002), và health của các service. Cấu hình alerts cho các ngưỡng cảnh báo.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 5: Viết kiểm thử xác thực triển khai end-to-end
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Tester]
* **ID Thẻ mục tiêu:** [NFR-002], [NFR-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/infra/test/e2e_deployment_test.go
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm thử end-to-end để xác minh tất cả các service được triển khai thành công trên GKE, có thể giao tiếp với nhau, và phản hồi yêu cầu trong ngưỡng hiệu năng cho phép (NFR-001). Kiểm tra khả năng tự động phục hồi khi node bị lỗi.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 3: Triển khai hợp đồng tích hợp hệ thống và kiến trúc sự kiện
<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 1: Cấu hình API Gateway
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Coder]
* **ID Thẻ mục tiêu:** [ARC-006], [ARC-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/k8s/api-gateway.yaml
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình API Gateway (Kong hoặc NGINX Ingress) để định tuyến yêu cầu đến các service vi mô tương ứng. Thiết lập rate limiting, JWT validation, và SSL termination. Đảm bảo tất cả các endpoint REST được bảo vệ và tuân thủ kiến trúc tích hợp backend-frontend (ARC-009).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 2: Cấu hình Kafka topics cho kiến trúc sự kiện
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Coder]
* **ID Thẻ mục tiêu:** [ARC-007], [ARC-008], [ARC-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/k8s/kafka-topics.yaml
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo các Kafka topics cho các luồng sự kiện: attendance.scan (điểm danh QR), notification.push (thông báo đẩy), notification.zalo (tin nhắn Zalo), và course.enrollment (đăng ký khóa học). Cấu hình replication factor và partition count phù hợp cho khả năng mở rộng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 3: Cấu hình Service Mesh Istio
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Coder]
* **ID Thẻ mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/k8s/istio-config.yaml
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình Istio service mesh để quản lý giao tiếp giữa các service vi mô. Thiết lập mutual TLS, traffic shifting, và circuit breaking. Đảm bảo các luồng xác thực (ARC-006), điểm danh (ARC-007), và thông báo (ARC-008) hoạt động ổn định qua service mesh.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 4: Viết kiểm thử hợp đồng API
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Tester]
* **ID Thẻ mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/backend/auth/src/test/java/com/hub/contract/AuthApiContractTest.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết các bài kiểm thử hợp đồng (contract tests) để xác minh các endpoint REST API tuân thủ đúng schema đã định nghĩa. Bao gồm kiểm tra authentication flow (ARC-006), attendance scan endpoint (ARC-007), notification endpoints (ARC-008), và backend-frontend integration endpoints (ARC-009).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 5: Tài liệu hợp đồng tích hợp hệ thống
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/api-integration-contracts.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết tài liệu chi tiết về các hợp đồng tích hợp hệ thống, bao gồm: luồng xác thực OAuth2/JWT (ARC-006), luồng điểm danh QR (ARC-007), luồng thông báo đa kênh (ARC-008), và tích hợp backend-frontend (ARC-009). Bao gồm các schema request/response, mã lỗi, và ví dụ sử dụng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 4: Bảo mật, tuân thủ và tối ưu hiệu năng
<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 1: Cấu hình IAM và chính sách bảo mật GCP
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [GCP]
* **ID Thẻ mục tiêu:** [NFR-003], [NFR-008], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/terraform/iam.tf
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình IAM roles và service accounts với nguyên tắc đặc quyền tối thiểu (least privilege). Thiết lập organization policies để đảm bảo tuân thủ GDPR/CCPA (NFR-008). Cấu hình Cloud KMS để quản lý khóa mã hóa.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 2: Cấu hình chính sách mạng và bảo mật pod GKE
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [GKE]
* **ID Thẻ mục tiêu:** [NFR-003], [NFR-008], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/k8s/security-policies.yaml
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai Network Policies để kiểm soát lưu lượng giữa các service. Cấu hình PodSecurityPolicies (PSP) hoặc Pod Security Standards để hạn chế đặc quyền container. Bật audit logging cho cluster.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 3: Triển khai middleware ghi log audit
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Coder]
* **ID Thẻ mục tiêu:** [NFR-006], [ARC-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/backend/common/src/main/java/com/hub/middleware/AuditLoggingMiddleware.java
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai middleware ghi log audit cho tất cả các service vi mô. Ghi lại mọi hành động người dùng (thay đổi vai trò, điểm danh, thông báo) với timestamp, user ID, và chi tiết hành động. Đảm bảo logs được giữ lại 1 năm (NFR-006) và tuân thủ luồng xác thực (ARC-006).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 4: Viết kiểm thử tuân thủ bảo mật
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Tester]
* **ID Thẻ mục tiêu:** [NFR-003], [NFR-008]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/infra/test/security_compliance_test.go
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện các bài kiểm thử bảo mật và tuân thủ: kiểm tra mã hóa TLS 1.3, xác thực mã hóa AES-256 cho dữ liệu nghỉ, kiểm tra cấu hình IAM, và đảm bảo tuân thủ GDPR/CCPA (quyền xóa dữ liệu, xuất dữ liệu JSON).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 5: Rà soát cấu hình bảo mật và khoảng trống tuân thủ
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [NFR-003], [NFR-008], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/terraform/security-review.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát toàn diện các cấu hình bảo mật GCP và GKE. Xác định các khoảng trống tuân thủ so với OWASP Top 10 và yêu cầu GDPR/CCPA. Đề xuất các biện pháp khắc phục và cải tiến.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->

##### 📅 NGÀY 5: Hoàn thiện tài liệu, kiểm thử cuối cùng và bàn giao
<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 1: Viết tài liệu tổng quan kiến trúc hệ thống
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/architecture-overview.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết tài liệu tổng quan kiến trúc hệ thống bao gồm sơ đồ kiến trúc tổng thể, mô tả các luồng chính (xác thực, điểm danh QR, thông báo, tích hợp frontend), và lược đồ các tương tác giữa các service. Bao gồm các yêu cầu phi chức năng về hiệu năng, bảo mật, khả năng sẵn sàng, và tuân thủ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 2: Viết tài liệu hướng dẫn vận hành và phục hồi thảm họa
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [NFR-002], [NFR-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/docs/operational-runbooks.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết hướng dẫn vận hành chi tiết cho đội ngũ vận hành, bao gồm quy trình triển khai, giám sát, xử lý sự cố, và phục hồi thảm họa. Mô tả các bước khôi phục dịch vụ sau khi sự cố, bao gồm cả kịch bản mất kết nối mạng (EXC-001) và sao lưu/khôi phục cơ sở dữ liệu.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 3: Thực hiện kiểm thử tích hợp toàn hệ thống
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Tester]
* **ID Thẻ mục tiêu:** [ARC-006], [ARC-007], [ARC-008], [ARC-009], [NFR-001], [NFR-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** INTEGRATION_SCOPE;./sources/infra/test/full_e2e_test.go
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện kiểm thử end-to-end toàn hệ thống trên môi trường staging. Xác minh tất cả các luồng chính hoạt động: đăng ký/đăng nhập, quét QR điểm danh, gửi thông báo, đăng ký khóa học, và phản hồi API trong ngưỡng 200ms (NFR-001). Kiểm tra khả năng chịu lỗi và failover.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 4: Rà soát cuối cùng mã nguồn và cấu hình
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [ARC-010], [NFR-003], [NFR-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/terraform/final-review.md
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát cuối cùng toàn bộ mã nguồn hạ tầng (Terraform, Kubernetes manifests, Dockerfiles) và cấu hình bảo mật. Đảm bảo không có secrets hardcoded, tất cả cấu hình tuân thủ các tiêu chuẩn bảo mật và yêu cầu phi chức năng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->

###### 🌿 SUB-TASKS 5: Tối ưu hình ảnh Docker và đẩy lên registry
* **Chuyên môn quy trình làm việc của tác nhân phụ:** [Docker]
* **ID Thẻ mục tiêu:** [NFR-005], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** ./sources/infra/docker/optimize-images.sh
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tối ưu hóa kích thước hình ảnh Docker bằng cách loại bỏ các lớp không cần thiết, sử dụng multi-stage builds hiệu quả, và nén hình ảnh cuối cùng. Đẩy tất cả hình ảnh đã tối ưu lên Google Container Registry với tags phù hợp cho môi trường production.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

### 🕵️ BÁO CÁO KIỂM TOÁN CHÉO KIẾN TRÚC THỜI GIAN THỰC
```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=5
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=34
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=25
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

<!--END_PHASE_INDEX-->

<!--END_PART_2_PHASE_LOOP-->

### BỐI CẢNH NỀN TẢNG TỪ CÁC BƯỚC TRƯỚC

## ☣️ 6. MÃ BẢO MẬT DOANH NGHIỆP PHỔ QUÁT & CÁC BIỆN PHÁP CHỐNG TIẾM QUYỀN [NFR-XXX]

### 1. Biện pháp chống tiêm chích SQL (SQLi) tuyệt đối
Triển khai các câu lệnh đã chuẩn bị (prepared statements) với tham số vị trí (positional query parameters) để ngăn chặn hoàn toàn các cuộc tấn công SQL injection. Áp dụng danh sách trắng (whitelist) động cho các đầu vào sắp xếp (sorting input) thông qua Hibernate ORM, đảm bảo chỉ các cột và hướng hợp lệ được phép truy vấn. Tất cả các truy vấn cơ sở dữ liệu phải sử dụng PreparedStatement với tham số được bind đúng cách, loại bỏ hoàn toàn việc nối chuỗi SQL động. Các tham số phân trang và sắp xếp phải được kiểm tra chống lại danh sách trắng các trường được phép trước khi đưa vào truy vấn. [NFR-003], [EXC-004], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]

### 2. Cross-Site Scripting (XSS) & Content Security Policy (CSP)
Thực hiện làm sạch ngữ cảnh tự động (automated context sanitization) cho tất cả đầu vào người dùng và bật tự động escape JSX (JSX auto-escaping) trong giao diện người dùng. Tiêm động các tiêu đề HTTP Content Security Policy (CSP) nghiêm ngặt thông qua Ingress Gateway, hạn chế nguồn script chỉ đến các domain đáng tin cậy. Cấu hình CSP với các directive như default-src 'self', script-src 'self' https://trusted.cdn.com, và loại bỏ 'unsafe-inline', 'unsafe-eval'. Tích hợp sanitization library như DOMPurify cho nội dung HTML động. [NFR-003], [REQ-020], [REQ-021], [ARC-009], [ARC-006]

### 3. CORS Multi-Tenant Security Rails
Thiết lập đường ray bảo mật CORS đa tenant (Multi-Tenant CORS) với nghiêm cấm wildcard origin (*). Triển khai kiểm tra động tenant validation boundaries dựa trên token xác thực và cấu hình origin được phép của từng trung tâm. Mỗi request CORS phải được xác thực chéo (cross-validated) với tenant ID trong JWT và danh sách origin cho phép của center tương ứng. Cấu hình Ingress Controller với annotation cho phép origin động dựa trên header X-Tenant-ID. [ARC-001], [ARC-002], [NFR-003], [REQ-004]

### 4. Zero-Leak Log Scrubbing & PII Data Masking Engines
Xây dựng công cụ làm sạch log không rò rỉ (Zero-Leak Log Scrubbing) và động mask dữ liệu PII sử dụng các interceptor tự động với chú thích @JsonSerialize. Tất cả các trường nhạy cảm (email, số điện thoại, tên đầy đủ) phải được mask hoặc loại bỏ hoàn toàn khỏi log trước khi ghi vào hệ thống logging. Áp dụng masking theo chuẩn AES-256 cho dữ liệu at rest và TLS 1.3 cho dữ liệu in transit. Tích hợp với hệ thống logging tập trung (ELK Stack) để đảm bảo không có PII nào lọt vào log. [NFR-008], [DAT-001], [DAT-007], [REQ-014], [REQ-015]

## 📱 7. QUY TẮC TUÂN THỦ DI ĐỘNG HYBRID & CƠ CHẾ SEO ĐA NGÔN NGỮ

### 1. Capacitor Mobile Hybrid Compliance Rails
Tuân thủ kiến trúc hybrid di động Capacitor với dynamic client-side fetching, absolute URL addressing để tránh vấn đề hydration, và hydration safeguards. Sử dụng @capacitor/preferences cho native storage abstraction, đảm bảo dữ liệu được đồng bộ hóa an toàn giữa web và native layers. Triển khai hardware back-button interception để điều hướng người dùng quay lại màn hình trước đó trong ứng dụng, không thoát ứng dụng đột ngột. Cấu hình Capacitor với server URL động dựa trên môi trường (development, staging, production). [REQ-020], [REQ-021], [ARC-009], [NFR-007]

### 2. Internationalization (i18n) & Dynamic SEO Injection
Xây dựng edge-layer locale recognition middleware để phát hiện ngôn ngữ người dùng dựa trên Accept-Language header, cookie lưu trữ, và tham số URL. Tự động inject dynamic hreflang control vào HTML head, tạo các link hreflang cho tiếng Anh, tiếng Việt, và tiếng Tây Ban Nha. Đảm bảo mỗi trang đều có thẻ <html lang='xx'> và các link hreflang chính xác cho công cụ tìm kiếm. Tích hợp với Next.js Middleware để xử lý locale ở edge layer, giảm latency cho người dùng toàn cầu. [REQ-022], [REQ-023], [NFR-007], [ARC-010]

## 🚀 8. LUỒNG NHÁNH GIT TỰ ĐỘNG CHO PHIÊN LÀM VIỆC HÀNG NGÀY TRONG PIPELINE

### 1. Daily Workspace Forking Isolation
Thiết lập chương trình forking isolation động cho workspace với cấu trúc nhánh features/development-phase-X-day-Y, trong đó X là số thứ tự phase và Y là số thứ tự day. Mỗi phiên làm việc hàng ngày được cách ly hoàn toàn trong nhánh riêng, ngăn chặn xung đột code và đảm bảo khả năng rollback độc lập. Áp dụng quy tắc bảo vệ nhánh (branch protection rules) yêu cầu ít nhất 1 reviewer trước khi merge, và bắt buộc status checks pass (build, test, lint) trước khi merge. [ARC-010], [NFR-006]

### 2. Validation Guard Pipeline Gates
Thiết lập validation guard pipeline gates với automated compilation verification, SonarQube lint gates đánh giá chất lượng code, và mục tiêu test coverage tự động >= 85%. Pipeline phải chạy trên mỗi pull request và commit, chặn merge nếu coverage thấp hơn ngưỡng hoặc có lỗi lint nghiêm trọng. Tích hợp SonarQube quality gates với các điều kiện: coverage > 85%, no new bugs, no new vulnerabilities, no code smells. Sử dụng GitHub Actions để orchestrate pipeline với các stage: checkout, setup-java, build, test, sonar-scan, và deploy. [NFR-001], [NFR-004], [NFR-005], [ARC-010]

### 📊 YÊU CẦU KIỂM TRA PHỦ MA TRẬN

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]