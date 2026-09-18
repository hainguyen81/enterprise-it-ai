## 📊 Kiểm soát Tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| Mã Tài liệu | UIUX-AUDIT-20260918154116 |
| Tên Dự án | social-scheduler |
| Phiên bản | 1.0 — Bản draft |
| Ngày Giờ | 2026/09/18 15:14:55 |
| Tác giả | Principal UI/UX Auditor |
| Phê duyệt | Chờ phê duyệt |

### Hệ thống Thiết kế Toàn cục & Kích thước Ký tự

*Lưu ý: SRS không cung cấp định nghĩa thiết kế token chi tiết. Bản thiết kế UI/UX giả định sử dụng hệ thống thiết kế doanh nghiệp tiêu chuẩn. Các token sau đây được đề xuất dựa trên các hạn chế kiến trúc được xác định:*

| Token | Giá trị (ví dụ) | Ghi chú |
| :--- | :--- | :--- |
| Màu thương hiệu | --color-primary: #004080; --color-secondary: #6c757d | Được sử dụng cho các yếu tố hành động chính và trung tính. |
| Kiểu chữ tiêu đề | --font-heading: 'Roboto', 700, 24px | Áp dụng cho tất cả các tiêu đề. |
| Kiểu chữ cơ thể | --font-body: 'Open Sans', 400, 16px | Áp dụng cho nội dung và nhãn. |
| Kích thước nút | --size-button-height: 44px; --size-button-padding: 12px 24px | Đảm bảo khả năng tiếp cận. |
| Độ cong góc | --radius-sm: 4px; --radius-md: 8px | Được sử dụng cho các góc bo. |
| Độ dày | --border-width: 1px | Được sử dụng cho các đường viền. |
| Điểm dừng phản hồi | --breakpoint-sm: 600px; --breakpoint-md: 900px; --breakpoint-lg: 1200px | Được sử dụng cho bố cục phản hồi. |
| Màu nền | --bg-primary: #ffffff; --bg-secondary: #f8f9fa | Áp dụng cho các vùng chính và phụ. |
| Màu văn bản | --text-primary: #212529; --text-secondary: #6c757d | Đảm bảo độ tương phản. |
| Mã hóa | AES‑256 (lưu trữ) | Được yêu cầu bởi [NFR-003]. |
| Xác thực OAuth | OAuth 2.0 | Được yêu cầu bởi [ARC-001]. |

Tất cả các giá trị token trên là giả định; nhóm thiết kế hệ thống phải xác nhận chúng với các bên liên quan trong dự án.

### Bản thiết kế khung dây (wireframe) theo Epic Module

#### Epic Module 1: Tích hợp Lịch đăng bài Đa nền tảng

**Mục đích:** Cho phép người dùng tạo, quản lý và theo dõi các lịch đăng bài trên Facebook, Instagram và TikTok. Hỗ trợ tự động hóa việc xuất bản, xử lý lỗi, thử lại và bảo vệ chống spam.

**Thành phần chính & Dòng chảy:**

| Màn hình | Vùng bố cục | Thành phần chính | Tương tác & Trạng thái | Xác thực/Phản hồi | Khả năng phản hồi & Khả năng tiếp cận | Token thiết kế được áp dụng | Nguồn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Đăng nhập / Xác thực OAuth** | Toàn màn hình | Logo, nút "Đăng nhập bằng OAuth", thông báo lỗi | Bắt đầu luồng OAuth 2.0 → chuyển hướng đến nhà cung cấp → xử lý mã truy cập. Hiển thị trạng thái *đang tải* trong khi chuyển hướng. | Xác thực mã thông báo, hiển thị lỗi *xác thực không thành công* (HTTP 400). | Các nút có thể tập trung bằng bàn phím; thông báo ARIA cho trạng thái. | `--color-primary`, `--size-button-height` | [ARC-001], [REQ-001] |
| **Bảng điều khiển người dùng** | Đầu trang, thanh bên, vùng nội dung chính | Thanh điều hướng, thẻ thống kê (lịch đã lên lịch, đã đăng, sắp tới), nút "Tạo lịch mới", liên kết nhanh đến đề xuất và hiệu suất | Chuyển đổi vai trò (Người dùng/Admin). Hiển thị *trống* khi không có lịch. | N/A | Bố cục lưới đáp ứng; sử dụng `aria-label` cho thẻ thống kê. | `--bg-primary`, `--radius-md` | [REQ-001], [DAT-001] |
| **Danh sách lịch đăng bài** | Vùng nội dung chính | Thanh tìm kiếm/bộ lọc (theo nền tảng, trạng thái), bảng dữ liệu (ID, nền tảng, nội dung, thời gian đã lên lịch, trạng thái), nút "Tạo lịch mới" | *Tải* dữ liệu khi vào; *sửa* hoặc *xóa* qua menu hành động hàng; *trạng thái* có thể là **scheduled**, **published**, **cancelled**, **failed**, **awaiting authentication**. Hiển thị *trạng thái đang tải* khi thao tác. | Xác thực phía máy khách cho định dạng thời gian (ISO‑8601) → hiển thị lỗi *định dạng không hợp lệ* (HTTP 400). Phát hiện trùng lặp nội dung trong cùng một giờ → lỗi *xung đột* (HTTP 409). Vượt quá giới hạn tốc độ (10 yêu cầu/phút) → cảnh báo *đã quá tải* (HTTP 429) với `Retry-After`. | Bảng đáp ứng: thu gọn cột trên thiết bị di động, cuộn ngang. Các hành động hàng có thể kích hoạt bằng bàn phím (Enter, Space). | `--breakpoint-sm`, `--color-danger: #dc3545` | [REQ-001], [EXC-001], [EXC-002], [EXC-003], [NFR-001] |
| **Chi tiết / Chỉnh sửa lịch** | Vùng nội dung chính (form toàn màn hình hoặc hộp thoại) | Các trường nhập liệu (nền tảng (Facebook, Instagram, TikTok), nội dung (văn bản), thời gian đã lên lịch (trình chọn ngày/giờ)), nút "Lưu", "Hủy", "Xóa", chỉ báo trạng thái *đang tải* | *Tải* dữ liệu lịch hiện tại khi chỉnh sửa; *cập nhật* qua API; hiển thị *thành công* hoặc *lỗi* (ví dụ: token hết hạn). Hiển thị *cảnh báo hiệu suất thấp* khi điểm dự đoán < 0.3 (xem Module 2). | Xác thực phía máy khách: nền tảng không được để trống, nội dung không được để trống, thời gian đã lên lịch phải là ISO‑8601 trong tương lai. Hiển thị lỗi xác thực ngay lập tức. | Form đáp ứng: xếp chồng theo chiều dọc trên thiết bị di động; trình chọn ngày tích hợp sẵn hỗ trợ điều hướng bằng bàn phím. | `--radius-md`, `--color-warning: #ffc107` | [REQ-001], [DAT-001], [REQ-002] |
| **Cửa sổ bật lên xác nhận xóa** | Toàn màn hình (trò chơi mô phỏng) | Tiêu đề, nội dung, nút "Xác nhận xóa", "Hủy" | Xác nhận xóa sau khi người dùng xác nhận. Hiển thị *trạng thái đang tải* trong khi xóa. | N/A | Các nút có thể tập trung bằng bàn phím; thông báo ARIA cho trạng thái. | `--color-danger` | [REQ-001] |
| **Cửa sổ bật lên lỗi / Thông báo** | Toàn màn hình (trò chơi mô phỏng) | Tiêu đề lỗi, mô tả, nút "Thử lại", "Đóng" | Hiển thị lỗi từ hệ thống (ví dụ: lỗi API bên thứ ba, token hết hạn, lỗi mạng). *Thử lại* có thể kích hoạt lại công việc đã lên lịch (tối đa 3 lần với backoff theo cấp số nhân). Hiển thị *trạng thái đang tải* trong khi thử lại. | N/A | Thông báo có thể đọc được bằng screen reader; các nút có thể tập trung bằng bàn phím. | `--color-danger` | [EXC-001], [EXC-002], [EXC-004] |
| **Cửa sổ bật lên cảnh báo giới hạn tốc độ** | Toàn màn hình (trò chơi mô phỏng) | Tiêu đề, thông báo "Bạn đã vượt quá giới hạn tốc độ. Vui lòng thử lại sau {Retry-After} giây.", nút "OK" | Hiển thị khi yêu cầu bị từ chối bởi HTTP 429. | N/A | Các nút có thể tập trung bằng bàn phím; thông báo ARIA cho người dùng phụ thuộc vào bàn phím. | `--color-warning` | [NFR-001] |
| **Cửa sổ bật lên cảnh báo hiệu suất thấp** | Toàn màn hình (trò chơi mô phỏng) | Tiêu đề, nội dung "Điểm dự đoán thấp (<0.3). Bạn có chắc chắn muốn tiếp tục không?", nút "Tiếp tục", "Hủy" | Hiển thị khi người dùng cố gắng lên lịch một bài đăng có điểm dự đoán thấp (xem Module 2). | N/A | Các nút có thể tập trung bằng bàn phím; thông báo ARIA. | `--color-warning` | [REQ-002] |
| **Quản lý kết nối nền tảng** | Thanh bên / Cài đặt | Danh sách các nền tảng (Facebook, Instagram, TikTok) với trạng thái kết nối, nút "Kết nối" / "Ngắt kết nối" | Bắt đầu luồng OAuth cho nền tảng được chọn; hiển thị *đang kết nối* trong khi chờ mã thông báo. Hiển thị *đã kết nối* sau khi nhận mã thông báo thành công. | Xác thực mã thông báo; hiển thị lỗi *xác thực không thành công*. | Các nút đáp ứng; sử dụng `aria-live` để thông báo trạng thái. | `--color-primary` | [ARC-001], [REQ-001] |
| **Cài đặt / Hồ sơ người dùng** | Thanh bên | Ảnh đại diện, trường tên, liên kết quản lý nền tảng, chế độ tối (nếu có) | Chỉnh sửa trường tên; tải lên ảnh đại diện; chuyển đổi chế độ tối. Hiển thị *trạng thái đang lưu* sau khi thay đổi. | Xác thực đầu vào (không được để trống). Hiển thị thông báo *cập nhật thành công*. | Các trường nhập liệu đáp ứng; các nút có thể tập trung bằng bàn phím. | `--bg-secondary` | [REQ-001] |

**Luồng ngoại lệ & Xử lý lỗi (được tham chiếu bởi các thẻ nguồn):**

- **[EXC-001]** – Lỗi API bên thứ ba: Hệ thống tự động *thử lại* tối đa 3 lần với backoff theo cấp số nhân. Nếu tất cả lần thử đều thất bại, lịch được đánh dấu là **failed** và một *cửa sổ bật lên lỗi* được hiển thị với tùy chọn *thủ công*.
- **[EXC-002]** – Token hết hạn: Phát hiện token không hợp lệ, khởi động lại quy trình OAuth cho người dùng, thu thập mã thông báo mới và tiếp tục lịch đang chờ xử lý. Nếu xác thực lại không thành công, lịch được chuyển sang trạng thái **awaiting authentication** và một *cửa sổ bật lên xác thực* được hiển thị.
- **[EXC-003]** – Bảo vệ chống spam: Vượt quá ngưỡng (ví dụ: >5 bài đăng trong 10 phút) sẽ kích hoạt *cửa sổ bật lên cảnh báo giới hạn tốc độ* và chặn các yêu cầu lên lịch tiếp theo trong 30 phút.
- **[EXC-004]** – Lỗi mạng: Ghi lại sự cố, đưa công việc vào *hàng đợi* để thử lại sau 5 phút, hiển thị *cửa sổ bật lên lỗi mạng* với thông báo "Yêu cầu của bạn sẽ được tự động thử lại sau 5 phút."

**Chế độ xem dành cho quản trị viên (theo RBAC):**

| Màn hình | Mô tả | Chức năng chính | Nguồn |
| :--- | :--- | :--- | :--- |
| **Bảng điều khiển quản trị** | Tổng quan về hệ thống, thống kê người dùng, kết nối nền tảng, lỗi gần đây | Xem tất cả lịch, người dùng và hiệu suất; kích hoạt/ngắt kích hoạt người dùng; xem nhật ký hệ thống | [REQ-001], [DAT-001], [DAT-002] |
| **Danh sách người dùng** | Danh sách người dùng với vai trò, trạng thái, ngày tạo | Tạo người dùng mới, chỉnh sửa vai trò, đặt lại mật khẩu, xóa người dùng | [REQ-001] |
| **Quản lý nền tảng** | Quản lý các client OAuth cho Facebook, Instagram, TikTok | Thêm/xóa client ID, bí mật, khóa chuyển đổi, xem trạng thái kết nối | [ARC-001], [REQ-001] |
| **Nhật ký hệ thống** | Dòng thời gian chi tiết về các sự kiện, lỗi, lần thử lại | Lọc theo mức độ nghiêm trọng, tải xuống CSV | [EXC-001], [EXC-004] |
| **Theo dõi hiệu suất** | Biểu đồ tổng hợp lượt thích, bình luận, chia sẻ trên tất cả lịch | Xuất dữ liệu, lọc theo người dùng/nền tảng | [DAT-002] |

Tất cả các màn hình quản trị đều tuân thủ cùng một hệ thống phân cấp phân trang, bộ lọc và mẫu thiết kế như giao diện người dùng, sử dụng các token thiết kế được xác định ở trên.

#### Epic Module 2: Đề xuất Nội dung được hỗ trợ bởi AI

**Mục đích:** Hiển thị cho người dùng các ý tưởng bài đăng được đề xuất dựa trên hiệu suất lịch sử, cho phép họ đánh giá điểm dự đoán và lên lịch các bài đăng được chọn.

**Thành phần chính & Dòng chảy:**

| Màn hình | Vùng bố cục | Thành phần chính | Tương tác & Trạng thái | Xác thực/Phản hồi | Khả năng phản hồi & Khả năng tiếp cận | Token thiết kế được áp dụng | Nguồn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Trang đề xuất nội dung** | Toàn màn hình | Thanh tiêu đề ("Đề xuất Nội dung"), lưới thẻ (mỗi thẻ: nội dung, điểm dự đoán, nút "Sử dụng để lên lịch"), thanh tìm kiếm/bộ lọc (theo điểm số) | *Tải* danh sách khi vào; *chọn* một thẻ để xem chi tiết; *lên lịch* một bài đăng được chọn sẽ chuyển hướng đến form Module 1 với nội dung được điền sẵn. Hiển thị *trạng thái đang tải* khi lấy đề xuất. | Nếu điểm dự đoán < 0.3, thẻ sẽ được đánh dấu bằng *cảnh báo hiệu suất thấp* (xem Module 1). Nếu mô hình ML không khả dụng, hiển thị *cảnh báo chung* và một đề xuất chung. | Lưới thẻ đáp ứng: 3 cột trên máy tính để bàn, 2 cột trên máy tính bảng, 1 cột trên thiết bị di động. Các thẻ có thể tập trung bằng bàn phím; nút "Sử dụng để lên lịch" có thể kích hoạt bằng Enter. | `--radius-md`, `--color-warning` | [REQ-002], [DAT-002] |
| **Chi tiết đề xuất** (cửa sổ bật lên / trang con) | Trung tâm | Nội dung được đề xuất, điểm dự đoán, thang đánh giá (0‑1), nút "Bỏ qua", "Sử dụng để lên lịch" | Hiển thị chi tiết; *lên lịch* chuyển hướng đến form Module 1. | N/A | Các nút có thể tập trung bằng bàn phím; thông báo ARIA cho điểm số. | `--color-primary` | [REQ-002] |

**Luồng ngoại lệ:** Không có ngoại lệ cụ thể được định nghĩa trong SRS cho Module 2.

**Chế độ xem dành cho quản trị viên (theo RBAC):**

| Màn hình | Mô tả | Chức năng chính | Nguồn |
| :--- | :--- | :--- | :--- |
| **Theo dõi mô hình ML** | Tổng quan về việc sử dụng mô hình, thời gian đào tạo, điểm số gần đây | Xem trạng thái mô hình, khởi động lại quá trình đào tạo (nếu cần) | [REQ-002] |

#### Epic Module 3: Xác thực Dữ liệu Đầu vào và Kiểm soát Tốc độ

**Mục đích:** Thực thi xác thực dữ liệu nghiêm ngặt và các giới hạn tốc độ theo từng người dùng để bảo vệ các nền tảng bên thứ ba và ngăn chặn spam.

**Thành phần chính & Dòng chảy:**

| Màn hình | Vùng bố cục | Thành phần chính | Tương tác & Trạng thái | Xác thực/Phản hồi | Khả năng phản hồi & Khả năng tiếp cận | Token thiết kế được áp dụng | Nguồn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Trang xác thực lỗi** (toàn màn hình) | Toàn màn hình | Mã lỗi (ví dụ: 400, 409, 429), tiêu đề, mô tả, nút "Quay lại trang trước" | Hiển thị thông báo lỗi chi tiết từ hệ thống (ví dụ: "Định dạng thời gian đã lên lịch không hợp lệ. Vui lòng sử dụng định dạng ISO‑8601."). | N/A | Các nút có thể tập trung bằng bàn phím; thông báo ARIA cho người dùng phụ thuộc vào bàn phím. | `--color-danger` | [REQ-003], [NFR-001] |
| **Cửa sổ bật lên cảnh báo trùng lặp** | Toàn màn hình (trò chơi mô phỏng) | Tiêu đề, nội dung, nút "OK" | Hiển thị khi phát hiện trùng lặp nội dung trong cùng một giờ (HTTP 409). | N/A | Các nút có thể tập trung bằng bàn phím; thông báo ARIA. | `--color-warning` | [REQ-003] |
| **Cửa sổ bật lên cảnh báo giới hạn tốc độ** (được tham chiếu bởi Module 1) | Toàn màn hình (trò chơi mô phỏng) | Tiêu đề, nội dung "Bạn đã vượt quá giới hạn tốc độ. Vui lòng thử lại sau {Retry-After} giây.", nút "OK" | Hiển thị khi yêu cầu bị từ chối bởi HTTP 429. | N/A | Các nút có thể tập trung bằng bàn phím; thông báo ARIA. | `--color-warning` | [NFR-001] |

Tất cả các xác thực được thực hiện phía máy khách với xác thực phía máy chủ bổ sung. Các thông báo lỗi tuân thủ các mẫu thiết kế được xác định ở trên.

**Chế độ xem dành cho quản trị viên (theo RBAC):**

| Màn hình | Mô tả | Chức năng chính | Nguồn |
| :--- | :--- | :--- | :--- |
| **Theo dõi tốc độ** | Biểu đồ thời gian thực về các yêu cầu theo từng người dùng, giới hạn đã đạt được, lần vi phạm | Điều chỉnh giới hạn tốc độ toàn cầu, xem nhật ký vi phạm | [NFR-001] |
| **Cấu hình xác thực** | Quản lý các quy tắc xác thực (ví dụ: định dạng ngày tháng, độ dài nội dung, danh sách từ cấm) | Thêm/sửa/xóa quy tắc xác thực | [REQ-003] |

### Bản phân chia bố cục màn hình

| Màn hình | Vai trò chính | Vùng bố cục chính | Thành phần chính | Trạng thái chính | Điểm dừng phản hồi | Ghi chú về khả năng tiếp cận | Token thiết kế được tham chiếu | Nguồn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Đăng nhập / Xác thực OAuth** | Tất cả người dùng | Toàn màn hình | Logo, nút "Đăng nhập bằng OAuth", thông báo lỗi | *chờ*, *đang tải*, *thành công*, *lỗi* | --breakpoint-sm, --breakpoint-md | Các nút có thể tập trung bằng bàn phím, thông báo ARIA | `--color-primary`, `--size-button-height` | [ARC-001], [REQ-001] |
| **Bảng điều khiển người dùng** | Người dùng / Quản trị viên | Đầu trang, thanh bên, vùng nội dung chính | Thanh điều hướng, thẻ thống kê, nút "Tạo lịch mới", liên kết nhanh | *rỗng*, *đang tải*, *có dữ liệu* | Các breakpoint tiêu chuẩn | `aria-label` cho thẻ, điều hướng bằng bàn phím cho thanh bên | `--bg-primary`, `--radius-md` | [REQ-001] |
| **Danh sách lịch đăng bài** | Người dùng | Vùng nội dung chính (bảng + thanh công cụ) | Thanh tìm kiếm/bộ lọc, bảng, nút hành động hàng | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Điều hướng bảng bằng bàn phím, thông báo ARIA cho trạng thái | `--breakpoint-sm` | [REQ-001], [EXC-001] |
| **Chi tiết / Chỉnh sửa lịch** | Người dùng | Form toàn màn hình hoặc hộp thoại | Các trường nhập liệu, nút hành động | *đang tải*, *thành công*, *lỗi* | Các breakpoint tiêu chuẩn | Các trường nhập liệu hỗ trợ nhập liệu bằng bàn phím, thông báo ARIA cho lỗi | `--radius-md` | [REQ-001] |
| **Trang đề xuất nội dung** | Người dùng | Lưới thẻ toàn màn hình | Thanh tiêu đề, lưới, bộ lọc | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Các thẻ có thể tập trung bằng bàn phím, thông báo ARIA cho điểm số | `--radius-md` | [REQ-002] |
| **Quản lý kết nối nền tảng** | Người dùng | Thanh bên / Cài đặt | Danh sách, nút "Kết nối" | *đang tải*, *đã kết nối*, *lỗi* | Các breakpoint tiêu chuẩn | Các nút có thể tập trung bằng bàn phím, thông báo ARIA | `--color-primary` | [ARC-001] |
| **Cài đặt / Hồ sơ người dùng** | Người dùng | Thanh bên | Ảnh đại diện, trường tên, liên kết | *đang chỉnh sửa*, *đang lưu*, *đã lưu* | Các breakpoint tiêu chuẩn | Các trường nhập liệu hỗ trợ nhập liệu bằng bàn phím, thông báo ARIA | `--bg-secondary` | [REQ-001] |
| **Trang xác thực lỗi** | Tất cả người dùng | Toàn màn hình | Mã lỗi, mô tả, nút "Quay lại" | *hiển thị* | Các breakpoint tiêu chuẩn | Các nút có thể tập trung bằng bàn phím, thông báo ARIA | `--color-danger` | [REQ-003] |
| **Bảng điều khiển quản trị** | Quản trị viên | Đầu trang, thanh bên, vùng nội dung chính | Thẻ thống kê, bảng người dùng, bảng lịch, bộ lọc nhật ký | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Điều hướng bằng bàn phím cho bảng, thông báo ARIA | `--bg-primary` | [REQ-001] |
| **Danh sách người dùng** | Quản trị viên | Vùng nội dung chính | Bảng người dùng, thanh công cụ | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Điều hướng bảng bằng bàn phím | `--radius-md` | [REQ-001] |
| **Quản lý nền tảng** | Quản trị viên | Vùng nội dung chính | Danh sách nền tảng, form thêm/sửa | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Các trường nhập liệu hỗ trợ nhập liệu bằng bàn phím | `--color-primary` | [ARC-001] |
| **Nhật ký hệ thống** | Quản trị viên | Vùng nội dung chính | Dòng thời gian, bộ lọc, nút xuất | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Điều hướng bằng bàn phím cho danh sách, thông báo ARIA | `--bg-secondary` | [EXC-001] |
| **Theo dõi hiệu suất** | Quản trị viên | Vùng nội dung chính | Biểu đồ, bảng, bộ lọc | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Biểu đồ hỗ trợ chú thích bằng văn bản, thông báo ARIA | `--color-primary` | [DAT-002] |
| **Theo dõi tốc độ** | Quản trị viên | Vùng nội dung chính | Biểu đồ, bảng, bộ lọc | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Biểu đồ hỗ trợ chú thích bằng văn bản | `--color-warning` | [NFR-001] |
| **Cấu hình xác thực** | Quản trị viên | Vùng nội dung chính | Danh sách quy tắc, form thêm/sửa | *đang tải*, *rỗng*, *có dữ liệu* | Các breakpoint tiêu chuẩn | Các trường nhập liệu hỗ trợ nhập liệu bằng bàn phím | `--color-danger` | [REQ-003] |

**Lưu ý về khả năng tiếp cận (chung):**
- Tất cả các nút và liên kết đều có thể tập trung bằng bàn phím (vòng tập trung rõ ràng).
- Các trường nhập liệu có nhãn được liên kết (`for`/`id`) và thông báo lỗi được liên kết (`aria-describedby`).
- Các trạng thái động (ví dụ: *đang tải*, *lỗi*) được thông báo cho người dùng phụ thuộc vào công nghệ hỗ trợ thông qua `aria-live` vùng.
- Màu nền và văn bản tuân thủ tỷ lệ tương phản tối thiểu 4.5:1 (được đảm bảo bởi các token `--color-primary`/`--color-danger` được xác định).
- Các trình chọn ngày/giờ hỗ trợ điều hướng bằng bàn phím và có nhãn rõ ràng.

**Lưu ý về khả năng phản hồi:**
- Bố cục sử dụng `--breakpoint-sm` (≤600px), `--breakpoint-md` (601‑900px), `--breakpoint-lg` (≥901px).
- Các bảng có thể cuộn ngang trên thiết bị di động; các thẻ nội dung có thể thu gọn.
- Các form chuyển sang chế độ xem theo chiều dọc trên thiết bị có kích thước dưới `--breakpoint-sm`.

**Lý do thiết kế UX:**
- Các bảng điều khiển tập trung vào hành động chính (tạo lịch mới, kết nối nền tảng) để hỗ trợ người dùng doanh nghiệp nhỏ.
- Các thông báo lỗi và xác thực được hiển thị ngay lập tức gần trường nhập liệu tương ứng để giảm sự bối rối.
- Các cửa sổ bật lên xác nhận được sử dụng cho các hành động nguy hiểm (xóa, lên lịch bài đăng có điểm dự đoán thấp) để ngăn chặn thao tác nhầm.
- Các thông báo dựa trên ARIA và các nút có thể tập trung bằng bàn phím đảm bảo khả năng sử dụng cho người dùng phụ thuộc vào bàn phím.
- Các chế độ xem dành cho quản trị viên được thiết kế để cho phép giám sát và khắc phục sự cố nhanh chóng, với các bộ lọc và liên kết rõ ràng.

**Bản đồ truy xuất nguồn:**
- Tất cả các màn hình chính đều được tham chiếu bởi các thẻ yêu cầu chức năng (`[REQ-001]`, `[REQ-002]`, `[REQ-003]`, `[ARC-001]`, `[NFR-001]`, `[EXC-001]`, `[EXC-002]`, `[EXC-003]`, `[EXC-004]`).
- Các thực thể dữ liệu (`[DAT-001]`, `[DAT-002]`) được tham chiếu trong các màn hình liên quan đến lịch và hiệu suất.
- Các quy tắc xác thực và xử lý lỗi được tham chiếu bởi các thẻ ngoại lệ tương ứng.

### Lưu ý về khả năng sẵn sàng UI/UX

- **Module 1 (Lịch đăng bài đa nền tảng):** Các form lên lịch và xử lý lỗi được xác định đầy đủ; các giới hạn tốc độ và bảo vệ chống spam được xác định; giao diện người dùng OAuth được xác định.
- **Module 2 (Đề xuất AI):** Các thành phần giao diện người dùng cho các đề xuất và điểm dự đoán được xác định; cảnh báo hiệu suất thấp được tích hợp; xử lý lỗi mô hình được xác định.
- **Module 3 (Xác thực & Tốc độ):** Các thông báo xác thực và giới hạn tốc độ được xác định; các trang xác thực lỗi được xác định; các chế độ xem dành cho quản trị viên để giám sát tốc độ được xác định.
- **RBAC & Quản trị:** Các màn hình quản trị được xác định để đáp ứng các quyền hạn của quản trị viên; các màn hình này được tham chiếu bởi các yêu cầu chức năng và thực thể dữ liệu.
- **Khả năng tiếp cận & Phản hồi:** Các cân nhắc về khả năng tiếp cận và phản hồi được ghi lại cho từng màn hình; các token thiết kế được xác định.
- **Khoảng trống:** Các thiết kế chi tiết cho màn hình "Phân tích cảm xúc nâng cao", "Lập lịch tự động theo mùa", "Tích hợp đa kênh nâng cao" không được xác định trong SRS; những màn hình này được coi là các khoảng trống sẵn sàng UI/UX.

**Tất cả các tiêu đề, nhãn, mô tả và văn bản hướng dẫn trong tài liệu này đều được viết bằng tiếng Việt để phù hợp với ngôn ngữ mục tiêu được chỉ định.**