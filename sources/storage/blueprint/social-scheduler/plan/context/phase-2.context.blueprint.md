# Giai đoạn 2: Dịch vụ Lịch Đăng Bài Tự Động

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã sơ đồ** | ARCH-20260911101625 |
| **Tên dự án** | social-scheduler |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Dịch vụ Lịch Đăng Bài Tự Động<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok. Mục tiêu là thiết lập cơ sở hạ tầng cần thiết để lên lịch và thực hiện các bài đăng tự động trên các nền tảng mạng xã hội.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/09/11 10:16:25 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok. Mục tiêu là thiết lập cơ sở hạ tầng cần thiết để lên lịch và thực hiện các bài đăng tự động trên các nền tảng mạng xã hội.

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Ma trận thư mục cho phép**:
  - `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java`
  - `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java`
  - `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/repository/SchedulingRepository.java`
  - `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/entity/Schedule.java`
  - `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/exception/SchedulingExceptionHandler.java`
  - `./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingControllerTest.java`
  - `./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingServiceTest.java`
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

### 🌤️ NGÀY 1: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

#### 📝 NHIỆM VỤ CON 1.1: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai điểm cuối API để lên lịch các bài đăng trên các nền tảng mạng xã hội. Xử lý các trường hợp ngoại lệ khi tích hợp với API bên thứ ba.

#### 📝 NHIỆM VỤ CON 1.2: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java;./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingControllerTest.java`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết các bài kiểm tra đơn vị và tích hợp cho điểm cuối API lịch đăng bài tự động. Đảm bảo các bài đăng được lên lịch chính xác vào thời điểm đã chỉ định và trạng thái hiển thị là "đã lên lịch".

#### 📝 NHIỆM VỤ CON 1.3: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/controller/SchedulingController.java`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho điểm cuối API lịch đăng bài tự động. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 1.4: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho điểm cuối API lịch đăng bài tự động. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng điểm cuối API.

### 🌤️ NGÀY 2: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok

#### 📝 NHIỆM VỤ CON 2.1: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai dịch vụ để xử lý các yêu cầu lên lịch bài đăng. Xử lý các trường hợp ngoại lệ khi tích hợp với API bên thứ ba.

#### 📝 NHIỆM VỤ CON 2.2: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java;./sources/backend/scheduling-service/src/test/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingServiceTest.java`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ lịch đăng bài tự động. Đảm bảo các bài đăng được lên lịch chính xác vào thời điểm đã chỉ định và trạng thái hiển thị là "đã lên lịch".

#### 📝 NHIỆM VỤ CON 2.3: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/scheduling-service/src/main/java/org/nlh4j/socialscheduler/schedulingservice/service/SchedulingService.java`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho dịch vụ lịch đăng bài tự động. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 2.4: Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-001], [EXC-001], [EXC-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho dịch vụ lịch đăng bài tự động. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng dịch vụ.