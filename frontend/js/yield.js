import { getApiHeaders } from './api.js';

// Ensure keyframes for spinner exist globally
if (!document.getElementById('spinner-style')) {
    const style = document.createElement('style');
    style.id = 'spinner-style';
    style.innerHTML = `@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }`;
    document.head.appendChild(style);
}

export async function submitYieldEstimation(event) {
    event.preventDefault();

    console.log("Starting Yield Estimation...");

    const submitBtn = document.querySelector('#yield-form .action-btn');
    const originalText = submitBtn.innerText;

    submitBtn.innerHTML = '<span class="spinner" style="display:inline-block; border: 2px solid #f3f3f3; border-radius: 50%; border-top: 2px solid #fff; width: 14px; height: 14px; animation: spin 1s linear infinite; margin-right: 5px; vertical-align: middle;"></span> <span style="vertical-align: middle;">Estimating...</span>';
    submitBtn.disabled = true;

    try {
        const payload = {
            crop_name: document.getElementById('yield-crop').value,
            land_size: parseFloat(document.getElementById('yield-land').value),
            soil_quality: document.getElementById('yield-soil').value,
            irrigation_availability: document.getElementById('yield-irrigation').value === 'true',
            rainfall_level: document.getElementById('yield-rainfall').value
        };

        console.log("Payload:", payload);

        const response = await fetch('http://localhost:8000/api/v1/yield/estimate', {
            method: 'POST',
            headers: getApiHeaders(),
            body: JSON.stringify(payload)
        });

        const resJson = await response.json();
        console.log("API Response:", resJson);

        if (!response.ok) {
            let errorMsg = `HTTP error! status: ${response.status}`;
            if (resJson.error) errorMsg = resJson.error;
            else if (resJson.detail) errorMsg = typeof resJson.detail === 'string' ? resJson.detail : JSON.stringify(resJson.detail);
            throw new Error(errorMsg);
        }

        if (resJson.status !== "success") {
            throw new Error(resJson.error || resJson.message || "Unknown error parsing response");
        }

        const data = resJson.data;

        const resultContainer = document.getElementById('yield-result');
        resultContainer.style.display = 'block';

        document.getElementById('res-yield').innerText = data.expected_yield.toFixed(2);
        document.getElementById('res-revenue').innerText = `₹${data.expected_revenue.toFixed(2)}`;

        // Render standard response string from the backend here
        document.getElementById('yield-advice-message').innerText = resJson.message;

        resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    } catch (error) {
        console.error('Yield Estimation error:', error);
        alert(`Error: ${error.message}`);
    } finally {
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
}
