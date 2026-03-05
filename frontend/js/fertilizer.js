import { getApiHeaders, apiFetch } from './api.js';

export async function submitFertilizerRecommendation(event) {
    event.preventDefault();

    const submitBtn = document.querySelector('#fertilizer-form .action-btn');
    const originalText = submitBtn.innerText;
    submitBtn.innerText = 'Analyzing...';
    submitBtn.disabled = true;

    try {
        const mode = document.getElementById('fert-mode').value;
        const landSize = parseFloat(document.getElementById('fert-land').value);

        let payload = {
            crop_type: document.getElementById('fert-crop').value,
            input_type: mode,
            land_size: landSize
        };

        if (mode === 'npk') {
            payload.n_value = parseFloat(document.getElementById('fert-n').value) || 0;
            payload.p_value = parseFloat(document.getElementById('fert-p').value) || 0;
            payload.k_value = parseFloat(document.getElementById('fert-k').value) || 0;
        } else {
            const checkboxes = document.querySelectorAll('#fert-checkboxes input[type="checkbox"]:checked');
            payload.symptoms = Array.from(checkboxes).map(cb => cb.value);

            if (payload.symptoms.length === 0) {
                alert("Please select at least one symptom.");
                return;
            }
        }

        const data = await apiFetch('/fertilizer-recommendation', {
            method: 'POST',
            body: JSON.stringify(payload)
        });

        if (data.status !== "success") {
            throw new Error(data.message || "Unknown error parsing response");
        }

        // Show results
        document.getElementById('fert-result').style.display = 'block';

        document.getElementById('res-fert-deficiency').innerText = data.data.deficiency_detected;
        document.getElementById('res-fert-name').innerText = data.data.fertilizer_name;
        document.getElementById('res-fert-qty').innerText = data.data.quantity_per_acre.toFixed(1);
        document.getElementById('res-fert-total').innerText = data.data.total_quantity.toFixed(1);

        // Replace dynamic string components using backend provided translation
        const adviceMessage = data.message;

        document.getElementById('fert-advice-message').innerText = adviceMessage;

    } catch (error) {
        console.error('Fertilizer Recommendation error:', error);
        alert(`Error: ${error.message}`);
    } finally {
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
}
