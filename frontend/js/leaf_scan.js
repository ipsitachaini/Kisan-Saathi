import { apiFetch } from './api.js';

export function setupLeafScan() {
    const imageInput = document.getElementById('leaf-image');

    imageInput.addEventListener('change', function (e) {
        const file = e.target.files[0];
        if (file) {
            // Show preview
            const reader = new FileReader();
            reader.onload = function (e) {
                const previewDiv = document.getElementById('image-preview');
                const imgEl = previewDiv.querySelector('img');
                const nameEl = document.getElementById('file-name-display');

                imgEl.src = e.target.result;
                nameEl.innerText = file.name;
                previewDiv.style.display = 'block';
            }
            reader.readAsDataURL(file);
        }
    });
}

export async function submitLeafScan(event) {
    event.preventDefault();

    const fileInput = document.getElementById('leaf-image');
    if (fileInput.files.length === 0) {
        alert('Please select an image first.');
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
        const result = await apiFetch('/leaf-scan/upload', {
            method: 'POST',
            body: formData
            // Note: apiFetch won't set Content-Type header when body is FormData
        });

        if (result) {
            renderScanResult(result);
        }
    } catch (error) {
        alert("Scan failed: " + error.message);
    }
}

function renderScanResult(result) {
    const resultBox = document.getElementById('scan-result');
    const diseaseName = document.getElementById('disease-name');
    const confPct = document.getElementById('confidence-pct');
    const confBar = document.getElementById('confidence-bar');

    diseaseName.innerText = result.disease_prediction;

    const percent = Math.round(result.confidence_score * 100);
    confPct.innerText = `${percent}%`;

    resultBox.style.display = 'block';

    // Animate bar
    setTimeout(() => {
        confBar.style.width = `${percent}%`;

        if (result.disease_prediction === "Healthy") {
            diseaseName.style.color = "var(--primary-color)";
            confBar.style.backgroundColor = "var(--primary-color)";
        } else {
            diseaseName.style.color = "#e53e3e";
            confBar.style.backgroundColor = "#e53e3e";
        }
    }, 100);
}
