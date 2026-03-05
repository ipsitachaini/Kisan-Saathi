import { getApiHeaders, apiFetch } from './api.js';

export async function submitCropRecommendation(event) {
    event.preventDefault();

    const submitBtn = document.querySelector('#crop-recommend-form .action-btn');
    const originalText = submitBtn.innerText;
    submitBtn.innerText = 'Finding Crops...';
    submitBtn.disabled = true;

    try {
        const payload = {
            land_size: parseFloat(document.getElementById('cr-land').value),
            soil_type: document.getElementById('cr-soil').value,
            season: document.getElementById('cr-season').value,
            water_availability: document.getElementById('cr-water').value
        };

        const data = await apiFetch('/crop-recommendation', {
            method: 'POST',
            body: JSON.stringify(payload)
        });

        if (data.status !== "success") {
            throw new Error(data.error || data.message || "Unknown error parsing response");
        }

        // Show results container
        document.getElementById('crop-recommend-result').style.display = 'block';

        // Test logic
        document.getElementById('cr-advice-main').innerText = data.message;
        const container = document.getElementById('cr-predictions-container');
        container.innerHTML = `<h3>Testing crops: ${data.data.recommended_crops.join(', ')}</h3>`;

    } catch (error) {
        console.error('Crop Recommendation error:', error);
        alert(error.message);
    } finally {
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
}
