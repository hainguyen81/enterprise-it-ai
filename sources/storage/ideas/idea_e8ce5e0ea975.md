# AR Wayfinder – Trợ lý Định hướng Thực tế Tăng cường cho Tòa nhà Công cộng

- **Domain:** Lĩnh vực: Spatial Computing
- **Technical Codename:** Tên kỹ thuật: ArWayfinder
- **Brand Name:** Tên thương mại: SpaceNavi
- **Problem Statement:** Vấn đề: Du khách và nhân viên trong các tòa nhà lớn như sân bay, trung tâm thương mại thường mất thời gian tìm đường do thiếu hướng dẫn trực quan, đặc biệt là người nước ngoài hoặc người khiếm thị.
- **Solution & Workflow:** Giải pháp & Quy trình: Sử dụng camera trên thiết bị di động và dữ liệu bản đồ tòa nhà để hiển thị chỉ dẫn điều hướng AR trên đường đi, hỗ trợ tìm đường theo thời gian thực.
- **Target Audience:** Đối tượng mục tiêu: Du khách, nhân viên, người khuyết tật thị giác, và các nhà quản lý cơ sở.
- **Unique Selling Proposition (USP):** Ưu điểm bán hàng (USP): Kết hợp bản đồ tòa nhà chính xác, chỉ dẫn AR theo thời gian thực và hỗ trợ ngoại ngữ, giúp điều hướng trong nhà trở nên trực quan và dễ tiếp cận.

##### Yêu cầu thực hiện MVP nhanh gọn
* [REQ-001] API lấy dữ liệu bản đồ tòa nhà từ tệp SVG/2D hoặc mô hình 3D.
* [REQ-002] Thuật toán tính toán đường đi tối ưu tránh các khu vực hạn chế.
* [DAT-001] Cơ sở dữ liệu lưu trữ lịch sử điều hướng của người dùng để đề xuất tuyến đường ưa thích.
* [EXC-001] Xử lý trường hợp mất kết nối mạng bằng cách cung cấp bản đồ ngoại tuyến và chỉ dẫn từng bước tĩnh.