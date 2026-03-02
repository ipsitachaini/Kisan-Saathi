import { getApiHeaders } from './api.js';

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

        const response = await fetch('http://localhost:8000/api/v1/crop-recommendation', {
            method: 'POST',
            headers: getApiHeaders(),
            body: JSON.stringify(payload)
        });

        console.log("Response Status:", response.status);

        let bodyText = await response.text();
        console.log("Raw Response Body:", bodyText);

        if (!bodyText) {
            console.log("Response is completely empty!");
            throw new Error(`Empty response from backend. Status: ${response.status}`);
        }

        let data;
        try {
            data = JSON.parse(bodyText);
        } catch (e) {
            throw new Error(`Non-JSON response: ${bodyText.substring(0, 100)}`);
        }

        if (!response.ok) {
            let errorMsg = data.error || data.message || `HTTP error ${response.status}`;
            if (data.detail) errorMsg = typeof data.detail === 'string' ? data.detail : JSON.stringify(data.detail);
            throw new Error(errorMsg);
        }

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
