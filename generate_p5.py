import os

PAGES = [
    ('channels.html', 'channels', '''
        <div x-data="{ 
            fbConnected: true, 
            zaloConnected: false, 
            tiktokConnected: false,
            shopeeConnected: true,
            activeModal: null, // 'facebook', 'zalo', 'tiktok', 'shopee'
            apiToken: '',
            apiSecret: '',
            openModal(type) {
                this.activeModal = type;
                this.apiToken = '';
                this.apiSecret = '';
            },
            saveConnection() {
                if (this.activeModal === 'facebook') this.fbConnected = true;
                if (this.activeModal === 'zalo') this.zaloConnected = true;
                if (this.activeModal === 'tiktok') this.tiktokConnected = true;
                if (this.activeModal === 'shopee') this.shopeeConnected = true;
                this.activeModal = null;
            }
        }">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-[#00F0FF]">hub</span> Trung Tâm Kết Nối Đa Kênh Lõi (API/Token)</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Facebook -->
                <div class="p-6 bg-[#121214] border border-blue-500/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-blue-500 rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined text-white text-3xl">forum</span></div>
                    <h3 class="text-lg font-bold text-white mb-2">Facebook</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Messenger & Bình luận Fanpage</p>
                    <template x-if="fbConnected"><button @click="fbConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!fbConnected"><button @click="openModal('facebook')" class="w-full py-2 bg-blue-500 text-white font-bold rounded-xl text-sm">Cấu Hình API</button></template>
                </div>
                
                <!-- Zalo -->
                <div class="p-6 bg-[#121214] border border-blue-400/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-blue-400 rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined text-white text-3xl">chat</span></div>
                    <h3 class="text-lg font-bold text-white mb-2">Zalo OA</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Zalo Official Account & ZNS</p>
                    <template x-if="zaloConnected"><button @click="zaloConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!zaloConnected"><button @click="openModal('zalo')" class="w-full py-2 bg-blue-400 text-white font-bold rounded-xl text-sm">Cấu Hình API</button></template>
                </div>

                <!-- Tiktok Shop -->
                <div class="p-6 bg-[#121214] border border-white/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-white text-black rounded-full flex items-center justify-center mb-4 font-bold text-xl">TT</div>
                    <h3 class="text-lg font-bold text-white mb-2">TikTok Shop</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Quản lý tin nhắn & Đơn hàng Tiktok</p>
                    <template x-if="tiktokConnected"><button @click="tiktokConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!tiktokConnected"><button @click="openModal('tiktok')" class="w-full py-2 bg-white text-black font-bold rounded-xl text-sm">Cấu Hình API</button></template>
                </div>

                <!-- Shopee -->
                <div class="p-6 bg-[#121214] border border-[#EE4D2D]/30 rounded-2xl flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-[#EE4D2D] text-white rounded-full flex items-center justify-center mb-4 font-bold text-xl">S</div>
                    <h3 class="text-lg font-bold text-white mb-2">Shopee</h3>
                    <p class="text-xs text-slate-400 mb-6 flex-1">Đồng bộ tin nhắn Shopee Chat</p>
                    <template x-if="shopeeConnected"><button @click="shopeeConnected = false" class="w-full py-2 text-sm font-bold text-green-400 border border-green-500/30 bg-green-500/10 rounded-xl">Đang Kết Nối</button></template>
                    <template x-if="!shopeeConnected"><button @click="openModal('shopee')" class="w-full py-2 bg-[#EE4D2D] text-white font-bold rounded-xl text-sm">Cấu Hình API</button></template>
                </div>
            </div>

            <!-- MODAL KẾT NỐI API -->
            <div x-show="activeModal !== null" style="display:none;" class="fixed inset-0 bg-black/90 flex items-center justify-center z-50 backdrop-blur-sm">
                <div class="bg-[#121214] border border-[#10B981]/30 p-8 rounded-3xl w-[500px] shadow-[0_0_50px_rgba(16,185,129,0.1)] relative" @click.outside="activeModal = null">
                    <h3 class="text-2xl font-bold mb-2 text-[#10B981]">Xác Thực API / Token</h3>
                    <p class="text-sm text-slate-400 mb-6">Nhập thông tin xác thực từ nền tảng để cấp quyền cho Bot hoạt động.</p>
                    
                    <div class="space-y-4">
                        <template x-if="activeModal === 'facebook'">
                            <div>
                                <label class="block text-xs font-bold text-slate-400 mb-2">Page Access Token</label>
                                <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none focus:border-[#10B981] text-white font-mono" placeholder="EAABw...">
                                <label class="block text-xs font-bold text-slate-400 mb-2 mt-4">Webhook Verify Token</label>
                                <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none focus:border-[#10B981] text-white font-mono" placeholder="my_verify_token">
                            </div>
                        </template>

                        <template x-if="activeModal === 'tiktok' || activeModal === 'shopee'">
                            <div>
                                <label class="block text-xs font-bold text-slate-400 mb-2">Shop ID</label>
                                <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none focus:border-[#10B981] text-white font-mono" placeholder="123456789">
                                <label class="block text-xs font-bold text-slate-400 mb-2 mt-4">App Secret / API Key</label>
                                <input type="password" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none focus:border-[#10B981] text-white font-mono" placeholder="••••••••••••••••">
                            </div>
                        </template>

                        <template x-if="activeModal === 'zalo'">
                            <div>
                                <label class="block text-xs font-bold text-slate-400 mb-2">Zalo OA Access Token</label>
                                <textarea class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl focus:outline-none focus:border-[#10B981] text-white font-mono h-24" placeholder="Nhập chuỗi token siêu dài..."></textarea>
                            </div>
                        </template>

                        <div class="flex gap-4 justify-end mt-8">
                            <button @click="activeModal = null" class="px-6 py-3 text-sm font-bold text-slate-400 hover:text-white">Hủy</button>
                            <button @click="saveConnection()" class="px-8 py-3 bg-[#10B981] text-black font-bold rounded-xl text-sm hover:bg-emerald-400">Kết Nối Hệ Thống</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    '''),

    ('tenant_settings.html', 'tenant_settings', '''
        <div x-data="{ activeTab: 'strategy' }">
            <h2 class="text-xl font-bold mb-6">Cài Đặt Cửa Hàng (Quản Trị Doanh Nghiệp)</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'general'" :class="activeTab === 'general' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Quản Trị Vận Hành</button>
                <button @click="activeTab = 'strategy'" :class="activeTab === 'strategy' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Chiến Lược Bán Hàng</button>
            </div>

            <!-- TAB QUẢN TRỊ VẬN HÀNH -->
            <div x-show="activeTab === 'general'" class="p-6 bg-[#121214] border border-white/5 rounded-2xl grid grid-cols-2 gap-8">
                <div class="space-y-4">
                    <label class="block text-xs font-bold text-slate-400">Tên Pháp Lý / Tên Cửa Hàng</label>
                    <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white" value="Công ty TNHH Bán Lẻ ABC">
                    
                    <label class="block text-xs font-bold text-slate-400 pt-4">Địa Chỉ Trụ Sở</label>
                    <input type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white" value="Tầng 5, Tòa nhà X, Hà Nội">
                </div>
                <div class="space-y-4 border-l border-white/5 pl-8">
                    <h3 class="font-bold text-sm text-primary mb-4">Khung Giờ Hoạt Động Của Nhân Viên</h3>
                    <div class="flex items-center gap-4">
                        <label class="text-xs text-slate-400 w-16">Giờ mở</label>
                        <input type="time" class="bg-[#0A0A0A] border border-white/10 p-2 text-sm rounded-lg text-white" value="08:00">
                    </div>
                    <div class="flex items-center gap-4">
                        <label class="text-xs text-slate-400 w-16">Giờ đóng</label>
                        <input type="time" class="bg-[#0A0A0A] border border-white/10 p-2 text-sm rounded-lg text-white" value="22:00">
                    </div>
                    <label class="block text-xs font-bold text-slate-400 pt-4">Tin nhắn tự động ngoài giờ làm việc</label>
                    <textarea class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white h-20">Hiện tại đã hết giờ làm việc. Bot AI của chúng tôi sẽ tạm thời ghi nhận yêu cầu của quý khách...</textarea>
                </div>
            </div>

            <!-- TAB CHIẾN LƯỢC BÁN HÀNG -->
            <div x-show="activeTab === 'strategy'" style="display:none;" class="p-6 bg-[#121214] border border-white/5 rounded-2xl">
                 <h3 class="font-bold text-lg text-[#FFD700] mb-4">Cấu Hình Chiến Lược Gói & Upsell (Cho Khách Hàng Của Bạn)</h3>
                 <div class="grid grid-cols-2 gap-6">
                    <div class="border border-white/10 p-6 rounded-2xl">
                        <div class="flex justify-between items-center mb-4">
                            <h4 class="font-bold">Kích hoạt Gói Dùng Thử (Free Trial)</h4>
                            <div class="relative inline-block w-10 align-middle select-none transition duration-200 ease-in cursor-pointer">
                                <input type="checkbox" name="toggle" id="toggle1" class="toggle-checkbox absolute block w-4 h-4 rounded-full bg-white border-4 appearance-none cursor-pointer"/>
                                <label for="toggle1" class="toggle-label block overflow-hidden h-6 rounded-full bg-green-500 cursor-pointer"></label>
                            </div>
                        </div>
                        <p class="text-xs text-slate-400 mb-4">Cho phép khách hàng đăng ký trải nghiệm miễn phí sản phẩm của cửa hàng.</p>
                        <label class="block text-xs font-bold text-slate-400 mb-2">Số ngày dùng thử</label>
                        <input type="number" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white" value="7">
                    </div>

                    <div class="border border-[#7B2DFF]/30 p-6 rounded-2xl bg-[#7B2DFF]/5">
                        <div class="flex justify-between items-center mb-4">
                            <h4 class="font-bold text-[#7B2DFF]">Tự Động Upsell (Gợi ý Mua Kèm)</h4>
                            <div class="relative inline-block w-10 align-middle select-none transition duration-200 ease-in cursor-pointer">
                                <input type="checkbox" checked class="accent-[#7B2DFF] w-5 h-5"/>
                            </div>
                        </div>
                        <p class="text-xs text-slate-400 mb-4">Bot AI sẽ tự động phân tích giỏ hàng và đề xuất sản phẩm liên quan khi khách sắp thanh toán.</p>
                        <label class="block text-xs font-bold text-slate-400 mb-2">Giới hạn số sản phẩm gợi ý</label>
                        <input type="number" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white" value="2">
                    </div>
                 </div>
            </div>
        </div>
    '''),

    ('bot_builder.html', 'bot_builder', '''
        <div x-data="{ 
            activeTab: 'rag', 
            uploading: false, 
            progress: 0,
            files: ['Chinh_sach_doi_tra.pdf'],
            uploadFile() {
                this.uploading = true;
                this.progress = 0;
                let interval = setInterval(() => {
                    this.progress += 10;
                    if(this.progress >= 100) {
                        clearInterval(interval);
                        setTimeout(() => {
                            this.uploading = false;
                            this.files.unshift('Bao_Cao_San_Pham_2026.docx');
                        }, 500);
                    }
                }, 200);
            }
        }">
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'rag'" class="pb-2 font-bold text-sm px-4 text-[#00F0FF] border-b-2 border-[#00F0FF]">Knowledge Base (RAG Training)</button>
            </div>

            <div x-show="activeTab === 'rag'" class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[400px]">
                <h2 class="text-xl font-bold mb-4">Kho Dữ Liệu RAG (Tài Liệu Đào Tạo Cho AI)</h2>
                
                <div @click="!uploading && uploadFile()" class="border-2 border-dashed border-white/10 rounded-xl p-10 flex flex-col items-center justify-center text-center cursor-pointer transition-colors" :class="uploading ? 'bg-white/5' : 'hover:bg-white/5'">
                    <span x-show="!uploading" class="material-symbols-outlined text-4xl text-slate-500 mb-2">cloud_upload</span>
                    <p x-show="!uploading" class="font-bold text-sm">Bấm vào đây để tải file tài liệu (PDF, DOCX) lên</p>
                    
                    <!-- Progress Bar Simulator -->
                    <div x-show="uploading" style="display:none;" class="w-full max-w-md">
                        <div class="flex justify-between text-xs mb-1"><span class="text-[#00F0FF]">Đang Vector hóa tài liệu (Training AI)...</span><span x-text="progress + '%'"></span></div>
                        <div class="w-full bg-white/10 rounded-full h-2 overflow-hidden">
                            <div class="bg-[#00F0FF] h-2 transition-all duration-200" :style="'width: ' + progress + '%'"></div>
                        </div>
                    </div>
                </div>

                <ul class="mt-6 space-y-2">
                    <template x-for="f in files" :key="f">
                        <li class="flex justify-between items-center bg-white/5 p-4 rounded-xl text-sm text-white">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 bg-red-500/20 text-red-400 rounded flex items-center justify-center"><span class="material-symbols-outlined">picture_as_pdf</span></div>
                                <div>
                                    <p class="font-bold" x-text="f"></p>
                                    <p class="text-[10px] text-slate-400">Kích thước: 2.4 MB</p>
                                </div>
                            </div>
                            <span class="text-xs text-green-400 bg-green-500/20 px-3 py-1 rounded border border-green-500/30">✓ Đã Vectorized</span>
                        </li>
                    </template>
                </ul>
            </div>
        </div>
    '''),

    ('content.html', 'content', '''
        <div x-data="{ 
            activeTab: 'media',
            uploading: false,
            images: ['https://placehold.co/400x400/121214/475569?text=Banner+Tet', 'https://placehold.co/400x400/121214/475569?text=Sale+Thang+8'],
            simulateUpload() {
                this.uploading = true;
                setTimeout(() => {
                    this.uploading = false;
                    this.images.unshift('https://placehold.co/400x400/10B981/0A0A0A?text=Anh+San+Pham+Moi');
                }, 1500);
            }
        }">
            <h2 class="text-xl font-bold mb-6">Quản Lý Nội Dung & Media</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button class="pb-2 font-bold text-sm px-4 text-[#00F0FF] border-b-2 border-[#00F0FF]">Thư Viện Media Đa Phương Tiện</button>
            </div>

            <div class="flex justify-between items-center mb-4">
                <h3 class="font-bold">Kho Ảnh / Video Của Doanh Nghiệp</h3>
                <button @click="simulateUpload()" class="px-6 py-2 bg-[#00F0FF] text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-cyan-400">
                    <span x-show="!uploading" class="material-symbols-outlined text-[18px]">upload</span> 
                    <span x-show="!uploading">Tải Lên Media</span>
                    <span x-show="uploading" class="material-symbols-outlined animate-spin text-[18px]">sync</span>
                    <span x-show="uploading">Đang xử lý...</span>
                </button>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <template x-for="img in images" :key="img">
                    <div class="aspect-square rounded-2xl overflow-hidden border border-white/10 relative group">
                        <img :src="img" class="w-full h-full object-cover transition-transform group-hover:scale-105">
                        <div class="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2">
                            <button class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center hover:bg-white/40"><span class="material-symbols-outlined text-white">visibility</span></button>
                            <button class="w-10 h-10 bg-red-500/80 rounded-full flex items-center justify-center hover:bg-red-500"><span class="material-symbols-outlined text-white">delete</span></button>
                        </div>
                    </div>
                </template>
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

print("Đã kích hoạt CHUYÊN SÂU: Form nhập Token API, Thanh Progress Bar Upload, Cấu hình Chiến Lược Bán Hàng Free Trial.")
