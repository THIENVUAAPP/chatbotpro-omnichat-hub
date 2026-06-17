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