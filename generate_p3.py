import os

PAGES = [
    ('channels.html', 'channels', '''
        <div x-data="{ 
            fbConnected: true, 
            zaloConnected: false, 
            webConnected: true,
            tiktokConnected: false,
            shopeeConnected: true,
            lazadaConnected: false,
            igConnected: false
        }">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-[#00F0FF]">hub</span> Trung Tâm Kết Nối Đa Kênh (Omnichannel)</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Facebook -->
                <div class="p-6 bg-[#121214] border border-blue-500/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-blue-500 rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined text-white text-3xl">forum</span></div>
                    <h3 class="text-lg font-bold text-white mb-2">Facebook</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Messenger & Bình luận Fanpage</p>
                    <template x-if="fbConnected"><button @click="fbConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!fbConnected"><button @click="fbConnected = true" class="w-full py-2 bg-blue-500 text-white font-bold rounded-xl text-sm">Kết Nối Ngay</button></template>
                </div>
                
                <!-- Zalo -->
                <div class="p-6 bg-[#121214] border border-blue-400/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-blue-400 rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined text-white text-3xl">chat</span></div>
                    <h3 class="text-lg font-bold text-white mb-2">Zalo OA</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Zalo Official Account & ZNS</p>
                    <template x-if="zaloConnected"><button @click="zaloConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!zaloConnected"><button @click="zaloConnected = true" class="w-full py-2 bg-blue-400 text-white font-bold rounded-xl text-sm">Kết Nối Ngay</button></template>
                </div>

                <!-- Tiktok Shop -->
                <div class="p-6 bg-[#121214] border border-white/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-white text-black rounded-full flex items-center justify-center mb-4 font-bold text-xl">TT</div>
                    <h3 class="text-lg font-bold text-white mb-2">TikTok Shop</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Quản lý tin nhắn & Đơn hàng Tiktok</p>
                    <template x-if="tiktokConnected"><button @click="tiktokConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!tiktokConnected"><button @click="tiktokConnected = true" class="w-full py-2 bg-white text-black font-bold rounded-xl text-sm">Kết Nối Ngay</button></template>
                </div>

                <!-- Shopee -->
                <div class="p-6 bg-[#121214] border border-[#EE4D2D]/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-[#EE4D2D] text-white rounded-full flex items-center justify-center mb-4 font-bold text-xl">S</div>
                    <h3 class="text-lg font-bold text-white mb-2">Shopee</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Đồng bộ tin nhắn Shopee Chat</p>
                    <template x-if="shopeeConnected"><button @click="shopeeConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!shopeeConnected"><button @click="shopeeConnected = true" class="w-full py-2 bg-[#EE4D2D] text-white font-bold rounded-xl text-sm">Kết Nối Ngay</button></template>
                </div>

                <!-- Lazada -->
                <div class="p-6 bg-[#121214] border border-[#0F146D]/50 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-gradient-to-r from-[#F53D2D] to-[#0F146D] text-white rounded-full flex items-center justify-center mb-4 font-bold text-xl">L</div>
                    <h3 class="text-lg font-bold text-white mb-2">Lazada</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Tích hợp Shop Assistant Lazada</p>
                    <template x-if="lazadaConnected"><button @click="lazadaConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!lazadaConnected"><button @click="lazadaConnected = true" class="w-full py-2 bg-gradient-to-r from-[#F53D2D] to-[#0F146D] text-white font-bold rounded-xl text-sm">Kết Nối Ngay</button></template>
                </div>

                <!-- Instagram -->
                <div class="p-6 bg-[#121214] border border-[#E1306C]/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-gradient-to-tr from-[#F56040] to-[#833AB4] text-white rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined text-2xl">photo_camera</span></div>
                    <h3 class="text-lg font-bold text-white mb-2">Instagram</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Instagram Direct Message (IG DM)</p>
                    <template x-if="igConnected"><button @click="igConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!igConnected"><button @click="igConnected = true" class="w-full py-2 bg-gradient-to-r from-[#F56040] to-[#833AB4] text-white font-bold rounded-xl text-sm">Kết Nối Ngay</button></template>
                </div>

                <!-- Web Livechat -->
                <div class="p-6 bg-[#121214] border border-[#10B981]/30 rounded-2xl flex flex-col items-center text-center lg:col-span-2">
                    <div class="w-14 h-14 bg-[#10B981] text-black rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined text-2xl">language</span></div>
                    <h3 class="text-lg font-bold text-white mb-2">Web Live Chat (Mã Nhúng JS)</h3>
                    <p class="text-xs text-slate-400 mb-4">Gắn đoạn mã sau vào thẻ &lt;head&gt; trên website của bạn để hiển thị bong bóng chat.</p>
                    <div class="w-full bg-[#0A0A0A] border border-white/10 p-3 rounded-xl text-left relative">
                        <code class="text-xs text-[#10B981] break-all">&lt;script src="https://chotnghindon.com/widget.js" tenant-id="12345" defer&gt;&lt;/script&gt;</code>
                        <button class="absolute top-2 right-2 p-1 bg-white/10 rounded hover:bg-white/20"><span class="material-symbols-outlined text-sm">content_copy</span></button>
                    </div>
                </div>
            </div>
        </div>
    '''),

    ('ecommerce.html', 'ecommerce', '''
        <div x-data="{ activeTab: 'orders' }">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-[#FFD700]">storefront</span> Quản Lý Bán Hàng Điện Tử</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5 overflow-x-auto custom-scrollbar whitespace-nowrap">
                <button @click="activeTab = 'orders'" :class="activeTab === 'orders' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Đơn Hàng</button>
                <button @click="activeTab = 'inventory'" :class="activeTab === 'inventory' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Sản Phẩm & Tồn Kho</button>
                <button @click="activeTab = 'shipping'" :class="activeTab === 'shipping' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Đối Tác Vận Chuyển</button>
                <button @click="activeTab = 'payment'" :class="activeTab === 'payment' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Cổng Thanh Toán</button>
            </div>

            <!-- Tabs cũ giữ nguyên -->
            <div x-show="activeTab === 'orders'" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Mã Đơn</th><th class="px-4 py-3">Khách Hàng</th><th class="px-4 py-3">Nguồn</th><th class="px-4 py-3">Trạng Thái</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5"><td class="px-4 py-3 font-bold">#ORD-999</td><td class="px-4 py-3">Nguyễn Văn A</td><td class="px-4 py-3"><span class="px-2 py-0.5 bg-[#EE4D2D]/20 text-[#EE4D2D] rounded text-xs">Shopee</span></td><td class="px-4 py-3"><span class="text-[#FFD700] text-xs">Đang giao</span></td></tr>
                    </tbody>
                </table>
            </div>

            <div x-show="activeTab === 'inventory'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Tên Sản Phẩm</th><th class="px-4 py-3">Tồn Kho Kho Bãi</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5"><td class="px-4 py-3 font-bold">Áo Thun Basic M</td><td class="px-4 py-3 font-bold text-red-400">2 (Sắp hết)</td></tr>
                    </tbody>
                </table>
            </div>

            <!-- TAB MỚI: VẬN CHUYỂN -->
            <div x-show="activeTab === 'shipping'" style="display:none;" class="grid grid-cols-1 md:grid-cols-3 gap-6">
                 <div class="p-6 bg-[#121214] border border-green-500/30 rounded-2xl flex flex-col items-center">
                    <div class="w-16 h-16 bg-green-500 text-white rounded-xl flex items-center justify-center font-bold text-xl mb-4">GHTK</div>
                    <h3 class="font-bold text-white mb-2">Giao Hàng Tiết Kiệm</h3>
                    <button class="w-full mt-4 py-2 bg-green-500/20 text-green-400 border border-green-500/30 font-bold rounded-xl text-sm">Đã Kết Nối</button>
                 </div>
                 <div class="p-6 bg-[#121214] border border-orange-500/30 rounded-2xl flex flex-col items-center">
                    <div class="w-16 h-16 bg-orange-500 text-white rounded-xl flex items-center justify-center font-bold text-xl mb-4">GHN</div>
                    <h3 class="font-bold text-white mb-2">Giao Hàng Nhanh</h3>
                    <button class="w-full mt-4 py-2 bg-white/5 text-slate-300 hover:bg-orange-500 hover:text-white font-bold rounded-xl text-sm transition-colors">Kết Nối Ngay</button>
                 </div>
                 <div class="p-6 bg-[#121214] border border-red-500/30 rounded-2xl flex flex-col items-center">
                    <div class="w-16 h-16 bg-red-600 text-white rounded-xl flex items-center justify-center font-bold text-xl mb-4">VTP</div>
                    <h3 class="font-bold text-white mb-2">Viettel Post</h3>
                    <button class="w-full mt-4 py-2 bg-white/5 text-slate-300 hover:bg-red-600 hover:text-white font-bold rounded-xl text-sm transition-colors">Kết Nối Ngay</button>
                 </div>
            </div>

            <!-- TAB MỚI: THANH TOÁN -->
            <div x-show="activeTab === 'payment'" style="display:none;" class="grid grid-cols-1 md:grid-cols-3 gap-6">
                 <div class="p-6 bg-[#121214] border border-blue-500/30 rounded-2xl flex flex-col items-center">
                    <div class="w-full py-4 text-center font-bold text-2xl text-blue-500 tracking-wider mb-4 border-b border-white/5">VNPAY</div>
                    <h3 class="font-bold text-white mb-2">Cổng VNPay</h3>
                    <button class="w-full mt-4 py-2 bg-blue-500/20 text-blue-400 border border-blue-500/30 font-bold rounded-xl text-sm">Đã Kết Nối</button>
                 </div>
                 <div class="p-6 bg-[#121214] border border-pink-500/30 rounded-2xl flex flex-col items-center">
                    <div class="w-full py-4 text-center font-bold text-2xl text-pink-500 tracking-wider mb-4 border-b border-white/5">MoMo</div>
                    <h3 class="font-bold text-white mb-2">Ví Điện Tử MoMo</h3>
                    <button class="w-full mt-4 py-2 bg-white/5 text-slate-300 hover:bg-pink-500 hover:text-white font-bold rounded-xl text-sm transition-colors">Kết Nối Ngay</button>
                 </div>
                 <div class="p-6 bg-[#121214] border border-purple-500/30 rounded-2xl flex flex-col items-center">
                    <div class="w-full py-4 text-center font-bold text-2xl text-purple-500 tracking-wider mb-4 border-b border-white/5">stripe</div>
                    <h3 class="font-bold text-white mb-2">Stripe (Quốc Tế)</h3>
                    <button class="w-full mt-4 py-2 bg-white/5 text-slate-300 hover:bg-purple-500 hover:text-white font-bold rounded-xl text-sm transition-colors">Kết Nối Ngay</button>
                 </div>
            </div>
        </div>
    '''),

    ('team_management.html', 'team_management', '''
        <div x-data="{ 
            users: [
                {email: 'quocthiencr7@gmail.com', role: 'Tenant Admin', online: true, resolved: 1205, speed: 0.8},
                {email: 'sale1@gmail.com', role: 'Agent', online: false, resolved: 342, speed: 1.5}
            ],
            newEmail: '',
            newRole: 'Agent',
            addUser() {
                if(this.newEmail) {
                    this.users.push({ email: this.newEmail, role: this.newRole, online: true, resolved: 0, speed: 0 });
                    this.newEmail = '';
                }
            },
            removeUser(index) {
                if(confirm('Xác nhận xóa?')) this.users.splice(index, 1);
            }
        }">
            <div class="flex justify-between items-center mb-6">
                <div>
                    <h2 class="text-xl font-bold flex items-center gap-2"><span class="material-symbols-outlined text-primary">groups</span> Quản Lý Đội Ngũ & Hiệu Suất (KPI)</h2>
                </div>
            </div>

            <div class="grid grid-cols-1 xl:grid-cols-4 gap-6">
                <div class="xl:col-span-1 bg-[#121214] border border-white/5 rounded-2xl p-6 h-fit">
                    <h3 class="font-bold text-sm mb-4">Thêm Nhân Viên</h3>
                    <div class="space-y-4">
                        <input x-model="newEmail" type="email" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white" placeholder="Email...">
                        <select x-model="newRole" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white">
                            <option>Manager</option><option>Agent</option>
                        </select>
                        <button @click="addUser()" class="w-full py-2 bg-primary text-[#0A0A0A] rounded-xl font-bold text-sm">Gửi Lời Mời</button>
                    </div>
                </div>

                <div class="xl:col-span-3 bg-[#121214] border border-white/5 rounded-2xl overflow-x-auto">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                            <tr>
                                <th class="px-6 py-4">Tài Khoản</th>
                                <th class="px-6 py-4">Vai Trò</th>
                                <th class="px-6 py-4 text-center">ĐH Chốt Thành Công</th>
                                <th class="px-6 py-4 text-center">Tốc Độ Phản Hồi</th>
                                <th class="px-6 py-4 text-right">Hành Động</th>
                            </tr>
                        </thead>
                        <tbody>
                            <template x-for="(user, index) in users" :key="index">
                                <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                    <td class="px-6 py-4 font-bold text-white flex items-center gap-3">
                                        <div class="relative">
                                            <div class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center text-xs uppercase" x-text="user.email.charAt(0)"></div>
                                            <span x-show="user.online" class="absolute bottom-0 right-0 w-2.5 h-2.5 bg-green-500 border-2 border-[#121214] rounded-full"></span>
                                        </div>
                                        <span x-text="user.email"></span>
                                    </td>
                                    <td class="px-6 py-4"><span class="px-2 py-1 bg-white/10 rounded text-[10px] font-bold" x-text="user.role"></span></td>
                                    <td class="px-6 py-4 text-center font-bold text-[#FFD700]" x-text="user.resolved + ' đơn'"></td>
                                    <td class="px-6 py-4 text-center font-bold text-[#10B981]" x-text="user.speed + ' giây'"></td>
                                    <td class="px-6 py-4 text-right">
                                        <button @click="removeUser(index)" class="text-red-400 text-xs font-bold" x-show="user.role !== 'Tenant Admin'">Xóa</button>
                                    </td>
                                </tr>
                            </template>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    ''')
]

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
            renderLayout('{ID}', content);
        });
    </script>
</body>
</html>'''

for html_file, page_id, content in PAGES:
    escaped_content = content.replace("`", "\\`").replace("${", "\\${")
    final_html = TEMPLATE.replace('{CONTENT}', escaped_content).replace('{ID}', page_id)
    with open(html_file, 'w') as f:
        f.write(final_html)

print("Đã bơm thêm Tiktok, Shopee, Lazada, GHTK, GHN, VNPay, Momo vào hệ thống.")
