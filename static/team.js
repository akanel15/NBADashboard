

// Call all functions from here
function teamPage(teamData, name) {
    window.localStorage.setItem("current_team", JSON.stringify([name]))
    window.localStorage.setItem("current_page", JSON.stringify({team: true, player: false}))

}

// // This is an example on how to use team data
// // call this function from the teamPage function
// function example(data) {
//     console.log(data)
// }