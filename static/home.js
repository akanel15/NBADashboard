function stage(){
    console.log("here")
    player_name = document.getElementById("Name").value
    player_team = document.getElementById("Team").value
    console.log([player_name, player_team])

    localStorage.setItem("current_player", JSON.stringify([player_name, player_team]))

    window.location.href = "/player"
}