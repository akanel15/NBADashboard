lightTheme = "https://unpkg.com/bulmaswatch/flatly/bulmaswatch.min.css";
darkTheme = "https://unpkg.com/bulmaswatch/darkly/bulmaswatch.min.css";

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

    if (theme == "light") {
        link = lightTheme
    }
    else if (theme == "dark") {
        link = darkTheme
    }

    document.getElementById("theme").href = link
}

initialiseTheme()
