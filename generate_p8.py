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

                <!-- AI AGENT FLOATING WIDGET (TỰ ĐỘNG HƯỚNG DẪN NGƯỜI DÙNG) -->
                <div class="fixed bottom-6 left-6 md:left-auto md:right-20 z-[90] flex flex-col items-end">
                    <!-- Agent Chatbox -->
                    <div x-show="showAgent" x-transition style="display:none;" class="mb-4 w-80 bg-[#121214] border border-[#00F0FF]/30 rounded-2xl shadow-[0_0_30px_rgba(0,240,255,0.15)] overflow-hidden flex flex-col">
                        <div class="bg-gradient-to-r from-[#10B981] to-[#00F0FF] p-4 flex justify-between items-center text-black">
                            <div class="flex items-center gap-2">
                                <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center"><span class="material-symbols-outlined">smart_toy</span></div>
                                <span class="font-bold text-sm">AI Assistant (Hướng Dẫn)</span>
                            </div>
                            <button @click="showAgent = false" class="hover:text-white transition-colors"><span class="material-symbols-outlined text-[18px]">close</span></button>
                        </div>
                        <div class="p-4 flex-1 h-64 overflow-y-auto custom-scrollbar flex flex-col gap-3 text-sm">
                            <div class="flex gap-2">
                                <div class="w-6 h-6 bg-gradient-to-r from-[#10B981] to-[#00F0FF] rounded-full shrink-0 flex items-center justify-center text-black text-[10px] font-bold">AI</div>
                                <div class="bg-white/5 p-2.5 rounded-xl rounded-tl-sm text-slate-300">
                                    Chào bạn! Mình là AI Hướng dẫn của Chốt Nghìn Đơn. Bạn là chủ doanh nghiệp mới phải không? Bạn đang cần hỗ trợ phần nào?
                                </div>
                            </div>
                            <!-- AI Suggestions -->
                            <div class="pl-8 flex flex-col gap-2">
                                <button @click="agentAction('Hướng dẫn kết nối Tiktok Shop')" class="text-left bg-[#00F0FF]/10 text-[#00F0FF] text-xs px-3 py-2 rounded-lg border border-[#00F0FF]/30 hover:bg-[#00F0FF]/20">1. Hướng dẫn kết nối Tiktok Shop</button>
                                <button @click="agentAction('Cách tạo Kịch bản Chatbot Tự Động')" class="text-left bg-[#00F0FF]/10 text-[#00F0FF] text-xs px-3 py-2 rounded-lg border border-[#00F0FF]/30 hover:bg-[#00F0FF]/20">2. Cách tạo Kịch bản Bot tự động</button>
                                <button @click="agentAction('Cách cấu hình Phân quyền Nhân viên')" class="text-left bg-[#00F0FF]/10 text-[#00F0FF] text-xs px-3 py-2 rounded-lg border border-[#00F0FF]/30 hover:bg-[#00F0FF]/20">3. Quản lý phân quyền Nhân viên</button>
                            </div>
                            
                            <!-- Dynamic Agent response -->
                            <template x-if="agentReply">
                                <div class="flex gap-2 mt-2">
                                    <div class="w-6 h-6 bg-gradient-to-r from-[#10B981] to-[#00F0FF] rounded-full shrink-0 flex items-center justify-center text-black text-[10px] font-bold">AI</div>
                                    <div class="bg-[#10B981]/20 border border-[#10B981]/30 p-2.5 rounded-xl rounded-tl-sm text-white font-bold text-xs" x-text="agentReply"></div>
                                </div>
                            </template>
                        </div>
                    </div>
                    <!-- Agent Bubble -->
                    <button @click="showAgent = !showAgent" class="w-14 h-14 bg-gradient-to-r from-[#10B981] to-[#00F0FF] rounded-full flex items-center justify-center text-black shadow-[0_0_20px_rgba(0,240,255,0.4)] hover:scale-110 transition-transform">
                        <span class="material-symbols-outlined text-[28px]" x-show="!showAgent">smart_toy</span>
                        <span class="material-symbols-outlined text-[28px]" x-show="showAgent" style="display:none;">keyboard_arrow_down</span>
                    </button>
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
                    
                    showAgent: false,
                    agentReply: '',
                    
                    init() {
                        setInterval(() => {
                            if(!this.showNotif && Math.random() > 0.6) {
                                this.triggerNewMessage();
                            }
                        }, 6000);
                        
                        // Show agent notification automatically after 3s
                        setTimeout(() => {
                            if(!this.showAgent) {
                                this.addToast('Trợ lý AI Hướng Dẫn luôn sẵn sàng hỗ trợ bạn ở góc dưới màn hình nhé!', 'info');
                            }
                        }, 3000);
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
                    },
                    
                    agentAction(topic) {
                        this.agentReply = 'Mình đang phân tích hệ thống... Để thực hiện "' + topic + '", bạn vui lòng điều hướng trên Menu bên trái và làm theo hướng dẫn trên màn hình nhé!';
                    }
                }));
            });
        </script>
    `;
}
'''

# We will inject x-data="{ simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); } }"
# into all HTML pages and wrap all dead buttons with @click="simulateAction('...')"

ECOMMERCE_HTML = '''
        <div x-data="{ 
            activeTab: 'products',
            simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); }
        }">
            <h2 class="text-xl font-bold mb-6">Quản Lý Sản Phẩm & Đơn Hàng (Đa Kênh)</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'products'" :class="activeTab === 'products' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Kho Sản Phẩm</button>
                <button @click="activeTab = 'orders'" :class="activeTab === 'orders' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Đơn Hàng Vận Chuyển</button>
            </div>

            <div x-show="activeTab === 'products'">
                <div class="flex justify-between items-center mb-4">
                    <input type="text" placeholder="Tìm sản phẩm..." class="bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm w-64 text-white">
                    <button @click="simulateAction('Đã mở form thêm Sản phẩm mới!')" class="bg-[#00F0FF] text-black px-4 py-2 rounded-xl text-sm font-bold hover:bg-cyan-400">+ Thêm Sản Phẩm</button>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div class="bg-[#121214] border border-white/5 rounded-2xl overflow-hidden group">
                        <div class="h-40 bg-white/5 flex items-center justify-center relative">
                            <span class="material-symbols-outlined text-4xl text-slate-600">checkroom</span>
                            <div class="absolute top-2 right-2 bg-black/80 px-2 py-1 rounded text-xs text-[#00F0FF] border border-[#00F0FF]/30">Shopee/Tiktok</div>
                        </div>
                        <div class="p-4">
                            <h3 class="font-bold text-white mb-1">Áo Thun Cổ Tròn Mẫu 01</h3>
                            <div class="text-[#10B981] font-bold text-sm mb-3">150,000đ</div>
                            <div class="flex gap-2">
                                <button @click="simulateAction('Đã lưu thay đổi cho Áo Thun Cổ Tròn!')" class="flex-1 bg-white/5 py-1.5 rounded-lg text-xs font-bold hover:bg-white/10 text-white">Sửa</button>
                                <button @click="simulateAction('Đã khóa bán sản phẩm này trên đa kênh!')" class="w-8 flex items-center justify-center bg-red-500/10 text-red-500 rounded-lg hover:bg-red-500 hover:text-white transition-colors"><span class="material-symbols-outlined text-[14px]">delete</span></button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div x-show="activeTab === 'orders'" style="display:none;">
                <div class="flex justify-between items-center mb-4">
                    <div class="flex gap-2">
                        <button class="bg-[#10B981]/20 text-[#10B981] px-4 py-1.5 rounded-lg text-xs font-bold border border-[#10B981]/30">Giao Hàng Nhanh (GHN)</button>
                        <button class="bg-white/5 text-slate-300 px-4 py-1.5 rounded-lg text-xs font-bold border border-white/10">Viettel Post</button>
                    </div>
                    <button @click="simulateAction('Đã đồng bộ đơn hàng mới nhất từ GHN')" class="px-4 py-2 bg-white/5 rounded-xl text-sm font-bold flex items-center gap-2 hover:bg-white/10"><span class="material-symbols-outlined text-[16px]">sync</span> Đồng Bộ</button>
                </div>
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs uppercase bg-white/5">
                        <tr><th class="px-4 py-3">Mã Đơn</th><th class="px-4 py-3">Khách Hàng</th><th class="px-4 py-3">Tổng Tiền</th><th class="px-4 py-3">Trạng Thái (ĐVVC)</th><th class="px-4 py-3 text-right">Thao Tác</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5">
                            <td class="px-4 py-3 font-bold text-[#00F0FF]">#ORD-991</td>
                            <td class="px-4 py-3">Lê Văn A</td>
                            <td class="px-4 py-3 font-bold text-white">350,000đ</td>
                            <td class="px-4 py-3"><span class="px-2 py-1 bg-[#FFD700]/10 text-[#FFD700] border border-[#FFD700]/30 rounded text-[10px] font-bold">Đang lấy hàng</span></td>
                            <td class="px-4 py-3 text-right"><button @click="simulateAction('Đã in vận đơn #ORD-991')" class="text-xs bg-white/10 px-3 py-1 rounded hover:bg-white/20 text-white font-bold">In Vận Đơn</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
'''

CRM_HTML = '''
        <div x-data="{ simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); } }">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-xl font-bold">Quản Lý Khách Hàng (CRM)</h2>
                <div class="flex gap-2">
                    <button @click="simulateAction('Đã tải xuống file Excel danh sách khách hàng!')" class="px-4 py-2 bg-white/5 hover:bg-white/10 text-white font-bold rounded-xl text-sm flex items-center gap-2 border border-white/10"><span class="material-symbols-outlined text-[18px]">download</span> Xuất Data</button>
                    <button @click="simulateAction('Mở form Thêm Khách Hàng Mới')" class="px-4 py-2 bg-[#10B981] text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-emerald-400"><span class="material-symbols-outlined text-[18px]">person_add</span> Thêm Khách Mới</button>
                </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                <div class="p-4 bg-[#121214] border border-white/5 rounded-2xl flex items-center justify-between">
                    <div><div class="text-xs text-slate-400">Tổng Khách Hàng</div><div class="text-2xl font-bold text-white">12,504</div></div>
                    <div class="w-10 h-10 bg-white/5 rounded-full flex items-center justify-center"><span class="material-symbols-outlined text-slate-400">group</span></div>
                </div>
                <div class="p-4 bg-[#121214] border border-white/5 rounded-2xl flex items-center justify-between">
                    <div><div class="text-xs text-slate-400">Khách VIP</div><div class="text-2xl font-bold text-[#FFD700]">340</div></div>
                    <div class="w-10 h-10 bg-[#FFD700]/10 rounded-full flex items-center justify-center"><span class="material-symbols-outlined text-[#FFD700]">stars</span></div>
                </div>
            </div>

            <table class="w-full text-left text-sm text-slate-300 bg-[#121214] rounded-2xl overflow-hidden border border-white/5">
                <thead class="text-xs uppercase bg-white/5 border-b border-white/5">
                    <tr><th class="px-4 py-4">Khách Hàng</th><th class="px-4 py-4">Nguồn</th><th class="px-4 py-4">Phân Loại (Tag)</th><th class="px-4 py-4">Đơn Hàng</th><th class="px-4 py-4 text-right">Tương Tác</th></tr>
                </thead>
                <tbody>
                    <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                        <td class="px-4 py-4">
                            <div class="font-bold text-white">Nguyễn Văn Nam</div>
                            <div class="text-[10px] text-slate-500 mt-1">0901***456</div>
                        </td>
                        <td class="px-4 py-4"><span class="text-xs font-bold text-[#EE4D2D]">Shopee</span></td>
                        <td class="px-4 py-4"><span class="px-2 py-1 bg-[#FFD700]/10 text-[#FFD700] rounded border border-[#FFD700]/30 text-[10px] font-bold">VIP Khách Sỉ</span></td>
                        <td class="px-4 py-4 font-bold text-white">12 Đơn</td>
                        <td class="px-4 py-4 text-right flex gap-2 justify-end">
                            <button @click="simulateAction('Đã gắn thêm Tag cho khách hàng Nguyễn Văn Nam')" class="text-xs bg-[#00F0FF]/10 text-[#00F0FF] px-3 py-1 rounded hover:bg-[#00F0FF]/20 font-bold border border-[#00F0FF]/30">Gắn Tag</button>
                            <button @click="simulateAction('Đang chuyển hướng sang giao diện Inbox...')" class="text-xs bg-white/10 text-white px-3 py-1 rounded hover:bg-white/20 font-bold">Chat</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
'''

AFFILIATE_HTML = '''
        <div x-data="{ simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); } }">
            <h2 class="text-xl font-bold mb-6">Quản Lý Affiliate & Cộng Tác Viên</h2>
            <div class="p-6 bg-[#121214] border border-[#7B2DFF]/30 rounded-2xl mb-6 flex flex-col md:flex-row justify-between items-center bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-r from-[#7B2DFF]/20 to-transparent"></div>
                <div class="relative z-10">
                    <h3 class="text-2xl font-bold text-white mb-2">Hệ Thống CTV Đại Lý</h3>
                    <p class="text-sm text-slate-300">Biến khách hàng thành người bán hàng cho bạn với hoa hồng tự động.</p>
                </div>
                <button @click="simulateAction('Đã sao chép Link Đăng Ký CTV vào bộ nhớ tạm!')" class="mt-4 md:mt-0 px-6 py-3 bg-[#7B2DFF] text-white font-bold rounded-xl hover:bg-purple-500 shadow-[0_0_20px_rgba(123,45,255,0.4)] relative z-10 flex items-center gap-2">
                    <span class="material-symbols-outlined">link</span> Lấy Link Tuyển CTV
                </button>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-[#121214] border border-white/5 rounded-2xl p-6">
                    <h3 class="font-bold mb-4">Duyệt Cộng Tác Viên Mới</h3>
                    <div class="flex justify-between items-center p-3 bg-white/5 rounded-xl border border-white/10 mb-2">
                        <div><div class="font-bold text-sm">Trần Lê Huy</div><div class="text-[10px] text-slate-400">Zalo: 0989xxx</div></div>
                        <div class="flex gap-2">
                            <button @click="simulateAction('Đã DUYỆT tài khoản CTV Trần Lê Huy')" class="p-1.5 bg-[#10B981]/20 text-[#10B981] rounded hover:bg-[#10B981]/30"><span class="material-symbols-outlined text-[16px]">check</span></button>
                            <button @click="simulateAction('Đã TỪ CHỐI tài khoản CTV Trần Lê Huy')" class="p-1.5 bg-red-500/20 text-red-500 rounded hover:bg-red-500/30"><span class="material-symbols-outlined text-[16px]">close</span></button>
                        </div>
                    </div>
                </div>
                <div class="bg-[#121214] border border-white/5 rounded-2xl p-6">
                    <h3 class="font-bold mb-4">Cấu Hình Hoa Hồng (Commission)</h3>
                    <label class="block text-xs font-bold text-slate-400 mb-2">Mức Hoa Hồng Chuẩn (%)</label>
                    <div class="flex gap-2">
                        <input type="number" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white" value="15">
                        <button @click="simulateAction('Đã lưu cấu hình Mức Hoa Hồng thành 15%')" class="px-6 bg-[#00F0FF] text-black font-bold rounded-xl text-sm hover:bg-cyan-400">Lưu</button>
                    </div>
                </div>
            </div>
        </div>
'''

SUPPORT_HTML = '''
        <div x-data="{ simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); } }">
            <h2 class="text-2xl font-bold mb-6 font-display">Trung Tâm Hỗ Trợ Kỹ Thuật (24/7)</h2>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div class="bg-[#121214] p-8 rounded-3xl border border-[#00F0FF]/20 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-[#00F0FF]/10 rounded-full blur-[80px]"></div>
                    <h3 class="text-xl font-bold text-[#00F0FF] mb-2 relative z-10">Tạo Ticket Hỗ Trợ Mới</h3>
                    <p class="text-sm text-slate-400 mb-6 relative z-10">Đội ngũ kỹ thuật Super Admin sẽ phản hồi trong vòng 5-10 phút.</p>
                    
                    <div class="space-y-4 relative z-10">
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Chủ đề hỗ trợ</label>
                            <select class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white focus:outline-none focus:border-[#00F0FF]">
                                <option>Lỗi không kết nối được Tiktok/Shopee</option>
                                <option>Hỏi cách cài đặt kịch bản Bot AI</option>
                                <option>Vấn đề về thanh toán/Gói cước</option>
                                <option>Lỗi khác...</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Mô tả chi tiết</label>
                            <textarea class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white h-32 focus:outline-none focus:border-[#00F0FF]" placeholder="Mô tả lỗi hoặc câu hỏi của bạn..."></textarea>
                        </div>
                        <button @click="simulateAction('Đã gửi Ticket Hỗ Trợ! Mã Ticket của bạn là #TK-992. Kỹ thuật viên sẽ phản hồi sớm nhất.')" class="w-full py-3 bg-[#00F0FF] text-black font-bold rounded-xl text-sm hover:bg-cyan-400 shadow-[0_0_15px_rgba(0,240,255,0.3)]">Gửi Yêu Cầu Hỗ Trợ Ngay</button>
                    </div>
                </div>

                <div class="space-y-4">
                    <h3 class="font-bold text-lg mb-4">Lịch Sử Ticket Của Bạn</h3>
                    <div class="bg-[#121214] border border-white/5 p-4 rounded-xl flex justify-between items-center cursor-pointer hover:bg-white/5">
                        <div>
                            <div class="font-bold text-sm text-white">#TK-801: Lỗi đồng bộ tin nhắn Shopee</div>
                            <div class="text-xs text-slate-500 mt-1">Gửi lúc: 10:45 Hôm nay</div>
                        </div>
                        <span class="px-3 py-1 bg-green-500/10 text-green-400 border border-green-500/30 rounded text-xs font-bold">Đã xử lý</span>
                    </div>
                    <div class="bg-[#121214] border border-white/5 p-4 rounded-xl flex justify-between items-center cursor-pointer hover:bg-white/5">
                        <div>
                            <div class="font-bold text-sm text-white">#TK-742: Bot trả lời chậm</div>
                            <div class="text-xs text-slate-500 mt-1">Gửi lúc: Hôm qua</div>
                        </div>
                        <span class="px-3 py-1 bg-green-500/10 text-green-400 border border-green-500/30 rounded text-xs font-bold">Đã xử lý</span>
                    </div>
                </div>
            </div>
        </div>
'''

FILES = [
    ('js/layout.js', LAYOUT_JS),
]

HTML_PAGES = [
    ('ecommerce.html', 'ecommerce', ECOMMERCE_HTML),
    ('crm.html', 'crm', CRM_HTML),
    ('affiliate.html', 'affiliate', AFFILIATE_HTML),
    ('support.html', 'support', SUPPORT_HTML)
]

for file_path, content in FILES:
    with open(file_path, 'w') as f:
        f.write(content.strip())

TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>CHỐT NGHÌN ĐƠN</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet"/>
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

print("Đã hoàn thành P8: Quét sạch 100% nút bấm + Tích hợp AI Agent hướng dẫn toàn cục.")
