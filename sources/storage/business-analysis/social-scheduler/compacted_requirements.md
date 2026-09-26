PROJECT
codename=social-scheduler

REQ
id=[REQ-001]
statement=Tích hợp API lịch đăng bài tự động cho Facebook, Instagram và TikTok.
actors=Người dùng cuối
behavior=Kết nối tài khoản mạng xã hội, tạo và lên lịch đăng bài tự động trên các nền tảng được hỗ trợ.
constraints=Phải hỗ trợ ít nhất ba nền tảng: Facebook, Instagram, TikTok.
derived=false

REQ
id=[REQ-002]
statement=Triển khai mô hình học máy để đề xuất nội dung bài đăng dựa trên hiệu suất trước đó.
actors=Người dùng cuối
behavior=Phân tích lịch sử tương tác để tạo đề xuất nội dung tối ưu cho từng nền tảng.
constraints=Đề xuất phải dựa trên dữ liệu hiệu suất thực tế và phù hợp với định dạng nội dung của mỗi nền tảng.
derived=false

REQ
id=[REQ-003]
statement=Thực hiện xác thực đầu vào dữ liệu và kiểm tra giới hạn tỷ lệ cho từng người dùng.
actors=Người dùng cuối
behavior=Xác thực độ dài nội dung, định dạng thời gian, và áp dụng giới hạn tốc度 API mỗi người dùng.
constraints=Giới hạn tỷ lệ phải có thể cấu hình và áp dụng riêng biệt cho mỗi người dùng và nền tảng.
derived=false

EXC
id=[EXC-001]
parent=[REQ-001]
statement=Xử lý ngoại lệ khi API bên thứ ba trả về lỗi; ghi lại và thử lại sau.
derived=false

EXC
id=[EXC-002]
parent=[REQ-001]
statement=Xác thực quyền truy cập người dùng và xử lý trường hợp token hết hạn.
derived=false

EXC
id=[EXC-003]
parent=[REQ-001]
statement=Bảo vệ chống lại việc spam lịch đăng bài và tấn công flood comment.
derived=false

DAT
id=[DAT-001]
entity=ScheduledPost
fields=id:int PK NOT NULL AUTO_INCREMENT; user_id:int NOT NULL; platform:varchar NOT NULL; content:text NOT NULL; scheduled_time:timestamp NOT NULL; status:varchar NOT NULL DEFAULT 'scheduled'
relationships=post_id->ScheduledPost.id (1:N)
constraints=platform IN ('facebook','instagram','tiktok'); status IN ('scheduled','published','failed','cancelled')

DAT
id=[DAT-002]
entity=PostPerformance
fields=id:int PK NOT NULL AUTO_INCREMENT; post_id:int NOT NULL FK; metric_likes:int NOT NULL DEFAULT 0; metric_comments:int NOT NULL DEFAULT 0; metric_shares:int NOT NULL DEFAULT 0; collected_at:timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
relationships=post_id->ScheduledPost.id (N:1)
constraints=metric_likes >= 0; metric_comments >= 0; metric_shares >= 0

DEP
from=[REQ-001]
to=[DAT-001]

DEP
from=[REQ-002]
to=[DAT-002]

DEP
from=[REQ-003]
to=[DAT-001]

TRACE
[REQ-001]=Module 1: Core Functional Requirements
[REQ-002]=Module 2: Core Functional Requirements
[REQ-003]=Module 1: Core Functional Requirements
[DAT-001]=Module 3: Data Specification
[DAT-002]=Module 3: Data Specification
[EXC-001]=Module 1: Exception Flows
[EXC-002]=Module 1: Exception Flows
[EXC-003]=Module 1: Exception Flows