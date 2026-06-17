// ROI Projection Calculator Logic (Calibrated for Vietnam Market - VND)
document.addEventListener('DOMContentLoaded', () => {
    const sliderTickets = document.getElementById('slider-tickets');
    const sliderCost = document.getElementById('slider-cost');
    const sliderDeflection = document.getElementById('slider-deflection');

    const valTickets = document.getElementById('val-tickets');
    const valCost = document.getElementById('val-cost');
    const valDeflection = document.getElementById('val-deflection');

    const roiSavings = document.getElementById('roi-savings');
    const roiAnnual = document.getElementById('roi-annual');

    if (!sliderTickets || !sliderCost || !sliderDeflection) return;

    function calculateROI() {
        const tickets = parseInt(sliderTickets.value, 10);
        const cost = parseFloat(sliderCost.value);
        const deflection = parseInt(sliderDeflection.value, 10) / 100;
        const currentLang = localStorage.getItem('chatbotpro_lang') || 'VIE';

        // Update slider labels in real-time
        if (valTickets) valTickets.textContent = tickets.toLocaleString();
        
        // Cost per ticket format
        if (valCost) {
            valCost.textContent = currentLang === 'VIE' 
                ? `${cost.toLocaleString()} VND` 
                : `${cost.toLocaleString()} VND`;
        }
        
        if (valDeflection) valDeflection.textContent = `${Math.round(deflection * 100)}%`;

        // Calculate Projected Monthly Savings
        // Savings = Tickets * Cost * DeflectionRate
        const monthlySavings = tickets * cost * deflection;
        if (roiSavings) {
            roiSavings.textContent = `${Math.round(monthlySavings).toLocaleString()} VND`;
        }

        // Annual ROI calculation based on Standard Plan (1.100.000 VND/mo)
        // Yearly fee: 13,200,000 VND.
        // ROI = (Annual Savings - Annual License) / Annual License * 100
        const annualLicense = 1100000 * 12;
        const annualSavings = monthlySavings * 12;
        const roiPercentage = ((annualSavings - annualLicense) / annualLicense) * 100;
        
        if (roiAnnual) {
            const labelText = currentLang === 'VIE' ? 'Tỷ suất ROI Hàng Năm' : 'Annual ROI';
            roiAnnual.innerHTML = `
                <span class="material-symbols-outlined text-sm">trending_up</span>
                ${Math.max(0, Math.round(roiPercentage)).toLocaleString()}% ${labelText}
            `;
        }
    }

    sliderTickets.addEventListener('input', calculateROI);
    sliderCost.addEventListener('input', calculateROI);
    sliderDeflection.addEventListener('input', calculateROI);

    // Listen for global language changes to refresh formatting
    document.addEventListener('langChanged', calculateROI);

    // Initial calculation
    calculateROI();
});
