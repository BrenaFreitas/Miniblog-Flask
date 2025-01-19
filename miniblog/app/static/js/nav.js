document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('.collapsible').addEventListener('click', function() {
    const content = document.querySelector('.content');
    const body = document.body;

    if (content.style.display === 'block') {
      content.style.display = 'none';
    } else {
      content.style.display = 'block';
      body.classList.toggle('nav-active');
    }
  });
});
