import { initializeAnimations } from './animations.js';
import { initializeLanguageSwitcher } from './language-switcher.js';

// Initialize all UI enhancements
document.addEventListener('DOMContentLoaded', () => {
    initializeAnimations();
    initializeLanguageSwitcher();
});