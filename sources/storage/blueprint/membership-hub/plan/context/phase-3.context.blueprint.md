# Giai đoạn 3: Quản lý điểm danh và thẻ thành viên

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID bản thiết kế** | ARCH-20260817205646 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Quản lý điểm danh và thẻ thành viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc quản lý điểm danh và thẻ thành viên. Chúng tôi sẽ xây dựng các chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh, xem thông tin thẻ thành viên và gia hạn thẻ thành viên.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/17 20:56:46 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc quản lý điểm danh và thẻ thành viên. Chúng tôi sẽ xây dựng các chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh, xem thông tin thẻ thành viên và gia hạn thẻ thành viên. Các chức năng này bao gồm:

- Quét mã QR để điểm danh
- Đảm bảo tính idempotency cho điểm danh
- Xem thông tin thẻ thành viên
- Gia hạn thẻ thành viên

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/attendance/`
- `./sources/backend/studentcard/`
- `./sources/backend/docs/`

## 3. Hướng dẫn chức năng của các chuyên gia con được chỉ định
- **Coder**: Hoạt động như một Nhà phát triển ứng dụng cấp cao/Chuyên gia. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và các ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
- **Tester**: Hoạt động như một Trưởng/QC/QA cấp cao. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử E2E tự động và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con nhiệm vụ liên quan đến phạm vi tích hợp hoặc end-to-end tổng thể nơi không có tệp mã cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
- **Doc**: Chức năng như một Nhà viết kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về việc biên soạn tài liệu Quy cách kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê dưới dạng thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
- **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh, vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
- **Docker**: Chuyên về việc đóng gói, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
- **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container tự nhiên trên Google Cloud Run.
- **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào các cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các chức năng quét mã QR để điểm danh, đảm bảo tính idempotency cho điểm danh, xem thông tin thẻ thành viên và gia hạn thẻ thành viên.
- Đảm bảo tuân thủ các tiêu chuẩn doanh nghiệp OWASP.
- Hoàn thành 100% bộ kiểm thử chức năng cho các yêu cầu được phân phối.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc hàng ngày

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Xây dựng chức năng quét mã QR để điểm danh<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 1.1: Xây dựng chức năng quét mã QR để điểm danh
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng quét mã QR để điểm danh. Chức năng này sẽ bao gồm việc giải mã mã QR, xác thực thông tin học viên và khóa học, và ghi nhận điểm danh vào cơ sở dữ liệu.

#### 📝 NHIỆM VỤ CON 1.2: Viết kiểm thử cho chức năng quét mã QR để điểm danh
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java;./sources/backend/attendance/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceTest.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng quét mã QR để điểm danh. Kiểm thử sẽ bao gồm việc kiểm tra giải mã mã QR, xác thực thông tin học viên và khóa học, và ghi nhận điểm danh vào cơ sở dữ liệu.

#### 📝 NHIỆM VỤ CON 1.3: Tài liệu chức năng quét mã QR để điểm danh
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/attendance.md

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng quét mã QR để điểm danh. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường đầu vào và các trường hợp kiểm tra.

#### 📝 NHIỆM VỤ CON 1.4: Xây dựng chức năng đảm bảo tính idempotency cho điểm danh
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-013]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng đảm bảo tính idempotency cho điểm danh. Chức năng này sẽ bao gồm việc kiểm tra xem điểm danh đã tồn tại cho học viên và khóa học trong ngày hiện tại chưa, và chỉ ghi nhận điểm danh mới nếu chưa tồn tại.

#### 📝 NHIỆM VỤ CON 1.5: Viết kiểm thử cho chức năng đảm bảo tính idempotency cho điểm danh
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/src/main/java/org/nlh4j/membership_hub/attendance/AttendanceService.java;./sources/backend/attendance/src/test/java/org/nlh4j/membership_hub/attendance/AttendanceTest.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-013]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng đảm bảo tính idempotency cho điểm danh. Kiểm thử sẽ bao gồm việc kiểm tra xem điểm danh đã tồn tại cho học viên và khóa học trong ngày hiện tại chưa, và chỉ ghi nhận điểm danh mới nếu chưa tồn tại.

#### 📝 NHIỆM VỤ CON 1.6: Tài liệu chức năng đảm bảo tính idempotency cho điểm danh
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/attendance.md

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-013]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng đảm bảo tính idempotency cho điểm danh. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường đầu vào và các trường hợp kiểm tra.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Xây dựng chức năng xem thông tin thẻ thành viên và gia hạn thẻ thành viên<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 2.1: Xây dựng chức năng xem thông tin thẻ thành viên
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng xem thông tin thẻ thành viên. Chức năng này sẽ bao gồm việc truy vấn cơ sở dữ liệu để lấy thông tin thẻ thành viên và trả về kết quả dưới dạng đối tượng thẻ thành viên.

#### 📝 NHIỆM VỤ CON 2.2: Viết kiểm thử cho chức năng xem thông tin thẻ thành viên
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java;./sources/backend/studentcard/src/test/java/org/nlh4j/membership_hub/studentcard/StudentCardTest.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng xem thông tin thẻ thành viên. Kiểm thử sẽ bao gồm việc kiểm tra truy vấn cơ sở dữ liệu và trả về kết quả dưới dạng đối tượng thẻ thành viên.

#### 📝 NHIỆM VỤ CON 2.3: Tài liệu chức năng xem thông tin thẻ thành viên
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/studentcard.md

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng xem thông tin thẻ thành viên. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường đầu vào và các trường hợp kiểm tra.

#### 📝 NHIỆM VỤ CON 2.4: Xây dựng chức năng gia hạn thẻ thành viên
##### Chuyên gia con được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-015]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Xây dựng chức năng gia hạn thẻ thành viên. Chức năng này sẽ bao gồm việc xác thực đầu vào, cập nhật cơ sở dữ liệu và trả về kết quả thành công hoặc thất bại.

#### 📝 NHIỆM VỤ CON 2.5: Viết kiểm thử cho chức năng gia hạn thẻ thành viên
##### Chuyên gia con được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/studentcard/src/main/java/org/nlh4j/membership_hub/studentcard/StudentCardService.java;./sources/backend/studentcard/src/test/java/org/nlh4j/membership_hub/studentcard/StudentCardTest.java

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-015]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Viết kiểm thử cho chức năng gia hạn thẻ thành viên. Kiểm thử sẽ bao gồm việc kiểm tra xác thực đầu vào, cập nhật cơ sở dữ liệu và trả về kết quả thành công hoặc thất bại.

#### 📝 NHIỆM VỤ CON 2.6: Tài liệu chức năng gia hạn thẻ thành viên
##### Chuyên gia con được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/studentcard.md

* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-015]<!--END_TAGS-->

* **Hướng dẫn nhiệm vụ kỹ thuật chi tiết:** Tài liệu chức năng gia hạn thẻ thành viên. Tài liệu sẽ bao gồm mô tả chi tiết về chức năng, các trường đầu vào và các trường hợp kiểm tra.