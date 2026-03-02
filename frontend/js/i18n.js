import { apiFetch } from './api.js';

class I18nManager {
    constructor(defaultLang = 'en') {
        this.currentLang = localStorage.getItem('ks_lang') || defaultLang;
        this.translations = {};
    }

    async init() {
        await this.loadTranslations(this.currentLang);
        this.updateUI();
    }

    async setLanguage(lang) {
        if (this.currentLang === lang && Object.keys(this.translations).length > 0) return;

        // Attempt to load new translations
        const success = await this.loadTranslations(lang);
        if (success) {
            this.currentLang = lang;
            localStorage.setItem('ks_lang', lang);
            this.updateUI();
            document.documentElement.lang = lang;

            // Attempt to save to backend if user is logged in
            const token = localStorage.getItem('kisan_saathi_token');
            if (token) {
                try {
                    await apiFetch('/users/me/language', {
                        method: 'PUT',
                        body: JSON.stringify({ language: lang })
                    });
                } catch (e) {
                    console.error("Failed to save language preference to DB", e);
                }
            }
        }
    }

    async loadTranslations(lang) {
        try {
            // In a real deployed environment, paths might need adjustment
            const response = await fetch(`locales/${lang}.json`);
            if (!response.ok) {
                throw new Error(`Could not load translations for ${lang}`);
            }
            this.translations = await response.json();
            return true;
        } catch (error) {
            console.error('Translation loading error:', error);
            // Fallback to English if loading fails
            if (lang !== 'en') {
                console.warn('Falling back to default language (English)');
                return await this.loadTranslations('en');
            }
            return false;
        }
    }

    translate(key) {
        return this.translations[key] || key;
    }

    updateUI() {
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            const translation = this.translate(key);
            if (translation !== key) {
                // If it's a placeholder attribute
                if (el.hasAttribute('placeholder')) {
                    el.setAttribute('placeholder', translation);
                } else {
                    el.innerHTML = translation;
                }
            }
        });
    }
}

// Ensure the module is available globally 
export const i18n = new I18nManager();
