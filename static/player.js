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
    });
  })
  .catch(function (error) {
    console.log("Fetch error: " + error);
  });

function player_page_functionality(data) {
  let player_data = data;
  seasons = player_data[0];
  points = player_data[1];

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
          data: points,
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        },
        {
          label: "Assists",
          data: [7, 10, 5, 12, 20, 23, 1, 1, 1, 1, 1, 1],
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        },
        {
          label: "Rebounds",
          data: [7, 10, 5, 12, 20, 23, 1, 1, 1, 1, 1, 1],
          backgroundColor: backgroundColor,
          borderWidth: 1,
          borderColor: borderColor,
          hoverBorderWidth: 3,
          hoverBorderColor: "#777",
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Custom Chart Title",
      },
    },
  });
}

function toggleData(index) {
  let vis = myGraph.isDatasetVisible(index);
  if (vis === true) {
    myGraph.hide(index);
  } else if (vis === false) {
    myGraph.show(index);
  }
}

function formatTable(data) {
  var tbody = document.getElementById("tableStatsBody");
  var tablehtml = "";

  for (let j = 0; j < data[0].length; j++) {
    // column in dataset
    tablehtml += "<tr>";
    for (let i = 0; i < data.length; i++) {
      // row in dataset
      if (i == 0) {
        tablehtml += "<th>" + data[i][j] + "</th>";
      } else {
        tablehtml += "<td>" + data[i][j] + "</td>";
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
