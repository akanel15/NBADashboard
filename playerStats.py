from nba_api.stats.endpoints import playercareerstats, teamvsplayer, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams
# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
teamDash = teamplayerdashboard.TeamPlayerDashboard('1610612747').get_data_frames()[1]
print(teamDash["PLAYER_ID"][10])

print("Enter player's name to check his career stats!")
playerToCheck = str(input())
print("Enter player's current team!")
currentTeam = str(input())

current_team = [team for team in nba_teams
                if team['full_name'] == currentTeam][0]

selected_player = [player for player in nba_players
                   if player['full_name'] == playerToCheck][0]

career = playercareerstats.PlayerCareerStats(player_id=str(selected_player.get('id')))
res = career.get_data_frames()[0]
print(res)

shotArea = teamvsplayer.TeamVsPlayer(team_id=str(current_team.get('id')), vs_player_id=str(selected_player.get('id')))
print(shotArea.get_data_frames()[6])
