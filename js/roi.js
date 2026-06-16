// ROI Projection Calculator Logic
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

        // Update slider values labels in real-time
        if (valTickets) valTickets.textContent = tickets.toLocaleString();
        if (valCost) valCost.textContent = `$${cost.toFixed(2)}`;
        if (valDeflection) valDeflection.textContent = `${Math.round(deflection * 100)}%`;

        // Calculate Projected Monthly Savings
        // Savings = Tickets * Cost * DeflectionRate
        const monthlySavings = tickets * cost * deflection;
        if (roiSavings) {
            roiSavings.textContent = `$${Math.round(monthlySavings).toLocaleString()}`;
        }

        // Annual ROI calculation
        // Pro License: $149/mo. Yearly fee: $1,788.
        // ROI = (Annual Savings - Annual License) / Annual License * 100
        const annualLicense = 149 * 12;
        const annualSavings = monthlySavings * 12;
        const roiPercentage = ((annualSavings - annualLicense) / annualLicense) * 100;
        
        if (roiAnnual) {
            roiAnnual.textContent = `${Math.max(0, Math.round(roiPercentage)).toLocaleString()}% Annual ROI`;
        }
    }

    sliderTickets.addEventListener('input', calculateROI);
    sliderCost.addEventListener('input', calculateROI);
    sliderDeflection.addEventListener('input', calculateROI);

    // Initial calculation
    calculateROI();
});
