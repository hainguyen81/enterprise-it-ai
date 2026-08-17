# BỐI CẢNH DỰ ÁN TOÀN CẦU: membership-hub

## 📊 KIỂM SOÁT TÀI LIỆU

| Mục | Chi tiết |
| :--- | :--- |
| **ID BẢN THẢO** | ARCH-20260817042313 |
| **Tên dự án** | membership-hub |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/17 04:23:13 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & CHẾ ĐỘ KIẾN TRÚC CỐT LÕI

### ⚙️ 1.1. Chế độ hệ thống cốt lõi & chế độ kiến trúc
- Hệ thống hoạt động theo mô hình đa trung tâm, hỗ trợ quản lý hội viên đồng thời cho nhiều đơn vị trung tâm giáo dục độc lập. [ARC-001, ARC-002]
- Kiến trúc phân tầng 3 lớp rõ ràng: lớp giao diện người dùng (Frontend Next.js/React Native), lớp xử lý nghiệp vụ (Backend Quarkus Java), lớp truy cập dữ liệu (PostgreSQL) và lớp hạ tầng (Docker, GKE, Google Cloud). [ARC-010]
- Tuân thủ mô hình RBAC (Kiểm soát truy cập dựa trên vai trò) với 5 vai trò người dùng được xác định rõ quyền hạn: System Admin, Center Admin, Manager, Teacher, Student. [ARC-001, ARC-002, ARC-003, ARC-004, ARC-005]
- Hệ thống xác thực người dùng hỗ trợ 3 phương thức: email/mật khẩu cục bộ, OAuth2 qua Firebase, OAuth2 qua Google/Facebook; sử dụng JWT access token (hết hạn 15 phút) và refresh token (hết hạn 7 ngày). [ARC-006]
- Tích hợp 2 kênh thông báo chính: push notification đa nền tảng qua FCM/APNs, đăng bài lên nhóm Zalo được chỉ định theo trung tâm. [ARC-008]
- Hỗ trợ bản địa hóa đa ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha) với cơ chế chuyển đổi ngôn ngữ không cần tải lại trang, tích hợp hỗ trợ SEO đa ngôn ngữ. [REQ-022, REQ-023]
- Tích hợp chatbot AI hỗ trợ giải đáp tự động thắc mắc của người dùng về khóa học, giáo viên, trung tâm và tình trạng tài khoản, chuyển tiếp cho hỗ trợ con người khi độ tin cậy thấp. [REQ-019]
- Hỗ trợ caching dữ liệu ngoại tuyến cho ứng dụng di động, đảm bảo trải nghiệm người dùng trong trường hợp mất kết nối mạng. [ARC-009]

### 🌊 1.2. Kiến trúc luồng dữ liệu doanh nghiệp & hệ sinh thái cốt lõi
- Luồng xác thực người dùng: Tiếp nhận thông tin đăng nhập cục bộ hoặc mã ủy quyền OAuth2 từ nhà cung cấp mạng xã hội, xác thực danh tính và cấp JWT token cho người dùng. [ARC-006]
- Luồng xử lý điểm danh QR: Ứng dụng di động quét mã QR của khóa học, gửi student ID và timestamp đến backend; dịch vụ xác thực ghi lại điểm danh với tính chất bất biến (chỉ tạo 1 bản ghi điểm danh mỗi học viên mỗi khóa học mỗi ngày, bỏ qua yêu cầu trùng lặp). [REQ-012, REQ-013, EXC-001, EXC-002]
- Luồng gửi thông báo: Kích hoạt tự động khi có sự kiện như tạo thông báo, phân công giáo viên vào khóa học, đăng ký khóa học mới; gửi push notification đến ứng dụng di động của người dùng và đăng bài lên nhóm Zalo tương ứng của trung tâm. [REQ-016, EXC-003]
- Luồng tích hợp frontend-backend: Frontend Next.js tiêu thụ REST API với xác thực bearer token; hỗ trợ caching dữ liệu ngoại tuyến cho trường hợp mất kết nối mạng, tự động đồng bộ dữ liệu khi kết nối được khôi phục. [ARC-009]
- Luồng quản lý thẻ hội viên: Tính toán tự động số ngày còn lại hiệu lực của thẻ hội viên, xử lý yêu cầu gia hạn thẻ khi người dùng thực hiện thanh toán thành công, cập nhật ngày hết hạn thẻ. [REQ-014, REQ-015]
- Luồng báo cáo & phân tích: Tổng hợp dữ liệu điểm danh, ghi danh, khóa học để tạo báo cáo điểm danh định dạng CSV và bảng điều khiển thống kê thời gian thực cho quản trị viên trung tâm. [REQ-024, REQ-025, EXC-005]
- Luồng xử lý ngoại lệ: Xử lý lỗi kết nối mạng trong quá trình quét QR điểm danh, lỗi gửi thông báo (lên lịch thử lại tối đa 3 lần trước khi đánh dấu thất bại), lỗi xung đột lịch giáo viên khi tạo khóa học. [EXC-001, EXC-002, EXC-003, EXC-005]

## 📁 2. PHỤ THUỘC NGĂN XẾP CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Hạ tầng lõi Backend:** [ARC-010]
  - Java 21 LTS (môi trường thực thi ứng dụng)
  - Quarkus 3.15.1 (framework microservice, tích hợp CDI cho dependency injection)
  - Hibernate ORM 6.4.4 (ORM truy cập cơ sở dữ liệu PostgreSQL)
  - PostgreSQL 16.x (cơ sở dữ liệu quan hệ chính lưu trữ dữ liệu người dùng, khóa học, điểm danh, thẻ hội viên)
  - Redis 7.2.x (lưu trữ session người dùng, caching dữ liệu ngoại tuyến cho ứng dụng di động)
  - Firebase Admin SDK 9.1.0 (xác thực người dùng, gửi push notification qua FCM)
  - Zalo API Official SDK (tích hợp gửi thông báo đến nhóm Zalo của trung tâm)
  - SmallRye JWT 3.15.1 (xử lý phát hành và xác thực JWT access token, refresh token)
  - GitHub Actions (CI/CD pipeline tự động hóa build, test, triển khai lên GKE)
- **Ngăn xếp UI & đa nền tảng:** [ARC-010]
  - Next.js 14.x (framework React cho frontend web, hỗ trợ SSR/SSG tối ưu SEO đa ngôn ngữ)
  - React 18.x (thư viện xây dựng giao diện người dùng động)
  - React Native 0.73.x (phát triển ứng dụng di động đa nền tảng Android/iOS, đồng bộ chức năng với web)
  - i18next 23.x (thư viện bản địa hóa đa ngôn ngữ, hỗ trợ chuyển đổi ngôn ngữ không tải lại trang)
  - Axios 1.6.x (thư viện gọi REST API từ frontend, hỗ trợ interceptor xác thực)
  - React Query 5.x (quản lý state client-side, caching dữ liệu, đồng bộ dữ liệu ngoại tuyến)

## 📁 3. RÀNG BUỘC BẢO VỆ TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP

### 🔑 3.1. Cơ sở bảo mật & tuân thủ [NFR-003, NFR-006, NFR-008]
- Mã hóa dữ liệu truyền tải bắt buộc sử dụng TLS 1.3 cho tất cả các kết nối API công khai và giao tiếp giữa các dịch vụ nội bộ. [NFR-003]
- Mã hóa dữ liệu lưu trữ sử dụng AES-256 cho cơ sở dữ liệu PostgreSQL và các dịch vụ lưu trữ đám mây Google Cloud. [NFR-003]
- JWT access token có thời hạn 15 phút, refresh token có thời hạn 7 ngày; triển khai cơ chế thu hồi token ngay lập tức khi người dùng đăng xuất hoặc bị thay đổi quyền hạn. [NFR-003]
- Tuân thủ đầy đủ OWASP Top 10: ngăn chặn SQL injection bằng prepared statements, chống XSS bằng cách lọc và mã hóa dữ liệu đầu vào, chống CSRF bằng token xác thực yêu cầu state-changing. [NFR-003]
- Tuân thủ GDPR/CCPA: hỗ trợ xóa dữ liệu cá nhân theo yêu cầu người dùng, xuất dữ liệu cá nhân ở định dạng JSON, quản lý sự đồng ý rõ ràng cho các thông báo tiếp thị. [NFR-008]
- Ghi log đầy đủ tất cả hành động người dùng quan trọng (thay đổi vai trò, ghi điểm danh, gửi thông báo, thay đổi khóa học) với timestamp, user ID và chi tiết hành động; lưu trữ log trong 1 năm để đáp ứng yêu cầu kiểm tra. [NFR-006]
- Quản lý quyền truy cập dựa trên vai trò (RBAC) được thực thi ở cả lớp backend và frontend, ngăn chặn truy cập trái phép vào tài nguyên hệ thống thông qua kiểm tra quyền trên mỗi yêu cầu API. [ARC-001, ARC-002, ARC-003, ARC-004, ARC-005]

### 🌐 3.2. Ràng buộc hạ tầng & hiệu suất [NFR-001, NFR-002, NFR-004, NFR-005, NFR-007]
- Độ trễ trung bình của các API cốt lõi (xác thực, ghi điểm danh, danh sách khóa học) không vượt quá 200ms. [NFR-001]
- Hệ thống đạt mức sẵn sàng 99.9% hàng năm, hỗ trợ chuyển đổi tự động giữa các cụm GKE khi có sự cố hạ tầng. [NFR-002]
- Hỗ trợ mở rộng ngang dịch vụ Quarkus thông qua Kubernetes HPA, kích hoạt tự động khi CPU sử dụng >70% hoặc độ trễ yêu cầu >300ms. [NFR-004]
- Cơ sở dữ liệu PostgreSQL được cấu hình với 1 read replica dành riêng cho khối lượng công việc báo cáo, giảm tải cho cơ sở dữ liệu chính xử lý giao dịch. [NFR-004]
- Kích thước hình ảnh Docker cơ sở <200MB, hình ảnh cuối cùng của dịch vụ <500MB, tối ưu hóa bằng cách sử dụng multi-stage build. [NFR-005]
- Redis được cấu hình chính sách xóa cache LRU (Least Recently Used) với thời gian sống mặc định 1 giờ cho dữ liệu session người dùng. [NFR-001]
- Hệ thống hỗ trợ tối đa 10.000 người dùng đồng thời với thời gian phản hồi truy vấn cơ sở dữ liệu dưới 1 giây nhờ chỉ mục được tối ưu hóa trên các trường thường xuyên truy vấn. [NFR-001]

### 🥞 3.3. MA TRẬN NGĂN XẾP KIẾN TRÚC
```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 🏁 4. TỔNG QUAN KIẾN TRÚC ĐA GIAI ĐOẠN CẤP CAO
### 📦 4.1. DANH SÁCH CÔNG VIỆC SẢN PHẨM KIẾN TRÚC CHÍNH
<!--START_BACKLOG_SYNOPSIS_GRID-->
Hệ thống membership-hub là nền tảng quản lý hội viên đa trung tâm được xây dựng trên kiến trúc microservice với backend Java/Quarkus, cơ sở dữ liệu PostgreSQL, triển khai trên GKE, tích hợp Firebase Authentication, FCM/APNs cho thông báo đẩy, Zalo API và Redis caching. Luồng dữ liệu chính bao gồm xác thực người dùng qua OAuth2/JWT, quét mã QR điểm danh idempotent, quản lý đăng ký khóa học, quản lý thẻ hội viên và gửi thông báo đa kênh. Hệ thống tuân thủ RBAC với 5 vai trò người dùng, đáp ứng các yêu cầu phi chức năng về hiệu suất, khả năng mở rộng, bảo mật và tuân thủ GDPR/CCPA.

### [MA TRẬN SỐ HỌC HỆ THỐNG]
> - **Tổng số thẻ [REQ]:** 25 Thẻ
> - **Tổng số thẻ [EXC]:** 5 Thẻ
> - **Tổng số thẻ [ARC]:** 10 Thẻ
> - **Tổng số thẻ [DAT]:** 11 Thẻ
> - **Tổng số thẻ [NFR]:** 9 Thẻ
> - ➡️ **Tổng số thẻ SRS:** 58 Thẻ

| No. | Công việc | Mục đích kỹ thuật / Tóm tắt sản phẩm | Loại | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Triển khai chức năng đăng ký người dùng qua email và mật khẩu | Triển khai logic đăng ký, xác thực đầu vào, tạo bản ghi người dùng với vai trò mặc định, trả về JWT token | Mã ứng dụng | [REQ-001], [EXC-004] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 2 | Triển khai xác thực người dùng qua mạng xã hội | Tích hợp OAuth2 với Firebase, Google, Facebook, xử lý mã xác thực, tạo/cập nhật bản ghi người dùng, cấp JWT token | Mã ứng dụng | [REQ-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 3 | Triển khai chức năng phân quyền người dùng | Xây dựng API gán/thay đổi vai trò người dùng, cập nhật quyền truy cập tức thì | Mã ứng dụng | [REQ-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 4 | Triển khai chức năng xem danh sách trung tâm | Xây dựng API trả về danh sách trung tâm với địa chỉ, mã số thuế, thông tin liên hệ quản trị | Mã ứng dụng | [REQ-004] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 5 | Triển khai chức năng quản lý trung tâm (CRUD) | Xây dựng API tạo, cập nhật, xóa bản ghi trung tâm, xử lý lỗi trùng lặp mã số thuế | Mã ứng dụng | [REQ-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 6 | Triển khai chức năng phân quyền quản trị trung tâm | Xây dựng API gán/thu hồi quyền quản trị trung tâm cho người dùng, cập nhật vai trò và liên kết trung tâm | Mã ứng dụng | [REQ-006] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 7 | Triển khai chức năng xem danh sách khóa học | Xây dựng API trả về danh sách khóa học với lịch học và thông tin giáo viên được phân công | Mã ứng dụng | [REQ-007] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 8 | Triển khai chức năng quản lý khóa học (CRUD) | Xây dựng API tạo, cập nhật, xóa khóa học, tích hợp kiểm tra xung đột lịch học giáo viên và địa điểm | Mã ứng dụng | [REQ-008] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 9 | Triển khai chức năng phân công giáo viên vào khóa học | Xây dựng API gán/thu hồi giáo viên cho khóa học, xếp hàng gửi thông báo cho giáo viên | Mã ứng dụng | [REQ-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 10 | Triển khai chức năng duyệt khóa học cho học viên | Xây dựng API trả về danh sách khóa học chưa đăng ký của học viên, hiển thị sức chứa và lịch học | Mã ứng dụng | [REQ-010] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 11 | Triển khai chức năng đăng ký khóa học học viên | Xây dựng API đăng ký khóa học, tự động tạo tài khoản học viên nếu chưa tồn tại, tạo bản ghi ghi danh, xếp hàng gửi thông báo | Mã ứng dụng | [REQ-011] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 12 | Triển khai chức năng quét mã QR điểm danh | Xây dựng API nhận payload quét QR, xác thực quan hệ học viên-khóa học, tạo bản ghi điểm danh | Mã ứng dụng | [REQ-012], [EXC-001] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 13 | Triển khai tính chất bất biến điểm danh | Triển khai logic kiểm tra trùng lặp điểm danh (cùng học viên, cùng khóa học, cùng ngày), đảm bảo chỉ tạo một bản ghi điểm danh | Mã ứng dụng | [REQ-013], [EXC-002] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 14 | Triển khai chức năng hiển thị thẻ hội viên | Xây dựng API trả về thông tin thẻ hội viên: tổng ngày hiệu lực, ngày đã sử dụng, ngày còn lại | Mã ứng dụng | [REQ-014] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 15 | Triển khai chức năng gia hạn thẻ hội viên | Xây dựng API gia hạn thẻ sau khi xác nhận thanh toán thành công, cập nhật ngày hết hạn, gửi thông báo xác nhận | Mã ứng dụng | [REQ-015] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 16 | Triển khai chức năng kích hoạt thông báo đa kênh | Xây dựng logic tạo bản ghi thông báo, xếp hàng gửi thông báo đẩy đến ứng dụng di động và gửi tin nhắn đến nhóm Zalo | Mã ứng dụng | [REQ-016], [EXC-003] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 17 | Triển khai chức năng quản lý khuyến mãi | Xây dựng API CRUD khuyến mãi (giảm giá, ưu đãi) với ngày bắt đầu/kết thúc, hiển thị khuyến mãi áp dụng cho học viên | Mã ứng dụng | [REQ-017] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 18 | Triển khai chức năng quản lý thông báo | Xây dựng API CRUD thông báo có ngày hết hạn tùy chọn, tự động ẩn thông báo sau ngày hết hạn, hiển thị toàn hệ thống | Mã ứng dụng | [REQ-018] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 19 | Tích hợp chatbot AI hỗ trợ khách hàng | Tích hợp dịch vụ chatbot AI, xử lý truy vấn người dùng về khóa học, giáo viên, trung tâm, tình trạng tài khoản, chuyển tiếp cho hỗ trợ con người khi độ tin cậy thấp | Mã ứng dụng | [REQ-019] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 20 | Triển khai giao diện người dùng vai trò cụ thể trên di động | Xây dựng giao diện đáp ứng cho từng vai trò (Student, Teacher, Admin) trên ứng dụng di động, đồng bộ chức năng với phiên bản web | Mã ứng dụng | [REQ-020] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 21 | Triển khai thông báo đẩy trên di động | Tích hợp FCM/APNs, xử lý đăng ký token thiết bị, gửi thông báo đẩy cho xác nhận điểm danh, thông báo mới, nhắc nhở | Mã ứng dụng | [REQ-021] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 22 | Triển khai phát hiện ngôn ngữ mặc định | Cấu hình logic phát hiện ngôn ngữ ưu tiên của người dùng (lưu trong hệ thống, sau đó là header Accept-Language), cập nhật UI tương ứng | Mã ứng dụng | [REQ-022] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 23 | Triển khai SEO đa ngôn ngữ | Cấu hình thẻ meta ngôn ngữ, thuộc tính hreflang cho các phiên bản ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha) | Mã ứng dụng | [REQ-023] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 24 | Triển khai chức năng tạo báo cáo điểm danh | Xây dựng API tạo báo cáo điểm danh hàng ngày cho trung tâm định dạng CSV, xử lý khôi phục dữ liệu điểm danh sau sự cố | Mã ứng dụng | [REQ-024], [EXC-005] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 25 | Triển khai bảng điều khiển tóm tắt ghi danh | Xây dựng API trả về dữ liệu tổng hợp: tổng số học viên, khóa học đang hoạt động, buổi học sắp tới (7 ngày tiếp theo) | Mã ứng dụng | [REQ-025] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 26 | Khởi tạo hạ tầng cơ sở dữ liệu và kiểm soát truy cập | Cấu hình schema PostgreSQL, tạo index, kiểm tra tính toàn vẹn dữ liệu, cấu hình RBAC, tích hợp xác thực JWT token, triển khai các luồng tích hợp hệ thống | Tài liệu doanh nghiệp | [DAT-ALL (1 to 11)], [ARC-001 to ARC-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 27 | Triển khai hạ tầng DevOps và đáp ứng yêu cầu phi chức năng | Xây dựng Dockerfile đa giai đoạn, cấu hình pipeline CI/CD với GitHub Actions, cấu hình GCP (VPC, IAM, Storage), triển khai GKE với HPA, cấu hình backup, disaster recovery, mã hóa dữ liệu, logging và audit | Hạ tầng DevOps | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| 28 | Xây dựng tài liệu kiến trúc và hướng dẫn vận hành | Xây dựng bản vẽ kiến trúc hệ thống, tài liệu schema cơ sở dữ liệu, hợp đồng API REST/Event, hướng dẫn vận hành, tài liệu tuân thủ GDPR/CCPA | Tài liệu doanh nghiệp | [ARC-010] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| **SUMMARY** | **Tổng số thẻ theo dõi đã bao phủ:** 60 | **Tổng số công việc:** 28 | **Trạng thái:** THẤT BẠI | **Tỷ lệ bao phủ:** 103.45% |
<!--END_BACKLOG_SYNOPSIS_GRID-->
<!--END_PART_1_BACKLOG_4_1-->

### 🔭 4.2. MA TRẬN TỔNG QUAN ĐA GIAI ĐOẠN
<!--START_PHASE_SYNOPSIS_GRID-->
### [CHU KỲ SỐ HỌC MA TRẬN]
> - **Tổng số công việc trong Backlog:** 28 Công việc
> - **Tổng số thẻ trong Backlog:** 60 Thẻ
> - **Tổng số công việc đã phân phối:** 28 Công việc
> - **Tổng số thẻ đã phân phối:** 60 Thẻ

| Giai đoạn | Dải ngày | ID Công việc được bao phủ | Thành phần kiến trúc / Đường dẫn mô-đun | Tóm tắt sản phẩm kỹ thuật | Đại lý phụ được giao | ID Thẻ mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 7 | Công việc 1, Công việc 2, Công việc 3, Công việc 4, Công việc 5, Công việc 6, Công việc 26, Công việc 28 | ./sources/backend/user-service/, ./sources/backend/center-service/, ./sources/docs/architecture/ | Triển khai cơ sở dữ liệu PostgreSQL với schema đầy đủ, cấu hình RBAC, tích hợp xác thực JWT/OAuth2, các API quản lý người dùng và trung tâm, cùng tài liệu kiến trúc hệ thống | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [EXC-004], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 2 | Ngày 1 - 2 | Công việc 7, Công việc 8, Công việc 9, Công việc 10, Công việc 11 | ./sources/backend/course-service/, ./sources/backend/enrollment-service/ | Triển khai API quản lý khóa học, phân công giáo viên, duyệt và đăng ký khóa học cho học viên với kiểm tra xung đột lịch | Coder, Tester, Reviewer, Doc | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 3 | Ngày 1 - 2 | Công việc 12, Công việc 13, Công việc 14, Công việc 15 | ./sources/backend/attendance-service/, ./sources/backend/card-service/ | Triển khai dịch vụ điểm danh QR idempotent, quản lý thẻ hội viên và gia hạn thẻ với tích hợp thanh toán | Coder, Tester, Reviewer, Doc | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [EXC-001], [EXC-002] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 4 | Ngày 1 - 4 | Công việc 16, Công việc 17, Công việc 18, Công việc 19, Công việc 20, Công việc 21, Công việc 22, Công việc 23, Công việc 24, Công việc 25 | ./sources/backend/notification-service/, ./sources/backend/promotion-service/, ./sources/backend/report-service/, ./sources/frontend/mobile-app/ | Triển khai hệ thống thông báo đa kênh (push, Zalo), quản lý khuyến mãi và thông báo, tích hợp chatbot AI, giao diện di động vai trò, bản địa hóa SEO, báo cáo điểm danh và bảng điều khiển | Coder, Tester, Reviewer, Doc | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-003], [EXC-005] <!--REGISTERED_PHASE_ROW--> |
| Giai đoạn 5 | Ngày 1 - 3 | Công việc 27 | ./sources/infra/ | Triển khai hạ tầng DevOps: Docker đa giai đoạn, CI/CD GitHub Actions, cấu hình GCP (VPC, IAM, Storage), triển khai GKE với HPA, cấu hình backup, disaster recovery, mã hóa dữ liệu, logging và audit | Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] <!--REGISTERED_PHASE_ROW--> |
| **Kiểm toán** | **Xác minh phân phối Backlog tổng** | **Tổng số Giai đoạn:** 5 | **Tổng số thẻ BackLog:** 60 | **Tổng số thẻ đã phân phối:** 60 | **Tổng số công việc đã phân phối:** 28 | **Trạng thái & Tuân thủ:** Đã xác minh (100%) |
<!--END_PHASE_SYNOPSIS_GRID-->

<!--START_PHASE_INDEX-->
### 📈 Giai đoạn 1 - Triển khai nền tảng quản lý người dùng, trung tâm và xác thực cốt lõi
- **Mục tiêu cốt lõi của giai đoạn:** Triển khai các module quản lý người dùng và trung tâm cốt lõi, hệ thống phân quyền RBAC, luồng xác thực OAuth2/JWT, schema cơ sở dữ liệu cho các thực thể cốt lõi, cùng tài liệu kiến trúc hệ thống nền tảng, tạo điều kiện cho việc triển khai các module chức năng khác trong các giai đoạn sau.
- **Bản đồ ma trận thư mục vật lý mục tiêu:** Liệt kê tất cả đường dẫn tệp cụ thể dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này, mỗi đường dẫn được đính kèm thẻ theo dõi tương ứng:
    * `./sources/backend/user-service/` [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001], [ARC-001], [ARC-006]
    * `./sources/backend/center-service/` [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]
    * `./sources/docs/architecture/` [ARC-010], [DAT-ALL (1 to 11)], [ARC-001 to ARC-009]
- **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:**
```sql
-- Tạo bảng vai trò người dùng [DAT-001]
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

-- Tạo bảng người dùng [DAT-001]
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

-- Tạo bảng trung tâm [DAT-003]
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE CHECK (LENGTH(tax_id) BETWEEN 10 AND 13 AND tax_id NOT LIKE '%[^0-9]%'),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255) CHECK (contact_email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Tạo bảng khóa học [DAT-004]
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);

-- Tạo bảng ghi danh [DAT-005]
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)
);

-- Tạo bảng điểm danh [DAT-006]
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id, attendance_date)
);

-- Tạo bảng thẻ hội viên [DAT-007]
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL UNIQUE REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);

-- Tạo bảng thông báo [DAT-008]
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(255),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

-- Tạo bảng khuyến mãi [DAT-009]
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(50) UNIQUE,
    discount_percent SMALLINT NOT NULL CHECK (discount_percent BETWEEN 0 AND 100),
    start_date DATE,
    end_date DATE,
    description TEXT
);

-- Tạo bảng thông báo hệ thống [DAT-009]
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Tạo bảng cài đặt hệ thống [DAT-011]
CREATE TABLE system_settings (
    setting_key VARCHAR(50) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description VARCHAR(255)
);

-- Tạo index cho các truy vấn thường dùng [DAT-ALL]
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role_id ON users(role_id);
CREATE INDEX idx_centers_tax_id ON centers(tax_id);
CREATE INDEX idx_courses_teacher_id ON courses(teacher_id);
CREATE INDEX idx_enrollments_student_id ON enrollments(student_id);
CREATE INDEX idx_enrollments_course_id ON enrollments(course_id);
CREATE INDEX idx_attendance_student_course_date ON attendance(student_id, course_id, attendance_date);
CREATE INDEX idx_notifications_user_id ON notifications(user_id);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  **Hợp đồng API REST:**
  1. `POST /api/v1/auth/register` [REQ-001]: Đăng ký người dùng mới với email/mật khẩu, trả về JWT access token và refresh token. Request body: `{email, password, fullName}`. Response 201: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  2. `POST /api/v1/auth/login` [REQ-001]: Đăng nhập với email/mật khẩu, trả về JWT token. Request body: `{email, password}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  3. `POST /api/v1/auth/oauth/{provider}` [REQ-002]: Xác thực OAuth2 với nhà cung cấp (firebase/google/facebook). Request body: `{oauthCode}`. Response 200: `{accessToken, refreshToken, user: {userId, email, fullName, role}}`.
  4. `PUT /api/v1/users/{userId}/role` [REQ-003]: Cập nhật vai trò người dùng. Request body: `{roleId}`. Response 200: `{userId, roleId, roleName}`.
  5. `GET /api/v1/centers` [REQ-004]: Lấy danh sách tất cả trung tâm. Response 200: `[{centerId, name, address, taxId, contactPhone, contactEmail}]`.
  6. `POST /api/v1/centers` [REQ-005]: Tạo trung tâm mới. Request body: `{name, address, taxId, contactPhone, contactEmail}`. Response 201: `{centerId, ...}`.
  7. `PUT /api/v1/centers/{centerId}` [REQ-005]: Cập nhật thông tin trung tâm. Request body: `{name, address, contactPhone, contactEmail}`. Response 200: `{centerId, ...}`.
  8. `DELETE /api/v1/centers/{centerId}` [REQ-005]: Xóa trung tâm. Response 204 No Content.
  9. `POST /api/v1/centers/{centerId}/admins` [REQ-006]: Gán quyền quản trị viên cho trung tâm. Request body: `{userId}`. Response 200: `{userId, centerId, role: 'CENTER_ADMIN'}`.
  10. `DELETE /api/v1/centers/{centerId}/admins/{userId}` [REQ-006]: Thu hồi quyền quản trị viên trung tâm. Response 204 No Content.

  **Hợp đồng sự kiện (Message Broker):**
  - `user.registered` [ARC-006]: Kích hoạt khi người dùng đăng ký thành công, payload: `{userId, email, role, provider}`.
  - `user.role.updated` [ARC-006]: Kích hoạt khi vai trò người dùng thay đổi, payload: `{userId, oldRole, newRole, updatedBy}`.
  - `center.created` [ARC-007]: Kích hoạt khi trung tâm mới được tạo, payload: `{centerId, name, taxId, createdBy}`.
  - `center.admin.assigned` [ARC-007]: Kích hoạt khi quản trị viên trung tâm được gán/thu hồi, payload: `{userId, centerId, action: 'ASSIGN'|'UNASSIGN', assignedBy}`.
- **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:**
  1. [EXC-004] Lỗi xác thực đầu vào: Khi người dùng gửi form đăng ký/đăng nhập với dữ liệu không hợp lệ (email sai định dạng, mật khẩu yếu, thiếu trường bắt buộc), hệ thống trả về mã lỗi 400 Bad Request với thông báo chi tiết từng trường lỗi, ví dụ: `{"errors": [{"field": "email", "message": "Định dạng email không hợp lệ"}, {"field": "password", "message": "Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường và số"}]}`. Áp dụng cho tất cả các endpoint đăng ký và đăng nhập [REQ-001], [REQ-002].
  2. Lỗi trùng lặp mã số thuế trung tâm: Khi tạo hoặc cập nhật trung tâm với mã số thuế đã tồn tại, hệ thống trả về mã lỗi 409 Conflict với thông báo "Mã số thuế đã được sử dụng bởi trung tâm khác" [REQ-005].
  3. Lỗi phân quyền không hợp lệ: Khi người dùng không có quyền thực hiện thao tác (ví dụ: người dùng thường cố gắng xóa trung tâm), hệ thống trả về mã lỗi 403 Forbidden với thông báo "Bạn không có quyền thực hiện thao tác này" [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005].
  4. Lỗi xác thực OAuth2 thất bại: Khi mã xác thực từ nhà cung cấp OAuth2 không hợp lệ hoặc đã hết hạn, hệ thống trả về mã lỗi 401 Unauthorized với thông báo "Mã xác thực không hợp lệ hoặc đã hết hạn" [REQ-002].

#### 📅 Nhật ký Phân phối Công việc Đại lý phụ theo Thứ tự Thời gian (Giai đoạn 1)

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 1: Thiết lập cấu trúc dự án, schema cơ sở dữ liệu và xác thực cốt lõi
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Thiết lập cấu trúc dự án microservice và schema cơ sở dữ liệu cốt lõi
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/main/resources/db/migration/V1__init_core_schema.sql`; `./sources/backend/center-service/src/main/resources/db/migration/V1__init_core_schema.sql`; `./sources/docs/architecture/database-schema.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo cấu trúc thư mục microservice cho user-service và center-service theo chuẩn Quarkus, triển khai script migration Flyway cho tất cả các bảng cốt lõi (users, roles, centers, courses, enrollments, attendance, student_cards, notifications, promotions, announcements, system_settings) với cấu trúc cột, khóa chính/khóa ngoại, ràng buộc CHECK và index như đã định nghĩa trong đặc tả DDL của giai đoạn. Viết tài liệu mô tả schema cơ sở dữ liệu với sơ đồ ERD và giải thích các ràng buộc toàn vẹn dữ liệu.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Cấu hình RBAC và tích hợp xác thực JWT/OAuth2 cơ bản
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/main/java/com/membershiphub/auth/JwtAuthFilter.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/auth/OAuth2Handler.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/auth/RbacEnforcer.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai bộ lọc xác thực JWT để xác thực token trên mọi yêu cầu API, tích hợp OAuth2 với Firebase, Google, Facebook, cấu hình cơ chế refresh token với thời hạn 7 ngày, triển khai logic phân quyền dựa trên vai trò người dùng (RBAC) với các quy tắc: System Admin có toàn quyền trên tất cả trung tâm, Center Admin chỉ quản lý trung tâm của mình, Manager có thể tạo thông báo, quản lý học viên, xem danh sách khóa học, Teacher chỉ xem khóa học và lịch dạy của mình, Student chỉ duyệt khóa học và xem thẻ hội viên cá nhân.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Triển khai endpoint đăng ký `POST /api/v1/auth/register` [REQ-001], endpoint đăng nhập `POST /api/v1/auth/login` [REQ-001], endpoint xác thực OAuth2 `POST /api/v1/auth/oauth/{provider}` [REQ-002], xử lý logic tạo bản ghi người dùng mặc định với vai trò Student, trả về JWT access token (hết hạn 15 phút) và refresh token. Kích hoạt sự kiện `user.registered` khi người dùng đăng ký thành công.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai trình xử lý ngoại lệ [EXC-004] trả về mã lỗi 400 Bad Request với thông báo chi tiết từng trường lỗi khi đầu vào không hợp lệ (email sai định dạng, mật khẩu yếu, thiếu trường bắt buộc).
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Viết tài liệu kiến trúc tổng quan hệ thống
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [ARC-001], [ARC-006], [ARC-007], [ARC-008], [ARC-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/system-overview.md`; `./sources/docs/architecture/auth-flow.md`; `./sources/docs/architecture/rbac-matrix.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu kiến trúc tổng quan hệ thống mô tả kiến trúc microservice, luồng dữ liệu chính (xác thực, điểm danh QR, thông báo), ma trận RBAC chi tiết cho 5 vai trò người dùng, tích hợp các dịch vụ bên thứ ba (Firebase Authentication, FCM/APNs, Zalo API, Redis caching). Viết tài liệu mô tả luồng xác thực OAuth2/JWT, luồng xử lý điểm danh QR idempotent, luồng gửi thông báo đa kênh.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 2: Triển khai chức năng đăng ký, xác thực người dùng và xác thực mạng xã hội
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai logic đăng ký và đăng nhập người dùng [REQ-001], [EXC-004]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-001], [EXC-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserService.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserDTO.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/user/UserController.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai logic đăng ký người dùng với email/mật khẩu, xác thực đầu vào (định dạng email hợp lệ, mật khẩu có ít nhất 8 ký tự bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt), mã hóa mật khẩu bằng bcrypt, tạo bản ghi người dùng mặc định với vai trò Student, trả về JWT token sau khi đăng ký thành công. Triển khai logic đăng nhập với email/mật khẩu, xác thực thông tin và cấp token.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Hoàn thiện endpoint `POST /api/v1/auth/register` và `POST /api/v1/auth/login` với schema request/response đầy đủ, tích hợp validation annotation cho các trường đầu vào.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai trình xử lý ngoại lệ [EXC-004] trả về danh sách lỗi chi tiết từng trường khi đầu vào không hợp lệ, mã lỗi 400 Bad Request.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Triển khai xác thực người dùng qua mạng xã hội [REQ-002]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/main/java/com/membershiphub/auth/OAuth2Service.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tích hợp OAuth2 với Firebase, Google, Facebook, xử lý mã xác thực từ nhà cung cấp, lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ, cấp JWT token sau khi xác thực thành công. Lưu trữ thông tin nhà cung cấp xác thực vào trường provider của bảng users.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Hoàn thiện endpoint `POST /api/v1/auth/oauth/{provider}` với xử lý logic trao đổi mã xác thực lấy thông tin người dùng, trả về JWT token và thông tin người dùng.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Xử lý lỗi khi mã xác thực OAuth2 không hợp lệ hoặc hết hạn, trả về mã lỗi 401 Unauthorized với thông báo "Mã xác thực không hợp lệ hoặc đã hết hạn".
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Viết unit test cho chức năng xác thực người dùng
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-001], [REQ-002], [EXC-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/test/java/com/membershiphub/auth/AuthServiceTest.java`; `./sources/backend/user-service/src/test/java/com/membershiphub/user/UserServiceTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: đăng ký thành công với email/mật khẩu hợp lệ, đăng ký thất bại với email đã tồn tại, đăng nhập thành công với thông tin hợp lệ, đăng nhập thất bại với mật khẩu sai, xác thực OAuth2 thành công với Google/Facebook, xác thực thất bại với mã không hợp lệ. Đảm bảo độ phủ mã ít nhất 90% cho các lớp xử lý xác thực.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 3: Triển khai API quản lý vai trò người dùng và quản lý trung tâm cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai API quản lý vai trò người dùng [REQ-003]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-003], [ARC-001], [ARC-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/main/java/com/membershiphub/user/RoleController.java`; `./sources/backend/user-service/src/main/java/com/membershiphub/user/RoleService.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `PUT /api/v1/users/{userId}/role` để cập nhật vai trò người dùng, kiểm tra quyền của người thực hiện thao tác (chỉ System Admin được phép thay đổi vai trò), cập nhật cột role_id trong bảng users, áp dụng quyền truy cập mới ngay lập tức.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Định nghĩa schema request body `{roleId: number}`, response body `{userId, roleId, roleName, permissions}`. Kích hoạt sự kiện `user.role.updated` khi vai trò thay đổi.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Trả về mã lỗi 403 Forbidden nếu người thực hiện không có quyền thay đổi vai trò, mã lỗi 404 Not Found nếu người dùng không tồn tại, mã lỗi 400 Bad Request nếu roleId không hợp lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Triển khai API quản lý trung tâm (CRUD) [REQ-004], [REQ-005]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-004], [REQ-005], [ARC-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterController.java`; `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterService.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai các API CRUD cho trung tâm: `GET /api/v1/centers` (lấy danh sách trung tâm với địa chỉ, mã số thuế, thông tin liên hệ quản trị), `POST /api/v1/centers` (tạo trung tâm mới), `PUT /api/v1/centers/{centerId}` (cập nhật thông tin trung tâm), `DELETE /api/v1/centers/{centerId}` (xóa trung tâm). Kiểm tra tính duy nhất của mã số thuế khi tạo hoặc cập nhật trung tâm.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Định nghĩa schema request/response cho các endpoint CRUD trung tâm, kích hoạt sự kiện `center.created` khi trung tâm mới được tạo, `center.updated` khi thông tin trung tâm thay đổi.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Trả về mã lỗi 409 Conflict nếu mã số thuế đã tồn tại, mã lỗi 404 Not Found nếu trung tâm không tồn tại khi cập nhật/xóa, mã lỗi 403 Forbidden nếu người dùng không có quyền quản lý trung tâm.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Viết unit test cho API quản lý vai trò và trung tâm
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-003], [REQ-004], [REQ-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/test/java/com/membershiphub/user/RoleControllerTest.java`; `./sources/backend/center-service/src/test/java/com/membershiphub/center/CenterControllerTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test và integration test cho các endpoint quản lý vai trò và trung tâm, bao gồm các trường hợp thành công, lỗi phân quyền, lỗi trùng lặp mã số thuế, lỗi không tìm thấy tài nguyên. Đảm bảo độ phủ mã ít nhất 90% cho các lớp controller và service tương ứng.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 4: Triển khai phân quyền quản trị trung tâm và tích hợp xác thực toàn hệ thống
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai API phân quyền quản trị trung tâm [REQ-006]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-006], [ARC-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/center-service/src/main/java/com/membershiphub/center/CenterAdminController.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `POST /api/v1/centers/{centerId}/admins` để gán quyền quản trị viên cho trung tâm cho người dùng được chọn, cập nhật vai trò người dùng thành 'CENTER_ADMIN' và lưu liên kết trung tâm. Triển khai API `DELETE /api/v1/centers/{centerId}/admins/{userId}` để thu hồi quyền quản trị viên, đặt lại vai trò người dùng về 'Student' và xóa liên kết trung tâm.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Định nghĩa schema request/response cho các endpoint phân quyền quản trị trung tâm, kích hoạt sự kiện `center.admin.assigned` khi quyền được gán hoặc thu hồi.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Trả về mã lỗi 403 Forbidden nếu người thực hiện không phải là System Admin, mã lỗi 404 Not Found nếu trung tâm hoặc người dùng không tồn tại, mã lỗi 400 Bad Request nếu người dùng đã là quản trị viên của trung tâm khác.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Tích hợp và kiểm tra luồng xác thực toàn hệ thống
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [ARC-006], [REQ-001], [REQ-002], [REQ-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/test/java/com/membershiphub/auth/AuthIntegrationTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra tích hợp toàn bộ luồng xác thực: đăng ký người dùng mới -> đăng nhập với email/mật khẩu -> đăng nhập với OAuth2 Google/Facebook -> sử dụng JWT token truy cập các endpoint được bảo vệ -> kiểm tra refresh token hoạt động đúng khi access token hết hạn. Kiểm tra logic phân quyền RBAC hoạt động đúng với từng vai trò người dùng.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Xử lý lỗi khi JWT token không hợp lệ hoặc hết hạn, trả về mã lỗi 401 Unauthorized với thông báo "Token xác thực không hợp lệ hoặc đã hết hạn".
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Xây dựng Dockerfile đa giai đoạn cho service backend
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Docker]
* **ID Thẻ mục tiêu:** [NFR-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/Dockerfile`; `./sources/backend/center-service/Dockerfile`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Xây dựng Dockerfile đa giai đoạn cho user-service và center-service, sử dụng base image JDK 21 slim, tối ưu kích thước hình ảnh dưới 200MB, cấu hình biến môi trường cho kết nối cơ sở dữ liệu, cổng ứng dụng và cấu hình xác thực.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 5: Viết integration test và kiểm tra chất lượng mã nguồn
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Viết integration test cho luồng chức năng người dùng và trung tâm
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/src/test/java/com/membershiphub/user/UserIntegrationTest.java`; `./sources/backend/center-service/src/test/java/com/membershiphub/center/CenterIntegrationTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết integration test cho các luồng: đăng ký người dùng -> đăng nhập -> cập nhật vai trò -> gán quyền quản trị trung tâm -> quản lý thông tin trung tâm. Kiểm tra tính toàn vẹn dữ liệu, ràng buộc khóa ngoại, logic phân quyền hoạt động đúng. Đảm bảo độ phủ tích hợp ít nhất 85%.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Kiểm tra chất lượng mã và sửa lỗi
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [EXC-004], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/`; `./sources/backend/center-service/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho tất cả các mã nguồn của user-service và center-service, phát hiện lỗi cú pháp, lỗi logic, điểm nghẽn hiệu suất, vi phạm chuẩn mã hóa, đề xuất và thực hiện sửa lỗi. Đảm bảo mã nguồn tuân thủ chuẩn Quarkus và Java 21, không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) [NFR-003].
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 6: Viết tài liệu kiến trúc và hợp đồng hệ thống
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Viết tài liệu hợp đồng API REST và sự kiện
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/api-contracts.md`; `./sources/docs/architecture/event-contracts.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho tất cả các endpoint của user-service và center-service, bao gồm phương thức HTTP, đường dẫn, schema request/response, mã lỗi, ví dụ sử dụng. Viết tài liệu hợp đồng sự kiện cho các topic message broker, bao gồm tên topic, schema payload, mô tả sự kiện.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Viết tài liệu hướng dẫn vận hành và tuân thủ
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [NFR-006], [NFR-008]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/operational-guide.md`; `./sources/docs/architecture/compliance.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn vận hành các service backend, bao gồm cách khởi chạy, cấu hình môi trường, giám sát, xử lý sự cố. Viết tài liệu tuân thủ RBAC, OWASP Top 10, GDPR/CCPA liên quan đến module quản lý người dùng và trung tâm, bao gồm quy trình xóa dữ liệu người dùng khi có yêu cầu, quy trình xuất dữ liệu người dùng dưới dạng JSON.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 7: Kiểm tra cuối cùng, tối ưu và đóng gói sản phẩm giai đoạn
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Kiểm tra bảo mật và tối ưu hiệu suất
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [NFR-001], [NFR-003], [NFR-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/user-service/`; `./sources/backend/center-service/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra bảo mật toàn diện cho các service: kiểm tra lỗi SQL injection, XSS, CSRF, kiểm tra cấu hình mã hóa mật khẩu bcrypt, kiểm tra cơ chế hết hạn JWT token, kiểm tra logic phân quyền RBAC không có lỗ hổng. Tối ưu truy vấn cơ sở dữ liệu, đảm bảo độ trễ API trung bình dưới 200ms [NFR-001]. Kiểm tra cấu hình logging ghi lại tất cả hành động người dùng (thay đổi vai trò, quản lý trung tâm) với timestamp, user ID và chi tiết hành động, đảm bảo log được lưu trữ 1 năm [NFR-006].
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Hoàn thiện tài liệu và đẩy hình ảnh Docker
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc], [Docker]
* **ID Thẻ mục tiêu:** [ARC-010], [NFR-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/`; `./sources/backend/user-service/Dockerfile`; `./sources/backend/center-service/Dockerfile`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Hoàn thiện tất cả tài liệu kiến trúc, đảm bảo tài liệu đầy đủ, chính xác, phù hợp với triển khai thực tế. Xây dựng và đẩy hình ảnh Docker cho user-service và center-service lên registry mục tiêu, đảm bảo kích thước hình ảnh dưới 500MB [NFR-005].
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Kiểm tra cuối cùng và xác nhận hoàn thành giai đoạn
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [EXC-004], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** Toàn bộ mã nguồn và tài liệu của giai đoạn 1
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra cuối cùng toàn bộ sản phẩm của giai đoạn 1, đảm bảo tất cả các yêu cầu và thẻ theo dõi đã được triển khai đầy đủ, không có lỗi còn tồn tại, xác nhận giai đoạn sẵn sàng cho giai đoạn tiếp theo.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->
### 📈 Giai đoạn 2 - Triển khai quản lý khóa học và đăng ký học viên
- **Mục tiêu cốt lõi của giai đoạn:** Triển khai các dịch vụ quản lý khóa học và đăng ký học viên, bao gồm API quản lý khóa học (CRUD), phân công giáo viên, duyệt khóa học và đăng ký khóa học cho học viên với kiểm tra xung đột lịch học.
- **Ma trận ánh xạ thư mục vật lý mục tiêu:**
  * `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java` [REQ-007], [REQ-008]
  * `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java` [REQ-007], [REQ-008]
  * `./sources/backend/course-service/src/main/java/com/membershiphub/course/TeacherAssignmentController.java` [REQ-009]
  * `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/CourseBrowseController.java` [REQ-010]
  * `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentController.java` [REQ-011]
  * `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java` [REQ-010], [REQ-011]
  * `./sources/docs/architecture/course-service-api.md` [REQ-007], [REQ-008], [REQ-009]
  * `./sources/docs/architecture/enrollment-service-api.md` [REQ-010], [REQ-011]

- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
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
    },
    "enrollmentService": {
      "basePath": "/api/v1",
      "endpoints": [
        {
          "method": "GET",
          "path": "/courses/available",
          "tags": ["REQ-010"],
          "summary": "Lấy danh sách khóa học chưa đăng ký của học viên",
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
        },
        {
          "method": "POST",
          "path": "/courses/{courseId}/enroll",
          "tags": ["REQ-011"],
          "summary": "Đăng ký khóa học cho học viên",
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
  }
  ```

#### 📅 Nhật ký phân phối công việc của Đại lý phụ theo thứ tự thời gian (Giai đoạn 2)

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 1: Triển khai API quản lý khóa học và phân công giáo viên

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai API CRUD quản lý khóa học [REQ-007], [REQ-008]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-007], [REQ-008]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseController.java`; `./sources/backend/course-service/src/main/java/com/membershiphub/course/CourseService.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API CRUD cho khóa học: `GET /api/v1/courses` (lấy danh sách khóa học với lịch học và giáo viên), `POST /api/v1/courses` (tạo khóa học mới với kiểm tra xung đột lịch học giáo viên), `PUT /api/v1/courses/{courseId}` (cập nhật thông tin khóa học), `DELETE /api/v1/courses/{courseId}` (xóa khóa học). Triển khai logic kiểm tra xung đột lịch học: khi tạo hoặc cập nhật khóa học, kiểm tra giáo viên được phân công có bị trùng lịch với khóa học khác không bằng cách truy vấn các khóa học hiện tại của giáo viên trong khoảng thời gian bắt đầu và kết thúc mới.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "endpoints": [
      {
        "method": "GET",
        "path": "/api/v1/courses",
        "tags": ["REQ-007"],
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
        "path": "/api/v1/courses",
        "tags": ["REQ-008"],
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
      }
    ]
  }
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho giai đoạn này.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Triển khai API phân công giáo viên vào khóa học [REQ-009]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/course-service/src/main/java/com/membershiphub/course/TeacherAssignmentController.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `POST /api/v1/courses/{courseId}/teachers` để gán giáo viên vào khóa học, kiểm tra quyền của người thực hiện (chỉ System Admin được phép phân công), và `DELETE /api/v1/courses/{courseId}/teachers/{teacherId}` để thu hồi phân công. Kích hoạt sự kiện `teacher.assigned` khi phân công thành công để hệ thống thông báo gửi thông báo cho giáo viên.
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
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho giai đoạn này.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Viết unit test cho dịch vụ quản lý khóa học
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/course-service/src/test/java/com/membershiphub/course/CourseServiceTest.java`; `./sources/backend/course-service/src/test/java/com/membershiphub/course/TeacherAssignmentTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: tạo khóa học thành công, tạo khóa học thất bại do trùng lịch giáo viên, cập nhật khóa học thành công, xóa khóa học thành công, phân công giáo viên thành công, thu hồi phân công thành công. Kiểm tra logic kiểm tra xung đột lịch học hoạt động đúng. Đảm bảo độ phủ mã ít nhất 90% cho các lớp service.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 4: Kiểm tra chất lượng mã nguồn dịch vụ khóa học
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/course-service/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn course-service, kiểm tra logic kiểm tra xung đột lịch học, đảm bảo không có lỗi logic, tuân thủ chuẩn mã hóa Quarkus/Java 21, kiểm tra bảo mật cơ bản (SQL injection, XSS). Đề xuất và thực hiện sửa lỗi nếu có.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 5: Viết tài liệu hợp đồng API dịch vụ khóa học
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [REQ-007], [REQ-008], [REQ-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/course-service-api.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho tất cả các endpoint của course-service, bao gồm phương thức HTTP, đường dẫn, schema request/response, mã lỗi, ví dụ sử dụng. Mô tả logic kiểm tra xung đột lịch học và cách xử lý.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "service": "course-service",
    "version": "v1",
    "endpoints": [
      {
        "method": "GET",
        "path": "/api/v1/courses",
        "summary": "Lấy danh sách khóa học",
        "tags": ["REQ-007"]
      },
      {
        "method": "POST",
        "path": "/api/v1/courses",
        "summary": "Tạo khóa học mới",
        "tags": ["REQ-008"]
      },
      {
        "method": "PUT",
        "path": "/api/v1/courses/{courseId}",
        "summary": "Cập nhật khóa học",
        "tags": ["REQ-008"]
      },
      {
        "method": "DELETE",
        "path": "/api/v1/courses/{courseId}",
        "summary": "Xóa khóa học",
        "tags": ["REQ-008"]
      },
      {
        "method": "POST",
        "path": "/api/v1/courses/{courseId}/teachers",
        "summary": "Phân công giáo viên",
        "tags": ["REQ-009"]
      },
      {
        "method": "DELETE",
        "path": "/api/v1/courses/{courseId}/teachers/{teacherId}",
        "summary": "Thu hồi phân công giáo viên",
        "tags": ["REQ-009"]
      }
    ]
  }
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 2: Triển khai duyệt khóa học và đăng ký học viên

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai API duyệt khóa học cho học viên [REQ-010]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/CourseBrowseController.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `GET /api/v1/courses/available` trả về danh sách khóa học chưa đăng ký của học viên, hiển thị sức chứa và lịch học. Loại bỏ các khóa học mà học viên đã có bản ghi ghi danh. Bao gồm thông tin: courseId, title, startDate, endDate, maxStudents, currentEnrollments.
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
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho giai đoạn này.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Triển khai API đăng ký khóa học học viên [REQ-011]
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-011]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentController.java`; `./sources/backend/enrollment-service/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `POST /api/v1/courses/{courseId}/enroll` để đăng ký khóa học cho học viên. Logic: kiểm tra học viên đã đăng ký khóa học này chưa, kiểm tra khóa học còn chỗ trống không, nếu học viên chưa có tài khoản cục bộ thì tự động tạo tài khoản với vai trò 'Student', tạo bản ghi ghi danh, kích hoạt sự kiện `student.enrolled` để hệ thống gửi thông báo cho học viên và nhóm Zalo của trung tâm.
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
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho giai đoạn này.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Viết integration test cho luồng đăng ký khóa học
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-010], [REQ-011]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/enrollment-service/src/test/java/com/membershiphub/enrollment/EnrollmentIntegrationTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết integration test cho luồng đăng ký khóa học: học viên duyệt khóa học chưa đăng ký -> đăng ký khóa học -> kiểm tra bản ghi ghi danh được tạo -> kiểm tra sự kiện `student.enrolled` được kích hoạt -> kiểm tra thông báo được gửi đến học viên và nhóm Zalo. Kiểm tra các trường hợp: đăng ký khóa học đã hết chỗ, đăng ký khóa học đã đăng ký trước đó, tự động tạo tài khoản học viên nếu chưa tồn tại.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 4: Kiểm tra chất lượng mã nguồn dịch vụ đăng ký
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-010], [REQ-011]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/enrollment-service/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn enrollment-service, kiểm tra logic tự động tạo tài khoản học viên, logic kiểm tra trùng lặp đăng ký, logic kiểm tra sức chứa khóa học. Đảm bảo không có lỗi logic, tuân thủ chuẩn mã hóa, kiểm tra bảo mật cơ bản.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 5: Viết tài liệu hợp đồng API dịch vụ đăng ký
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [REQ-010], [REQ-011]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/enrollment-service-api.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho enrollment-service, bao gồm endpoint duyệt khóa học và đăng ký khóa học, schema request/response, mã lỗi, ví dụ sử dụng. Mô tả logic tự động tạo tài khoản học viên và luồng thông báo sau đăng ký.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "service": "enrollment-service",
    "version": "v1",
    "endpoints": [
      {
        "method": "GET",
        "path": "/api/v1/courses/available",
        "summary": "Lấy danh sách khóa học chưa đăng ký",
        "tags": ["REQ-010"]
      },
      {
        "method": "POST",
        "path": "/api/v1/courses/{courseId}/enroll",
        "summary": "Đăng ký khóa học cho học viên",
        "tags": ["REQ-011"]
      }
    ]
  }
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->
<!--END_PHASE_INDEX-->

<!--START_PHASE_INDEX-->
### 📈 Giai đoạn 3 - Triển khai dịch vụ điểm danh QR và quản lý thẻ hội viên
- **Mục tiêu cốt lõi của giai đoạn:** Triển khai dịch vụ điểm danh QR có tính bất biến (idempotent) để đảm bảo mỗi học viên chỉ có một bản ghi điểm danh mỗi ngày cho mỗi khóa học, xây dựng dịch vụ quản lý thẻ hội viên với chức năng hiển thị ngày còn lại và gia hạn thẻ sau khi thanh toán thành công, xử lý các ngoại lệ liên quan đến kết nối mạng và gửi thông báo, đảm bảo tính toàn vẹn dữ liệu điểm danh và trải nghiệm người dùng liền mạch.
- **Bản đồ đường dẫn thành phần vật lý mục tiêu:**
  * `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceController.java` [REQ-012], [REQ-013], [EXC-001], [EXC-002]
  * `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java` [REQ-012], [REQ-013], [EXC-001], [EXC-002]
  * `./sources/backend/attendance-service/src/main/resources/db/migration/V2__add_attendance_unique_constraint.sql` [DAT-006], [REQ-013]
  * `./sources/backend/card-service/src/main/java/com/membershiphub/card/CardController.java` [REQ-014], [REQ-015]
  * `./sources/backend/card-service/src/main/java/com/membershiphub/card/CardService.java` [REQ-014], [REQ-015]
  * `./sources/backend/card-service/src/main/resources/db/migration/V2__add_card_check_constraints.sql` [DAT-007], [REQ-015]
  * `./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/AttendanceServiceTest.java` [REQ-012], [REQ-013], [EXC-001], [EXC-002]
  * `./sources/backend/card-service/src/test/java/com/membershiphub/card/CardServiceTest.java` [REQ-014], [REQ-015]
  * `./sources/docs/architecture/attendance-service-api.md` [ARC-010], [REQ-012], [REQ-013]
  * `./sources/docs/architecture/card-service-api.md` [ARC-010], [REQ-014], [REQ-015]
- **Đặc tả DDL SQL cơ sở dữ liệu [DAT-XXX]:**
  ```sql
  -- Thêm ràng buộc duy nhất cho bảng điểm danh để đảm bảo tính bất biến (mỗi học viên chỉ điểm danh 1 lần/ngày/khóa học) [DAT-006], [REQ-013]
  ALTER TABLE attendance
  ADD CONSTRAINT uk_student_course_date UNIQUE (student_id, course_id, attendance_date);
  
  -- Thêm ràng buộc CHECK cho bảng thẻ hội viên để đảm bảo ngày còn lại không âm và không vượt quá tổng ngày hiệu lực [DAT-007], [REQ-014]
  ALTER TABLE student_cards
  ADD CONSTRAINT chk_remaining_days CHECK (remaining_days >= 0 AND remaining_days <= validity_days);
  ```
- **Hợp đồng định tuyến API và sự kiện [REQ-XXX], [ARC-XXX]:**
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
      },
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
- **Trình xử lý ngoại lệ cục bộ của giai đoạn [EXC-XXX]:**
  * [EXC-001] Lỗi kết nối mạng trong quá trình quét mã QR: Nếu học viên quét mã QR nhưng kết nối mạng bị gián đoạn, khi ứng dụng di động tự động thử lại sau khi kết nối được khôi phục, hệ thống sẽ ghi nhận điểm danh một lần duy nhất, trả về trạng thái `RECORDED` cho yêu cầu thử lại.
  * [EXC-002] Gửi điểm danh trùng lặp: Nếu học viên quét mã QR cùng một khóa học nhiều lần trong cùng một ngày, hệ thống phát hiện trùng lặp dựa trên ràng buộc duy nhất (student_id, course_id, attendance_date), trả về trạng thái `DUPLICATE` và không tạo bản ghi điểm danh mới.
  * Ngoại lệ thanh toán thất bại khi gia hạn thẻ: Nếu giao dịch thanh toán cho gia hạn thẻ không thành công, hệ thống trả về mã lỗi 402 Payment Required với thông báo "Giao dịch thanh toán không thành công, vui lòng thử lại".

#### 📅 Nhật ký phân phối công việc phụ đại lý theo thứ tự thời gian (Giai đoạn 3)

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 1: Triển khai dịch vụ điểm danh QR và logic bất biến điểm danh
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai logic cốt lõi của dịch vụ điểm danh QR
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceController.java`; `./sources/backend/attendance-service/src/main/java/com/membershiphub/attendance/AttendanceService.java`; `./sources/backend/attendance-service/src/main/resources/db/migration/V2__add_attendance_unique_constraint.sql`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai endpoint `POST /api/v1/attendance/scan` để xử lý yêu cầu quét mã QR điểm danh: nhận payload chứa mã QR khóa học và ID học viên, xác thực học viên đã đăng ký khóa học tương ứng với mã QR, tạo bản ghi điểm danh với thời gian hiện tại. Triển khai logic kiểm tra trùng lặp điểm danh dựa trên ràng buộc duy nhất (student_id, course_id, attendance_date) để đảm bảo chỉ tạo một bản ghi điểm danh mỗi ngày cho mỗi học viên và khóa học. Triển khai xử lý yêu cầu thử lại khi lỗi kết nối mạng, đảm bảo điểm danh được ghi nhận đúng một lần sau khi kết nối được khôi phục.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Triển khai endpoint `POST /api/v1/attendance/scan` với schema request/response như đã định nghĩa, kích hoạt sự kiện `attendance.recorded` khi điểm danh được ghi nhận thành công, sự kiện `attendance.duplicate` khi phát hiện điểm danh trùng lặp.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ [EXC-001] (lỗi kết nối mạng) bằng cách lưu tạm yêu cầu điểm danh vào hàng đợi Redis khi không thể kết nối cơ sở dữ liệu, tự động xử lý hàng đợi khi kết nối được khôi phục. Triển khai xử lý ngoại lệ [EXC-002] (điểm danh trùng lặp) bằng cách bắt lỗi vi phạm ràng buộc duy nhất, trả về trạng thái `DUPLICATE` và thông báo "Bạn đã điểm danh cho khóa học này trong ngày hôm nay".
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Viết unit test cho dịch vụ điểm danh
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-012], [REQ-013], [EXC-001], [EXC-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/AttendanceServiceTest.java`; `./sources/backend/attendance-service/src/test/java/com/membershiphub/attendance/AttendanceControllerTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: quét mã QR thành công và tạo bản ghi điểm danh, quét mã QR trùng lặp trong cùng ngày trả về trạng thái DUPLICATE, quét mã QR khi học viên chưa đăng ký khóa học trả về lỗi 403 Forbidden, quét mã QR không hợp lệ trả về lỗi 400 Bad Request, xử lý yêu cầu khi kết nối mạng bị gián đoạn và thử lại sau khi khôi phục. Đảm bảo độ phủ mã ít nhất 90% cho các lớp xử lý điểm danh.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Kiểm tra chất lượng mã nguồn dịch vụ điểm danh
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-012], [REQ-013], [EXC-001], [EXC-002], [NFR-001]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/attendance-service/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn attendance-service, kiểm tra logic kiểm tra trùng lặp điểm danh hoạt động đúng, đảm bảo không có lỗi logic trong xử lý mã QR và xác thực quan hệ học viên-khóa học, kiểm tra hiệu suất truy vấn cơ sở dữ liệu đảm bảo độ trễ API trung bình dưới 200ms [NFR-001], kiểm tra không có lỗi bảo mật cơ bản (SQL injection, XSS). Đề xuất và thực hiện sửa lỗi nếu có.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 2: Triển khai quản lý thẻ hội viên và gia hạn thẻ
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai logic cốt lõi của dịch vụ quản lý thẻ hội viên
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-014], [REQ-015], [DAT-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/card-service/src/main/java/com/membershiphub/card/CardController.java`; `./sources/backend/card-service/src/main/java/com/membershiphub/card/CardService.java`; `./sources/backend/card-service/src/main/resources/db/migration/V2__add_card_check_constraints.sql`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai endpoint `GET /api/v1/cards/student/{studentId}` để trả về thông tin thẻ hội viên của học viên: tổng ngày hiệu lực, ngày đã sử dụng, ngày còn lại, ngày hết hạn. Triển khai endpoint `POST /api/v1/cards/{cardId}/renew` để gia hạn thẻ: nhận số ngày gia hạn và ID giao dịch thanh toán thành công, cập nhật ngày hết hạn của thẻ, tính toán lại số ngày còn lại, kích hoạt sự kiện `card.renewed` để gửi thông báo xác nhận cho học viên. Triển khai logic kiểm tra tính hợp lệ của giao dịch thanh toán trước khi cập nhật thẻ.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Triển khai các endpoint của card-service với schema request/response như đã định nghĩa, kích hoạt sự kiện `card.renewed` khi gia hạn thẻ thành công để hệ thống gửi thông báo cho học viên.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ khi giao dịch thanh toán không hợp lệ, trả về mã lỗi 402 Payment Required với thông báo "Giao dịch thanh toán không hợp lệ hoặc đã hết hạn". Triển khai xử lý ngoại lệ khi thẻ hội viên không tồn tại, trả về mã lỗi 404 Not Found.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Viết unit và integration test cho dịch vụ quản lý thẻ
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-014], [REQ-015]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/card-service/src/test/java/com/membershiphub/card/CardServiceTest.java`; `./sources/backend/card-service/src/test/java/com/membershiphub/card/CardIntegrationTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: lấy thông tin thẻ hội viên thành công, gia hạn thẻ thành công với số ngày hợp lệ, gia hạn thẻ thất bại với giao dịch thanh toán không hợp lệ, gia hạn thẻ thất bại khi thẻ không tồn tại. Viết integration test cho luồng gia hạn thẻ: gửi yêu cầu gia hạn -> kiểm tra thông tin thẻ được cập nhật -> kiểm tra sự kiện `card.renewed` được kích hoạt -> kiểm tra thông báo được gửi cho học viên. Đảm bảo độ phủ mã ít nhất 90% cho các lớp xử lý thẻ hội viên.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Viết tài liệu hợp đồng API cho dịch vụ điểm danh và quản lý thẻ
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [REQ-012], [REQ-013], [REQ-014], [REQ-015]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/attendance-service-api.md`; `./sources/docs/architecture/card-service-api.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho attendance-service và card-service, bao gồm phương thức HTTP, đường dẫn, schema request/response, mã lỗi, ví dụ sử dụng. Mô tả logic kiểm tra trùng lặp điểm danh, quy tắc tính ngày còn lại của thẻ hội viên, quy trình gia hạn thẻ và tích hợp thanh toán.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 4: Kiểm tra cuối cùng và xác nhận hoàn thành giai đoạn 3
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-012], [REQ-013], [REQ-014], [REQ-015], [EXC-001], [EXC-002], [DAT-006], [DAT-007], [ARC-010]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/attendance-service/`; `./sources/backend/card-service/`; `./sources/docs/architecture/attendance-service-api.md`; `./sources/docs/architecture/card-service-api.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra cuối cùng toàn bộ sản phẩm của giai đoạn 3, đảm bảo tất cả các yêu cầu và thẻ theo dõi đã được triển khai đầy đủ: logic điểm danh bất biến hoạt động đúng, chức năng hiển thị và gia hạn thẻ hoạt động chính xác, các ngoại lệ được xử lý đúng, tài liệu API đầy đủ và chính xác, không có lỗi còn tồn tại, xác nhận giai đoạn sẵn sàng cho giai đoạn tiếp theo.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->

### 📈 Giai đoạn 4 - Triển khai hệ thống thông báo đa kênh, quản lý khuyến mãi, tích hợp chatbot AI và báo cáo phân tích
- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Triển khai hoàn chỉnh các tính năng giao tiếp đa kênh (thông báo đẩy di động, tin nhắn nhóm Zalo), quản lý khuyến mãi và thông báo hệ thống, tích hợp chatbot AI hỗ trợ khách hàng, giao diện di động vai trò tương ứng, bản địa hóa/SEO đa ngôn ngữ và các báo cáo phân tích cốt lõi, hoàn thiện tất cả các yêu cầu chức năng người dùng cuối của hệ thống membership-hub, đảm bảo tích hợp liền mạch giữa các microservice và giao diện người dùng.
- **Bản đồ ma trận đường dẫn vật lý mục tiêu:** Liệt kê tất cả đường dẫn tệp dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này, mỗi dòng đường dẫn được nối với ID thẻ theo dõi tương ứng:
  * `./sources/backend/notification-service/` [REQ-016], [EXC-003], [ARC-008]
  * `./sources/backend/promotion-service/` [REQ-017], [REQ-018]
  * `./sources/backend/report-service/` [REQ-024], [REQ-025], [EXC-005]
  * `./sources/frontend/mobile-app/` [REQ-020], [REQ-021], [REQ-022], [REQ-023]
  * `./sources/docs/architecture/notification-service-api.md` [ARC-010]
  * `./sources/docs/architecture/promotion-service-api.md` [ARC-010]
  * `./sources/docs/architecture/report-service-api.md` [ARC-010]
  * `./sources/docs/architecture/chatbot-integration.md` [ARC-010]
  * `./sources/docs/architecture/localization-seo-guide.md` [ARC-010]
  * `./sources/docs/architecture/mobile-app-guide.md` [ARC-010]
- **Đặc tả DDL SQL cơ sở dữ liệu [DAT-XXX]:**
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
- **Hợp đồng định tuyến API và sự kiện [REQ-XXX], [ARC-XXX]:**
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
    },
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
- **Trình xử lý ngoại lệ cục bộ của giai đoạn [EXC-XXX]:**
  * **[EXC-003] Lỗi gửi thông báo thất bại:** Khi không thể gửi thông báo đẩy (token thiết bị không hợp lệ, hết hạn) hoặc tin nhắn Zalo thất bại, hệ thống ghi lại lỗi với đầy đủ thông tin: timestamp, ID người dùng/nhóm Zalo, loại thông báo, lý do thất bại. Hệ thống tự động lên lịch thử lại tối đa 3 lần với khoảng cách tăng dần (1 phút, 5 phút, 15 phút). Nếu vẫn thất bại sau 3 lần thử, đánh dấu trạng thái `delivered = false` trong bảng notifications và gửi thông báo cảnh báo cho quản trị viên hệ thống để xử lý thủ công.
  * **[EXC-005] Khôi phục hệ thống sau sự cố:** Khi dịch vụ khôi phục hoạt động sau thời gian ngừng hoạt động, hệ thống tự động xử lý tất cả các yêu cầu điểm danh đang chờ trong hàng đợi Redis theo thứ tự FIFO (First In First Out), đồng bộ dữ liệu điểm danh với cơ sở dữ liệu chính để đảm bảo tính nhất quán. Sau khi xử lý xong, hệ thống gửi thông báo cho tất cả người dùng liên quan về các sự kiện điểm danh đã được xử lý trong thời gian sự cố.

#### 📅 Nhật ký công việc theo ngày của giai đoạn 4

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 1: Triển khai dịch vụ thông báo và quản lý khuyến mãi cơ bản
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai API quản lý thông báo và khuyến mãi
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-016], [REQ-017], [REQ-018], [EXC-003], [DAT-008], [DAT-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationController.java`; `./sources/backend/notification-service/src/main/java/com/membershiphub/notification/NotificationService.java`; `./sources/backend/promotion-service/src/main/java/com/membershiphub/promotion/PromotionController.java`; `./sources/backend/promotion-service/src/main/java/com/membershiphub/promotion/PromotionService.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API CRUD cho quản lý thông báo (announcements): `POST /api/v1/notifications/announcements` (tạo thông báo mới), `GET /api/v1/notifications/announcements` (lấy danh sách thông báo còn hiệu lực), `DELETE /api/v1/notifications/announcements/{announcementId}` (xóa thông báo). Triển khai logic tự động ẩn thông báo sau ngày hết hạn nếu được cấu hình. Triển khai API CRUD cho quản lý khuyến mãi (promotions): `POST /api/v1/promotions` (tạo khuyến mãi mới), `GET /api/v1/promotions/active` (lấy danh sách khuyến mãi còn hiệu lực), `DELETE /api/v1/promotions/{promoId}` (xóa khuyến mãi). Triển khai logic tự động ẩn khuyến mãi sau ngày hết hạn. Triển khai logic gửi thông báo đẩy qua FCM/APNs và tin nhắn đến nhóm Zalo được chỉ định. Triển khai xử lý ngoại lệ [EXC-003] với cơ chế thử lại tối đa 3 lần khi gửi thông báo thất bại, lưu lỗi vào bảng notifications với trạng thái delivered = false.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
    "endpoints": [
      {
        "method": "POST",
        "path": "/api/v1/notifications/announcements",
        "tags": ["REQ-018"],
        "request": {
          "required": ["title", "content"],
          "properties": {
            "title": {"type": "string", "maxLength": 150},
            "content": {"type": "string", "maxLength": 2000},
            "expiryDate": {"type": "date", "optional": true},
            "targetZaloGroup": {"type": "string", "optional": true}
          }
        }
      },
      {
        "method": "GET",
        "path": "/api/v1/notifications/announcements",
        "tags": ["REQ-018"]
      },
      {
        "method": "POST",
        "path": "/api/v1/promotions",
        "tags": ["REQ-017"],
        "request": {
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
      {
        "method": "GET",
        "path": "/api/v1/promotions/active",
        "tags": ["REQ-017"]
      }
    ],
    "events": [
      {
        "topic": "announcement.created",
        "tags": ["REQ-018"],
        "payload": {
          "announcementId": {"type": "uuid"},
          "title": {"type": "string"},
          "expiryDate": {"type": "date", "optional": true}
        }
      },
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
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ [EXC-003] trả về mã lỗi 500 Internal Server Error với thông báo "Gửi thông báo thất bại, hệ thống sẽ thử lại sau" khi lần thử đầu tiên thất bại, lên lịch thử lại tự động. Nếu thất bại sau 3 lần thử, ghi log lỗi chi tiết và gửi cảnh báo cho quản trị viên.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Viết unit test cho dịch vụ thông báo và khuyến mãi
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-016], [REQ-017], [REQ-018], [EXC-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/notification-service/src/test/java/com/membershiphub/notification/NotificationServiceTest.java`; `./sources/backend/promotion-service/src/test/java/com/membershiphub/promotion/PromotionServiceTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: tạo thông báo thành công, lấy danh sách thông báo còn hiệu lực (lọc bỏ thông báo đã hết hạn), xóa thông báo thành công, tạo khuyến mãi thành công, lấy danh sách khuyến mãi còn hiệu lực, xử lý lỗi gửi thông báo thất bại với cơ chế thử lại 3 lần, kiểm tra trạng thái delivered được cập nhật đúng sau khi thử lại thất bại. Đảm bảo độ phủ mã ít nhất 90% cho các lớp service tương ứng.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Kiểm tra chất lượng mã nguồn dịch vụ thông báo và khuyến mãi
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-016], [REQ-017], [REQ-018], [EXC-003], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/notification-service/`; `./sources/backend/promotion-service/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn notification-service và promotion-service, kiểm tra logic gửi thông báo đa kênh hoạt động đúng, logic tự động ẩn thông báo/khuyến mãi hết hạn hoạt động chính xác, cơ chế thử lại khi gửi thông báo thất bại hoạt động đúng, đảm bảo không có lỗi bảo mật cơ bản (SQL injection, XSS, CSRF) [NFR-003], tuân thủ chuẩn mã hóa Quarkus/Java 21. Đề xuất và thực hiện sửa lỗi nếu có.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 4: Viết tài liệu hợp đồng API cho dịch vụ thông báo và khuyến mãi
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [REQ-016], [REQ-017], [REQ-018]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/notification-service-api.md`; `./sources/docs/architecture/promotion-service-api.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho notification-service và promotion-service, bao gồm tất cả endpoint quản lý thông báo, quản lý khuyến mãi, schema request/response, mã lỗi, ví dụ sử dụng. Mô tả luồng gửi thông báo đa kênh (push, Zalo) và cơ chế thử lại khi gửi thất bại, quy tắc tự động ẩn thông báo/khuyến mãi hết hạn.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 2: Triển khai tích hợp chatbot AI và bản địa hóa/SEO đa ngôn ngữ
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Tích hợp chatbot AI và triển khai bản địa hóa/SEO
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-019], [REQ-022], [REQ-023], [NFR-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/chatbot-service/src/main/java/com/membershiphub/chatbot/ChatbotController.java`; `./sources/backend/chatbot-service/src/main/java/com/membershiphub/chatbot/ChatbotService.java`; `./sources/frontend/web/src/components/ChatbotWidget.tsx`; `./sources/frontend/web/src/hooks/useLocale.ts`; `./sources/frontend/web/src/app/[locale]/layout.tsx`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tích hợp dịch vụ chatbot AI bên thứ ba, triển khai endpoint `POST /api/v1/chatbot/query` để xử lý truy vấn người dùng về khóa học, giáo viên, trung tâm, tình trạng tài khoản. Triển khai logic chuyển tiếp truy vấn cho hỗ trợ con người khi độ tin cậy của câu trả lời chatbot dưới 70%. Triển khai logic phát hiện ngôn ngữ ưu tiên: ưu tiên ngôn ngữ đã lưu trong cài đặt người dùng, sau đó là header `Accept-Language` của trình duyệt, mặc định là Tiếng Việt. Triển khai cấu hình SEO đa ngôn ngữ: thẻ `<html lang="...">` chính xác cho mỗi ngôn ngữ, thuộc tính `hreflang` cho các phiên bản ngôn ngữ (en, vi, es), thẻ meta ngôn ngữ cho mỗi trang. Đảm bảo chuyển đổi ngôn ngữ không cần tải lại trang [NFR-007].
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
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Viết unit test cho chatbot và bản địa hóa/SEO
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-019], [REQ-022], [REQ-023]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/chatbot-service/src/test/java/com/membershiphub/chatbot/ChatbotServiceTest.java`; `./sources/frontend/web/src/test/components/ChatbotWidget.test.tsx`; `./sources/frontend/web/src/test/hooks/useLocale.test.ts`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho chatbot: xử lý truy vấn thành công trả về câu trả lời liên quan, chuyển tiếp cho hỗ trợ con người khi độ tin cậy dưới 70%, xử lý truy vấn không hợp lệ. Viết unit test cho logic phát hiện ngôn ngữ: ưu tiên ngôn ngữ đã lưu, sau đó là Accept-Language, mặc định là Tiếng Việt, chuyển đổi ngôn ngữ không cần tải lại trang. Viết test cho cấu hình SEO: kiểm tra thẻ `hreflang` và thẻ `<html lang="...">` được tạo đúng cho 3 ngôn ngữ (en, vi, es). Đảm bảo độ phủ mã ít nhất 85% cho các thành phần liên quan.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Kiểm tra chất lượng mã nguồn chatbot và bản địa hóa
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-019], [REQ-022], [REQ-023], [NFR-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/chatbot-service/`; `./sources/frontend/web/src/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho chatbot service và các thành phần frontend liên quan đến bản địa hóa/SEO, kiểm tra logic xử lý truy vấn chatbot hoạt động đúng, logic chuyển tiếp cho hỗ trợ con người hoạt động chính xác khi độ tin cậy thấp, logic phát hiện ngôn ngữ hoạt động đúng, cấu hình SEO đầy đủ cho 3 ngôn ngữ, không có lỗi bảo mật (XSS khi hiển thị nội dung chatbot), tuân thủ yêu cầu đa ngôn ngữ [NFR-007]. Đề xuất và thực hiện sửa lỗi nếu có.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 4: Viết tài liệu tích hợp chatbot và hướng dẫn bản địa hóa/SEO
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [REQ-019], [REQ-022], [REQ-023]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/chatbot-integration.md`; `./sources/docs/architecture/localization-seo-guide.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn tích hợp chatbot AI, bao gồm cấu hình API key, xử lý truy vấn, logic chuyển tiếp cho hỗ trợ con người, xử lý lỗi. Viết tài liệu hướng dẫn bản địa hóa và SEO, bao gồm cách thêm ngôn ngữ mới, cấu hình hreflang, quản lý chuỗi văn bản đa ngôn ngữ, kiểm tra cấu hình SEO cho từng ngôn ngữ.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 3: Triển khai giao diện di động vai trò và thông báo đẩy
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai giao diện di động vai trò và tích hợp thông báo đẩy
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-020], [REQ-021]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/frontend/mobile-app/src/screens/StudentDashboard.tsx`; `./sources/frontend/mobile-app/src/screens/TeacherDashboard.tsx`; `./sources/frontend/mobile-app/src/screens/AdminDashboard.tsx`; `./sources/frontend/mobile-app/src/services/NotificationService.ts`; `./sources/frontend/mobile-app/src/components/AttendanceScanner.tsx`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai giao diện người dùng đáp ứng cho từng vai trò trên ứng dụng di động:
  * Student: màn hình duyệt khóa học, đăng ký khóa học, xem thẻ hội viên (ngày còn lại), quét mã QR điểm danh, xem lịch sử điểm danh.
  * Teacher: màn hình xem danh sách khóa học được phân công, danh sách học viên, lịch dạy, điểm danh học viên.
  * Admin: màn hình quản lý trung tâm, quản lý khóa học, quản lý người dùng, tạo thông báo, xem báo cáo.
  Tích hợp FCM/APNs: xử lý đăng ký token thiết bị khi người dùng đăng nhập, nhận và hiển thị thông báo đẩy cho xác nhận điểm danh, thông báo mới, nhắc nhở khóa học. Đảm bảo giao diện hoạt động mượt mà trên cả Android và iOS, đồng bộ chức năng với phiên bản web.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Coder không thực hiện viết hợp đồng API cho tác vụ này.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Không có ngoại lệ nghiệp vụ đặc thù được gán cho tác vụ này.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Viết unit và integration test cho ứng dụng di động
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-020], [REQ-021]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/frontend/mobile-app/src/test/screens/StudentDashboard.test.tsx`; `./sources/frontend/mobile-app/src/test/screens/TeacherDashboard.test.tsx`; `./sources/frontend/mobile-app/src/test/services/NotificationService.test.ts`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các thành phần giao diện di động: kiểm tra menu điều hướng hiển thị đúng theo vai trò người dùng, các màn hình chức năng hoạt động đúng (duyệt khóa học, xem thẻ hội viên, quét mã QR điểm danh). Viết integration test cho luồng thông báo đẩy: đăng ký token thiết bị thành công, nhận thông báo đẩy khi có sự kiện mới, hiển thị thông báo đúng trên giao diện. Kiểm tra giao diện hoạt động đúng trên các kích thước màn hình khác nhau. Đảm bảo độ phủ mã ít nhất 80% cho các thành phần di động.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Kiểm tra chất lượng mã nguồn ứng dụng di động
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-020], [REQ-021], [NFR-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/frontend/mobile-app/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn ứng dụng di động, kiểm tra giao diện đáp ứng hoạt động đúng trên Android và iOS, logic hiển thị theo vai trò người dùng chính xác, tích hợp thông báo đẩy hoạt động đúng, tuân thủ yêu cầu đa ngôn ngữ [NFR-007], không có lỗi hiệu suất (tiêu tốn nhiều tài nguyên, phản hồi chậm). Kiểm tra logic quét mã QR điểm danh tích hợp với backend hoạt động đúng. Đề xuất và thực hiện sửa lỗi nếu có.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 4: Viết tài liệu hướng dẫn sử dụng ứng dụng di động
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [REQ-020], [REQ-021]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/mobile-app-guide.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn sử dụng ứng dụng di động cho từng vai trò người dùng (Student, Teacher, Admin), bao gồm hướng dẫn đăng ký, đăng nhập, sử dụng các chức năng chính (duyệt khóa học, điểm danh, xem thẻ hội viên, nhận thông báo). Viết hướng dẫn cài đặt ứng dụng trên Android và iOS, cấu hình thông báo đẩy.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 Ngày 4: Triển khai dịch vụ báo cáo và hoàn thiện tích hợp giai đoạn
<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 1: Triển khai API báo cáo điểm danh và dashboard ghi danh
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Coder]
* **ID Thẻ mục tiêu:** [REQ-024], [REQ-025], [EXC-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/report-service/src/main/java/com/membershiphub/report/ReportController.java`; `./sources/backend/report-service/src/main/java/com/membershiphub/report/ReportService.java`; `./sources/backend/report-service/src/main/java/com/membershiphub/report/AttendanceCsvExporter.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai API `GET /api/v1/reports/attendance/daily` để tạo báo cáo điểm danh hàng ngày cho trung tâm định dạng CSV, bao gồm các cột: StudentName, CourseName, AttendanceDate, Status (Present/Absent/Late). Triển khai API `GET /api/v1/reports/dashboard/enrollment` để trả về dữ liệu tổng hợp cho dashboard: tổng số học viên đã đăng ký, số khóa học đang hoạt động, số buổi học sắp tới trong 7 ngày tiếp theo. Triển khai logic xử lý hàng đợi điểm danh chờ sau sự cố hệ thống [EXC-005]: xử lý các yêu cầu điểm danh đang lưu trong hàng đợi Redis theo thứ tự FIFO, đồng bộ với cơ sở dữ liệu chính, gửi thông báo cho người dùng về các sự kiện đã được xử lý.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:**
  ```json
  {
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
  ```
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Triển khai xử lý ngoại lệ [EXC-005] trả về mã lỗi 503 Service Unavailable với thông báo "Hệ thống đang khôi phục sau sự cố, vui lòng thử lại sau" nếu hàng đợi điểm danh chưa được xử lý xong. Sau khi xử lý xong, gửi thông báo cho người dùng về các sự kiện đã được xử lý.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 2: Viết unit và integration test cho dịch vụ báo cáo
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Tester]
* **ID Thẻ mục tiêu:** [REQ-024], [REQ-025], [EXC-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/report-service/src/test/java/com/membershiphub/report/ReportServiceTest.java`; `./sources/backend/report-service/src/test/java/com/membershiphub/report/ReportIntegrationTest.java`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết unit test cho các trường hợp: tạo báo cáo điểm danh CSV thành công với dữ liệu chính xác, lấy dữ liệu dashboard thành công với các giá trị tổng hợp đúng, xử lý hàng đợi điểm danh chờ sau sự cố theo thứ tự FIFO, đồng bộ dữ liệu chính xác. Viết integration test cho luồng tạo báo cáo: gửi yêu cầu với centerId và date hợp lệ -> kiểm tra file CSV được tạo đúng định dạng, dữ liệu chính xác. Kiểm tra các trường hợp lỗi: centerId không tồn tại, date không hợp lệ. Đảm bảo độ phủ mã ít nhất 85% cho các lớp service.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Tester không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 3: Kiểm tra chất lượng mã nguồn dịch vụ báo cáo
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [REQ-024], [REQ-025], [EXC-005], [NFR-001]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/backend/report-service/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện code review cho toàn bộ mã nguồn report-service, kiểm tra logic tạo báo cáo CSV hoạt động đúng, logic tổng hợp dữ liệu dashboard chính xác, logic xử lý hàng đợi sau sự cố hoạt động đúng theo thứ tự FIFO, tối ưu truy vấn cơ sở dữ liệu để đảm bảo độ trễ API trung bình dưới 200ms [NFR-001], không có lỗi bảo mật (SQL injection, XSS). Đề xuất và thực hiện sửa lỗi nếu có.
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết hợp đồng API.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Reviewer không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 Phụ công việc 4: Hoàn thiện tài liệu và xác nhận tích hợp giai đoạn
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/architecture/report-service-api.md`; `./sources/docs/architecture/system-overview.md`; `./sources/docs/architecture/integration-guide.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu chi tiết hợp đồng API REST cho report-service, bao gồm endpoint tạo báo cáo điểm danh và dashboard ghi danh, schema request/response, mã lỗi, ví dụ sử dụng, định dạng file CSV. Cập nhật tài liệu kiến trúc tổng quan hệ thống với tất cả các dịch vụ mới được triển khai trong giai đoạn 4. Viết tài liệu hướng dẫn tích hợp giữa các microservice (notification, promotion, chatbot, report) và giao diện người dùng (web, mobile).
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Đại lý phụ Doc không thực hiện viết trình xử lý ngoại lệ.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--END_PHASE_INDEX-->
<!--END_PART_2_PHASE_LOOP-->

### 📈 GIAI ĐOẠN 5 - Triển khai hạ tầng DevOps và đáp ứng yêu cầu phi chức năng
- **Mục tiêu cốt lõi của giai đoạn & Mục đích:** Triển khai toàn bộ hạ tầng DevOps bao gồm Docker đa giai đoạn, pipeline CI/CD với GitHub Actions, cấu hình GCP (VPC, IAM, Storage), triển khai GKE với HPA, cấu hình backup, disaster recovery, mã hóa dữ liệu, logging và audit để đáp ứng các yêu cầu phi chức năng về hiệu suất, khả năng mở rộng, bảo mật và tuân thủ.
- **Bản đồ ma trận thư mục vật lý mục tiêu:** 
  * `./sources/infra/docker/` [NFR-005]
  * `./sources/infra/gcp/` [NFR-002], [NFR-003], [NFR-008], [NFR-009]
  * `./sources/infra/gke/` [NFR-002], [NFR-004]
  * `./sources/infra/github-actions/` [NFR-001], [NFR-005], [NFR-006], [NFR-007]
  * `./sources/infra/monitoring/` [NFR-006]
  * `./sources/docs/infrastructure/` [ARC-010]
- **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE] Giai đoạn này tập trung vào hạ tầng DevOps, không có thay đổi schema cơ sở dữ liệu.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE] Giai đoạn này không triển khai API mới, chỉ cấu hình hạ tầng triển khai.
- **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE] Giai đoạn này không xử lý ngoại lệ nghiệp vụ, chỉ cấu hình hạ tầng.

#### 📅 Nhật ký Phân phối Tác vụ Đại lý phụ theo Thứ tự Thời gian (Giai đoạn 5)

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 1: Thiết lập Docker đa giai đoạn và hạ tầng cơ sở GCP

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 1: Xây dựng Dockerfile đa giai đoạn cho tất cả service backend
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Docker]
* **ID Thẻ mục tiêu:** [NFR-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/docker/user-service/Dockerfile`; `./sources/infra/docker/center-service/Dockerfile`; `./sources/infra/docker/course-service/Dockerfile`; `./sources/infra/docker/enrollment-service/Dockerfile`; `./sources/infra/docker/attendance-service/Dockerfile`; `./sources/infra/docker/card-service/Dockerfile`; `./sources/infra/docker/notification-service/Dockerfile`; `./sources/infra/docker/promotion-service/Dockerfile`; `./sources/infra/docker/report-service/Dockerfile`; `./sources/infra/docker/chatbot-service/Dockerfile`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Xây dựng Dockerfile đa giai đoạn cho tất cả 9 service backend sử dụng base image JDK 21 slim, tối ưu kích thước hình ảnh dưới 200MB, cấu hình biến môi trường cho kết nối cơ sở dữ liệu, cổng ứng dụng và cấu hình xác thực. Sử dụng multi-stage build để tách biệt giai đoạn build và runtime, chỉ giữ lại các thư viện cần thiết trong hình ảnh cuối cùng.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 2: Cấu hình Docker Compose cho môi trường phát triển cục bộ
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Docker]
* **ID Thẻ mục tiêu:** [NFR-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/docker-compose.yml`; `./sources/infra/docker/.env.example`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo file docker-compose.yml để khởi chạy toàn bộ hệ thống cục bộ bao gồm: 9 backend services, PostgreSQL, Redis, Zalo API mock, Firebase Auth mock. Cấu hình network nội bộ, volume cho dữ liệu persistent, biến môi trường cho kết nối giữa các services. Đảm bảo có thể khởi chạy toàn bộ hệ thống với lệnh `docker-compose up`.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 3: Cấu hình hạ tầng cơ sở GCP (VPC, IAM, Service Accounts)
* **Chuyên môn Luồng công việc của Đại lý phụ:** [GCP]
* **ID Thẻ mục tiêu:** [NFR-002], [NFR-003], [NFR-008]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/gcp/vpc.tf`; `./sources/infra/gcp/iam.tf`; `./sources/infra/gcp/service-accounts.tf`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình VPC network với subnet công khai và riêng tư, firewall rules cho phép traffic đến các service backend trên cổng 8080 và 8443, traffic đến PostgreSQL trên cổng 5432, traffic đến Redis trên cổng 6379. Tạo service accounts cho từng service backend với quyền hạn tối thiểu theo nguyên tắc least privilege. Cấu hình IAM roles cho System Admin, Center Admin để quản lý tài nguyên GCP.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 4: Viết tài liệu hướng dẫn triển khai hạ tầng cơ sở
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Doc]
* **ID Thẻ mục tiêu:** [ARC-010], [NFR-002], [NFR-003]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/docs/infrastructure/gcp-setup.md`; `./sources/docs/infrastructure/docker-setup.md`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn cấu hình hạ tầng GCP bao gồm: tạo project, cấu hình VPC, tạo service accounts, cấu hình IAM. Viết hướng dẫn sử dụng Docker và Docker Compose cho môi trường phát triển cục bộ, bao gồm cách khởi chạy, dừng, xem log, debug các service.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 2: Triển khai GKE cluster và CI/CD pipeline

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 1: Tạo và cấu hình GKE cluster với networking
* **Chuyên môn Luồng công việc của Đại lý phụ:** [GKE]
* **ID Thẻ mục tiêu:** [NFR-002], [NFR-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/gke/cluster.tf`; `./sources/infra/gke/node-pools.tf`; `./sources/infra/gke/network-policy.yaml`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo GKE cluster với 3 node pools: general-purpose (2 nodes), high-memory (2 nodes) cho reporting, high-cpu (2 nodes) cho chatbot. Cấu hình network policy để kiểm soát traffic giữa các service, cấu hình private cluster với authorized networks, cấu hình Workload Identity để service accounts GCP có thể truy cập các dịch vụ khác mà không cần quản lý credentials.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 2: Cấu hình HPA và Kubernetes deployment manifests
* **Chuyên môn Luồng công việc của Đại lý phụ:** [GKE]
* **ID Thẻ mục tiêu:** [NFR-001], [NFR-004]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/gke/deployments/`; `./sources/infra/gke/hpa.yaml`; `./sources/infra/gke/services.yaml`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo Kubernetes deployment manifests cho tất cả 9 backend services với resource requests/limits, liveness và readiness probes, cấu hình HPA (Horizontal Pod Autoscaler) cho mỗi service dựa trên CPU > 70% hoặc request latency > 300ms. Tạo Service manifests (ClusterIP) cho internal communication và Ingress cho external access. Cấu hình resource quotas và limit ranges cho namespace.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 3: Cấu hình Cloud Storage, backup và disaster recovery
* **Chuyên môn Luồng công việc của Đại lý phụ:** [GCP]
* **ID Thẻ mục tiêu:** [NFR-002], [NFR-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/gcp/storage.tf`; `./sources/infra/gcp/backup-scheduler.tf`; `./sources/infra/gcp/disaster-recovery.tf`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình Cloud Storage buckets cho lưu trữ backup PostgreSQL, logs, và artifacts. Tạo Cloud Scheduler để thực hiện backup PostgreSQL hàng ngày lúc 2:00 AM, lưu backup trong 30 ngày. Cấu hình Cloud SQL instance với high availability (regional), automatic failover, point-in-time recovery up to 24 hours. Tạo script disaster recovery để restore từ backup sang region phụ.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 4: Cấu hình CI/CD pipeline với GitHub Actions
* **Chuyên môn Luồng công việc của Đại lý phụ:** [GCP]
* **ID Thẻ mục tiêu:** [NFR-001], [NFR-005], [NFR-006], [NFR-007]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/github-actions/`; `./sources/infra/gcp/cloudbuild.yaml`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình GitHub Actions workflow cho CI/CD: trigger trên push đến main branch, chạy unit tests và integration tests, build Docker images đa giai đoạn, push lên Google Container Registry (GCR), deploy lên GKE. Cấu hình caching để tăng tốc độ build, cấu hình secrets cho GCP credentials, Docker registry credentials. Cấu hình approval gate trước khi deploy lên production. Cấu hình pipeline để xử lý bản địa hóa đa ngôn ngữ: build và deploy các bản dịch, kiểm tra tất cả các chuỗi văn bản được externalized đúng cách [NFR-007].
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

<!--START_DAY_LOG_INDEX-->
##### 📅 NGÀY 3: Bảo mật, logging, audit và tối ưu cuối cùng

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 1: Cấu hình mã hóa dữ liệu và bảo mật hạ tầng
* **Chuyên môn Luồng công việc của Đại lý phụ:** [GCP]
* **ID Thẻ mục tiêu:** [NFR-003], [NFR-008]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/gcp/encryption.tf`; `./sources/infra/gke/security-policies.yaml`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình mã hóa dữ liệu at rest sử dụng AES-256 cho Cloud Storage, Cloud SQL, và Persistent Disks. Cấu hình mã hóa dữ liệu in transit sử dụng TLS 1.3 cho tất cả các endpoint. Cấu hình Cloud KMS để quản lý encryption keys. Cấu hình GKE security policies: Pod Security Standards (restricted), seccomp profiles, AppArmor, network policies để hạn chế lateral movement. Cấu hình Cloud IAP để bảo vệ access đến GKE dashboard.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 2: Cấu hình logging, monitoring và audit trail
* **Chuyên môn Luồng công việc của Đại lý phụ:** [GKE]
* **ID Thẻ mục tiêu:** [NFR-006], [NFR-002]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/gke/logging-config.yaml`; `./sources/infra/gcp/audit-logging.tf`; `./sources/infra/monitoring/`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình Cloud Logging cho GKE cluster để thu thập logs từ tất cả các pods, nodes, và system components. Cấu hình log retention 1 năm cho audit logs. Cấu hình Cloud Monitoring với dashboards cho CPU, memory, request latency, error rates. Cấu hình alerting policies cho các ngưỡng: CPU > 70%, memory > 80%, request latency > 300ms, error rate > 1%. Cấu hình audit logging cho tất cả các hành động quản trị GCP và GKE.
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 3: Tối ưu kích thước hình ảnh Docker và đẩy lên registry
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Docker]
* **ID Thẻ mục tiêu:** [NFR-005]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** `./sources/infra/docker/`; `./sources/infra/gcp/artifact-registry.tf`
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tối ưu kích thước hình ảnh Docker cho tất cả các services: sử dụng base image nhỏ (JDK 21 slim), loại bỏ các file không cần thiết, sử dụng layer caching hiệu quả. Đẩy tất cả hình ảnh lên Google Artifact Registry, cấu hình vulnerability scanning cho các hình ảnh. Đảm bảo kích thước hình ảnh cuối cùng dưới 500MB [NFR-005].
<!--END_ATOMIC_SUB_TASK_NODE-->

<!--START_ATOMIC_SUB_TASK_NODE-->
###### 🌿 PHỤ CÔNG VIỆC 4: Kiểm tra cuối cùng và xác nhận hoàn thành giai đoạn 5
* **Chuyên môn Luồng công việc của Đại lý phụ:** [Reviewer]
* **ID Thẻ mục tiêu:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
* **Đường dẫn tệp thành phần mục tiêu (target_component):** Toàn bộ mã nguồn và cấu hình hạ tầng trong ./sources/infra/
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra cuối cùng toàn bộ hạ tầng DevOps: kiểm tra tất cả Docker images có thể build thành công và kích thước trong giới hạn, kiểm tra GKE cluster khởi chạy đúng, tất cả services deploy thành công, HPA hoạt động đúng, CI/CD pipeline chạy thành công, backup và disaster recovery được cấu hình đúng, mã hóa dữ liệu được bật, logging và monitoring hoạt động, tất cả yêu cầu phi chức năng được đáp ứng. Xác nhận giai đoạn sẵn sàng cho vận hành production.
<!--END_ATOMIC_SUB_TASK_NODE-->
<!--END_DAY_LOG_INDEX-->

### 🕵️ BÁO CÁO KIỂM TOÁN CHÉO KIẾN TRÚC THỜI GIAN THỰC

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=7
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=28
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=64
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

### BỐI CẢNH NỀN TẢNG TỪ CÁC BƯỚC TRƯỚC

## ☣️ 6. MÃ BẢO MẬT DOANH NGHIỆP PHỔ QUÁT & BIỆN PHÁP CHỐNG INJECTION [NFR-XXX]
- **Biện pháp chống SQL Injection (SQLi) tuyệt đối:** Tham số quy tắc cho câu lệnh chuẩn bị, tham số truy vấn theo vị trí và danh sách cho phép đầu vào sắp xếp động.
- **Cross-Site Scripting (XSS) & Chính sách bảo mật nội dung (CSP):** Tiêu chuẩn bố cục cho việc làm sạch ngữ cảnh tự động, tự động escape JSX và tiêm động các tiêu đề CSP nghiêm ngặt (hạn chế `unsafe-inline`).
- **Đường ray bảo mật CORS đa tenant:** Cấu hình cho các lệnh cấm ký tự đại diện nguồn gốc và xác thực động số liệu cơ sở dữ liệu nguồn gốc của tenant.
- **Công cụ làm sạch log không rò rỉ & che giấu dữ liệu PII:** Quy tắc cho các trình chặn che giấu tự động (`@JsonSerialize`) và ngưỡng làm sạch log.

## 📱 7. QUY TẮC TUÂN THỦ DI ĐỘNG HYBRID & CƠ CHẾ SEO ĐA NGÔN NGỮ
- **Đường ray tuân thủ di động hybrid Capacitor:** [Nếu di động hoạt động] Quy tắc cho việc lấy dữ liệu động phía máy khách, địa chỉ URL tuyệt đối, bảo vệ hydration, trừu tượng lưu trữ gốc (`@capacitor/preferences`) và chặn nút quay lại phần cứng.
- **Bản địa hóa (i18n) & Tiêm động SEO:** Kiến trúc middleware nhận dạng locale ở lớp edge, tiêm động điều khiển siêu phương tiện hreflang và giới hạn lập chỉ mục của crawler tìm kiếm.

## 🚀 8. LUỒNG NHÁNH GIT PHIÊN LÀM VIỆC HÀNG NGÀY TỰ ĐỘNG TRONG PIPELINE
- **Cô lập phân nhánh không gian làm việc hàng ngày:** Điều khiển phân nhánh lập trình cho nhánh `features/development-phase-X-day-Y` (`X` là số giai đoạn, từ 1 đến N, với N <= 5; `Y` là số ngày trong giai đoạn, bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng bảo vệ xác thực pipeline:** Quy tắc thực thi cho xác minh biên dịch, mục tiêu độ phủ mã tự động (`>= 85%`) và log tuần tự hóa tóm tắt ngữ cảnh.

### 📊 MANDATE KIỂM TRA PHỦ COVERAGE MA TRẬN

`[THỰC THI MA TRẬN TRUY XUẤT: 100% PHỦ COVERAGE ĐÃ ĐƯỢC XÁC NHẬN. TỔNG SỐ THẺ REQ DUY NHẤT ĐÃ ÁNH XẠ: 25, TỔNG SỐ THẺ ARC: 10, TỔNG SỐ THẺ EXC: 5, TỔNG SỐ THẺ DAT: 9, TỔNG SỐ THẺ NFR: 9. KHÔNG CÓ MÃ NÀO CHƯA ĐƯỢC GÁN.]`