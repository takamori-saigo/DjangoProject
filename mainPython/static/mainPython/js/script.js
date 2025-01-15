document.querySelector('.button').addEventListener('click', () => {
  const navContainer = document.getElementById('nav-container');
  if (document.activeElement === navContainer) {
    navContainer.blur(); // Скрыть меню
  } else {
    navContainer.focus(); // Показать меню
  }
});