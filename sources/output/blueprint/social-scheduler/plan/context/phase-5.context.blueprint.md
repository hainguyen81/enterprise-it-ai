# Giai đoạn 5: Triển khai và tài liệu hệ thống

## 📊 Tài liệu kiểm soát

| Mục | Chi tiết |
| :--- | :--- |
| **Mã sơ đồ** | ARCH-20260911204512 |
| **Tên dự án** | social-scheduler |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai và tài liệu hệ thống<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai hệ thống và tạo tài liệu kỹ thuật cho hệ thống. Giai đoạn này tập trung vào việc triển khai hệ thống và tạo tài liệu kỹ thuật để đảm bảo hệ thống hoạt động đúng cách và dễ dàng bảo trì.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/09/11 20:45:12 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Triển khai hệ thống và tạo tài liệu kỹ thuật cho hệ thống. Giai đoạn này tập trung vào việc triển khai hệ thống và tạo tài liệu kỹ thuật để đảm bảo hệ thống hoạt động đúng cách và dễ dàng bảo trì.

## 2. Phạm vi kỹ thuật cho phép và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Mã thông báo cốt lõi của khung nền tảng**:
  - Khi khởi tạo sơ đồ hoạt động vòng đời (đặc biệt trong Giai đoạn 1 - NGÀY 1), bạn phải chèn và khai báo các mô tả xây dựng kho lưu trữ chính trước khi phát hành bất kỳ thành phần nguồn ứng dụng nào.
  - Đối với các kiến trúc dịch vụ vi mô, bạn phải thực hiện việc định nghĩa đường dẫn bắt buộc của một mô tả dự án cha `./sources/backend/pom.xml` và các mô tả mô-đun con cô lập `./sources/backend/<service-name>/pom.xml`.
  - Đối với các ứng dụng giao diện người dùng hoạt động, bạn phải thực hiện việc đăng ký đường dẫn cấu hình rõ ràng của `./sources/frontend/package.json` và `./sources/frontend/tsconfig.json`. Tất cả các tài sản xây dựng được tạo ra phải ánh xạ nghiêm ngặt với mã theo dõi hệ thống kiến trúc `[ARC-000]`.

## 3. Hướng dẫn chức năng của các Sub-Agent chuyên dụng
- **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chính. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và các ứng dụng frontend/mobile. Bị cấm viết bộ kiểm thử hoặc tài liệu cơ sở hạ tầng.
- **Tester**: Hoạt động như một Nhà kiểm thử QC/QA Cấp cao/Chính. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng kiểm tra chất lượng. Trách nhiệm là tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử tự động E2E và kịch bản xác nhận hiệu suất. Bị cấm sửa đổi mã sản xuất ứng dụng. Nếu nhiệm vụ con mục tiêu liên quan đến phạm vi tích hợp hoặc điểm cuối-to-end mà không có tệp mã nguồn cụ thể nào có thể bị giới hạn, bạn phải xuất ra mã thông báo `INTEGRATION_SCOPE` như tham số đầu tiên của cặp dấu chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
- **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tham chiếu lược đồ, sơ đồ hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp công nghệ hoạt động của dự án. Mỗi tệp tài liệu kỹ thuật được tạo ra phải được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
- **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, sửa các lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
- **Docker**: Chuyên về việc đóng gói, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
- **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container trên Google Cloud Run.
- **GKE**: Chuyên về điều phối sản xuất container trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các khối lượng công việc dịch vụ vi mô vào các cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này.
- Đảm bảo tuân thủ các tiêu chuẩn doanh nghiệp OWASP.
- Đảm bảo bao phủ kiểm thử chức năng hoàn chỉnh cho các yêu cầu được phân bổ.
- Đảm bảo ánh xạ 100% các mã theo dõi Tag ID.

## 5. Nhật ký thực hiện kiến trúc hàng ngày

### 🌤️ NGÀY 1: Triển khai hệ thống
<!--DAY_HEADER_START-->Triển khai hệ thống<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 1.1: Triển khai hệ thống
##### Chuyên môn công việc của Sub-Agent: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/devops/docker-compose.yml`

* **Mã theo dõi mục tiêu:**
<!--START_TAGS-->[EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai hệ thống sử dụng Docker Compose. Đảm bảo tất cả các dịch vụ được triển khai đúng cách và hệ thống hoạt động đúng cách.

### 🌤️ NGÀY 2: Tạo tài liệu kỹ thuật
<!--DAY_HEADER_START-->Tạo tài liệu kỹ thuật<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 2.1: Tạo tài liệu kỹ thuật
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:**
<!--START_TAGS-->[DOC-001]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho hệ thống. Đảm bảo tài liệu kỹ thuật bao gồm tất cả các thông tin cần thiết để hiểu và bảo trì hệ thống.