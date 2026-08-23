# GIAI ĐOẠN 5: <!--PHASE_NAME_START-->Triển khai Hạ tầng DevOps, Tích hợp Hệ thống và Tài liệu Doanh nghiệp<!--PHASE_NAME_END-->

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã bản thiết kế** | ARCH-20260822094056 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai Hạ tầng DevOps, Tích hợp Hệ thống và Tài liệu Doanh nghiệp<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Hoàn thiện toàn bộ hạ tầng DevOps và đám mây, triển khai cụm GKE với auto-scaling, cấu hình hạ tầng GCP qua Terraform, xây dựng pipeline CI/CD GitHub Actions, tích hợp API Gateway và Kafka, đảm bảo tuân thủ các yêu cầu phi chức năng về bảo mật, hiệu năng và khả năng sẵn sàng, đồng thời bàn giao toàn bộ tài liệu hệ thống doanh nghiệp.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/22 09:40:56 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (Đặc vụ SA) |
| **Phê duyệt** | Đang chờ xem xét quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 5 tập trung vào việc hoàn thiện hạ tầng DevOps và đám mây cho hệ thống membership-hub. Các mục tiêu kỹ thuật cốt lõi bao gồm: (1) Cấu hình hạ tầng GCP bao gồm VPC, IAM, Cloud SQL, Redis Memorystore, và Cloud Storage thông qua Terraform; (2) Xây dựng Dockerfile đa giai đoạn cho tất cả service vi mô với kích thước hình ảnh tối ưu; (3) Triển khai cụm GKE với 3 node pools, cấu hình HPA auto-scaling dựa trên CPU và độ trễ; (4) Cấu hình PostgreSQL read replicas cho khối lượng công việc báo cáo; (5) Xây dựng pipeline CI/CD GitHub Actions với quét lỗ hổng bảo mật và kiểm tra chất lượng mã; (6) Cấu hình API Gateway, Kafka topics, và Istio service mesh cho kiến trúc sự kiện; (7) Triển khai các chính sách bảo mật, IAM, audit logging và tuân thủ GDPR/CCPA; (8) Hoàn thiện toàn bộ tài liệu hệ thống doanh nghiệp bao gồm bản vẽ kiến trúc, hợp đồng API, hướng dẫn vận hành và tài liệu cơ sở dữ liệu. Giai đoạn này đảm bảo hệ thống sẵn sàng cho môi trường production với mục tiêu uptime 99.9%, độ trễ API dưới 200ms, và tuân thủ nghiêm ngặt OWASP Top 10.

## 2. Phạm vi kỹ thuật được phép và ranh giới thư mục
Tất cả đường dẫn tệp đều bắt đầu với gốc kho lưu trữ `./sources/`, tuân thủ cấu trúc kiến trúc vi mô đã định nghĩa:
* **Hạ tầng Terraform và đám mây GCP:**
  * ./sources/infra/terraform/main.tf [ARC-010], [NFR-002], [NFR-003], [NFR-004], [NFR-009]
  * ./sources/infra/terraform/gke-cluster.tf [ARC-010], [NFR-002], [NFR-004]
  * ./sources/infra/terraform/postgres-replica.tf [ARC-010], [NFR-004], [NFR-009]
  * ./sources/infra/terraform/iam.tf [ARC-010], [NFR-003], [NFR-008]
  * ./sources/infra/terraform/monitoring.tf [ARC-010], [NFR-006], [NFR-002]
  * ./sources/infra/terraform/security-policies.tf [ARC-010], [NFR-003], [NFR-008]
* **Container hóa Docker:**
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
* **Kubernetes manifests:**
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
* **CI/CD và kiểm thử:**
  * ./sources/infra/.github/workflows/ci-cd.yml [ARC-010], [NFR-001], [NFR-006]
  * ./sources/infra/test/infra_test.go [ARC-010], [NFR-002], [NFR-004]
  * ./sources/infra/test/e2e_deployment_test.go [ARC-010], [NFR-002], [NFR-004]
  * ./sources/infra/test/security_compliance_test.go [ARC-010], [NFR-003], [NFR-008]
  * ./sources/infra/test/full_e2e_test.go [ARC-010], [NFR-001], [NFR-002], [NFR-006]
* **Tài liệu doanh nghiệp:**
  * ./sources/docs/architecture-overview.md [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
  * ./sources/docs/api-integration-contracts.md [ARC-006], [ARC-007], [ARC-008], [ARC-009]
  * ./sources/docs/operational-runbooks.md [ARC-010], [NFR-002], [NFR-009]
  * ./sources/docs/database-architecture.md [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]
  * ./sources/docs/user-guide.md [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]

## 3. Chỉ thị chức năng cho tác nhân phụ chuyên dụng
* **Coder**: Đóng vai trò là Nhà phát triển ứng dụng cấp cao/Chính. Chịu trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên cả backend services và frontend/ứng dụng di động. Bị cấm viết bộ kiểm thử hoặc manifest hạ tầng.
* **Tester**: Đóng vai trò là Kiểm soát chất lượng (QC/QA) cấp cao. Chuyên về kỹ thuật bộ kiểm thử, xác thực và cổng chất lượng. Chịu trách nhiệm tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác thực hiệu năng. Bị cấm sửa mã nguồn sản xuất. Nếu mục tiêu nhiệm vụ liên quan đến phạm vi kiểm thử tích hợp hoặc end-to-end mà không có tệp mã ứng dụng cụ thể nào có thể bị giới hạn, bạn PHẢI xuất ra literal token `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp dấu chấm phẩy.
* **Doc**: Hoạt động như là Nhà viết kỹ thuật chính và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Đặc tả kỹ thuật toàn diện, tài liệu tham chiếu schema, bản vẽ kiến trúc hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp ngăn xếp kiến trúc đang hoạt động của dự án. Mỗi tệp tài liệu kỹ thuật được tạo PHẢI được liệt kê là thực thể đường dẫn tệp cụ thể có phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Chịu trách nhiệm xác minh trình biên dịch, cổng phân tích tĩnh và vá bảo vệ phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, sửa lỗi hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
* **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
* **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Chịu trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container một cách tự nhiên trên Google Cloud Run.
* **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Chịu trách nhiệm xây dựng Kubernetes deployment manifests, điều khiển định tuyến, cấu hình HPA, Helm charts và triển khai workloads vi mô vào cụm GKE đang hoạt động.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
Giai đoạn 5 được coi là hoàn thành khi đáp ứng đầy đủ các mốc định lượng sau:
1. Toàn bộ hạ tầng GCP được cấu hình qua Terraform bao gồm VPC, IAM, Cloud SQL, Redis, và Cloud Storage với mã hóa AES-256 và TLS 1.3.
2. Cụm GKE được triển khai với 3 node pools, HPA auto-scaling hoạt động dựa trên CPU > 70% và độ trễ > 300ms, đảm bảo uptime 99.9%.
3. Tất cả Dockerfile đa giai đoạn được xây dựng với kích thước hình ảnh cuối cùng < 500MB, đã được đẩy lên Google Container Registry.
4. Pipeline CI/CD GitHub Actions hoạt động đầy đủ với build, test, quét lỗ hổng bảo mật (Snyk), và triển khai tự động lên GKE.
5. API Gateway, Kafka topics, và Istio service mesh được cấu hình và tích hợp thành công giữa các service vi mô.
6. Tất cả yêu cầu phi chức năng được tuân thủ: bảo mật (OWASP Top 10, TLS 1.3, AES-256), hiệu năng (API < 200ms), khả năng sẵn sàng (HPA, failover), logging (1 năm), và tuân thủ GDPR/CCPA.
7. Tất cả bộ kiểm thử hạ tầng, bảo mật và tích hợp toàn hệ thống đều vượt qua, đảm bảo hệ thống sẵn sàng production.
8. Toàn bộ tài liệu doanh nghiệp được hoàn thiện: bản vẽ kiến trúc, hợp đồng API, hướng dẫn vận hành, tài liệu cơ sở dữ liệu, và hướng dẫn người dùng.
9. 100% các thẻ theo dõi yêu cầu được phân phối cho giai đoạn 5 ([ARC-006] đến [ARC-010], [NFR-001] đến [NFR-009]) được ánh xạ đầy đủ vào các nhiệm vụ kỹ thuật và tài liệu, không có thẻ nào bị thiếu.

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC TỪNG NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Triển khai hạ tầng đám mây cơ bản và container hóa<!--DAY_HEADER_END-->

#### 📝 Công việc con 1.1: Cấu hình hạ tầng GCP cơ bản
##### Đại lý phụ trách: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/terraform/main.tf
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-010], [NFR-002], [NFR-003], [NFR-004], [NFR-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình hạ tầng GCP bao gồm tạo dự án, mạng VPC, subnet, firewall rules, Cloud SQL (PostgreSQL) với high availability, Redis Memorystore, và Cloud Storage. Đảm bảo mã hóa dữ liệu nghỉ (AES-256) và TLS 1.3 cho kết nối. Áp dụng các chính sách IAM để tuân thủ NFR-003 và NFR-008. Cấu hình sao lưu tự động hàng ngày và point-in-time recovery cho PostgreSQL (NFR-009).

#### 📝 Công việc con 1.2: Xây dựng Dockerfile đa giai đoạn cho tất cả service vi mô
##### Đại lý phụ trách: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/docker/Dockerfile.auth-service
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-005], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng Dockerfile đa giai đoạn (multi-stage) cho từng service vi mô (auth, center, course, enrollment, attendance, membership, notification, promotion, report, ai-chatbot). Sử dụng base image nhỏ (distroless hoặc alpine) để đảm bảo kích thước hình ảnh cuối cùng < 500MB (NFR-005). Tối ưu hóa layer caching và loại bỏ các công cụ không cần thiết trong giai đoạn production.

#### 📝 Công việc con 1.3: Tạo cụm GKE với auto-scaling
##### Đại lý phụ trách: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/terraform/gke-cluster.tf
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-002], [NFR-004], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo cụm GKE với 3 node pools (system, application, cache). Cấu hình Horizontal Pod Autoscaler (HPA) dựa trên CPU > 70% và độ trễ yêu cầu > 300ms (NFR-004). Bật auto-scaling cho node pools. Cấu hình network policies và PodSecurityPolicy để đảm bảo an ninh.

#### 📝 Công việc con 1.4: Cấu hình PostgreSQL read replicas
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/terraform/postgres-replica.tf
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-004], [NFR-009], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình 2 read replicas cho PostgreSQL để phân tán khối lượng công việc báo cáo. Thiết lập connection pooling với PgBouncer. Cấu hình automated failover cho primary instance. Đảm bảo backup hàng ngày và point-in-time recovery trong 24 giờ (NFR-009).

#### 📝 Công việc con 1.5: Viết kiểm thử xác thực hạ tầng
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/infra/test/infra_test.go
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết các bài kiểm thử xác thực hạ tầng sử dụng Terratest để kiểm tra việc provision VPC, Cloud SQL, Redis, và GKE cluster. Xác minh các cấu hình auto-scaling và network policies hoạt động như mong đợi.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Triển khai Kubernetes và CI/CD pipeline<!--DAY_HEADER_END-->

#### 📝 Công việc con 2.1: Tạo Kubernetes deployment manifests và services
##### Đại lý phụ trách: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/k8s/deployment-auth-service.yaml
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-002], [NFR-004], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo Kubernetes Deployment, Service, và HorizontalPodAutoscaler cho tất cả các service vi mô. Cấu hình resource requests/limits, liveness/readiness probes, và rolling update strategy. Đảm bảo high availability với ít nhất 2 replicas cho mỗi service.

#### 📝 Công việc con 2.2: Đẩy hình ảnh Docker lên Google Container Registry
##### Đại lý phụ trách: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/docker/push-images.sh
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-005], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo script để đẩy tất cả hình ảnh Docker đã được build lên Google Container Registry (GCR) với tags phiên bản phù hợp. Cấu hình image pull policy là Always cho môi trường staging và IfNotPresent cho production.

#### 📝 Công việc con 2.3: Cấu hình pipeline CI/CD GitHub Actions
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/.github/workflows/ci-cd.yml
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-001], [NFR-006], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Xây dựng pipeline CI/CD với GitHub Actions bao gồm: build và test cho mỗi service, quét lỗ hổng bảo mật (Snyk), build Docker images, đẩy lên GCR, triển khai lên GKE. Tích hợp kiểm tra chất lượng mã (SonarQube) và logging cho pipeline (NFR-006).

#### 📝 Công việc con 2.4: Cấu hình Cloud Logging và Monitoring
##### Đại lý phụ trách: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/terraform/monitoring.tf
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-006], [NFR-002], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình Cloud Logging để thu thập logs từ tất cả các service và GKE cluster. Thiết lập Cloud Monitoring với các dashboard hiển thị metrics hiệu năng (NFR-001), availability (NFR-002), và health của các service. Cấu hình alerts cho các ngưỡng cảnh báo.

#### 📝 Công việc con 2.5: Viết kiểm thử xác thực triển khai end-to-end
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/infra/test/e2e_deployment_test.go
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết bài kiểm thử end-to-end để xác minh tất cả các service được triển khai thành công trên GKE, có thể giao tiếp với nhau, và phản hồi yêu cầu trong ngưỡng hiệu năng cho phép (NFR-001). Kiểm tra khả năng tự động phục hồi khi node bị lỗi.

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Triển khai hợp đồng tích hợp hệ thống và kiến trúc sự kiện<!--DAY_HEADER_END-->

#### 📝 Công việc con 3.1: Cấu hình API Gateway
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/k8s/api-gateway.yaml
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [ARC-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình API Gateway (Kong hoặc NGINX Ingress) để định tuyến yêu cầu đến các service vi mô tương ứng. Thiết lập rate limiting, JWT validation, và SSL termination. Đảm bảo tất cả các endpoint REST được bảo vệ và tuân thủ kiến trúc tích hợp backend-frontend (ARC-009).

<!--START_API_CONTRACT-->
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
<!--END_API_CONTRACT-->

#### 📝 Công việc con 3.2: Cấu hình Kafka topics cho kiến trúc sự kiện
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/k8s/kafka-topics.yaml
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tạo các Kafka topics cho các luồng sự kiện: attendance.scan (điểm danh QR), notification.push (thông báo đẩy), notification.zalo (tin nhắn Zalo), và course.enrollment (đăng ký khóa học). Cấu hình replication factor và partition count phù hợp cho khả năng mở rộng.

#### 📝 Công việc con 3.3: Cấu hình Service Mesh Istio
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/k8s/istio-config.yaml
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình Istio service mesh để quản lý giao tiếp giữa các service vi mô. Thiết lập mutual TLS, traffic shifting, và circuit breaking. Đảm bảo các luồng xác thực (ARC-006), điểm danh (ARC-007), và thông báo (ARC-008) hoạt động ổn định qua service mesh.

#### 📝 Công việc con 3.4: Viết kiểm thử hợp đồng API
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/backend/auth/src/test/java/com/hub/contract/AuthApiContractTest.java
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết các bài kiểm thử hợp đồng (contract tests) để xác minh các endpoint REST API tuân thủ đúng schema đã định nghĩa. Bao gồm kiểm tra authentication flow (ARC-006), attendance scan endpoint (ARC-007), notification endpoints (ARC-008), và backend-frontend integration endpoints (ARC-009).

#### 📝 Công việc con 3.5: Tài liệu hợp đồng tích hợp hệ thống
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/api-integration-contracts.md
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết tài liệu chi tiết về các hợp đồng tích hợp hệ thống, bao gồm: luồng xác thực OAuth2/JWT (ARC-006), luồng điểm danh QR (ARC-007), luồng thông báo đa kênh (ARC-008), và tích hợp backend-frontend (ARC-009). Bao gồm các schema request/response, mã lỗi, và ví dụ sử dụng.

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->Bảo mật, tuân thủ và tối ưu hiệu năng<!--DAY_HEADER_END-->

#### 📝 Công việc con 4.1: Cấu hình IAM và chính sách bảo mật GCP
##### Đại lý phụ trách: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/terraform/iam.tf
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-003], [NFR-008], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Cấu hình IAM roles và service accounts với nguyên tắc đặc quyền tối thiểu (least privilege). Thiết lập organization policies để đảm bảo tuân thủ GDPR/CCPA (NFR-008). Cấu hình Cloud KMS để quản lý khóa mã hóa.

#### 📝 Công việc con 4.2: Cấu hình chính sách mạng và bảo mật pod GKE
##### Đại lý phụ trách: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/k8s/security-policies.yaml
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-003], [NFR-008], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai Network Policies để kiểm soát lưu lượng giữa các service. Cấu hình PodSecurityPolicies (PSP) hoặc Pod Security Standards để hạn chế đặc quyền container. Bật audit logging cho cluster.

#### 📝 Công việc con 4.3: Triển khai middleware ghi log audit
##### Đại lý phụ trách: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/backend/common/src/main/java/org/nlh4j/membership_hub/middleware/AuditLoggingMiddleware.java
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-006], [ARC-006]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Triển khai middleware ghi log audit cho tất cả các service vi mô. Ghi lại mọi hành động người dùng (thay đổi vai trò, điểm danh, thông báo) với timestamp, user ID, và chi tiết hành động. Đảm bảo logs được giữ lại 1 năm (NFR-006) và tuân thủ luồng xác thực (ARC-006).

#### 📝 Công việc con 4.4: Viết kiểm thử tuân thủ bảo mật
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/infra/test/security_compliance_test.go
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-003], [NFR-008]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện các bài kiểm thử bảo mật và tuân thủ: kiểm tra mã hóa TLS 1.3, xác thực mã hóa AES-256 cho dữ liệu nghỉ, kiểm tra cấu hình IAM, và đảm bảo tuân thủ GDPR/CCPA (quyền xóa dữ liệu, xuất dữ liệu JSON).

#### 📝 Công việc con 4.5: Rà soát cấu hình bảo mật và khoảng trống tuân thủ
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/terraform/security-review.md
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-003], [NFR-008], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát toàn diện các cấu hình bảo mật GCP và GKE. Xác định các khoảng trống tuân thủ so với OWASP Top 10 và yêu cầu GDPR/CCPA. Đề xuất các biện pháp khắc phục và cải tiến.

### 🌤️ NGÀY 5: <!--DAY_HEADER_START-->Hoàn thiện tài liệu, kiểm thử cuối cùng và bàn giao<!--DAY_HEADER_END-->

#### 📝 Công việc con 5.1: Viết tài liệu tổng quan kiến trúc hệ thống
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/architecture-overview.md
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết tài liệu tổng quan kiến trúc hệ thống bao gồm sơ đồ kiến trúc tổng thể, mô tả các luồng chính (xác thực, điểm danh QR, thông báo, tích hợp frontend), và lược đồ các tương tác giữa các service. Bao gồm các yêu cầu phi chức năng về hiệu năng, bảo mật, khả năng sẵn sàng, và tuân thủ.

#### 📝 Công việc con 5.2: Viết tài liệu hướng dẫn vận hành và phục hồi thảm họa
##### Đại lý phụ trách: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/docs/operational-runbooks.md
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-010], [NFR-002], [NFR-009]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Viết hướng dẫn vận hành chi tiết cho đội ngũ vận hành, bao gồm quy trình triển khai, giám sát, xử lý sự cố, và phục hồi thảm họa. Mô tả các bước khôi phục dịch vụ sau khi sự cố, bao gồm cả kịch bản mất kết nối mạng (EXC-001) và sao lưu/khôi phục cơ sở dữ liệu.

#### 📝 Công việc con 5.3: Thực hiện kiểm thử tích hợp toàn hệ thống
##### Đại lý phụ trách: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** INTEGRATION_SCOPE;./sources/infra/test/full_e2e_test.go
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-006], [ARC-007], [ARC-008], [ARC-009], [NFR-001], [NFR-002]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện kiểm thử end-to-end toàn hệ thống trên môi trường staging. Xác minh tất cả các luồng chính hoạt động: đăng ký/đăng nhập, quét QR điểm danh, gửi thông báo, đăng ký khóa học, và phản hồi API trong ngưỡng 200ms (NFR-001). Kiểm tra khả năng chịu lỗi và failover.

#### 📝 Công việc con 5.4: Rà soát cuối cùng mã nguồn và cấu hình
##### Đại lý phụ trách: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/terraform/final-review.md
* **Thẻ truy xuất:** <!--START_TAGS-->[ARC-010], [NFR-003], [NFR-004]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Thực hiện rà soát cuối cùng toàn bộ mã nguồn hạ tầng (Terraform, Kubernetes manifests, Dockerfiles) và cấu hình bảo mật. Đảm bảo không có secrets hardcoded, tất cả cấu hình tuân thủ các tiêu chuẩn bảo mật và yêu cầu phi chức năng.

#### 📝 Công việc con 5.5: Tối ưu hình ảnh Docker và đẩy lên registry
##### Đại lý phụ trách: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn đích:** ./sources/infra/docker/optimize-images.sh
* **Thẻ truy xuất:** <!--START_TAGS-->[NFR-005], [ARC-010]<!--END_TAGS-->
* **Hướng dẫn nhiệm vụ kỹ thuật cấp thấp:** Tối ưu hóa kích thước hình ảnh Docker bằng cách loại bỏ các lớp không cần thiết, sử dụng multi-stage builds hiệu quả, và nén hình ảnh cuối cùng. Đẩy tất cả hình ảnh đã tối ưu lên Google Container Registry với tags phù hợp cho môi trường production.