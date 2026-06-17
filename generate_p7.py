import os

LAYOUT_JS = '''
const NAV_GROUPS = [
    {
        title: 'CỐT LÕI (NHÓM B & C)',
        items: [
            { id: 'dashboard', icon: 'dashboard', label: 'Dashboard & Inbox', role: 'all' },
            { id: 'bot_builder', icon: 'smart_toy', label: 'Flow Builder & RAG', role: 'admin' },
            { id: 'campaigns', icon: 'campaign', label: 'Chiến Dịch & Mẫu', role: 'all' }
        ]
    },
    {
        title: 'VẬN HÀNH BÁN HÀNG',
        items: [
            { id: 'channels', icon: 'hub', label: 'Quản Lý Kênh', role: 'admin' },
            { id: 'ecommerce', icon: 'shopping_cart', label: 'Sản Phẩm & Đơn', role: 'all' },
            { id: 'crm', icon: 'group', label: 'CRM Khách Hàng', role: 'all' },
            { id: 'content', icon: 'article', label: 'Nội Dung & Banner', role: 'all' }
        ]
    },
    {
        title: 'CÀI ĐẶT DOANH NGHIỆP',
        items: [
            { id: 'team_management', icon: 'admin_panel_settings', label: 'Phân Quyền Team', role: 'admin' },
            { id: 'tenant_settings', icon: 'settings', label: 'Thiết Lập Tenant', role: 'admin' },
            { id: 'analytics', icon: 'insert_chart', label: 'Báo Cáo Phân Tích', role: 'all' }
        ]
    },
    {
        title: 'HỆ THỐNG',
        items: [
            { id: 'affiliate', icon: 'diversity_3', label: 'Affiliate & CTV', role: 'admin' },
            { id: 'support', icon: 'help_clinic', label: 'Hỗ Trợ 24/7', role: 'all' },
            { id: 'admin_panel', icon: 'local_police', label: 'Super Admin', role: 'super_admin' }
        ]
    }
];

function renderLayout(activeId, contentHtml) {
    const root = document.getElementById('root');
    const role = 'super_admin'; 
    
    let navHtml = '';
    NAV_GROUPS.forEach(group => {
        const visibleItems = group.items.filter(item => {
            if (role === 'super_admin') return true;
            if (role === 'admin' && item.role !== 'super_admin') return true;
            return item.role === 'all';
        });

        if (visibleItems.length > 0) {
            navHtml += `
                <div class="mt-6 mb-2 px-6 hidden md:block">
                    <span class="text-[11px] font-black text-slate-500 uppercase tracking-widest">${group.title}</span>
                </div>
            `;
            visibleItems.forEach(item => {
                navHtml += `
                    <a href="${item.id}.html" class="flex items-center gap-4 px-6 py-3 transition-all ${item.id === activeId ? 'text-[#10B981] bg-white/5 border-l-4 border-[#10B981]' : 'text-slate-400 hover:text-white hover:bg-white/5'}">
                        <span class="material-symbols-outlined text-[22px]">${item.icon}</span>
                        <span class="font-bold text-[15px] hidden md:block">${item.label}</span>
                    </a>
                `;
            });
        }
    });

    root.innerHTML = `
        <div class="flex h-screen bg-[#0A0A0A] text-white font-body overflow-hidden" 
             x-data="globalState()" 
             @show-toast.window="addToast($event.detail.msg, $event.detail.type)">
            
            <!-- Sidebar -->
            <div class="w-20 md:w-72 bg-[#121214] border-r border-white/5 flex flex-col transition-all duration-300 z-20">
                <div class="h-[72px] flex items-center justify-center md:justify-start md:px-6 border-b border-white/5 shrink-0">
                    <div class="w-8 h-8 rounded bg-gradient-to-br from-[#10B981] to-[#00F0FF] flex items-center justify-center font-bold text-black font-display shadow-[0_0_15px_rgba(16,185,129,0.5)]">CN</div>
                    <span class="ml-3 font-display font-black tracking-widest bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400 hidden md:block text-lg">CHỐT NGHÌN ĐƠN</span>
                </div>
                <div class="flex-1 overflow-y-auto custom-scrollbar py-4">
                    ${navHtml}
                </div>
                <div class="p-4 border-t border-white/5 flex items-center gap-3 shrink-0 bg-[#0A0A0A]/50">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-r from-[#7B2DFF] to-[#00F0FF] flex items-center justify-center font-bold">TC</div>
                    <div class="hidden md:block">
                        <div class="text-sm font-bold">Thiên CR7</div>
                        <div class="text-[11px] font-bold text-[#FFD700] uppercase tracking-wider">Super Admin</div>
                    </div>
                </div>
            </div>

            <!-- Main Content -->
            <div class="flex-1 flex flex-col h-screen overflow-hidden relative">
                <!-- Header / Global Bell -->
                <header class="h-[72px] bg-[#121214]/80 backdrop-blur-md border-b border-white/5 flex items-center justify-between px-8 z-10 shrink-0">
                    <div class="font-bold text-lg hidden sm:block">Không gian làm việc</div>
                    
                    <div class="flex items-center gap-6">
                        <div class="relative cursor-pointer" @click="showNotif = !showNotif">
                            <span class="material-symbols-outlined text-slate-300 hover:text-white transition-colors text-3xl">notifications</span>
                            <span x-show="unreadCount > 0" style="display:none;" class="absolute 0 -right-1 w-5 h-5 bg-red-500 rounded-full flex items-center justify-center text-[10px] font-bold text-white shadow-[0_0_10px_rgba(239,68,68,0.8)] animate-pulse" x-text="unreadCount"></span>

                            <div x-show="showNotif" @click.outside="showNotif = false" style="display:none;" class="absolute right-0 top-12 w-80 bg-[#121214] border border-white/10 rounded-2xl shadow-2xl z-50 overflow-hidden">
                                <div class="p-4 border-b border-white/10 font-bold flex justify-between">
                                    <span>Thông Báo Đa Kênh</span>
                                    <span class="text-xs text-[#00F0FF] cursor-pointer" @click="unreadCount = 0; notifications = []">Đọc tất cả</span>
                                </div>
                                <div class="max-h-80 overflow-y-auto custom-scrollbar">
                                    <template x-for="n in notifications" :key="n.id">
                                        <div class="p-4 border-b border-white/5 hover:bg-white/5 flex gap-3 text-sm">
                                            <div class="w-8 h-8 rounded-full flex items-center justify-center text-white shrink-0" :class="n.platform === 'Tiktok' ? 'bg-black border border-white/20' : (n.platform==='Shopee' ? 'bg-[#EE4D2D]' : 'bg-blue-500')">
                                                <span class="material-symbols-outlined text-[16px]" x-text="n.icon"></span>
                                            </div>
                                            <div>
                                                <div class="font-bold text-white text-[13px]" x-text="n.title"></div>
                                                <div class="text-xs text-slate-400 mt-1 line-clamp-2" x-text="n.message"></div>
                                                <div class="text-[10px] text-slate-500 mt-2" x-text="n.time"></div>
                                            </div>
                                        </div>
                                    </template>
                                    <div x-show="notifications.length === 0" class="p-8 text-center text-slate-500 text-sm">Không có thông báo mới</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </header>

                <main class="flex-1 overflow-y-auto p-4 md:p-8 custom-scrollbar bg-[#0A0A0A]">
                    ${contentHtml}
                </main>

                <!-- GLOBAL TOAST CONTAINER -->
                <div class="fixed bottom-6 right-6 z-[100] flex flex-col gap-2">
                    <template x-for="toast in toasts" :key="toast.id">
                        <div x-show="toast.show" x-transition.opacity.duration.300ms class="px-6 py-3 rounded-xl shadow-2xl flex items-center gap-3 border border-white/10 font-bold text-sm"
                             :class="toast.type === 'success' ? 'bg-[#10B981] text-black shadow-[0_0_20px_rgba(16,185,129,0.3)]' : 'bg-[#FFD700] text-black shadow-[0_0_20px_rgba(255,215,0,0.3)]'">
                            <span class="material-symbols-outlined" x-text="toast.type === 'success' ? 'check_circle' : 'info'"></span>
                            <span x-text="toast.msg"></span>
                        </div>
                    </template>
                </div>

            </div>
        </div>
        
        <script>
            document.addEventListener('alpine:init', () => {
                Alpine.data('globalState', () => ({
                    toasts: [],
                    toastCounter: 0,
                    showNotif: false,
                    unreadCount: 0,
                    notifications: [],
                    
                    init() {
                        setInterval(() => {
                            if(!this.showNotif && Math.random() > 0.6) {
                                this.triggerNewMessage();
                            }
                        }, 6000);
                    },

                    triggerNewMessage() {
                        const platforms = [
                            {p: 'Tiktok', i: 'shopping_bag', title: 'Tin nhắn mới từ Tiktok Shop'},
                            {p: 'Shopee', i: 'local_mall', title: 'Đơn hàng mới trên Shopee'},
                            {p: 'Facebook', i: 'forum', title: 'Bình luận mới trên Fanpage'}
                        ];
                        const rand = platforms[Math.floor(Math.random() * platforms.length)];
                        
                        this.unreadCount++;
                        this.notifications.unshift({
                            id: Date.now(),
                            platform: rand.p,
                            icon: rand.i,
                            title: rand.title,
                            message: 'Khách hàng vừa gửi 1 yêu cầu cần hỗ trợ ngay. Hãy kiểm tra Inbox.',
                            time: 'Vừa xong'
                        });
                        
                        this.addToast('🔔 ' + rand.title, 'warning');
                    },

                    addToast(msg, type = 'success') {
                        const id = ++this.toastCounter;
                        this.toasts.push({ id, msg, type, show: true });
                        setTimeout(() => {
                            const toast = this.toasts.find(t => t.id === id);
                            if(toast) toast.show = false;
                        }, 3000);
                        setTimeout(() => {
                            this.toasts = this.toasts.filter(t => t.id !== id);
                        }, 3500);
                    }
                }));
            });
        </script>
    `;
}
'''

INDEX_HTML = '''<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>CHỐT NGHÌN ĐƠN - X10 Doanh Số Từ AI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { "primary": "#10B981", "secondary": "#7B2DFF", "tertiary": "#FFD700", "accent": "#00F0FF", "background": "#0A0A0A", "surface": "#121214" },
                    fontFamily: { "display": ["Plus Jakarta Sans", "sans-serif"], "body": ["Inter", "sans-serif"] }
                }
            }
        }
    </script>
</head>
<body class="bg-[#0A0A0A] text-white font-body overflow-x-hidden selection:bg-[#10B981] selection:text-black">
    <!-- Navbar -->
    <nav class="fixed w-full z-50 top-0 transition-all duration-300 bg-[#0A0A0A]/80 backdrop-blur-lg border-b border-white/10">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-[#10B981] to-[#00F0FF] flex items-center justify-center font-bold text-black font-display text-xl shadow-[0_0_20px_rgba(16,185,129,0.4)]">CN</div>
                <span class="font-display font-black tracking-widest text-xl">CHỐT NGHÌN ĐƠN</span>
            </div>
            <div class="hidden md:flex gap-8 text-sm font-bold text-slate-300">
                <a href="#features" class="hover:text-white transition-colors">Tính năng</a>
                <a href="#pricing" class="hover:text-white transition-colors text-[#00F0FF]">Bảng giá</a>
                <a href="#" class="hover:text-white transition-colors">Đối tác</a>
            </div>
            <div class="flex gap-4">
                <a href="dashboard.html" class="px-6 py-2.5 rounded-full border border-white/20 text-sm font-bold hover:bg-white/5 transition-colors">Đăng Nhập</a>
                <a href="#pricing" class="px-6 py-2.5 rounded-full bg-[#10B981] text-black text-sm font-bold hover:bg-emerald-400 transition-colors shadow-[0_0_20px_rgba(16,185,129,0.3)]">Dùng Thử Miễn Phí</a>
            </div>
        </div>
    </nav>

    <!-- Hero -->
    <section class="pt-40 pb-20 px-6 relative">
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-[#10B981]/20 blur-[120px] rounded-full pointer-events-none"></div>
        <div class="max-w-4xl mx-auto text-center relative z-10">
            <div class="inline-block px-4 py-1.5 rounded-full border border-[#00F0FF]/30 bg-[#00F0FF]/10 text-[#00F0FF] text-xs font-bold uppercase tracking-widest mb-6">Omnichannel AI Chatbot</div>
            <h1 class="text-5xl md:text-7xl font-display font-black leading-tight mb-8">
                GIÚP CHO 10,000 CHỦ DOANH NGHIỆP <br/>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#10B981] via-[#00F0FF] to-[#7B2DFF]">X10 DOANH SỐ TỪ AI</span>
            </h1>
            <p class="text-xl text-slate-400 mb-10 max-w-2xl mx-auto leading-relaxed">
                Hệ thống tự động hóa tư vấn, chốt đơn, và chăm sóc khách hàng đa nền tảng (Tiktok, Shopee, Facebook, Zalo) bằng sức mạnh của AI RAG.
            </p>
            <div class="flex justify-center gap-4">
                <a href="#pricing" class="px-8 py-4 rounded-full bg-white text-black text-lg font-black hover:bg-slate-200 transition-colors">Bắt đầu dùng thử Free</a>
                <a href="#features" class="px-8 py-4 rounded-full border border-white/20 text-lg font-bold hover:bg-white/5 transition-colors flex items-center gap-2">Tìm hiểu thêm <span class="material-symbols-outlined">arrow_downward</span></a>
            </div>
        </div>
    </section>

    <!-- Pricing (The requested section outside dashboard) -->
    <section id="pricing" class="py-24 px-6 bg-[#121214] border-t border-white/5">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-4xl font-display font-black mb-4">Gói Thanh Toán Siêu Thông Minh</h2>
                <p class="text-slate-400">Chọn giải pháp phù hợp nhất để bứt phá doanh thu cho doanh nghiệp của bạn.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Free Trial -->
                <div class="p-8 rounded-3xl bg-[#0A0A0A] border border-white/10 relative hover:border-[#10B981]/50 transition-colors">
                    <h3 class="text-xl font-bold mb-2">GÓI MIỄN PHÍ TRẢI NGHIỆM</h3>
                    <div class="text-5xl font-black mb-2">$0</div>
                    <p class="text-sm text-slate-400 mb-8">Dùng thử 7 ngày đẩy đủ tính năng</p>
                    <ul class="space-y-4 mb-8 text-sm">
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#10B981]">check_circle</span> Giới hạn 100 tin nhắn AI</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#10B981]">check_circle</span> Kết nối 1 Fanpage / 1 Tiktok</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#10B981]">check_circle</span> 1 Nhân viên quản lý</li>
                    </ul>
                    <a href="dashboard.html" class="block w-full py-3 text-center border border-white/20 rounded-xl font-bold hover:bg-white/10 transition-colors">Bắt Đầu Trải Nghiệm</a>
                </div>

                <!-- Pro -->
                <div class="p-8 rounded-3xl bg-gradient-to-b from-[#121214] to-[#0A0A0A] border border-[#00F0FF]/50 relative transform md:-translate-y-4 shadow-[0_0_50px_rgba(0,240,255,0.15)]">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#00F0FF] text-black px-4 py-1 rounded-full text-xs font-black uppercase tracking-widest">Phổ Biến Nhất</div>
                    <h3 class="text-xl font-bold mb-2 text-[#00F0FF]">GÓI PRO (CHUYÊN NGHIỆP)</h3>
                    <div class="text-5xl font-black mb-2">$99 <span class="text-lg text-slate-500 font-normal">/ tháng</span></div>
                    <p class="text-sm text-slate-400 mb-8">Dành cho Shop chạy Ads, Live Stream</p>
                    <ul class="space-y-4 mb-8 text-sm">
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#00F0FF]">check_circle</span> 10,000 tin nhắn AI / tháng</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#00F0FF]">check_circle</span> Không giới hạn kênh kết nối</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#00F0FF]">check_circle</span> Đào tạo AI bằng file PDF/DOCX (RAG)</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#00F0FF]">check_circle</span> Không giới hạn nhân viên</li>
                    </ul>
                    <a href="dashboard.html" class="block w-full py-3 text-center bg-[#00F0FF] text-black rounded-xl font-bold hover:bg-cyan-400 transition-colors shadow-[0_0_20px_rgba(0,240,255,0.3)]">Nâng Cấp Ngay</a>
                </div>

                <!-- Enterprise -->
                <div class="p-8 rounded-3xl bg-[#0A0A0A] border border-[#FFD700]/30 relative hover:border-[#FFD700]/50 transition-colors">
                    <h3 class="text-xl font-bold mb-2 text-[#FFD700]">GÓI ENTERPRISE (TẬP ĐOÀN)</h3>
                    <div class="text-5xl font-black mb-2">$500+ <span class="text-lg text-slate-500 font-normal">/ tháng</span></div>
                    <p class="text-sm text-slate-400 mb-8">Hệ thống AI riêng biệt, bảo mật tuyệt đối</p>
                    <ul class="space-y-4 mb-8 text-sm">
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#FFD700]">check_circle</span> Không giới hạn tin nhắn</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#FFD700]">check_circle</span> Tùy chỉnh LLM & Server Riêng</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#FFD700]">check_circle</span> White-label (Xóa logo)</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-[#FFD700]">check_circle</span> Hỗ trợ kỹ thuật 24/7 trực tiếp</li>
                    </ul>
                    <a href="dashboard.html" class="block w-full py-3 text-center bg-[#FFD700] text-black rounded-xl font-bold hover:bg-yellow-400 transition-colors">Liên Hệ Sales</a>
                </div>
            </div>
        </div>
    </section>
</body>
</html>
'''

CAMPAIGNS_HTML = '''
        <div x-data="{
            simulateAction(msg) {
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } }));
            }
        }">
            <div class="flex justify-between items-center mb-8">
                <h2 class="text-2xl font-bold font-display tracking-tight">Chiến Dịch & Mẫu Tin Nhắn</h2>
                <button @click="simulateAction('Đang tạo chiến dịch Broadcast mới...')" class="px-6 py-2.5 bg-[#10B981] text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.3)]">
                    <span class="material-symbols-outlined">campaign</span> Tạo Chiến Dịch Gửi Loạt
                </button>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <!-- Danh sách chiến dịch -->
                <div class="lg:col-span-2 space-y-4">
                    <div class="bg-[#121214] border border-white/5 p-6 rounded-2xl flex justify-between items-center group hover:border-[#00F0FF]/30 transition-all">
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 rounded-full bg-[#00F0FF]/10 text-[#00F0FF] flex items-center justify-center">
                                <span class="material-symbols-outlined">send</span>
                            </div>
                            <div>
                                <h3 class="font-bold text-lg">Sale Cuối Tuần Tháng 10</h3>
                                <div class="text-xs text-slate-400 mt-1 flex gap-4">
                                    <span>Gửi qua: Facebook, Zalo</span>
                                    <span>Đối tượng: Khách đã mua hàng</span>
                                </div>
                            </div>
                        </div>
                        <div class="text-right">
                            <div class="text-xs text-green-400 bg-green-500/20 px-2 py-1 rounded border border-green-500/30 inline-block mb-1">Đã Hoàn Thành</div>
                            <div class="font-bold text-sm">Đã gửi: 2,504</div>
                        </div>
                    </div>
                    
                    <div class="bg-[#121214] border border-white/5 p-6 rounded-2xl flex justify-between items-center group hover:border-[#10B981]/30 transition-all">
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 rounded-full bg-[#10B981]/10 text-[#10B981] flex items-center justify-center">
                                <span class="material-symbols-outlined animate-pulse">schedule</span>
                            </div>
                            <div>
                                <h3 class="font-bold text-lg">Chúc Mừng Sinh Nhật Tháng 11</h3>
                                <div class="text-xs text-slate-400 mt-1 flex gap-4">
                                    <span>Gửi qua: Zalo ZNS</span>
                                    <span>Đối tượng: Khách sinh nhật T11</span>
                                </div>
                            </div>
                        </div>
                        <div class="text-right">
                            <div class="text-xs text-[#FFD700] bg-[#FFD700]/10 px-2 py-1 rounded border border-[#FFD700]/30 inline-block mb-1">Đang Lên Lịch</div>
                            <div class="font-bold text-sm">Dự kiến: 150 người</div>
                        </div>
                    </div>
                </div>

                <!-- Mẫu tin nhắn (Templates) -->
                <div class="bg-[#121214] border border-white/5 rounded-2xl p-6">
                    <h3 class="font-bold mb-4 flex items-center gap-2"><span class="material-symbols-outlined text-[#FFD700]">library_books</span> Kho Mẫu Tin Nhắn (ZNS/FB)</h3>
                    <div class="space-y-4">
                        <div class="p-4 bg-[#0A0A0A] border border-white/5 rounded-xl">
                            <div class="flex justify-between items-center mb-2">
                                <span class="text-xs font-bold text-[#EE4D2D]">Mẫu Đánh Giá Shopee</span>
                                <button class="text-slate-500 hover:text-white"><span class="material-symbols-outlined text-[16px]">edit</span></button>
                            </div>
                            <p class="text-xs text-slate-400">"Cảm ơn {name} đã mua hàng tại {shop}. Xin đánh giá 5 sao để nhận xu nhé!"</p>
                        </div>
                        <div class="p-4 bg-[#0A0A0A] border border-white/5 rounded-xl">
                            <div class="flex justify-between items-center mb-2">
                                <span class="text-xs font-bold text-blue-400">Zalo ZNS Xóa Giỏ Hàng</span>
                                <button class="text-slate-500 hover:text-white"><span class="material-symbols-outlined text-[16px]">edit</span></button>
                            </div>
                            <p class="text-xs text-slate-400">"Bạn ơi, sản phẩm {product} trong giỏ hàng sắp hết. Quay lại chốt đơn ngay nào!"</p>
                        </div>
                        <button @click="simulateAction('Mở giao diện tạo Mẫu Zalo ZNS mới')" class="w-full py-2 border border-white/10 rounded-xl text-xs font-bold hover:bg-white/5">+ Thêm Mẫu Mới</button>
                    </div>
                </div>
            </div>
        </div>
'''

FILES = [
    ('js/layout.js', LAYOUT_JS),
    ('index.html', INDEX_HTML),
]

HTML_PAGES = [
    ('campaigns.html', 'campaigns', CAMPAIGNS_HTML),
]

# Write standalone files
for file_path, content in FILES:
    with open(file_path, 'w') as f:
        f.write(content.strip())

# Write wrapped HTML pages
TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>CHỐT NGHÌN ĐƠN</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { "primary": "#10B981", "secondary": "#7B2DFF", "tertiary": "#FFD700", "accent": "#00F0FF", "background": "#0A0A0A", "surface": "#121214" },
                    fontFamily: { "display": ["Plus Jakarta Sans", "sans-serif"], "body": ["Inter", "sans-serif"] }
                }
            }
        }
    </script>
</head>
<body>
    <div id="root"></div>
    <script src="js/layout.js"></script>
    <script>
        const content = `{CONTENT}`;
        document.addEventListener('DOMContentLoaded', () => {
            renderLayout('{ID}', content);
        });
    </script>
</body>
</html>'''

for html_file, page_id, content in HTML_PAGES:
    escaped_content = content.replace("`", "\\`").replace("${", "\\${")
    final_html = TEMPLATE.replace('{CONTENT}', escaped_content).replace('{ID}', page_id)
    with open(html_file, 'w') as f:
        f.write(final_html)

print("Đã hoàn thành P7: Trang Chủ (Pricing) và Cấu trúc Sidebar chuẩn Group.")
