// Shared Premium UI Logic for ChatbotPro Omnichat Business Hub
document.addEventListener('DOMContentLoaded', () => {
    initCommonStyles();
    initLanguageSelector();
    initLeadCaptureModal();
    initToastSystem();
    initGlobalLinkHandlers();
    
    // Core Role Permissions & SideBar Link adjustments
    initRoleSwitcher();
    applyRolePermissions();
    checkRoleAccess();
    
    // Global floating voice sales chatbot
    initFloatingSalesBot();
    
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
        "nav-crm": "Hội thoại & CRM",
        "nav-api": "Cài đặt API",
        "nav-guides": "Hướng dẫn",
        "nav-settings": "Cài Đặt",
        "nav-admin-terminal": "Admin Terminal",
        "copyright": "© 2026 ChatbotPro. Trợ lý Trí Tuệ Nhân Tạo Doanh Nghiệp.",
        "nav-team": "Phân quyền Team",
        "nav-logout": "Quay Lại Web",
        "nav-market": "Thị Trường AI",

        // Role Switcher & Access Control
        "role-label": "VAI TRÒ:",
        "role-owner": "Chủ Doanh Nghiệp",
        "role-staff": "Nhân Viên Trực",
        "role-access-denied-title": "TRUY CẬP BỊ TỪ CHỐI",
        "role-access-denied-desc": "Bạn đang ở vai trò Nhân Viên. Bạn không có quyền truy cập vào trang cấu hình API hoặc phân quyền team. Vui lòng liên hệ Chủ Doanh Nghiệp để cấu hình hệ thống.",
        "role-access-denied-btn": "Quay lại Bảng CRM",

        // Landing Page: Hero Section
        "hero-badge": "v4.0 Core Nhân Viên Số Hoạt Động",
        "hero-title": "CỖ MÁY CHỐT ĐƠN <br/><span class=\"bg-gradient-to-r from-emerald-500 to-teal-600 bg-clip-text text-transparent font-extrabold\">TỰ ĐỘNG 24/7</span>",
        "hero-desc": "Đừng để khách hàng chờ. Trợ lý AI phản hồi nhanh trong 5 giây, tự động chăm sóc và chốt đơn đa kênh theo dữ liệu tri thức riêng của doanh nghiệp.",
        "hero-acquire": "ĐĂNG KÝ SỬ DỤNG NGAY",
        "hero-demo": "ĐẶT LỊCH DEMO 1-1",
        "trust-title": "ĐƯỢC TIN DÙNG BỞI CÁC TỔ CHỨC ĐẦU NGÀNH",

        // Landing Page: Architectural Flow (Steps)
        "steps-title": "Lợi Ích Vượt Trội",
        "steps-sub": "Đột phá doanh thu nhờ trợ lý AI thông minh thế hệ mới.",
        "step-1-title": "AI phản hồi nhanh như thật",
        "step-1-desc": "Trả lời khách hàng ngay lập tức trong 5 giây, hành văn tự nhiên mang lại cảm xúc giống như người thật.",
        "step-2-title": "Tự động chăm sóc không bỏ sót",
        "step-2-desc": "Hoạt động bền bỉ 24/7 đa kênh Zalo, Facebook, TikTok, WhatsApp, giải quyết mọi yêu cầu tức thì.",
        "step-3-title": "Tăng chuyển đổi bền vững",
        "step-3-desc": "Tự động nhận diện nhu cầu mua sắm, đề xuất tư vấn thuyết phục để chốt đơn nhanh chóng.",

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
        "copyright-secure": "Thanh toán bảo mật chuẩn quốc tế",

        // Dashboard & CRM
        "dash-title": "Bảng Điều Khiển CRM",
        "dash-sub": "Giám sát hiệu suất nhân viên số và dữ liệu khách hàng.",
        "dash-card-revenue": "Doanh Thu AI",
        "dash-card-chats": "Hội Thoại Hoàn Tất",
        "dash-card-deflection": "Tỷ Lệ Tự Động Hóa",
        "dash-card-satisfaction": "Mức Độ Hài Lòng",
        "dash-roster-title": "Danh Sách Khách Hàng",
        "dash-roster-sub": "Tự động đồng bộ từ Messenger, Zalo OA và Zalo cá nhân.",
        "dash-search-placeholder": "Tìm kiếm...",
        "dash-col-name": "KHÁCH HÀNG",
        "dash-col-channel": "KÊNH KẾT NỐI",
        "dash-col-status": "TRẠNG THÁI",
        "dash-col-date": "NGÀY TƯ VẤN",
        "dash-col-action": "THAO TÁC",
        "dash-status-auto": "Tự động hóa",
        "dash-status-manual": "Cần nhân sự trực",

        // Environment Variables (Cấu hình API)
        "env-title": "Cấu Hình API & Hệ Thống",
        "dash-env-sub": "Cấu hình API Keys kết nối LLM, cơ sở dữ liệu và các thông số mô hình.",
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
        
        // Social Connections (Integrations Grid)
        "channels-tab-title": "Cấu Hình Kênh Kết Nối",
        "channels-tab-sub": "Đồng bộ Access Token, Webhook và tài khoản mạng xã hội để tự động hóa chốt đơn.",
        "chan-status-connected": "Đang hoạt động",
        "chan-status-disconnected": "Chưa kết nối",
        "chan-btn-connect": "KẾT NỐI KÊNH",
        "chan-btn-disconnect": "NGẤT KẾT NỐI",
        "chan-modal-title": "Cấu Hình Kết Nối API Kênh",
        "chan-modal-webhook-label": "Webhook URL (Nhận sự kiện tin nhắn)",
        "chan-modal-token-label": "Access Token / API Key kết nối",
        "chan-modal-id-label": "Page ID / Shop ID / Group ID",
        "chan-btn-copy": "Sao Chép",
        "chan-btn-save": "LƯU KẾT NỐI",

        // Inbox & Chat Console
        "chat-tab-all": "Tất cả",
        "chat-tab-zalo": "Zalo OA",
        "chat-tab-facebook": "Facebook Page/Msg",
        "chat-tab-tiktok": "TikTok Shop",
        "chat-tab-shopee": "Shopee / Lazada",
        "chat-tab-website": "Website Widget",
        "chat-autopilot-active": "AI tự động trực",
        "chat-autopilot-inactive": "Nhân viên trực chat",
        "chat-autopilot-toggle": "Chế độ tự động (AI Autopilot)",
        "chat-input-placeholder": "Nhập tin nhắn... (Gõ tin nhắn tự động tắt AI)",
        "chat-ai-suggestions": "AI GỢI Ý PHẢN HỒI",
        "chat-crm-details": "THÔNG TIN KHÁCH HÀNG CRM",
        "chat-crm-phone": "Số điện thoại",
        "chat-crm-address": "Địa chỉ đơn hàng",
        "chat-crm-notes": "Ghi chú đơn hàng",
        "chat-btn-takeover": "👤 Can thiệp thủ công",
        "chat-btn-enable-ai": "🤖 Kích hoạt lại AI",
        "chat-ai-suggest-badge": "AI gợi ý chốt đơn",
        "chat-active-threads": "Hội thoại đang hoạt động",

        // Team Management Page
        "team-title": "Phân Quyền & Đội Ngũ Nhân Sự",
        "team-sub": "Thiết lập tài khoản, vai trò và phân quyền truy cập chức năng cho nhân viên.",
        "team-col-name": "NHÂN SỰ",
        "team-col-role": "VAI TRÒ HỆ THỐNG",
        "team-col-status": "TRẠNG THÁI",
        "team-col-permissions": "PHÂN QUYỀN TRUY CẬP TRANG",
        "team-col-action": "THAO TÁC",
        "team-btn-add": "Thêm Thành Viên",
        "team-status-active": "Hoạt động",
        "team-status-inactive": "Tạm khóa",
        "team-modal-add-title": "Thêm Nhân Sự Đội Ngũ",
        "team-modal-label-name": "Tên Nhân Viên",
        "team-modal-label-email": "Địa Chỉ Email",
        "team-modal-label-role": "Vai Trò Nhân Sự",
        "team-modal-label-permissions": "Phân Quyền Chi Tiết",
        "team-btn-save": "LƯU NHÂN SỰ",
        "team-perm-crm": "Quản lý CRM & Chat",
        "team-perm-api": "Cấu hình API & Kênh",
        "team-perm-guides": "Xem tài liệu Hướng dẫn",
        "team-perm-team": "Quản lý Đội ngũ",
        "team-tab-roster": "Phân Quyền Nhân Sự",
        "team-tab-owner": "Cấu Hình Chủ Sở Hữu & Giọng Nói AI",
        "owner-card-profile": "Hồ Sơ & Logo Doanh Nghiệp",
        "owner-card-voice": "Cấu Hình Giọng Nói AI & Kênh Hotline",
        "owner-label-avatar": "Avatar Chủ Doanh Nghiệp (Ảnh/Video)",
        "owner-label-logo": "Logo Thương Hiệu",
        "owner-label-voice-model": "Mô Hình Giọng Nói AI",
        "owner-label-voice-speed": "Tốc Độ Đọc Giọng Nói",
        "owner-label-hotline": "Số Điện Thoại Hotline",
        "owner-btn-save": "LƯU CÀI ĐẶT CHỦ SỞ HỮU",


        // Floating Sales Bot
        "bot-greeting": "Chào bạn! Mình là Trợ lý Voice AI của ChatbotPro. Bật Giọng Nói để nghe mình phản hồi trực tiếp nhé! Bạn cần tư vấn gói Starter (550k/tháng), Standard (1.1M/tháng) hay Edition (2.75M/tháng)? Hotline: 0901.234.567",
        "bot-voice-on": "Bật Giọng Nói Real-time 🔊",
        "bot-voice-off": "Tắt Giọng Nói 🔇",
        "bot-placeholder": "Hỏi bot bán hàng... (Bằng tiếng Việt)",
        "bot-socials-title": "Mạng xã hội:",
        "bot-hotline-title": "Hotline hỗ trợ:"
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
        "nav-api": "API & Channels",
        "nav-guides": "User Guides",
        "nav-settings": "Settings",
        "nav-admin-terminal": "Admin Terminal",
        "copyright": "© 2026 ChatbotPro. Digital Luxury AI Assistant Platform.",
        "nav-team": "Team Permissions",
        "nav-logout": "Back to Web",
        "nav-market": "AI Markets",

        // Role Switcher & Access Control
        "role-label": "ROLE:",
        "role-owner": "Owner / Admin",
        "role-staff": "Chat Staff / Agent",
        "role-access-denied-title": "ACCESS DENIED",
        "role-access-denied-desc": "You are currently logged in with the Staff role. You do not have permissions to access API configurations or Team Permissions. Please contact the Owner.",
        "role-access-denied-btn": "Return to CRM",

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
        "faq-title": "FAQ",
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
        "checkout-method-wallet": "PAYPAL / MOMO",
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
        "dash-search-placeholder": "Search...",
        "dash-col-name": "CLIENT NAME",
        "dash-col-channel": "CHANNEL",
        "dash-col-status": "STATUS",
        "dash-col-date": "DATE CONVERSATION",
        "dash-col-action": "ACTION",
        "dash-status-auto": "Automated",
        "dash-status-manual": "Staff required",

        // Environment Variables
        "env-title": "API Keys & Integrations",
        "dash-env-sub": "Configure keys for LLM providers, databases, and connection credentials.",
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
        "env-placeholder-value": "Value...",
        
        // Social Connections (Integrations Grid)
        "channels-tab-title": "Social Channels Connection",
        "channels-tab-sub": "Link Zalo OA, Facebook Messenger, TikTok Shop, Shopee, and other endpoints via credentials or API tokens.",
        "chan-status-connected": "Active",
        "chan-status-disconnected": "Not connected",
        "chan-btn-connect": "CONNECT CHANNEL",
        "chan-btn-disconnect": "DISCONNECT",
        "chan-modal-title": "Configure Channel API Connection",
        "chan-modal-webhook-label": "Webhook URL (Incoming events)",
        "chan-modal-token-label": "Access Token / API connection Key",
        "chan-modal-id-label": "Page ID / Shop ID / Group ID",
        "chan-btn-copy": "Copy",
        "chan-btn-save": "CONFIRM CONNECTION",

        // Inbox & Chat Console
        "chat-tab-all": "All",
        "chat-tab-zalo": "Zalo OA",
        "chat-tab-facebook": "Facebook Page/Msg",
        "chat-tab-tiktok": "TikTok Shop",
        "chat-tab-shopee": "Shopee / Lazada",
        "chat-tab-website": "Website Widget",
        "chat-autopilot-active": "AI active",
        "chat-autopilot-inactive": "Staff direct active",
        "chat-autopilot-toggle": "AI Autopilot Mode",
        "chat-input-placeholder": "Type response message... (Typing switches AI autopilot off automatically)",
        "chat-ai-suggestions": "AI SUGGESTED REPLIES",
        "chat-crm-details": "CRM CUSTOMER DOSSIER",
        "chat-crm-phone": "Phone number",
        "chat-crm-address": "Shipping address",
        "chat-crm-notes": "Order logs & notes",
        "chat-btn-takeover": "👤 Manual Takeover",
        "chat-btn-enable-ai": "🤖 Re-enable AI Autopilot",
        "chat-ai-suggest-badge": "AI suggest",
        "chat-active-threads": "Active conversations",

        // Team Management Page
        "team-title": "Team & Member Permissions",
        "team-sub": "Manage employee credentials, access roles, and custom page permissions.",
        "team-col-name": "TEAM MEMBER",
        "team-col-role": "SYSTEM ROLE",
        "team-col-status": "STATUS",
        "team-col-permissions": "PAGE PERMISSIONS",
        "team-col-action": "ACTIONS",
        "team-btn-add": "Add Team Member",
        "team-status-active": "Active",
        "team-status-inactive": "Locked",
        "team-modal-add-title": "Add New Team Member",
        "team-modal-label-name": "Staff Name",
        "team-modal-label-email": "Email Address",
        "team-modal-label-role": "System Role",
        "team-modal-label-permissions": "Detailed Permissions",
        "team-btn-save": "SAVE MEMBER",
        "team-perm-crm": "Manage CRM & Chat Console",
        "team-perm-api": "Modify API & Channel Settings",
        "team-perm-guides": "View Help Manuals & Guides",
        "team-perm-team": "Manage Team Members",
        "team-tab-roster": "Staff Permissions",
        "team-tab-owner": "Owner Profile & Voice AI Config",
        "owner-card-profile": "Profile & Business Logo",
        "owner-card-voice": "AI Voice & Hotline Setup",
        "owner-label-avatar": "Owner Avatar (Image/Video)",
        "owner-label-logo": "Brand Logo",
        "owner-label-voice-model": "AI Voice Model",
        "owner-label-voice-speed": "Speech Playback Rate",
        "owner-label-hotline": "Hotline Support Number",
        "owner-btn-save": "SAVE OWNER SETTINGS",

        // Floating Sales Bot
        "bot-greeting": "Hello! I am ChatbotPro's voice assistant. Please turn Voice Mode ON to hear my spoken answers! Ask me about our Starter, Standard, or Edition plans. Hotline: 0901.234.567",
        "bot-voice-on": "Voice Mode ON 🔊",
        "bot-voice-off": "Voice Mode OFF 🔇",
        "bot-placeholder": "Ask our sales bot...",
        "bot-socials-title": "Social media:",
        "bot-hotline-title": "Hotline support:"
    }
};

// 1. Inject common styles dynamically
function initCommonStyles() {
    const styleId = 'chatbotpro-common-styles';
    if (document.getElementById(styleId)) return;

    const styles = `
        .lang-active-indicator {
            background: linear-gradient(90deg, #6750a4 0%, #d97706 100%);
        }
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
        
        .access-denied-overlay {
            position: fixed;
            inset: 0;
            background: rgba(248, 250, 252, 0.9);
            backdrop-filter: blur(32px);
            -webkit-backdrop-filter: blur(32px);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .access-denied-visible {
            opacity: 1 !important;
        }

        /* Floating voice widget wave animation styles */
        .sound-wave {
            display: flex;
            align-items: center;
            gap: 2px;
            height: 20px;
        }
        .sound-wave span {
            display: block;
            width: 3px;
            height: 4px;
            background: #6750a4;
            border-radius: 2px;
            transition: height 0.15s ease;
        }
        .sound-wave.speaking span {
            animation: wave-rise 1s infinite alternate;
        }
        .sound-wave.speaking span:nth-child(2) { animation-delay: 0.15s; }
        .sound-wave.speaking span:nth-child(3) { animation-delay: 0.3s; }
        .sound-wave.speaking span:nth-child(4) { animation-delay: 0.45s; }
        .sound-wave.speaking span:nth-child(5) { animation-delay: 0.6s; }

        @keyframes wave-rise {
            0% { height: 4px; }
            100% { height: 18px; }
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
    document.documentElement.setAttribute('lang', lang === 'VIE' ? 'vi' : 'en');
    
    const dict = translations[lang] || translations.VIE;
    
    document.querySelectorAll('[data-translate]').forEach(el => {
        const key = el.getAttribute('data-translate');
        if (dict[key]) {
            el.innerHTML = dict[key];
        }
    });

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
    if (document.getElementById('language-selector-overlay')) return;

    const overlay = document.createElement('div');
    overlay.id = 'language-selector-overlay';
    overlay.className = 'fixed inset-0 z-[100] flex items-center justify-center bg-[#f8f9fc]/90 backdrop-blur-2xl opacity-0 pointer-events-none transition-all duration-300';
    
    let activeLang = localStorage.getItem('chatbotpro_lang') || 'VIE';

    const overlayContent = `
        <div class="relative w-full max-w-2xl px-6 py-12 text-center modal-scale">
            <button id="close-lang-selector" class="absolute top-0 right-6 text-on-surface-variant hover:text-primary transition-colors group">
                <span class="material-symbols-outlined text-[32px] group-hover:rotate-90 transition-transform duration-300">close</span>
            </button>
            <h2 class="font-display-lg text-headline-md bg-gradient-to-r from-primary to-tertiary bg-clip-text text-transparent font-bold mb-4">Chọn Ngôn Ngữ / Select Language</h2>
            <p class="font-body-lg text-body-sm text-on-surface-variant mb-12 max-w-md mx-auto">Chọn ngôn ngữ để cập nhật toàn bộ nội dung hệ thống.</p>
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

    document.body.addEventListener('click', (e) => {
        const langBtn = e.target.closest('[aria-label="language"]') || 
                        e.target.closest('.material-symbols-outlined')?.parentElement?.classList.contains('language') || 
                        (e.target.innerText === 'language' && e.target.classList.contains('material-symbols-outlined'));
        if (langBtn) {
            e.preventDefault();
            overlay.classList.add('modal-visible');
        }
    });

    document.getElementById('close-lang-selector').addEventListener('click', () => {
        overlay.classList.remove('modal-visible');
    });

    overlay.querySelectorAll('.lang-card').forEach(card => {
        card.addEventListener('click', () => {
            const selectedLang = card.getAttribute('data-lang');
            localStorage.setItem('chatbotpro_lang', selectedLang);
            
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
                translatePage();
                
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

    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) overlay.classList.remove('modal-visible');
    });
}

// 3. Lead Capture Modal Ingestion and Binding
function initLeadCaptureModal() {
    if (document.getElementById('lead-capture-modal')) return;

    const modal = document.createElement('div');
    modal.id = 'lead-capture-modal';
    modal.className = 'fixed inset-0 z-[90] flex items-center justify-center bg-[#050505]/30 backdrop-blur-sm opacity-0 pointer-events-none transition-all duration-300';
    
    const modalContent = `
        <div class="relative w-full max-w-2xl px-4 md:px-0 mx-auto modal-scale">
            <div class="bg-white/95 backdrop-blur-[40px] rounded-[24px] border border-outline-variant/30 shadow-[0_15px_50px_rgba(103,80,164,0.15)] overflow-hidden text-on-surface">
                <button id="close-lead-modal" aria-label="Close dialog" class="absolute top-6 right-6 text-on-surface-variant hover:text-primary transition-colors z-20 group">
                    <span class="material-symbols-outlined text-[24px] group-hover:rotate-90 transition-transform duration-300">close</span>
                </button>
                <div class="flex flex-col md:flex-row">
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
                    </div>
                    <div class="md:w-7/12 p-8 md:p-10 relative bg-white">
                        <div class="mb-6">
                            <h2 class="font-display-lg-mobile text-xl font-bold bg-gradient-to-r from-primary via-secondary to-tertiary bg-clip-text text-transparent mb-2" data-translate="modal-title">Mở Khóa Trợ Lý AI</h2>
                            <p class="font-body-sm text-body-sm text-on-surface-variant" data-translate="modal-subtitle">Nhận ngay tài liệu hướng dẫn tích hợp Zalo/Messenger chi tiết.</p>
                        </div>
                        <form id="lead-capture-form" class="space-y-4">
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-name" data-translate="modal-label-name">Họ và Tên</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[18px]">person</span>
                                    </span>
                                    <input class="w-full bg-surface-container border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-4 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors" id="modal-name" required placeholder="Jane Doe" type="text"/>
                                </div>
                            </div>
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-email" data-translate="modal-label-email">Email Doanh Nghiệp</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[18px]">mail</span>
                                    </span>
                                    <input class="w-full bg-surface-container border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-4 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors" id="modal-email" required placeholder="jane@company.com" type="email"/>
                                </div>
                            </div>
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
                                </div>
                            </div>
                            <div class="pt-2">
                                <button type="submit" class="w-full bg-gradient-to-r from-primary to-secondary hover:brightness-105 text-white font-label-caps text-label-caps py-3 px-6 rounded-lg transition-all shadow-[0_0_20px_rgba(103,80,164,0.1)] flex items-center justify-center space-x-2">
                                    <span data-translate="modal-btn-submit">Đăng Ký Nhận Hướng Dẫn</span>
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

    document.getElementById('close-lead-modal').addEventListener('click', () => {
        modal.classList.remove('modal-visible');
    });
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('modal-visible');
    });

    document.getElementById('lead-capture-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('modal-name').value;
        const email = document.getElementById('modal-email').value;
        modal.classList.remove('modal-visible');
        
        const lang = localStorage.getItem('chatbotpro_lang') || 'VIE';
        window.showToast(
            lang === 'VIE' ? `Đăng ký thành công cho ${name} (${email}).` : `Access requested successfully for ${name} (${email}).`,
            'success'
        );
        document.getElementById('lead-capture-form').reset();
    });

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
            translatePage();
            modal.classList.add('modal-visible');
        }
    });
}

// 4. Premium Toast Notification System
function initToastSystem() {
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.className = 'fixed bottom-6 right-6 z-[120] flex flex-col gap-3 max-w-md w-full px-4 sm:px-0';
        document.body.appendChild(toastContainer);
    }

    window.showToast = function(message, type = 'success', duration = 4000) {
        const toast = document.createElement('div');
        toast.className = 'luxury-toast rounded-xl overflow-hidden flex flex-col w-full';
        
        let borderClass = 'border-l-4 border-l-primary';
        let icon = 'check_circle';
        let iconColor = 'text-primary';
        
        if (type === 'success') {
            borderClass = 'border-l-4 border-l-[#10b981]';
            icon = 'verified';
            iconColor = 'text-[#10b981]';
        } else if (type === 'error') {
            borderClass = 'border-l-4 border-l-[#ef4444]';
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
        toast.offsetHeight;
        toast.classList.add('toast-show');

        toast.querySelector('.toast-close-btn').addEventListener('click', () => {
            toast.classList.remove('toast-show');
            setTimeout(() => toast.remove(), 400);
        });

        const progressBar = toast.querySelector('.toast-progress-bar');
        setTimeout(() => {
            if (progressBar) progressBar.style.width = '0%';
        }, 50);

        setTimeout(() => {
            if (toast.parentElement) {
                toast.classList.remove('toast-show');
                setTimeout(() => toast.remove(), 400);
            }
        }, duration);
    };
}

// 5. Global Link Handlers & Nav Active Synchronization
function initGlobalLinkHandlers() {
    const currentPath = window.location.pathname;
    const sidebarLinks = document.querySelectorAll('aside nav a, nav.desktop-nav a, nav ul a');
    if (sidebarLinks.length > 0) {
        sidebarLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href || href === '#' || href.startsWith('#')) return;
            const isMatch = currentPath.includes(href) || (currentPath.endsWith('/') && href === 'index.html');
            
            if (isMatch) {
                sidebarLinks.forEach(l => {
                    l.classList.remove('bg-primary/10', 'text-primary', 'border-r-2', 'border-primary', 'active');
                    l.classList.add('text-on-surface-variant');
                });
                link.classList.add('bg-primary/10', 'text-primary', 'border-r-2', 'border-primary', 'active');
                link.classList.remove('text-on-surface-variant');
            }
        });
    }

    document.body.addEventListener('click', (e) => {
        const loginBtn = e.target.closest('button');
        if (loginBtn && (loginBtn.textContent.trim().includes('LOGIN') || loginBtn.textContent.trim().includes('ĐĂNG NHẬP') || loginBtn.getAttribute('data-translate') === 'nav-login')) {
            e.preventDefault();
            window.location.href = 'dashboard.html';
        }
    });
}

// 6. Role Switcher & Dynamic SideNavBar Permissions
function initRoleSwitcher() {
    const isAdminPage = ['dashboard.html', 'env-vars.html', 'team.html', 'guides.html', 'tradingview.html'].some(p => window.location.pathname.includes(p));
    if (!isAdminPage) return;

    const headerContainer = document.querySelector('header .flex.items-center.gap-stack-md');
    if (!headerContainer) return;

    const existing = document.getElementById('role-switcher-container');
    if (existing) existing.remove();

    const roleContainer = document.createElement('div');
    roleContainer.id = 'role-switcher-container';
    roleContainer.className = 'relative ml-2';

    const currentRole = localStorage.getItem('chatbotpro_role') || 'owner';
    const roleTextKey = currentRole === 'owner' ? 'role-owner' : 'role-staff';

    roleContainer.innerHTML = `
        <button id="role-switcher-btn" class="flex items-center gap-2 px-4 py-2 bg-slate-50 border border-outline-variant/50 rounded-full hover:border-primary/50 hover:bg-white transition-all text-xs font-semibold text-on-surface-variant active:scale-95">
            <span class="material-symbols-outlined text-[18px]">admin_panel_settings</span>
            <span id="active-role-text" data-translate="${roleTextKey}">${currentRole === 'owner' ? 'Chủ Doanh Nghiệp' : 'Nhân Viên Trực'}</span>
            <span class="material-symbols-outlined text-[16px] transition-transform duration-200">expand_more</span>
        </button>
        <div id="role-switcher-dropdown" class="absolute right-0 mt-2 w-56 bg-white border border-outline-variant/30 rounded-xl shadow-lg opacity-0 pointer-events-none transition-all duration-200 z-50">
            <div class="p-2 flex flex-col gap-1">
                <button data-role="owner" class="role-opt-btn w-full text-left px-3 py-2.5 rounded-lg text-xs font-semibold hover:bg-primary/5 hover:text-primary transition-all flex items-center gap-2">
                    <span class="material-symbols-outlined text-[16px]">military_tech</span>
                    <span data-translate="role-owner">Chủ Doanh Nghiệp</span>
                </button>
                <button data-role="staff" class="role-opt-btn w-full text-left px-3 py-2.5 rounded-lg text-xs font-semibold hover:bg-primary/5 hover:text-primary transition-all flex items-center gap-2">
                    <span class="material-symbols-outlined text-[16px]">support_agent</span>
                    <span data-translate="role-staff">Nhân Viên Trực</span>
                </button>
            </div>
        </div>
    `;

    headerContainer.insertBefore(roleContainer, headerContainer.lastElementChild);

    const btn = document.getElementById('role-switcher-btn');
    const dropdown = document.getElementById('role-switcher-dropdown');

    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isClosed = dropdown.classList.contains('pointer-events-none');
        if (isClosed) {
            dropdown.classList.remove('opacity-0', 'pointer-events-none');
            btn.querySelector('.material-symbols-outlined:last-child').style.transform = 'rotate(180deg)';
        } else {
            dropdown.classList.add('opacity-0', 'pointer-events-none');
            btn.querySelector('.material-symbols-outlined:last-child').style.transform = 'rotate(0deg)';
        }
    });

    document.addEventListener('click', () => {
        dropdown.classList.add('opacity-0', 'pointer-events-none');
        btn.querySelector('.material-symbols-outlined:last-child').style.transform = 'rotate(0deg)';
    });

    dropdown.querySelectorAll('.role-opt-btn').forEach(opt => {
        opt.addEventListener('click', () => {
            const role = opt.getAttribute('data-role');
            localStorage.setItem('chatbotpro_role', role);
            
            const lang = localStorage.getItem('chatbotpro_lang') || 'VIE';
            const msg = role === 'owner' 
                ? (lang === 'VIE' ? 'Đã chuyển sang vai trò: Chủ Doanh Nghiệp' : 'Switched to Owner role') 
                : (lang === 'VIE' ? 'Đã chuyển sang vai trò: Nhân Viên Trực Chat' : 'Switched to Staff role');
            window.showToast(msg, 'info');

            applyRolePermissions();
            checkRoleAccess();
            translatePage();
        });
    });
}

function applyRolePermissions() {
    const currentRole = localStorage.getItem('chatbotpro_role') || 'owner';
    const textSpan = document.getElementById('active-role-text');
    if (textSpan) {
        textSpan.setAttribute('data-translate', currentRole === 'owner' ? 'role-owner' : 'role-staff');
    }

    document.querySelectorAll('[data-role-required="owner"]').forEach(el => {
        if (currentRole === 'owner') {
            el.style.display = '';
        } else {
            el.style.display = 'none';
        }
    });
}

function checkRoleAccess() {
    const currentRole = localStorage.getItem('chatbotpro_role') || 'owner';
    const currentPath = window.location.pathname;
    const isRestrictedPage = ['env-vars.html', 'team.html'].some(p => currentPath.includes(p));
    
    if (isRestrictedPage && currentRole === 'staff') {
        if (document.getElementById('access-denied-blocker')) return;

        const overlay = document.createElement('div');
        overlay.id = 'access-denied-blocker';
        overlay.className = 'access-denied-overlay';

        overlay.innerHTML = `
            <div class="glass-panel p-10 rounded-2xl max-w-lg w-full text-center border-l-4 border-l-[#ef4444] bg-white shadow-2xl relative overflow-hidden">
                <span class="material-symbols-outlined text-[#ef4444] text-[64px] mb-4">gavel</span>
                <h2 class="font-display-lg text-2xl font-bold text-on-surface mb-4" data-translate="role-access-denied-title">TRUY CẬP BỊ TỪ CHỐI</h2>
                <p class="font-body-sm text-body-sm text-on-surface-variant mb-8 leading-relaxed" data-translate="role-access-denied-desc">Bạn không có quyền truy cập trang cấu hình API hoặc phân quyền team.</p>
                <button onclick="window.location.href='dashboard.html'" class="btn-gradient w-full py-3 rounded-lg text-white font-label-caps text-label-caps font-bold active:scale-95 flex items-center justify-center gap-2">
                    <span class="material-symbols-outlined text-sm">hub</span>
                    <span data-translate="role-access-denied-btn">Quay lại Bảng CRM</span>
                </button>
            </div>
        `;

        document.body.appendChild(overlay);
        translatePage();
        
        overlay.offsetHeight;
        overlay.classList.add('access-denied-visible');
        document.body.style.overflow = 'hidden';

        setTimeout(() => {
            window.location.href = 'dashboard.html';
        }, 3000);
    } else {
        const blocker = document.getElementById('access-denied-blocker');
        if (blocker) {
            blocker.classList.remove('access-denied-visible');
            setTimeout(() => {
                blocker.remove();
                document.body.style.overflow = '';
            }, 300);
        }
    }
}

// 7. Floating Voice-Enabled Sales Chatbot Widget (NEW REQUIREMENT)
function initFloatingSalesBot() {
    if (document.getElementById('floating-sales-bot-root')) return;

    // Load configs from LocalStorage with fallback defaults
    const savedHotline = localStorage.getItem('chatbotpro_hotline') || '0901.234.567';
    const cleanHotline = savedHotline.replace(/\./g, '').trim();
    const savedZalo = localStorage.getItem('chatbotpro_zalo') || 'https://zalo.me/0901234567';
    const savedFb = localStorage.getItem('chatbotpro_fb') || 'https://m.me/chatbotpro';
    const savedYt = localStorage.getItem('chatbotpro_youtube') || 'https://youtube.com/chatbotpro';
    const savedTiktok = localStorage.getItem('chatbotpro_tiktok') || 'https://tiktok.com/@chatbotpro';
    
    // Avatar
    const savedAvatar = localStorage.getItem('chatbotpro_avatar') || 'https://lh3.googleusercontent.com/aida-public/AB6AXuCBIUDhUh4WJokbt6eaR39WWnllSy3R5Y2ubYoM-BXYHAwjzsVLJ7F-UFxq44aIjStlSz4yIerWvEkrAPrzw6z_cFBn7pvuFAveUQWde_R54XtdWFoAOtbfenopAKkMYinI9KbPkuMa-nlTrq9G2gzMewhy4la7j1XcgHYQtKBKga_mdkLyPzwBiZsVtofpmOMVKuyV9-Gz1kR-qSnedfV9f4m3BtsRFQitanKo4j4TlgSahv5oYZPfuAbw9umqPv5J90xX_nb7TEf4';
    const isVideoAvatar = savedAvatar.startsWith('data:video') || savedAvatar.includes('blob:') || savedAvatar.includes('.mp4');

    // Create wrapper element
    const widgetRoot = document.createElement('div');
    widgetRoot.id = 'floating-sales-bot-root';
    widgetRoot.className = 'fixed bottom-6 right-6 z-[90] flex flex-col items-end gap-3';
    
    // Injected button and chat panel
    widgetRoot.innerHTML = `
        <!-- Floating Toggle Button -->
        <button id="sales-bot-trigger" class="w-14 h-14 bg-gradient-to-r from-primary to-secondary text-white rounded-full shadow-[0_5px_25px_rgba(103,80,164,0.3)] hover:brightness-105 active:scale-95 transition-all duration-300 flex items-center justify-center relative border border-white/20">
            <span class="material-symbols-outlined text-[28px] animate-pulse">voice_chat</span>
            <span class="absolute -top-1 -right-1 w-3 h-3 bg-[#10b981] rounded-full border border-white"></span>
        </button>

        <!-- Glass Chat Panel -->
        <div id="sales-bot-panel" class="w-96 h-[530px] bg-white/95 backdrop-blur-[32px] border border-outline-variant/30 rounded-3xl shadow-[0_15px_50px_rgba(103,80,164,0.18)] flex flex-col overflow-hidden opacity-0 pointer-events-none translate-y-6 transition-all duration-300">
            <!-- Header -->
            <div class="px-5 py-4 border-b border-outline-variant/30 flex justify-between items-center bg-slate-50/50">
                <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-full bg-primary/10 border border-primary/20 flex items-center justify-center text-primary relative shrink-0 overflow-hidden">
                        ${isVideoAvatar 
                            ? `<video src="${savedAvatar}" autoplay loop muted playsinline class="w-full h-full object-cover"></video>` 
                            : `<img src="${savedAvatar}" class="w-full h-full object-cover" />`}
                        <span class="absolute bottom-0 right-0 w-2 h-2 bg-[#10b981] rounded-full border border-white"></span>
                    </div>
                    <div>
                        <h4 class="font-semibold text-xs text-on-surface">ChatbotPro Voice AI</h4>
                        <!-- Glowing Voice Waves -->
                        <div class="sound-wave mt-1" id="bot-voice-waves">
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                    </div>
                </div>
                <!-- Close Button -->
                <button id="close-sales-bot" class="text-on-surface-variant hover:text-on-surface transition-colors">
                    <span class="material-symbols-outlined text-[20px]">close</span>
                </button>
            </div>

            <!-- Voice Toggle & Contact bar -->
            <div class="px-5 py-2.5 border-b border-outline-variant/10 flex justify-between items-center bg-slate-50/20 text-[11px]">
                <button id="btn-toggle-bot-voice" class="px-3 py-1 bg-slate-100 hover:bg-slate-200 border border-outline-variant/40 rounded-full font-bold text-slate-700 flex items-center gap-1 active:scale-95 transition-all">
                    <span class="material-symbols-outlined text-[14px]">volume_off</span>
                    <span data-translate="bot-voice-off">Voice Mode OFF 🔇</span>
                </button>
                <div class="text-on-surface-variant">
                    <span data-translate="bot-hotline-title">Hotline:</span> 
                    <a href="tel:${cleanHotline}" class="font-bold text-primary hover:underline">${savedHotline}</a>
                </div>
            </div>

            <!-- Messages Stream -->
            <div class="flex-grow overflow-y-auto p-4 chat-scroll flex flex-col gap-3.5 bg-slate-50/20" id="sales-bot-stream">
                <!-- Initial Bot Message -->
                <div class="flex items-start gap-2.5 max-w-[85%]">
                    <div class="w-7 h-7 rounded-full bg-primary/10 border border-primary/20 flex items-center justify-center text-primary shrink-0 text-xs">
                        🤖
                    </div>
                    <div class="bg-slate-100 text-on-surface px-3.5 py-2 rounded-2xl rounded-tl-none text-[11.5px] leading-relaxed shadow-sm" id="bot-initial-bubble">
                        <!-- Loaded dynamically -->
                    </div>
                </div>
            </div>

            <!-- Quick Action Links -->
            <div class="px-4 py-2 bg-slate-50/80 border-t border-outline-variant/20 flex gap-2 overflow-x-auto text-[10px] shrink-0 select-none">
                <a href="${savedZalo}" target="_blank" class="px-2.5 py-1.5 bg-primary/10 text-primary border border-primary/20 rounded-lg font-bold shrink-0 flex items-center gap-1 active:scale-95 transition-all">
                    <span class="material-symbols-outlined text-xs">chat</span> Zalo OA
                </a>
                <a href="${savedFb}" target="_blank" class="px-2.5 py-1.5 bg-[#1877f2]/10 text-[#1877f2] border border-[#1877f2]/20 rounded-lg font-bold shrink-0 flex items-center gap-1 active:scale-95 transition-all">
                    <span class="material-symbols-outlined text-xs">forum</span> Messenger
                </a>
                <a href="${savedYt}" target="_blank" class="px-2.5 py-1.5 bg-red-600/10 text-red-600 border border-red-600/20 rounded-lg font-bold shrink-0 flex items-center gap-1 active:scale-95 transition-all">
                    <span class="material-symbols-outlined text-xs">video_library</span> YouTube
                </a>
                <a href="${savedTiktok}" target="_blank" class="px-2.5 py-1.5 bg-slate-900/10 text-slate-800 border border-slate-900/20 rounded-lg font-bold shrink-0 flex items-center gap-1 active:scale-95 transition-all">
                    <span class="material-symbols-outlined text-xs">music_note</span> TikTok
                </a>
                <a href="checkout.html" class="px-2.5 py-1.5 bg-amber-500/10 text-amber-600 border border-amber-500/20 rounded-lg font-bold shrink-0 flex items-center gap-1 active:scale-95 transition-all">
                    <span class="material-symbols-outlined text-xs">shopping_cart</span> Mua Gói
                </a>
            </div>

            <!-- Text Input Area -->
            <div class="p-3 border-t border-outline-variant/30 flex gap-2 bg-slate-50/50 shrink-0">
                <input class="flex-grow bg-white border border-outline-variant/40 rounded-xl px-3.5 py-2 text-xs focus:outline-none focus:border-primary placeholder:text-slate-400" id="sales-bot-input" data-translate-placeholder="bot-placeholder" placeholder="Hỏi bot bán hàng... (Bằng tiếng Việt)" type="text"/>
                <button id="btn-send-sales-bot" class="btn-gradient p-2.5 rounded-xl flex items-center justify-center active:scale-95 transition-all">
                    <span class="material-symbols-outlined text-[16px]">send</span>
                </button>
            </div>
        </div>
    `;

    document.body.appendChild(widgetRoot);

    const trigger = document.getElementById('sales-bot-trigger');
    const panel = document.getElementById('sales-bot-panel');
    const closeBtn = document.getElementById('close-sales-bot');
    const toggleVoiceBtn = document.getElementById('btn-toggle-bot-voice');
    const waves = document.getElementById('bot-voice-waves');
    
    const input = document.getElementById('sales-bot-input');
    const sendBtn = document.getElementById('btn-send-sales-bot');
    const stream = document.getElementById('sales-bot-stream');
    const initialBubble = document.getElementById('bot-initial-bubble');

    let voiceEnabled = false;

    // Set dynamic initial message
    const lang = localStorage.getItem('chatbotpro_lang') || 'VIE';
    const initialText = lang === 'VIE'
        ? `Chào bạn! Mình là Trợ lý Voice AI của ChatbotPro. Bật Giọng Nói để nghe mình phản hồi trực tiếp nhé! Bạn cần tư vấn gói Starter (550k/tháng), Standard (1.1M/tháng) hay Edition (2.75M/tháng)? Hotline: ${savedHotline}`
        : `Hello! I am ChatbotPro's voice assistant. Please turn Voice Mode ON to hear my spoken answers! Ask me about our Starter, Standard, or Edition plans. Hotline: ${savedHotline}`;
    initialBubble.textContent = initialText;

    // Trigger toggle
    trigger.addEventListener('click', () => {
        const isClosed = panel.classList.contains('pointer-events-none');
        if (isClosed) {
            panel.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-6');
            trigger.classList.add('scale-0');
            setTimeout(() => {
                if (voiceEnabled) speakText(initialText);
            }, 300);
        }
    });

    closeBtn.addEventListener('click', () => {
        panel.classList.add('opacity-0', 'pointer-events-none', 'translate-y-6');
        trigger.classList.remove('scale-0');
        window.speechSynthesis.cancel();
        waves.classList.remove('speaking');
    });

    // Voice mode toggling
    toggleVoiceBtn.addEventListener('click', () => {
        voiceEnabled = !voiceEnabled;
        const currentLang = localStorage.getItem('chatbotpro_lang') || 'VIE';
        if (voiceEnabled) {
            toggleVoiceBtn.innerHTML = `<span class="material-symbols-outlined text-[14px]">volume_up</span> <span>${currentLang === 'VIE' ? 'Bật Giọng Nói Real-time 🔊' : 'Voice Mode ON 🔊'}</span>`;
            toggleVoiceBtn.className = 'px-3 py-1 bg-[#10b981]/15 border border-[#10b981]/30 rounded-full font-bold text-[#10b981] flex items-center gap-1 active:scale-95 transition-all';
            
            // Speak last bot message
            const botMessages = stream.querySelectorAll('.bg-slate-100');
            if (botMessages.length > 0) {
                const lastMsgText = botMessages[botMessages.length - 1].textContent.trim();
                speakText(lastMsgText);
            } else {
                speakText(initialText);
            }
        } else {
            toggleVoiceBtn.innerHTML = `<span class="material-symbols-outlined text-[14px]">volume_off</span> <span>${currentLang === 'VIE' ? 'Tắt Giọng Nói 🔇' : 'Voice Mode OFF 🔇'}</span>`;
            toggleVoiceBtn.className = 'px-3 py-1 bg-slate-100 hover:bg-slate-200 border border-outline-variant/40 rounded-full font-bold text-slate-700 flex items-center gap-1 active:scale-95 transition-all';
            window.speechSynthesis.cancel();
            waves.classList.remove('speaking');
        }
    });

    // Speech synthesis function
    function speakText(text) {
        if (!('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel(); // Stop current speech

        // Remove html/markdown and prepare phone number read out
        const spokenHotline = savedHotline.split('').map(c => c === '.' ? ', ' : c).join('');
        const cleanText = text
            .replace(/<[^>]*>/g, '')
            .replace(/hotline:?/i, 'hót lai')
            .replace(new RegExp(savedHotline.replace(/\./g, '\\.'), 'g'), spokenHotline);

        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = 'vi-VN';
        
        // Find best Vietnamese voice
        const voices = window.speechSynthesis.getVoices();
        const viVoice = voices.find(v => v.lang.includes('vi') || v.lang.includes('VI'));
        if (viVoice) utterance.voice = viVoice;

        // Load custom playback speed configured by the Owner
        const savedSpeed = parseFloat(localStorage.getItem('chatbotpro_voice_speed')) || 1.0;
        utterance.rate = savedSpeed;
        utterance.pitch = 1.05;

        utterance.onstart = () => {
            waves.classList.add('speaking');
        };

        utterance.onend = () => {
            waves.classList.remove('speaking');
        };

        utterance.onerror = () => {
            waves.classList.remove('speaking');
        };

        window.speechSynthesis.speak(utterance);
    }

    // Send logic
    function handleSend() {
        const text = input.value.trim();
        if (!text) return;

        // User message bubble
        const userBubble = document.createElement('div');
        userBubble.className = 'flex items-start gap-2.5 max-w-[85%] self-end flex-row-reverse';
        userBubble.innerHTML = `
            <div class="w-7 h-7 rounded-full bg-slate-100 flex items-center justify-center text-slate-600 shrink-0 text-xs font-semibold">
                👤
            </div>
            <div class="bg-primary/10 text-on-surface px-3.5 py-2 rounded-2xl rounded-tr-none text-[11.5px] leading-relaxed shadow-sm">
                ${text}
            </div>
        `;
        stream.appendChild(userBubble);
        input.value = '';
        stream.scrollTop = stream.scrollHeight;

        // Simulate chatbot reply
        setTimeout(() => {
            const currentLang = localStorage.getItem('chatbotpro_lang') || 'VIE';
            let botReply = '';
            
            const q = text.toLowerCase();
            if (q.includes('giá') || q.includes('gói') || q.includes('package') || q.includes('standard') || q.includes('starter') || q.includes('edition')) {
                botReply = currentLang === 'VIE'
                    ? 'Bên em có 3 gói: Starter (550k/tháng), Standard (1.1 triệu/tháng - khuyên dùng), và Edition (2.75 triệu/tháng). Có hỗ trợ thanh toán hàng năm và giảm giá 15% đấy ạ.'
                    : 'We offer 3 tiers: Starter (550k VND/mo), Standard (1.1M VND/mo - recommended), and Edition (2.75M VND/mo). Get 15% off on annual billing.';
            } else if (q.includes('hotline') || q.includes('sđt') || q.includes('liên hệ') || q.includes('contact') || q.includes('điện thoại') || q.includes('zalo')) {
                botReply = currentLang === 'VIE'
                    ? `Anh chị có thể kết nối ngay với tụi em qua Hotline/Zalo: ${savedHotline}. Tụi em trực hỗ trợ 24/7!`
                    : `Please reach us immediately via Hotline/Zalo: ${savedHotline}. We support you 24/7!`;
            } else if (q.includes('dữ liệu') || q.includes('nạp') || q.includes('file') || q.includes('pdf') || q.includes('website')) {
                botReply = currentLang === 'VIE'
                    ? 'ChatbotPro có thể tự động học thông tin từ các tệp PDF, DOCX, Excel XLSX hoặc trực tiếp từ website của bạn. Nạp tri thức chỉ mất 1-2 phút thôi.'
                    : 'ChatbotPro ingests and learns automatically from PDF, DOCX, XLSX files, or website URLs in under 2 minutes.';
            } else {
                botReply = currentLang === 'VIE'
                    ? `Cảm ơn câu hỏi của bạn. ChatbotPro là giải pháp AI trả lời tự động khách hàng dưới 5 giây trên Zalo OA, Messenger và Website. Bạn có muốn gọi hotline ${savedHotline} tư vấn trực tiếp không?`
                    : `Thank you. ChatbotPro is the premium multi-channel AI responder (Zalo, Messenger, Website) under 5 seconds. Connect to our Sales team via Zalo/Hotline: ${savedHotline}!`;
            }

            const botBubble = document.createElement('div');
            botBubble.className = 'flex items-start gap-2.5 max-w-[85%]';
            botBubble.innerHTML = `
                <div class="w-7 h-7 rounded-full bg-primary/10 border border-primary/20 flex items-center justify-center text-primary shrink-0 text-xs">
                    🤖
                </div>
                <div class="bg-slate-100 text-on-surface px-3.5 py-2 rounded-2xl rounded-tl-none text-[11.5px] leading-relaxed shadow-sm">
                    ${botReply}
                </div>
            `;
            stream.appendChild(botBubble);
            stream.scrollTop = stream.scrollHeight;

            if (voiceEnabled) speakText(botReply);
        }, 1000);
    }

    sendBtn.addEventListener('click', handleSend);
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') handleSend();
    });
}

