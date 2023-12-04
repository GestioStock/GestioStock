
export function openTab(tabName) {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => link.classList.remove('active'));
  
    const tabContents = document.querySelectorAll('.tabcontent');
    tabContents.forEach(content => content.style.display = 'none');
  
    document.getElementById(tabName).classList.add('active');
    document.getElementById(`contenido${tabName.charAt(tabName.length - 1)}`).style.display = 'block';
  }