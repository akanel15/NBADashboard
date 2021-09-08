lightTheme = "https://jenil.github.io/bulmaswatch/default/bulmaswatch.min.css";
darkTheme = "https://jenil.github.io/bulmaswatch/cyborg/bulmaswatch.min.css";

function changeTheme() {
    link = "";
    theme = "";
    
    if (document.getElementById("theme").href == lightTheme) { // change to dark theme
        link = darkTheme;
        theme = "dark";
    } else { // change to light theme
        link = lightTheme;
        theme = "light"
    }
    localStorage.setItem("theme", theme);
    document.getElementById("theme").href = link;
}

function initialiseTheme() {
    theme = localStorage.getItem("theme")
    link = ""

    if (theme == "dark") {
        link = darkTheme
    } else {
        link = lightTheme
    }


    document.getElementById("theme").href = link
}

initialiseTheme()


// Event listener for mobile navbar so that it is toggable
document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
  
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
  
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
  
          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
  
        });
      });
    }
  
  });