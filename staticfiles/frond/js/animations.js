// UI animations and transitions
export const initializeAnimations = () => {
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
};