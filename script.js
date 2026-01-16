// =========================
// MOBILE MENU TOGGLE
// =========================
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('mobile-active');
        mobileMenuToggle.classList.toggle('active');
    });
}

// =========================
// SMOOTH SCROLLING FOR ANCHOR LINKS
// =========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// =========================
// SCROLL ANIMATIONS
// =========================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
        }
    });
}, observerOptions);

// Observe all steps and cards
document.querySelectorAll('.step, .example-card, .pricing-card').forEach(el => {
    observer.observe(el);
});

// =========================
// NAVBAR SCROLL EFFECT
// =========================
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = 'none';
    }
    
    lastScroll = currentScroll;
});

// =========================
// STEP INTERACTIVE DEMO
// =========================
const modeOptions = document.querySelectorAll('.mode-option');
if (modeOptions.length > 0) {
    modeOptions.forEach(option => {
        option.addEventListener('click', () => {
            modeOptions.forEach(opt => opt.classList.remove('active'));
            option.classList.add('active');
        });
    });
}

// =========================
// PRICING CARD HOVER EFFECTS
// =========================
const pricingCards = document.querySelectorAll('.pricing-card');
pricingCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        pricingCards.forEach(c => {
            if (c !== this) {
                c.style.opacity = '0.7';
            }
        });
    });
    
    card.addEventListener('mouseleave', function() {
        pricingCards.forEach(c => {
            c.style.opacity = '1';
        });
    });
});

// =========================
// EXAMPLE CARDS CLICK HANDLER
// =========================
const exampleCards = document.querySelectorAll('.example-card');
exampleCards.forEach(card => {
    card.addEventListener('click', () => {
        // In a real app, this would open a video modal or navigate to video page
        console.log('Example video clicked');
    });
});

// =========================
// ADD FADE-IN ANIMATION CSS
// =========================
const style = document.createElement('style');
style.textContent = `
    .step, .example-card, .pricing-card {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    
    .step.fade-in, .example-card.fade-in, .pricing-card.fade-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    @media (max-width: 768px) {
        .nav-links.mobile-active {
            display: flex;
            flex-direction: column;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            padding: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border-top: 1px solid var(--border-color);
        }
        
        .mobile-menu-toggle.active span:nth-child(1) {
            transform: rotate(45deg) translate(5px, 5px);
        }
        
        .mobile-menu-toggle.active span:nth-child(2) {
            opacity: 0;
        }
        
        .mobile-menu-toggle.active span:nth-child(3) {
            transform: rotate(-45deg) translate(7px, -6px);
        }
    }
`;
document.head.appendChild(style);
