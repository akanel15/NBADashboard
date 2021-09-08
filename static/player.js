fetch('/getdata', {
    method: "POST",
    credentials: "include",
    body: localStorage.getItem("current_player"),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  .then(function(response) {
    if (response.status !== 200) {
      console.log(`Looks like there was a problem. Status code: ${response.status}`);
      return;
    }
    response.json().then(function(data) {
        player_page_functionality(data)
    });
  })
  .catch(function(error) {
    console.log("Fetch error: " + error);
});;

function player_page_functionality(data){
  window.localStorage.setItem('player_data', JSON.stringify(data));
}
