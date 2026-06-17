# PROMPT KỸ THUẬT TỔNG THỂ: HỆ THỐNG SAAS CHATBOT BÁN HÀNG ĐA KÊNH (TÍCH HỢP CLAUDE AI)

> Tài liệu này được viết ở dạng prompt kỹ thuật chi tiết, dùng để đưa trực tiếp cho dev hoặc AI code (Claude Code, Cursor, v.v...) làm căn cứ xây dựng toàn bộ hệ thống. Mô hình: **SaaS multi-tenant** — một hệ thống duy nhất, nhiều doanh nghiệp (tenant) cùng sử dụng, mỗi tenant có dữ liệu tách biệt hoàn toàn.

---

## 0. BỐI CẢNH & MỤC TIÊU HỆ THỐNG

Xây dựng một nền tảng SaaS cho phép bất kỳ doanh nghiệp nào (gọi là "tenant") đăng ký, kết nối các kênh chat của họ (Facebook Messenger, Zalo OA, Instagram, Website Widget, TikTok Shop...), cấu hình một chatbot bán hàng tự động sử dụng Claude API làm bộ não xử lý ngôn ngữ tự nhiên, với khả năng:

- Trả lời tự động mọi tin nhắn đến từ mọi kênh, không bỏ sót tin nhắn nào dù ngắn nhất (ví dụ một dấu chấm hỏi).
- Tự thu thập thông tin và tạo đơn hàng ngay trong hội thoại, không cần khách điền form.
- Tự động chuyển giao (escalate) cho nhân viên thật khi gặp tình huống ngoài khả năng xử lý.
- Vận hành ở quy mô lớn (hàng nghìn đơn hàng/tháng) với hiệu năng ổn định, chi phí gọi AI được kiểm soát.
- Cho phép Anthropic/chủ hệ thống (Super Admin) quản lý nhiều tenant, thu phí theo gói (subscription billing), theo dõi sức khỏe hệ thống.
- Hỗ trợ mô hình đối tác/affiliate giới thiệu khách hàng mới.

Ngăn xếp công nghệ giả định: Frontend Next.js/React, Backend Node.js, Database PostgreSQL (multi-tenant qua `tenant_id`), Claude API cho xử lý hội thoại, Queue (Redis/BullMQ) cho xử lý webhook bất đồng bộ, lưu file qua S3-compatible storage.

---

## 1. KIẾN TRÚC MULTI-TENANT (NỀN TẢNG CHO TOÀN BỘ HỆ THỐNG)

Mọi bảng dữ liệu nghiệp vụ (đơn hàng, khách hàng, hội thoại, sản phẩm...) phải có cột `tenant_id` để tách dữ liệu giữa các doanh nghiệp. Mọi API endpoint phải kiểm tra `tenant_id` của người dùng đang đăng nhập trước khi truy vấn, tuyệt đối không cho phép truy cập chéo dữ liệu giữa các tenant. Mỗi tenant có một subdomain riêng hoặc custom domain (ví dụ `shopA.tenplatform.com` hoặc domain riêng của khách hàng nếu dùng gói white-label).

---

## 2. DANH SÁCH ĐẦY ĐỦ CÁC TRANG/MODULE (SITEMAP CHI TIẾT)

### NHÓM A — Xác thực, Tài khoản & Onboarding

| Trang                            | Mô tả chức năng                                                                                                                                                                                                        | Vai trò truy cập          |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Trang chủ/Landing page           | Giới thiệu sản phẩm SaaS siêu hay, đọc là muốn mua ngay sở hữu ngay công cụ tuyệt vời này, bảng giá gói chính sách siue6 thông minh có gói miễn phí sử dụng btrai3 nghiệm full chức năng, CTA đăng ký đẹp mắt đẳng cấp | Public                    |
| Đăng ký tài khoản                | Form đăng ký tenant mới, xác thực email/SĐT                                                                                                                                                                            | Public                    |
| Đăng nhập                        | Đăng nhập bằng email, gmail 1 chạm, hỗ trợ SSO (Google)                                                                                                                                                                | Public                    |
| Onboarding wizard                | Hướng dẫn từng bước sau đăng ký: tạo doanh nghiệp, kết nối kênh đầu tiên, nhập sản phẩm đầu tiên, test bot                                                                                                             | Tenant Admin mới          |
| Chuyển đổi Workspace             | Cho phép 1 tài khoản quản lý nhiều doanh nghiệp/tenant, chuyển qua lại                                                                                                                                                 | User quản lý nhiều tenant |
| Trang chấp nhận lời mời (Invite) | Nhân viên nhận email mời vào team, tạo mật khẩu lần đầu                                                                                                                                                                | Người được mời            |

### NHÓM B — Dashboard Tổng quan

| Trang                    | Mô tả chức năng                                                                                                          | Vai trò truy cập                                                                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dashboard chính          | Số liệu real-time: hội thoại hôm nay, doanh số qua bot, tỷ lệ chuyển đổi, đơn đang chờ xử lý, cảnh báo escalate tồn đọng | Tenant Admin, Manager                                                                                                                                                   |
| Dashboard theo nhân viên | Mỗi nhân viên xem hiệu suất cá nhân: số hội thoại đã xử lý, thời gian phản hồi trung bình                                | Agent (nhân viên CSKH) báo cáo kết quả chi tiết tỷ lệ chốt thành công, chưa thành công, đang xử lý, chờ phàn hồi, bị từ chối, khách chưa trả lời, follow up, upscale... |

### NHÓM C — Hội thoại & Vận hành Chatbot (Lõi hệ thống)

| Trang                                       | Mô tả chức năng                                                                                                             | Vai trò truy cập      |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------- |
| Inbox hội thoại đa kênh                     | Danh sách tất cả hội thoại từ mọi kênh trong 1 màn hình, lọc theo kênh/trạng thái/nhân viên phụ trách                       | Admin, Manager, Agent |
| Chi tiết hội thoại                          | Khung chat trực tiếp, lịch sử đầy đủ, thông tin khách hàng bên cạnh, nút chuyển Bot ⇄ Người, nút gắn tag                    | Admin, Manager, Agent |
| Trình xây kịch bản Bot (Flow Builder)       | Kéo-thả hoặc cấu hình luồng hội thoại, nhánh điều kiện, các bước thu thập thông tin đơn hàng                                | Admin, Manager        |
| Cấu hình System Prompt / Personality Bot    | Soạn tính cách bot, giọng văn, phạm vi trả lời, thông tin doanh nghiệp đưa vào ngữ cảnh Claude                              | Admin, Manager        |
| Quản lý Knowledge Base / FAQ                | Kho câu hỏi-trả lời, tài liệu sản phẩm, chính sách bot dùng để trả lời chính xác (RAG)                                      | Admin, Manager        |
| Cấu hình từ khóa & quy tắc Escalate         | Danh sách từ khóa, ngưỡng giá trị đơn, số lần lặp câu hỏi khiến bot tự chuyển người                                         | Admin, Manager        |
| Test/Preview Bot (Sandbox)                  | Khung chat thử nghiệm bot trước khi áp dụng vào kênh thật                                                                   | Admin, Manager        |
| A/B Testing kịch bản                        | So sánh hiệu quả 2 phiên bản system prompt/câu trả lời khác nhau theo tỷ lệ chuyển đổi                                      | Admin, Manager        |
| Quản lý mẫu câu trả lời nhanh (Quick Reply) | Soạn sẵn các câu trả lời nhân viên dùng nhanh khi tiếp nhận hội thoại                                                       | Admin, Manager, Agent |
| Quản lý Broadcast/Chiến dịch nhắn tin       | Gửi tin nhắn hàng loạt (remarketing, thông báo khuyến mãi) tới danh sách khách theo kênh, tuân thủ chính sách từng platform | Admin, Manager        |
| Trang Lịch sử Webhook/Log tin nhắn lỗi      | Theo dõi tin nhắn gửi/nhận thất bại, lỗi kết nối kênh để xử lý kỹ thuật                                                     | Admin, Dev            | gửi tin nhắn hàng loạt tự động, người đã đăng ký kênh, kết bạn, comments, nhắn tin riêng... |

### NHÓM D — Quản lý Kênh kết nối

| Trang                         | Mô tả chức năng                                                    | Vai trò truy cập |
| ----------------------------- | ------------------------------------------------------------------ | ---------------- |
| Trang Kết nối kênh            | Liên kết Facebook Page, Zalo OA, Instagram, TikTok Shop qua OAuth  | Admin            |
| Cài đặt riêng từng kênh       | Giờ hoạt động, tin nhắn chào mừng, người phụ trách riêng theo kênh | Admin, Manager   |
| Quản lý Website Chat Widget   | Tùy chỉnh giao diện, vị trí, màu sắc, lấy mã nhúng (embed code)    | Admin, Manager   |
| Trạng thái kết nối & cảnh báo | Hiển thị kênh nào bị mất kết nối/token hết hạn cần làm mới         | Admin            |

### NHÓM E — Sản phẩm & Bán hàng

| Trang                          | Mô tả chức năng                                                                                             | Vai trò truy cập      |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------- | --------------------- |
| Quản lý sản phẩm/dịch vụ       | Thêm/sửa/xóa, giá, hình ảnh, video, phản hồi của khách hàng, biến thể (size/màu), mô tả dùng cho bot tư vấn | Admin, Manager        |
| Quản lý danh mục sản phẩm      | Phân loại nhóm sản phẩm                                                                                     | Admin, Manager        |
| Quản lý tồn kho                | Cập nhật số lượng, đồng bộ real-time để bot không chốt đơn hàng hết kho                                     | Admin, Manager        |
| Quản lý đơn hàng               | Danh sách đơn, lọc theo kênh/trạng thái/nhân viên, xuất Excel                                               | Admin, Manager, Agent |
| Chi tiết đơn hàng              | Thông tin khách, sản phẩm, lịch sử thay đổi trạng thái, ghi chú nội bộ                                      | Admin, Manager, Agent |
| Quản lý mã giảm giá/khuyến mãi | Tạo mã, điều kiện áp dụng, thời hạn                                                                         | Admin, Manager        |
| Cài đặt thanh toán             | Kết nối cổng thanh toán (VNPay, Momo, visa, paypal, chuyển khoản), cấu hình COD                             | Admin                 |
| Cài đặt vận chuyển             | Cấu hình đơn vị vận chuyển, phí ship theo khu vực                                                           | Admin                 |

### NHÓM F — CRM & Khách hàng

| Trang                              | Mô tả chức năng                                                                                             | Vai trò truy cập      |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------- |
| Danh sách khách hàng               | Hợp nhất khách từ mọi kênh, tìm kiếm, lọc theo tag                                                          | Admin, Manager, Agent |
| Chi tiết khách hàng                | Lịch sử thời gian mua hàng, lịch sử thời gian chat toàn bộ kênh, ghi chú nội bộ, giá trị đơn trọn đời (LTV) | Admin, Manager, Agent |
| Quản lý Tag & Phân khúc khách hàng | Gắn nhãn khách (VIP, khách mới, khách bỏ giỡ...)                                                            | Admin, Manager        |
| Chăm sóc khách hàng tự động        | Cấu hình kịch bản nhắc nhở hội thoại bỏ giỡ (cart/conversation abandonment), nhắc tái mua                   | Admin, Manager        |

### NHÓM G — Quản lý Nội dung

| Trang                              | Mô tả chức năng                                          | Vai trò truy cập |
| ---------------------------------- | -------------------------------------------------------- | ---------------- |
| Quản lý bài viết/Blog              | Soạn nội dung marketing, SEO                             | Admin, Manager   |
| Quản lý banner/Khuyến mãi hiển thị | Banner trên web/widget chat                              | Admin, Manager   |
| Thư viện Media                     | Lưu trữ ảnh/video dùng chung cho bot, bài viết, sản phẩm | Admin, Manager   |

### NHÓM H — Quản lý Team & Phân quyền

| Trang                                               | Mô tả chức năng                                                                                                                                          | Vai trò truy cập |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Quản lý thành viên Team                             | Thêm/xóa nhân viên, gửi lời mời                                                                                                                          | Admin            |
| Phân quyền theo vai trò (Role-Based Access Control) | Định nghĩa quyền hạn: Admin (toàn quyền), Manager (quản lý vận hành, không đổi billing), Agent (chỉ xử lý hội thoại được giao), Viewer (chỉ xem báo cáo) | Admin            |
| Phân công hội thoại                                 | Chia hội thoại tự động hoặc thủ công cho nhân viên/nhóm                                                                                                  | Admin, Manager   |
| Theo dõi hiệu suất nhân viên                        | Số hội thoại xử lý, thời gian phản hồi, đánh giá khách hàng (CSAT)                                                                                       | Admin, Manager   |

### NHÓM I — Cài đặt Doanh nghiệp (Tenant Settings)

| Trang                                    | Mô tả chức năng                                                                                                            | Vai trò truy cập |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Thông tin doanh nghiệp                   | Tên, logo, địa chỉ, số điện thoại, hình ảnh, video, tài liệu daonh nghiệp, tất cả các file tải lên, mã số thuế, ngành hàng | Admin            |
| Cài đặt chung                            | Múi giờ, ngôn ngữ hiển thị, đơn vị tiền tệ                                                                                 | Admin            |
| Quản lý gói dịch vụ & Billing            | Xem gói hiện tại, giới hạn sử dụng (số hội thoại/tháng, số kênh), nâng/hạ cấp gói                                          | Admin            |
| Lịch sử thanh toán & Hóa đơn             | Xem và xuất hóa đơn các kỳ thanh toán                                                                                      | Admin            |
| Quản lý API Key & Tích hợp bên thứ ba    | Tạo API key riêng cho tenant, kết nối CRM/ERP/Email Marketing ngoài                                                        | Admin            |
| Cài đặt giới hạn sử dụng Claude API      | Đặt ngưỡng chi phí/số lượng request gọi AI mỗi ngày để tránh phát sinh chi phí bất ngờ                                     | Admin            |
| Cài đặt bảo mật & quyền riêng tư dữ liệu | Chính sách lưu trữ dữ liệu khách hàng, xuất/xóa dữ liệu theo yêu cầu                                                       | Admin            |

### NHÓM J — Super Admin (Quản trị toàn hệ thống — dành cho chủ platform)

| Trang                                     | Mô tả chức năng                                                                                          | Vai trò truy cập                                                                             |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Quản lý tất cả Tenant                     | Danh sách toàn bộ doanh nghiệp đang dùng hệ thống, trạng thái hoạt động, khóa/mở tài khoản               | Super Admin                                                                                  |
| Chi tiết Tenant                           | Xem cấu hình, mức sử dụng, lịch sử thanh toán của từng tenant                                            | Super Admin                                                                                  |
| Quản lý setup các Gói & Bảng giá Platform | Tạo/sửa các gói dịch vụ bán cho tenant (Free, Basic, Pro, Enterprise)                                    | Super Admin                                                                                  |
| Quản lý Đối tác/Affiliate                 | Danh sách đối tác giới thiệu khách, theo dõi hoa hồng, lịch sử giới thiệu                                | Super Admin                                                                                  |
| Hồ sơ Đối tác                             | Thông tin đối tác, hợp đồng, setup các chính sách gói hoa hồng đang áp dụng, link giới thiệu riêng       | Super Admin, Đối tác (xem giới hạn) chính sách setup riêng cho thành viên vip được cấp riêng |
| Giám sát hệ thống & Chi phí AI            | Theo dõi uptime, lỗi API theo từng tenant, tổng chi phí gọi Claude API toàn hệ thống và theo từng tenant | Super Admin                                                                                  |
| Cấu hình White-label                      | Cho phép đối tác/tenant lớn gắn thương hiệu riêng (logo, domain riêng) lên hệ thống                      | Super Admin                                                                                  |
| Quản lý thông báo hệ thống                | Gửi thông báo bảo trì, cập nhật tính năng tới toàn bộ tenant                                             | Super Admin                                                                                  |

### NHÓM K — Báo cáo & Phân tích

| Trang                 | Mô tả chức năng                                                          | Vai trò truy cập |
| --------------------- | ------------------------------------------------------------------------ | ---------------- |
| Báo cáo doanh số      | Theo thời gian, kênh, sản phẩm, nhân viên                                | Admin, Manager   |
| Báo cáo hiệu suất Bot | Câu hỏi bot không trả lời được, tỷ lệ escalate, tỷ lệ chuyển đổi qua bot | Admin, Manager   |
| Báo cáo khách hàng    | Khách mới/quay lại, giá trị đơn trung bình, phân khúc                    | Admin, Manager   |
| Xuất báo cáo          | Xuất Excel/PDF theo khoảng thời gian tùy chọn                            | Admin, Manager   |

### NHÓM L — Hỗ trợ, Tài liệu & An toàn hệ thống

| Trang                                   | Mô tả chức năng                                                     | Vai trò truy cập   |
| --------------------------------------- | ------------------------------------------------------------------- | ------------------ |
| Trung tâm trợ giúp                      | Tài liệu hướng dẫn sử dụng, video, FAQ hệ thống                     | Mọi user           |
| Liên hệ hỗ trợ kỹ thuật                 | Gửi ticket hỗ trợ tới team platform                                 | Mọi user           |
| Nhật ký hoạt động (Audit Log)           | Ghi lại ai thao tác gì, khi nào — phục vụ truy vết sự cố và bảo mật | Admin, Super Admin |
| Trang trạng thái hệ thống (Status Page) | Hiển thị tình trạng hoạt động các dịch vụ (uptime công khai)        | Public             |

---

## 3. PHÂN QUYỀN CHI TIẾT (ROLE MATRIX)

| Vai trò           | Phạm vi quyền                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| Super Admin       | Toàn quyền trên mọi tenant, billing platform, cấu hình hệ thống                                |
| Tenant Admin      | Toàn quyền trong phạm vi tenant của mình: billing, phân quyền, kết nối kênh, cấu hình bot      |
| Manager           | Quản lý vận hành: sản phẩm, đơn hàng, hội thoại, nhân viên — không có quyền billing/xóa tenant |
| Agent             | Chỉ xử lý hội thoại/đơn hàng được phân công, không có quyền cấu hình hệ thống                  |
| Viewer            | Chỉ xem báo cáo, không thao tác chỉnh sửa                                                      |
| Đối tác/Affiliate | Chỉ xem hồ sơ giới thiệu, hoa hồng của chính mình                                              |

---

## 4. YÊU CẦU KỸ THUẬT BẮT BUỘC (NON-FUNCTIONAL REQUIREMENTS)

Hệ thống phải xử lý webhook bất đồng bộ qua hàng đợi (queue) để không bị nghẽn khi lượng tin nhắn tăng cao. Mọi tin nhắn đến — kể cả nội dung cực ngắn như một dấu chấm hỏi — phải được tiếp nhận và phản hồi trong thời gian hợp lý (mục tiêu dưới 5 giây cho phản hồi tự động). Hệ thống cần cơ chế gộp tin nhắn liên tiếp gửi dồn (message batching/debounce) trước khi gọi Claude API để tránh trả lời rời rạc và lãng phí chi phí gọi API. Cần giới hạn (rate limit) số lượng request gọi Claude API theo tenant để tránh một tenant dùng vượt mức ảnh hưởng tenant khác và tránh phát sinh chi phí ngoài kiểm soát. Cần cơ chế fallback (câu trả lời mặc định an toàn) khi Claude API lỗi hoặc timeout, không để khách hàng nhận im lặng. Toàn bộ dữ liệu nhạy cảm (thông tin thanh toán, số điện thoại khách) phải được mã hóa khi lưu trữ. Hệ thống cần được thiết kế để mở rộng theo chiều ngang (horizontal scaling) khi số tenant và lượng hội thoại tăng.

---

_Hết tài liệu._
