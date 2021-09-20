

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
      tradeTableFormat(data); // pass rankings to table to be formatted
      let offensive = data[14][0];
      let defensive = data[14][1];
      let rank = data[14][2];
      rankingChart(rank, offensive, defensive);
      
    });
  })
  .catch(function (error) {
    console.log("Fetch error: " + error);
  });

function player_page_functionality(data) {
  let player_data = data;
  let seasons = player_data[0];
  let av_points = player_data[7];
  let av_assists = player_data[9];
  let av_rebounds = player_data[8];
  let av_steals = player_data[10];
  let av_blocks = player_data[11];



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

  const line = {
    id: 'line',
    beforeDraw(chart, args, options){
      const{ctx, chartArea: {top, right, bottom, left, width, height}, scales:{x, y}} = chart;
      ctx.save();
      if(seasons.length> 3){
        ctx.strokeStyle = 'red';
        ctx.strokeRect(x.getPixelForValue(seasons.length-2.5), top+40, 0, height-40);
        ctx.font = "20px Georgia";
        ctx.fillStyle = 'white';
        ctx.fillText("Predictions", x.getPixelForValue(seasons.length-3), 50)
      }
      ctx.restore();
    }
  }

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
    plugins: [line]
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
  
  let team = data[13];
  let seasons = data[0];
  let ppg = data[7];
  let apg = data[9];
  let rpg = data[8];
  let spg = data[10];
  let bpg = data[11];
  let fg_pct = data[12];
  for (i = 0; i < fg_pct.length; i++) 
  {
    fg_pct[i] = fg_pct[i] * 100
  }

  let table_dat = [seasons, team, ppg, fg_pct, apg, rpg, spg, bpg];

  for (let j = 0; j < table_dat[0].length; j++) {
    // column in dataset
    tablehtml += "<tr>";
    for (let i = 0; i < table_dat.length; i++) {
      // row in dataset
      if (i == 0) {
        tablehtml += "<th>" + table_dat[i][j] + "</th>";
      } 
      else if (i == 1) {
        tablehtml += "<td>" + table_dat[i][j] + "</td>";
      }
      else {
        num = table_dat[i][j];
        
        num = Math.round(num * 10) / 10;
        tablehtml += "<td>" + num + "</td>";
      }
    }
    tablehtml += "</tr>";
  }

  tbody.outerHTML = tablehtml;
}


function tradeTableFormat(data)
{
  var tbody = document.getElementById("tradeTableBody");
  var tablehtml = "";

  let closest_players = data[15];
  
  for (let i = 0; i < 10; i++) 
  {
    // column in dataset
    tablehtml += "<tr>";
    for (let j = 0; j < closest_players[0].length; j++) 
    {
      // row in dataset
      if (j == 0) 
      {
        tablehtml += "<th>" + closest_players[i][j] + "</th>";
      } 
      else
      {
        //player score @ 1,2,3 off,def,overall
        //compare to current player score and get difference

        let difference = ""
        let player_scores = data[14][j-1];
        let cur_score = closest_players[i][j];
        
        let dif = cur_score - player_scores;

        if (dif > 0)
        {
          //means it is better
          //add grean up arrow + diff
          difference = " &#8593".fontcolor("green") + String(dif).fontcolor("green");
        }
        else if (dif < 0)
        {
          //means it is worse
          //add red down arrow + abs(diff)
          difference = " &#8595".fontcolor("red") + String(Math.abs(dif)).fontcolor("red");
        }

    
        tablehtml += "<td>" + closest_players[i][j] + difference + "</td>";
      }
    }
    tablehtml += "</tr>";
  }
  tbody.innerHTML = tablehtml;
}

function formatRatingTable(num)
{
  let dat = localStorage.getItem("player_data");
  dat = JSON.parse(dat);

  var tbody = document.getElementById("tradeTableBody");
  var tablehtml = "";

  let closest_players = dat[15];
  sorting_by = [];
  for (i = 0; i < closest_players.length; i++)
  {
    sorting_by.push(closest_players[i][num]);
  }
  
  //  ort ratings based on off/def/overall and display the highest 10 for each
  let new_closest = counting_sort(sorting_by, closest_players);
  new_closest.reverse()
  
  for (let i = 0; i < 10; i++) 
  {
    // column in dataset
    tablehtml += "<tr>";
    for (let j = 0; j < new_closest[0].length; j++) 
    {
      // row in dataset
      if (j == 0) 
      {
        tablehtml += "<th>" + new_closest[i][j] + "</th>";
      } 
      else
      {
        //player score @ 1,2,3 off,def,overall
        //compare to current player score and get difference

        let difference = ""
        let player_scores = dat[14][j-1];
        let cur_score = new_closest[i][j];
        
        let dif = cur_score - player_scores;

        if (dif > 0)
        {
          //means it is better
          //add grean up arrow + diff
          difference = " &#8593".fontcolor("green") + String(dif).fontcolor("green");
        }
        else if (dif < 0)
        {
          //means it is worse
          //add red down arrow + abs(diff)
          difference = " &#8595".fontcolor("red") + String(Math.abs(dif)).fontcolor("red");
        }

    
        tablehtml += "<td>" + new_closest[i][j] + difference + "</td>";
      }
    }
    tablehtml += "</tr>";
  }
  tbody.innerHTML = tablehtml;
}  


function counting_sort(sorting_arr, init_arr)
{
    let m = Math.max(...sorting_arr); // find the max element to form count and position arrays
    let count = [];
    let pos = [];
    for (i = 0; i < m+1; i++)
    {
      count.push(0)
      pos.push(0)
    }

    for (i = 0; i < sorting_arr.length; i++)
    {
        count[sorting_arr[i]] += 1;
        // determining the number of each element in the array
    }

    for (j = 1; j < count.length; j++)
    {
        pos[j] = pos[j-1] + count[j-1];
        // using count array to determine the position each item will go
    }

    let output_arr = new Array(sorting_arr.length);

    for (i = 0; i < sorting_arr.length; i++)
    {
        output_arr[pos[sorting_arr[i]]] = init_arr[i]; // finding the position that element goes and storing
        pos[sorting_arr[i]] += 1; // incrementing the position to know where the next one will go
    }

    return output_arr      
}

window.onload = (event) => {
  document.getElementById("playerName").innerHTML = localStorage
    .getItem("current_player")
    .slice(2, -2);
};




// Ranking Chart
function rankingChart(ranking, off, def) {
  // 0 < ranking < 100
  function calc_offset(tot_outer, rank) {
    return tot_outer - (tot_outer * rank) / 100
  }

  let root = document.documentElement;
  let total_outer = getComputedStyle(root).getPropertyValue("--total-outer");

  root.style.setProperty("--offset-outer", calc_offset(total_outer, ranking));
  root.style.setProperty("--offset-off-outer", calc_offset(total_outer, off));
  root.style.setProperty("--offset-def-outer", calc_offset(total_outer, def));

  document.getElementById("rank").innerText = ranking.toString();
  document.getElementById("off_rank").innerText = off.toString();
  document.getElementById("def_rank").innerText = def.toString();
}

