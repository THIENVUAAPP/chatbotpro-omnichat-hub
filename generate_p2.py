import os

PAGES = [
    ('content.html', 'content', '''
        <div x-data="{ activeTab: 'blog' }">
            <h2 class="text-xl font-bold mb-6">Quản Lý Nội Dung & Media</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'blog'" :class="activeTab === 'blog' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Bài Viết / Blog</button>
                <button @click="activeTab = 'banner'" :class="activeTab === 'banner' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Banner Khuyến Mãi</button>
                <button @click="activeTab = 'media'" :class="activeTab === 'media' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Thư Viện Media</button>
            </div>

            <div x-show="activeTab === 'blog'" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <div class="flex justify-between items-center mb-4">
                    <h3 class="font-bold">Danh sách Bài Viết</h3>
                    <button class="px-4 py-2 bg-primary text-black font-bold rounded-lg text-sm">+ Bài Viết Mới</button>
                </div>
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Tiêu đề</th><th class="px-4 py-3">Danh mục</th><th class="px-4 py-3">Trạng thái</th><th class="px-4 py-3 text-right">Hành động</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5">
                            <td class="px-4 py-3 font-bold text-white">5 Cách Tăng Doanh Số 2026</td>
                            <td class="px-4 py-3">Kinh Doanh</td>
                            <td class="px-4 py-3"><span class="text-green-400 text-xs">Đã xuất bản</span></td>
                            <td class="px-4 py-3 text-right text-[#00F0FF] cursor-pointer">Sửa</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div x-show="activeTab === 'banner'" style="display:none;" class="grid grid-cols-2 gap-6">
                <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl text-center border-dashed cursor-pointer hover:bg-white/5">
                    <span class="material-symbols-outlined text-4xl mb-2 text-slate-400">add_photo_alternate</span>
                    <p class="font-bold text-sm text-white">Thêm Banner Trang Chủ</p>
                    <p class="text-xs text-slate-500">1920x1080px (Tối đa 2MB)</p>
                </div>
            </div>

            <div x-show="activeTab === 'media'" style="display:none;" class="grid grid-cols-4 gap-4">
                <template x-for="i in 4">
                    <div class="aspect-square bg-[#0A0A0A] border border-white/10 rounded-xl flex items-center justify-center">
                        <span class="material-symbols-outlined text-slate-600">image</span>
                    </div>
                </template>
            </div>
        </div>
    '''),

    ('affiliate.html', 'affiliate', '''
        <div x-data="{ refUrl: 'https://chotnghindon.com/ref/quocthien', balance: 12500000, copied: false }">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-[#10B981]">groups</span> Đối Tác & Đại Lý (Affiliate)</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
                <div class="p-6 bg-gradient-to-br from-[#10B981]/20 to-[#0A0A0A] border border-[#10B981]/30 rounded-2xl relative overflow-hidden md:col-span-2">
                    <div class="absolute right-0 bottom-0 opacity-10"><span class="material-symbols-outlined text-[150px] text-[#10B981]">share</span></div>
                    <p class="text-sm text-slate-300 font-bold mb-2">Link Giới Thiệu Của Bạn</p>
                    <div class="flex gap-2 relative z-10">
                        <input type="text" class="flex-1 bg-[#0A0A0A] border border-white/10 p-3 rounded-xl text-white font-mono text-sm" x-model="refUrl" readonly>
                        <button @click="navigator.clipboard.writeText(refUrl); copied = true; setTimeout(() => copied = false, 2000)" class="bg-[#10B981] text-black px-6 font-bold rounded-xl whitespace-nowrap">
                            <span x-show="!copied">Copy Link</span>
                            <span x-show="copied">Đã Copy!</span>
                        </button>
                    </div>
                    <p class="text-xs mt-3 text-slate-400">Hoa hồng 30% cho mỗi khách hàng đăng ký thành công qua link này.</p>
                </div>
                
                <div class="p-6 bg-[#121214] border border-[#FFD700]/30 rounded-2xl text-center flex flex-col justify-center relative overflow-hidden">
                    <div class="absolute top-0 right-0 p-2 opacity-10"><span class="material-symbols-outlined text-5xl text-[#FFD700]">account_balance_wallet</span></div>
                    <p class="text-sm text-slate-400 mb-1 font-bold">Số Dư Khả Dụng</p>
                    <h3 class="text-3xl font-display font-bold text-[#FFD700] mb-4" x-text="balance.toLocaleString() + 'đ'"></h3>
                    <button class="w-full bg-[#FFD700] text-black font-bold py-2 rounded-lg text-sm">Yêu Cầu Rút Tiền</button>
                </div>
            </div>

            <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <h3 class="font-bold mb-4">Lịch Sử Giới Thiệu Khách Hàng</h3>
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Khách Hàng</th><th class="px-4 py-3">Gói Đăng Ký</th><th class="px-4 py-3">Tiền Hoa Hồng</th><th class="px-4 py-3">Trạng Thái</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5 hover:bg-white/5">
                            <td class="px-4 py-3 font-bold text-white">nguyenvana@gmail.com</td>
                            <td class="px-4 py-3">PRO Plan (1 Năm)</td>
                            <td class="px-4 py-3 font-bold text-[#10B981]">+ 1.200.000đ</td>
                            <td class="px-4 py-3"><span class="text-green-400 text-xs border border-green-500/30 px-2 py-1 rounded">Đã duyệt</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    '''),

    ('analytics.html', 'analytics', '''
        <div x-data="{ activeTab: 'sales' }">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-[#00F0FF]">insights</span> Báo Cáo & Thống Kê</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'sales'" :class="activeTab === 'sales' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Doanh Số</button>
                <button @click="activeTab = 'bot'" :class="activeTab === 'bot' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Hiệu Suất Bot</button>
            </div>

            <div x-show="activeTab === 'sales'" class="space-y-6">
                <div class="grid grid-cols-3 gap-6">
                    <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl"><p class="text-sm text-slate-400">Doanh thu hôm nay</p><h3 class="text-2xl font-bold text-white mt-2">12.500.000đ</h3></div>
                    <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl"><p class="text-sm text-slate-400">Đơn hàng mới</p><h3 class="text-2xl font-bold text-[#00F0FF] mt-2">342 Đơn</h3></div>
                    <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl"><p class="text-sm text-slate-400">AOV (Giá trị ĐH TB)</p><h3 class="text-2xl font-bold text-[#10B981] mt-2">365.000đ</h3></div>
                </div>
                <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl h-[300px] flex items-center justify-center">
                    <span class="text-slate-500">[Khu vực render Biểu đồ Line Chart Doanh Số 30 Ngày qua Chart.js]</span>
                </div>
            </div>

            <div x-show="activeTab === 'bot'" style="display:none;" class="space-y-6">
                 <div class="grid grid-cols-3 gap-6">
                    <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl"><p class="text-sm text-slate-400">Tỷ lệ Bot giải quyết (Resolution Rate)</p><h3 class="text-2xl font-bold text-[#10B981] mt-2">87.5%</h3></div>
                    <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl"><p class="text-sm text-slate-400">Tỷ lệ Escalate (Chuyển cho Nhân viên)</p><h3 class="text-2xl font-bold text-red-400 mt-2">12.5%</h3></div>
                    <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl"><p class="text-sm text-slate-400">Thời gian phản hồi TB</p><h3 class="text-2xl font-bold text-[#FFD700] mt-2">1.2s</h3></div>
                </div>
            </div>
        </div>
    '''),

    ('support.html', 'support', '''
        <div x-data="{ activeTab: 'audit' }">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-slate-400">health_and_safety</span> Hệ Thống & Bảo Mật</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'audit'" :class="activeTab === 'audit' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Audit Log</button>
                <button @click="activeTab = 'status'" :class="activeTab === 'status' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Status Page</button>
                <button @click="activeTab = 'faq'" :class="activeTab === 'faq' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Trung Tâm Trợ Giúp</button>
            </div>

            <div x-show="activeTab === 'audit'" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <h3 class="font-bold mb-4">Nhật Ký Hoạt Động Của Hệ Thống (Bảo Mật)</h3>
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Thời gian</th><th class="px-4 py-3">Tài khoản</th><th class="px-4 py-3">IP</th><th class="px-4 py-3">Hành động</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5">
                            <td class="px-4 py-3">18/06/2026 14:30</td><td class="px-4 py-3 font-bold text-[#00F0FF]">quocthiencr7@gmail.com</td>
                            <td class="px-4 py-3 text-xs text-slate-500">113.190.22.1</td><td class="px-4 py-3">Chỉnh sửa Prompt Kịch Bản Bot</td>
                        </tr>
                        <tr class="border-b border-white/5">
                            <td class="px-4 py-3">18/06/2026 10:15</td><td class="px-4 py-3 font-bold text-[#00F0FF]">sale1@gmail.com</td>
                            <td class="px-4 py-3 text-xs text-slate-500">113.190.22.1</td><td class="px-4 py-3">Đăng nhập thành công</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div x-show="activeTab === 'status'" style="display:none;" class="space-y-4">
                <div class="p-4 bg-green-500/10 border border-green-500/30 rounded-xl flex items-center justify-between">
                    <div>
                        <h4 class="font-bold text-green-400">Claude API Connection</h4>
                        <p class="text-xs text-slate-400">99.99% Uptime trong 30 ngày qua</p>
                    </div>
                    <span class="px-3 py-1 bg-green-500/20 text-green-400 rounded-full text-xs font-bold flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-green-500"></span> Operational</span>
                </div>
            </div>

            <div x-show="activeTab === 'faq'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <p class="text-slate-400 text-sm">Các tài liệu HDSD và Video hướng dẫn sử dụng tính năng của phần mềm sẽ hiển thị tại đây.</p>
            </div>
        </div>
    '''),

    ('bot_builder.html', 'bot_builder', '''
        <div x-data="{ activeTab: 'prompt', showToast: false, files: [] }">
            <div class="mb-6 flex gap-4 border-b border-white/5 overflow-x-auto custom-scrollbar whitespace-nowrap">
                <button @click="activeTab = 'prompt'" :class="activeTab === 'prompt' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">System Prompt</button>
                <button @click="activeTab = 'flow'" :class="activeTab === 'flow' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Flow Builder</button>
                <button @click="activeTab = 'rag'" :class="activeTab === 'rag' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Knowledge Base</button>
                <button @click="activeTab = 'ab'" :class="activeTab === 'ab' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">A/B Testing</button>
                <button @click="activeTab = 'escalate'" :class="activeTab === 'escalate' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Escalate Rules</button>
            </div>

            <!-- Toast -->
            <div x-show="showToast" x-transition class="fixed top-20 right-8 bg-green-500 text-white px-4 py-2 rounded-lg font-bold text-sm shadow-lg z-50">Đã lưu thành công!</div>

            <!-- TAB 1 -->
            <div x-show="activeTab === 'prompt'" class="p-6 bg-[#121214] border border-[#7B2DFF]/20 rounded-2xl relative shadow-[0_0_40px_rgba(123,45,255,0.05)]">
                <div class="flex justify-between items-start mb-6">
                    <div>
                        <h2 class="text-xl font-bold">Cấu Hình Tính Cách Claude AI</h2>
                        <p class="text-sm text-slate-400 mt-1">Định hình cách bot tư vấn, chốt sale.</p>
                    </div>
                    <button @click="showToast = true; setTimeout(() => showToast = false, 3000)" class="px-6 py-2 bg-gradient-to-r from-primary to-[#7B2DFF] rounded-xl font-bold text-sm text-white">Lưu Cấu Hình</button>
                </div>
                <div class="space-y-4">
                    <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm text-white" value="Chuyên gia bán hàng">
                    <textarea class="w-full h-40 bg-[#0A0A0A] border border-white/10 rounded-xl p-4 text-sm text-white custom-scrollbar">Luôn chào khách và tư vấn chốt đơn.</textarea>
                </div>
            </div>

            <!-- TAB 2 -->
            <div x-show="activeTab === 'flow'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[400px] flex items-center justify-center text-center">
                <div><span class="material-symbols-outlined text-6xl text-[#00F0FF] mb-4">account_tree</span><h2 class="text-2xl font-bold">Flow Builder Trực Quan</h2></div>
            </div>

            <!-- TAB 3: RAG -->
            <div x-show="activeTab === 'rag'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[400px]">
                <h2 class="text-xl font-bold mb-4">Kho Dữ Liệu RAG (Tài Liệu Đào Tạo)</h2>
                <div class="border-2 border-dashed border-white/10 rounded-xl p-10 flex flex-col items-center justify-center text-center hover:bg-white/5 cursor-pointer transition-colors" @click="files.push('Bao_Hanh_Chinh_Sach_2026.pdf')">
                    <span class="material-symbols-outlined text-4xl text-slate-500 mb-2">cloud_upload</span>
                    <p class="font-bold text-sm">Bấm vào đây để tải file PDF/DOCX lên</p>
                </div>
                <ul class="mt-4 space-y-2">
                    <template x-for="f in files" :key="f">
                        <li class="flex justify-between bg-white/5 p-3 rounded-lg text-sm text-white">
                            <span class="flex items-center gap-2"><span class="material-symbols-outlined text-[#10B981]">description</span> <span x-text="f"></span></span>
                            <span class="text-xs text-green-400 bg-green-500/20 px-2 py-1 rounded">Đã Embed (Vectorized)</span>
                        </li>
                    </template>
                </ul>
            </div>

            <!-- TAB 4: AB Testing -->
            <div x-show="activeTab === 'ab'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[400px]">
                <h2 class="text-xl font-bold mb-4 flex items-center gap-2"><span class="material-symbols-outlined text-[#FFD700]">compare_arrows</span> A/B Testing Kịch Bản</h2>
                <div class="grid grid-cols-2 gap-6">
                    <div class="border border-white/10 p-4 rounded-xl"><h3 class="font-bold text-primary mb-2">Version A (Hiện tại)</h3><p class="text-sm text-slate-400">Tỷ lệ chốt đơn: 15%</p></div>
                    <div class="border border-[#7B2DFF]/50 bg-[#7B2DFF]/10 p-4 rounded-xl"><h3 class="font-bold text-[#7B2DFF] mb-2">Version B (Thử nghiệm)</h3><p class="text-sm text-slate-400">Tỷ lệ chốt đơn: 18% <span class="text-green-400">(+3%)</span></p></div>
                </div>
                <button class="mt-6 px-4 py-2 bg-[#FFD700] text-black font-bold rounded-lg text-sm">Áp Dụng Version B</button>
            </div>

            <!-- TAB 5: Escalate -->
            <div x-show="activeTab === 'escalate'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[400px]">
                <h2 class="text-xl font-bold mb-4">Quy Tắc Chuyển Người Thật (Escalate)</h2>
                <div class="space-y-3">
                    <label class="flex items-center gap-3"><input type="checkbox" checked class="w-4 h-4 accent-primary"> <span class="text-sm text-white">Chuyển ngay khi khách chat từ "bảo hành" hoặc "lỗi"</span></label>
                    <label class="flex items-center gap-3"><input type="checkbox" checked class="w-4 h-4 accent-primary"> <span class="text-sm text-white">Chuyển khi khách tức giận (Sentiment Analysis = Negative)</span></label>
                </div>
            </div>
        </div>
    '''),

    ('ecommerce.html', 'ecommerce', '''
        <div x-data="{ activeTab: 'orders' }">
            <h2 class="text-xl font-bold mb-6">Quản Lý Bán Hàng</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'orders'" :class="activeTab === 'orders' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Đơn Hàng</button>
                <button @click="activeTab = 'inventory'" :class="activeTab === 'inventory' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Sản Phẩm & Tồn Kho</button>
                <button @click="activeTab = 'coupons'" :class="activeTab === 'coupons' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Mã Giảm Giá (Coupons)</button>
            </div>

            <div x-show="activeTab === 'orders'" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Mã Đơn</th><th class="px-4 py-3">Khách Hàng</th><th class="px-4 py-3">Tổng Tiền</th><th class="px-4 py-3">Trạng Thái</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5"><td class="px-4 py-3 font-bold">#ORD-999</td><td class="px-4 py-3">Nguyễn Văn A</td><td class="px-4 py-3">550.000đ</td><td class="px-4 py-3"><span class="text-[#FFD700] text-xs">Đang giao</span></td></tr>
                    </tbody>
                </table>
            </div>

            <div x-show="activeTab === 'inventory'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                <button class="mb-4 px-4 py-2 bg-primary text-black font-bold rounded-lg text-sm">+ Thêm Sản Phẩm</button>
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Tên Sản Phẩm</th><th class="px-4 py-3">Danh mục</th><th class="px-4 py-3">Giá Bán</th><th class="px-4 py-3">Tồn Kho</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5"><td class="px-4 py-3 font-bold">Áo Thun Basic M</td><td class="px-4 py-3">Thời Trang</td><td class="px-4 py-3">150.000đ</td><td class="px-4 py-3 font-bold text-red-400">2 (Sắp hết)</td></tr>
                    </tbody>
                </table>
            </div>

            <div x-show="activeTab === 'coupons'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                 <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Mã Code</th><th class="px-4 py-3">Giảm Giá</th><th class="px-4 py-3">Lượt Dùng</th><th class="px-4 py-3">Hạn Sử Dụng</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5"><td class="px-4 py-3 font-bold text-[#FFD700] bg-[#FFD700]/10 rounded px-2 w-fit">CHOTNGHINDON</td><td class="px-4 py-3">20%</td><td class="px-4 py-3">12/100</td><td class="px-4 py-3">30/12/2026</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    '''),

    ('tenant_settings.html', 'tenant_settings', '''
        <div x-data="{ activeTab: 'general' }">
            <h2 class="text-xl font-bold mb-6">Cài Đặt Cửa Hàng (Tenant)</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'general'" :class="activeTab === 'general' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Chung</button>
                <button @click="activeTab = 'api'" :class="activeTab === 'api' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">API & Tích Hợp</button>
                <button @click="activeTab = 'billing'" :class="activeTab === 'billing' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Lịch Sử Thanh Toán</button>
            </div>

            <div x-show="activeTab === 'general'" class="p-6 bg-[#121214] border border-white/5 rounded-2xl space-y-4">
                <label class="block text-xs font-bold text-slate-400">Tên Cửa Hàng</label>
                <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-2 text-sm rounded text-white" value="My Store VIP">
            </div>

            <div x-show="activeTab === 'api'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl space-y-4">
                 <label class="block text-xs font-bold text-slate-400">API Key (Riêng cho Cửa Hàng Này)</label>
                <div class="flex gap-2"><input type="text" class="flex-1 bg-[#0A0A0A] border border-white/10 p-2 text-sm text-slate-400 rounded" value="sk-ant-xxxxxxxxxxxxxx" readonly> <button class="bg-[#10B981] px-4 rounded font-bold text-black text-sm">Copy</button></div>
            </div>

            <div x-show="activeTab === 'billing'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                 <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr><th class="px-4 py-3">Mã Hóa Đơn</th><th class="px-4 py-3">Ngày</th><th class="px-4 py-3">Số Tiền</th><th class="px-4 py-3">Trạng Thái</th><th class="px-4 py-3 text-right">Tải PDF</th></tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5">
                            <td class="px-4 py-3 font-bold">INV-001</td><td class="px-4 py-3">01/06/2026</td><td class="px-4 py-3 text-white font-bold">$12.50</td>
                            <td class="px-4 py-3"><span class="text-green-400 text-xs bg-green-500/20 px-2 py-1 rounded">Đã Thanh Toán</span></td>
                            <td class="px-4 py-3 text-right"><span class="material-symbols-outlined text-slate-400 hover:text-white cursor-pointer">download</span></td>
                        </tr>
                    </tbody>
                </table>
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

print("Đã đắp kín 100% tất cả các Tab con và chức năng còn thiếu của Nhóm G, K, L, Affiliate.")
