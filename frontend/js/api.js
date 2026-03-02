// API configuration
const API_BASE_URL = 'http://localhost:8000/api/v1';

// Helper function to get the JWT token
export function getToken() {
    return localStorage.getItem('kisan_saathi_token');
}

// Helper function to set the JWT token
export function setToken(token) {
    localStorage.setItem('kisan_saathi_token', token);
}

// Helper function to remove the JWT token
export function clearToken() {
    localStorage.removeItem('kisan_saathi_token');
}

// Check if user is logged in
export function isAuthenticated() {
    return !!getToken();
}

// Helper function to get standardized API headers
export function getApiHeaders() {
    const headers = {
        'Content-Type': 'application/json',
        'Accept-Language': localStorage.getItem('ks_lang') || 'en'
    };
    const token = getToken();
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
}

// Generic fetch wrapper with auth token injection
export async function apiFetch(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;

    // Set default headers
    const headers = {
        ...(options.headers || {})
    };

    // Only set Content-Type to application/json if not explicitly provided and not sending FormData
    if (!headers['Content-Type'] && !(options.body instanceof FormData)) {
        headers['Content-Type'] = 'application/json';
    }

    // Add authorization token if available
    const token = getToken();
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    const fetchOptions = {
        ...options,
        headers
    };

    try {
        const response = await fetch(url, fetchOptions);

        // Handle 401 Unauthorized globally (e.g., token expired)
        if (response.status === 401) {
            clearToken();
            window.location.hash = '#login';
            window.location.reload();
            return null;
        }

        const data = await response.json();

        if (!response.ok) {
            let errorMsg = 'An API error occurred';
            if (data.detail) {
                if (Array.isArray(data.detail)) {
                    // FastAPI validation error array parsing
                    errorMsg = data.detail.map(e => `${e.loc.join('.')}: ${e.msg}`).join('\n');
                } else if (typeof data.detail === 'string') {
                    errorMsg = data.detail;
                } else {
                    errorMsg = JSON.stringify(data.detail);
                }
            }
            throw new Error(errorMsg);
        }

        return data;
    } catch (error) {
        console.error(`API Error on ${endpoint}:`, error);
        throw error;
    }
}
