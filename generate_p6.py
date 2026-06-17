import os

# 1. Nâng cấp layout.js để hỗ trợ Toast Thông báo toàn cục và Chuông (Global Bell)
LAYOUT_JS = '''
const NAV_ITEMS = [
    { id: 'dashboard', icon: 'chat', label: 'Inbox & Chat', role: 'all' },
    { id: 'crm', icon: 'group', label: 'Quản Lý Khách Hàng (CRM)', role: 'all' },
    { id: 'ecommerce', icon: 'storefront', label: 'Đơn Hàng & Vận Chuyển', role: 'all' },
    { id: 'bot_builder', icon: 'smart_toy', label: 'AI Bot Builder & RAG', role: 'admin' },
    { id: 'content', icon: 'perm_media', label: 'Media & Nội Dung', role: 'all' },
    { id: 'analytics', icon: 'monitoring', label: 'Báo Cáo & Phân Tích', role: 'all' },
    { id: 'affiliate', icon: 'diversity_3', label: 'Affiliate & CTV', role: 'admin' },
    { id: 'channels', icon: 'hub', label: 'Kết Nối Kênh', role: 'admin' },
    { id: 'team_management', icon: 'badge', label: 'Team & Phân Quyền', role: 'admin' },
    { id: 'support', icon: 'help_clinic', label: 'Hỗ Trợ (24/7)', role: 'all' },
    { id: 'tenant_settings', icon: 'settings', label: 'Cài Đặt Cửa Hàng', role: 'admin' },
    { id: 'admin_panel', icon: 'local_police', label: 'Super Admin', role: 'super_admin' },
];

function renderLayout(activeId, contentHtml) {
    const root = document.getElementById('root');
    const role = 'super_admin'; 
    
    const visibleNav = NAV_ITEMS.filter(item => {
        if (role === 'super_admin') return true;
        if (role === 'admin' && item.role !== 'super_admin') return true;
        return item.role === 'all';
    });

    const navHtml = visibleNav.map(item => `
        <a href="${item.id}.html" class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${item.id === activeId ? 'bg-gradient-to-r from-[#10B981]/20 to-transparent text-[#10B981] border-l-4 border-[#10B981]' : 'text-slate-400 hover:bg-white/5 hover:text-white'}">
            <span class="material-symbols-outlined">${item.icon}</span>
            <span class="font-bold text-sm hidden md:block">${item.label}</span>
        </a>
    `).join('');

    root.innerHTML = `
        <!-- X-DATA TOÀN CỤC CHỨA TOAST VÀ THÔNG BÁO CHUÔNG -->
        <div class="flex h-screen bg-[#0A0A0A] text-white font-body overflow-hidden" 
             x-data="globalState()" 
             @show-toast.window="addToast($event.detail.msg, $event.detail.type)">
            
            <!-- Sidebar -->
            <div class="w-20 md:w-64 bg-[#121214] border-r border-white/5 flex flex-col transition-all duration-300 z-20">
                <div class="h-16 flex items-center justify-center md:justify-start md:px-6 border-b border-white/5">
                    <div class="w-8 h-8 rounded bg-gradient-to-br from-[#10B981] to-[#00F0FF] flex items-center justify-center font-bold text-black font-display shadow-[0_0_15px_rgba(16,185,129,0.5)]">CN</div>
                    <span class="ml-3 font-display font-black tracking-widest bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400 hidden md:block">CHỐT NGHÌN ĐƠN</span>
                </div>
                <div class="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-1">
                    ${navHtml}
                </div>
                <div class="p-4 border-t border-white/5 flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-r from-[#7B2DFF] to-[#00F0FF] flex items-center justify-center font-bold">TC</div>
                    <div class="hidden md:block">
                        <div class="text-sm font-bold">Thiên CR7</div>
                        <div class="text-xs text-[#FFD700]">Super Admin</div>
                    </div>
                </div>
            </div>

            <!-- Main Content -->
            <div class="flex-1 flex flex-col h-screen overflow-hidden relative">
                <!-- Header / Global Bell -->
                <header class="h-16 bg-[#121214]/80 backdrop-blur-md border-b border-white/5 flex items-center justify-between px-6 z-10">
                    <div class="font-bold text-lg hidden sm:block">Không gian làm việc</div>
                    
                    <!-- BELL NOTIFICATIONS -->
                    <div class="flex items-center gap-4">
                        <!-- Nút báo động hệ thống / Toast Test -->
                        <div class="relative cursor-pointer" @click="showNotif = !showNotif">
                            <span class="material-symbols-outlined text-slate-300 hover:text-white transition-colors">notifications</span>
                            
                            <!-- Dấu chấm đỏ báo tin nhắn mới -->
                            <span x-show="unreadCount > 0" style="display:none;" class="absolute -top-1 -right-1 w-4 h-4 bg-red-500 rounded-full flex items-center justify-center text-[9px] font-bold text-white shadow-[0_0_10px_rgba(239,68,68,0.8)] animate-pulse" x-text="unreadCount"></span>

                            <!-- Dropdown thông báo -->
                            <div x-show="showNotif" @click.outside="showNotif = false" style="display:none;" class="absolute right-0 top-10 w-80 bg-[#121214] border border-white/10 rounded-2xl shadow-2xl z-50 overflow-hidden">
                                <div class="p-4 border-b border-white/10 font-bold flex justify-between">
                                    <span>Thông Báo Đa Kênh</span>
                                    <span class="text-xs text-[#00F0FF] cursor-pointer" @click="unreadCount = 0; notifications = []">Đọc tất cả</span>
                                </div>
                                <div class="max-h-64 overflow-y-auto custom-scrollbar">
                                    <template x-for="n in notifications" :key="n.id">
                                        <div class="p-4 border-b border-white/5 hover:bg-white/5 flex gap-3 text-sm">
                                            <div class="w-8 h-8 rounded-full flex items-center justify-center text-white" :class="n.platform === 'Tiktok' ? 'bg-black border border-white/20' : (n.platform==='Shopee' ? 'bg-[#EE4D2D]' : 'bg-blue-500')">
                                                <span class="material-symbols-outlined text-[16px]" x-text="n.icon"></span>
                                            </div>
                                            <div>
                                                <div class="font-bold text-white" x-text="n.title"></div>
                                                <div class="text-xs text-slate-400 mt-1" x-text="n.message"></div>
                                                <div class="text-[10px] text-slate-500 mt-1" x-text="n.time"></div>
                                            </div>
                                        </div>
                                    </template>
                                    <div x-show="notifications.length === 0" class="p-8 text-center text-slate-500 text-sm">Không có thông báo mới</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </header>

                <main class="flex-1 overflow-y-auto p-4 md:p-8 custom-scrollbar">
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
            // Alpine Component cho Global State (Toast & Real-time Inbox Notification)
            document.addEventListener('alpine:init', () => {
                Alpine.data('globalState', () => ({
                    toasts: [],
                    toastCounter: 0,
                    showNotif: false,
                    unreadCount: 0,
                    notifications: [],
                    
                    init() {
                        // Kích hoạt giả lập hệ thống Real-time nhắn tin (Auto Bell)
                        setInterval(() => {
                            // Chỉ giả lập ngẫu nhiên nếu người dùng đang không mở bảng thông báo
                            if(!this.showNotif && Math.random() > 0.7) {
                                this.triggerNewMessage();
                            }
                        }, 8000); // Mỗi 8s có cơ hội nổ tin nhắn
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
                            message: 'Khách hàng vừa gửi 1 yêu cầu cần hỗ trợ ngay.',
                            time: 'Vừa xong'
                        });
                        
                        // Kêu 1 tiếng tinh (Dùng audio base64 nhỏ để giả lập tiếng chuông nếu cần, ở đây dùng toast)
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

# 2. Nâng cấp dashboard.html (Inbox)
DASHBOARD_HTML = '''
        <div x-data="{ 
            replying: false,
            // Phát sự kiện toast toàn cục
            simulateAction(msg) {
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } }));
            }
        }" class="h-full flex flex-col md:flex-row gap-6">
            <!-- Left: Danh sách tin nhắn (Đa nền tảng) -->
            <div class="w-full md:w-1/3 bg-[#121214] rounded-2xl border border-white/5 flex flex-col h-[600px] md:h-full">
                <div class="p-4 border-b border-white/5 font-bold text-lg flex justify-between items-center">
                    <span>Hộp Thư Siêu Tốc (Đa Nền Tảng)</span>
                    <!-- Badge báo hiệu Live -->
                    <span class="px-2 py-1 bg-red-500/20 text-red-500 text-[10px] rounded animate-pulse border border-red-500/50">● LIVE</span>
                </div>
                <div class="flex-1 overflow-y-auto custom-scrollbar">
                    <!-- Tiktok Msg -->
                    <div class="p-4 border-b border-white/5 bg-white/5 cursor-pointer flex gap-3">
                        <div class="w-10 h-10 rounded-full bg-black border border-white/20 flex items-center justify-center font-bold">TT</div>
                        <div class="flex-1">
                            <div class="flex justify-between items-center"><span class="font-bold text-sm">Nguyễn Phương</span><span class="text-xs text-slate-500">2p trước</span></div>
                            <div class="text-xs text-[#00F0FF] mt-1 font-bold">Tiktok Shop</div>
                            <div class="text-sm text-slate-300 mt-1 line-clamp-1">Sản phẩm này còn màu trắng size M không shop?</div>
                        </div>
                    </div>
                    <!-- Shopee Msg -->
                    <div class="p-4 border-b border-white/5 hover:bg-white/5 transition-colors cursor-pointer flex gap-3">
                        <div class="w-10 h-10 rounded-full bg-[#EE4D2D] text-white flex items-center justify-center font-bold">S</div>
                        <div class="flex-1">
                            <div class="flex justify-between items-center"><span class="font-bold text-sm">Trần Văn Bình</span><span class="text-xs text-slate-500">15p trước</span></div>
                            <div class="text-xs text-[#EE4D2D] mt-1 font-bold">Shopee</div>
                            <div class="text-sm text-slate-400 mt-1 line-clamp-1">Cho mình hỏi bao giờ hàng được giao vậy?</div>
                        </div>
                    </div>
                    <!-- FB Msg -->
                    <div class="p-4 border-b border-white/5 hover:bg-white/5 transition-colors cursor-pointer flex gap-3">
                        <div class="w-10 h-10 rounded-full bg-blue-500 text-white flex items-center justify-center"><span class="material-symbols-outlined text-sm">forum</span></div>
                        <div class="flex-1">
                            <div class="flex justify-between items-center"><span class="font-bold text-sm">Lê Thu Hà</span><span class="text-xs text-slate-500">1h trước</span></div>
                            <div class="text-xs text-blue-400 mt-1 font-bold">Facebook Messenger</div>
                            <div class="text-sm text-slate-400 mt-1 line-clamp-1">Shop tư vấn giúp mình bộ áo dài tết nhé.</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right: Cửa sổ Chat -->
            <div class="flex-1 bg-[#121214] rounded-2xl border border-white/5 flex flex-col h-[600px] md:h-full relative overflow-hidden">
                <div class="p-4 border-b border-white/5 flex items-center justify-between">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-black border border-white/20 flex items-center justify-center font-bold">TT</div>
                        <div>
                            <div class="font-bold">Nguyễn Phương</div>
                            <div class="text-xs text-[#10B981] flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-[#10B981]"></span> Online trên Tiktok</div>
                        </div>
                    </div>
                    <button @click="simulateAction('Đã chặn khách hàng này trên mọi nền tảng')" class="p-2 bg-red-500/10 text-red-500 rounded hover:bg-red-500/20"><span class="material-symbols-outlined text-[18px]">block</span></button>
                </div>
                
                <div class="flex-1 p-4 overflow-y-auto flex flex-col gap-4">
                    <div class="self-start max-w-[80%] flex gap-3">
                        <div class="w-8 h-8 rounded-full bg-black text-white flex items-center justify-center text-xs">TT</div>
                        <div class="bg-[#1A1A1D] p-3 rounded-2xl rounded-tl-sm text-sm border border-white/5">
                            Sản phẩm này còn màu trắng size M không shop?
                        </div>
                    </div>
                    <!-- Bot AI Reply -->
                    <div class="self-end max-w-[80%] flex gap-3 flex-row-reverse">
                        <div class="w-8 h-8 rounded-full bg-gradient-to-r from-[#10B981] to-[#00F0FF] text-black font-bold flex items-center justify-center text-xs shadow-[0_0_10px_rgba(0,240,255,0.5)]">AI</div>
                        <div class="bg-gradient-to-r from-[#10B981]/20 to-[#00F0FF]/20 border border-[#00F0FF]/30 p-3 rounded-2xl rounded-tr-sm text-sm text-white">
                            Chào bạn! Sản phẩm Áo Sơ Mi mã A01 hiện tại VẪN CÒN màu Trắng size M nhé. Bạn có muốn mình tạo đơn luôn để kịp giao trong hôm nay không ạ? 😊
                        </div>
                    </div>
                </div>

                <!-- Input box -->
                <div class="p-4 bg-[#121214] border-t border-white/5">
                    <div class="flex gap-2">
                        <button @click="simulateAction('Đã gửi tệp đính kèm')" class="p-3 bg-white/5 rounded-xl hover:bg-white/10 text-slate-400"><span class="material-symbols-outlined">attach_file</span></button>
                        <input type="text" placeholder="Nhập tin nhắn để AI duyệt lại hoặc bấm gửi ngay..." class="flex-1 bg-[#0A0A0A] border border-white/10 rounded-xl px-4 text-sm focus:outline-none focus:border-[#00F0FF] text-white">
                        <button @click="simulateAction('Đã gửi tin nhắn qua Tiktok Shop thành công!')" class="p-3 bg-[#00F0FF] text-black rounded-xl hover:bg-cyan-400 shadow-[0_0_10px_rgba(0,240,255,0.3)]"><span class="material-symbols-outlined">send</span></button>
                    </div>
                </div>
            </div>
        </div>
'''

# 3. Nâng cấp team_management.html (Add Gmail trực tiếp)
TEAM_MANAGEMENT_HTML = '''
        <div x-data="{ 
            showInviteModal: false,
            showGmailModal: false,
            importing: false,
            simulateAction(msg) {
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } }));
            },
            startGmailImport() {
                this.importing = true;
                setTimeout(() => {
                    this.importing = false;
                    this.showGmailModal = false;
                    this.simulateAction('Đã đồng bộ thành công 2 tài khoản từ Google Workspace!');
                }, 2000);
            }
        }">
            <div class="flex justify-between items-center mb-8">
                <h2 class="text-xl font-bold">Phân Quyền Nhóm Cửa Hàng</h2>
                <div class="flex gap-2">
                    <!-- Nút Mới: Add Google Workspace -->
                    <button @click="showGmailModal = true" class="px-4 py-2 bg-white text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-slate-200">
                        <svg class="w-4 h-4" viewBox="0 0 24 24"><path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
                        Thêm Bằng Gmail (Direct)
                    </button>
                    <!-- Nút Email thông thường -->
                    <button @click="showInviteModal = true" class="px-4 py-2 bg-[#10B981] text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-emerald-400">
                        <span class="material-symbols-outlined text-[18px]">person_add</span> Thêm Nhân Viên
                    </button>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- User card -->
                <div class="bg-[#121214] p-6 rounded-2xl border border-white/5">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-12 h-12 bg-gradient-to-r from-[#7B2DFF] to-[#00F0FF] rounded-full flex items-center justify-center font-bold text-lg">TC</div>
                        <div>
                            <div class="font-bold">Thiên CR7</div>
                            <div class="text-xs text-slate-400">quocthiencr7@gmail.com</div>
                        </div>
                    </div>
                    <div class="mb-4"><span class="px-3 py-1 bg-[#FFD700]/20 text-[#FFD700] rounded text-[10px] font-bold border border-[#FFD700]/50 uppercase tracking-wider">Super Admin Hệ Thống</span></div>
                    <div class="flex gap-2">
                        <button @click="simulateAction('Không thể chỉnh sửa Super Admin!')" class="flex-1 py-2 bg-white/5 hover:bg-white/10 rounded-lg text-sm text-slate-300 font-bold">Chỉnh sửa</button>
                    </div>
                </div>

                <div class="bg-[#121214] p-6 rounded-2xl border border-white/5">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center font-bold text-lg">H</div>
                        <div>
                            <div class="font-bold">Trần Minh Hiếu</div>
                            <div class="text-xs text-slate-400">hieu.sale@gmail.com</div>
                        </div>
                    </div>
                    <div class="mb-4"><span class="px-3 py-1 bg-[#10B981]/10 text-[#10B981] rounded text-[10px] font-bold border border-[#10B981]/30 uppercase tracking-wider">Sale / CSKH</span></div>
                    <div class="flex gap-2">
                        <button @click="simulateAction('Đã lưu phân quyền cho nhân viên Hiếu')" class="flex-1 py-2 bg-white/5 hover:bg-white/10 rounded-lg text-sm text-slate-300 font-bold">Chỉnh sửa</button>
                        <button @click="simulateAction('Đã xóa nhân viên khỏi hệ thống')" class="w-10 flex items-center justify-center bg-red-500/10 text-red-500 hover:bg-red-500 hover:text-white rounded-lg transition-colors"><span class="material-symbols-outlined text-[18px]">delete</span></button>
                    </div>
                </div>
            </div>

            <!-- MODAL THÊM BẰNG GMAIL -->
            <div x-show="showGmailModal" style="display:none;" class="fixed inset-0 bg-black/90 flex items-center justify-center z-50 backdrop-blur-sm">
                <div class="bg-[#121214] border border-white/10 p-8 rounded-3xl w-[450px] text-center" @click.outside="!importing && (showGmailModal = false)">
                    <svg class="w-16 h-16 mx-auto mb-4" viewBox="0 0 24 24"><path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
                    <h3 class="text-xl font-bold mb-2">Thêm Trực Tiếp Từ Google Workspace</h3>
                    <p class="text-sm text-slate-400 mb-6">Đồng bộ tự động tài khoản Gmail của nhân viên/khách hàng vào hệ thống.</p>
                    
                    <div x-show="!importing">
                        <div class="text-left bg-[#0A0A0A] p-4 rounded-xl border border-white/5 mb-6 text-sm">
                            <label class="flex items-center gap-3 mb-3 cursor-pointer">
                                <input type="checkbox" checked class="accent-[#10B981] w-4 h-4">
                                <span>nguyen.a@gmail.com (Quyền Sale)</span>
                            </label>
                            <label class="flex items-center gap-3 cursor-pointer">
                                <input type="checkbox" checked class="accent-[#10B981] w-4 h-4">
                                <span>tran.b@gmail.com (Quyền Media)</span>
                            </label>
                        </div>
                        <div class="flex gap-4">
                            <button @click="showGmailModal = false" class="flex-1 py-3 bg-white/5 hover:bg-white/10 rounded-xl font-bold">Hủy</button>
                            <button @click="startGmailImport()" class="flex-1 py-3 bg-white text-black font-bold rounded-xl hover:bg-slate-200">Import Ngay</button>
                        </div>
                    </div>

                    <div x-show="importing" class="py-8">
                        <span class="material-symbols-outlined animate-spin text-4xl text-blue-500 mb-2">sync</span>
                        <p class="text-blue-400 font-bold">Đang kết nối Google API & Thêm User...</p>
                    </div>
                </div>
            </div>
            
            <!-- MODAL THÊM EMAIL -->
            <div x-show="showInviteModal" style="display:none;" class="fixed inset-0 bg-black/90 flex items-center justify-center z-50 backdrop-blur-sm">
                <div class="bg-[#121214] border border-[#10B981]/30 p-8 rounded-3xl w-[400px]" @click.outside="showInviteModal = false">
                    <h3 class="text-xl font-bold mb-4 text-[#10B981]">Thêm Nhân Viên (Thủ Công)</h3>
                    <input type="email" placeholder="Nhập email nhân viên..." class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl mb-4 focus:outline-none focus:border-[#10B981] text-white">
                    <select class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl mb-6 text-white focus:outline-none focus:border-[#10B981]">
                        <option>Quyền: Admin Cửa Hàng</option>
                        <option>Quyền: Sale / CSKH</option>
                        <option>Quyền: Marketing / Content</option>
                    </select>
                    <button @click="showInviteModal = false; simulateAction('Đã gửi email lời mời kích hoạt!')" class="w-full py-3 bg-[#10B981] text-black font-bold rounded-xl text-sm hover:bg-emerald-400">Gửi Lời Mời</button>
                </div>
            </div>
        </div>
'''

# 4. Nâng cấp Analytics (Toast vào nút Export)
ANALYTICS_HTML = '''
        <div x-data="{
            simulateAction(msg) {
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } }));
            }
        }">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-xl font-bold">Báo Cáo Phân Tích (Analytics)</h2>
                <div class="flex gap-2">
                    <button @click="simulateAction('Đang tạo và tải file PDF báo cáo...')" class="px-4 py-2 bg-white/5 hover:bg-white/10 text-white font-bold rounded-xl text-sm flex items-center gap-2 border border-white/10"><span class="material-symbols-outlined text-[18px]">picture_as_pdf</span> Xuất PDF</button>
                    <button @click="simulateAction('Dữ liệu đã được xuất ra file Excel. Bắt đầu tải xuống...')" class="px-4 py-2 bg-[#10B981]/20 hover:bg-[#10B981]/30 text-[#10B981] font-bold rounded-xl text-sm flex items-center gap-2 border border-[#10B981]/30"><span class="material-symbols-outlined text-[18px]">table_chart</span> Xuất Excel</button>
                </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                    <div class="text-xs text-slate-400 mb-1">Tổng Doanh Thu (T10)</div>
                    <div class="text-3xl font-display font-black text-[#10B981]">85.4M</div>
                    <div class="text-xs text-green-400 mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">trending_up</span> +12% so với tháng trước</div>
                </div>
                <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                    <div class="text-xs text-slate-400 mb-1">Đơn Chốt Qua AI</div>
                    <div class="text-3xl font-display font-black text-[#00F0FF]">1,402</div>
                    <div class="text-xs text-green-400 mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">trending_up</span> +5.2%</div>
                </div>
                <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                    <div class="text-xs text-slate-400 mb-1">Khách Hàng Mới</div>
                    <div class="text-3xl font-display font-black text-white">450</div>
                </div>
                <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                    <div class="text-xs text-slate-400 mb-1">Tỷ Lệ Chốt Đơn (CR)</div>
                    <div class="text-3xl font-display font-black text-[#FFD700]">32.4%</div>
                </div>
            </div>
            <div class="p-8 bg-[#121214] border border-white/5 rounded-2xl text-center text-slate-500">
                <span class="material-symbols-outlined text-6xl mb-4 text-white/5">insert_chart</span>
                <p>Khu vực nhúng biểu đồ TradingView / Chart.js cho Phân tích dòng tiền</p>
            </div>
        </div>
'''

FILES = [
    ('js/layout.js', LAYOUT_JS),
]

HTML_PAGES = [
    ('dashboard.html', 'dashboard', DASHBOARD_HTML),
    ('team_management.html', 'team_management', TEAM_MANAGEMENT_HTML),
    ('analytics.html', 'analytics', ANALYTICS_HTML),
]

# Write JS
for file_path, content in FILES:
    with open(file_path, 'w') as f:
        f.write(content.strip())

# Write HTMLs
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

print("Đã kích hoạt P6: Thông báo Chuông toàn cục, Tin nhắn Inbox Auto, Thêm user bằng Gmail trực tiếp, Toast 100% các nút.")
