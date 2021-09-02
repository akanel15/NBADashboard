console.log("hi world");


function changeTheme() {
    resTheme = "";
    lightTheme = "https://unpkg.com/bulmaswatch/flatly/bulmaswatch.min.css";
    darkTheme = "https://unpkg.com/bulmaswatch/darkly/bulmaswatch.min.css";
    
    if (document.getElementById("theme").href == lightTheme) {
        resTheme = darkTheme;
    } else {
        resTheme = lightTheme;
    }

    document.getElementById("theme").href = resTheme;
}