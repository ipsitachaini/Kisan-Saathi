import { apiFetch } from './api.js';

export async function loadDashboard() {
    try {
        const summary = await apiFetch('/dashboard/summary');

        if (summary) {
            renderDashboard(summary);
        }
    } catch (error) {
        console.error('Failed to load dashboard', error);
        document.getElementById('weather-summary').innerHTML = '<span style="color:red">Failed to load data.</span>';
    }
}

function renderDashboard(data) {
    // Render Weather
    if (data.weather) {
        const weatherHtml = `
            <div style="font-size: 2rem; font-weight: bold; color: var(--text-color);">
                ${data.weather.temperature}°C
            </div>
            <div style="color: var(--text-light);">${data.weather.condition}</div>
            <div style="font-size: 0.85rem; margin-top: 0.5rem; color: var(--primary-color);">📍 ${data.weather.location}</div>
        `;
        document.getElementById('weather-summary').innerHTML = weatherHtml;
    }

    // Render Recent Activity
    const activityList = document.getElementById('activity-list');
    activityList.innerHTML = '';

    if (data.recent_activity && data.recent_activity.length > 0) {
        data.recent_activity.forEach(activity => {
            const date = new Date(activity.date).toLocaleDateString();
            const icon = activity.type === 'scan' ? '🍃' : '🌾';

            const li = document.createElement('li');
            li.innerHTML = `
                <div style="display: flex; gap: 0.5rem;">
                    <span>${icon}</span>
                    <div style="flex: 1;">
                        <div style="font-weight: 500;">${activity.summary}</div>
                        <div style="font-size: 0.75rem; color: var(--text-light);">${date}</div>
                    </div>
                </div>
            `;
            activityList.appendChild(li);
        });
    } else {
        activityList.innerHTML = '<li>No recent activity to show.</li>';
    }

    // Render Alerts if we had an alerts container
    if (data.active_alerts && data.active_alerts.length > 0) {
        console.log("Active alerts:", data.active_alerts);
    }
}
