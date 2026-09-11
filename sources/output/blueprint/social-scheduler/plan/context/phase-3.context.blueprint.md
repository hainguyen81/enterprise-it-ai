# Giai đoạn 3: Dịch vụ đề xuất nội dung bằng AI

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã sơ đồ** | ARCH-20260911101625 |
| **Tên dự án** | social-scheduler |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Dịch vụ đề xuất nội dung bằng AI<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó. Giai đoạn này tập trung vào việc phát triển và tích hợp dịch vụ đề xuất nội dung bằng AI, bao gồm việc tạo ra các điểm cuối API, triển khai mô hình học máy và xử lý các ngoại lệ liên quan đến đề xuất nội dung.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/09/11 10:16:25 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó. Giai đoạn này tập trung vào việc phát triển và tích hợp dịch vụ đề xuất nội dung bằng AI, bao gồm việc tạo ra các điểm cuối API, triển khai mô hình học máy và xử lý các ngoại lệ liên quan đến đề xuất nội dung.

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- **Ma trận thư mục cho phép**:
  - `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/controller/ContentController.java`
  - `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/service/ContentService.java`
  - `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepository.java`
  - `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetric.java`
  - `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandler.java`
  - `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/controller/ContentControllerTest.java`
  - `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/service/ContentServiceTest.java`
  - `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepositoryTest.java`
  - `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetricTest.java`
  - `./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandlerTest.java`
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

### 🌤️ NGÀY 1: Triển khai điểm cuối API đề xuất nội dung

#### 📝 NHIỆM VỤ CON 1.1: Triển khai điểm cuối API đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/controller/ContentController.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai điểm cuối API để nhận yêu cầu đề xuất nội dung từ người dùng. Đảm bảo điểm cuối này có thể xử lý các yêu cầu đồng thời và trả về các đề xuất nội dung phù hợp.

#### 📝 NHIỆM VỤ CON 1.2: Triển khai điểm cuối API đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/controller/ContentController.java;./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/controller/ContentControllerTest.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử điểm cuối API đề xuất nội dung để đảm bảo nó có thể xử lý các yêu cầu đồng thời và trả về các đề xuất nội dung phù hợp. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 1.3: Triển khai điểm cuối API đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/controller/ContentController.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho điểm cuối API đề xuất nội dung. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 1.4: Triển khai điểm cuối API đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho điểm cuối API đề xuất nội dung. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng điểm cuối API.

### 🌤️ NGÀY 2: Triển khai dịch vụ đề xuất nội dung

#### 📝 NHIỆM VỤ CON 2.1: Triển khai dịch vụ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/service/ContentService.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai dịch vụ đề xuất nội dung để xử lý logic đề xuất nội dung dựa trên hiệu suất trước đó của các bài đăng. Đảm bảo dịch vụ này có thể tích hợp với các mô hình học máy để tạo ra các đề xuất nội dung phù hợp.

#### 📝 NHIỆM VỤ CON 2.2: Triển khai dịch vụ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/service/ContentService.java;./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/service/ContentServiceTest.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử dịch vụ đề xuất nội dung để đảm bảo nó có thể xử lý logic đề xuất nội dung dựa trên hiệu suất trước đó của các bài đăng. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 2.3: Triển khai dịch vụ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/service/ContentService.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho dịch vụ đề xuất nội dung. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 2.4: Triển khai dịch vụ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho dịch vụ đề xuất nội dung. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng dịch vụ.

### 🌤️ NGÀY 3: Triển khai kho lưu trữ đề xuất nội dung

#### 📝 NHIỆM VỤ CON 3.1: Triển khai kho lưu trữ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepository.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai kho lưu trữ đề xuất nội dung để tương tác với cơ sở dữ liệu và lưu trữ các đề xuất nội dung. Đảm bảo kho lưu trữ này có thể xử lý các truy vấn phức tạp và lưu trữ các đề xuất nội dung một cách hiệu quả.

#### 📝 NHIỆM VỤ CON 3.2: Triển khai kho lưu trữ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepository.java;./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepositoryTest.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử kho lưu trữ đề xuất nội dung để đảm bảo nó có thể tương tác với cơ sở dữ liệu và lưu trữ các đề xuất nội dung. Đảm bảo các trường hợp kiểm thử bao gồm các truy vấn phức tạp và lưu trữ các đề xuất nội dung một cách hiệu quả.

#### 📝 NHIỆM VỤ CON 3.3: Triển khai kho lưu trữ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/repository/ContentRepository.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho kho lưu trữ đề xuất nội dung. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 3.4: Triển khai kho lưu trữ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho kho lưu trữ đề xuất nội dung. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng kho lưu trữ.

### 🌤️ NGÀY 4: Triển khai thực thể hiệu suất bài đăng

#### 📝 NHIỆM VỤ CON 4.1: Triển khai thực thể hiệu suất bài đăng
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetric.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai thực thể hiệu suất bài đăng để lưu trữ các chỉ số hiệu suất của các bài đăng. Đảm bảo thực thể này có thể ánh xạ với các bảng cơ sở dữ liệu tương ứng và lưu trữ các chỉ số hiệu suất một cách hiệu quả.

#### 📝 NHIỆM VỤ CON 4.2: Triển khai thực thể hiệu suất bài đăng
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetric.java;./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetricTest.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử thực thể hiệu suất bài đăng để đảm bảo nó có thể ánh xạ với các bảng cơ sở dữ liệu tương ứng và lưu trữ các chỉ số hiệu suất một cách hiệu quả. Đảm bảo các trường hợp kiểm thử bao gồm các yêu cầu hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 4.3: Triển khai thực thể hiệu suất bài đăng
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/entity/PerformanceMetric.java`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho thực thể hiệu suất bài đăng. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 4.4: Triển khai thực thể hiệu suất bài đăng
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [REQ-002]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho thực thể hiệu suất bài đăng. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng thực thể.

### 🌤️ NGÀY 5: Triển khai bộ xử lý ngoại lệ đề xuất nội dung

#### 📝 NHIỆM VỤ CON 5.1: Triển khai bộ xử lý ngoại lệ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandler.java`

* **Mã theo dõi mục tiêu:** [EXC-003], [EXC-004]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai bộ xử lý ngoại lệ đề xuất nội dung để xử lý các ngoại lệ liên quan đến đề xuất nội dung. Đảm bảo bộ xử lý này có thể ghi lại các ngoại lệ và cung cấp các thông báo lỗi phù hợp cho người dùng.

#### 📝 NHIỆM VỤ CON 5.2: Triển khai bộ xử lý ngoại lệ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandler.java;./sources/backend/content-service/src/test/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandlerTest.java`

* **Mã theo dõi mục tiêu:** [EXC-003], [EXC-004]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Kiểm thử bộ xử lý ngoại lệ đề xuất nội dung để đảm bảo nó có thể ghi lại các ngoại lệ và cung cấp các thông báo lỗi phù hợp cho người dùng. Đảm bảo các trường hợp kiểm thử bao gồm các ngoại lệ hợp lệ và không hợp lệ.

#### 📝 NHIỆM VỤ CON 5.3: Triển khai bộ xử lý ngoại lệ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/content-service/src/main/java/org/nlh4j/socialscheduler/contentservice/exception/ContentExceptionHandler.java`

* **Mã theo dõi mục tiêu:** [EXC-003], [EXC-004]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Đánh giá mã nguồn cho bộ xử lý ngoại lệ đề xuất nội dung. Đảm bảo mã nguồn tuân thủ các tiêu chuẩn lập trình và xử lý các trường hợp ngoại lệ một cách thích hợp.

#### 📝 NHIỆM VỤ CON 5.4: Triển khai bộ xử lý ngoại lệ đề xuất nội dung
##### Chuyên môn công việc của Sub-Agent: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/technical-documentation.md`

* **Mã theo dõi mục tiêu:** [EXC-003], [EXC-004]

* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo tài liệu kỹ thuật cho bộ xử lý ngoại lệ đề xuất nội dung. Đảm bảo tài liệu kỹ thuật bao gồm các thông tin cần thiết để hiểu và sử dụng bộ xử lý.