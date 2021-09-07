function stage(){
    console.log("here")
    player_name = document.getElementById("Name").value
    console.log(player_name)

    localStorage.setItem("current_player", JSON.stringify([player_name]))

    window.location.href = "/player"
}