import { getApiHeaders } from './api.js';

export async function submitPostHarvestAnalysis(event) {
    event.preventDefault();

    const submitBtn = document.querySelector('#post-harvest-form .action-btn');
    const originalText = submitBtn.innerText;
    submitBtn.innerText = 'Analyzing Storage...';
    submitBtn.disabled = true;

    try {
        const payload = {
            crop_type: document.getElementById('crop-type').value,
            temperature: parseFloat(document.getElementById('temperature').value),
            humidity: parseFloat(document.getElementById('humidity').value),
            storage_duration: parseInt(document.getElementById('duration').value, 10),
            storage_method: document.getElementById('method').value,
            location: "Kisan Farm"
        };

        const response = await fetch('http://localhost:8000/api/v1/post-harvest', {
            method: 'POST',
            headers: getApiHeaders(),
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const prediction = await response.json();

        if (!response.ok) {
            let errorMsg = `HTTP error! status: ${response.status}`;
            if (prediction.detail) errorMsg = typeof prediction.detail === 'string' ? prediction.detail : JSON.stringify(prediction.detail);
            throw new Error(prediction.message || errorMsg);
        }
        if (prediction.status !== "success") {
            throw new Error(prediction.message || "Unknown error");
        }

        renderPredictionResult(prediction);

    } catch (error) {
        console.error('Post Harvest error:', error);
        alert(`Error: ${error.message}`);
    } finally {
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
}

function renderPredictionResult(prediction) {
    const resultBox = document.getElementById('prediction-result');
    const riskScoreEl = document.getElementById('risk-score');
    const lossPctEl = document.getElementById('loss-pct');
    const sellSuggEl = document.getElementById('sell-suggestion');
    const storageAdvEl = document.getElementById('storage-advice');

    // Format risk score as percentage for UI
    const riskPercent = Math.round(prediction.data.spoilage_risk_score * 100);
    riskScoreEl.innerText = `${riskPercent}%`;
    lossPctEl.innerText = `${prediction.data.loss_percentage.toFixed(1)}%`;

    // Extract pre-translated values dynamically
    sellSuggEl.innerText = prediction.data.sell_suggestion;
    storageAdvEl.innerText = prediction.data.storage_advice;

    // Color coding based on risk
    if (riskPercent < 30) {
        riskScoreEl.style.color = '#2f855a'; // green
    } else if (riskPercent < 60) {
        riskScoreEl.style.color = '#dd6b20'; // orange
    } else {
        riskScoreEl.style.color = '#e53e3e'; // red
    }

    resultBox.style.display = 'block';
}
