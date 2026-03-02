import { apiFetch } from './api.js';

export async function sendChatMessage(event) {
    event.preventDefault();

    const inputEl = document.getElementById('chat-input');
    const message = inputEl.value.trim();

    if (!message) return;

    // Clear input
    inputEl.value = '';

    // Add user message to UI
    appendMessage(message, false);

    try {
        // Fetch from API
        const response = await apiFetch('/chatbot/chat', {
            method: 'POST',
            body: JSON.stringify({ message: message })
        });

        if (response && response.message_text) {
            appendMessage(response.message_text, true);
        }
    } catch (error) {
        appendMessage(window.i18n ? window.i18n.translate('chatError') : "Sorry, I am having trouble connecting to the server.", true);
    }
}

function appendMessage(text, isBot) {
    const history = document.getElementById('chat-history');

    const msgDiv = document.createElement('div');
    msgDiv.className = `chat-message ${isBot ? 'bot-message' : 'user-message'}`;

    const avatar = isBot ? '🤖' : '👤';

    msgDiv.innerHTML = `
        <div class="msg-avatar">${avatar}</div>
        <div class="msg-content">${text}</div>
    `;

    history.appendChild(msgDiv);

    // Scroll to bottom
    history.scrollTop = history.scrollHeight;
}
