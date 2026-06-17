import os

PAGES = [
    ('dashboard.html', 'dashboard', '''
        <div x-data="{ count: 12450 }">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                <div class="p-5 bg-[#121214] border border-white/5 rounded-2xl relative overflow-hidden">
                    <div class="absolute top-0 right-0 p-3 opacity-10"><span class="material-symbols-outlined text-5xl text-[#00F0FF]">chat</span></div>
                    <div class="text-xs text-slate-400 mb-1 uppercase tracking-wider">Tổng Hội Thoại</div>
                    <div class="text-2xl font-display font-bold text-[#00F0FF]" x-text="count.toLocaleString()"></div>
                    <div class="text-[10px] text-primary mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">trending_up</span> +15% tuần này</div>
                </div>
                <!-- ... other stat boxes ... -->
            </div>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[600px]">
                <div class="bg-[#121214] border border-white/5 rounded-2xl flex flex-col overflow-hidden">
                    <div class="p-4 border-b border-white/5 flex justify-between items-center bg-white/5">
                        <h3 class="font-bold text-sm">Inbox Đa Kênh</h3>
                    </div>
                    <div class="flex-1 overflow-y-auto custom-scrollbar p-2 space-y-2">
                        <div class="p-3 bg-white/5 rounded-xl cursor-pointer hover:bg-white/10 border-l-2 border-[#00F0FF]">
                            <div class="flex justify-between items-start mb-1">
                                <span class="font-bold text-sm text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-blue-500"></span> Nguyễn Văn A</span>
                                <span class="text-[10px] text-slate-500">Vừa xong</span>
                            </div>
                            <p class="text-xs text-slate-400 truncate">Sản phẩm này còn màu đen size M không shop?</p>
                        </div>
                    </div>
                </div>

                <div class="bg-[#121214] border border-white/5 rounded-2xl flex flex-col overflow-hidden lg:col-span-2 relative">
                    <div class="p-4 border-b border-white/5 flex justify-between items-center bg-white/5">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 bg-slate-700 rounded-full"></div>
                            <div>
                                <div class="font-bold text-sm">Nguyễn Văn A</div>
                                <div class="text-[10px] text-slate-400">Facebook Messenger</div>
                            </div>
                        </div>
                    </div>
                    <div class="flex-1 overflow-y-auto p-4 space-y-4">
                        <div class="flex justify-start">
                            <div class="max-w-[70%] bg-white/5 rounded-2xl rounded-tl-none p-3 text-sm text-slate-300">
                                Sản phẩm này còn màu đen size M không shop?
                            </div>
                        </div>
                        <div class="flex justify-end">
                            <div class="max-w-[70%] bg-gradient-to-r from-primary to-[#10B981]/80 text-[#0A0A0A] rounded-2xl rounded-tr-none p-3 text-sm font-medium">
                                Dạ chào anh A, sản phẩm Quần Jeans mã 01 màu Đen size M bên em vẫn còn hàng ạ.
                            </div>
                        </div>
                    </div>
                    <div class="p-4 border-t border-white/5 bg-white/5 flex gap-2">
                        <input type="text" class="flex-1 bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-[#00F0FF]" placeholder="Nhập tin nhắn..." @keyup.enter="$event.target.value=''; count++">
                        <button class="p-2 text-[#00F0FF]"><span class="material-symbols-outlined text-[20px]">send</span></button>
                    </div>
                </div>
            </div>
        </div>
    '''),

    ('bot_builder.html', 'bot_builder', '''
        <div x-data="{ activeTab: 'prompt', showToast: false }">
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'prompt'" :class="activeTab === 'prompt' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">System Prompt</button>
                <button @click="activeTab = 'flow'" :class="activeTab === 'flow' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Flow Builder</button>
                <button @click="activeTab = 'rag'" :class="activeTab === 'rag' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Knowledge Base (RAG)</button>
            </div>

            <!-- Toast -->
            <div x-show="showToast" x-transition.opacity.duration.500ms class="fixed top-20 right-8 bg-green-500 text-white px-4 py-2 rounded-lg font-bold text-sm shadow-lg z-50">
                Lưu cấu hình thành công!
            </div>

            <div x-show="activeTab === 'prompt'" class="p-6 bg-[#121214] border border-[#7B2DFF]/20 rounded-2xl min-h-[500px] relative shadow-[0_0_40px_rgba(123,45,255,0.05)]">
                <div class="absolute top-0 right-0 w-64 h-64 bg-[#7B2DFF]/10 rounded-full blur-[80px] pointer-events-none"></div>
                <div class="flex justify-between items-start mb-6">
                    <div>
                        <h2 class="text-xl font-bold flex items-center gap-2"><span class="material-symbols-outlined text-[#7B2DFF]">psychology</span> Cấu Hình Tính Cách Claude AI</h2>
                        <p class="text-sm text-slate-400 mt-1">Định hình cách bot tư vấn, chốt sale.</p>
                    </div>
                    <button @click="showToast = true; setTimeout(() => showToast = false, 3000)" class="px-6 py-2 bg-gradient-to-r from-primary to-[#7B2DFF] rounded-xl font-bold text-sm flex items-center gap-2 hover:opacity-90 transition-opacity">
                        <span class="material-symbols-outlined text-[18px]">save</span> Lưu Cấu Hình Bot
                    </button>
                </div>
                <div class="space-y-4 relative z-10">
                    <div>
                        <label class="block text-xs font-bold text-slate-300 mb-2">Vai Trò (Role)</label>
                        <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white" value="Chuyên gia bán hàng">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-300 mb-2">Quy tắc ứng xử</label>
                        <textarea class="w-full h-40 bg-[#0A0A0A] border border-white/10 rounded-xl p-4 text-sm text-white custom-scrollbar">Luôn chào khách và tư vấn chốt đơn.</textarea>
                    </div>
                </div>
            </div>

            <div x-show="activeTab === 'flow'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[500px] flex items-center justify-center">
                <div class="text-center">
                    <span class="material-symbols-outlined text-6xl text-[#00F0FF] mb-4">account_tree</span>
                    <h2 class="text-2xl font-bold text-white mb-2">Kịch Bản Kéo Thả Trực Quan</h2>
                    <p class="text-slate-400">Xây dựng luồng quyết định cho AI trước khi gọi Claude API.</p>
                </div>
            </div>

            <div x-show="activeTab === 'rag'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[500px]">
                <h2 class="text-xl font-bold mb-4">Kho Dữ Liệu RAG (Tài Liệu Đào Tạo)</h2>
                <div class="border-2 border-dashed border-white/10 rounded-xl p-10 flex items-center justify-center text-center cursor-pointer hover:bg-white/5 transition-colors">
                    <div>
                        <span class="material-symbols-outlined text-4xl text-slate-500 mb-2">cloud_upload</span>
                        <p class="font-bold text-sm">Kéo thả file PDF, DOCX hoặc TXT vào đây</p>
                        <p class="text-xs text-slate-500 mt-1">Bot sẽ tự học các chính sách, bảo hành từ tài liệu này</p>
                    </div>
                </div>
            </div>
        </div>
    '''),

    ('team_management.html', 'team_management', '''
        <div x-data="{ 
            users: [
                {email: 'quocthiencr7@gmail.com', role: 'Tenant Admin', online: true},
                {email: 'sale1@gmail.com', role: 'Agent', online: false}
            ],
            newEmail: '',
            newRole: 'Agent',
            addUser() {
                if(this.newEmail) {
                    this.users.push({ email: this.newEmail, role: this.newRole, online: true });
                    this.newEmail = '';
                }
            },
            removeUser(index) {
                if(confirm('Bạn có chắc chắn muốn xóa nhân viên này?')) {
                    this.users.splice(index, 1);
                }
            }
        }">
            <div class="flex justify-between items-center mb-6">
                <div>
                    <h2 class="text-xl font-bold">Quản Lý Nhân Viên (Team)</h2>
                    <p class="text-sm text-slate-400 mt-1">Phân quyền, mời nhân viên mới vào vận hành hệ thống.</p>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="bg-[#121214] border border-white/5 rounded-2xl p-6 h-fit">
                    <h3 class="font-bold text-lg mb-4 flex items-center gap-2"><span class="material-symbols-outlined text-primary">person_add</span> Thêm Tài Khoản Mới</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Địa Chỉ Email</label>
                            <input x-model="newEmail" @keyup.enter="addUser()" type="email" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-primary" placeholder="nhanvien@gmail.com">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-2">Phân Quyền (Role)</label>
                            <select x-model="newRole" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-primary">
                                <option value="Manager">Manager</option>
                                <option value="Agent">Agent</option>
                                <option value="Viewer">Viewer</option>
                            </select>
                        </div>
                        <button @click="addUser()" class="w-full py-3 bg-primary text-[#0A0A0A] rounded-xl font-bold text-sm hover:bg-emerald-400 transition-colors mt-2">
                            Gửi Lời Mời Trực Tiếp
                        </button>
                    </div>
                </div>

                <div class="lg:col-span-2 bg-[#121214] border border-white/5 rounded-2xl overflow-hidden">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                            <tr>
                                <th class="px-6 py-4">Tài Khoản</th>
                                <th class="px-6 py-4">Vai Trò</th>
                                <th class="px-6 py-4">Trạng Thái</th>
                                <th class="px-6 py-4 text-right">Hành Động</th>
                            </tr>
                        </thead>
                        <tbody>
                            <template x-for="(user, index) in users" :key="index">
                                <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                    <td class="px-6 py-4 font-bold text-white flex items-center gap-3">
                                        <div class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center text-xs uppercase" x-text="user.email.charAt(0)"></div>
                                        <span x-text="user.email"></span>
                                    </td>
                                    <td class="px-6 py-4">
                                        <span class="px-2 py-1 bg-white/10 rounded text-[10px] font-bold uppercase border border-white/20" x-text="user.role"></span>
                                    </td>
                                    <td class="px-6 py-4">
                                        <span x-show="user.online" class="text-green-400 text-xs font-bold flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-green-500"></span> Online</span>
                                        <span x-show="!user.online" class="text-slate-500 text-xs flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-slate-500"></span> Offline</span>
                                    </td>
                                    <td class="px-6 py-4 text-right">
                                        <button @click="removeUser(index)" class="text-red-400 hover:text-red-500 text-xs font-bold" x-show="user.role !== 'Tenant Admin'">Xóa</button>
                                    </td>
                                </tr>
                            </template>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    '''),

    ('admin_panel.html', 'admin_panel', '''
        <div x-data="{
            tenants: [
                {name: 'Shop Thời Trang A', owner: 'shopA@gmail.com', plan: 'PRO', status: 'Active', cost: 12.50},
                {name: 'Trà Sữa C', owner: 'trasua@gmail.com', plan: 'FREE TRIAL', status: 'Locked', cost: 0.10}
            ],
            toggleStatus(index) {
                this.tenants[index].status = this.tenants[index].status === 'Active' ? 'Locked' : 'Active';
            }
        }">
            <div class="p-6 bg-[#121214] border border-[#FFD700]/20 rounded-2xl min-h-[500px] shadow-[0_0_30px_rgba(255,215,0,0.05)] relative overflow-hidden">
                <div class="absolute top-0 right-0 w-96 h-96 bg-[#FFD700]/5 rounded-full blur-[100px] pointer-events-none"></div>
                <div class="flex justify-between items-center mb-6 relative z-10">
                    <div>
                        <h2 class="text-xl font-bold flex items-center gap-2"><span class="material-symbols-outlined text-[#FFD700]">corporate_fare</span> Quản Lý Tất Cả Tenant</h2>
                        <p class="text-sm text-slate-400 mt-1">Danh sách doanh nghiệp sử dụng nền tảng CHỐT NGHÌN ĐƠN.</p>
                    </div>
                    <button @click="tenants.unshift({name: 'Cửa Hàng Mới', owner: 'new@gmail.com', plan: 'PRO', status: 'Active', cost: 0.0})" class="px-4 py-2 bg-[#FFD700] text-[#0A0A0A] font-bold rounded-lg hover:bg-yellow-400 transition-colors text-sm">+ Tạo Tenant Mới</button>
                </div>
                
                <div class="overflow-x-auto relative z-10">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                            <tr>
                                <th class="px-4 py-3">Tên Doanh Nghiệp</th>
                                <th class="px-4 py-3">Chủ Sở Hữu</th>
                                <th class="px-4 py-3">Gói (Plan)</th>
                                <th class="px-4 py-3">Chi Phí AI</th>
                                <th class="px-4 py-3">Trạng Thái</th>
                                <th class="px-4 py-3 text-right">Hành Động</th>
                            </tr>
                        </thead>
                        <tbody>
                            <template x-for="(t, index) in tenants" :key="index">
                                <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                    <td class="px-4 py-3 font-bold text-white" x-text="t.name"></td>
                                    <td class="px-4 py-3" x-text="t.owner"></td>
                                    <td class="px-4 py-3"><span class="px-2 py-1 bg-white/10 rounded text-[10px] font-bold" x-text="t.plan"></span></td>
                                    <td class="px-4 py-3 text-[#10B981]" x-text="'$' + t.cost.toFixed(2)"></td>
                                    <td class="px-4 py-3">
                                        <span x-show="t.status === 'Active'" class="px-2 py-1 bg-primary/20 text-primary rounded text-xs">Active</span>
                                        <span x-show="t.status === 'Locked'" class="px-2 py-1 bg-red-500/20 text-red-400 rounded text-xs">Locked</span>
                                    </td>
                                    <td class="px-4 py-3 text-right">
                                        <button @click="toggleStatus(index)" class="text-[#00F0FF] hover:underline text-xs font-bold mr-2" x-text="t.status === 'Active' ? 'Khóa' : 'Mở Khóa'"></button>
                                    </td>
                                </tr>
                            </template>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    '''),

    ('channels.html', 'channels', '''
        <div x-data="{ fbConnected: true, zaloConnected: false, webConnected: true }">
            <h2 class="text-xl font-bold mb-6">Kết Nối Kênh Bán Hàng</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Facebook -->
                <div class="p-6 bg-[#121214] border border-blue-500/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center mb-4">
                        <span class="material-symbols-outlined text-white text-3xl">forum</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-2">Facebook Messenger</h3>
                    <p class="text-xs text-slate-400 mb-6">Kết nối Fanpage để Bot tự động trả lời.</p>
                    
                    <template x-if="fbConnected">
                        <div class="w-full">
                            <div class="w-full flex justify-between items-center px-4 py-2 bg-blue-500/10 rounded-xl mb-4">
                                <span class="text-sm font-bold text-blue-400">Đang Kết Nối</span>
                                <span class="w-3 h-3 bg-green-500 rounded-full"></span>
                            </div>
                            <button @click="fbConnected = false" class="w-full py-2 text-sm font-bold text-red-400 hover:bg-white/5 rounded-xl">Ngắt Kết Nối</button>
                        </div>
                    </template>
                    <template x-if="!fbConnected">
                        <button @click="fbConnected = true" class="w-full py-3 bg-blue-500 text-white font-bold rounded-xl text-sm">Kết Nối Ngay</button>
                    </template>
                </div>
                
                <!-- Zalo -->
                <div class="p-6 bg-[#121214] border border-blue-400/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-blue-400 rounded-full flex items-center justify-center mb-4">
                        <span class="material-symbols-outlined text-white text-3xl">chat</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-2">Zalo Official Account</h3>
                    <p class="text-xs text-slate-400 mb-6">Tích hợp Zalo OA và gửi tin nhắn ZNS.</p>
                    
                    <template x-if="zaloConnected">
                        <div class="w-full">
                            <div class="w-full flex justify-between items-center px-4 py-2 bg-blue-400/10 rounded-xl mb-4">
                                <span class="text-sm font-bold text-blue-400">Đang Kết Nối</span>
                                <span class="w-3 h-3 bg-green-500 rounded-full"></span>
                            </div>
                            <button @click="zaloConnected = false" class="w-full py-2 text-sm font-bold text-red-400 hover:bg-white/5 rounded-xl">Ngắt Kết Nối</button>
                        </div>
                    </template>
                    <template x-if="!zaloConnected">
                        <button @click="zaloConnected = true" class="w-full py-3 bg-blue-400 text-white font-bold rounded-xl text-sm">Kết Nối Ngay</button>
                    </template>
                </div>
            </div>
        </div>
    '''),

    ('crm.html', 'crm', '''
        <div x-data="{ showModal: false, customers: [{name: 'Lương Thu C', phone: '0933111222', ltv: 5400000, vip: true}], newName: '', newPhone: '' }">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-xl font-bold">Quản Lý Khách Hàng (CRM)</h2>
                <button @click="showModal = true" class="px-4 py-2 bg-white/10 text-white font-bold rounded-lg text-sm hover:bg-white/20 transition-colors flex items-center gap-2">
                    <span class="material-symbols-outlined text-[18px]">person_add</span> Thêm Khách Hàng
                </button>
            </div>
            
            <!-- Modal Thêm Khách -->
            <div x-show="showModal" style="display:none;" class="fixed inset-0 bg-black/80 flex items-center justify-center z-50">
                <div class="bg-[#121214] border border-white/10 p-6 rounded-2xl w-96 relative" @click.outside="showModal = false">
                    <h3 class="text-lg font-bold mb-4">Thêm Khách Hàng Thủ Công</h3>
                    <div class="space-y-4">
                        <input x-model="newName" type="text" placeholder="Tên khách hàng" class="w-full bg-[#0A0A0A] border border-white/10 p-2 text-sm rounded focus:outline-none focus:border-[#00F0FF] text-white">
                        <input x-model="newPhone" type="text" placeholder="Số điện thoại" class="w-full bg-[#0A0A0A] border border-white/10 p-2 text-sm rounded focus:outline-none focus:border-[#00F0FF] text-white">
                        <div class="flex gap-2 justify-end mt-4">
                            <button @click="showModal = false" class="px-4 py-2 text-sm font-bold text-slate-400">Hủy</button>
                            <button @click="customers.push({name: newName, phone: newPhone, ltv: 0, vip: false}); showModal = false; newName=''; newPhone=''" class="px-4 py-2 bg-[#00F0FF] text-black font-bold rounded text-sm">Lưu</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
                <!-- Tags sidebar -->
                <div class="lg:col-span-1 space-y-4">
                    <div class="bg-[#121214] border border-white/5 rounded-2xl p-4">
                        <h3 class="font-bold text-sm mb-3">Phân Khúc (Tags)</h3>
                        <ul class="space-y-2 text-sm text-slate-300">
                            <li class="flex justify-between items-center p-2 bg-white/5 rounded-lg text-[#FFD700]">
                                <span>VIP</span> <span class="bg-[#0A0A0A] px-2 py-0.5 rounded text-xs" x-text="customers.filter(c=>c.vip).length"></span>
                            </li>
                            <li class="flex justify-between items-center p-2 hover:bg-white/5 rounded-lg">
                                <span>Tất Cả</span> <span class="bg-[#0A0A0A] px-2 py-0.5 rounded text-xs" x-text="customers.length"></span>
                            </li>
                        </ul>
                    </div>
                </div>
                <!-- Customer List -->
                <div class="lg:col-span-3 bg-[#121214] border border-white/5 rounded-2xl p-6">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                            <tr>
                                <th class="px-4 py-3">Tên Khách Hàng</th>
                                <th class="px-4 py-3">SĐT / Email</th>
                                <th class="px-4 py-3">LTV (Chi Tiêu)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <template x-for="(c, i) in customers" :key="i">
                                <tr class="border-b border-white/5 hover:bg-white/5">
                                    <td class="px-4 py-3 font-bold text-white flex items-center gap-2">
                                        <div class="w-8 h-8 rounded-full bg-slate-700"></div> <span x-text="c.name"></span>
                                    </td>
                                    <td class="px-4 py-3 text-slate-400" x-text="c.phone"></td>
                                    <td class="px-4 py-3 font-bold text-[#FFD700]">
                                        <span x-text="c.ltv.toLocaleString() + 'đ'"></span>
                                        <span x-show="c.vip" class="ml-2 px-1 bg-[#FFD700]/20 rounded text-[10px]">VIP</span>
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
    # Escape backticks and ${}
    escaped_content = content.replace("`", "\\`").replace("${", "\\${")
    final_html = TEMPLATE.replace('{CONTENT}', escaped_content).replace('{ID}', page_id)
    with open(html_file, 'w') as f:
        f.write(final_html)

print("Đã chèn logic AlpineJS và kích hoạt tính năng động cho toàn bộ các trang chính.")
