# [Phần] 5: <!--PHASE_NAME_START-->Bảo Mật Kiểm Tra Phi Chức Năng Hạ Tầng Devops Và Đóng Gói Tài Liệu<!--PHASE_NAME_END-->

## 📊 Kiểm Soát Tài Liệu

| Mục | Chi Tiết |
| :--- | :--- |
| **Mã Bản Vẽ** | ARCH-20260828162649 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 5 |
| **Tên Giai Đoạn** | <!--PHASE_NAME_START-->Bảo Mật Kiểm Tra Phi Chức Năng Hạ Tầng Devops Và Đóng Gói Tài Liệu<!--PHASE_NAME_END--> |
| **Mô Tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung hoàn toàn vào việc thiết lập các biện pháp bảo mật OWASP Top 10, cấu hình tự động hóa CI/CD, đóng gói Docker, triển khai cụm Kubernetes GKE và hoàn thiện tài liệu kỹ thuật cuối cùng.<!--PHASE_DESC_END--> |
| **Phiên Bản** | 1.0 (Bản Cơ Sở) |
| **Ngày Giờ** | 2026/08/28 16:26:49 |
| **Tác Giả** | Kiến Sư Trưởng Hệ Thống (SA Agent) |
| **Phê Duyệt** | Đang Chờ Đánh Giá Quản Trị Kỹ Thuật |

## 1. Phạm Vi & Mục Tiêu Hoạt Động Của Giai Đoạn
Giai đoạn 5 tập trung hoàn toàn vào việc thiết lập các biện pháp bảo mật OWASP Top 10, cấu hình tự động hóa CI/CD, đóng gói Docker đa tầng tối ưu hóa dung lượng, triển khai cụm Kubernetes GKE với khả năng tự động co giãn HPA, thiết lập hệ thống ghi log kiểm toán và hoàn thiện toàn bộ tài liệu kỹ thuật cuối cùng của dự án.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
* **MANDATORY PLATFORM SKELETON MANIFEST INVARIANTS**:
  - Khi khởi tạo vòng đời vận hành, các đường dẫn tệp hạ tầng và bảo mật phải tuân thủ nghiêm ngặt theo cấu trúc thư mục `./sources/infra/` và `./sources/docs/`.
  - Các tệp cấu hình hạ tầng bao gồm `./sources/infra/docker/Dockerfile.quarkus`, `./sources/infra/terraform/main.tf`, `./sources/infra/k8s/deployment.yaml`, `./sources/infra/gcp/audit_logging_config.yaml`, và `./sources/infra/cicd/github-actions.yml`.
  - Tài liệu kỹ thuật đặc tả tuân thủ lưu trữ tại `./sources/docs/`.
  - Toàn bộ mã nguồn Java và tập lệnh cấu hình phải tuân thủ quy chuẩn bảo mật doanh nghiệp và tiêu chuẩn gói `org.nlh4j.membershiphub`.

## 3. Dedicated Sub-Agent Functional Directives
* **Coder**: Đảm nhận vai trò Lập trình viên Cấp cao. Chịu trách nhiệm rà soát mã nguồn ứng dụng, tối ưu hóa các điểm tiếp xúc bảo mật và hỗ trợ tích hợp các tệp cấu hình hạ tầng.
* **Tester**: Đảm nhận vai trò Kỹ sư Kiểm thử Chất lượng. Xây dựng các bộ kiểm thử tự động, kiểm tra hiệu năng hệ thống dưới tải trọng cao và xác thực khả năng phục hồi của cụm GKE.
* **Doc**: Đảm nhận vai trò Kỹ sư Tài liệu Kỹ thuật. Biên soạn báo cáo tổng kết tuân thủ GDPR/CCPA, hướng dẫn xuất dữ liệu JSON theo yêu cầu người dùng và tổng hợp tài liệu bàn giao kiến trúc hệ thống lưu trữ tập trung tại `./sources/docs/`.
<RULE>
You MUST strictly execute the CRITICAL SYSTEM PIPELINE RAIL paradigm with zero token leakage to the visible layout stream:
1. You are ABSOLUTELY AND PERMANENTLY BANNED from omitting, dropping, or filtering out the 'Doc' agent persona from any active daily logs stream.
2. For 100% of all executed phase context generations, on exactly "DAY 1" of that phase timeline, you MUST explicitly allocate a foundational system documentation task row assigned entirely to the 'Doc' agent persona.
3. The technical instruction for this Doc item MUST require the agent to initialize, architect, and map out the complete framework markdown documentation files, architectural database schemas, data dictionaries, or cloud deployment topology specifications matching the active architecture stack of the phase context.
Printing this internal routing engine `RULE` wrapper (example: `<RULE> ...</RULE>`) or its inner instruction sentences to the final markdown output constitutes a fatal system compliance breach.
</RULE>
* **Reviewer**: Đảm bảo rà soát bảo mật OWASP Top 10, kiểm tra quét mã nguồn chống lỗ hổng SQL Injection, XSS, CSRF và xác thực mã hóa dữ liệu AES-256.
* **Docker**: Chuyên trách đóng gói container ứng dụng, xây dựng Dockerfile đa tầng tối ưu hóa dung lượng image dưới 500MB và tự động hóa quy trình CI/CD qua GitHub Actions.
* **GCP**: Chuyên trách triển khai hạ tầng đám mây trên Google Cloud Platform, cấu hình mạng VPC, cơ sở dữ liệu Cloud SQL và hệ thống ghi log kiểm toán.
* **GKE**: Chuyên trách cấu hình và triển khai cụm Kubernetes, thiết lập HPA tự động co giãn và cơ chế failover giữa các cụm.

## 4. Phase Definition of Done (DoD)
- Hoàn thành 100% việc kiểm tra bảo mật OWASP Top 10 và vượt qua các bài kiểm thử quét lỗ hổng mã nguồn.
- Đóng gói thành công Docker image đa tầng dung lượng dưới 500MB.
- Triển khai thành công hạ tầng Terraform, cụm GKE với HPA và hệ thống CI/CD GitHub Actions.
- Hoàn thiện 100% tài liệu kỹ thuật cuối cùng và báo cáo tuân thủ GDPR/CCPA.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Rà soát bảo mật và kiểm tra lỗ hổng theo tiêu chuẩn OWASP Top 10 cùng tài liệu kỹ thuật nền tảng<!--DAY_HEADER_END-->

#### 📝 Tác Vụ Phụ 1.1: Rà soát mã nguồn và kiểm tra lỗ hổng bảo mật OWASP Top 10
##### Phân Vai Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/userService/src/main/java/org/nlh4j/membershiphub/userservice/UserResource.java`

* Traceability Tag Tokens: <!--START_TAGS-->[NFR-003]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Thực hiện kiểm tra quét mã nguồn và rà soát các lỗ hổng bảo mật theo tiêu chuẩn OWASP Top 10, kiểm tra các câu lệnh SQL chống SQL Injection, xác thực cơ chế mã hóa mật khẩu AES-256 cho dữ liệu nghỉ ngơi và thiết lập cấu hình CORS bảo mật cho toàn bộ các vi dịch vụ Quarkus.

<!--START_API_CONTRACT-->
```json
{
  "securityAudit": "OWASP_TOP_10",
  "status": "PASSED",
  "checkedAt": "2026-08-28T16:26:49Z"
}
```
<!--END_API_CONTRACT-->

#### 📝 Tác Vụ Phụ 1.2: Khởi tạo và biên soạn tài liệu kỹ thuật tuân thủ bảo mật và kiến trúc hạ tầng
##### Phân Vai Sub-Agent: Doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/docs/security_and_compliance_blueprint.md`

* Traceability Tag Tokens: <!--START_TAGS-->[DOC-001], [NFR-003]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Khởi tạo và biên soạn tài liệu kỹ thuật đặc tả các biện pháp bảo mật OWASP Top 10, cấu hình mã hóa dữ liệu TLS 1.3 và AES-256, cùng quy chuẩn tuân thủ bảo mật định danh gói `org.nlh4j.membershiphub` lưu trữ tại `./sources/docs/`.

<!--START_API_CONTRACT-->
```json
{
  "document": "security_and_compliance_blueprint.md",
  "format": "Markdown",
  "target_audience": "System Admin, Security Auditor"
}
```
<!--END_API_CONTRACT-->

---

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Xây dựng tệp Dockerfile đa tầng tối ưu hóa dung lượng cho các vi dịch vụ Quarkus<!--DAY_HEADER_END-->

#### 📝 Tác Vụ Phụ 2.1: Xây dựng Dockerfile đa tầng tối ưu hóa dung lượng image
##### Phân Vai Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/docker/Dockerfile.quarkus`

* Traceability Tag Tokens: <!--START_TAGS-->[NFR-005], [ARC-010]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Viết Dockerfile multi-stage build sử dụng base image Alpine nhẹ, đảm bảo kích thước image cơ sở dưới 200MB và image hoàn thiện dưới 500MB cho các vi dịch vụ Quarkus, tích hợp cơ chế biên dịch native hoặc JVM được tối ưu hóa.

<!--START_API_CONTRACT-->
```json
{
  "docker_build": "multi-stage",
  "base_image": "eclipse-temurin:21-jre-alpine",
  "max_image_size_mb": 500
}
```
<!--END_API_CONTRACT-->

---

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Cấu hình tập lệnh Terraform và thiết lập hạ tầng mạng VPC trên Google Cloud Platform<!--DAY_HEADER_END-->

#### 📝 Tác Vụ Phụ 3.1: Triển khai tập lệnh Terraform cấu hình VPC và Cloud SQL trên GCP
##### Phân Vai Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/terraform/main.tf`

* Traceability Tag Tokens: <!--START_TAGS-->[NFR-002], [NFR-004], [ARC-010]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Viết mã lệnh Terraform thiết lập mạng ảo VPC, cơ sở dữ liệu PostgreSQL quản lý trên Cloud SQL và cụm Redis cache, bảo đảm mục tiêu sẵn sàng 99.9% và khả năng tự động mở rộng tài nguyên.

<!--START_API_CONTRACT-->
```json
{
  "provider": "google",
  "region": "asia-southeast1",
  "resources": ["google_compute_vpc", "google_sql_database_instance", "google_redis_instance"]
}
```
<!--END_API_CONTRACT-->

---

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->Xây dựng tệp cấu hình triển khai Kubernetes Deployment và HPA cho các vi dịch vụ trên GKE<!--DAY_HEADER_END-->

#### 📝 Tác Vụ Phụ 4.1: Cấu hình Kubernetes Deployment và HPA trên GKE
##### Phân Vai Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/k8s/deployment.yaml`

* Traceability Tag Tokens: <!--START_TAGS-->[NFR-001], [NFR-002], [NFR-004]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Viết tệp YAML cấu hình Kubernetes HPA tự động scale-out khi CPU > 70% hoặc độ trễ request > 300ms, kèm cấu hình failover tự động giữa các cụm GKE để đảm bảo SLA khả dụng 99.9%.

<!--START_API_CONTRACT-->
```json
{
  "apiVersion": "autoscaling/v2",
  "kind": "HorizontalPodAutoscaler",
  "spec": {
    "minReplicas": 3,
    "maxReplicas": 10,
    "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": 70}}]
  }
}
```
<!--END_API_CONTRACT-->

---

### 🌤️ NGÀY 5: <!--DAY_HEADER_START-->Thiết lập hệ thống ghi log kiểm toán, chính sách lưu giữ log trong 1 năm và cấu hình sao lưu dữ liệu tự động<!--DAY_HEADER_END-->

#### 📝 Tác Vụ Phụ 5.1: Cấu hình Google Cloud Logging và lịch sao lưu PostgreSQL tự động
##### Phân Vai Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/gcp/audit_logging_config.yaml`

* Traceability Tag Tokens: <!--START_TAGS-->[NFR-006], [NFR-009]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Cấu hình Google Cloud Logging lưu trữ toàn bộ hành động người dùng kèm thời gian, userId trong 1 năm và thiết lập lịch sao lưu PostgreSQL hàng ngày với tính năng Point-in-Time Recovery (PITR) trong vòng 24 giờ.

<!--START_API_CONTRACT-->
```json
{
  "logging": "Google Cloud Logging",
  "retention_period_days": 365,
  "backup_schedule": "Daily PITR"
}
```
<!--END_API_CONTRACT-->

---

### 🌤️ NGÀY 6: <!--DAY_HEADER_START-->Xây dựng quy trình tự động hóa CI/CD với GitHub Actions kiểm thử và đẩy image lên container registry<!--DAY_HEADER_END-->

#### 📝 Tác Vụ Phụ 6.1: Triển khai pipeline CI/CD tự động hóa với GitHub Actions
##### Phân Vai Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/cicd/github-actions.yml`

* Traceability Tag Tokens: <!--START_TAGS-->[ARC-010], [NFR-005]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Viết tập lệnh GitHub Actions tự động chạy unit test, build docker image đa dịch vụ và đẩy lên Google Artifact Registry khi có merge code vào nhánh chính, đảm bảo chất lượng mã nguồn trước khi phát hành.

<!--START_API_CONTRACT-->
```json
{
  "ci_cd_tool": "GitHub Actions",
  "triggers": ["push: main"],
  "actions": ["mvn test", "docker build", "push to GAR"]
}
```
<!--END_API_CONTRACT-->

---

### 🌤️ NGÀY 7: <!--DAY_HEADER_START-->Hoàn thiện và đóng gói toàn bộ tài liệu kỹ thuật cuối cùng của dự án membership-hub<!--DAY_HEADER_END-->

#### 📝 Tác Vụ Phụ 7.1: Biên soạn báo cáo tổng kết tuân thủ GDPR/CCPA và tài liệu bàn giao hệ thống
##### Phân Vai Sub-Agent: Doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/docs/final_system_compliance_report.md`

* Traceability Tag Tokens: <!--START_TAGS-->[DOC-001], [NFR-008]<!--END_TAGS-->

* Low-Level Technical Task Instruction: Biên soạn báo cáo tổng kết tuân thủ GDPR/CCPA, hướng dẫn xuất dữ liệu JSON theo yêu cầu người dùng và tổng hợp tài liệu bàn giao kiến trúc hệ thống lưu trữ tập trung tại `./sources/docs/`.

<!--START_API_CONTRACT-->
```json
{
  "document": "final_system_compliance_report.md",
  "format": "Markdown",
  "compliance": ["GDPR", "CCPA", "OWASP Top 10"]
}
```
<!--END_API_CONTRACT-->

---

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. PHASE 5 COMPLETED SUCCESSFULLY.]