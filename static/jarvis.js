let isLightMode = true;

function toggleLight() {
    const body = document.body;
    const button = document.getElementById('sun_moon');
    
    if (isLightMode) {
        // Switch to dark mode
        body.style.backgroundColor = "black";
        body.style.color = "white";
        button.textContent = "Dark";
        
        // Change nav and div colors for dark mode
        const nav = document.querySelector('nav');
        const links = nav.querySelectorAll('a');
        links.forEach(link => {
            link.style.color = "lightblue"; // Change link color
        });
    } else {
        // Switch to light mode
        body.style.backgroundColor = "white";
        body.style.color = "black";
        button.textContent = "Light";
        
        // Change nav and div colors for light mode
        const nav = document.querySelector('nav');
        nav.style.backgroundColor = "#fff"; // Light background for nav
        const links = nav.querySelectorAll('a');
        links.forEach(link => {
            link.style.color = "blue"; // Change link color
        });
    }
    
    isLightMode = !isLightMode; // Toggle mode
}
