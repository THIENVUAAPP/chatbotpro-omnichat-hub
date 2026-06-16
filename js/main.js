// Shared Premium UI Logic for ChatbotPro Omnichat Business Hub
document.addEventListener('DOMContentLoaded', () => {
    initCommonStyles();
    initLanguageSelector();
    initLeadCaptureModal();
    initToastSystem();
    initGlobalLinkHandlers();
});

// 1. Inject common cyber-glass styles dynamically to ensure consistency
function initCommonStyles() {
    const styleId = 'chatbotpro-common-styles';
    if (document.getElementById(styleId)) return;

    const styles = `
        /* Language Selector custom styles */
        .lang-active-indicator {
            background: linear-gradient(90deg, #cfbcff 0%, #e7c365 100%);
        }
        
        /* Lead modal animation & transitions */
        .modal-visible {
            opacity: 1 !important;
            pointer-events: auto !important;
        }
        .modal-scale {
            transform: scale(0.95);
            transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.3s ease;
        }
        .modal-visible .modal-scale {
            transform: scale(1) !important;
        }
        
        /* Toast Notification Styles */
        .luxury-toast {
            background: rgba(20, 18, 24, 0.85);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(207, 188, 255, 0.15);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 0 1px rgba(255, 255, 255, 0.05);
            transform: translateY(20px);
            opacity: 0;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .luxury-toast.toast-show {
            transform: translateY(0);
            opacity: 1;
        }
        .toast-progress-bar {
            height: 2px;
            background: linear-gradient(90deg, #cfbcff 0%, #e7c365 100%);
            width: 100%;
            transition: width linear;
        }
    `;

    const styleEl = document.createElement('style');
    styleEl.id = styleId;
    styleEl.innerHTML = styles;
    document.head.appendChild(styleEl);
}

// 2. Language Selector Implementation
const languages = [
    { name: 'English', code: 'ENG', native: 'English' },
    { name: 'Japanese', code: 'JPN', native: '日本語' },
    { name: 'Chinese', code: 'ZHO', native: '中文' },
    { name: 'French', code: 'FRA', native: 'Français' },
    { name: 'German', code: 'DEU', native: 'Deutsch' },
    { name: 'Vietnamese', code: 'VIE', native: 'Tiếng Việt' },
    { name: 'Spanish', code: 'SPA', native: 'Español' },
    { name: 'Italian', code: 'ITA', native: 'Italiano' },
    { name: 'Korean', code: 'KOR', native: '한국어' },
    { name: 'Russian', code: 'RUS', native: 'Русский' },
    { name: 'Portuguese', code: 'POR', native: 'Português' },
    { name: 'Arabic', code: 'ARA', native: 'العربية' },
    { name: 'Hindi', code: 'HIN', native: 'हिन्दी' },
    { name: 'Dutch', code: 'NLD', native: 'Nederlands' },
    { name: 'Swedish', code: 'SWE', native: 'Svenska' },
    { name: 'Polish', code: 'POL', native: 'Polski' },
    { name: 'Turkish', code: 'TUR', native: 'Türkçe' },
    { name: 'Danish', code: 'DAN', native: 'Dansk' },
    { name: 'Finnish', code: 'FIN', native: 'Suomi' },
    { name: 'Norwegian', code: 'NOR', native: 'Norsk' }
];

function initLanguageSelector() {
    // Check if selector element already exists
    if (document.getElementById('language-selector-overlay')) return;

    // Create Language Selector Overlay
    const overlay = document.createElement('div');
    overlay.id = 'language-selector-overlay';
    overlay.className = 'fixed inset-0 z-[100] flex items-center justify-center bg-[#050505]/90 backdrop-blur-2xl opacity-0 pointer-events-none transition-all duration-300';
    
    // Default selected language
    let activeLang = localStorage.getItem('chatbotpro_lang') || 'ENG';

    const overlayContent = `
        <div class="relative w-full max-w-4xl px-6 py-12 text-center modal-scale">
            <!-- Close Button -->
            <button id="close-lang-selector" class="absolute top-0 right-6 text-on-surface-variant hover:text-primary transition-colors group">
                <span class="material-symbols-outlined text-[32px] group-hover:rotate-90 transition-transform duration-300">close</span>
            </button>
            
            <h2 class="font-display-lg text-display-lg bg-gradient-to-r from-primary to-tertiary bg-clip-text text-transparent font-bold mb-4">Select Region & Language</h2>
            <p class="font-body-lg text-body-lg text-on-surface-variant mb-12 max-w-xl mx-auto">Choose your localized administrative layout and workspace language context.</p>
            
            <!-- Grid of Languages -->
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 text-left max-h-[50vh] overflow-y-auto pr-2">
                ${languages.map(lang => `
                    <div data-lang="${lang.code}" class="lang-card bg-surface-container/40 backdrop-blur-md border ${lang.code === activeLang ? 'border-primary' : 'border-outline-variant/20'} p-5 rounded-xl cursor-pointer hover:border-primary/50 relative overflow-hidden group transition-all duration-300 hover:-translate-y-0.5">
                        <div class="flex flex-col justify-between h-full">
                            <span class="font-mono-data text-mono-data text-xs text-outline group-hover:text-primary transition-colors">${lang.code}</span>
                            <span class="font-display-lg text-lg font-bold text-on-surface mt-2">${lang.native}</span>
                            <span class="text-xs text-on-surface-variant/70 mt-1">${lang.name}</span>
                        </div>
                        <div class="lang-indicator absolute bottom-0 left-0 right-0 h-[3px] bg-gradient-to-r from-primary to-tertiary transition-transform duration-300 ${lang.code === activeLang ? 'scale-x-100' : 'scale-x-0'} origin-left"></div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;

    overlay.innerHTML = overlayContent;
    document.body.appendChild(overlay);

    // Bind event listeners to open the selector
    document.body.addEventListener('click', (e) => {
        const langBtn = e.target.closest('[aria-label="language"]') || e.target.closest('.material-symbols-outlined')?.parentElement?.classList.contains('language') || (e.target.innerText === 'language' && e.target.classList.contains('material-symbols-outlined'));
        if (langBtn) {
            e.preventDefault();
            overlay.classList.add('modal-visible');
        }
    });

    // Close button
    document.getElementById('close-lang-selector').addEventListener('click', () => {
        overlay.classList.remove('modal-visible');
    });

    // Clicking language cards
    overlay.querySelectorAll('.lang-card').forEach(card => {
        card.addEventListener('click', () => {
            const selectedLang = card.getAttribute('data-lang');
            localStorage.setItem('chatbotpro_lang', selectedLang);
            
            // Update UI indicators
            overlay.querySelectorAll('.lang-card').forEach(c => {
                c.classList.remove('border-primary');
                c.classList.add('border-outline-variant/20');
                c.querySelector('.lang-indicator').classList.remove('scale-x-100');
                c.querySelector('.lang-indicator').classList.add('scale-x-0');
            });
            
            card.classList.add('border-primary');
            card.classList.remove('border-outline-variant/20');
            card.querySelector('.lang-indicator').classList.add('scale-x-100');
            card.querySelector('.lang-indicator').classList.remove('scale-x-0');

            setTimeout(() => {
                overlay.classList.remove('modal-visible');
                const selectedLangObj = languages.find(l => l.code === selectedLang);
                window.showToast(`System layout set to ${selectedLangObj.name} (${selectedLang})`, 'success');
            }, 200);
        });
    });

    // Close on clicking backdrop
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            overlay.classList.remove('modal-visible');
        }
    });
}

// 3. Lead Capture Modal Injection and Binding
function initLeadCaptureModal() {
    if (document.getElementById('lead-capture-modal')) return;

    const modal = document.createElement('div');
    modal.id = 'lead-capture-modal';
    modal.className = 'fixed inset-0 z-[90] flex items-center justify-center bg-[#050505]/80 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300';
    
    const modalContent = `
        <div class="relative w-full max-w-2xl px-4 md:px-0 mx-auto modal-scale">
            <div class="bg-surface/90 backdrop-blur-[40px] rounded-[24px] border border-outline-variant/30 shadow-[0_0_50px_rgba(207,188,255,0.15)] overflow-hidden">
                <!-- Close Button -->
                <button id="close-lead-modal" aria-label="Close dialog" class="absolute top-6 right-6 text-on-surface-variant hover:text-primary transition-colors z-20 group">
                    <span class="material-symbols-outlined text-[24px] group-hover:rotate-90 transition-transform duration-300">close</span>
                </button>
                <div class="flex flex-col md:flex-row">
                    <!-- Visual / Branding Area -->
                    <div class="md:w-5/12 bg-surface-container-low/50 p-8 flex flex-col justify-between border-b md:border-b-0 md:border-r border-outline-variant/20 relative overflow-hidden">
                        <div class="absolute -top-20 -left-20 w-40 h-40 bg-primary/20 blur-[50px] rounded-full"></div>
                        <div class="relative z-10">
                            <div class="flex items-center space-x-2 mb-8">
                                <span class="material-symbols-outlined text-primary text-[28px]">smart_toy</span>
                                <span class="font-display-lg text-body-lg font-bold tracking-tight text-white">ChatbotPro</span>
                            </div>
                            <div class="mt-8 space-y-6">
                                <div class="flex items-start space-x-3">
                                    <span class="material-symbols-outlined text-tertiary text-[20px] mt-1" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                                    <p class="font-body-sm text-body-sm text-on-surface-variant">Access to proprietary LLM sales scripts.</p>
                                </div>
                                <div class="flex items-start space-x-3">
                                    <span class="material-symbols-outlined text-tertiary text-[20px] mt-1" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                                    <p class="font-body-sm text-body-sm text-on-surface-variant">Advanced CRM blueprints.</p>
                                </div>
                                <div class="flex items-start space-x-3">
                                    <span class="material-symbols-outlined text-tertiary text-[20px] mt-1" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                                    <p class="font-body-sm text-body-sm text-on-surface-variant">Priority onboarding.</p>
                                </div>
                            </div>
                        </div>
                        <div class="mt-12 relative z-10">
                            <p class="font-mono-data text-mono-data text-on-surface-variant opacity-60 uppercase tracking-widest text-xs">Digital Luxury AI</p>
                        </div>
                    </div>
                    
                    <!-- Form Area -->
                    <div class="md:w-7/12 p-8 md:p-10 relative">
                        <div class="mb-6">
                            <h2 class="font-display-lg-mobile text-display-lg-mobile md:text-xl font-bold bg-gradient-to-r from-primary via-secondary to-tertiary bg-clip-text text-transparent mb-2">Unlock AI Sales.</h2>
                            <p class="font-body-sm text-body-sm text-on-surface-variant">Request your bespoke integration guide and join the elite automated tier.</p>
                        </div>
                        <form id="lead-capture-form" class="space-y-4">
                            <!-- Name Field -->
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-name">Full Name</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[18px]">person</span>
                                    </span>
                                    <input class="w-full bg-surface-container-highest border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-4 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors placeholder:text-outline/50" id="modal-name" required placeholder="Jane Doe" type="text"/>
                                </div>
                            </div>
                            <!-- Email Field -->
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-email">Enterprise Email</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant">
                                        <span class="material-symbols-outlined text-[18px]">mail</span>
                                    </span>
                                    <input class="w-full bg-surface-container-highest border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-4 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors placeholder:text-outline/50" id="modal-email" required placeholder="jane@company.com" type="email"/>
                                </div>
                            </div>
                            <!-- Business Type Dropdown -->
                            <div class="space-y-2">
                                <label class="font-label-caps text-label-caps text-on-surface block text-xs" for="modal-business">Business Type</label>
                                <div class="relative">
                                    <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-on-surface-variant z-10 pointer-events-none">
                                        <span class="material-symbols-outlined text-[18px]">domain</span>
                                    </span>
                                    <select class="w-full bg-surface-container-highest border border-outline-variant/30 text-on-surface font-mono-data text-mono-data rounded-lg pl-10 pr-10 py-2.5 focus:ring-0 focus:border-primary focus:outline-none transition-colors appearance-none cursor-pointer" id="modal-business" required>
                                        <option disabled selected value="">Select category...</option>
                                        <option value="finance">Financial Services</option>
                                        <option value="saas">Enterprise SaaS</option>
                                        <option value="ecommerce">High-Volume E-Commerce</option>
                                        <option value="other">Other / Consultancy</option>
                                    </select>
                                    <span class="absolute inset-y-0 right-0 flex items-center pr-3 text-on-surface-variant pointer-events-none">
                                        <span class="material-symbols-outlined text-[20px]">expand_more</span>
                                    </span>
                                </div>
                            </div>
                            <!-- Action Button -->
                            <div class="pt-2">
                                <button type="submit" class="w-full bg-gradient-to-r from-primary-container to-secondary-container hover:brightness-125 text-white font-label-caps text-label-caps py-3 px-6 rounded-lg transition-all shadow-[0_0_20px_rgba(207,188,255,0.1)] hover:shadow-[0_0_25px_rgba(207,188,255,0.3)] flex items-center justify-center space-x-2">
                                    <span>Get Elite Access</span>
                                    <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    `;

    modal.innerHTML = modalContent;
    document.body.appendChild(modal);

    // Bind event listeners to close buttons
    document.getElementById('close-lead-modal').addEventListener('click', () => {
        modal.classList.remove('modal-visible');
    });
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('modal-visible');
        }
    });

    // Form submission
    document.getElementById('lead-capture-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('modal-name').value;
        const email = document.getElementById('modal-email').value;
        
        modal.classList.remove('modal-visible');
        
        // Show success toast
        window.showToast(`Access requested for ${name} (${email}). Guide sent!`, 'success');
        
        // Clear fields
        document.getElementById('lead-capture-form').reset();
    });

    // Bind CTA click triggers
    document.body.addEventListener('click', (e) => {
        const ctaBtn = e.target.closest('.trigger-lead-capture') || 
                       (e.target.innerText === 'VIEW ARCHITECTURE' && e.target.classList.contains('border-tertiary')) ||
                       (e.target.innerText === 'CONTACT SALES' && e.target.classList.contains('border-tertiary/50'));
        if (ctaBtn) {
            e.preventDefault();
            modal.classList.add('modal-visible');
        }
    });
}

// 4. Premium Toast Notification System
function initToastSystem() {
    // Create toast container if not exists
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.className = 'fixed bottom-6 right-6 z-[120] flex flex-col gap-3 max-w-md w-full px-4 sm:px-0';
        document.body.appendChild(toastContainer);
    }

    // Expose showToast globally
    window.showToast = function(message, type = 'success', duration = 4000) {
        const toast = document.createElement('div');
        toast.className = 'luxury-toast rounded-xl overflow-hidden flex flex-col w-full';
        
        // Set accent colors based on type
        let borderClass = 'border-l-4 border-l-primary';
        let icon = 'check_circle';
        let iconColor = 'text-primary';
        
        if (type === 'success') {
            borderClass = 'border-l-4 border-l-[#10b981]'; // Emerald Success
            icon = 'verified';
            iconColor = 'text-[#10b981]';
        } else if (type === 'error') {
            borderClass = 'border-l-4 border-l-error';
            icon = 'error';
            iconColor = 'text-error';
        } else if (type === 'info') {
            borderClass = 'border-l-4 border-l-tertiary';
            icon = 'info';
            iconColor = 'text-tertiary';
        }

        toast.innerHTML = `
            <div class="flex items-center gap-4 px-5 py-4 ${borderClass}">
                <span class="material-symbols-outlined ${iconColor} text-[22px]">${icon}</span>
                <div class="flex-grow">
                    <p class="font-body-sm text-body-sm text-on-surface font-medium">${message}</p>
                </div>
                <button class="toast-close-btn text-on-surface-variant hover:text-on-surface transition-colors">
                    <span class="material-symbols-outlined text-[18px]">close</span>
                </button>
            </div>
            <div class="toast-progress-bar" style="width: 100%; transition-duration: ${duration}ms"></div>
        `;

        toastContainer.appendChild(toast);
        
        // Trigger reflow for slide/fade in animation
        toast.offsetHeight;
        toast.classList.add('toast-show');

        // Close button action
        toast.querySelector('.toast-close-btn').addEventListener('click', () => {
            toast.classList.remove('toast-show');
            setTimeout(() => toast.remove(), 400);
        });

        // Trigger progress bar countdown
        const progressBar = toast.querySelector('.toast-progress-bar');
        setTimeout(() => {
            if (progressBar) progressBar.style.width = '0%';
        }, 50);

        // Auto remove
        setTimeout(() => {
            if (toast.parentElement) {
                toast.classList.remove('toast-show');
                setTimeout(() => toast.remove(), 400);
            }
        }, duration);
    };
}

// 5. Global Link Handlers
function initGlobalLinkHandlers() {
    // Detect page context to bind specific events
    const currentPath = window.location.pathname;
    
    // Sidebar Active State Auto-matching
    const sidebarLinks = document.querySelectorAll('aside nav a, nav.desktop-nav a, nav.desktop-nav + nav a, .desktop-nav nav a');
    if (sidebarLinks.length > 0) {
        sidebarLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href || href === '#' || href.startsWith('#')) return;
            
            // Normalize path matching
            const isMatch = currentPath.includes(href) || 
                            (currentPath.endsWith('/') && href === 'index.html');
            
            if (isMatch) {
                // Remove active classes from siblings
                sidebarLinks.forEach(l => {
                    l.classList.remove('bg-primary-container/20', 'text-primary', 'border-r-2', 'border-primary', 'active');
                    l.classList.add('text-on-surface-variant');
                });
                
                // Add active classes to matched link
                link.classList.add('bg-primary-container/20', 'text-primary', 'border-r-2', 'border-primary', 'active');
                link.classList.remove('text-on-surface-variant');
            }
        });
    }

    // Bind custom login redirection
    const loginBtn = Array.from(document.querySelectorAll('button')).find(el => el.textContent.trim().includes('ENTERPRISE LOGIN'));
    if (loginBtn) {
        loginBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = 'dashboard.html';
        });
    }
}
