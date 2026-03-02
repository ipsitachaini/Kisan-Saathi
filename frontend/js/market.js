import { getApiHeaders } from './api.js';

export async function submitMarketIntelligence(event) {
    event.preventDefault();

    const submitBtn = document.querySelector('#market-form .action-btn');
    const originalText = submitBtn.innerText;
    submitBtn.innerText = 'Checking Prices...';
    submitBtn.disabled = true;

    try {
        const payload = {
            crop_name: document.getElementById('mkt-crop').value,
            quantity_quintals: parseFloat(document.getElementById('mkt-qty').value)
        };

        const response = await fetch('http://localhost:8000/api/v1/market-price', {
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

        document.getElementById('market-result').style.display = 'block';

        if (document.getElementById('res-mkt-local')) document.getElementById('res-mkt-local').innerText = data.data.local_mandi_price.toFixed(2);
        if (document.getElementById('res-mkt-dist')) document.getElementById('res-mkt-dist').innerText = data.data.district_market_price.toFixed(2);
        if (document.getElementById('res-mkt-state')) document.getElementById('res-mkt-state').innerText = data.data.state_market_price.toFixed(2);

        let trendKey = "valSteady";
        let demandTrendEl = document.getElementById('res-mkt-demand');
        if (demandTrendEl) demandTrendEl.style.color = "#d69e2e"; // fallback color for steady
        if (data.data.demand_trend === "high") {
            trendKey = "valHigh";
            if (demandTrendEl) demandTrendEl.style.color = "#2f855a";
        } else if (data.data.demand_trend === "low") {
            trendKey = "optLow";
            if (demandTrendEl) demandTrendEl.style.color = "#e53e3e";
        }

        if (demandTrendEl) demandTrendEl.innerText = window.i18n.translate(trendKey) || data.data.demand_trend;
        if (document.getElementById('res-mkt-total')) document.getElementById('res-mkt-total').innerText = data.data.total_estimated_value.toFixed(2);

        if (document.getElementById('mkt-advice-message')) document.getElementById('mkt-advice-message').innerText = data.message;
        if (document.getElementById('mkt-transport-advice')) document.getElementById('mkt-transport-advice').innerText = window.i18n.translate(data.data.transport_advice_key);

    } catch (error) {
        console.error('Market Price error:', error);
        alert(`Error: ${error.message}`);
    } finally {
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
    }
}
