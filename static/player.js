

let myGraph = null;

fetch("/getdata", {
  method: "POST",
  credentials: "include",
  body: localStorage.getItem("current_player"),
  cache: "no-cache",
  headers: new Headers({
    "content-type": "application/json",
  }),
})
  .then(function (response) {
    if (response.status !== 200) {
      console.log(
        `Looks like there was a problem. Status code: ${response.status}`
      );
      return;
    }
    response.json().then(function (data) {
      // Store data in local storage
      window.localStorage.setItem("player_data", JSON.stringify(data));
      player_page_functionality(data); // pass data onto chartJs
      formatTable(data); // pass data to be formatted into a table

      let rank = 100;
      rankingChart(rank);
    });
  })
  .catch(function (error) {
    console.log("Fetch error: " + error);
  });

function player_page_functionality(data) {
  let player_data = data;
  seasons = player_data[0];
  av_points = player_data[7];
  av_assists = player_data[9];
  av_rebounds = player_data[8];
  av_steals = player_data[10];
  av_blocks = player_data[11];



  let borderColor = [
    "rgb(255, 99, 132)",
    "rgb(255, 159, 64)",
    "rgb(255, 205, 86)",
    "rgb(75, 192, 192)",
    "rgb(54, 162, 235)",
    "rgb(153, 102, 255)",
    "rgb(201, 203, 207)",
  ];
  let backgroundColor = [
    "rgba(255, 99, 132, 0.2)",
    "rgba(255, 159, 64, 0.2)",
    "rgba(255, 205, 86, 0.2)",
    "rgba(75, 192, 192, 0.2)",
    "rgba(54, 162, 235, 0.2)",
    "rgba(153, 102, 255, 0.2)",
    "rgba(201, 203, 207, 0.2)",
  ];


  let myChart = document.getElementById("myChart");

  myGraph = new Chart(myChart, {
    type: "bar", //"line"
    data: {
      labels: seasons,
      datasets: [
        {
          label: "Points",
          data: av_points,
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        },
        {
          label: "Assists",
          data: av_assists,
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        },
        {
          label: "Rebounds",
          data: av_rebounds,
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        },
        {
          label: "Steals",
          data: av_steals,
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        },
        {
          label: "Blocks",
          data: av_blocks,
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        }
      ],
    },
  });
  for (let i = 1; i<= 4; i++)
  {
    myGraph.hide(i);
  }
}

function toggleData(index)
{
  for (let i =0; i <= 4; i++)
  {
    let vis = myGraph.isDatasetVisible(i);
    if (vis === true)
    {
      myGraph.hide(i);
    } 
  }
  myGraph.show(index);
}



function formatTable(data) {
  var tbody = document.getElementById("tableStatsBody");
  var tablehtml = "";
  console.log(data);
  
  let sub = data.slice(0,1);
  console.log(sub);
  sub.push(data.slice(2,3)[0]);
  console.log(sub);
  let other = data.slice(7,12);  
  console.log(other);
  for (item = 0; item< other.length; item++)
  {
    sub.push(other[item]);
  }
  console.log(sub);



  for (let j = 0; j < sub[0].length; j++) {
    // column in dataset
    tablehtml += "<tr>";
    for (let i = 0; i < sub.length; i++) {
      // row in dataset
      if (i == 0) {
        tablehtml += "<th>" + sub[i][j] + "</th>";
      } else {
        num = sub[i][j];
        console.log(num);
        
        num = Math.round(num * 10) / 10;
        tablehtml += "<td>" + num + "</td>";
      }
    }
    tablehtml += "</tr>";
  }

  tbody.outerHTML = tablehtml;
}

window.onload = (event) => {
  document.getElementById("playerName").innerHTML = localStorage
    .getItem("current_player")
    .slice(2, -2);
  document.getElementById("teamName").innerHTML = localStorage
    .getItem("current_team")
    .slice(2, -2);
};




// Ranking Chart
function rankingChart(ranking) {
  // 0 < ranking < 100

  let root = document.documentElement;
  let total_outer = getComputedStyle(root).getPropertyValue("--total-outer");

  root.style.setProperty("--offset-outer", total_outer - (total_outer * ranking) / 100);

  document.getElementById("rank").innerText = ranking.toString();
}

