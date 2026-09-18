```json
{
  "technical_codename": "social-scheduler",
  "target_device": "Web_Desktop",
  "screens": [
    {
      "screen_id": "SCR_001_LOGIN",
      "screen_title": "Đăng nhập / Xác thực OAuth",
      "layout_structure": "Flexbox column với nội dung được căn giữa, toàn màn hình",
      "sections": [
        {
          "section_name": "Navigation_Bar",
          "visual_hierarchy_weight": 1 "Hiển thị thanh điều hướng",
          "elements": [
            {
              "element_id": "logo_img",
              "element_type": "Card",
              "label_en": "Company logo",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-001]",
                "data_tag": null
              },
              "ux_justification": "Hiển thị nhận diện thương hiệu ở đầu trang để người dùng xác định ứng dụng và xây dựng niềm tin."
            },
            {
              "element_id": "btn_login_oauth",
              "element_type": "Button",
              "label_en": "Login with OAuth",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-001]",
                "data_tag": null
              },
              "ux_justification": "Cung cấp một điểm tương tác duy nhất để bắt đầu luồng OAuth 2.0, tuân thủ [ARC-001] và giảm ma sát cho người dùng."
            },
            {
              "element_id": "error_message",
              "element_type": "Alert",
              "label_en": "Authentication error",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-001]",
                "data_tag": null
              },
              "ux_justification": "Thông báo cho người dùng về các vấn đề xác thực một cách rõ ràng, hỗ trợ khả năng tiếp cận và giúp người dùng nhanh chóng thực hiện các bước tiếp theo."
            }
          ]
        },
        {
          "section_name": "Main_Data_Table",
          "visual_hierarchy_weight": 3,
          "elements": [
            {
              "element_id": "oauth_redirect_status",
              "element_type": "Alert",
              "label_en": "Redirect status",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-001]",
                "data_tag": null
              },
              "ux_justification": "Thông báo cho người dùng về trạng thái của quá trình chuyển hướng đến nhà cung cấp OAuth, đảm bảo tính minh bạch trong quá trình xác thực."
            }
          ]
        }
      ]
    },
    {
      "screen_id": "SCR_002_DASHBOARD",
      "screen_title": "Bảng điều khiển người dùng",
      "layout_structure": "Flexbox row‑wrap với thanh bên (240px) và vùng nội dung chính",
      "sections": [
        {
          "section_name": "Navigation_Bar",
          "visual_hierarchy_weight": 1,
          "elements": [
            {
              "element_id": "nav_dashboard",
              "element_type": "Button",
              "label_en": "Dashboard",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-001]",
                "data_tag": null
              },
              "ux_justification": "Cung cấp điều hướng chính để người dùng truy cập nhanh vào bảng điều khiển chính."
            },
            {
              "element_id": "nav_schedule",
              "element_type": "Button",
              "label_en": "Lịch đăng bài",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-001]",
                "data_tag": null
              },
              "ux_justification": "Cho phép người dùng truy cập vào lịch đăng bài của họ."
            },
            {
              "element_id": "nav_content_suggestion",
              "element_type": "Button",
              "label_en": "Đề xuất nội dung",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-002]",
                "data_tag": null
              },
              "ux_justification": "Cung cấp quyền truy cập vào các đề xuất nội dung được hỗ trợ bởi AI."
            },
            {
              "element_id": "nav_platform_connections",
              "element_type": "Button",
              "label_en": "Kết nối nền tảng",
              "placeholder_or_value": null,
              "traceability": {
                "requirement_tag": "[REQ-001]",
                "data_tag": null
              },
              "ux_justification": "Cho phép người dùng quản lý các kết nối OAuth cho các nền tảng mạng xã hội."
            },
            {
              "element