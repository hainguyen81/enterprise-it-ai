# Giai đoạn 5: <!--PHASE_NAME_START-->Triển khai hạ tầng DevOps và đáp ứng yêu cầu phi chức năng<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản thảo** | ARCH-20260817042313 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai hạ tầng DevOps và đáp ứng yêu cầu phi chức năng<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai toàn bộ hạ tầng DevOps bao gồm Docker đa giai đoạn, pipeline CI/CD với GitHub Actions, cấu hình GCP (VPC, IAM, Storage), triển khai GKE với HPA, cấu hình backup, disaster recovery, mã hóa dữ liệu, logging và audit để đáp ứng các yêu cầu phi chức năng về hiệu suất, khả năng mở rộng, bảo mật và tuân thủ.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày/Giờ** | 2026/08/17 04:23:13 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn

Giai đoạn 5 tập trung vào việc triển khai toàn bộ hạ tầng DevOps và đáp ứng các yêu cầu phi chức năng (NFR) cho hệ thống membership-hub. Giai đoạn này bao gồm Công việc 27 với các mục tiêu kiến trúc cốt lõi sau:

1. **Container hóa và tối ưu hình ảnh**: Xây dựng Dockerfile đa giai đoạn cho tất cả 9 service backend, đảm bảo kích thước hình ảnh build <200MB và hình ảnh cuối cùng <500MB [NFR-005]. Cấu hình Docker Compose cho môi trường phát triển cục bộ.
2. **Hạ tầng GCP cơ bản**: Thiết lập VPC network với subnet công khai/riêng tư, firewall rules, IAM roles, và service accounts với nguyên tắc least privilege [NFR-002], [NFR-003], [NFR-008].
3. **Triển khai GKE**: Tạo GKE cluster với 3 node pools (general-purpose, high-memory, high-cpu), cấu hình network policies, private cluster, Workload Identity [NFR-002], [NFR-004].
4. **Tự động mở rộng**: Cấu hình HPA (Horizontal Pod Autoscaler) cho tất cả services dựa trên CPU >70% hoặc độ trễ yêu cầu >300ms [NFR-001], [NFR-004].
5. **Backup và Disaster Recovery**: Cấu hình Cloud Storage cho backup, Cloud Scheduler để backup PostgreSQL hàng ngày, Cloud SQL với high availability và automatic failover, point-in-time recovery 24 giờ, và script DR để restore sang region phụ [NFR-002], [NFR-009].
6. **CI/CD Pipeline**: Xây dựng GitHub Actions workflow tự động hóa build, test, push Docker images lên GCR, và deploy lên GKE với approval gate [NFR-001], [NFR-005], [NFR-006], [NFR-007].
7. **Bảo mật hạ tầng**: Cấu hình mã hóa at-rest (AES-256) và in-transit (TLS 1.3), Cloud KMS, GKE security policies (Pod Security Standards, seccomp, AppArmor), Cloud IAP [NFR-003], [NFR-008].
8. **Logging và Monitoring**: Cấu hình Cloud Logging với retention 1 năm, Cloud Monitoring với dashboards và alerting policies, audit logging cho hành động quản trị [NFR-006], [NFR-002].
9. **Tài liệu hóa**: Viết tài liệu hướng dẫn triển khai hạ tầng GCP, Docker, và hướng dẫn vận hành [ARC-010].

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục

### Thư mục hạ tầng
- `./sources/infra/docker/` [NFR-005]
- `./sources/infra/gcp/` [NFR-002], [NFR-003], [NFR-008], [NFR-009]
- `./sources/infra/gke/` [NFR-002], [NFR-004]
- `./sources/infra/github-actions/` [NFR-001], [NFR-005], [NFR-006], [NFR-007]
- `./sources/infra/monitoring/` [NFR-006]

### Tài liệu kiến trúc
- `./sources/docs/infrastructure/` [ARC-010]

### Điểm cuối API và Sự kiện
- Không có API mới hoặc sự kiện nghiệp vụ được triển khai trong giai đoạn này. Giai đoạn tập trung vào hạ tầng triển khai và cấu hình.

## 3. Chỉ thị chức năng chuyên biệt cho Đại lý phụ

*   **Docker**: Chuyên về containerization, multi-stage Dockerfile engineering, package optimization, và pushing verified application image assets. Chịu trách nhiệm xây dựng Dockerfile cho tất cả services, cấu hình Docker Compose, tối ưu kích thước hình ảnh và đẩy lên registry.
*   **GCP**: Chuyên về cloud automation trong Google Cloud Platform. Chịu trách nhiệm cấu hình VPC, IAM, service accounts, Cloud Storage, backup/restore, Cloud SQL, mã hóa dữ liệu, Cloud KMS, CI/CD pipeline với GitHub Actions, và đẩy hình ảnh lên Google Artifact Registry.
*   **GKE**: Chuyên về production container orchestration trong Google Kubernetes Engine. Chịu trách nhiệm tạo và cấu hình GKE cluster, node pools, network policies, Kubernetes deployment manifests, HPA, services, ingress, logging, monitoring, và audit trail.
*   **Doc**: Hoạt động như Nhà viết kỹ thuật chính. Chuyên biên soạn tài liệu hạ tầng, hướng dẫn triển khai GCP, hướng dẫn sử dụng Docker, và tài liệu vận hành hệ thống. Mọi tệp tài liệu phải có đuôi `.md` và nằm trong `./sources/docs/infrastructure/`.
*   **Reviewer**: Chịu trách nhiệm kiểm tra cuối cùng toàn bộ hạ tầng DevOps, xác minh tất cả yêu cầu phi chức năng được đáp ứng, kiểm tra bảo mật, và xác nhận giai đoạn sẵn sàng cho vận hành production.

## 4. Định nghĩa Hoàn thành của Giai đoạn (DoD)

1. Tất cả 9 service backend có Dockerfile đa giai đoạn build thành công với kích thước build image <200MB và final image <500MB [NFR-005].
2. Docker Compose có thể khởi chạy toàn bộ hệ thống cục bộ (9 backend services, PostgreSQL, Redis, mocks) với lệnh `docker-compose up`.
3. Hạ tầng GCP cơ bản (VPC, IAM, service accounts) được cấu hình đúng và sẵn sàng cho deployment.
4. GKE cluster được tạo với 3 node pools (general-purpose, high-memory, high-cpu), network policies, Workload Identity, và private cluster với authorized networks [NFR-002], [NFR-004].
5. HPA được cấu hình cho tất cả services với metrics CPU >70% và request latency >300ms, hoạt động tự động mở rộng và thu hẹp [NFR-001], [NFR-004].
6. Backup PostgreSQL hàng ngày được cấu hình (Cloud Scheduler 2:00 AM, retention 30 ngày), Cloud SQL có high availability (regional), automatic failover, point-in-time recovery 24 giờ [NFR-002], [NFR-009].
7. CI/CD pipeline GitHub Actions hoạt động đầy đủ: trigger trên push to main, chạy unit/integration tests, build multi-stage Docker images, push lên GCR, deploy lên GKE với approval gate [NFR-001], [NFR-005], [NFR-006], [NFR-007].
8. Mã hóa dữ liệu at-rest (AES-256) và in-transit (TLS 1.3) được bật trên Cloud Storage, Cloud SQL, Persistent Disks, và tất cả endpoint. Cloud KMS được cấu hình để quản lý encryption keys [NFR-003], [NFR-008].
9. Logging và monitoring được cấu hình: Cloud Logging với retention 1 năm cho audit logs, Cloud Monitoring với dashboards (CPU, memory, latency, error rate), alerting policies (CPU >70%, memory >80%, latency >300ms, error rate >1%) [NFR-006], [NFR-002].
10. Tất cả 9 thẻ NFR ([NFR-001] đến [NFR-009]) được ánh xạ, triển khai và xác nhận đáp ứng đầy đủ.
11. Tài liệu hạ tầng (GCP setup, Docker setup, GKE deployment, CI/CD pipeline, security, monitoring) được hoàn thiện đầy đủ và chính xác [ARC-010].
12. Không có lỗi bảo mật nghiêm trọng (SQL injection, XSS, CSRF, misconfiguration) được phát hiện trong quá trình review, tuân thủ đầy đủ OWASP Top 10 và yêu cầu mã hóa dữ liệu [NFR-003].

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC THEO TỪNG NGÀY

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->Thiết lập Docker đa giai đoạn và hạ tầng cơ sở GCP<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Xây dựng Dockerfile đa giai đoạn cho tất cả service backend
##### Đại lý phụ được giao: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/docker/user-service/Dockerfile`; `./sources/infra/docker/center-service/Dockerfile`; `./sources/infra/docker/course-service/Dockerfile`; `./sources/infra/docker/enrollment-service/Dockerfile`; `./sources/infra/docker/attendance-service/Dockerfile`; `./sources/infra/docker/card-service/Dockerfile`; `./sources/infra/docker/notification-service/Dockerfile`; `./sources/infra/docker/promotion-service/Dockerfile`; `./sources/infra/docker/report-service/Dockerfile`; `./sources/infra/docker/chatbot-service/Dockerfile`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Xây dựng Dockerfile đa giai đoạn cho 9 service backend sử dụng base image JDK 21 slim, tối ưu kích thước hình ảnh build <200MB, cấu hình biến môi trường cho kết nối cơ sở dữ liệu, cổng ứng dụng (8080/8443) và cấu hình xác thực. Sử dụng multi-stage build để tách biệt giai đoạn build (Maven/Gradle) và runtime, chỉ giữ lại các thư viện cần thiết trong hình ảnh cuối cùng. Đảm bảo hình ảnh cuối cùng <500MB. Cấu hình health check và liveness probe cho từng service.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 2: Cấu hình Docker Compose cho môi trường phát triển cục bộ
##### Đại lý phụ được giao: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/docker-compose.yml`; `./sources/infra/docker/.env.example`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo file docker-compose.yml để khởi chạy toàn bộ hệ thống cục bộ bao gồm: 9 backend services, PostgreSQL 16, Redis 7, Zalo API mock, Firebase Auth mock. Cấu hình internal Docker network, volume mounts cho dữ liệu persistent và logs, biến môi trường cho kết nối giữa các services thông qua service names. Cấu hình health checks cho từng container. Tạo file `.env.example` với tất cả biến môi trường cần thiết (DB credentials, JWT secrets, API keys). Đảm bảo có thể khởi chạy toàn bộ hệ thống với lệnh `docker-compose up` và dừng với `docker-compose down`.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 3: Cấu hình hạ tầng cơ sở GCP (VPC, IAM, Service Accounts)
##### Đại lý phụ được giao: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gcp/vpc.tf`; `./sources/infra/gcp/iam.tf`; `./sources/infra/gcp/service-accounts.tf`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-002], [NFR-003], [NFR-008]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình VPC network với 2 subnet: public subnet (10.0.1.0/24) cho bastion và load balancer, private subnet (10.0.2.0/24) cho GKE nodes và dịch vụ nội bộ. Cấu hình firewall rules: cho phép inbound TCP 8080/8443 đến GKE nodes, TCP 5432 đến Cloud SQL, TCP 6379 đến Redis, TCP 22 đến bastion từ authorized networks. Tạo service accounts riêng cho từng service backend với quyền hạn tối thiểu theo nguyên tắc least privilege (ví dụ: chỉ quyền đọc Cloud Storage cho report-service, chỉ quyền gửi FCM cho notification-service). Cấu hình IAM roles cho System Admin (quyền quản lý toàn bộ dự án) và Center Admin (quyền giới hạn theo trung tâm).
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 4: Viết tài liệu hướng dẫn triển khai hạ tầng cơ sở
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/infrastructure/gcp-setup.md`; `./sources/docs/infrastructure/docker-setup.md`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[ARC-010], [NFR-002], [NFR-003]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết tài liệu hướng dẫn chi tiết cấu hình hạ tầng GCP bao gồm: tạo project, kích hoạt API cần thiết (Compute Engine, GKE, Cloud SQL, Cloud Storage, Cloud Logging), cấu hình VPC network, tạo service accounts và IAM roles, cấu hình firewall rules. Viết hướng dẫn sử dụng Docker và Docker Compose cho môi trường phát triển cục bộ: cách khởi chạy, dừng, xem log, debug các services, quản lý biến môi trường. Bao gồm các bước xác minh cấu hình và kiểm tra kết nối giữa các services.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->Triển khai GKE cluster và CI/CD pipeline<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Tạo và cấu hình GKE cluster với networking
##### Đại lý phụ được giao: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gke/cluster.tf`; `./sources/infra/gke/node-pools.tf`; `./sources/infra/gke/network-policy.yaml`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo GKE cluster (Kubernetes 1.28+) với 3 node pools: general-purpose (2 nodes, e2-standard-4) cho services thông thường, high-memory (2 nodes, e2-highmem-4) cho reporting, high-cpu (2 nodes, e2-highcpu-4) cho chatbot. Cấu hình private cluster với authorized networks cho API server access. Cấu hình Workload Identity để service accounts GCP có thể truy cập các dịch vụ khác mà không cần quản lý credentials. Cấu hình network policy để kiểm soát traffic giữa các service (mặc định deny all, allow only required ports). Cấu hình Cloud NAT cho outbound traffic từ private nodes.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 2: Cấu hình HPA và Kubernetes deployment manifests
##### Đại lý phụ được giao: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gke/deployments/`; `./sources/infra/gke/hpa.yaml`; `./sources/infra/gke/services.yaml`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-001], [NFR-004]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo Kubernetes deployment manifests cho tất cả 9 backend services trong thư mục `./sources/infra/gke/deployments/`. Mỗi deployment phải có: resource requests/limits (CPU, memory), liveness probe (HTTP /health/ready), readiness probe (HTTP /health/ready), image pull policy (IfNotPresent), replica count tối thiểu 2. Tạo file `hpa.yaml` cấu hình Horizontal Pod Autoscaler cho mỗi service: minReplicas=2, maxReplicas=10, metrics CPU >70% hoặc request latency >300ms (sử dụng custom metric từ Cloud Monitoring). Tạo file `services.yaml` với ClusterIP services cho internal communication và Ingress cho external access qua HTTPS. Cấu hình resource quotas và limit ranges cho namespace mặc định.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 3: Cấu hình Cloud Storage, backup và disaster recovery
##### Đại lý phụ được giao: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gcp/storage.tf`; `./sources/infra/gcp/backup-scheduler.tf`; `./sources/infra/gcp/disaster-recovery.tf`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-002], [NFR-009]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình Cloud Storage buckets: một bucket cho backup PostgreSQL (tên: `membership-hub-backups`), một bucket cho application logs (tên: `membership-hub-logs`), một bucket cho build artifacts (tên: `membership-hub-artifacts`). Cấu hình retention policy cho backup bucket (30 ngày). Tạo Cloud Scheduler job để thực hiện backup PostgreSQL hàng ngày lúc 2:00 AM sử dụng Cloud SQL Admin API, lưu backup dưới dạng SQL dump vào bucket backup. Cấu hình Cloud SQL instance với high availability (regional), automatic failover, point-in-time recovery up to 24 hours. Tạo script disaster recovery (bash/python) để restore từ backup sang region phụ (ví dụ: từ asia-southeast1 sang asia-east1) trong trường hợp sự cố khu vực. Script phải bao gồm: restore Cloud SQL, update DNS records, cập nhật GKE cluster endpoints.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 4: Cấu hình CI/CD pipeline với GitHub Actions
##### Đại lý phụ được giao: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/github-actions/`; `./sources/infra/gcp/cloudbuild.yaml`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-001], [NFR-005], [NFR-006], [NFR-007]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình GitHub Actions workflow trong thư mục `./sources/infra/github-actions/`: workflow `ci-cd.yml` trigger trên push đến nhánh `main` và pull requests. Pipeline bao gồm các bước: checkout code, setup Java 21, cache Maven dependencies, run unit tests và integration tests với coverage check (>=85%), build multi-stage Docker images cho tất cả 9 services, push images lên Google Artifact Registry (GCR) với tags `sha-<commit>` và `latest`, deploy lên GKE cluster sử dụng `gcloud container clusters get-credentials`. Cấu hình secrets cho GCP credentials, GCR credentials, và các API keys. Thêm approval gate (environment protection rules) trước khi deploy lên production. Cấu hình bước đặc biệt để xử lý bản địa hóa đa ngôn ngữ: build và deploy các bản dịch, kiểm tra tất cả chuỗi văn bản được externalized đúng cách [NFR-007]. Cấu hình caching cho Docker layers và Maven dependencies để tăng tốc độ build.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

### 🌤️ Ngày 3: <!--DAY_HEADER_START-->Bảo mật, logging, audit và tối ưu cuối cùng<!--DAY_HEADER_END-->

#### 📝 Phụ công việc 1: Cấu hình mã hóa dữ liệu và bảo mật hạ tầng
##### Đại lý phụ được giao: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gcp/encryption.tf`; `./sources/infra/gke/security-policies.yaml`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-003], [NFR-008]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình mã hóa dữ liệu at-rest sử dụng AES-256 cho Cloud Storage buckets, Cloud SQL instance, và GKE Persistent Disks. Cấu hình mã hóa dữ liệu in-transit sử dụng TLS 1.3 cho tất cả các endpoint công khai và giao tiếp nội bộ giữa các services (sử dụng Istio sidecar hoặc NGINX ingress với TLS termination). Cấu hình Cloud KMS (Key Management Service) để quản lý encryption keys với rotation tự động 90 ngày. Cấu hình GKE security policies: Pod Security Standards ở chế độ `restricted`, seccomp profiles (RuntimeDefault), AppArmor profiles, network policies để hạn chế lateral movement. Cấu hình Cloud IAP (Identity-Aware Proxy) để bảo vệ access đến GKE dashboard và bastion host. Đảm bảo tất cả secrets (JWT signing key, DB passwords, API keys) được lưu trữ trong Secret Manager và mount vào pods dưới dạng environment variables hoặc volume mounts.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 2: Cấu hình logging, monitoring và audit trail
##### Đại lý phụ được giao: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gke/logging-config.yaml`; `./sources/infra/gcp/audit-logging.tf`; `./sources/infra/monitoring/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-006], [NFR-002]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Cấu hình Cloud Logging cho GKE cluster để thu thập logs từ tất cả các pods (stdout/stderr), nodes, và system components (kube-apiserver, etcd, scheduler). Cấu hình log retention 1 năm cho audit logs (đáp ứng yêu cầu kiểm tra). Tạo các dashboard trong Cloud Monitoring cho: CPU utilization, memory utilization, request latency (p95, p99), error rate (5xx), queue depth. Cấu hình alerting policies với các ngưỡng: CPU >70% (trung bình 5 phút), memory >80%, request latency >300ms, error rate >1%. Cấu hình audit logging cho tất cả các hành động quản trị GCP (qua Cloud Audit Logs) và GKE (via Kubernetes audit logs), lưu trữ trong Cloud Logging với retention 1 năm. Cấu hình notification channels (email, SMS) cho alerting policies gửi đến quản trị viên hệ thống.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 3: Tối ưu kích thước hình ảnh Docker và đẩy lên registry
##### Đại lý phụ được giao: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/docker/`; `./sources/infra/gcp/artifact-registry.tf`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-005]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tối ưu kích thước hình ảnh Docker cho tất cả 9 services: sử dụng base image nhỏ nhất có thể (JDK 21-slim hoặc distroless), loại bỏ các file không cần thiết (source code, documentation, tests) trong giai đoạn runtime, sử dụng layer caching hiệu quả bằng cách sắp xếp thứ tự COPY từ ít thay đổi đến nhiều thay đổi. Đẩy tất cả hình ảnh đã tối ưu lên Google Artifact Registry (GCR) trong repository `membership-hub`. Cấu hình vulnerability scanning (Container Analysis) cho tất cả hình ảnh để phát hiện CVE. Đảm bảo kích thước hình ảnh cuối cùng của mỗi service dưới 500MB [NFR-005]. Cấu hình image pull secrets cho GKE để có thể pull images từ GCR.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]

#### 📝 Phụ công việc 4: Kiểm tra cuối cùng và xác nhận hoàn thành giai đoạn
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** Toàn bộ mã nguồn và cấu hình hạ tầng trong `./sources/infra/`
* **Thẻ theo dõi khả năng truy xuất:** <!--START_TAGS-->[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->
* **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thực hiện kiểm tra cuối cùng toàn bộ hạ tầng DevOps: (1) Xác minh tất cả Docker images build thành công, kích thước trong giới hạn, và có thể push lên GCR; (2) Xác minh GKE cluster khởi chạy đúng, tất cả 9 services deploy thành công và health check pass; (3) Xác minh HPA hoạt động đúng bằng cách tải giả lập; (4) Xác minh CI/CD pipeline chạy thành công end-to-end từ push đến deploy; (5) Xác minh backup và disaster recovery được cấu hình đúng (test restore từ backup); (6) Xác minh mã hóa dữ liệu at-rest và in-transit được bật; (7) Xác minh logging, monitoring, và audit trail hoạt động, logs được giữ retention 1 năm; (8) Xác minh tất cả yêu cầu phi chức năng [NFR-001] đến [NFR-009] được đáp ứng; (9) Xác minh không có lỗi bảo mật nghiêm trọng (misconfiguration, public exposure, weak encryption). Xác nhận giai đoạn sẵn sàng cho vận hành production.
* **Đặc tả SQL DDL Schema Cơ sở dữ liệu [DAT-XXX]:** [NOT APPLICABLE]
* **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** [NOT APPLICABLE]
* **Trình xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** [NOT APPLICABLE]