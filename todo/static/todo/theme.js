(function initTheme() {
  const link = document.getElementById('theme-css');
  link.href = '/static/todo/bs/css/bootstrap.min.css';
  document.documentElement.style.setProperty('--theme-primary', '#1a1a2e');
  document.documentElement.style.setProperty('--theme-bg', '#0f0f1a');
  document.documentElement.classList.add('custom-theme');
})();
