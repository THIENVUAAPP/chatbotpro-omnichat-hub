// layout.js - Centralized Layout Manager for CHỐT NGHÌN ĐƠN Multi-tenant SaaS

const THEME = {
    bg: '#0A0A0A',
    surface: '#121214',
    primary: '#10B981', // Emerald Green
    accent: '#FFD700', // Victory Gold
    glow: '#7B2DFF' // Royal Purple
};

const MENU_ITEMS = [
    {
        group: 'CỐT LÕI (NHÓM B & C)',
        items: [
            { id: 'dashboard', icon: 'dashboard', label: 'Dashboard & Inbox', url: 'dashboard.html' },
            { id: 'bot_builder', icon: 'smart_toy', label: 'Flow Builder & RAG', url: 'bot_builder.html' },
            { id: 'broadcast', icon: 'campaign', label: 'Chiến Dịch & Mẫu', url: 'broadcast.html' }
        ]
    },
    {
        group: 'VẬN HÀNH BÁN HÀNG',
        items: [
            { id: 'channels', icon: 'hub', label: 'Quản Lý Kênh', url: 'channels.html' },
            { id: 'ecommerce', icon: 'shopping_cart', label: 'Sản Phẩm & Đơn', url: 'ecommerce.html' },
            { id: 'crm', icon: 'groups', label: 'CRM Khách Hàng', url: 'crm.html' },
            { id: 'content', icon: 'article', label: 'Nội Dung & Banner', url: 'content.html' }
        ]
    },
    {
        group: 'CÀI ĐẶT DOANH NGHIỆP',
        items: [
            { id: 'team', icon: 'shield_person', label: 'Phân Quyền Team', url: 'team_management.html' },
            { id: 'settings', icon: 'settings', label: 'Thiết Lập Tenant', url: 'tenant_settings.html' },
            { id: 'analytics', icon: 'analytics', label: 'Báo Cáo Phân Tích', url: 'analytics.html' }
        ]
    }
];

const ADMIN_MENU = {
    group: 'SUPER ADMIN (NHÓM J)',
    items: [
        { id: 'admin_panel', icon: 'admin_panel_settings', label: 'Quản Lý Toàn Hệ Thống', url: 'admin_panel.html' },
        { id: 'affiliate', icon: 'handshake', label: 'Đối Tác & Hoa Hồng', url: 'affiliate.html' }
    ]
};

function renderLayout(activeId, contentHTML) {
    const role = localStorage.getItem('chatbotpro_role') || 'member';
    const userEmail = localStorage.getItem('chatbotpro_user') || 'khachhang@gmail.com';
    const plan = localStorage.getItem('chatbotpro_plan');

    let menusToRender = [...MENU_ITEMS];
    if (role === 'admin') {
        menusToRender.push(ADMIN_MENU);
    }
    // Hỗ trợ cũng thêm vào cuối
    menusToRender.push({
        group: 'HỖ TRỢ',
        items: [{ id: 'support', icon: 'help_center', label: 'Trợ Giúp & Lỗi', url: 'support.html' }]
    });

    const sidebarHTML = menusToRender.map(group => `
        <div class="mb-6">
            <div class="text-xs font-bold text-slate-500 mb-2 px-4 uppercase tracking-wider">${group.group}</div>
            <ul class="space-y-1">
                ${group.items.map(item => `
                    <li>
                        <a href="${item.url}" class="flex items-center gap-3 px-4 py-2 rounded-xl transition-all ${activeId === item.id ? 'bg-primary/10 text-primary border-l-2 border-primary font-bold' : 'text-slate-400 hover:bg-white/5 hover:text-white'}">
                            <span class="material-symbols-outlined text-[20px]">${item.icon}</span>
                            <span class="text-sm">${item.label}</span>
                        </a>
                    </li>
                `).join('')}
            </ul>
        </div>
    `).join('');

    const freeTrialBanner = plan === 'free_trial' ? `
        <div class="w-full bg-[#FFD700]/10 border-b border-[#FFD700]/30 px-6 py-2 flex items-center justify-between z-40 relative">
            <div class="flex items-center gap-3 text-[#FFD700]">
                <span class="material-symbols-outlined text-sm">new_releases</span>
                <span class="font-bold text-xs uppercase tracking-wider">Tài khoản Free Trial - Giới hạn 500 tin nhắn AI</span>
            </div>
            <button onclick="window.location.href='checkout.html'" class="px-4 py-1.5 bg-[#FFD700] text-[#0A0A0A] font-bold text-xs rounded-full hover:bg-yellow-400 transition-colors shadow-[0_0_15px_rgba(255,215,0,0.4)]">Nâng Cấp VIP</button>
        </div>
    ` : '';

    const fullHTML = `
        <div class="flex h-screen bg-[#0A0A0A] text-white font-body overflow-hidden">
            <!-- Sidebar -->
            <aside class="w-64 bg-[#121214] border-r border-white/5 flex flex-col h-full flex-shrink-0 relative z-20">
                <div class="p-6">
                    <div class="font-display font-extrabold text-2xl bg-gradient-to-r from-primary to-[#FFD700] bg-clip-text text-transparent cursor-pointer" onclick="window.location.href='index.html'">
                        CHỐT NGHÌN ĐƠN
                    </div>
                    <div class="text-[10px] text-slate-500 mt-1 tracking-widest uppercase">Multi-Tenant Platform</div>
                </div>
                <div class="flex-1 overflow-y-auto custom-scrollbar px-2 pb-6">
                    ${sidebarHTML}
                </div>
                <div class="p-4 border-t border-white/5 bg-[#121214]">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-10 h-10 rounded-full bg-gradient-to-br from-primary to-[#7B2DFF] flex items-center justify-center font-bold text-sm shadow-[0_0_10px_rgba(123,45,255,0.3)]">
                            ${userEmail.charAt(0).toUpperCase()}
                        </div>
                        <div class="overflow-hidden">
                            <div class="text-xs font-bold text-white truncate">${userEmail}</div>
                            <div class="text-[10px] text-[#00F0FF] uppercase tracking-wider mt-0.5">${role.toUpperCase()}</div>
                        </div>
                    </div>
                    <button onclick="logout()" class="w-full py-2 flex items-center justify-center gap-2 text-xs font-bold text-red-400 hover:bg-red-500/10 rounded-lg transition-colors">
                        <span class="material-symbols-outlined text-[16px]">logout</span> Đăng Xuất
                    </button>
                </div>
            </aside>

            <!-- Main Content Area -->
            <main class="flex-1 flex flex-col h-full relative z-10 overflow-hidden bg-gradient-to-br from-[#0A0A0A] to-[#0d0d12]">
                <!-- Glow Effect -->
                <div class="absolute top-0 right-0 w-96 h-96 bg-[#7B2DFF]/10 rounded-full blur-[120px] pointer-events-none"></div>
                
                ${freeTrialBanner}

                <!-- Header -->
                <header class="h-16 px-8 flex items-center justify-between border-b border-white/5 bg-[#121214]/50 backdrop-blur-md sticky top-0 z-30">
                    <div class="font-display font-bold text-lg text-slate-200" id="header-title">Trang Quản Trị</div>
                    <div class="flex items-center gap-4">
                        <button class="relative p-2 text-slate-400 hover:text-white transition-colors">
                            <span class="material-symbols-outlined">notifications</span>
                            <span class="absolute top-1.5 right-1.5 w-2 h-2 bg-red-500 rounded-full"></span>
                        </button>
                        <button class="px-4 py-1.5 bg-white/5 border border-white/10 rounded-lg text-xs font-bold hover:bg-white/10 transition-colors flex items-center gap-2">
                            <span class="material-symbols-outlined text-[16px]">storefront</span> Cửa Hàng Demo
                        </button>
                    </div>
                </header>

                <!-- Page Content -->
                <div class="flex-1 overflow-y-auto p-8 relative z-20 custom-scrollbar">
                    ${contentHTML}
                </div>
            </main>
        </div>
    `;

    document.getElementById('root').innerHTML = fullHTML;
    
    // Set Header Title based on active item
    const allItems = menusToRender.flatMap(g => g.items);
    const currentItem = allItems.find(i => i.id === activeId);
    if(currentItem) {
        document.getElementById('header-title').innerText = currentItem.label;
    }
}

function logout() {
    localStorage.removeItem('chatbotpro_user');
    localStorage.removeItem('chatbotpro_role');
    localStorage.removeItem('chatbotpro_plan');
    window.location.href = 'login.html';
}

// Chạy bảo vệ Route chung (Trừ login, index, checkout)
window.addEventListener('DOMContentLoaded', () => {
    const user = localStorage.getItem('chatbotpro_user');
    const path = window.location.pathname;
    if (!user && !path.includes('login.html') && !path.includes('index.html')) {
        window.location.href = 'login.html';
    }
});
