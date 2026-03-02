import { apiFetch, setToken } from './api.js';

export async function login(email, password) {
    try {
        const formData = new FormData();
        formData.append('username', email); // OAuth2 expects 'username'
        formData.append('password', password);

        const response = await apiFetch('/auth/login', {
            method: 'POST',
            body: formData
        });

        if (response && response.access_token) {
            setToken(response.access_token);
            return true;
        }
        return false;
    } catch (error) {
        alert(error.message || 'Login failed.');
        return false;
    }
}

export async function register(fullName, email, password) {
    try {
        const response = await apiFetch('/auth/register', {
            method: 'POST',
            body: JSON.stringify({
                email: email,
                full_name: fullName,
                password: password
            })
        });

        if (response && response.id) {
            // Auto login after successful registration
            return await login(email, password);
        }
        return false;
    } catch (error) {
        alert(error.message || 'Registration failed.');
        return false;
    }
}
