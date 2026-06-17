import os

DASHBOARD_HTML = '''
        <div x-data="{ 
            replyText: '',
            messages: [
                { sender: 'customer', text: 'Chào shop, cho mình hỏi áo thun mã 01 còn hàng không?', time: '10:30' },
                { sender: 'bot', text: 'Dạ áo thun mã 01 hiện tại bên em vẫn còn đủ size ạ. Bạn muốn lấy màu gì?', time: '10:31' }
            ],
            
            sendMessage() {
                if(this.replyText.trim() === '') return;
                this.messages.push({
                    sender: 'admin',
                    text: this.replyText,
                    time: new Date().toLocaleTimeString('vi-VN', {hour: '2-digit', minute:'2-digit'})
                });
                this.replyText = '';
                
                // Scroll to bottom simulation
                setTimeout(() => {
                    const chatBox = this.$refs.chatContainer;
                    if(chatBox) chatBox.scrollTop = chatBox.scrollHeight;
                }, 100);
            }
        }">
            <h2 class="text-2xl font-bold mb-6 font-display">Dashboard & Inbox Đa Kênh</h2>
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[calc(100vh-160px)]">
                <!-- Danh sách chat -->
                <div class="bg-[#121214] border border-white/5 rounded-2xl flex flex-col h-full overflow-hidden">
                    <div class="p-4 border-b border-white/5 flex justify-between items-center bg-[#0A0A0A]/50">
                        <div class="font-bold text-sm">Hộp thư đến</div>
                        <div class="flex gap-2">
                            <span class="w-6 h-6 bg-blue-500 rounded flex items-center justify-center text-white"><span class="material-symbols-outlined text-[14px]">forum</span></span>
                            <span class="w-6 h-6 bg-black border border-white/20 rounded flex items-center justify-center text-white"><span class="material-symbols-outlined text-[14px]">shopping_bag</span></span>
                        </div>
                    </div>
                    <div class="flex-1 overflow-y-auto custom-scrollbar p-2 space-y-1">
                        <div class="p-3 bg-white/10 border-l-4 border-[#00F0FF] rounded-lg cursor-pointer">
                            <div class="flex justify-between items-center mb-1">
                                <div class="font-bold text-sm text-[#00F0FF]">Nguyễn Thị Mai</div>
                                <div class="text-[10px] text-slate-400">10:30</div>
                            </div>
                            <div class="text-xs text-slate-300 truncate">Chào shop, cho mình hỏi áo thun mã...</div>
                        </div>
                        <div class="p-3 hover:bg-white/5 rounded-lg cursor-pointer transition-colors border-l-4 border-transparent">
                            <div class="flex justify-between items-center mb-1">
                                <div class="font-bold text-sm text-white">Trần Văn Hoàng</div>
                                <div class="text-[10px] text-slate-400">09:15</div>
                            </div>
                            <div class="text-xs text-slate-400 truncate">Mình muốn đặt 2 đôi giày thể thao...</div>
                        </div>
                    </div>
                </div>

                <!-- Khung Chat Chính -->
                <div class="lg:col-span-2 bg-[#121214] border border-white/5 rounded-2xl flex flex-col h-full relative overflow-hidden">
                    <!-- Chat Header -->
                    <div class="p-4 border-b border-white/5 bg-[#0A0A0A]/50 flex justify-between items-center z-10 relative">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 bg-gradient-to-br from-[#10B981] to-[#00F0FF] rounded-full flex items-center justify-center font-bold text-black shadow-[0_0_10px_rgba(16,185,129,0.5)]">M</div>
                            <div>
                                <div class="font-bold text-sm flex items-center gap-2">Nguyễn Thị Mai <span class="px-2 py-0.5 bg-[#FFD700]/10 text-[#FFD700] rounded text-[10px] border border-[#FFD700]/30">VIP</span></div>
                                <div class="text-xs text-slate-400">Đến từ: Tiktok Shop</div>
                            </div>
                        </div>
                        <button class="bg-[#10B981]/20 text-[#10B981] px-3 py-1.5 rounded-lg text-xs font-bold border border-[#10B981]/30 hover:bg-[#10B981]/30">Tạo Đơn Hàng</button>
                    </div>

                    <!-- Chat Messages -->
                    <div class="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar" x-ref="chatContainer">
                        <template x-for="(msg, i) in messages" :key="i">
                            <div class="flex" :class="msg.sender === 'customer' ? 'justify-start' : 'justify-end'">
                                <div class="max-w-[70%]">
                                    <div class="flex items-end gap-2" :class="msg.sender === 'customer' ? 'flex-row' : 'flex-row-reverse'">
                                        <div class="w-6 h-6 rounded-full flex items-center justify-center text-[10px] shrink-0"
                                             :class="msg.sender === 'customer' ? 'bg-slate-700' : (msg.sender === 'bot' ? 'bg-gradient-to-r from-[#7B2DFF] to-[#00F0FF] font-bold text-black' : 'bg-[#10B981] text-black font-bold')">
                                            <span x-text="msg.sender === 'customer' ? 'M' : (msg.sender === 'bot' ? 'AI' : 'AD')"></span>
                                        </div>
                                        <div class="p-3 rounded-2xl text-sm"
                                             :class="msg.sender === 'customer' ? 'bg-[#0A0A0A] border border-white/10 rounded-tl-sm text-slate-200' : (msg.sender === 'bot' ? 'bg-[#7B2DFF]/20 border border-[#7B2DFF]/30 rounded-tr-sm text-white' : 'bg-[#10B981]/20 border border-[#10B981]/30 rounded-tr-sm text-white')">
                                            <span x-text="msg.text"></span>
                                        </div>
                                    </div>
                                    <div class="text-[10px] text-slate-500 mt-1" :class="msg.sender === 'customer' ? 'text-left ml-8' : 'text-right mr-8'" x-text="msg.time"></div>
                                </div>
                            </div>
                        </template>
                    </div>

                    <!-- Chat Input -->
                    <div class="p-4 border-t border-white/5 bg-[#0A0A0A]/50 z-10 relative">
                        <div class="flex items-center gap-2">
                            <button class="w-10 h-10 rounded-xl bg-white/5 hover:bg-white/10 flex items-center justify-center text-slate-400 shrink-0"><span class="material-symbols-outlined">add_circle</span></button>
                            <input @keydown.enter="sendMessage" x-model="replyText" type="text" placeholder="Nhập tin nhắn để trả lời khách hàng..." class="flex-1 bg-[#121214] border border-white/10 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-[#00F0FF] text-white">
                            <button @click="sendMessage" class="w-10 h-10 rounded-xl bg-[#00F0FF] hover:bg-cyan-400 flex items-center justify-center text-black shrink-0 shadow-[0_0_10px_rgba(0,240,255,0.4)]"><span class="material-symbols-outlined text-[20px]">send</span></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
'''

BOT_BUILDER_HTML = '''
        <div x-data="{ 
            activeTab: 'flow',
            isUploading: false,
            uploadProgress: 0,
            uploadedFile: null,
            docs: [
                {name: 'csach_doitra_2026.pdf', size: '2.4 MB', status: 'Đã Vector hóa'},
                {name: 'banggia_si_v3.docx', size: '1.1 MB', status: 'Đã Vector hóa'}
            ],
            
            triggerUpload() { this.$refs.fileInput.click(); },
            handleFileSelect(event) {
                const file = event.target.files[0];
                if(!file) return;
                this.isUploading = true;
                this.uploadProgress = 0;
                this.uploadedFile = file.name;
                const interval = setInterval(() => {
                    this.uploadProgress += Math.floor(Math.random() * 15) + 5;
                    if(this.uploadProgress >= 100) {
                        this.uploadProgress = 100;
                        clearInterval(interval);
                        setTimeout(() => {
                            this.isUploading = false;
                            this.docs.unshift({ name: this.uploadedFile, size: (file.size / (1024*1024)).toFixed(2) + ' MB', status: 'Vừa tải lên (Đang xử lý)' });
                            window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã tải lên ' + this.uploadedFile, type: 'success' } }));
                            this.$refs.fileInput.value = '';
                        }, 800);
                    }
                }, 300);
            }
        }">
            <h2 class="text-2xl font-bold mb-6 font-display">Flow Builder & Đào Tạo RAG AI</h2>
            
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'flow'" :class="activeTab === 'flow' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Kịch Bản Flow</button>
                <button @click="activeTab = 'rag'" :class="activeTab === 'rag' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Kho Tri Thức (RAG)</button>
            </div>

            <!-- TAB FLOW: NEW FAKE DIAGRAM -->
            <div x-show="activeTab === 'flow'" class="relative h-[600px] bg-[#121214] border border-white/5 rounded-2xl overflow-hidden bg-[url('https://www.transparenttextures.com/patterns/graphy.png')]">
                <!-- Toolbar -->
                <div class="absolute top-4 left-4 flex gap-2 z-10">
                    <button class="bg-black/80 backdrop-blur border border-white/10 px-4 py-2 rounded-xl text-xs font-bold text-[#00F0FF] hover:bg-white/5">+ Thêm Block Tin Nhắn</button>
                    <button class="bg-black/80 backdrop-blur border border-white/10 px-4 py-2 rounded-xl text-xs font-bold text-[#10B981] hover:bg-white/5">+ Rẽ Nhánh Điều Kiện</button>
                </div>
                
                <!-- Fake Nodes -->
                <div class="absolute top-20 left-1/2 -translate-x-1/2 w-64 bg-[#0A0A0A] border border-[#00F0FF]/50 rounded-xl p-4 shadow-[0_0_20px_rgba(0,240,255,0.2)] z-10">
                    <div class="flex items-center gap-2 mb-2 border-b border-white/10 pb-2">
                        <span class="material-symbols-outlined text-[#00F0FF] text-[18px]">play_circle</span>
                        <span class="font-bold text-sm text-[#00F0FF]">Bắt Đầu Kịch Bản</span>
                    </div>
                    <div class="text-xs text-slate-400">Kích hoạt khi: Khách nhắn tin lần đầu</div>
                </div>
                
                <!-- Fake Line -->
                <div class="absolute top-[150px] left-1/2 -translate-x-1/2 w-0.5 h-16 bg-[#00F0FF]/50 z-0"></div>

                <div class="absolute top-[210px] left-1/2 -translate-x-1/2 w-64 bg-[#0A0A0A] border border-[#10B981]/50 rounded-xl p-4 shadow-[0_0_20px_rgba(16,185,129,0.2)] z-10">
                    <div class="flex items-center gap-2 mb-2 border-b border-white/10 pb-2">
                        <span class="material-symbols-outlined text-[#10B981] text-[18px]">chat</span>
                        <span class="font-bold text-sm text-[#10B981]">Gửi Tin Nhắn AI</span>
                    </div>
                    <div class="text-xs text-slate-300">"Chào bạn, tôi có thể giúp gì cho bạn hôm nay?"</div>
                </div>
                
                <!-- Sơ đồ rẽ nhánh -->
                <div class="absolute top-[310px] left-1/2 -translate-x-[160px] w-[320px] h-0.5 bg-[#10B981]/50 z-0"></div>
                <div class="absolute top-[310px] left-[calc(50%-160px)] w-0.5 h-10 bg-[#10B981]/50 z-0"></div>
                <div class="absolute top-[310px] left-[calc(50%+160px)] w-0.5 h-10 bg-[#10B981]/50 z-0"></div>

                <div class="absolute top-[350px] left-[calc(50%-220px)] w-56 bg-[#0A0A0A] border border-[#FFD700]/50 rounded-xl p-4 z-10">
                    <div class="flex items-center gap-2 mb-2 border-b border-white/10 pb-2">
                        <span class="material-symbols-outlined text-[#FFD700] text-[18px]">call_split</span>
                        <span class="font-bold text-sm text-[#FFD700]">Hỏi về Sản Phẩm</span>
                    </div>
                    <div class="text-xs text-slate-400">Kích hoạt AI RAG tư vấn</div>
                </div>

                <div class="absolute top-[350px] left-[calc(50%+40px)] w-56 bg-[#0A0A0A] border border-red-500/50 rounded-xl p-4 z-10">
                    <div class="flex items-center gap-2 mb-2 border-b border-white/10 pb-2">
                        <span class="material-symbols-outlined text-red-500 text-[18px]">support_agent</span>
                        <span class="font-bold text-sm text-red-500">Khiếu nại / Gặp NV</span>
                    </div>
                    <div class="text-xs text-slate-400">Chuyển đoạn chat cho Admin</div>
                </div>
            </div>

            <!-- TAB RAG -->
            <div x-show="activeTab === 'rag'" style="display:none;">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="md:col-span-1">
                        <div class="bg-[#121214] border border-[#00F0FF]/30 p-6 rounded-2xl border-dashed relative text-center hover:bg-white/5 transition-colors cursor-pointer" @click="triggerUpload">
                            <input type="file" x-ref="fileInput" @change="handleFileSelect" class="hidden" accept=".pdf,.docx,.txt" />
                            <div x-show="!isUploading">
                                <div class="w-16 h-16 bg-[#00F0FF]/10 text-[#00F0FF] rounded-full flex items-center justify-center mx-auto mb-4"><span class="material-symbols-outlined text-3xl">upload_file</span></div>
                                <h3 class="font-bold text-white mb-2">Tải Tài Liệu Mới</h3>
                                <p class="text-xs text-slate-400">Kéo thả hoặc bấm để chọn file PDF, DOCX</p>
                            </div>
                            <div x-show="isUploading" style="display:none;" class="py-4">
                                <span class="material-symbols-outlined text-[#00F0FF] animate-spin text-4xl mb-4">autorenew</span>
                                <div class="text-sm font-bold text-white mb-2" x-text="'Đang tải lên: ' + uploadProgress + '%'"></div>
                                <div class="w-full bg-white/10 rounded-full h-2">
                                    <div class="bg-gradient-to-r from-[#10B981] to-[#00F0FF] h-2 rounded-full transition-all duration-300" :style="'width: ' + uploadProgress + '%'"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="md:col-span-2 space-y-4">
                        <template x-for="(doc, idx) in docs" :key="idx">
                            <div class="bg-[#121214] border border-white/5 p-4 rounded-xl flex items-center justify-between">
                                <div class="flex items-center gap-4">
                                    <span class="material-symbols-outlined text-red-400 text-3xl" x-show="doc.name.includes('.pdf')">picture_as_pdf</span>
                                    <span class="material-symbols-outlined text-blue-400 text-3xl" x-show="doc.name.includes('.doc')">description</span>
                                    <span class="material-symbols-outlined text-slate-400 text-3xl" x-show="!doc.name.includes('.pdf') && !doc.name.includes('.doc')">insert_drive_file</span>
                                    <div>
                                        <div class="font-bold text-white text-sm" x-text="doc.name"></div>
                                        <div class="text-xs text-slate-500 flex gap-4 mt-1"><span x-text="doc.size"></span><span class="text-[#10B981]" x-text="doc.status"></span></div>
                                    </div>
                                </div>
                                <button @click="docs.splice(idx, 1)" class="text-slate-500 hover:text-red-500"><span class="material-symbols-outlined">delete</span></button>
                            </div>
                        </template>
                    </div>
                </div>
            </div>
        </div>
'''

ECOMMERCE_HTML = '''
        <div x-data="{ 
            activeTab: 'products',
            showModal: false,
            newProduct: { name: '', price: '', channel: 'Shopee' },
            products: [
                { name: 'Áo Thun Cổ Tròn Mẫu 01', price: '150,000đ', channel: 'Shopee/Tiktok' }
            ],
            saveProduct() {
                if(!this.newProduct.name || !this.newProduct.price) return;
                this.products.unshift({
                    name: this.newProduct.name,
                    price: this.newProduct.price + 'đ',
                    channel: this.newProduct.channel
                });
                this.showModal = false;
                this.newProduct.name = ''; this.newProduct.price = '';
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã thêm sản phẩm thành công!', type: 'success' } }));
            }
        }">
            <h2 class="text-xl font-bold mb-6">Quản Lý Sản Phẩm & Đơn Hàng (Đa Kênh)</h2>
            <div class="mb-6 flex gap-4 border-b border-white/5">
                <button @click="activeTab = 'products'" :class="activeTab === 'products' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Kho Sản Phẩm</button>
                <button @click="activeTab = 'orders'" :class="activeTab === 'orders' ? 'text-[#00F0FF] border-b-2 border-[#00F0FF]' : 'text-slate-400'" class="pb-2 font-bold text-sm px-4">Đơn Hàng Vận Chuyển</button>
            </div>

            <div x-show="activeTab === 'products'">
                <div class="flex justify-between items-center mb-4">
                    <input type="text" placeholder="Tìm sản phẩm..." class="bg-[#0A0A0A] border border-white/10 rounded-xl px-4 py-2 text-sm w-64 text-white">
                    <button @click="showModal = true" class="bg-[#00F0FF] text-black px-4 py-2 rounded-xl text-sm font-bold hover:bg-cyan-400">+ Thêm Sản Phẩm</button>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <template x-for="(prod, idx) in products" :key="idx">
                        <div class="bg-[#121214] border border-white/5 rounded-2xl overflow-hidden group">
                            <div class="h-40 bg-white/5 flex items-center justify-center relative">
                                <span class="material-symbols-outlined text-4xl text-slate-600">checkroom</span>
                                <div class="absolute top-2 right-2 bg-black/80 px-2 py-1 rounded text-xs text-[#00F0FF] border border-[#00F0FF]/30" x-text="prod.channel"></div>
                            </div>
                            <div class="p-4">
                                <h3 class="font-bold text-white mb-1" x-text="prod.name"></h3>
                                <div class="text-[#10B981] font-bold text-sm mb-3" x-text="prod.price"></div>
                                <div class="flex gap-2">
                                    <button class="flex-1 bg-white/5 py-1.5 rounded-lg text-xs font-bold hover:bg-white/10 text-white">Sửa</button>
                                    <button @click="products.splice(idx,1)" class="w-8 flex items-center justify-center bg-red-500/10 text-red-500 rounded-lg hover:bg-red-500 hover:text-white transition-colors"><span class="material-symbols-outlined text-[14px]">delete</span></button>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
            </div>

            <div x-show="activeTab === 'orders'" style="display:none;">
                <div class="flex justify-between items-center mb-4">
                    <div class="flex gap-2">
                        <button class="bg-[#10B981]/20 text-[#10B981] px-4 py-1.5 rounded-lg text-xs font-bold border border-[#10B981]/30">Giao Hàng Nhanh (GHN)</button>
                    </div>
                </div>
                <div class="bg-[#121214] border border-white/5 rounded-2xl overflow-hidden">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="text-xs uppercase bg-white/5 border-b border-white/5">
                            <tr><th class="px-4 py-4">Mã Đơn</th><th class="px-4 py-4">Khách Hàng</th><th class="px-4 py-4">Tổng Tiền</th><th class="px-4 py-4">Trạng Thái</th></tr>
                        </thead>
                        <tbody>
                            <tr class="border-b border-white/5"><td class="px-4 py-3 font-bold text-[#00F0FF]">#ORD-991</td><td class="px-4 py-3">Lê Văn A</td><td class="px-4 py-3 font-bold text-white">350,000đ</td><td class="px-4 py-3"><span class="px-2 py-1 bg-[#FFD700]/10 text-[#FFD700] border border-[#FFD700]/30 rounded text-[10px] font-bold">Đang lấy hàng</span></td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- ADD PRODUCT MODAL -->
            <div x-show="showModal" style="display:none;" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[100] flex items-center justify-center">
                <div class="bg-[#121214] border border-[#00F0FF]/30 p-6 rounded-2xl w-96 shadow-2xl">
                    <h3 class="text-lg font-bold mb-4 text-[#00F0FF]">Thêm Sản Phẩm Mới</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Tên Sản Phẩm</label>
                            <input x-model="newProduct.name" type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Giá (VNĐ)</label>
                            <input x-model="newProduct.price" type="number" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Kênh Bán</label>
                            <select x-model="newProduct.channel" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                                <option>Shopee</option>
                                <option>Tiktok</option>
                                <option>Facebook</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex justify-end gap-2 mt-6">
                        <button @click="showModal = false" class="px-4 py-2 bg-white/5 rounded-lg text-sm font-bold text-white hover:bg-white/10">Hủy</button>
                        <button @click="saveProduct" class="px-4 py-2 bg-[#00F0FF] rounded-lg text-sm font-bold text-black hover:bg-cyan-400 shadow-[0_0_15px_rgba(0,240,255,0.3)]">Lưu Sản Phẩm</button>
                    </div>
                </div>
            </div>
        </div>
'''

CRM_HTML = '''
        <div x-data="{ 
            showModal: false,
            newCus: { name: '', phone: '', source: 'Manual' },
            customers: [
                { name: 'Nguyễn Văn Nam', phone: '0901***456', source: 'Shopee', tag: 'VIP Khách Sỉ' }
            ],
            saveCustomer() {
                if(!this.newCus.name) return;
                this.customers.unshift({
                    name: this.newCus.name,
                    phone: this.newCus.phone || 'N/A',
                    source: this.newCus.source,
                    tag: 'Khách Mới'
                });
                this.showModal = false;
                this.newCus.name = ''; this.newCus.phone = '';
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã thêm Khách Hàng mới thành công!', type: 'success' } }));
            }
        }">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-xl font-bold">Quản Lý Khách Hàng (CRM)</h2>
                <button @click="showModal = true" class="px-4 py-2 bg-[#10B981] text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.3)]">
                    <span class="material-symbols-outlined text-[18px]">person_add</span> Thêm Khách Mới
                </button>
            </div>
            
            <table class="w-full text-left text-sm text-slate-300 bg-[#121214] rounded-2xl overflow-hidden border border-white/5">
                <thead class="text-xs uppercase bg-white/5 border-b border-white/5">
                    <tr><th class="px-4 py-4">Khách Hàng</th><th class="px-4 py-4">Nguồn</th><th class="px-4 py-4">Phân Loại (Tag)</th><th class="px-4 py-4 text-right">Thao Tác</th></tr>
                </thead>
                <tbody>
                    <template x-for="(cus, idx) in customers" :key="idx">
                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                            <td class="px-4 py-4">
                                <div class="font-bold text-white" x-text="cus.name"></div>
                                <div class="text-[10px] text-slate-500 mt-1" x-text="cus.phone"></div>
                            </td>
                            <td class="px-4 py-4"><span class="text-xs font-bold text-[#00F0FF]" x-text="cus.source"></span></td>
                            <td class="px-4 py-4"><span class="px-2 py-1 bg-[#FFD700]/10 text-[#FFD700] rounded border border-[#FFD700]/30 text-[10px] font-bold" x-text="cus.tag"></span></td>
                            <td class="px-4 py-4 text-right flex gap-2 justify-end">
                                <button @click="customers.splice(idx,1)" class="text-xs bg-red-500/10 text-red-500 px-3 py-1 rounded hover:bg-red-500 hover:text-white transition-colors font-bold border border-red-500/30">Xóa</button>
                            </td>
                        </tr>
                    </template>
                </tbody>
            </table>

            <!-- MODAL -->
            <div x-show="showModal" style="display:none;" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[100] flex items-center justify-center">
                <div class="bg-[#121214] border border-[#10B981]/30 p-6 rounded-2xl w-96 shadow-2xl">
                    <h3 class="text-lg font-bold mb-4 text-[#10B981]">Thêm Khách Hàng Thủ Công</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Họ Tên</label>
                            <input x-model="newCus.name" type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Số Điện Thoại</label>
                            <input x-model="newCus.phone" type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                        </div>
                    </div>
                    <div class="flex justify-end gap-2 mt-6">
                        <button @click="showModal = false" class="px-4 py-2 bg-white/5 rounded-lg text-sm font-bold text-white hover:bg-white/10">Hủy</button>
                        <button @click="saveCustomer" class="px-4 py-2 bg-[#10B981] rounded-lg text-sm font-bold text-black hover:bg-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.3)]">Lưu Thông Tin</button>
                    </div>
                </div>
            </div>
        </div>
'''

CAMPAIGNS_HTML = '''
        <div x-data="{
            showModal: false,
            newCamp: { name: '', target: 'Tất cả khách hàng' },
            campaigns: [
                { name: 'Sale Cuối Tuần Tháng 10', target: 'Khách đã mua', status: 'Đã Hoàn Thành', color: 'green', count: '2,504' }
            ],
            saveCamp() {
                if(!this.newCamp.name) return;
                this.campaigns.unshift({
                    name: this.newCamp.name,
                    target: this.newCamp.target,
                    status: 'Đang Lên Lịch',
                    color: 'yellow',
                    count: '0'
                });
                this.showModal = false;
                this.newCamp.name = '';
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã tạo chiến dịch thành công!', type: 'success' } }));
            }
        }">
            <div class="flex justify-between items-center mb-8">
                <h2 class="text-2xl font-bold font-display tracking-tight">Chiến Dịch Gửi Loạt (Broadcast)</h2>
                <button @click="showModal = true" class="px-6 py-2.5 bg-[#10B981] text-black font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.3)]">
                    <span class="material-symbols-outlined">campaign</span> Tạo Chiến Dịch Mới
                </button>
            </div>

            <div class="space-y-4">
                <template x-for="(c, idx) in campaigns" :key="idx">
                    <div class="bg-[#121214] border border-white/5 p-6 rounded-2xl flex justify-between items-center group">
                        <div class="flex items-center gap-4">
                            <div class="w-12 h-12 rounded-full flex items-center justify-center" :class="c.color === 'green' ? 'bg-[#10B981]/10 text-[#10B981]' : 'bg-[#FFD700]/10 text-[#FFD700] animate-pulse'">
                                <span class="material-symbols-outlined">send</span>
                            </div>
                            <div>
                                <h3 class="font-bold text-lg" x-text="c.name"></h3>
                                <div class="text-xs text-slate-400 mt-1 flex gap-4">
                                    <span x-text="'Đối tượng: ' + c.target"></span>
                                </div>
                            </div>
                        </div>
                        <div class="text-right">
                            <div class="text-xs px-2 py-1 rounded border inline-block mb-1" :class="c.color === 'green' ? 'text-green-400 bg-green-500/20 border-green-500/30' : 'text-[#FFD700] bg-[#FFD700]/10 border-[#FFD700]/30'" x-text="c.status"></div>
                            <div class="font-bold text-sm" x-text="'Số lượng: ' + c.count"></div>
                        </div>
                    </div>
                </template>
            </div>

            <!-- MODAL -->
            <div x-show="showModal" style="display:none;" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[100] flex items-center justify-center">
                <div class="bg-[#121214] border border-[#10B981]/30 p-6 rounded-2xl w-96 shadow-2xl">
                    <h3 class="text-lg font-bold mb-4 text-[#10B981]">Khởi Tạo Chiến Dịch Mới</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Tên Chiến Dịch</label>
                            <input x-model="newCamp.name" type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Tệp Khách Hàng</label>
                            <select x-model="newCamp.target" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                                <option>Tất cả khách hàng (Zalo, FB)</option>
                                <option>Khách hàng VIP</option>
                                <option>Khách chưa mua hàng</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex justify-end gap-2 mt-6">
                        <button @click="showModal = false" class="px-4 py-2 bg-white/5 rounded-lg text-sm font-bold text-white hover:bg-white/10">Hủy</button>
                        <button @click="saveCamp" class="px-4 py-2 bg-[#10B981] rounded-lg text-sm font-bold text-black hover:bg-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.3)]">Lên Lịch Gửi</button>
                    </div>
                </div>
            </div>
        </div>
'''

TEAM_MANAGEMENT_HTML = '''
        <div x-data="{ 
            showModal: false,
            newMem: { name: '', role: 'Admin' },
            members: [
                { name: 'Thiên CR7', role: 'Super Admin', status: 'Active' },
                { name: 'Nhân Viên Sale 01', role: 'Sale', status: 'Active' }
            ],
            saveMem() {
                if(!this.newMem.name) return;
                this.members.push({
                    name: this.newMem.name,
                    role: this.newMem.role,
                    status: 'Active'
                });
                this.showModal = false;
                this.newMem.name = '';
                window.dispatchEvent(new CustomEvent('show-toast', { detail: { msg: 'Đã thêm nhân viên thành công!', type: 'success' } }));
            }
        }">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-xl font-bold">Phân Quyền Team (Nhân Sự)</h2>
                <button @click="showModal = true" class="px-4 py-2 bg-[#7B2DFF] text-white font-bold rounded-xl text-sm flex items-center gap-2 hover:bg-purple-500 shadow-[0_0_15px_rgba(123,45,255,0.4)]">
                    <span class="material-symbols-outlined text-[18px]">person_add</span> Thêm Nhân Viên
                </button>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <template x-for="(m, idx) in members" :key="idx">
                    <div class="bg-[#121214] border border-white/5 p-6 rounded-2xl flex items-center gap-4">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-r from-slate-600 to-slate-800 flex items-center justify-center font-bold text-white shadow-lg"
                             :class="m.role === 'Super Admin' ? 'from-[#FFD700] to-orange-500 text-black' : ''">
                            <span class="material-symbols-outlined" x-text="m.role === 'Super Admin' ? 'local_police' : 'person'"></span>
                        </div>
                        <div class="flex-1">
                            <div class="font-bold text-white text-sm" x-text="m.name"></div>
                            <div class="text-[10px] font-bold mt-1 inline-block px-2 py-0.5 rounded border"
                                 :class="m.role === 'Super Admin' ? 'text-[#FFD700] border-[#FFD700]/30 bg-[#FFD700]/10' : 'text-[#00F0FF] border-[#00F0FF]/30 bg-[#00F0FF]/10'" x-text="m.role"></div>
                        </div>
                        <button @click="if(m.role !== 'Super Admin') members.splice(idx,1)" class="text-slate-500 hover:text-red-500" x-show="m.role !== 'Super Admin'"><span class="material-symbols-outlined text-[18px]">delete</span></button>
                    </div>
                </template>
            </div>

            <!-- MODAL -->
            <div x-show="showModal" style="display:none;" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[100] flex items-center justify-center">
                <div class="bg-[#121214] border border-[#7B2DFF]/30 p-6 rounded-2xl w-96 shadow-2xl">
                    <h3 class="text-lg font-bold mb-4 text-[#7B2DFF]">Mời Nhân Viên Mới</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Tên Hiển Thị</label>
                            <input x-model="newMem.name" type="text" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-400 mb-1">Phân Quyền (Role)</label>
                            <select x-model="newMem.role" class="w-full bg-[#0A0A0A] border border-white/10 p-2.5 rounded-lg text-sm text-white">
                                <option>Admin (Quản lý)</option>
                                <option>Sale (Chỉ chat với khách)</option>
                                <option>Marketing (Chỉ xem báo cáo)</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex justify-end gap-2 mt-6">
                        <button @click="showModal = false" class="px-4 py-2 bg-white/5 rounded-lg text-sm font-bold text-white hover:bg-white/10">Hủy</button>
                        <button @click="saveMem" class="px-4 py-2 bg-[#7B2DFF] rounded-lg text-sm font-bold text-white hover:bg-purple-500 shadow-[0_0_15px_rgba(123,45,255,0.4)]">Thêm Nhân Viên</button>
                    </div>
                </div>
            </div>
        </div>
'''

HTML_PAGES = [
    ('dashboard.html', 'dashboard', DASHBOARD_HTML),
    ('bot_builder.html', 'bot_builder', BOT_BUILDER_HTML),
    ('ecommerce.html', 'ecommerce', ECOMMERCE_HTML),
    ('crm.html', 'crm', CRM_HTML),
    ('campaigns.html', 'campaigns', CAMPAIGNS_HTML),
    ('team_management.html', 'team_management', TEAM_MANAGEMENT_HTML)
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

print("Đã hoàn thành P10: Đại Tu Toàn Diện - Thêm dữ liệu động, Modal và Flow Builder Sơ đồ khối.")
