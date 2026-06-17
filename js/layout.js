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