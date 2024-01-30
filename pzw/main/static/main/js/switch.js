// Function to toggle themes
function toggleTheme() {
    document.body.classList.toggle('theme1');
    document.body.classList.toggle('theme2');

    // Stores the selected theme in localStorage
    const currentTheme = document.body.classList.contains('theme1') ? 'theme1' : 'theme2';
    localStorage.setItem('selectedTheme', currentTheme);
}

// Event listener for the colorSwitchButton
document.getElementById('colorSwitchButton').addEventListener('click', toggleTheme);

// Checks for a previously selected theme in localStorage and applies it
const savedTheme = localStorage.getItem('selectedTheme');
if (savedTheme) {
    document.body.classList.add(savedTheme);
}
