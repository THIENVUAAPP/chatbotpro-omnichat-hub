import os

PAGES = [
    ('dashboard.html', 'dashboard', '''
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl relative overflow-hidden">
                <div class="absolute top-0 right-0 p-4 opacity-10"><span class="material-symbols-outlined text-6xl text-[#00F0FF]">chat</span></div>
                <div class="text-sm text-slate-400 mb-1">Tổng Hội Thoại</div>
                <div class="text-3xl font-display font-bold text-[#00F0FF]">12,450</div>
                <div class="text-xs text-primary mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">trending_up</span> +15% so với tuần trước</div>
            </div>
            <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl relative overflow-hidden">
                <div class="absolute top-0 right-0 p-4 opacity-10"><span class="material-symbols-outlined text-6xl text-[#FFD700]">shopping_bag</span></div>
                <div class="text-sm text-slate-400 mb-1">Đơn Hàng Tự Động</div>
                <div class="text-3xl font-display font-bold text-[#FFD700]">842</div>
                <div class="text-xs text-primary mt-2 flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">trending_up</span> +8% so với tuần trước</div>
            </div>
            <div class="p-6 bg-[#121214] border border-[#10B981]/20 rounded-2xl relative overflow-hidden shadow-[0_0_20px_rgba(16,185,129,0.1)]">
                <div class="absolute top-0 right-0 w-32 h-32 bg-[#10B981]/20 rounded-full blur-[40px] -mr-10 -mt-10 pointer-events-none"></div>
                <div class="text-sm text-slate-400 mb-1">Claude AI Token Used</div>
                <div class="text-3xl font-display font-bold text-[#10B981]">1.2M</div>
                <div class="text-xs text-slate-400 mt-2">Chi phí dự kiến: $12.50</div>
            </div>
        </div>
        <div class="p-6 bg-[#121214] border border-white/5 rounded-2xl min-h-[400px]">
            <h2 class="text-lg font-bold mb-4">Biểu đồ Tương Tác & Chuyển Đổi</h2>
            <div class="flex items-center justify-center h-64 text-slate-500 border border-dashed border-white/10 rounded-xl bg-white/5">
                [Khu vực tích hợp Chart.js hiển thị Biểu đồ]
            </div>
        </div>
    '''),
    ('bot_builder.html', 'bot_builder', '''
        <div class="p-6 bg-[#121214] border border-[#7B2DFF]/20 rounded-2xl min-h-[500px] relative">
            <div class="absolute top-0 right-0 w-64 h-64 bg-[#7B2DFF]/10 rounded-full blur-[80px] pointer-events-none"></div>
            <h2 class="text-xl font-bold mb-2 flex items-center gap-2"><span class="material-symbols-outlined text-[#7B2DFF]">psychology</span> Cấu Hình Tính Cách Claude AI</h2>
            <p class="text-sm text-slate-400 mb-6">Nhập System Prompt để định hình cách bot tư vấn và chốt sale.</p>
            
            <textarea class="w-full h-64 bg-[#0A0A0A] border border-white/10 rounded-xl p-4 text-sm text-white focus:border-[#7B2DFF] focus:outline-none mb-4" placeholder="Bạn là một chuyên gia bán hàng..."></textarea>
            <button class="px-6 py-3 bg-gradient-to-r from-primary to-[#7B2DFF] rounded-xl font-bold text-sm flex items-center gap-2 hover:opacity-90 transition-opacity">
                <span class="material-symbols-outlined text-[18px]">save</span> Lưu Cấu Hình Bot
            </button>
        </div>
    '''),
    ('admin_panel.html', 'admin_panel', '''
        <div class="p-6 bg-[#121214] border border-[#FFD700]/20 rounded-2xl min-h-[500px] shadow-[0_0_30px_rgba(255,215,0,0.05)]">
            <div class="flex justify-between items-center mb-6">
                <div>
                    <h2 class="text-xl font-bold flex items-center gap-2"><span class="material-symbols-outlined text-[#FFD700]">corporate_fare</span> Quản Lý Tenants (Doanh Nghiệp)</h2>
                    <p class="text-sm text-slate-400 mt-1">Danh sách các doanh nghiệp đang sử dụng nền tảng CHỐT NGHÌN ĐƠN.</p>
                </div>
                <button class="px-4 py-2 bg-[#FFD700] text-[#0A0A0A] font-bold rounded-lg hover:bg-yellow-400 transition-colors">+ Tạo Tenant Mới</button>
            </div>
            
            <div class="overflow-x-auto">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="text-xs text-slate-500 uppercase bg-white/5 border-b border-white/5">
                        <tr>
                            <th class="px-4 py-3">Tên Doanh Nghiệp</th>
                            <th class="px-4 py-3">Chủ Sở Hữu</th>
                            <th class="px-4 py-3">Gói (Plan)</th>
                            <th class="px-4 py-3">Trạng Thái</th>
                            <th class="px-4 py-3 text-right">Hành Động</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                            <td class="px-4 py-3 font-bold text-white">Shop Thời Trang A</td>
                            <td class="px-4 py-3">shopA@gmail.com</td>
                            <td class="px-4 py-3"><span class="px-2 py-1 bg-[#FFD700]/20 text-[#FFD700] rounded text-xs font-bold">PRO</span></td>
                            <td class="px-4 py-3"><span class="px-2 py-1 bg-primary/20 text-primary rounded text-xs">Active</span></td>
                            <td class="px-4 py-3 text-right">
                                <button class="text-[#00F0FF] hover:underline text-xs font-bold">Quản lý</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    ''')
]

# Generate simple placeholders for the rest
OTHER_PAGES = ['broadcast', 'channels', 'ecommerce', 'crm', 'content', 'team_management', 'tenant_settings', 'affiliate', 'analytics', 'support']
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
    # Need to escape backticks if any, but since content has only double/single quotes, it's fine.
    # Actually wait, JS template literal uses backticks.
    # So we must use backticks in template, and escape any existing backticks or ${ in the content.
    escaped_content = content.replace("`", "\\`").replace("${", "\\${")
    final_html = TEMPLATE.replace('{CONTENT}', escaped_content).replace('{ID}', page_id)
    with open(html_file, 'w') as f:
        f.write(final_html)

print("Đã tạo và cập nhật toàn bộ 13 file HTML layout mới.")
