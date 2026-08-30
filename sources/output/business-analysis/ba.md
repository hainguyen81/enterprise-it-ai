# YÊU CẦU CHUYÊN GIA: social-scheduler

## 📊 Kiểm soát Tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **SRS ID** | SRS-20260830153530 |
| **Project Name** | social-scheduler |
| **Version** | 1.0 (Cơ sở) |
| **Date Time** | 2026/08/30 15:35:30 |
| **Author** | Principal Business Analyst (BA) / Product Strategist (BA Agent) |
| **Approval** | Chờ phê duyệt quản trị kỹ thuật |

## 1. Tổng quan Dự án & Kiến trúc Toàn cầu

- **Mục tiêu Sản phẩm & Giá trị Cốt lõi**
  * Tự động hóa lịch đăng bài trên mạng xã hội để đảm bảo sự hiện diện nhất quán.
  * Cung cấp đề xuất nội dung được hỗ trợ bởi AI nhằm nâng cao tương tác.
  * Cho phép xuất bản đa nền tảng (Facebook, Instagram, TikTok) từ một giao diện duy nhất.

- **Đối tượng Mục tiêu**
  * Chủ doanh nghiệp nhỏ.
  * Quản lý tiếp thị.
  * Chuyên gia marketing tự do.

- **Ma trận Vai trò & Quyền hạn (RBAC)**
  * **[ARC-001]** Quản trị viên: toàn quyền truy cập vào hệ thống, quản lý người dùng, cấu hình nền tảng, xem tất cả lịch đăng bài và báo cáo.
  * **[ARC-002]** Chủ doanh nghiệp: tạo và quản lý lịch đăng bài cho doanh nghiệp của mình, xem báo cáo hiệu suất, cấu hình quyền truy cập của người dùng được chỉ định.
  * **[ARC-003]** Quản lý tiếp thị: lên lịch và theo dõi lịch đăng bài được chỉ định, xem báo cáo hiệu suất cho các chiến dịch được giao.
  * **[ARC-004]** Người dùng lên lịch: tạo và chỉnh sửa lịch đăng bài cá nhân, xem nội dung được đề xuất bởi AI.

- **Blueprint Stack Công nghệ & Hạ tầng**
  * **[ARC-005]** Lõi ứng dụng: Java Spring Boot (v3.2.x) với Kotlin, tích hợp Quarkus cho API gateway.
  * **[ARC-005]** Dịch vụ front-end: React Native (v0.73) cho di động, Next.js (v14) cho web.
  * **[ARC-005]** Cơ sở dữ liệu: PostgreSQL (v15) cho dữ liệu quan hệ, Redis (v7) cho bộ nhớ đệm và theo dõi phiên làm việc.
  * **[ARC-005]** Dịch vụ bên ngoài: GraphQL API gateways cho Facebook, Instagram, TikTok, cùng với SDK xác thực OAuth2.
  * **[ARC-005]** Máy học: Python với scikit-learn và TensorFlow (v2.15) để đào tạo mô hình đề xuất nội dung.
  * **[ARC-005]** CI/CD: GitLab CI, Docker, Kubernetes (GKE) với tự động hóa triển khai canary.
  * **[ARC-005]** Bảo mật: JWT access tokens với thời gian hết hạn ngắn, đa yếu tố cho vai trò quản trị, kiểm toán toàn bộ nhật ký thay đổi dữ liệu.

## 2. Các Mô-đun Tính năng Nâng cao

### Mô-đun 1: Tích hợp Lịch đăng bài Tự động

- **Yêu cầu chức năng cốt lõi**: **[REQ-001]** Tự động hóa lịch đăng bài trên Facebook, Instagram và TikTok thông qua tích hợp API.

  **Tiêu chí chấp nhận**
  * Given tôi là một chủ doanh nghiệp đã xác thực,
    When tôi kết nối tài khoản mạng xã hội của mình và tạo một lịch đăng bài mới với nền tảng, nội dung và thời gian đã chọn,
    Then hệ thống phải lưu lịch đăng bài đó và hiển thị xác nhận thành công với mã lịch đăng bài tương ứng.
  * Given một lịch đăng bài đã lên lịch với trạng thái "đã lên lịch",
    When thời điểm đã lên lịch đã đến,
    Then hệ thống phải gọi API tương ứng của nền tảng và ghi lại kết quả xuất bản trong bảng hiệu suất bài đăng.
  * Given bất kỳ lỗi nào từ API bên thứ ba,
    When hệ thống nhận được phản hồi lỗi,
    Then hệ thống phải ghi lại lỗi vào bảng nhật ký, đánh dấu lịch đăng bài là "lỗi", và lên lịch thử lại sau một khoảng thời gian configurable.

  **Luồng ngoại lệ**
  * **[EXC-001]** Khi API bên thứ ba trả về lỗi, hệ thống phải ghi lại chi tiết lỗi (bao gồm mã lỗi, phản hồi, timestamp), đánh dấu lịch đăng bài là "lỗi", và tự động lên lịch thử lại sau khoảng thời gian thử lại configurable (ví dụ: 5 phút). Nếu số lần thử lại vượt quá ngưỡng tối đa, lịch đăng bài sẽ bị đánh dấu là "thất bại" và thông báo được gửi đến người dùng.

  **Từ điển Dữ liệu**
  * **[DAT-001]** Bảng lưu trữ lịch đăng bài

    | Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
    |-----------|-------------|------------|-------------|
    | id | uuid | PK | Khóa chính, UUID của lịch đăng bài |
    | userId | uuid | FK | Tham chiếu đến Users(userId), không null |
    | platform | varchar |  | Tên nền tảng mạng xã hội (ví dụ: Facebook, Instagram, TikTok), không null |
    | content | text |  | Nội dung bài đăng, không null |
    | scheduledTime | timestamp |  | Thời điểm dự kiến xuất bản, không null |
    | status | varchar |  | Trạng thái hiện tại của lịch đăng bài (ví dụ: đã lên lịch, đã xuất bản, lỗi, đã hủy), không null |

    ```mermaid
    erDiagram
        Users ||--o{ Scheduling : "userId"
        Scheduling {
          uuid id PK "Primary key, UUID"
          uuid userId FK "References Users(userId)"
          varchar platform "Social platform name"
          text content "Post content text"
          timestamp scheduledTime "Scheduled publishing datetime"
          varchar status "Current status of scheduled post"
        }
    ```

  * **[DAT-004]** Bảng thông tin người dùng

    | Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
    |-----------|-------------|------------|-------------|
    | id | uuid | PK | Khóa chính, UUID của người dùng |
    | username | varchar |  | Tên người dùng, không null, duy nhất |
    | email | varchar |  | Địa chỉ email, không null, duy nhất |
    | passwordHash | varchar |  | Băm mật khẩu, không null |
    | createdAt | timestamp |  | Thời điểm tạo tài khoản, không null |
    | updatedAt | timestamp |  | Thời điểm cập nhật tài khoản cuối cùng |

    ```mermaid
    erDiagram
        Users {
          uuid id PK "Primary key"
          varchar username "User's chosen username"
          varchar email "User's email address"
          varchar passwordHash "Hashed password"
          timestamp createdAt "Account creation timestamp"
          timestamp updatedAt "Last update timestamp"
        }
    ```

### Mô-đun 2: Công cụ Đề xuất Nội dung được hỗ trợ bởi AI

- **Yêu cầu chức năng cốt lõi**: **[REQ-002]** Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó.

  **Tiêu chí chấp nhận**
  * Given một người dùng có lịch sử bài đăng,
    When mô hình được huấn luyện,
    Then hệ thống phải cung cấp danh sách nội dung được sắp xếp theo dự đoán tương tác cho mỗi lịch đăng bài được lên lịch tiếp theo.
  * Given một lịch đăng bài được lên lịch mới,
    When người dùng chấp nhận một gợi ý nội dung,
    Then nội dung được chấp nhận phải được điền vào trường nội dung của lịch đăng bài đó.

  **Luồng ngoại lệ**
  * **[EXC-004]** Khi mô hình học máy gặp lỗi trong quá trình dự đoán (ví dụ: đầu vào không hợp lệ, lỗi thuật toán), hệ thống phải ghi lại sự kiện lỗi, sử dụng nội dung mẫu mặc định, và thông báo cho quản trị viên để can thiệp thủ công.

  **Từ điển Dữ liệu**
  * **[DAT-002]** Bảng hiệu suất bài đăng

    | Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
    |-----------|-------------|------------|-------------|
    | id | uuid | PK | Khóa chính, UUID của bản ghi hiệu suất |
    | postId | varchar |  | Tham chiếu đến lịch đăng bài (social-scheduler ID), không null |
    | metricLikes | smallint |  | Số lượt thích thu được |
    | metricComments | smallint |  | Số bình luận thu được |
    | metricShares | smallint |  | Số lượt chia sẻ thu được |
    | collectedAt | timestamp |  | Thời điểm thu thập chỉ số |

    ```mermaid
    erDiagram
        Scheduling ||--o{ PostPerformance : "postId"
        Scheduling {
          uuid id PK "Primary key"
          uuid userId FK "References Users(userId)"
          varchar platform "Platform name"
          text content "Post content"
          timestamp scheduledTime "Scheduled time"
          varchar status "Status"
        }
        PostPerformance {
          uuid id PK "Primary key"
          varchar postId "Reference to scheduled post"
          smallint metricLikes "Number of likes"
          smallint metricComments "Number of comments"
          smallint metricShares "Number of shares"
          timestamp collectedAt "Timestamp of collection"
        }
    ```

### Mô-đun 3: Xác thực, Kiểm soát Tỷ lệ & Bảo mật

- **Yêu cầu chức năng cốt lõi**: **[REQ-003]** Thực hiện xác thực đầu vào dữ liệu và kiểm tra giới hạn tỷ lệ cho từng người dùng.

  **Tiêu chí chấp nhận**
  * Given một yêu cầu tạo lịch đăng bài mới,
    When đầu vào không hợp lệ (ví dụ: thiếu nền tảng, định dạng thời gian không hợp lệ),
    Then hệ thống phải trả về một thông báo lỗi cụ thể và không tạo lịch đăng bài.
  * Given một người dùng vượt quá giới hạn tỷ lệ được phép (ví dụ: quá 10 yêu cầu trong 5 phút),
    When người dùng thực hiện một yêu cầu mới,
    Then hệ thống phải từ chối yêu cầu với một thông báo "vượt quá giới hạn tỷ lệ" và ghi lại sự kiện này.

  **Luồng ngoại lệ**
  * **[EXC-002]** Khi token xác thực hết hạn hoặc không hợp lệ, hệ thống phải làm mới token (nếu có refresh token) hoặc yêu cầu người dùng đăng nhập lại, và ghi lại sự kiện xác thực không thành công.
  * **[EXC-003]** Khi phát hiện một người dùng tạo nhiều lịch đăng bài trong một khoảng thời gian ngắn (ví dụ: < 1 phút), hệ thống phải tạm thời chặn người dùng đó (ví dụ: 5 phút) và ghi lại sự kiện spam.

  **Từ điển Dữ liệu**
  * **[DAT-003]** Bảng theo dõi tỷ lệ giới hạn

    | Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
    |-----------|-------------|------------|-------------|
    | id | uuid | PK | Khóa chính, UUID của bản ghi tỷ lệ |
    | userId | uuid | FK | Tham chiếu đến Users(userId), không null |
    | platform | varchar |  | Nền tảng mục tiêu cho quy tắc tỷ lệ, không null |
    | requestCount | int |  | Số yêu cầu trong cửa sổ hiện tại, không null |
    | windowStart | timestamp |  | Thời điểm bắt đầu cửa sổ tỷ lệ, không null |
    | windowEnd | timestamp |  | Thời điểm kết thúc cửa sổ tỷ lệ, không null |

    ```mermaid
    erDiagram
        Users ||--o{ RateLimitTracking : "userId"
        Users {
          uuid id PK "Primary key"
          varchar username "User's chosen username"
          varchar email "User's email address"
          varchar passwordHash "Hashed password"
          timestamp createdAt "Account creation timestamp"
          timestamp updatedAt "Last update timestamp"
        }
        RateLimitTracking {
          uuid id PK "Primary key"
          uuid userId FK "References Users(userId)"
          varchar platform "Target platform"
          int requestCount "Request count"
          timestamp windowStart "Window start"
          timestamp windowEnd "Window end"
        }
    ```

## 3. Các Yêu cầu Phi chức năng Toàn cầu

- **[NFR-001]** Hiệu suất
  * Thời gian phản hồi trung bình cho các yêu cầu tạo lịch đăng bài phải dưới 200 ms.
  * Thông lượng xử lý lịch đăng bài phải đạt ít nhất 500 yêu cầu mỗi giây.
  * Dịch vụ đề xuất nội dung phải phản hồi trong vòng 100 ms sau khi có yêu cầu.

- **[NFR-002]** Bảo mật
  * Tất cả dữ liệu truyền tải phải được mã hóa bằng TLS 1.3.
  * Xác thực phải sử dụng JWT access token với thời gian hết hạn tối đa là 15 phút; refresh token phải có thời gian sống dài hơn nhưng phải được lưu trữ an toàn trong Redis.
  * Tuân thủ OWASP Top 10: ngăn chặn SQL injection, XSS, và CSRF thông qua các prepared statement và Content Security Policy.
  * Vai trò quản trị viên phải được bảo vệ bằng xác thực đa yếu tố (MFA).
  * Mã hóa dữ liệu nhạy cảm tại chỗ (PSE) cho các trường như passwordHash và nội dung bài đăng.

- **[NFR-003]** Khả năng mở rộng, Tính sẵn sàng cao & Cô lập đa租
  * Hệ thống phải hỗ trợ ít nhất 10,000 người dùng đồng thời với mỗi người dùng có không gian dữ liệu riêng biệt (bộ nhớ tách biệt theo tenant).
  * Triển khai tự động hóa trong Kubernetes với tối thiểu ba bản sao cho mỗi service; sử dụng bộ cân bằng tải và kiểm tra độ khỏe để đảm bảo 99.9% thời gian hoạt động.
  * Cô lập dữ liệu theo tenant thông qua schema prefixes hoặc các cơ sở dữ liệu riêng biệt; đảm bảo không có sự rò rỉ dữ liệu giữa các tenant.
  * Hỗ trợ khả năng mở rộng theo chiều ngang cho dịch vụ đề xuất (sử dụng hàng đợi tin nhắn và các worker có thể mở rộng độc lập).

[EXECUTION_REMEDIATION_PAYLOAD_START]
{
  "technical_codename": "social-scheduler",
  "descriptive_name": "SocialScheduler",
  "brand_name": "LịchĐăngBài",
  "requirement_tags": [
    "[REQ-001]",
    "[REQ-002]",
    "[REQ-003]",
    "[DAT-001]",
    "[DAT-002]",
    "[DAT-003]",
    "[DAT-004]",
    "[EXC-001]",
    "[EXC-002]",
    "[EXC-003]",
    "[EXC-004]",
    "[ARC-001]",
    "[ARC-002]",
    "[ARC-003]",
    "[ARC-004]",
    "[ARC-005]",
    "[NFR-001]",
    "[NFR-002]",
    "[NFR-003]"
  ]
}