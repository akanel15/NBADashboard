from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams

nba_players = players.get_players()
playerToCheck = "Stephen Curry"

selected_player = [player for player in nba_players
                   if player['full_name'] == playerToCheck][0]


career = playercareerstats.PlayerCareerStats(player_id=str(selected_player.get('id')))
#print(career)
res = career.get_data_frames()[0]
print(res)
print(res.PLAYER_ID[0]) 