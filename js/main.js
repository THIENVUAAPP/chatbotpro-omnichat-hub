// Shared Premium UI Logic for ChatbotPro Omnichat Business Hub
document.addEventListener('DOMContentLoaded', () => {
    initCommonStyles();
    initLanguageSelector();
    initLeadCaptureModal();
    initToastSystem();
    initGlobalLinkHandlers();
    
    // Run translation on load
    translatePage();
});

// Translation dictionary for VIE/ENG
const translations = {
    VIE: {
        // Navigation Global
        "nav-features": "Tính Năng",
        "nav-pricing": "Bảng Giá",
        "nav-roi": "Tỷ Suất ROI",
        "nav-login": "ĐĂNG NHẬP ADMIN",
        "nav-status": "Trạng Thái Hệ Thống",
        "nav-health": "API Health",
        "nav-support": "Hỗ Trợ",
        "nav-home": "Trang Chủ",
        "nav-crm": "CRM Khách Hàng",
        "nav-api": "Cấu Hình API",
        "nav-guides": "Hướng Dẫn",
        "nav-settings": "Cài Đặt",
        "nav-admin-terminal": "Admin Terminal",
        "copyright": "© 2026 ChatbotPro. Trợ lý Trí Tuệ Nhân Tạo Doanh Nghiệp.",

        // Landing Page: Hero Section
        "hero-badge": "v4.0 Core Nhân Viên Số Hoạt Động",
        "hero-title": "Tự Động Hóa Tư Vấn.<br/><span class=\"luxury-gradient\">Trợ Lý AI Đa Kênh.</span>",
        "hero-desc": "Đừng để khách hàng chờ. AI phản hồi trong 5 giây, hoạt động 24/7. Trợ lý AI giảm tới 80% khối lượng tư vấn lặp lại, chốt đơn tự động theo dữ liệu riêng của bạn.",
        "hero-acquire": "ĐĂNG KÝ SỬ DỤNG NGAY",
        "hero-demo": "ĐẶT LỊCH DEMO 1-1",
        "trust-title": "ĐƯỢC TIN DÙNG BỞI CÁC TỔ CHỨC ĐẦU NGÀNH",

        // Landing Page: Architectural Flow (Steps)
        "steps-title": "Quy Trình Triển Khai",
        "steps-sub": "Chỉ từ 15 phút để đưa nhân viên số vào vận hành thực tế.",
        "step-1-title": "1. Thu Thập Tri Thức",
        "step-1-desc": "AI tự động học từ tài liệu PDF, DOCX, XLSX hoặc link website của doanh nghiệp.",
        "step-2-title": "2. Huấn Luyện & Test",
        "step-2-desc": "Tinh chỉnh kịch bản bán hàng, giọng điệu phản hồi và sản phẩm của doanh nghiệp.",
        "step-3-title": "3. Chạy Đa Kênh",
        "step-3-desc": "Tự động tư vấn chốt đơn 24/7 trên Zalo, Messenger, WhatsApp, Instagram.",

        // Landing Page: Bento Grid & Features
        "bento-title": "Nền Tảng Đa Kênh Tiên Tiến",
        "bento-sub": "Tích Hợp Không Giới Hạn. Kết Nối Mọi Nơi.",
        "api-title": "Đồng Bộ Hệ Thống",
        "api-desc": "Đồng bộ Zalo OA, Fanpage, Instagram, WhatsApp, Website Chatbot và tự động phản hồi bình luận quảng cáo.",
        "lexicon-title": "Trí Tuệ Đa Ngôn Ngữ",
        "lexicon-desc": "Tự động nhận diện ngôn ngữ của khách hàng và trả lời thông minh chuẩn bối cảnh.",

        // Landing Page: Channels
        "channels-title": "Ứng Dụng Trong Các Lĩnh Vực",
        "channels-sub": "Thiết kế kịch bản chuyên biệt cho từng phòng ban và ngành nghề.",
        "chan-sales": "Tư Vấn Bán Hàng",
        "chan-sales-desc": "Chăm sóc, tư vấn chốt đơn và tự động báo đơn mới.",
        "chan-admission": "Tư Vấn Tuyển Sinh",
        "chan-admission-desc": "Thu thập thông tin học viên và chuyển tiếp Lead tự động.",
        "chan-support": "Hỗ Trợ Kỹ Thuật",
        "chan-support-desc": "Giải đáp thắc mắc FAQ và hướng dẫn sử dụng phần mềm.",
        "chan-more": "Xem 27 Ngành Khác",
        "chan-more-desc": "Tùy biến linh hoạt theo yêu cầu",

        // Landing Page: ROI Calculator
        "roi-title": "Tỷ Suất ROI Thực Tế",
        "roi-sub": "Tính toán mức chi phí tiết kiệm được khi đưa trợ lý AI vào hoạt động.",
        "roi-label-tickets": "Số Tin Nhắn / Tháng",
        "roi-label-cost": "Chi Phí Trung Bình / Tin",
        "roi-label-deflection": "Tỷ Lệ AI Trả Lời Thành Công",
        "roi-savings-title": "CHI PHÍ TIẾT KIỆM HÀNG THÁNG",
        "roi-annual-savings": "Tỷ Suất ROI Hàng Năm",

        // Landing Page: Pricing
        "pricing-title": "Gói Dịch Vụ Hợp Lý",
        "pricing-sub": "Chi phí trọn gói, hỗ trợ trọn đời, thanh toán hàng năm.",
        "price-starter-sub": "Phù hợp chủ shop, cá nhân kinh doanh.",
        "price-starter-f1": "5.000 tin trả lời / tháng",
        "price-starter-f2": "Tối đa 1 trợ lý AI",
        "price-starter-f3": "Đầy đủ tính năng cốt lõi",
        "price-starter-btn": "MUA GÓI STARTER",
        "price-pro-sub": "Phù hợp cho doanh nghiệp nhỏ.",
        "price-pro-f1": "10.000 tin trả lời / tháng",
        "price-pro-f2": "Tối đa 2 trợ lý AI",
        "price-pro-f3": "Đầy đủ tính năng & Tùy biến",
        "price-pro-f4": "Hỗ trợ Zalo OA, Fanpage",
        "price-pro-btn": "MUA GÓI STANDARD",
        "price-elite-sub": "Doanh nghiệp vừa và lớn.",
        "price-elite-f1": "25.000 tin trả lời / tháng",
        "price-elite-f2": "Tối đa 5 trợ lý AI",
        "price-elite-f3": "White-label (Thông tin, Logo riêng)",
        "price-elite-f4": "Tích hợp API hệ thống",
        "price-elite-btn": "MUA GÓI EDITION",

        // Landing Page: FAQs
        "faq-title": "Câu Hỏi Thường Gặp",
        "faq-sub": "Giải đáp thắc mắc về triển khai trợ lý ảo AI.",
        "faq-q1": "Dữ liệu của doanh nghiệp có được bảo mật không?",
        "faq-a1": "Tuyệt đối bảo mật. Dữ liệu tri thức huấn luyện của bạn được mã hóa, lưu trữ cô lập và không bao giờ chia sẻ ra ngoài.",
        "faq-q2": "Thời gian triển khai mất bao lâu?",
        "faq-a2": "Hệ thống cực kỳ linh hoạt. Bạn có thể import dữ liệu PDF/DOCX/Website và kiểm thử chatbot AI chỉ trong 15 phút.",
        "faq-q3": "AI có bị ảo giác và trả lời sai thông tin không?",
        "faq-a3": "Không. Nhờ kiến trúc 'Enforcement Engineering', AI của chúng tôi bắt buộc chỉ trích xuất câu trả lời dựa trên tệp tri thức chuẩn đã duyệt, tránh ảo giác 100%.",

        // Landing Page: Urgency Sale
        "urgency-badge": "ƯU ĐÃI: TẶNG HƯỚNG DẪN 1-1 KHI ĐĂNG KÝ HÔM NAY",
        "urgency-title": "Bắt Đầu Số Hóa Doanh Nghiệp",
        "urgency-desc": "Đưa nhân viên số AI vào vận hành ngay để tối ưu hóa 80% thời gian trực chat, phản hồi khách hàng trong 5 giây 24/7.",
        "urgency-btn": "TRIỂN KHAI AI CHATBOT NGAY",

        // Checkout Page
        "checkout-title": "Phương Thức Thanh Toán",
        "checkout-desc": "Mọi giao dịch đều được mã hóa bảo mật 256-bit SSL.",
        "checkout-method-card": "THẺ QUỐC TẾ",
        "checkout-method-wallet": "VÍ ĐIỆN TỬ",
        "checkout-method-apple": "MOMO / ZALOPAY",
        "checkout-label-number": "SỐ THẺ",
        "checkout-label-expiry": "NGÀY HẾT HẠN",
        "checkout-label-name": "TÊN TRÊN THẺ",
        "checkout-billing-title": "Thông Tin Hóa Đơn",
        "checkout-label-address": "ĐỊA CHỈ",
        "checkout-label-city": "THÀNH PHỐ",
        "checkout-label-zip": "MÃ BƯU CHÍNH",
        "checkout-summary-title": "Thông Tin Gói Đăng Ký",
        "checkout-subtotal": "Tạm tính",
        "checkout-tax": "Thuế (10% VAT gồm trong giá)",
        "checkout-btn-pay": "THANH TOÁN NGAY",
        "checkout-secure": "Thanh toán bảo mật chuẩn quốc tế",

        // Dashboard & CRM
        "dash-title": "Bảng Điều Khiển CRM",
        "dash-sub": "Giám sát hiệu suất nhân viên số và dữ liệu khách hàng.",
        "dash-card-revenue": "Doanh Thu AI",
        "dash-card-chats": "Hội Thoại Hoàn Tất",
        "dash-card-deflection": "Tỷ Lệ Tự Động Hóa",
        "dash-card-satisfaction": "Mức Độ Hài Lòng",
        "dash-roster-title": "Danh Sách Khách Hàng",
        "dash-roster-sub": "Tự động đồng bộ từ Messenger, Zalo OA và Zalo cá nhân.",
        "dash-search-placeholder": "Tìm kiếm khách hàng, kênh kết nối...",
        "dash-col-name": "KHÁCH HÀNG",
        "dash-col-channel": "KÊNH",
        "dash-col-status": "TRẠNG THÁI",
        "dash-col-date": "NGÀY TƯ VẤN",
        "dash-col-action": "THAO TÁC",
        "dash-status-auto": "Tự động hóa",
        "dash-status-manual": "Cần nhân sự trực",

        // Environment Variables (Cấu hình API)
        "env-title": "Quản Lý Biến Môi Trường API",
        "dash-env-sub": "Cấu hình API Keys kết nối LLM, Zalo OA, Messenger và các webhook.",
        "env-btn-add": "Thêm Biến Môi Trường",
        "env-col-key": "TÊN BIẾN (KEY)",
        "env-col-value": "GIÁ TRỊ (VALUE)",
        "env-col-desc": "MÔ TẢ KẾT NỐI",
        "env-col-action": "HÀNH ĐỘNG",
        "env-btn-reveal": "Hiện",
        "env-btn-hide": "Ẩn",
        "env-btn-delete": "Xóa",
        "env-btn-audit": "Xem Nhật Ký",
        "env-btn-deploy": "Áp Dụng Thay Đổi",
        "env-card-infra": "Khóa Hạ Tầng Core",
        "env-card-params": "Tham Số Hệ Thống",
        "env-label-model": "Mô Hình Mặc Định",
        "env-label-tokens": "Số Token Tối Đa",
        "env-label-temp": "Độ Sáng Tạo (Temperature)",
        "env-label-cache": "Bật Bộ Nhớ Đệm Vector",
        "env-card-connections": "Kết Nối Hoạt Động",
        "env-card-details": "Chi Tiết Môi Trường",
        "env-detail-env": "Môi trường hiện tại:",
        "env-detail-region": "Khu vực:",
        "env-detail-updated": "Cập nhật lần cuối:",
        "env-detail-hash": "Mã phiên bản:",
        "env-placeholder-key": "TÊN_BIẾN_MỚI",
        "env-placeholder-value": "Giá trị...",
        
        // Guides Page
        "guides-title": "Trung Tâm Hướng Dẫn Sử Dụng",
        "dash-guides-sub": "Tài liệu hướng dẫn cấu hình AI, Zalo OA và tối ưu tri thức.",
        "guide-doc-title": "Cẩm Nang Triển Khai Trợ Lý AI",
        "guide-section-1": "1. Hướng dẫn nạp tri thức (Knowledge Ingestion)",
        "guide-section-1-desc": "AI Chatbot có thể tự học từ các file .pdf, .docx, .xlsx hoặc website URL. Bạn chỉ cần tải tệp lên trong mục quản lý tri thức, hệ thống sẽ tự động phân tách và xử lý bối cảnh trong 1-2 phút.",
        "guide-section-2": "2. Cấu hình đồng bộ Zalo OA & Messenger",
        "guide-section-2-desc": "Truy cập mục Cấu HÌnh API, điền Access Token của Zalo Developer và Messenger Webhook. Trợ lý AI sẽ ngay lập tức tiếp nhận inbox mới và phản hồi tự động trong 5 giây.",
        "guides-hero-title": "Làm Chủ <span class=\"luxury-gradient\">Trí Tuệ AI</span>",
        "guides-hero-desc": "Khám phá tài liệu hướng dẫn chuyên sâu, tài liệu API và các bài học nâng cao cho hệ thống ChatbotPro.",
        "guides-tile-start-title": "Bắt Đầu Triển Khai",
        "guides-tile-start-desc": "Các khái niệm cốt lõi, thiết lập ban đầu và chiến lược khởi chạy nhân viên số AI.",
        "guides-tile-api-title": "Tích Hợp API",
        "guides-tile-api-desc": "Tài liệu Endpoint, Webhook và các giao thức xác thực bảo mật hệ thống.",
        "guides-tile-skills-title": "Kỹ Năng AI Chuyên Sâu",
        "guides-tile-skills-desc": "Prompt engineering, quản lý ngữ cảnh (context window) và cơ chế định tuyến LLM.",
        "guides-btn-read": "Đọc Hướng Dẫn",
        "guides-btn-docs": "Xem Tài Liệu",
        "guides-btn-master": "Làm Chủ Kỹ Năng",
        "guides-video-title": "Video Hướng Dẫn Nổi Bật",
        "guides-video-archive": "Xem Toàn Bộ Kho Lưu Trữ",
        "guides-v1-title": "Cấu Hình Đường Truyền Neural",
        "guides-v2-title": "Tối Ưu Ngữ Cảnh AI (Context Windows)",
        "guides-search-placeholder": "Tìm kiếm tài liệu...",
        "guides-video-tag-tutorial": "HƯỚNG DẪN",
        "guides-video-tag-deep": "CHUYÊN SÂU",

        // Lead capture modal
        "modal-title": "Mở Khóa Trợ Lý AI",
        "modal-subtitle": "Nhận ngay tài liệu hướng dẫn tích hợp Zalo/Messenger chi tiết.",
        "modal-label-name": "Họ và Tên",
        "modal-label-email": "Email Doanh Nghiệp",
        "modal-label-business": "Lĩnh Vực Hoạt Động",
        "modal-select-placeholder": "Chọn lĩnh vực...",
        "modal-option-finance": "Dịch vụ Tài chính / BĐS",
        "modal-option-saas": "SaaS / Phần mềm",
        "modal-option-ecommerce": "Bán lẻ / E-Commerce",
        "modal-option-other": "Khác / Dịch vụ tư vấn",
        "modal-btn-submit": "Đăng Ký Nhận Hướng Dẫn",
        "modal-benefit-1": "Nhận kịch bản tư vấn chốt đơn mẫu.",
        "modal-benefit-2": "Nhận tài liệu API Webhook Zalo OA.",
        "modal-benefit-3": "Tặng 1 buổi tư vấn 1-1 cùng chuyên gia."
    },
    ENG: {
        // Navigation Global
        "nav-features": "Features",
        "nav-pricing": "Pricing",
        "nav-roi": "ROI Calculator",
        "nav-login": "ENTERPRISE LOGIN",
        "nav-status": "System Status",
        "nav-health": "API Health",
        "nav-support": "Support",
        "nav-home": "Home",
        "nav-crm": "CRM Intelligence",
        "nav-api": "API Configuration",
        "nav-guides": "User Guides",
        "nav-settings": "Settings",
        "nav-admin-terminal": "Admin Terminal",
        "copyright": "© 2026 ChatbotPro. Digital Luxury AI Assistant Platform.",

        // Landing Page: Hero Section
        "hero-badge": "v4.0 Enterprise Core Online",
        "hero-title": "Command The Void.<br/><span class=\"luxury-gradient\">Digital Luxury AI.</span>",
        "hero-desc": "The apex of conversational intelligence. AI responds to clients in 5 seconds, operating 24/7. Reduces up to 80% repetitive support load, automating sales based on your data.",
        "hero-acquire": "ACQUIRE LICENSE NOW",
        "hero-demo": "CONTACT SALES",
        "trust-title": "TRUSTED BY APEX ORGANIZATIONS",

        // Landing Page: Architectural Flow (Steps)
        "steps-title": "Architectural Flow",
        "steps-sub": "Three phases to total command in just 15 minutes.",
        "step-1-title": "1. Connect Knowledge",
        "step-1-desc": "AI automatically ingests and learns from PDF, DOCX, XLSX files, or website links.",
        "step-2-title": "2. Train & Refine",
        "step-2-desc": "Fine-tune sales scripts, response tone, and specific product guidelines.",
        "step-3-title": "3. Deploy Multi-Channel",
        "step-3-desc": "Unleash omnipresent 24/7 support across Zalo, Messenger, WhatsApp, Instagram.",

        // Landing Page: Bento Grid & Features
        "bento-title": "Omnipresent Connectivity",
        "bento-sub": "20+ Languages. Infinite Integrations.",
        "api-title": "API Neural Net",
        "api-desc": "Dock seamlessly with Zalo OA, Fanpage, Instagram, WhatsApp, and auto-reply to ad comments.",
        "lexicon-title": "Global Lexicon",
        "lexicon-desc": "Fluent in power. Automatically detects customer language and responds contextually.",

        // Landing Page: Channels
        "channels-title": "30 Specialized Channels",
        "channels-sub": "Bespoke environments for every elite discipline and workflow.",
        "chan-sales": "Financial Sales",
        "chan-sales-desc": "Customer nurturing, sales closing, and automatic order routing.",
        "chan-admission": "Admissions Advisor",
        "chan-admission-desc": "Lead capture, candidate qualification, and CRM synchronization.",
        "chan-support": "DevOps Architect",
        "chan-support-desc": "Infrastructure as code queries and instant software documentation help.",
        "chan-more": "View 27 More",
        "chan-more-desc": "Specialized domains",

        // Landing Page: ROI Calculator
        "roi-title": "Real-Time ROI Projection",
        "roi-sub": "Calculate the financial impact of automating your channels.",
        "roi-label-tickets": "Monthly Support Tickets",
        "roi-label-cost": "Avg. Cost Per Resolution",
        "roi-label-deflection": "ChatbotPro Deflection Rate",
        "roi-savings-title": "PROJECTED MONTHLY SAVINGS",
        "roi-annual-savings": "Annual ROI",

        // Landing Page: Pricing
        "pricing-title": "Acquisition Tiers",
        "pricing-sub": "All-inclusive pricing, lifetime support, billed annually.",
        "price-starter-sub": "Essential tools for individual professionals.",
        "price-starter-f1": "5,000 response messages / month",
        "price-starter-f2": "Max 1 AI assistant",
        "price-starter-f3": "All core features included",
        "price-starter-btn": "INITIATE STARTER",
        "price-pro-sub": "Full capability for elite power users.",
        "price-pro-f1": "10,000 response messages / month",
        "price-pro-f2": "Max 2 AI assistants",
        "price-pro-f3": "Advanced customization & white-label",
        "price-pro-f4": "Zalo OA & Messenger support",
        "price-pro-btn": "ACQUIRE PRO LICENSE",
        "price-elite-sub": "Bespoke deployment for large organizations.",
        "price-elite-f1": "25,000 response messages / month",
        "price-elite-f2": "Max 5 AI assistants",
        "price-elite-f3": "Complete Whitelabel options",
        "price-elite-f4": "Custom API Integrations",
        "price-elite-btn": "CONTACT SALES",

        // Landing Page: FAQs
        "faq-title": "Enterprise Inquiries",
        "faq-sub": "Clarity before command.",
        "faq-q1": "Is my proprietary data secure?",
        "faq-a1": "Absolute isolation. We utilize military-grade encryption (AES-256) at rest and in transit. Your data is never shared.",
        "faq-q2": "How fast is deployment?",
        "faq-a2": "Standard knowledge base ingestion takes under 15 minutes. Custom setups are live in a few hours.",
        "faq-q3": "Does the AI hallucinate or provide false answers?",
        "faq-a3": "No. Our 'Enforcement Engineering' limits the AI to only extract answers from your approved documents, avoiding hallucinations.",

        // Landing Page: Urgency Sale
        "urgency-badge": "LIMITED AVAILABILITY: BATCH 004 CLOSING",
        "urgency-title": "Secure Your Node Now",
        "urgency-desc": "Deploy our digital luxury AI to automate 80% of client chats, responding within 5s 24/7.",
        "urgency-btn": "ACQUIRE LICENSE NOW",

        // Checkout Page
        "checkout-title": "Payment Method",
        "checkout-desc": "All transactions are secure and encrypted.",
        "checkout-method-card": "CREDIT CARD",
        "checkout-method-wallet": "PAYPAL",
        "checkout-method-apple": "APPLE PAY",
        "checkout-label-number": "CARD NUMBER",
        "checkout-label-expiry": "EXPIRY DATE",
        "checkout-label-name": "CARDHOLDER NAME",
        "checkout-billing-title": "Billing Address",
        "checkout-label-address": "STREET ADDRESS",
        "checkout-label-city": "CITY",
        "checkout-label-zip": "ZIP / POSTAL",
        "checkout-summary-title": "Order Summary",
        "checkout-subtotal": "Subtotal",
        "checkout-tax": "Tax (VAT included)",
        "checkout-btn-pay": "PAY NOW",
        "checkout-secure": "256-bit SSL Secure Checkout",

        // Dashboard & CRM
        "dash-title": "CRM Dashboard",
        "dash-sub": "Monitor automated AI agent operations and client details.",
        "dash-card-revenue": "AI Revenue",
        "dash-card-chats": "Completed Chats",
        "dash-card-deflection": "Deflection Rate",
        "dash-card-satisfaction": "Satisfaction Rate",
        "dash-roster-title": "Client Roster",
        "dash-roster-sub": "Synced in real-time from Zalo, Messenger, and Website.",
        "dash-search-placeholder": "Search clients, channels...",
        "dash-col-name": "CLIENT NAME",
        "dash-col-channel": "CHANNEL",
        "dash-col-status": "STATUS",
        "dash-col-date": "DATE CONVERSATION",
        "dash-col-action": "ACTION",
        "dash-status-auto": "Automated",
        "dash-status-manual": "Staff required",

        // Environment Variables
        "env-title": "API Keys Control Manager",
        "dash-env-sub": "Configure keys for LLM providers, Zalo API, and webhooks.",
        "env-btn-add": "Add Variable",
        "env-col-key": "VARIABLE KEY",
        "env-col-value": "VALUE",
        "env-col-desc": "DESCRIPTION",
        "env-col-action": "ACTION",
        "env-btn-reveal": "Show",
        "env-btn-hide": "Hide",
        "env-btn-delete": "Delete",
        "env-btn-audit": "Audit Log",
        "env-btn-deploy": "Deploy Changes",
        "env-card-infra": "Core Infrastructure Keys",
        "env-card-params": "System Parameters",
        "env-label-model": "Default Model",
        "env-label-tokens": "Max Tokens Per Request",
        "env-label-temp": "Temperature",
        "env-label-cache": "Enable Vector Cache",
        "env-card-connections": "Active Connections",
        "env-card-details": "Environment Details",
        "env-detail-env": "Current Env:",
        "env-detail-region": "Region:",
        "env-detail-updated": "Last Updated:",
        "env-detail-hash": "Version Hash:",
        "env-placeholder-key": "NEW_VARIABLE_KEY",
        "env-placeholder-value": "Value...",       "checkout-secure": "256-bit SSL Secure Checkout",

        // Dashboard & CRM
        "dash-title": "CRM Dashboard",
        "dash-sub": "Monitor automated AI agent operations and client details.",
        "dash-card-revenue": "AI Revenue",
        "dash-card-chats": "Completed Chats",
        "dash-card-deflection": "Deflection Rate",
        "dash-card-satisfaction": "Satisfaction Rate",
        "dash-roster-title": "Client Roster",
        "dash-roster-sub": "Synced in real-time from Zalo, Messenger, and Website.",
        "dash-search-placeholder": "Search clients, channels...",
        "dash-col-name": "CLIENT NAME",
        "dash-col-channel": "CHANNEL",
        "dash-col-status": "STATUS",
        "dash-col-date": "DATE CONVERSATION",
        "dash-col-action": "ACTION",
        "dash-status-auto": "Automated",
        "dash-status-manual": "Staff required",

        // Environment Variables
        "env-title": "API Keys Control Manager",
        "dash-env-sub": "Configure keys for LLM providers, Zalo API, and webhooks.",
        "env-btn-add": "Add Variable",
        "env-col-key": "VARIABLE KEY",
        "env-col-value": "VALUE",
        "env-col-desc": "DESCRIPTION",
        "env-col-action": "ACTION",
        "env-btn-reveal": "Show",
        "env-btn-hide": "Hide",
        "env-btn-delete": "Delete",

        // Guides Page
        "guides-title": "User Mastery Support Center",
        "dash-guides-sub": "Documentation on training, integrations, and performance.",
        "guide-doc-title": "AI Agent Deployment Playbook",
        "guide-section-1": "1. Knowledge Base Ingestion Guide",
        "guide-section-1-desc": "Ingest document files (.pdf, .docx, .xlsx) or website links. The crawler index will parse and structure data within 1-2 minutes for immediate retrieval.",
        "guide-section-2": "2. Zalo OA & Messenger Webhook Setup",
        "guide-section-2-desc": "Retrieve access tokens from Zalo Developer or Meta Developer portals, input them in API Configs, and verify webhooks for instant 5s response automation.",
        "guides-hero-title": "Master Your <span class=\"luxury-gradient\">Intelligence</span>",
        "guides-hero-desc": "Explore comprehensive guides, API references, and advanced tutorials designed for power users operating the ChatbotPro framework.",
        "guides-tile-start-title": "Getting Started",
        "guides-tile-start-desc": "Core concepts, initial setup, and deployment strategies for your first autonomous agent.",
        "guides-tile-api-title": "API Integration",
        "guides-tile-api-desc": "RESTful endpoints, webhooks, and secure authentication protocols for custom telemetry.",
        "guides-tile-skills-title": "Advanced AI Skills",
        "guides-tile-skills-desc": "Prompt engineering, context window management, and custom LLM routing mechanics.",
        "guides-btn-read": "Read Guide",
        "guides-btn-docs": "View Docs",
        "guides-btn-master": "Master Skills",
        "guides-video-title": "Featured Transmissions",
        "guides-video-archive": "View All Archive",
        "guides-v1-title": "Configuring Neural Pathways",
        "guides-v2-title": "Mastering Context Windows",
        "guides-search-placeholder": "Search documentation...",
        "guides-video-tag-tutorial": "TUTORIAL",
        "guides-video-tag-deep": "DEEP DIVE",

        // Lead capture modal
        "modal-title": "Unlock AI Sales",
        "modal-subtitle": "Request your bespoke integration guide and join the automated tier.",
        "modal-label-name": "Full Name",
        "modal-label-email": "Enterprise Email",
        "modal-label-business": "Business Type",
        "modal-select-placeholder": "Select category...",
        "modal-option-finance": "Financial Services / Real Estate",
        "modal-option-saas": "Enterprise SaaS",
        "modal-option-ecommerce": "High-Volume E-Commerce",
        "modal-option-other": "Other / Consultancy",
        "modal-btn-submit": "Get Elite Access",
        "modal-benefit-1": "Access to sales scripts.",
        "modal-benefit-2": "API Webhook blueprints.",
        "modal-benefit-3": "Onboarding consultation."
    }
};

// 1. Inject common cyber-glass light mode styles dynamically
function initCommonStyles() {
    const styleId = 'chatbotpro-common-styles';
    if (document.getElementById(styleId)) return;

    const styles = `
        /* Language Selector custom styles */
        .lang-active-indicator {
            background: linear-gradient(90deg, #6750a4 0%, #d97706 100%);
        }
        
        /* Lead modal animation & transitions */
        .modal-visible {
            opacity: 1 !important;
            pointer-events: auto !important;
        }
        .modal-scale {
            transform: scale(0.95);
            transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.3s ease;
        }
        .modal-visible .modal-scale {
            transform: scale(1) !important;
        }
        
        /* Toast Notification Styles - Bright Premium Mode */
        .luxury-toast {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(103, 80, 164, 0.15);
            box-shadow: 0 10px 30px rgba(103, 80, 164, 0.08), inset 0 0 0 1px rgba(255, 255, 255, 0.6);
            color: #0f172a;
            transform: translateY(20px);
            opacity: 0;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .luxury-toast.toast-show {
            transform: translateY(0);
            opacity: 1;
        }
        .toast-progress-bar {
            height: 2px;
            background: linear-gradient(90deg, #6750a4 0%, #d97706 100%);
            width: 100%;
            transition: width linear;
        }
    `;

    const styleEl = document.createElement('style');
    styleEl.id = styleId;
    styleEl.innerHTML = styles;
    document.head.appendChild(styleEl);
}

// Translate page contents dynamically
function translatePage() {
    const lang = localStorage.getItem('chatbotpro_lang') || 'VIE';
    
    // Set document lang attribute
    document.documentElement.setAttribute('lang', lang === 'VIE' ? 'vi' : 'en');
    
    const dict = translations[lang] || translations.VIE;
    
    // Find all elements with data-translate attribute
    document.querySelectorAll('[data-translate]').forEach(el => {
        const key = el.getAttribute('data-translate');
        if (dict[key]) {
            el.innerHTML = dict[key];
        }
    });

    // Find all inputs/textareas with data-translate-placeholder
    document.querySelectorAll('[data-translate-placeholder]').forEach(el => {
        const key = el.getAttribute('data-translate-placeholder');
        if (dict[key]) {
            el.setAttribute('placeholder', dict[key]);
        }
    });
}

// 2. Language Selector Implementation
const languages = [
    { name: 'Vietnamese', code: 'VIE', native: 'Tiếng Việt' },
    { name: 'English', code: 'ENG', native: 'English' }
];

function initLanguageSelector() {
    // Check if selector element already exists
    if (document.getElementById('language-selector-overlay')) return;

    // Create Language Selector Overlay
    const overlay = document.createElement('div');
    overlay.id = 'language-selector-overlay';
    overlay.className = 'fixed inset-0 z-[100] flex items-center justify-center bg-[#f8f9fc]/90 backdrop-blur-2xl opacity-0 pointer-events-none transition-all duration-300';
    
    // Default selected language
    let activeLang = localStorage.getItem('chatbotpro_lang') || 'VIE';

    const overlayContent = `
        <div class="relative w-full max-w-2xl px-6 py-12 text-center modal-scale">
            <!-- Close Button -->
            <button id="close-lang-selector" class="absolute top-0 right-6 text-on-surface-variant hover:text-primary transition-colors group">
                <span class="material-symbols-outlined text-[32px] group-hover:rotate-90 transition-transform duration-300">close</span>
            </button>
            
            <h2 class="font-display-lg text-headline-md bg-gradient-to-r from-primary to-tertiary bg-clip-text text-transparent font-bold mb-4" data-translate="modal-title-lang">Chọn Ngôn Ngữ / Select Language</h2>
            <p class="font-body-lg text-body-sm text-on-surface-variant mb-12 max-w-md mx-auto">Chọn ngôn ngữ để cập nhật toàn bộ nội dung hệ thống.</p>
            
            <!-- Grid of Languages -->
            <div class="grid grid-cols-2 gap-6 text-left max-w-md mx-auto">
                ${languages.map(lang => `
                    <div data-lang="${lang.code}" class="lang-card bg-white border ${lang.code === activeLang ? 'border-primary shadow-[0_0_15px_rgba(103,80,164,0.15)]' : 'border-outline-variant/30'} p-6 rounded-2xl cursor-pointer hover:border-primary/50 relative overflow-hidden group transition-all duration-300 hover:-translate-y-0.5">
                        <div class="flex flex-col justify-between h-full">
                            <span class="font-mono-data text-mono-data text-xs text-outline group-hover:text-primary transition-colors">${lang.code}</span>
                            <span class="font-display-lg text-lg font-bold text-on-surface mt-2">${lang.native}</span>
                            <span class="text-xs text-on-surface-variant/70 mt-1">${lang.name}</span>
                        </div>
                        <div class="lang-indicator absolute bottom-0 left-0 right-0 h-[4px] bg-gradient-to-r from-primary to-tertiary transition-transform duration-300 ${lang.code === activeLang ? 'scale-x-100' : 'scale-x-0'} origin-left"></div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;

    overlay.innerHTML = overlayContent;
    document.body.appendChild(overlay);

    // Bind event listeners to open the selector
    document.body.addEventListener('click', (e) => {
        const langBtn = e.target.closest('[aria-label="language"]') || e.target.closest('.material-symbols-outlined')?.parentElement?.classList.contains('language') || (e.target.innerText === 'language' && e.target.classList.contains('material-symbols-outlined'));
        if (langBtn) {
            e.preventDefault();
            overlay.classList.add('modal-visible');
        }
    });

    // Close button
    document.getElementById('close-lang-selector').addEventListener('click', () => {
        overlay.classList.remove('modal-visible');
    });

    // Clicking language cards
    overlay.querySelectorAll('.lang-card').forEach(card => {
        card.addEventListener('click', () => {
            const selectedLang = card.getAttribute('data-lang');
            localStorage.setItem('chatbotpro_lang', selectedLang);
            
            // Update UI indicators
            overlay.querySelectorAll('.lang-card').forEach(c => {
                c.classList.remove('border-primary', 'shadow-[0_0_15px_rgba(103,80,164,0.15)]');
                c.classList.add('border-outline-variant/30');
                c.querySelector('.lang-indicator').classList.remove('scale-x-100');
                c.querySelector('.lang-indicator').classList.add('scale-x-0');
            });
            
            card.classList.add('border-primary', 'shadow-[0_0_15px_rgba(103,80,164,0.15)]');
            card.classList.remove('border-outline-variant/30');
            card.querySelector('.lang-indicator').classList.add('scale-x-100');
            card.querySelector('.lang-indicator').classList.remove('scale-x-0');

            setTimeout(() => {
                overlay.classList.remove('modal-visible');
                const selectedLangObj = languages.find(l => l.code === selectedLang);
                
                // Translate the elements
                translatePage();
                
                // Call global triggers for calculators or charts if any
                const event = new CustomEvent('langChanged', { detail: selectedLang });
                document.dispatchEvent(event);

                window.showToast(
                    selectedLang === 'VIE' 
                        ? `Đã chuyển đổi giao diện sang Tiếng Việt` 
                        : `Language context updated to English`, 
                    'success'
                );
            }, 200);
        });
    });

    // Close on clicking backdrop
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            overlay.classList.remove('modal-visible');
        }
    });
}

// 3. Lead Capture Modal Injection and Binding - Bright Theme
function initLeadCaptureModal() {
    if (document.getElementById('lead-capture-modal')) return;

    const modal = document.createElement('div');
    modal.id = 'lead-capture-modal';
    modal.className = 'fixed inset-0 z-[90] flex items-center justify-center bg-[#050505]/30 backdrop-blur-sm opacity-0 pointer-events-none transition-all duration-300';
    
    const modalContent = `
        <div class="relative w-full max-w-2xl px-4 md:px-0 mx-auto modal-scale">
            <div class="bg-white/95 backdrop-blur-[40px] rounded-[24px] border border-outline-variant/30 shadow-[0_15px_50px_rgba(103,80,164,0.15)] overflow-hidden text-on-surface">
                <!-- Close Button -->
                <button id="close-lead-modal" aria-label="Close dialog" class="absolute top-6 right-6 text-on-surface-variant hover:text-primary transition-colors z-20 group">
                    <span class="material-symbols-outlined text-[24px] group-hover:rotate-90 transition-transform duration-300">close</span>
                </button>
                <div class="flex flex-col md:flex-row">
                    <!-- Visual / Branding Area -->
                    <div class="md:w-5/12 bg-primary/5 p-8 flex flex-col justify-between border-b md:border-b-0 md:border-r border-outline-variant/20 relative overflow-hidden">
                        <div class="absolute -top-20 -left-20 w-40 h-40 bg-primary-container/40 blur-[50px] rounded-full"></div>
                        <div class="relative z-10">
                            <div class="flex items-center space-x-2 mb-8">
                                <span class="material-symbols-outlined text-primary text-[28px]">smart_toy</span>
                                <span class="font-display-lg text-body-lg font-bold tracking-tight text-primary">ChatbotPro</span>
                            </div>
                            <div class="mt-8 space-y-6">
                                <div class="flex items-start space-x-3">
                                    <span class="material-symbols-outlined text-tertiary text-[20px] mt-1" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                                    <p class="font-body-sm text-body-sm text-on-surface-variant" data-translate="modal-benefit-1">Nhận kịch bản tư vấn chốt đơn mẫu.</p>
                                </div>
                                <div class="flex items-start space-x-3">
                                    <span class="material-symbols-outlined text-tertiary text-[20px] mt-1" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                                    <p class="font-body-sm text-body-sm text-on-surface-variant" data-translate="modal-benefit-2">Nhận tài liệu API Webhook Zalo OA.</p>
                                </div>
                                <div class="flex items-start space-x-3">
                                    <span class="material-symbols-outlined text-tertiary text-[20px] mt-1" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                                    <p class="font-body-sm text-body-sm text-on-surface-variant" data-translate="modal-benefit-3">Tặng 1 buổi tư vấn 1-1 cùng chuyên gia.</p>
                                </div>
                            </div>
                        </div>
                        <div class="mt-12 relative z-10">
                            <p class="font-mono-data text-mono-data text-on-surface-variant opacity-60 uppercase tracking-widest text-xs">ChatbotPro AI</p>
                        </div>
                    </div>
                    
                    // Form Area
                    <div class="md:w-7/12 p-8 md:p-10 relative bg-white">
                        <div class="mb-6">
                            <h2 class="font-display-lg-mobile text-xl font-bold bg-gradient-to-r from-primary via-secondary to-tertiary bg-clip-text text-transparent mb-2" data-translate="modal-title">Mở Khóa Trợ Lý AI</h2>
                            <p class="font-body-sm text-body-sm text-on-surface-variant" data-translate="modal-subtitle">Nhận ngay tài liệu hướng dẫn tích hợp Zalo/Messenger chi tiết.</p>
                        </div>
                        <form id="lead-capture-form" class="space-y-4">
                            <!-- Name Field -->
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-name" data-translate="modal-label-name">Họ và Tên</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[18px]">person</span>
                                    </span>
                                    <input class="w-full bg-surface-container border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-4 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors placeholder:text-outline/50" id="modal-name" required placeholder="Jane Doe" type="text"/>
                                </div>
                            </div>
                            <!-- Email Field -->
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-email" data-translate="modal-label-email">Email Doanh Nghiệp</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[18px]">mail</span>
                                    </span>
                                    <input class="w-full bg-surface-container border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-4 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors placeholder:text-outline/50" id="modal-email" required placeholder="jane@company.com" type="email"/>
                                </div>
                            </div>
                            <!-- Business Type Dropdown -->
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-business" data-translate="modal-label-business">Lĩnh Vực Hoạt Động</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant z-10 pointer-events-none">
                                        <span class="material-symbols-outlined text-[18px]">domain</span>
                                    </span>
                                    <select class="w-full bg-surface-container border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-10 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors appearance-none cursor-pointer" id="modal-business" required>
                                        <option disabled selected value="" data-translate="modal-select-placeholder">Chọn lĩnh vực...</option>
                                        <option value="finance" data-translate="modal-option-finance">Dịch vụ Tài chính / BĐS</option>
                                        <option value="saas" data-translate="modal-option-saas">SaaS / Phần mềm</option>
                                        <option value="ecommerce" data-translate="modal-option-ecommerce">Bán lẻ / E-Commerce</option>
                                        <option value="other" data-translate="modal-option-other">Khác / Dịch vụ tư vấn</option>
                                    </select>
                                    <span class="absolute inset-y-0 right-0 flex items-center pr-3 text-on-surface-variant pointer-events-none">
                                        <span class="material-symbols-outlined text-[20px]">expand_more</span>
                                    </span>
                                </div>
                            </div>
                            <!-- Action Button -->
                            <div class="pt-2">
                                <button type="submit" class="w-full bg-gradient-to-r from-primary to-secondary hover:brightness-105 text-white font-label-caps text-label-caps py-3 px-6 rounded-lg transition-all shadow-[0_0_20px_rgba(103,80,164,0.1)] hover:shadow-[0_0_25px_rgba(103,80,164,0.2)] flex items-center justify-center space-x-2">
                                    <span data-translate="modal-btn-submit">Đăng Ký Nhận Hướng Dẫn</span>
                                    <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    `;

    modal.innerHTML = modalContent;
    document.body.appendChild(modal);

    // Bind event listeners to close buttons
    document.getElementById('close-lead-modal').addEventListener('click', () => {
        modal.classList.remove('modal-visible');
    });
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('modal-visible');
        }
    });

    // Form submission
    document.getElementById('lead-capture-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('modal-name').value;
        const email = document.getElementById('modal-email').value;
        
        modal.classList.remove('modal-visible');
        
        // Show success toast
        const currentLang = localStorage.getItem('chatbotpro_lang') || 'VIE';
        const successMsg = currentLang === 'VIE'
            ? `Đã đăng ký thành công cho ${name} (${email}). Hướng dẫn đã gửi vào hộp thư!`
            : `Access requested successfully for ${name} (${email}). Integration playbook sent!`;
        window.showToast(successMsg, 'success');
        
        // Clear fields
        document.getElementById('lead-capture-form').reset();
    });

    // Bind CTA click triggers
    document.body.addEventListener('click', (e) => {
        const ctaBtn = e.target.closest('.trigger-lead-capture') || 
                       (e.target.innerText && (
                           e.target.innerText.includes('ĐẶT LỊCH DEMO') || 
                           e.target.innerText.includes('VIEW ARCHITECTURE') ||
                           e.target.innerText.includes('CONTACT SALES') ||
                           e.target.innerText.includes('YÊU CẦU DEMO')
                       ));
        if (ctaBtn) {
            e.preventDefault();
            // Translate the modal before showing
            translatePage();
            modal.classList.add('modal-visible');
        }
    });
}

// 4. Premium Toast Notification System - Light Mode Colors
function initToastSystem() {
    // Create toast container if not exists
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.className = 'fixed bottom-6 right-6 z-[120] flex flex-col gap-3 max-w-md w-full px-4 sm:px-0';
        document.body.appendChild(toastContainer);
    }

    // Expose showToast globally
    window.showToast = function(message, type = 'success', duration = 4000) {
        const toast = document.createElement('div');
        toast.className = 'luxury-toast rounded-xl overflow-hidden flex flex-col w-full';
        
        // Set accent colors based on type
        let borderClass = 'border-l-4 border-l-primary';
        let icon = 'check_circle';
        let iconColor = 'text-primary';
        
        if (type === 'success') {
            borderClass = 'border-l-4 border-l-[#10b981]'; // Emerald Success
            icon = 'verified';
            iconColor = 'text-[#10b981]';
        } else if (type === 'error') {
            borderClass = 'border-l-4 border-l-[#ef4444]'; // Red Error
            icon = 'error';
            iconColor = 'text-[#ef4444]';
        } else if (type === 'info') {
            borderClass = 'border-l-4 border-l-tertiary';
            icon = 'info';
            iconColor = 'text-tertiary';
        }

        toast.innerHTML = `
            <div class="flex items-center gap-4 px-5 py-4 ${borderClass}">
                <span class="material-symbols-outlined ${iconColor} text-[22px]">${icon}</span>
                <div class="flex-grow">
                    <p class="font-body-sm text-body-sm text-on-surface font-medium">${message}</p>
                </div>
                <button class="toast-close-btn text-on-surface-variant hover:text-on-surface transition-colors">
                    <span class="material-symbols-outlined text-[18px]">close</span>
                </button>
            </div>
            <div class="toast-progress-bar" style="width: 100%; transition-duration: ${duration}ms"></div>
        `;

        toastContainer.appendChild(toast);
        
        // Trigger reflow for slide/fade in animation
        toast.offsetHeight;
        toast.classList.add('toast-show');

        // Close button action
        toast.querySelector('.toast-close-btn').addEventListener('click', () => {
            toast.classList.remove('toast-show');
            setTimeout(() => toast.remove(), 400);
        });

        // Trigger progress bar countdown
        const progressBar = toast.querySelector('.toast-progress-bar');
        setTimeout(() => {
            if (progressBar) progressBar.style.width = '0%';
        }, 50);

        // Auto remove
        setTimeout(() => {
            if (toast.parentElement) {
                toast.classList.remove('toast-show');
                setTimeout(() => toast.remove(), 400);
            }
        }, duration);
    };
}

// 5. Global Link Handlers
function initGlobalLinkHandlers() {
    // Detect page context to bind specific events
    const currentPath = window.location.pathname;
    
    // Sidebar Active State Auto-matching
    const sidebarLinks = document.querySelectorAll('aside nav a, nav.desktop-nav a, nav.desktop-nav + nav a, .desktop-nav nav a');
    if (sidebarLinks.length > 0) {
        sidebarLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href || href === '#' || href.startsWith('#')) return;
            
            // Normalize path matching
            const isMatch = currentPath.includes(href) || 
                            (currentPath.endsWith('/') && href === 'index.html');
            
            if (isMatch) {
                // Remove active classes from siblings
                sidebarLinks.forEach(l => {
                    l.classList.remove('bg-primary/10', 'text-primary', 'border-r-2', 'border-primary', 'active');
                    l.classList.add('text-on-surface-variant');
                });
                
                // Add active classes to matched link
                link.classList.add('bg-primary/10', 'text-primary', 'border-r-2', 'border-primary', 'active');
                link.classList.remove('text-on-surface-variant');
            }
        });
    }

    // Bind custom login redirection
    document.body.addEventListener('click', (e) => {
        const loginBtn = e.target.closest('button');
        if (loginBtn && loginBtn.textContent.trim().includes('LOGIN') || loginBtn && loginBtn.textContent.trim().includes('ĐĂNG NHẬP')) {
            e.preventDefault();
            window.location.href = 'dashboard.html';
        }
    });
}
