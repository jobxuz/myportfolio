// Language switcher UI functionality
export const initializeLanguageSwitcher = () => {
    document.querySelectorAll('.dropdown-content a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            document.querySelector('.dropbtn').textContent = e.target.textContent;
        });
    });
};