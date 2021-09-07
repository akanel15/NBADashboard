from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
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


def player_info(pid):
    career = playercareerstats.PlayerCareerStats(player_id=pid)
    for year in career.get_data_frames()[0]['SEASON_ID']:
        player_ActiveYears.append(year)
    for pts in career.get_data_frames()[0]['PTS']:
        player_Points.append(pts)
    return player_ActiveYears, player_Points


# LeBron James information.
print(player_info('2544'))
