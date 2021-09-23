from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
from nba_api.stats.static import players
import numpy
import math
from playerStats import offensive_rating_calc, defensive_rating_calc
from countingSort import counting_sort


# This function provides the method of calculating all the player rating from the api and ordering them
def rating_calculator():
    all_player = []
    ov_arr = []
    nba_players = players.get_players()
    for player in nba_players:
        if player['is_active']:
            all_player.append([player['full_name'],player['id']])

    ratings_arr = []

    for i in range(len(all_player)):

        pl_id = all_player[i][1]
     
        career = playercareerstats.PlayerCareerStats(player_id=str(pl_id))

        
        gp = career.get_data_frames()[0]['GP'].values[-1]
        pts = career.get_data_frames()[0]['PTS'].values[-1]
        ast = career.get_data_frames()[0]['AST'].values[-1]
        reb = career.get_data_frames()[0]['REB'].values[-1]
        fg_pct = career.get_data_frames()[0]['FG_PCT'].values[-1]
        stl = career.get_data_frames()[0]['STL'].values[-1]
        blk = career.get_data_frames()[0]['BLK'].values[-1]

        if pts == None:
            pts = 0
        if numpy.isnan(reb):
            reb = 0
        if ast == None:
            ast = 0
        if stl == None:
            stl = 0
        if blk == None:
            blk = 0
        if fg_pct == None:
            fg_pct = 0

        # Standardise values
        ppg = pts/gp
        apg = ast/gp
        rpg = reb/gp
        spg = stl/gp
        bpg = blk/gp

        #player_stats = [ppg, apg, rpg, fg_pct, spg, bpg]
        player_name  = all_player[i][0]
        off_rating = offensive_rating_calc(ppg, apg, rpg, fg_pct)
        def_rating = defensive_rating_calc(spg, bpg)
        overall_rating = math.ceil(off_rating * 0.5 + def_rating * 0.5)

        ratings_arr.append([player_name, off_rating, def_rating, overall_rating])
        ov_arr.append(overall_rating)
    
    # sort players based off their overall rating
    sorted_player_ratings = counting_sort(ov_arr,ratings_arr)
    return sorted_player_ratings
