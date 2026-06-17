// Enhanced Role Access for Omnichannel Dashboard
document.addEventListener('DOMContentLoaded', () => {
    const currentRole = localStorage.getItem('chatbotpro_role') || 'owner';
    
    // Specifically for dashboard.html
    if (window.location.pathname.includes('dashboard.html')) {
        const omnichannelBar = document.getElementById('omnichannel-bar');
        if (omnichannelBar) {
            const addPlatformBtn = omnichannelBar.querySelector('button');
            if (currentRole === 'staff') {
                // If User/Staff, they cannot add new platforms
                if(addPlatformBtn) addPlatformBtn.style.display = 'none';
                
                // Maybe hide some platforms that are not assigned to them? (Mock logic: hide Lazada and IG for staff)
                const platforms = omnichannelBar.querySelectorAll('div.flex.items-center.gap-3');
                if (platforms.length > 7) {
                    platforms[6].style.display = 'none'; // Hide Lazada
                    platforms[7].style.display = 'none'; // Hide IG
                }
            } else {
                if(addPlatformBtn) addPlatformBtn.style.display = 'flex';
            }
        }
    }
});

// UI logic for toggling AI switch visually in the horizontal bar
document.addEventListener('click', (e) => {
    if (e.target.closest('#omnichannel-bar label')) {
        const label = e.target.closest('#omnichannel-bar label');
        const span = label.querySelector('span');
        const input = label.querySelector('input');
        
        // Wait for next tick to let the checkbox state update naturally
        setTimeout(() => {
            if (input.checked) {
                span.textContent = 'AI ON';
                span.className = 'ml-1.5 text-[9px] font-bold text-primary uppercase';
            } else {
                span.textContent = 'AI OFF';
                span.className = 'ml-1.5 text-[9px] font-bold text-slate-400 uppercase';
            }
            window.showToast(input.checked ? 'Đã bật AI Tự Động' : 'Đã tắt AI', 'success');
        }, 10);
    }
});
