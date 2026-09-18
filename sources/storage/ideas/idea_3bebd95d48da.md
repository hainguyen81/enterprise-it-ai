# SolarSense Pro

- **Lĩnh vực:** Giám sát và tối ưu hóa sản lượng pin mặt trời cho hộ gia đình
- **Tên kỹ thuật:** SolarSensePro
- **Tên thương mại:** SunTrack
- **Vấn đề:** Chủ nhà có hệ thống pin mặt trời khó theo dõi sản lượng, phát hiện sự cố và tối ưu hóa thời điểm sử dụng điện.
- **Giải pháp & Quy trình:** SolarSense Pro kết nối với bộ điều khiển inverter qua API, hiển thị biểu đồ công suất theo thời gian thực, cảnh báo sự cố và đề xuất lịch sử dụng điện tiết kiệm.
- **Đối tượng mục tiêu:** Chủ nhà có lắp đặt pin mặt trời, công ty quản lý bất động sản
- **Điểm khác biệt (USP):** Giám sát công suất pin mặt trời theo thời gian thực, cảnh báo sự cố và đề xuất sử dụng điện tiết kiệm, tất cả trong một giao diện đơn giản.

##### Hợp đồng yêu cầu triển khai MVP nhanh
* **[REQ-001]** Kết nối với inverter solar qua API để thu thập dữ liệu công suất.
* **[REQ-002]** Hiển thị biểu đồ công suất theo ngày/giờ và cảnh báo khi công suất thấp.
* **[DAT-001]** Lưu trữ dữ liệu công suất và lịch sử trong cơ sở dữ liệu thời gian thực.
* **[EXC-001]** Xử lý khi mất kết nối thiết bị, lưu dữ liệu đệm và đồng bộ khi trực tuyến trở lại.