# Giai đoạn 4: Kiến trúc và triển khai dịch vụ xác thực và giới hạn tỷ lệ

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã sơ đồ** | ARCH-20260911101625 |
| **Tên dự án** | social-scheduler |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Kiến trúc và triển khai dịch vụ xác thực và giới hạn tỷ lệ<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc triển khai dịch vụ xác thực và giới hạn tỷ lệ, bao gồm việc thiết lập cơ sở dữ liệu, xác thực mã thông báo và triển khai các điểm cuối API. Giai đoạn này đảm bảo rằng hệ thống có thể xác thực người dùng và giới hạn số lần gọi API mỗi phút để ngăn chặn lạm dụng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/09/11 10:16:25 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc triển khai dịch vụ xác thực và giới hạn tỷ lệ, bao gồm việc thiết lập cơ sở dữ liệu, xác thực mã thông báo và triển khai các điểm cuối API. Giai đoạn này đảm bảo rằng hệ thống có thể xác thực người dùng và giới hạn số lần gọi API mỗi phút để ngăn chặn lạm dụng.

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Ma trận thư mục cho phép**:
  - `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/entity/User.java`
  - `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/AuthService.java`
  - `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/controller/AuthController.java`
  - `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/RateLimitService.java`
  - `./sources/docs/technical-documentation.md`

## 3. Hướng dẫn chức năng của các Sub-Agent
- **Coder**: Hoạt động như một Nhà phát triển ứng dụng cấp cao/Chủ tịch. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và các ứng dụng máy khách frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
- **Tester**: Hoạt động như một Trưởng/QA/QC cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng kiểm tra chất lượng. Trách nhiệm là tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử tự động E2E và các kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu nhiệm vụ con mục tiêu liên quan đến phạm vi tích hợp hoặc điểm cuối-to-end mà không có tệp mã cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất ra mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp dấu chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
- **Doc**: Chức năng như một Nhà viết tài liệu kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn các tài liệu Quy cách kỹ thuật toàn diện, tham chiếu lược đồ, sơ đồ hệ thống và danh mục kiến trúc doanh nghiệp được tùy chỉnh phù hợp với các lớp công nghệ hoạt động của dự án. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
- **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, sửa các lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
- **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
- **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container tự nhiên trên Google Cloud Run.
- **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các khối lượng công việc dịch vụ vi mô vào các cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các nhiệm vụ được phân phối cho giai đoạn này.
- Đảm bảo tuân thủ các tiêu chuẩn doanh nghiệp OWASP.
- Đảm bảo hoàn thành kiểm tra chức năng cho các yêu cầu được phân phối.
- Đảm bảo ánh xạ 100% các mã theo dõi.

## 5. Nhật ký thực hiện kiến trúc hàng ngày

### 🌤️ NGÀY 1: Triển khai cơ sở dữ liệu và xác thực mã thông báo

#### 📝 NHIỆM VỤ CON 1.1: Triển khai cơ sở dữ liệu cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/entity/User.java`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai lớp thực thể User cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các trường như userId, username, password, email và role.

#### 📝 NHIỆM VỤ CON 1.2: Triển khai cơ sở dữ liệu cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/entity/User.java;./sources/backend/auth-service/src/test/java/org/nlh4j/socialscheduler/authservice/entity/UserTest.java`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử lớp thực thể User để đảm bảo nó có thể ánh xạ với các bảng cơ sở dữ liệu tương ứng và lưu trữ các thông tin người dùng một cách hiệu quả. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 1.3: Triển khai cơ sở dữ liệu cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/entity/User.java`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho lớp thực thể User. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 1.4: Triển khai cơ sở dữ liệu cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho lớp thực thể User. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng lớp thực thể.

### 🌤️ NGÀY 2: Triển khai xác thực mã thông báo và các điểm cuối API

#### 📝 NHIỆM VỤ CON 2.1: Triển khai xác thực mã thông báo cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/AuthService.java`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai dịch vụ xác thực mã thông báo cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các phương thức như authenticate, generateToken, refreshToken và validateToken.

#### 📝 NHIỆM VỤ CON 2.2: Triển khai xác thực mã thông báo cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/AuthService.java;./sources/backend/auth-service/src/test/java/org/nlh4j/socialscheduler/authservice/service/AuthServiceTest.java`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử dịch vụ xác thực mã thông báo để đảm bảo nó có thể xác thực người dùng và tạo mã thông báo một cách hiệu quả. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 2.3: Triển khai xác thực mã thông báo cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/AuthService.java`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho dịch vụ xác thực mã thông báo. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 2.4: Triển khai xác thực mã thông báo cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho dịch vụ xác thực mã thông báo. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng dịch vụ.

### 🌤️ NGÀY 3: Triển khai các điểm cuối API và kiểm tra giới hạn tỷ lệ

#### 📝 NHIỆM VỤ CON 3.1: Triển khai điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/controller/AuthController.java`

* **Mã theo dõi mục tiêu:** [REQ-003], [ARC-006]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các điểm cuối như /authenticate, /generate-token, /refresh-token và /validate-token.

#### 📝 NHIỆM VỤ CON 3.2: Triển khai điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/controller/AuthController.java;./sources/backend/auth-service/src/test/java/org/nlh4j/socialscheduler/authservice/controller/AuthControllerTest.java`

* **Mã theo dõi mục tiêu:** [REQ-003], [ARC-006]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ để đảm bảo nó có thể xác thực người dùng và tạo mã thông báo một cách hiệu quả. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 3.3: Triển khai điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/controller/AuthController.java`

* **Mã theo dõi mục tiêu:** [REQ-003], [ARC-006]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 3.4: Triển khai điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-003], [ARC-006]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho điểm cuối API cho dịch vụ xác thực và giới hạn tỷ lệ. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng điểm cuối API.

### 🌤️ NGÀY 4: Triển khai kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ

#### 📝 NHIỆM VỤ CON 4.1: Triển khai kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/RateLimitService.java`

* **Mã theo dõi mục tiêu:** [REQ-003], [EXC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai dịch vụ kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ, bao gồm các phương thức như checkRateLimit và updateRateLimit.

#### 📝 NHIỆM VỤ CON 4.2: Triển khai kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/RateLimitService.java;./sources/backend/auth-service/src/test/java/org/nlh4j/socialscheduler/authservice/service/RateLimitServiceTest.java`

* **Mã theo dõi mục tiêu:** [REQ-003], [EXC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử dịch vụ kiểm tra giới hạn tỷ lệ để đảm bảo nó có thể kiểm tra và cập nhật giới hạn tỷ lệ một cách hiệu quả. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 4.3: Triển khai kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth-service/src/main/java/org/nlh4j/socialscheduler/authservice/service/RateLimitService.java`

* **Mã theo dõi mục tiêu:** [REQ-003], [EXC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho dịch vụ kiểm tra giới hạn tỷ lệ. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 4.4: Triển khai kiểm tra giới hạn tỷ lệ cho dịch vụ xác thực và giới hạn tỷ lệ
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-003], [EXC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho dịch vụ kiểm tra giới hạn tỷ lệ. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng dịch vụ.