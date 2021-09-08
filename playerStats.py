from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams

# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
# get_players returns a list of dictionaries, each representing a player.


# print("Enter your team name in full!")
current_team = 'Los Angeles Lakers'  # str(input())
inputTeam = [team for team in nba_teams
             if team['full_name'] == current_team][0]
teamDash = teamplayerdashboard.TeamPlayerDashboard(team_id=inputTeam.get('id')).get_data_frames()[1]

playerId_List = []
for player_id in teamDash['PLAYER_ID']:
    playerId_List.append(player_id)

playerToCheck = "Stephen Curry"


def get_ID(playerToCheck):
    nba_players = players.get_players()

    selected_player = [player for player in nba_players
                       if player['full_name'] == playerToCheck][0]

    career = playercareerstats.PlayerCareerStats(player_id=str(selected_player.get('id')))
    res = career.get_data_frames()[0]

    return res.PLAYER_ID[0]


def player_info(player):
    player_ActiveYears = []
    player_Points = []
    player_Gameplayed = []
    player_Rebounds = []
    player_Assists = []
    player_Steals = []
    player_Blocks = []
    pid = get_ID(player)
    career = playercareerstats.PlayerCareerStats(player_id=pid)
    for year in career.get_data_frames()[0]['SEASON_ID']:
        player_ActiveYears.append(year)
    for pts in career.get_data_frames()[0]['PTS']:
        player_Points.append(pts)
    for gp in career.get_data_frames()[0]['GP']:
        player_Gameplayed.append(gp)
    for reb in career.get_data_frames()[0]['REB']:
        player_Rebounds.append(reb)
    for ast in career.get_data_frames()[0]['AST']:
        player_Assists.append(ast)
    for stl in career.get_data_frames()[0]['STL']:
        player_Steals.append(stl)
    for blk in career.get_data_frames()[0]['BLK']:
        player_Blocks.append(blk)

    return [player_ActiveYears, player_Points, player_Gameplayed, player_Rebounds, player_Assists, player_Steals, player_Blocks]
