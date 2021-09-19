from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams
from predict import predict
import numpy
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

def gen_player_score():
    all_player = []
    nba_players = players.get_players()
    for player in nba_players:
        if player['is_active']:
            all_player.append([player['full_name'],player['id']])
    
    ratings_arr = []

    for i in range(0, 20, 1):

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

    return ratings_arr


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


    array = [player_ActiveYears, player_Points, player_Gameplayed, player_Rebounds, player_Assists, player_Steals,
            player_Blocks, division(player_Points, player_Gameplayed), division(player_Rebounds, player_Gameplayed),
            division(player_Assists, player_Gameplayed), division(player_Steals, player_Gameplayed),
            division(player_Blocks, player_Gameplayed), player_fg, player_team]
    
    #predict(array[7])


    return array

def division(list1, list2):
    res = [0] * len(list1)
    for i in range(len(list1)):
        res[i] = list1[i] / list2[i]
    return res

def offensive_rating_calc(pts, ast, reb, fg_pct):
    MAX_PTS = 27
    MAX_AST = 7
    MAX_REB = 10
    MAX_FG = 50

    # pts worth 50%
    if pts >= MAX_PTS:
        pts_score = 1
    else:
        pts_score = pts/MAX_PTS

    
    # ast worth 20%
    if ast >= MAX_AST:
        ast_score = 1
    else:
        ast_score = ast/MAX_AST

    # reb worth 20%
    if reb >= MAX_REB:
        reb_score = 1
    else:
        reb_score = reb/MAX_REB
    
    # fg percentage worth 10%
    if fg_pct >= MAX_FG:
        fg_score = 1
    else:
        fg_score = fg_pct/MAX_FG

    off_factor = pts_score * 0.25 + ast_score * 0.1 + reb_score * 0.1 + fg_score * 0.05 + 0.5
    off_rating = off_factor * 100
    off_rating = round(off_rating)

    return off_rating

def defensive_rating_calc(stl, blk):
    # Calculated as an overall sum of both catigories to make fair
    MAX_SUM = 3.4

    tot = stl + blk
    # stl and blk worth 100 of rating%
    if tot >= MAX_SUM:
        def_factor = 1
    else:
        def_factor = tot/MAX_SUM * 0.5 + 0.5
    
    def_rating = def_factor * 100
    def_rating = round(def_rating)
    return def_rating

    

b = gen_player_score()
print(b)