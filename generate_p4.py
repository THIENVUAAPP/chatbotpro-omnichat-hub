import os

admin_html_content = '''
        <div x-data="{ 
            activeTab: 'overview',
            platforms: [
                {name: 'Facebook Messenger', type: 'Social', active: true, users: 1205},
                {name: 'Zalo OA', type: 'Social', active: true, users: 850},
                {name: 'Tiktok Shop', type: 'E-commerce', active: true, users: 430},
                {name: 'Shopee', type: 'E-commerce', active: true, users: 610},
                {name: 'Lazada', type: 'E-commerce', active: false, users: 0}
            ],
            showPlatformModal: false,
            newPlatformName: '',
            newPlatformType: 'Social',
            addPlatform() {
                if(this.newPlatformName) {
                    this.platforms.push({name: this.newPlatformName, type: this.newPlatformType, active: true, users: 0});
                    this.showPlatformModal = false;
                    this.newPlatformName = '';
                }
            },
            tenants: [
                {name: 'Shop Thời Trang A', owner: 'shopA@gmail.com', plan: 'ENTERPRISE', status: 'Active', rev: 500},
                {name: 'Trà Sữa C', owner: 'trasua@gmail.com', plan: 'PRO', status: 'Active', rev: 99},
                {name: 'Nội Thất X', owner: 'noithat@gmail.com', plan: 'FREE TRIAL', status: 'Locked', rev: 0}
            ]
        }">
            <!-- HEADER -->
            <div class="mb-8 p-8 bg-gradient-to-r from-[#FFD700]/20 to-[#0A0A0A] border border-[#FFD700]/50 rounded-3xl relative overflow-hidden shadow-[0_0_50px_rgba(255,215,0,0.1)]">
                <div class="absolute right-0 top-0 opacity-10"><span class="material-symbols-outlined text-[200px] text-[#FFD700]">admin_panel_settings</span></div>
                <h1 class="text-3xl font-display font-bold text-[#FFD700] mb-2 flex items-center gap-3">
                    <span class="material-symbols-outlined text-4xl">local_police</span> SUPER ADMIN DASHBOARD
                </h1>
                <p class="text-slate-300">Trung tâm Điều khiển Lõi & Quản trị Thanh toán Siêu Cao Cấp toàn hệ thống.</p>
            </div>

            <!-- TAB NAVIGATION -->
            <div class="mb-8 flex gap-2 border-b border-white/10 overflow-x-auto custom-scrollbar whitespace-nowrap">
                <button @click="activeTab = 'overview'" :class="activeTab === 'overview' ? 'bg-[#FFD700] text-black shadow-[0_0_15px_rgba(255,215,0,0.5)]' : 'text-slate-400 hover:bg-white/5'" class="px-6 py-3 font-bold text-sm rounded-t-xl transition-all flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">query_stats</span> TỔNG QUAN & DÒNG TIỀN</button>
                <button @click="activeTab = 'platforms'" :class="activeTab === 'platforms' ? 'bg-[#FFD700] text-black shadow-[0_0_15px_rgba(255,215,0,0.5)]' : 'text-slate-400 hover:bg-white/5'" class="px-6 py-3 font-bold text-sm rounded-t-xl transition-all flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">extension</span> QUẢN LÝ NỀN TẢNG (APP STORE)</button>
                <button @click="activeTab = 'tenants'" :class="activeTab === 'tenants' ? 'bg-[#FFD700] text-black shadow-[0_0_15px_rgba(255,215,0,0.5)]' : 'text-slate-400 hover:bg-white/5'" class="px-6 py-3 font-bold text-sm rounded-t-xl transition-all flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">corporate_fare</span> DANH SÁCH KHÁCH HÀNG (TENANTS)</button>
                <button @click="activeTab = 'whitelabel'" :class="activeTab === 'whitelabel' ? 'bg-[#FFD700] text-black shadow-[0_0_15px_rgba(255,215,0,0.5)]' : 'text-slate-400 hover:bg-white/5'" class="px-6 py-3 font-bold text-sm rounded-t-xl transition-all flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">branding_watermark</span> WHITE-LABEL & ĐẠI LÝ</button>
            </div>

            <!-- TAB 1: OVERVIEW & BILLING -->
            <div x-show="activeTab === 'overview'" class="space-y-6">
                <!-- Metrics Khổng Lồ -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="p-8 bg-[#121214] border border-[#10B981]/30 rounded-3xl relative overflow-hidden text-center">
                        <div class="text-slate-400 font-bold mb-2 uppercase tracking-widest text-xs">Tổng Doanh Thu Hệ Thống (MRR)</div>
                        <div class="text-5xl font-display font-black text-[#10B981] mb-2">$124,500</div>
                        <div class="text-sm text-green-400 flex items-center justify-center gap-1"><span class="material-symbols-outlined text-sm">trending_up</span> +15.4% so với tháng trước</div>
                    </div>
                    <div class="p-8 bg-[#121214] border border-[#00F0FF]/30 rounded-3xl relative overflow-hidden text-center">
                        <div class="text-slate-400 font-bold mb-2 uppercase tracking-widest text-xs">Tổng Doanh Nghiệp (Tenants)</div>
                        <div class="text-5xl font-display font-black text-[#00F0FF] mb-2">1,205</div>
                        <div class="text-sm text-slate-400">Đang hoạt động trên nền tảng</div>
                    </div>
                    <div class="p-8 bg-[#121214] border border-[#FFD700]/30 rounded-3xl relative overflow-hidden text-center">
                        <div class="text-slate-400 font-bold mb-2 uppercase tracking-widest text-xs">Chi Phí Server & AI API</div>
                        <div class="text-5xl font-display font-black text-[#FFD700] mb-2">$12,300</div>
                        <div class="text-sm text-slate-400">Claude API & AWS Cloud</div>
                    </div>
                </div>

                <!-- Cấu hình Gói Cước Siêu Cao Cấp -->
                <div class="p-8 bg-[#121214] border border-white/5 rounded-3xl">
                    <h2 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-[#FFD700]">payments</span> Cấu Hình Gói Cước Khách Hàng (Pricing Plans)</h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="p-6 border border-white/10 rounded-2xl bg-white/5">
                            <h3 class="font-bold text-lg mb-2">Gói FREE TRIAL</h3>
                            <div class="text-3xl font-black text-white mb-4">$0 <span class="text-sm font-normal text-slate-400">/tháng</span></div>
                            <ul class="text-sm text-slate-400 space-y-2 mb-6"><li>✓ Giới hạn 100 tin nhắn AI</li><li>✓ Chỉ 1 Nhân viên</li></ul>
                            <button class="w-full py-2 bg-white/10 text-white font-bold rounded-xl hover:bg-white/20">Chỉnh Sửa Giới Hạn</button>
                        </div>
                        <div class="p-6 border border-[#00F0FF]/50 rounded-2xl bg-[#00F0FF]/5 relative">
                            <div class="absolute top-0 right-0 bg-[#00F0FF] text-black text-[10px] font-bold px-2 py-1 rounded-bl-lg rounded-tr-xl uppercase">Phổ Biến Nhất</div>
                            <h3 class="font-bold text-lg mb-2 text-[#00F0FF]">Gói PRO</h3>
                            <div class="text-3xl font-black text-white mb-4">$99 <span class="text-sm font-normal text-slate-400">/tháng</span></div>
                            <ul class="text-sm text-slate-400 space-y-2 mb-6"><li>✓ 10,000 tin nhắn AI</li><li>✓ Không giới hạn nhân viên</li></ul>
                            <button class="w-full py-2 bg-[#00F0FF] text-black font-bold rounded-xl hover:bg-cyan-400">Chỉnh Sửa Giới Hạn</button>
                        </div>
                        <div class="p-6 border border-[#FFD700]/50 rounded-2xl bg-[#FFD700]/5">
                            <h3 class="font-bold text-lg mb-2 text-[#FFD700]">Gói ENTERPRISE</h3>
                            <div class="text-3xl font-black text-white mb-4">$500+ <span class="text-sm font-normal text-slate-400">/tháng</span></div>
                            <ul class="text-sm text-slate-400 space-y-2 mb-6"><li>✓ Tùy chỉnh LLM Server riêng</li><li>✓ Khách hàng VIP</li></ul>
                            <button class="w-full py-2 bg-[#FFD700] text-black font-bold rounded-xl hover:bg-yellow-400">Chỉnh Sửa Giới Hạn</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: QUẢN LÝ NỀN TẢNG (NÚT THÊM NỀN TẢNG NGƯỜI DÙNG VÀO ADMIN) -->
            <div x-show="activeTab === 'platforms'" style="display:none;" class="space-y-6">
                <div class="flex justify-between items-center bg-[#121214] p-6 rounded-3xl border border-white/5">
                    <div>
                        <h2 class="text-xl font-bold flex items-center gap-2"><span class="material-symbols-outlined text-[#00F0FF]">apps</span> Kho Ứng Dụng & Nền Tảng (App Store Admin)</h2>
                        <p class="text-sm text-slate-400 mt-1">Quản lý các nền tảng (Facebook, Shopee,...) để cấp quyền cho User kết nối.</p>
                    </div>
                    <!-- ĐÂY LÀ NÚT THÊM NỀN TẢNG -->
                    <button @click="showPlatformModal = true" class="px-6 py-3 bg-[#00F0FF] text-black font-bold rounded-xl hover:bg-cyan-400 shadow-[0_0_15px_rgba(0,240,255,0.3)] flex items-center gap-2">
                        <span class="material-symbols-outlined">add_circle</span> Thêm Nền Tảng Mới Vào Hệ Thống
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 xl:grid-cols-4 gap-6">
                    <template x-for="(plat, idx) in platforms" :key="idx">
                        <div class="bg-[#121214] border border-white/5 rounded-2xl p-6 relative">
                            <div class="flex justify-between items-start mb-4">
                                <div class="w-12 h-12 bg-white/10 rounded-xl flex items-center justify-center font-bold text-xl uppercase" x-text="plat.name.substring(0,2)"></div>
                                <div class="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in cursor-pointer" @click="plat.active = !plat.active">
                                    <div :class="plat.active ? 'bg-green-500' : 'bg-slate-600'" class="w-10 h-6 rounded-full shadow-inner transition-colors"></div>
                                    <div :class="plat.active ? 'translate-x-4 bg-white' : 'translate-x-0 bg-slate-300'" class="absolute w-4 h-4 rounded-full shadow inset-y-0 left-1 top-1 transition-transform"></div>
                                </div>
                            </div>
                            <h3 class="font-bold text-lg text-white mb-1" x-text="plat.name"></h3>
                            <p class="text-xs text-slate-400 mb-4" x-text="plat.type"></p>
                            <div class="pt-4 border-t border-white/5 flex justify-between items-center text-sm">
                                <span class="text-slate-500">Đang sử dụng:</span>
                                <span class="font-bold text-[#00F0FF]" x-text="plat.users + ' Doanh nghiệp'"></span>
                            </div>
                        </div>
                    </template>
                </div>
            </div>

            <!-- MODAL THÊM NỀN TẢNG -->
            <div x-show="showPlatformModal" style="display:none;" class="fixed inset-0 bg-black/90 flex items-center justify-center z-50 backdrop-blur-sm">
                <div class="bg-[#121214] border border-[#00F0FF]/30 p-8 rounded-3xl w-[500px] shadow-[0_0_50px_rgba(0,240,255,0.1)] relative" @click.outside="showPlatformModal = false">
                    <h3 class="text-2xl font-bold mb-2 text-[#00F0FF]">Thêm Nền Tảng Kết Nối Mới</h3>
                    <p class="text-sm text-slate-400 mb-6">Cấu hình API gốc để cấp phép cho toàn bộ các Tenant.</p>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Tên Nền Tảng (Ví dụ: Telegram, Line...)</label>
                            <input x-model="newPlatformName" type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none focus:border-[#00F0FF] text-white">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Phân loại</label>
                            <select x-model="newPlatformType" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none focus:border-[#00F0FF] text-white">
                                <option>Social Messaging</option>
                                <option>E-commerce Platform</option>
                                <option>Payment Gateway</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Client ID / App ID</label>
                            <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none text-white" placeholder="Bắt buộc...">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Client Secret / App Secret</label>
                            <input type="password" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none text-white" placeholder="Bắt buộc...">
                        </div>
                        <div class="flex gap-4 justify-end mt-8">
                            <button @click="showPlatformModal = false" class="px-6 py-3 text-sm font-bold text-slate-400 hover:text-white">Hủy</button>
                            <button @click="addPlatform()" class="px-8 py-3 bg-[#00F0FF] text-black font-bold rounded-xl text-sm hover:bg-cyan-400 shadow-[0_0_15px_rgba(0,240,255,0.3)]">Lưu Nền Tảng Lõi</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: DANH SÁCH TENANTS (GIỮ LẠI TỪ BẢN CŨ NHƯNG ĐẸP HƠN) -->
            <div x-show="activeTab === 'tenants'" style="display:none;" class="p-8 bg-[#121214] border border-white/5 rounded-3xl">
                <div class="flex justify-between items-center mb-6">
                    <h2 class="text-xl font-bold">Quản Lý Toàn Bộ Khách Hàng (Tenants)</h2>
                    <input type="text" placeholder="Tìm kiếm theo email, domain..." class="bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm w-64 text-white">
                </div>
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-4">Tên Doanh Nghiệp</th><th class="px-4 py-4">Chủ Sở Hữu</th><th class="px-4 py-4">Gói (Plan)</th><th class="px-4 py-4">Doanh Thu Mang Lại</th><th class="px-4 py-4">Trạng Thái</th><th class="px-4 py-4 text-right">Khóa Khẩn Cấp</th></tr>
                    </thead>
                    <tbody>
                        <template x-for="(t, index) in tenants" :key="index">
                            <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                <td class="px-4 py-4 font-bold text-white" x-text="t.name"></td>
                                <td class="px-4 py-4" x-text="t.owner"></td>
                                <td class="px-4 py-4"><span class="px-2 py-1 bg-[#FFD700]/10 text-[#FFD700] rounded text-[10px] font-bold" x-text="t.plan"></span></td>
                                <td class="px-4 py-4 text-[#10B981] font-bold" x-text="'$' + t.rev + '/tháng'"></td>
                                <td class="px-4 py-4">
                                    <span x-show="t.status === 'Active'" class="text-green-400 text-xs flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-green-500"></span> Active</span>
                                    <span x-show="t.status === 'Locked'" class="text-red-400 text-xs flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-red-500"></span> Locked</span>
                                </td>
                                <td class="px-4 py-4 text-right">
                                    <button @click="t.status = t.status === 'Active' ? 'Locked' : 'Active'" class="text-red-400 hover:text-red-500 text-xs font-bold px-3 py-1 bg-red-500/10 rounded" x-text="t.status === 'Active' ? 'Khóa Dịch Vụ' : 'Mở Khóa'"></button>
                                </td>
                            </tr>
                        </template>
                    </tbody>
                </table>
            </div>

            <!-- TAB 4: WHITE-LABEL -->
            <div x-show="activeTab === 'whitelabel'" style="display:none;" class="p-8 bg-[#121214] border border-white/5 rounded-3xl">
                <h2 class="text-xl font-bold mb-6">Cấu Hình White-label (Bán Lại Dưới Tên Thương Hiệu Khác)</h2>
                <div class="grid grid-cols-2 gap-8">
                    <div class="space-y-4">
                        <label class="block text-xs font-bold text-slate-400">Tên Nền Tảng (Logo Text)</label>
                        <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white" value="CHỐT NGHÌN ĐƠN">
                        
                        <label class="block text-xs font-bold text-slate-400 pt-4">Tên miền tùy chỉnh (Custom Domain)</label>
                        <div class="flex gap-2">
                            <input type="text" class="flex-1 bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white" value="app.chotnghindon.com">
                            <button class="bg-[#10B981] px-4 rounded-xl font-bold text-black text-sm">Verify DNS</button>
                        </div>
                    </div>
                    <div class="border-2 border-dashed border-white/10 rounded-2xl flex flex-col items-center justify-center p-8 text-center">
                        <span class="material-symbols-outlined text-6xl text-slate-600 mb-4">image</span>
                        <p class="font-bold text-white mb-1">Tải Logo Hệ Thống</p>
                        <p class="text-xs text-slate-500">Đề xuất: 500x500px, nền trong suốt PNG</p>
                    </div>
                </div>
            </div>
        </div>
'''

TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>CHỐT NGHÌN ĐƠN SUPER ADMIN</title>
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
    <style>
        .custom-scrollbar::-webkit-scrollbar { width: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 10px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }
    </style>
</head>
<body>
    <div id="root"></div>
    <script src="js/layout.js"></script>
    <script>
        const content = `{CONTENT}`;
        document.addEventListener('DOMContentLoaded', () => {
            renderLayout('admin_panel', content);
        });
    </script>
</body>
</html>'''

escaped_content = admin_html_content.replace("`", "\\`").replace("${", "\\${")
final_html = TEMPLATE.replace('{CONTENT}', escaped_content)

with open('admin_panel.html', 'w') as f:
    f.write(final_html)

print("Đã hoàn thành Đập Đi Xây Lại Super Admin Dashboard (Quản trị thanh toán cao cấp & Thêm nền tảng hệ thống).")
