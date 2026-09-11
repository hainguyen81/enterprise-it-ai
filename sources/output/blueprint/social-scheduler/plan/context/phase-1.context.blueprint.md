# Giai đoạn 1: Thiết lập cơ sở hạ tầng và xác thực

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã sơ đồ** | ARCH-20260911101625 |
| **Tên dự án** | social-scheduler |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Thiết lập cơ sở hạ tầng và xác thực<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc thiết lập cơ sở hạ tầng cơ bản và xác thực cho hệ thống.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/09/11 10:16:25 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc thiết lập cơ sở hạ tầng cơ bản và xác thực cho hệ thống. Các nhiệm vụ bao gồm:
- Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.
- Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok.
- Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó.
- Thực hiện xác thực đầu vào dữ liệu và kiểm tra giới hạn tỷ lệ cho từng người dùng.

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Ma trận thư mục cho phép**:
  - `./sources/backend/pom.xml`
  - `./sources/backend/scheduling-service/pom.xml`
  - `./sources/backend/content-service/pom.xml`
  - `./sources/backend/auth-service/pom.xml`
  - `./sources/docs/technical-documentation.md`
  - `./sources/infra/devops/docker-compose.yml`
  - `./sources/infra/devops/kubernetes-deployment.yaml`

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

### 🌤️ NGÀY 1: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống

#### 📝 NHIỆM VỤ CON 1.1: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/pom.xml`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

#### 📝 NHIỆM VỤ CON 1.2: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/pom.xml;./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/SchedulingServiceTest.java`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

#### 📝 NHIỆM VỤ CON 1.3: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/pom.xml`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

#### 📝 NHIỆM VỤ CON 1.4: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/pom.xml`

* **Mã theo dõi mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

### 🌤️ NGÀY 2: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống

#### 📝 NHIỆM VỤ CON 2.1: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/pom.xml`

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

#### 📝 NHIỆM VỤ CON 2.2: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/pom.xml;./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/SchedulingServiceTest.java`

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

#### 📝 NHIỆM VỤ CON 2.3: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/pom.xml`

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.

#### 📝 NHIỆM VỤ CON 2.4: Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/pom.xml`

* **Mã theo dõi mục tiêu:** [DAT-001], [DAT-002], [DAT-003]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Khởi tạo cơ sở dữ liệu và thiết lập mã thông báo cho hệ thống.