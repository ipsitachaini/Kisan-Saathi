import { isAuthenticated, clearToken } from './api.js';
import { login, register } from './auth.js';
import { loadDashboard } from './dashboard.js';
import { submitPostHarvestAnalysis } from './post_harvest.js';
import { setupLeafScan, submitLeafScan } from './leaf_scan.js';
import { sendChatMessage } from './chatbot.js';
import { submitBudgetCalculation } from './budget.js';
import { submitYieldEstimation } from './yield.js';
import { submitFertilizerRecommendation } from './fertilizer.js';
import { submitDiseaseAdvisory } from './disease.js';
import { submitCropRecommendation } from './crop_recommend.js';
import { submitMarketIntelligence } from './market.js';

document.addEventListener('DOMContentLoaded', () => {
    console.log('Kisan Saathi initialized.');

    // Core Elements
    const loginContainer = document.getElementById('login-container');
    const dashboardContainer = document.getElementById('dashboard-container');
    const authForm = document.getElementById('auth-form');
    const toggleAuthMode = document.getElementById('toggle-auth-mode');

    // Nav Elements
    const navLinks = document.querySelectorAll('.main-nav a');

    // Feature Sections
    const postHarvestSection = document.getElementById('post-harvest-section');
    const leafScanSection = document.getElementById('leaf-scan-section');
    const chatbotSection = document.getElementById('chatbot-section');
    const budgetSection = document.getElementById('budget-section');
    const yieldSection = document.getElementById('yield-section');
    const fertilizerSection = document.getElementById('fertilizer-section');
    const diseaseSection = document.getElementById('disease-section');
    const cropRecommendSection = document.getElementById('crop-recommend-section');
    const marketPriceSection = document.getElementById('market-price-section');

    // Action Buttons
    const actionBtns = document.querySelectorAll('.action-btn');

    let isRegisterMode = false;

    // --- Routing & Display Logic ---
    function checkAuth() {
        if (isAuthenticated()) {
            loginContainer.style.display = 'none';
            dashboardContainer.style.display = 'block';
            updateNavForUser(true);
            loadDashboard();
        } else {
            loginContainer.style.display = 'block';
            dashboardContainer.style.display = 'none';
            hideAllFeatures();
            updateNavForUser(false);
        }
    }

    function updateNavForUser(loggedIn) {
        const navUl = document.querySelector('.main-nav ul');

        // Remove existing nav links except the language selector
        const items = Array.from(navUl.children);
        items.forEach(li => {
            if (!li.querySelector('#language-selector')) {
                li.remove();
            }
        });

        const langLi = navUl.querySelector('li:has(#language-selector)') || navUl.lastElementChild;

        if (loggedIn) {
            const dashLi = document.createElement('li');
            dashLi.innerHTML = `<a href="#dashboard" class="nav-link" data-i18n="navDashboard">${window.i18n.translate('navDashboard')}</a>`;

            const logoutLi = document.createElement('li');
            logoutLi.innerHTML = `<a href="#logout" id="logout-btn" data-i18n="navLogout">${window.i18n.translate('navLogout')}</a>`;

            navUl.insertBefore(dashLi, langLi);
            navUl.insertBefore(logoutLi, langLi);

            document.getElementById('logout-btn').addEventListener('click', (e) => {
                e.preventDefault();
                clearToken();
                checkAuth();
            });

            // Re-attach listeners to new links
            document.querySelectorAll('.nav-link').forEach(link => {
                link.addEventListener('click', handleNavigation);
            });
        } else {
            const loginLi = document.createElement('li');
            loginLi.innerHTML = `<a href="#login" class="nav-link" data-i18n="navLogin">${window.i18n.translate('navLogin')}</a>`;
            navUl.insertBefore(loginLi, langLi);
        }
    }

    function hideAllFeatures() {
        postHarvestSection.style.display = 'none';
        leafScanSection.style.display = 'none';
        chatbotSection.style.display = 'none';
        budgetSection.style.display = 'none';
        yieldSection.style.display = 'none';
        fertilizerSection.style.display = 'none';
        diseaseSection.style.display = 'none';
        cropRecommendSection.style.display = 'none';
        marketPriceSection.style.display = 'none';
    }

    function handleNavigation(e) {
        e.preventDefault();
        const target = e.target.getAttribute('href');

        if (target === '#dashboard' && isAuthenticated()) {
            hideAllFeatures();
            dashboardContainer.querySelector('.dashboard-grid').style.display = 'grid';
        }
    }

    // --- Authentication Events ---
    toggleAuthMode.addEventListener('click', (e) => {
        e.preventDefault();
        isRegisterMode = !isRegisterMode;

        const title = document.getElementById('auth-title');
        const submitBtn = document.getElementById('auth-submit');
        const nameGroup = document.getElementById('name-group');

        if (isRegisterMode) {
            title.innerText = window.i18n.translate('authRegisterTitle');
            submitBtn.innerText = window.i18n.translate('btnRegister');
            nameGroup.style.display = 'block';
            toggleAuthMode.innerText = window.i18n.translate('linkHaveAccount');
        } else {
            title.innerText = window.i18n.translate('authLoginTitle');
            submitBtn.innerText = window.i18n.translate('btnLogin');
            nameGroup.style.display = 'none';
            toggleAuthMode.innerText = window.i18n.translate('linkNeedAccount');
        }
    });

    authForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('auth-email').value;
        const password = document.getElementById('auth-password').value;
        const name = document.getElementById('auth-name').value;

        let success = false;

        if (isRegisterMode) {
            success = await register(name, email, password);
        } else {
            success = await login(email, password);
        }

        if (success) {
            authForm.reset();
            checkAuth();
        }
    });

    // --- Feature Events ---

    // Quick Actions routing
    // Better routing logic by targeting specific data attributes rather than raw array indices
    document.querySelectorAll('[data-target]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const targetId = e.target.getAttribute('data-target');
            if (targetId) {
                hideAllFeatures();
                document.querySelector('.dashboard-grid').style.display = 'none';
                const targetSection = document.getElementById(targetId);
                if (targetSection) {
                    targetSection.style.display = 'block';
                    // Scroll into view
                    targetSection.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // Wiring up the forms to the imported modules
    document.getElementById('post-harvest-form').addEventListener('submit', submitPostHarvestAnalysis);
    document.getElementById('budget-form').addEventListener('submit', submitBudgetCalculation);
    document.getElementById('yield-form').addEventListener('submit', submitYieldEstimation);
    document.getElementById('fertilizer-form').addEventListener('submit', submitFertilizerRecommendation);
    document.getElementById('disease-form').addEventListener('submit', submitDiseaseAdvisory);
    document.getElementById('crop-recommend-form').addEventListener('submit', submitCropRecommendation);
    document.getElementById('market-form').addEventListener('submit', submitMarketIntelligence);

    setupLeafScan();
    document.getElementById('leaf-scan-form').addEventListener('submit', submitLeafScan);

    document.getElementById('chat-form').addEventListener('submit', sendChatMessage);

    // --- Language Selector Events ---
    const langSelector = document.getElementById('language-selector');
    if (langSelector) {
        // Set initial value based on localStorage
        const savedLang = localStorage.getItem('ks_lang') || 'en';
        langSelector.value = savedLang;

        langSelector.addEventListener('change', async (e) => {
            const newLang = e.target.value;
            await window.i18n.setLanguage(newLang);
            updateNavForUser(isAuthenticated()); // Refresh nav text
            populateCropDropdowns(); // Re-populate with new language if needed
        });
    }

    // --- Crop Dropdown Population ---
    async function populateCropDropdowns() {
        try {
            const response = await fetch('/crops.config.json');
            if (!response.ok) throw new Error('Failed to load crop config');
            const crops = await response.json();

            // Group crops by category
            const groupedCrops = {};
            crops.forEach(crop => {
                if (!groupedCrops[crop.category]) {
                    groupedCrops[crop.category] = [];
                }
                groupedCrops[crop.category].push(crop);
            });

            // Get all dropdowns
            const cropSelects = document.querySelectorAll('.crop-select');

            cropSelects.forEach(select => {
                // Clear existing options
                select.innerHTML = '<option value="" disabled selected>Search & Select Crop</option>';

                // Create optgroups for each category
                for (const [category, categoryCrops] of Object.entries(groupedCrops)) {
                    const optgroup = document.createElement('optgroup');
                    optgroup.label = parseCategoryName(category);

                    categoryCrops.forEach(crop => {
                        const option = document.createElement('option');
                        option.value = crop.id;
                        // Use translation if available, otherwise fallback to the name in config
                        // We will add data-i18n attributes for dynamic translation
                        option.setAttribute('data-i18n', `crop_${crop.id}`);
                        option.textContent = window.i18n.translate(`crop_${crop.id}`) === `crop_${crop.id}`
                            ? crop.name
                            : window.i18n.translate(`crop_${crop.id}`);
                        optgroup.appendChild(option);
                    });

                    select.appendChild(optgroup);
                }
            });
        } catch (error) {
            console.error('Error populating crop dropdowns:', error);
        }
    }

    function parseCategoryName(cat) {
        return cat.charAt(0).toUpperCase() + cat.slice(1);
    }

    // Initialize translations and layout
    window.i18n.init().then(() => {
        populateCropDropdowns();
        checkAuth();
    });
});
