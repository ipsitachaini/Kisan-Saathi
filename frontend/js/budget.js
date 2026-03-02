import { getApiHeaders } from './api.js';

// Ensure keyframes for spinner exist globally
if (!document.getElementById('spinner-style')) {
    const style = document.createElement('style');
    style.id = 'spinner-style';
    style.innerHTML = `@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }`;
    document.head.appendChild(style);
}

export async function submitBudgetCalculation(event) {
    event.preventDefault();
    console.log("Starting Budget Calculation...");

    const submitBtn = document.querySelector('#budget-form .action-btn');
    const originalText = submitBtn.innerText;
    submitBtn.innerHTML = '<span class="spinner" style="display:inline-block; border: 2px solid #f3f3f3; border-radius: 50%; border-top: 2px solid #fff; width: 14px; height: 14px; animation: spin 1s linear infinite; margin-right: 5px; vertical-align: middle;"></span> <span style="vertical-align: middle;">Calculating...</span>';
    submitBtn.disabled = true;

    try {
        const payload = {
            total_budget: parseFloat(document.getElementById('budget-total').value),
            land_size: parseFloat(document.getElementById('budget-land').value),
            crop: document.getElementById('budget-crop').value
        };

        const response = await fetch('http://localhost:8000/api/v1/budget/calculate', {
            method: 'POST',
            headers: getApiHeaders(),
            body: JSON.stringify(payload)
        });

        const resJson = await response.json();

        if (!response.ok) {
            let errorMsg = `HTTP error! status: ${response.status}`;
            if (resJson.error) errorMsg = resJson.error;
            else if (resJson.detail) errorMsg = typeof resJson.detail === 'string' ? resJson.detail : JSON.stringify(resJson.detail);
            throw new Error(errorMsg);
        }

        if (resJson.status !== "success") {
            throw new Error(resJson.error || resJson.message || "Unknown error...");
        }

        const data = resJson.data;

        // Show results
        const resultContainer = document.getElementById('budget-result');
        resultContainer.style.display = 'block';

        // Format money to ₹
        const fmt = (val) => `₹${val.toFixed(2)}`;

        document.getElementById('res-labour').innerText = fmt(data.labour_cost);
        document.getElementById('res-machine').innerText = fmt(data.machine_cost);
        document.getElementById('res-diesel').innerText = fmt(data.diesel_cost);
        document.getElementById('res-seed').innerText = fmt(data.seed_cost);
        document.getElementById('res-fertilizer').innerText = fmt(data.fertilizer_cost);
        document.getElementById('res-pesticide').innerText = fmt(data.pesticide_cost);

        // Use translated response from backend
        const adviceMessage = resJson.message;

        const adviceBox = document.getElementById('budget-advice-message');
        adviceBox.innerText = adviceMessage;

        if (data.is_sufficient) {
            adviceBox.style.color = '#276749'; // Green positive
        } else {
            adviceBox.style.color = '#9b2c2c'; // Red negative
        }

        resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    } catch (error) {
        console.error('Budget Calculation error:', error);
        alert(`Error: ${error.message}`);
    } finally {
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
}
