import os

PAGES = [
    ('dashboard.html', 'dashboard', '''
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            <div class="p-5 bg-[#121214] border border-white/5 rounded-2xl relative overflow-hidden">
                <div class="absolute top-0 right-0 p-3 opacity-10"><span class="material-symbols-outlined text-5xl text-[#00F0FF]">chat</span></div>
                <div class="text-xs text-slate-400 mb-1 uppercase tracking-wider">Tổng Hội Thoại</div>
                <div class="text-2xl font-display font-bold text-[#00F0FF]">12,450</div>
                <div class="text-[10px] text-primary mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">trending_up</span> +15% tuần này</div>
            </div>
            <div class="p-5 bg-[#121214] border border-white/5 rounded-2xl relative overflow-hidden">
                <div class="absolute top-0 right-0 p-3 opacity-10"><span class="material-symbols-outlined text-5xl text-[#FFD700]">shopping_bag</span></div>
                <div class="text-xs text-slate-400 mb-1 uppercase tracking-wider">Đơn Hàng Tự Động</div>
                <div class="text-2xl font-display font-bold text-[#FFD700]">842</div>
                <div class="text-[10px] text-primary mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">trending_up</span> +8% tuần này</div>
            </div>
            <div class="p-5 bg-[#121214] border border-white/5 rounded-2xl relative overflow-hidden">
                <div class="absolute top-0 right-0 p-3 opacity-10"><span class="material-symbols-outlined text-5xl text-[#10B981]">attach_money</span></div>
                <div class="text-xs text-slate-400 mb-1 uppercase tracking-wider">Doanh Thu (Tháng)</div>
                <div class="text-2xl font-display font-bold text-[#10B981]">420.5M</div>
                <div class="text-[10px] text-primary mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[12px]">trending_up</span> +12% tháng này</div>
            </div>
            <div class="p-5 bg-[#121214] border border-[#10B981]/20 rounded-2xl relative overflow-hidden shadow-[0_0_20px_rgba(16,185,129,0.1)]">
                <div class="absolute top-0 right-0 w-24 h-24 bg-[#10B981]/20 rounded-full blur-[30px] -mr-8 -mt-8 pointer-events-none"></div>
                <div class="text-xs text-slate-400 mb-1 uppercase tracking-wider">Claude AI Token Used</div>
                <div class="text-2xl font-display font-bold text-[#10B981]">1.2M</div>
                <div class="text-[10px] text-slate-400 mt-2">Chi phí ước tính: $12.50</div>
            </div>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[600px]">
            <!-- Inbox List -->
            <div class="bg-[#121214] border border-white/5 rounded-2xl flex flex-col overflow-hidden">
                <div class="p-4 border-b border-white/5 flex justify-between items-center bg-white/5">
                    <h3 class="font-bold text-sm">Inbox Đa Kênh</h3>
                    <button class="text-xs text-[#00F0FF] hover:underline">Lọc</button>
                </div>
                <div class="flex-1 overflow-y-auto custom-scrollbar p-2 space-y-2">
                    <div class="p-3 bg-white/5 rounded-xl cursor-pointer hover:bg-white/10 border-l-2 border-[#00F0FF]">
                        <div class="flex justify-between items-start mb-1">
                            <span class="font-bold text-sm text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-blue-500"></span> Nguyễn Văn A</span>
                            <span class="text-[10px] text-slate-500">Vừa xong</span>
                        </div>
                        <p class="text-xs text-slate-400 truncate">Sản phẩm này còn màu đen size M không shop?</p>
                    </div>
                    <div class="p-3 rounded-xl cursor-pointer hover:bg-white/5">
                        <div class="flex justify-between items-start mb-1">
                            <span class="font-bold text-sm text-slate-300 flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-green-500"></span> Trần Thị B</span>
                            <span class="text-[10px] text-slate-500">5p trước</span>
                        </div>
                        <p class="text-xs text-slate-400 truncate">Cảm ơn shop, mình đã nhận hàng.</p>
                    </div>
                </div>
            </div>

            <!-- Chat Area -->
            <div class="bg-[#121214] border border-white/5 rounded-2xl flex flex-col overflow-hidden lg:col-span-2 relative">
                <div class="absolute inset-0 bg-[#0A0A0A]/50 flex items-center justify-center z-10 backdrop-blur-sm hidden">
                    <button class="px-6 py-2 bg-gradient-to-r from-primary to-[#7B2DFF] rounded-xl font-bold text-sm">Nhận Hỗ Trợ Khách Này</button>
                </div>
                <div class="p-4 border-b border-white/5 flex justify-between items-center bg-white/5">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 bg-slate-700 rounded-full"></div>
                        <div>
                            <div class="font-bold text-sm">Nguyễn Văn A</div>
                            <div class="text-[10px] text-slate-400">Đến từ Facebook Messenger</div>
                        </div>
                    </div>
                    <div class="flex gap-2">
                        <button class="px-3 py-1.5 bg-[#FFD700]/10 text-[#FFD700] border border-[#FFD700]/30 rounded-lg text-xs font-bold hover:bg-[#FFD700]/20">Tạo Đơn Hàng</button>
                        <button class="px-3 py-1.5 bg-[#7B2DFF]/10 text-[#7B2DFF] border border-[#7B2DFF]/30 rounded-lg text-xs font-bold hover:bg-[#7B2DFF]/20">Gắn Tag</button>
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
                            <div class="text-[10px] text-[#0A0A0A]/60 mb-1 flex items-center justify-end gap-1"><span class="material-symbols-outlined text-[12px]">smart_toy</span> Claude AI tự động trả lời</div>
                            Dạ chào anh A, sản phẩm Quần Jeans mã 01 màu Đen size M bên em vẫn còn hàng ạ. Anh có muốn em lên đơn luôn cho anh không ạ?
                        </div>
                    </div>
                </div>
                <div class="p-4 border-t border-white/5 bg-white/5">
                    <div class="flex gap-2">
                        <button class="p-2 text-slate-400 hover:text-white"><span class="material-symbols-outlined text-[20px]">add_circle</span></button>
                        <input type="text" class="flex-1 bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-[#00F0FF]" placeholder="Nhập tin nhắn (Sẽ vô hiệu hóa AI nếu nhân viên nhắn)...">
                        <button class="p-2 text-[#00F0FF] hover:text-[#00F0FF]/80"><span class="material-symbols-outlined text-[20px]">send</span></button>
                    </div>
                </div>
            </div>
        </div>
    '''),

    ('bot_builder.html', 'bot_builder', '''
        <div class="mb-6 flex gap-4 border-b border-white/5">
            <button class="pb-2 text-[#00F0FF] border-b-2 border-[#00F0FF] font-bold text-sm px-4">System Prompt</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Flow Builder</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Knowledge Base (RAG)</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Quy Tắc Escalate</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Test Sandbox</button>
        </div>

        <div class="p-6 bg-[#121214] border border-[#7B2DFF]/20 rounded-2xl min-h-[500px] relative shadow-[0_0_40px_rgba(123,45,255,0.05)]">
            <div class="absolute top-0 right-0 w-64 h-64 bg-[#7B2DFF]/10 rounded-full blur-[80px] pointer-events-none"></div>
            
            <div class="flex justify-between items-start mb-6">
                <div>
                    <h2 class="text-xl font-bold flex items-center gap-2"><span class="material-symbols-outlined text-[#7B2DFF]">psychology</span> Cấu Hình Tính Cách Claude AI</h2>
                    <p class="text-sm text-slate-400 mt-1">Định hình cách bot tư vấn, chốt sale và giao tiếp với khách hàng.</p>
                </div>
                <button class="px-6 py-2 bg-gradient-to-r from-primary to-[#7B2DFF] rounded-xl font-bold text-sm flex items-center gap-2 hover:opacity-90 transition-opacity">
                    <span class="material-symbols-outlined text-[18px]">save</span> Lưu Cấu Hình Bot
                </button>
            </div>
            
            <div class="space-y-4 relative z-10">
                <div>
                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">Vai Trò (Role)</label>
                    <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-[#7B2DFF]" value="Bạn là một chuyên gia bán hàng thời trang cao cấp của thương hiệu XYZ.">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">Quy tắc ứng xử (Guidelines)</label>
                    <textarea class="w-full h-40 bg-[#0A0A0A] border border-white/10 rounded-xl p-4 text-sm text-white focus:border-[#7B2DFF] focus:outline-none custom-scrollbar">1. Luôn chào hỏi thân thiện và gọi khách hàng bằng Anh/Chị.
2. Trả lời ngắn gọn, tập trung vào lợi ích sản phẩm.
3. Khi khách hỏi giá, hãy nhắc đến giá trị sản phẩm trước.
4. Tự động đề xuất lên đơn nếu khách hàng đã chốt màu và size.
5. Tuyệt đối không tự bịa ra chính sách bảo hành ngoài tài liệu.</textarea>
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">Ngôn ngữ & Tone giọng</label>
                    <select class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-[#7B2DFF]">
                        <option>Chuyên nghiệp, Lịch sự</option>
                        <option selected>Trẻ trung, Năng động, Dùng Emoji</option>
                        <option>Sang trọng, Đẳng cấp</option>
                    </select>
                </div>
            </div>
        </div>
    '''),

    ('broadcast.html', 'broadcast', '''
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold">Chiến Dịch Nhắn Tin (Broadcast)</h2>
            <button class="px-4 py-2 bg-primary text-[#0A0A0A] font-bold rounded-lg text-sm hover:bg-[#0ea5e9] transition-colors flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">add</span> Tạo Chiến Dịch Mới
            </button>
        </div>
        <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
            <table class="w-full text-left text-sm text-slate-300">
                <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                    <tr>
                        <th class="px-4 py-3">Tên Chiến Dịch</th>
                        <th class="px-4 py-3">Kênh</th>
                        <th class="px-4 py-3">Đối Tượng (Tag)</th>
                        <th class="px-4 py-3">Thời Gian Gửi</th>
                        <th class="px-4 py-3">Trạng Thái</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="border-b border-white/5 hover:bg-white/5">
                        <td class="px-4 py-3 font-bold text-white">Khuyến Mãi Lễ 30/4</td>
                        <td class="px-4 py-3 flex gap-1"><span class="material-symbols-outlined text-[#00F0FF] text-[16px]">forum</span> FB Messenger</td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-white/10 rounded text-xs">Khách Cũ</span></td>
                        <td class="px-4 py-3 text-slate-400">28/04/2026 08:00</td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-green-500/20 text-green-400 rounded text-xs font-bold">Đã Gửi (1,240)</span></td>
                    </tr>
                    <tr class="hover:bg-white/5">
                        <td class="px-4 py-3 font-bold text-white">Ra Mắt BST Mùa Hè</td>
                        <td class="px-4 py-3 flex gap-1"><span class="material-symbols-outlined text-blue-400 text-[16px]">chat</span> Zalo OA</td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-white/10 rounded text-xs">VIP</span></td>
                        <td class="px-4 py-3 text-slate-400">15/05/2026 10:00</td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-[#FFD700]/20 text-[#FFD700] rounded text-xs font-bold">Lên Lịch</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    '''),

    ('channels.html', 'channels', '''
        <h2 class="text-xl font-bold mb-6">Kết Nối Kênh Bán Hàng</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Facebook -->
            <div class="p-6 bg-[#121214] border border-blue-500/30 rounded-2xl flex flex-col items-center text-center hover:border-blue-500 transition-colors">
                <div class="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center mb-4">
                    <span class="material-symbols-outlined text-white text-3xl">forum</span>
                </div>
                <h3 class="text-lg font-bold text-white mb-2">Facebook Messenger</h3>
                <p class="text-xs text-slate-400 mb-6">Kết nối Fanpage để Bot tự động trả lời tin nhắn và comment.</p>
                <div class="w-full flex justify-between items-center px-4 py-2 bg-blue-500/10 rounded-xl mb-4">
                    <span class="text-sm font-bold text-blue-400">Shop Quần Áo A</span>
                    <span class="w-3 h-3 bg-green-500 rounded-full shadow-[0_0_10px_#22c55e]"></span>
                </div>
                <button class="w-full py-2 bg-white/5 hover:bg-white/10 rounded-xl text-sm font-bold text-red-400">Ngắt Kết Nối</button>
            </div>
            
            <!-- Zalo -->
            <div class="p-6 bg-[#121214] border border-blue-400/30 rounded-2xl flex flex-col items-center text-center hover:border-blue-400 transition-colors">
                <div class="w-16 h-16 bg-blue-400 rounded-full flex items-center justify-center mb-4">
                    <span class="material-symbols-outlined text-white text-3xl">chat</span>
                </div>
                <h3 class="text-lg font-bold text-white mb-2">Zalo Official Account</h3>
                <p class="text-xs text-slate-400 mb-6">Tự động trả lời tin nhắn Zalo OA, tích hợp gửi ZNS.</p>
                <button class="w-full py-3 bg-blue-500 hover:bg-blue-600 rounded-xl text-sm font-bold text-white mb-2">Kết Nối Zalo OA</button>
                <span class="text-xs text-slate-500">Yêu cầu quyền Quản trị viên OA</span>
            </div>

            <!-- Website Widget -->
            <div class="p-6 bg-[#121214] border border-[#00F0FF]/30 rounded-2xl flex flex-col items-center text-center hover:border-[#00F0FF] transition-colors">
                <div class="w-16 h-16 bg-[#00F0FF]/20 rounded-full flex items-center justify-center mb-4 border border-[#00F0FF]/50">
                    <span class="material-symbols-outlined text-[#00F0FF] text-3xl">public</span>
                </div>
                <h3 class="text-lg font-bold text-white mb-2">Website Livechat Widget</h3>
                <p class="text-xs text-slate-400 mb-6">Mã nhúng Widget bong bóng chat cho Landing Page, Website.</p>
                <button class="w-full py-3 bg-white/5 border border-[#00F0FF]/50 hover:bg-[#00F0FF]/20 rounded-xl text-sm font-bold text-[#00F0FF] mb-2">Lấy Mã Nhúng</button>
                <button class="w-full py-2 text-xs font-bold text-slate-400 hover:text-white">Tùy Chỉnh Giao Diện</button>
            </div>
        </div>
    '''),

    ('ecommerce.html', 'ecommerce', '''
        <div class="mb-6 flex gap-4 border-b border-white/5">
            <button class="pb-2 text-[#00F0FF] border-b-2 border-[#00F0FF] font-bold text-sm px-4">Quản Lý Đơn Hàng</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Sản Phẩm & Kho</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Mã Giảm Giá</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Cấu Hình Thanh Toán / Ship</button>
        </div>
        <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
            <div class="flex justify-between items-center mb-6">
                <div class="flex gap-2">
                    <input type="text" class="bg-[#0A0A0A] border border-white/10 rounded-lg px-3 py-1.5 text-sm text-white focus:outline-none focus:border-[#00F0FF]" placeholder="Tìm mã đơn hàng, tên khách...">
                    <select class="bg-[#0A0A0A] border border-white/10 rounded-lg px-3 py-1.5 text-sm text-white focus:outline-none">
                        <option>Tất Cả Trạng Thái</option>
                        <option>Chờ Xác Nhận</option>
                        <option>Đang Giao</option>
                    </select>
                </div>
                <button class="px-4 py-2 bg-white/10 text-white font-bold rounded-lg text-sm hover:bg-white/20 transition-colors flex items-center gap-2">
                    <span class="material-symbols-outlined text-[18px]">download</span> Xuất Excel
                </button>
            </div>
            <table class="w-full text-left text-sm text-slate-300">
                <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                    <tr>
                        <th class="px-4 py-3">Mã Đơn</th>
                        <th class="px-4 py-3">Khách Hàng</th>
                        <th class="px-4 py-3">Sản Phẩm</th>
                        <th class="px-4 py-3">Tổng Tiền</th>
                        <th class="px-4 py-3">Thanh Toán</th>
                        <th class="px-4 py-3">Trạng Thái</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="border-b border-white/5 hover:bg-white/5">
                        <td class="px-4 py-3 font-bold text-[#00F0FF]">#ORD-9921</td>
                        <td class="px-4 py-3">Nguyễn Văn A<br><span class="text-xs text-slate-500">0901234567</span></td>
                        <td class="px-4 py-3">Áo thun basic (Đen, L) x1</td>
                        <td class="px-4 py-3 font-bold text-white">250,000đ</td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-blue-500/20 text-blue-400 rounded text-[10px] font-bold">Chuyển Khoản</span></td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-yellow-500/20 text-yellow-400 rounded text-xs font-bold">Chờ Gói Hàng</span></td>
                    </tr>
                    <tr class="hover:bg-white/5">
                        <td class="px-4 py-3 font-bold text-[#00F0FF]">#ORD-9920</td>
                        <td class="px-4 py-3">Trần Thị B<br><span class="text-xs text-slate-500">0987654321</span></td>
                        <td class="px-4 py-3">Quần Jeans mã 02 (Xanh, M) x2</td>
                        <td class="px-4 py-3 font-bold text-white">800,000đ</td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-slate-500/20 text-slate-400 rounded text-[10px] font-bold">COD</span></td>
                        <td class="px-4 py-3"><span class="px-2 py-1 bg-green-500/20 text-green-400 rounded text-xs font-bold">Đang Giao</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    '''),

    ('crm.html', 'crm', '''
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold">Quản Lý Khách Hàng (CRM)</h2>
            <button class="px-4 py-2 bg-white/10 text-white font-bold rounded-lg text-sm hover:bg-white/20 transition-colors flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">person_add</span> Thêm Khách Hàng
            </button>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
            <div class="lg:col-span-1 space-y-4">
                <div class="bg-[#121214] border border-white/5 rounded-2xl p-4">
                    <h3 class="font-bold text-sm mb-3">Phân Khúc (Tags)</h3>
                    <ul class="space-y-2 text-sm text-slate-300">
                        <li class="flex justify-between items-center p-2 bg-white/5 rounded-lg text-[#FFD700] cursor-pointer">
                            <span>VIP (Mua > 3 lần)</span> <span class="bg-[#0A0A0A] px-2 py-0.5 rounded text-xs">120</span>
                        </li>
                        <li class="flex justify-between items-center p-2 hover:bg-white/5 rounded-lg cursor-pointer">
                            <span>Khách Mới</span> <span class="bg-[#0A0A0A] px-2 py-0.5 rounded text-xs">5,432</span>
                        </li>
                        <li class="flex justify-between items-center p-2 hover:bg-white/5 rounded-lg text-red-400 cursor-pointer">
                            <span>Bỏ Giỏ Hàng</span> <span class="bg-[#0A0A0A] px-2 py-0.5 rounded text-xs">84</span>
                        </li>
                    </ul>
                </div>
                <div class="bg-gradient-to-br from-[#7B2DFF]/20 to-transparent border border-[#7B2DFF]/30 rounded-2xl p-4 cursor-pointer hover:border-[#7B2DFF] transition-colors">
                    <h3 class="font-bold text-sm text-[#7B2DFF] mb-1 flex items-center gap-1"><span class="material-symbols-outlined text-[16px]">robot_2</span> Auto Follow-up</h3>
                    <p class="text-xs text-slate-400">Cấu hình bot tự nhắn tin nhắc nhở khách hàng bỏ giỏ hàng sau 24h.</p>
                </div>
            </div>
            <div class="lg:col-span-3 bg-[#121214] border border-white/5 rounded-2xl p-6">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr>
                            <th class="px-4 py-3">Tên Khách Hàng</th>
                            <th class="px-4 py-3">SĐT / Email</th>
                            <th class="px-4 py-3">LTV (Chi Tiêu)</th>
                            <th class="px-4 py-3">Lần Chat Cuối</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5 hover:bg-white/5 cursor-pointer">
                            <td class="px-4 py-3 font-bold text-white flex items-center gap-2">
                                <div class="w-8 h-8 rounded-full bg-gradient-to-r from-pink-500 to-orange-400"></div> Lương Thu C
                            </td>
                            <td class="px-4 py-3 text-slate-400">0933111222</td>
                            <td class="px-4 py-3 font-bold text-[#FFD700]">5,400,000đ <span class="px-1 bg-[#FFD700]/20 rounded text-[10px]">VIP</span></td>
                            <td class="px-4 py-3 text-xs text-slate-500">Hôm nay 09:12</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    '''),

    ('team_management.html', 'team_management', '''
        <div class="flex justify-between items-center mb-6">
            <div>
                <h2 class="text-xl font-bold">Quản Lý Nhân Viên (Team)</h2>
                <p class="text-sm text-slate-400 mt-1">Phân quyền, mời nhân viên mới vào vận hành hệ thống.</p>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <!-- Add User Form -->
            <div class="bg-[#121214] border border-white/5 rounded-2xl p-6 h-fit">
                <h3 class="font-bold text-lg mb-4 flex items-center gap-2"><span class="material-symbols-outlined text-primary">person_add</span> Thêm Tài Khoản Mới</h3>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-400 mb-2">Địa Chỉ Email</label>
                        <input type="email" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-primary" placeholder="nhanvien@gmail.com">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-400 mb-2">Phân Quyền (Role)</label>
                        <select class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-primary">
                            <option value="manager">Manager (Quản lý vận hành)</option>
                            <option value="agent" selected>Agent (Nhân viên chốt đơn)</option>
                            <option value="viewer">Viewer (Chỉ xem báo cáo)</option>
                        </select>
                    </div>
                    <button class="w-full py-3 bg-primary text-[#0A0A0A] rounded-xl font-bold text-sm hover:bg-emerald-400 transition-colors mt-2">
                        Gửi Lời Mời Trực Tiếp
                    </button>
                    <p class="text-[10px] text-slate-500 text-center mt-2">Tài khoản này không cần đặt mật khẩu, sẽ sử dụng đăng nhập Google (1 chạm).</p>
                </div>
            </div>

            <!-- Team List -->
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
                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                            <td class="px-6 py-4 font-bold text-white flex items-center gap-3">
                                <div class="w-8 h-8 rounded-full bg-[#7B2DFF] flex items-center justify-center text-xs">Q</div>
                                quocthiencr7@gmail.com
                            </td>
                            <td class="px-6 py-4"><span class="px-2 py-1 bg-[#FFD700]/20 text-[#FFD700] rounded text-[10px] font-bold uppercase border border-[#FFD700]/30">Tenant Admin</span></td>
                            <td class="px-6 py-4"><span class="text-green-400 text-xs font-bold flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-green-500"></span> Online</span></td>
                            <td class="px-6 py-4 text-right"></td>
                        </tr>
                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                            <td class="px-6 py-4 font-bold text-slate-300 flex items-center gap-3">
                                <div class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center text-xs">S</div>
                                sale1@gmail.com
                            </td>
                            <td class="px-6 py-4"><span class="px-2 py-1 bg-white/10 text-slate-300 rounded text-[10px] uppercase">Agent</span></td>
                            <td class="px-6 py-4"><span class="text-slate-500 text-xs flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-slate-500"></span> Offline</span></td>
                            <td class="px-6 py-4 text-right">
                                <button class="text-red-400 hover:text-red-500 text-xs font-bold">Xóa</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    '''),

    ('admin_panel.html', 'admin_panel', '''
        <div class="mb-6 flex gap-4 border-b border-white/5">
            <button class="pb-2 text-[#FFD700] border-b-2 border-[#FFD700] font-bold text-sm px-4">Quản Lý Tenants</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Gói & Bảng Giá Platform</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Giám Sát Chi Phí AI</button>
            <button class="pb-2 text-slate-400 hover:text-white font-bold text-sm px-4">Cấu Hình White-label</button>
        </div>
        <div class="p-6 bg-[#121214] border border-[#FFD700]/20 rounded-2xl min-h-[500px] shadow-[0_0_30px_rgba(255,215,0,0.05)] relative overflow-hidden">
            <div class="absolute top-0 right-0 w-96 h-96 bg-[#FFD700]/5 rounded-full blur-[100px] pointer-events-none"></div>
            
            <div class="flex justify-between items-center mb-6 relative z-10">
                <div>
                    <h2 class="text-xl font-bold flex items-center gap-2"><span class="material-symbols-outlined text-[#FFD700]">corporate_fare</span> Tất Cả Doanh Nghiệp Đăng Ký</h2>
                    <p class="text-sm text-slate-400 mt-1">Danh sách các doanh nghiệp đang sử dụng nền tảng CHỐT NGHÌN ĐƠN.</p>
                </div>
                <button class="px-4 py-2 bg-[#FFD700] text-[#0A0A0A] font-bold rounded-lg hover:bg-yellow-400 transition-colors text-sm">+ Tạo Tenant Mới</button>
            </div>
            
            <div class="overflow-x-auto relative z-10">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr>
                            <th class="px-4 py-3">Tên Doanh Nghiệp</th>
                            <th class="px-4 py-3">Chủ Sở Hữu</th>
                            <th class="px-4 py-3">Gói (Plan)</th>
                            <th class="px-4 py-3">Chi Phí AI Tháng</th>
                            <th class="px-4 py-3">Trạng Thái</th>
                            <th class="px-4 py-3 text-right">Hành Động</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                            <td class="px-4 py-3 font-bold text-white">Shop Thời Trang A</td>
                            <td class="px-4 py-3">shopA@gmail.com</td>
                            <td class="px-4 py-3"><span class="px-2 py-1 bg-[#FFD700]/20 text-[#FFD700] rounded text-[10px] font-bold border border-[#FFD700]/30">PRO</span></td>
                            <td class="px-4 py-3 text-[#10B981]">$12.50</td>
                            <td class="px-4 py-3"><span class="px-2 py-1 bg-primary/20 text-primary rounded text-xs">Active</span></td>
                            <td class="px-4 py-3 text-right">
                                <button class="text-[#00F0FF] hover:underline text-xs font-bold mr-2">Cấu Hình</button>
                                <button class="text-red-400 hover:underline text-xs font-bold">Khóa</button>
                            </td>
                        </tr>
                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                            <td class="px-4 py-3 font-bold text-white">Trà Sữa C</td>
                            <td class="px-4 py-3">trasua@gmail.com</td>
                            <td class="px-4 py-3"><span class="px-2 py-1 bg-white/10 text-slate-300 rounded text-[10px] font-bold">FREE TRIAL</span></td>
                            <td class="px-4 py-3 text-[#10B981]">$0.10</td>
                            <td class="px-4 py-3"><span class="px-2 py-1 bg-red-500/20 text-red-400 rounded text-xs">Locked</span></td>
                            <td class="px-4 py-3 text-right">
                                <button class="text-[#00F0FF] hover:underline text-xs font-bold mr-2">Cấu Hình</button>
                                <button class="text-green-400 hover:underline text-xs font-bold">Mở Khóa</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    '''),
    
    ('tenant_settings.html', 'settings', '''
        <div class="max-w-4xl">
            <h2 class="text-xl font-bold mb-6">Thiết Lập Doanh Nghiệp (Tenant Settings)</h2>
            <div class="bg-[#121214] border border-white/5 rounded-2xl p-6 mb-6">
                <h3 class="font-bold text-sm mb-4 border-b border-white/5 pb-2 text-[#00F0FF]">Thông Tin Cơ Bản</h3>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-400 mb-2">Tên Doanh Nghiệp</label>
                        <input type="text" class="w-full max-w-md bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-[#00F0FF]" value="Cửa Hàng Thời Trang B">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-400 mb-2">Ngành Hàng</label>
                        <select class="w-full max-w-md bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none">
                            <option>Thời Trang</option>
                            <option>Mỹ Phẩm</option>
                            <option>F&B</option>
                        </select>
                    </div>
                </div>
            </div>
            
            <div class="bg-[#121214] border border-white/5 rounded-2xl p-6 mb-6">
                <h3 class="font-bold text-sm mb-4 border-b border-white/5 pb-2 text-[#10B981]">Giới Hạn Claude AI & Billing</h3>
                <div class="flex justify-between items-center bg-[#0A0A0A] border border-white/5 rounded-xl p-4">
                    <div>
                        <div class="font-bold text-white text-sm mb-1">Gói Hiện Tại: <span class="text-[#FFD700]">PRO PLAN</span></div>
                        <div class="text-xs text-slate-400">Giới hạn 100,000 tin nhắn AI / tháng. Đã dùng: 12,450.</div>
                    </div>
                    <button class="px-4 py-2 bg-white/10 text-white font-bold rounded-lg text-sm hover:bg-white/20 transition-colors">Đổi Gói</button>
                </div>
                <div class="mt-4">
                    <label class="block text-xs font-bold text-slate-400 mb-2">Ngưỡng cảnh báo chi phí AI ($/ngày)</label>
                    <input type="number" class="w-full max-w-xs bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-[#10B981]" value="5.0">
                </div>
            </div>
            
            <div class="bg-[#121214] border border-white/5 rounded-2xl p-6">
                <h3 class="font-bold text-sm mb-4 border-b border-white/5 pb-2 text-[#7B2DFF]">API Keys (Tích Hợp Bên Thứ 3)</h3>
                <p class="text-xs text-slate-400 mb-4">Sử dụng API Key này để kết nối CHỐT NGHÌN ĐƠN với ERP, hệ thống kế toán hoặc CRM bên ngoài.</p>
                <div class="flex gap-2 max-w-xl">
                    <input type="text" class="flex-1 bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-slate-500 font-mono" value="sk_tenant_9a8b7c6d5e4f3g2h1" readonly>
                    <button class="px-4 py-2 bg-white/10 text-white font-bold rounded-xl text-sm hover:bg-white/20 transition-colors">Copy</button>
                    <button class="px-4 py-2 border border-red-500/50 text-red-400 font-bold rounded-xl text-sm hover:bg-red-500/10 transition-colors">Revoke</button>
                </div>
            </div>
        </div>
    ''')
]

# Generate simple placeholders for the rest
OTHER_PAGES = ['content', 'affiliate', 'analytics', 'support']
for p in OTHER_PAGES:
    html_name = p + '.html'
    if not any(page[0] == html_name for page in PAGES):
        PAGES.append((html_name, p, f'''
            <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[400px] flex flex-col items-center justify-center text-center">
                <span class="material-symbols-outlined text-6xl text-slate-600 mb-4">construction</span>
                <h2 class="text-2xl font-bold text-white mb-2">Giao Diện {p.replace('_', ' ').title()} Đang Hoàn Thiện</h2>
                <p class="text-slate-400">Tính năng này đang trong quá trình lắp ráp giao diện theo chuẩn Vibe Coding.</p>
            </div>
        '''))

TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>CHỐT NGHÌN ĐƠN</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        "primary": "#10B981",
                        "secondary": "#7B2DFF",
                        "tertiary": "#FFD700",
                        "accent": "#00F0FF",
                        "background": "#0A0A0A",
                        "surface": "#121214"
                    },
                    fontFamily: {
                        "display": ["Plus Jakarta Sans", "sans-serif"],
                        "body": ["Inter", "sans-serif"],
                    }
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
    # Escape backticks and ${} to prevent template literal errors in the output JS
    escaped_content = content.replace("`", "\\`").replace("${", "\\${")
    final_html = TEMPLATE.replace('{CONTENT}', escaped_content).replace('{ID}', page_id)
    with open(html_file, 'w') as f:
        f.write(final_html)

print("Đã tạo mockup giao diện cực khủng cho toàn bộ các module.")
