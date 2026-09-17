// TOGGLE DARK / LIGHT THEME
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Cek preferensi tema tersimpan
if (localStorage.getItem('devTheme') === 'dark') {
  body.classList.add('dark-mode');
  themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
}

themeToggle.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  const isDark = body.classList.contains('dark-mode');
  
  themeToggle.innerHTML = isDark 
    ? '<i class="fa-solid fa-sun"></i>' 
    : '<i class="fa-solid fa-moon"></i>';
    
  localStorage.setItem('devTheme', isDark ? 'dark' : 'light');
});

// LOGIKA TAMBAHAN PRAKTIKUM GIT (Untuk Latihan Branching Feature)
console.log('ITSENJA Sprint 05: Repositori latihan praktikum Git aktif.');
