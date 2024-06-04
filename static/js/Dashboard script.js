const body = document.querySelector("body"),
  sidebar = body.querySelector("nav"),
  toggle = body.querySelector(".toggle"),
  searchBtn = body.querySelector(".search-box"),
  modeSwitch = body.querySelector(".toggle-switch"),
  modeText = body.querySelector(".mode-text");

toggle.addEventListener("click", () => {
  sidebar.classList.toggle("close");
});

document.addEventListener('DOMContentLoaded', function() {
  const userDropdown = document.getElementById('userDropdown');
  const userDropdownMenu = document.querySelector('.userdb1');
  const contentDropdown = document.getElementById('contentDropdown');
  const contentDropdownMenu = document.querySelector('.contentDropdownMenu');

  userDropdown.addEventListener('click', function(event) {
    event.preventDefault();
    userDropdownMenu.classList.toggle('show');
    userDropdown.classList.toggle('active');
  });

  // Close the dropdown when clicking outside of it
  document.addEventListener('click', function(event) {
    if (!userDropdown.contains(event.target) && !userDropdownMenu.contains(event.target)) {
      userDropdownMenu.classList.remove('show');
      userDropdown.classList.remove('active');
    }
  });

  contentDropdown.addEventListener('click', function(event) {
    event.preventDefault();
    contentDropdownMenu.classList.toggle('show');
    contentDropdown.classList.toggle('active');
  });

  // Close the dropdown when clicking outside of it
  document.addEventListener('click', function(event) {
    if (!contentDropdown.contains(event.target) && !contentDropdownMenu.contains(event.target)) {
      contentDropdownMenu.classList.remove('show');
      contentDropdown.classList.remove('active')
    }
  });

});




