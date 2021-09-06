from nba_api.stats.endpoints import playercareerstats, teamvsplayer, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams

# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()

# print("Enter your team name in full!")
current_team = 'Los Angeles Lakers'  # str(input())
inputTeam = [team for team in nba_teams
             if team['full_name'] == current_team][0]
teamDash = teamplayerdashboard.TeamPlayerDashboard(team_id=inputTeam.get('id')).get_data_frames()[1]

playerId_List = []
for player_id in teamDash['PLAYER_ID']:
    playerId_List.append(player_id)

player_ActiveYears = []
player_Points = []

# for player_id in playerId_List:
    # careerInfo = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]

# shotArea = teamvsplayer.TeamVsPlayer(team_id=str(current_team.get('id')), vs_player_id=str(selected_player.get('id')))
# print(shotArea.get_data_frames()[6])
