// Add smooth transitions for hover effects
document.querySelectorAll('.social-icon, .nav-items a, .skill-tag').forEach(element => {
    element.style.transition = 'all 0.3s ease';
});

// Add hover effect to skill tags
document.querySelectorAll('.skill-tag').forEach(tag => {
    tag.addEventListener('mouseenter', () => {
        tag.style.transform = 'translateY(-2px)';
        tag.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
    });

    tag.addEventListener('mouseleave', () => {
        tag.style.transform = 'translateY(0)';
        tag.style.boxShadow = 'none';
    });
});

// Language switcher functionality
document.querySelectorAll('.dropdown-content a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const language = e.target.dataset.lang;
        document.querySelector('.dropbtn').textContent = e.target.textContent;
        // Here you can add logic to change the language
    });
});


// ----------------------------
let navItem = document.getElementById("navItem");
let navIcon = document.getElementById("navIcon");

navIcon.addEventListener("click", function () {
  navItem.classList.toggle("show"); 
});
// -----------------------------