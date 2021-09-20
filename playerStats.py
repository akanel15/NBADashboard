from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams
from predict import player_predictor
from potential_trades import closest_players_by_rating
import math




def players_in_the_team(teamName):
    player_name = []
    nba_teams = teams.get_teams()

    selected_team = [team for team in nba_teams
                     if team['full_name'] == teamName][0]

    info = teamplayerdashboard.TeamPlayerDashboard(team_id=selected_team.get('id'))

    for player in info.get_data_frames()[1]['PLAYER_NAME']:
        player_name.append(player)

    return player_name


def get_ID(playerName):
    nba_players = players.get_players()

    selected_player = [player for player in nba_players
                       if player['full_name'] == playerName][0]

    career = playercareerstats.PlayerCareerStats(player_id=str(selected_player.get('id')))

    return career.get_data_frames()[0].PLAYER_ID[0]


def player_info(player):
    player_ActiveYears = []
    player_Points = []
    player_Gameplayed = []
    player_Rebounds = []
    player_Assists = []
    player_Steals = []
    player_Blocks = []
    player_fg = []
    player_team = []

    pid = get_ID(player)
    ind = int(pid)

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
    for team in career.get_data_frames()[0]['TEAM_ABBREVIATION']:
        player_team.append(team)
    for fg in career.get_data_frames()[0]['FG_PCT']:
        player_fg.append(fg)
    

    ppg = division(player_Points, player_Gameplayed)
    rpg = division(player_Rebounds, player_Gameplayed)
    apg = division(player_Assists, player_Gameplayed)
    spg = division(player_Steals, player_Gameplayed)
    bpg = division(player_Blocks, player_Gameplayed)

    array = [player_ActiveYears, player_Points, player_Gameplayed, player_Rebounds, player_Assists, player_Steals,
            player_Blocks, ppg, rpg, apg, spg, bpg, player_fg, player_team]
    

    off_rating = offensive_rating_calc(ppg[-1], apg[-1], rpg[-1], player_fg[-1])
    def_rating = defensive_rating_calc(spg[-1], bpg[-1])
    overall_rating = math.ceil(off_rating * 0.5 + def_rating * 0.5)
    array.append([off_rating, def_rating, overall_rating])

    closest_players = closest_players_by_rating(player, overall_rating)
    array.append(closest_players)
    array.append(ind)
    
    #predict(array[7])

    last_activeyear = array[0][-1][0] + array[0][-1][1] + array[0][-1][2] + array[0][-1][3]
    next_season1_beforedash = int(last_activeyear) + 1
    next_season1_afterdash = int(last_activeyear[2] + last_activeyear[3]) + 2
    next_season2_beforedash = int(last_activeyear) + 2
    next_season2_afterdash = int(last_activeyear[2] + last_activeyear[3]) + 3
    next_2_season = [str(next_season1_beforedash) + '-' + str(next_season1_afterdash), str(next_season2_beforedash) +
                     '-' + str(next_season2_afterdash)]
    



    if len(array[0]) <= 3:
        return array
    
    for element in next_2_season:
        array[0].append(element)
    for i in range(7, 13):
        future_season_stats = player_predictor(array[i], 0.3)
        for element in future_season_stats:
            array[i].append(element)

    return array


def division(list1, list2):
    res = [0] * len(list1)
    for i in range(len(list1)):
        res[i] = list1[i] / list2[i]
    return res

def offensive_rating_calc(pts, ast, reb, fg_pct):
    MAX_PTS = 28
    MAX_AST = 8
    MAX_REB = 11
    MAX_FG = 0.5

    # pts worth 60%
    if pts >= MAX_PTS:
        pts_score = 1
    else:
        pts_score = pts/MAX_PTS

    
    # ast worth 15%
    if ast >= MAX_AST:
        ast_score = 1
    else:
        ast_score = ast/MAX_AST

    # reb worth 15%
    if reb >= MAX_REB:
        reb_score = 1
    else:
        reb_score = reb/MAX_REB
    
    # fg percentage worth 10%
    if fg_pct >= MAX_FG:
        fg_score = 1
    else:
        fg_score = fg_pct/MAX_FG

    off_factor = pts_score * 0.30 + ast_score * 0.075 + reb_score * 0.075 + fg_score * 0.05 + 0.5
    off_rating = off_factor * 100
    off_rating = round(off_rating)

    return off_rating

def defensive_rating_calc(stl, blk):
    # Calculated as an overall sum of both catigories to make fair
    MAX_STL = 1.3
    MAX_BLK = 1.3
    
    if stl >= MAX_STL:
        stl_score = 1
    else:
        stl_score = stl/MAX_STL

    if blk >= MAX_BLK:
        blk_score = 1
    else:
        blk_score = blk/MAX_BLK


    def_factor = blk_score * 0.25 + stl_score * 0.25 + 0.5
    def_rating = def_factor * 100
    def_rating = round(def_rating)

    return def_rating

lebron = player_info('LeBron James')
print(lebron[8])
print(lebron[9])
