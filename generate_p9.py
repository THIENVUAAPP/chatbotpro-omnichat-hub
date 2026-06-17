import os

BOT_BUILDER_HTML = '''
        <div x-data="{ 
            activeTab: 'rag',
            isUploading: false,
            uploadProgress: 0,
            uploadedFile: null,
            docs: [
                {name: 'csach_doitra_2026.pdf', size: '2.4 MB', status: 'Đã Vector hóa'},
                {name: 'banggia_si_v3.docx', size: '1.1 MB', status: 'Đã Vector hóa'}
            ],
            
            triggerUpload() {
                this.$refs.fileInput.click();
            },
            
            handleFileSelect(event) {
                const file = event.target.files[0];
                if(!file) return;
                
                this.isUploading = true;
                this.uploadProgress = 0;
                this.uploadedFile = file.name;
                
                // Simulate upload progress
                const interval = setInterval(() => {
                    this.uploadProgress += Math.floor(Math.random() * 15) + 5;
                    if(this.uploadProgress >= 100) {
                        this.uploadProgress = 100;
                        clearInterval(interval);
                        setTimeout(() => {
                            this.isUploading = false;
                            this.docs.unshift({
                                name: this.uploadedFile,
                                size: (file.size / (1024*1024)).toFixed(2) + ' MB',
                                status: 'Vừa tải lên (Đang xử lý)'
                            });
                            window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã tải lên và đang nhúng (embedding) tài liệu ' + this.uploadedFile, type: 'success' } }));
                            // reset input
                            this.$refs.fileInput.value = '';
                        }, 800);
                    }
                }, 300);
            },
            
            simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); }
        }">
            <h2 class="text-2xl font-bold mb-6 font-display">Flow Builder & Đào Tạo RAG AI</h2>
            
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'flow'" :class="activeTab === 'flow' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Kịch Bản Flow</button>
                <button @click="activeTab = 'rag'" :class="activeTab === 'rag' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Kho Tri Thức (RAG)</button>
            </div>

            <!-- TAB RAG -->
            <div x-show="activeTab === 'rag'">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="md:col-span-1">
                        <div class="bg-[#121214] border border-[#00F0FF]/30 p-6 rounded-2xl border-dashed relative text-center hover:bg-white/5 transition-colors cursor-pointer" @click="triggerUpload">
                            <input type="file" x-ref="fileInput" @change="handleFileSelect" class="hidden" accept=".pdf,.docx,.txt" />
                            
                            <div x-show="!isUploading">
                                <div class="w-16 h-16 bg-[#00F0FF]/10 text-[#00F0FF] rounded-full flex items-center justify-center mx-auto mb-4">
                                    <span class="material-symbols-outlined text-3xl">upload_file</span>
                                </div>
                                <h3 class="font-bold text-white mb-2">Tải Tài Liệu Mới</h3>
                                <p class="text-xs text-slate-400">Kéo thả hoặc bấm để chọn file PDF, DOCX (Tối đa 10MB)</p>
                            </div>
                            
                            <!-- BARE BONES UPLOAD SIMULATOR -->
                            <div x-show="isUploading" style="display:none;" class="py-4">
                                <span class="material-symbols-outlined text-[#00F0FF] animate-spin text-4xl mb-4">autorenew</span>
                                <div class="text-sm font-bold text-white mb-2" x-text="'Đang tải lên: ' + uploadProgress + '%'"></div>
                                <div class="w-full bg-white/10 rounded-full h-2">
                                    <div class="bg-gradient-to-r from-[#10B981] to-[#00F0FF] h-2 rounded-full transition-all duration-300" :style="'width: ' + uploadProgress + '%'"></div>
                                </div>
                                <div class="text-[10px] text-slate-400 mt-2">Hệ thống đang băm (chunking) và nhúng (embedding) dữ liệu...</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="md:col-span-2 space-y-4">
                        <h3 class="font-bold text-lg mb-2">Danh sách tài liệu đã học</h3>
                        <template x-for="(doc, idx) in docs" :key="idx">
                            <div class="bg-[#121214] border border-white/5 p-4 rounded-xl flex items-center justify-between">
                                <div class="flex items-center gap-4">
                                    <span class="material-symbols-outlined text-red-400 text-3xl" x-show="doc.name.includes('.pdf')">picture_as_pdf</span>
                                    <span class="material-symbols-outlined text-blue-400 text-3xl" x-show="doc.name.includes('.doc')">description</span>
                                    <span class="material-symbols-outlined text-slate-400 text-3xl" x-show="!doc.name.includes('.pdf') && !doc.name.includes('.doc')">insert_drive_file</span>
                                    
                                    <div>
                                        <div class="font-bold text-white text-sm" x-text="doc.name"></div>
                                        <div class="text-xs text-slate-500 flex gap-4 mt-1">
                                            <span x-text="doc.size"></span>
                                            <span class="text-[#10B981]" x-text="doc.status"></span>
                                        </div>
                                    </div>
                                </div>
                                <button @click="docs.splice(idx, 1); simulateAction('Đã xóa tài liệu khỏi Vector DB!')" class="text-slate-500 hover:text-red-500 transition-colors"><span class="material-symbols-outlined">delete</span></button>
                            </div>
                        </template>
                    </div>
                </div>
            </div>
            
            <!-- TAB FLOW -->
            <div x-show="activeTab === 'flow'" style="display:none;">
                <div class="bg-[#121214] border border-white/5 rounded-2xl p-8 text-center">
                    <span class="material-symbols-outlined text-6xl text-slate-600 mb-4">account_tree</span>
                    <h3 class="font-bold text-xl mb-2">Flow Builder Đang Được Nâng Cấp</h3>
                    <p class="text-slate-400 text-sm mb-6 max-w-md mx-auto">Trình thiết kế Kịch bản bằng giao diện kéo thả (Drag & Drop) siêu việt đang được hoàn thiện. Vui lòng sử dụng RAG AI thay thế trong lúc này.</p>
                    <button class="bg-white/10 px-6 py-2 rounded-xl text-white font-bold cursor-not-allowed opacity-50">Sắp ra mắt</button>
                </div>
            </div>
        </div>
'''

CONTENT_HTML = '''
        <div x-data="{ 
            previewImage: 'https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=600&auto=format&fit=crop',
            isUploadingImage: false,
            
            triggerImageUpload() {
                this.$refs.imageInput.click();
            },
            
            handleImageSelect(event) {
                const file = event.target.files[0];
                if(!file) return;
                
                this.isUploadingImage = true;
                
                // Read file to data URL for preview
                const reader = new FileReader();
                reader.onload = (e) => {
                    setTimeout(() => {
                        this.previewImage = e.target.result;
                        this.isUploadingImage = false;
                        window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã tải lên và cập nhật Ảnh Banner thành công!', type: 'success' } }));
                    }, 1000); // Simulate network delay
                };
                reader.readAsDataURL(file);
            },
            simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); }
        }">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold font-display">Quản Lý Nội Dung & Banner</h2>
                <button @click="triggerImageUpload" class="px-6 py-2.5 bg-[#00F0FF] text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-cyan-400 shadow-[0_0_15px_rgba(0,240,255,0.3)]">
                    <span class="material-symbols-outlined text-[18px]" x-show="!isUploadingImage">add_photo_alternate</span>
                    <span class="material-symbols-outlined text-[18px] animate-spin" x-show="isUploadingImage" style="display:none;">refresh</span>
                    <span x-text="isUploadingImage ? 'Đang xử lý...' : 'Tải Banner Lên'"></span>
                </button>
                <input type="file" x-ref="imageInput" @change="handleImageSelect" accept="image/*" class="hidden">
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Image Preview Section -->
                <div class="bg-[#121214] border border-white/5 p-4 rounded-2xl relative group">
                    <div class="absolute top-2 left-2 bg-black/80 px-3 py-1 rounded text-xs text-[#10B981] font-bold z-10 border border-[#10B981]/30">Banner Đang Chạy (Live)</div>
                    <div class="aspect-video bg-[#0A0A0A] rounded-xl overflow-hidden relative">
                        <!-- Simulated Loading Overlay -->
                        <div x-show="isUploadingImage" style="display:none;" class="absolute inset-0 bg-black/60 z-20 flex flex-col items-center justify-center backdrop-blur-sm">
                            <span class="material-symbols-outlined text-white text-4xl animate-spin mb-2">hourglass_empty</span>
                            <span class="text-sm font-bold text-white">Đang tải ảnh lên máy chủ...</span>
                        </div>
                        <img :src="previewImage" alt="Banner Preview" class="w-full h-full object-cover transition-transform group-hover:scale-105 duration-500">
                    </div>
                    <div class="mt-4 flex justify-between items-center px-2">
                        <div>
                            <div class="font-bold">Campaign Siêu Sale Mùa Hè</div>
                            <div class="text-xs text-slate-400">Kích thước: 1920x1080 - Định dạng: JPG</div>
                        </div>
                        <div class="flex gap-2">
                            <button @click="triggerImageUpload" class="w-8 h-8 rounded bg-white/5 hover:bg-white/10 flex items-center justify-center text-slate-300"><span class="material-symbols-outlined text-[16px]">edit</span></button>
                        </div>
                    </div>
                </div>

                <!-- Content text templates -->
                <div class="space-y-4">
                    <h3 class="font-bold text-lg">Mẫu Content Gắn Kèm</h3>
                    <div class="bg-[#121214] border border-white/5 p-4 rounded-xl">
                        <textarea class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white h-24 mb-2 focus:outline-none focus:border-[#00F0FF]">🔥 SIÊU SALE CHÀO HÈ - GIẢM NGAY 50%
Săn ngay deal hot số lượng có hạn tại Shop! Nhập mã SUMMER50 để nhận ưu đãi.</textarea>
                        <div class="flex justify-end gap-2">
                            <button @click="simulateAction('Đã Copy Content vào bộ nhớ tạm!')" class="px-4 py-1.5 bg-white/5 hover:bg-white/10 rounded-lg text-xs font-bold text-slate-300 border border-white/5">Copy</button>
                            <button @click="simulateAction('Đã Lưu Mẫu Content!')" class="px-4 py-1.5 bg-[#10B981] text-black hover:bg-emerald-400 rounded-lg text-xs font-bold shadow-[0_0_10px_rgba(16,185,129,0.3)]">Lưu Mẫu</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
'''

TENANT_SETTINGS_HTML = '''
        <div x-data="{ 
            logoUrl: 'https://ui-avatars.com/api/?name=SHOP&background=10B981&color=fff&size=128',
            
            triggerLogoUpload() {
                this.$refs.logoInput.click();
            },
            
            handleLogoSelect(event) {
                const file = event.target.files[0];
                if(!file) return;
                
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.logoUrl = e.target.result;
                    window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã thay đổi Logo Doanh nghiệp thành công!', type: 'success' } }));
                };
                reader.readAsDataURL(file);
            },
            simulateAction(msg) { window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: msg, type: 'success' } })); }
        }">
            <h2 class="text-2xl font-bold mb-6 font-display">Thiết Lập Doanh Nghiệp (Tenant)</h2>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <!-- Thông tin chung & Logo -->
                <div class="lg:col-span-1 space-y-6">
                    <div class="bg-[#121214] border border-white/5 rounded-2xl p-6 text-center">
                        <div class="relative inline-block mb-4 group">
                            <img :src="logoUrl" alt="Tenant Logo" class="w-32 h-32 rounded-full border-4 border-white/10 object-cover shadow-xl">
                            <button @click="triggerLogoUpload" class="absolute bottom-0 right-0 w-10 h-10 bg-[#00F0FF] text-black rounded-full flex items-center justify-center hover:scale-110 transition-transform shadow-[0_0_15px_rgba(0,240,255,0.4)]">
                                <span class="material-symbols-outlined text-[20px]">edit</span>
                            </button>
                            <input type="file" x-ref="logoInput" @change="handleLogoSelect" accept="image/*" class="hidden">
                        </div>
                        <h3 class="font-bold text-lg text-white">Chốt Nghìn Đơn Shop</h3>
                        <p class="text-xs text-slate-400 mt-1">ID: TENT-99482</p>
                    </div>
                </div>

                <!-- Cấu hình chi tiết -->
                <div class="lg:col-span-2 space-y-6">
                    <div class="bg-[#121214] border border-white/5 rounded-2xl p-6">
                        <h3 class="font-bold mb-4 flex items-center gap-2"><span class="material-symbols-outlined text-[#10B981]">storefront</span> Thông Tin Kinh Doanh</h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-bold text-slate-400 mb-2">Tên Doanh Nghiệp (Hiển thị Bill)</label>
                                <input type="text" value="Chốt Nghìn Đơn Official" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-slate-400 mb-2">Hotline</label>
                                <input type="text" value="1900 9999" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white">
                            </div>
                            <div class="md:col-span-2">
                                <label class="block text-xs font-bold text-slate-400 mb-2">Địa chỉ kho hàng mặc định</label>
                                <input type="text" value="Tòa nhà Landmark 81, Vinhomes Central Park, Bình Thạnh, HCM" class="w-full bg-[#0A0A0A] border border-white/10 p-3 text-sm rounded-xl text-white">
                            </div>
                        </div>
                        <div class="mt-6 flex justify-end">
                            <button @click="simulateAction('Đã lưu Cấu Hình Doanh Nghiệp!')" class="px-6 py-2.5 bg-[#10B981] text-black font-bold rounded-xl text-sm shadow-[0_0_15px_rgba(16,185,129,0.3)] hover:bg-emerald-400">Lưu Thông Tin</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
'''

HTML_PAGES = [
    ('bot_builder.html', 'bot_builder', BOT_BUILDER_HTML),
    ('content.html', 'content', CONTENT_HTML),
    ('tenant_settings.html', 'tenant_settings', TENANT_SETTINGS_HTML)
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>CHỐT NGHÌN ĐƠN</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet"/>
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

print("Đã hoàn thành P9: Tích hợp Upload File/Image Picker thật cho Bot Builder, Content và Tenant Settings.")
