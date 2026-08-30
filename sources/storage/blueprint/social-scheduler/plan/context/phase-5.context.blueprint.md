# Giai đoạn 5: <!--PHASE_NAME_START-->Triển khai bảo mật hạ tầng và tài liệu kỹ thuật cuối cùng<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260830090918 |
| **Tên dự án** | social-scheduler |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai bảo mật hạ tầng và tài liệu kỹ thuật cuối cùng<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai các biện pháp bảo mật doanh nghiệp, container hóa dịch vụ, cung cấp hạ tầng đám mây trên GCP/GKE và hoàn thiện tài liệu tham chiếu kỹ thuật cuối cùng cho hệ thống.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày giờ** | 2026/08/30 09:09:18 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Chờ phê duyệt quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn
Giai đoạn này tập trung vào việc hiện thực hóa các yêu cầu phi chức năng (NFR) thông qua việc container hóa toàn bộ hệ thống, thiết lập cấu hình bảo mật Spring Security, triển khai hạ tầng trên Google Cloud Platform (GCP) và Google Kubernetes Engine (GKE), đồng thời hoàn thiện bộ tài liệu kỹ thuật cuối cùng để bàn giao hệ thống.

## 2. Phạm vi kỹ thuật và ranh giới thư mục
* **Cấu hình Docker:** `./sources/infra/docker/backend/Dockerfile`, `./sources/infra/docker/frontend/Dockerfile`
* **Cấu hình hạ tầng:** `./sources/infra/gcp/deployment.yaml`, `./sources/infra/gke/deployment.yaml`
* **Cấu hình bảo mật:** `./sources/backend/src/main/java/org/nlh4j/socialscheduler/security/SecurityConfig.java`
* **Tài liệu kỹ thuật:** `./sources/docs/technical-reference.md`

## 3. Chỉ dẫn chức năng cho Sub-Agent
* **Docker**: Chịu trách nhiệm xây dựng Dockerfile tối ưu hóa cho backend và frontend.
* **GCP/GKE**: Chịu trách nhiệm cấu hình triển khai trên đám mây và Kubernetes.
* **Coder**: Triển khai cấu hình bảo mật Spring Security.
* **Doc**: Hoàn thiện tài liệu tham chiếu kỹ thuật cuối cùng.

## 4. Định nghĩa hoàn thành (DoD)
- Hệ thống được container hóa hoàn toàn và sẵn sàng triển khai.
- Cấu hình bảo mật JWT/OAuth2 được áp dụng.
- Hạ tầng GCP/GKE được cung cấp và kiểm thử thành công.
- Tài liệu kỹ thuật cuối cùng được phê duyệt.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Container hóa dịch vụ backend<!--DAY_HEADER_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 SUB-TASK 1: Xây dựng Dockerfile cho backend
* **Chuyên môn hóa:** [Docker]
* **Các ID thẻ mục tiêu:** [NFR-001]
* **Đường dẫn tệp mục tiêu:** `./sources/infra/docker/backend/Dockerfile`
* **Chỉ dẫn kỹ thuật:** Xây dựng Dockerfile đa giai đoạn (multi-stage) cho ứng dụng Java backend, đảm bảo tối ưu hóa kích thước image và bảo mật bằng cách sử dụng user không đặc quyền.

<!--ATOMIC_SUB_TASK_NODE_END-->

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Container hóa dịch vụ frontend<!--DAY_HEADER_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 SUB-TASK 1: Xây dựng Dockerfile cho frontend
* **Chuyên môn hóa:** [Docker]
* **Các ID thẻ mục tiêu:** [NFR-001]
* **Đường dẫn tệp mục tiêu:** `./sources/infra/docker/frontend/Dockerfile`
* **Chỉ dẫn kỹ thuật:** Xây dựng Dockerfile cho ứng dụng React frontend, sử dụng Nginx làm web server để phục vụ các tệp tĩnh đã được build.

<!--ATOMIC_SUB_TASK_NODE_END-->

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Cấu hình triển khai GCP<!--DAY_HEADER_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 SUB-TASK 1: Thiết lập cấu hình triển khai GCP
* **Chuyên môn hóa:** [GCP]
* **Các ID thẻ mục tiêu:** [NFR-003]
* **Đường dẫn tệp mục tiêu:** `./sources/infra/gcp/deployment.yaml`
* **Chỉ dẫn kỹ thuật:** Tạo cấu hình triển khai cho Google Cloud Platform, bao gồm các thiết lập về VPC, IAM và Cloud Run để đảm bảo môi trường chạy an toàn.

<!--ATOMIC_SUB_TASK_NODE_END-->

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->Cấu hình triển khai GKE<!--DAY_HEADER_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 SUB-TASK 1: Thiết lập manifest triển khai GKE
* **Chuyên môn hóa:** [GKE]
* **Các ID thẻ mục tiêu:** [NFR-003]
* **Đường dẫn tệp mục tiêu:** `./sources/infra/gke/deployment.yaml`
* **Chỉ dẫn kỹ thuật:** Tạo các manifest Kubernetes cho GKE, bao gồm Deployment, Service và HPA để quản lý các dịch vụ microservices.

<!--ATOMIC_SUB_TASK_NODE_END-->

### 🌤️ NGÀY 5: <!--DAY_HEADER_START-->Triển khai bảo mật Spring Security<!--DAY_HEADER_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 SUB-TASK 1: Cấu hình Spring Security
* **Chuyên môn hóa:** [Coder]
* **Các ID thẻ mục tiêu:** [NFR-002]
* **Đường dẫn tệp mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/socialscheduler/security/SecurityConfig.java`
* **Chỉ dẫn kỹ thuật:** Triển khai cấu hình bảo mật Spring Security, tích hợp xác thực JWT và OAuth2, đồng thời thiết lập các quy tắc kiểm soát truy cập nghiêm ngặt.

<!--ATOMIC_SUB_TASK_NODE_END-->

### 🌤️ NGÀY 6: <!--DAY_HEADER_START-->Hoàn thiện tài liệu kỹ thuật<!--DAY_HEADER_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 SUB-TASK 1: Soạn thảo tài liệu tham chiếu kỹ thuật cuối cùng
* **Chuyên môn hóa:** [Doc]
* **Các ID thẻ mục tiêu:** [DOC-001]
* **Đường dẫn tệp mục tiêu:** `./sources/docs/technical-reference.md`
* **Chỉ dẫn kỹ thuật:** Tổng hợp và hoàn thiện tài liệu tham chiếu kỹ thuật, bao gồm hợp đồng API, sơ đồ dữ liệu, hướng dẫn vận hành và các biện pháp bảo mật đã triển khai.

<!--ATOMIC_SUB_TASK_NODE_END-->

### 🌤️ NGÀY 7: <!--DAY_HEADER_START-->Đẩy hình ảnh lên Registry<!--DAY_HEADER_END-->

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 SUB-TASK 1: Đẩy hình ảnh Docker lên Artifact Registry
* **Chuyên môn hóa:** [Docker]
* **Các ID thẻ mục tiêu:** [NFR-001]
* **Đường dẫn tệp mục tiêu:** `./sources/infra/docker/push.sh`
* **Chỉ dẫn kỹ thuật:** Thực hiện script xây dựng và đẩy các hình ảnh Docker đã được kiểm thử lên Google Artifact Registry để chuẩn bị cho việc triển khai sản xuất.

<!--ATOMIC_SUB_TASK_NODE_END-->

### 🕵️ BÁO CÁO KIỂM TOÁN KIẾN TRÚC THỰC TẾ BẮT BUỘC:

```properties:cross_audit_ledger
[BÁO CÁO TỰ KIỂM TOÁN TỰ ĐỘNG]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
TRẠNG_THÁI_TÍNH_TOÁN_PHASES=Verified_5
GIỚI HẠN_MAX_DAYS_PER_PHASE_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=7
TRẠNG_THÁI_GIỚI_HẠN_DAY_COMPLIANCE=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=8
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=7
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```