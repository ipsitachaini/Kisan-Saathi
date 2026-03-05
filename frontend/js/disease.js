import { getApiHeaders, apiFetch } from './api.js';

export async function submitDiseaseAdvisory(event) {
    event.preventDefault();

    const submitBtn = document.querySelector('#disease-form .action-btn');
    const originalText = submitBtn.innerText;
    submitBtn.innerText = 'Analyzing...';
    submitBtn.disabled = true;

    try {
        const checkboxes = document.querySelectorAll('#disease-checkboxes input[type="checkbox"]:checked');
        const symptoms = Array.from(checkboxes).map(cb => cb.value);

        if (symptoms.length === 0) {
            alert("Please select at least one symptom.");
            return;
        }

        const payload = {
            crop_type: document.getElementById('disease-crop').value,
            symptoms
        };

        const data = await apiFetch('/disease-advisory', {
            method: 'POST',
            body: JSON.stringify(payload)
        });

        if (data.status !== "success") {
            throw new Error(data.message || "Unknown error parsing response");
        }

        // Show results
        document.getElementById('disease-result').style.display = 'block';

        document.getElementById('res-dis-issue').innerText = data.data.possible_issue;
        document.getElementById('res-dis-treatment').innerText = data.data.treatment;
        document.getElementById('res-dis-prevention').innerText = data.data.prevention;
        document.getElementById('res-dis-cost').innerText = `₹${data.data.cost_estimate.toFixed(2)}`;

        // Replace dynamic string components
        const adviceMessage = data.message;
        document.getElementById('disease-advice-message').innerText = adviceMessage;

    } catch (error) {
        console.error('Disease Advisory error:', error);
        alert(`Error: ${error.message}`);
    } finally {
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
}
