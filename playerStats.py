from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams
from predict import predict


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
        all_player.append([player['full_name'],player['id']])
    
    kar_id = all_player[2][1]
    
    career = playercareerstats.PlayerCareerStats(player_id=str(kar_id))
    #last_yr = career.get_data_frames()[0]['SEASON_ID'][-1]

    array = [career.get_data_frames()[0]['GP'], career.get_data_frames()[0]['PTS'], career.get_data_frames()[0]["AST"]
             , career.get_data_frames()[0]['REB'], career.get_data_frames()[0]['FG_PCT'],
             career.get_data_frames()[0]['STL'], career.get_data_frames()[0]['BLK']]
    return array


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
    MAX_PTS = 31
    MAX_AST = 11
    MAX_REB = 14
    MAX_FG = 55

    #pts wort 50%
    if pts >= MAX_PTS:
        pts_score = 1
    else:
        pts_score = pts/MAX_PTS

    
    #ast worth 20%
    if ast >= MAX_AST:
        ast_score = 1
    else:
        ast_score = ast/MAX_AST

    #reb worth 20%
    if reb >= MAX_REB:
        reb_score = 1
    else:
        reb_score = reb/MAX_REB
    
    # fg percentage worth 10%
    if fg_pct >= MAX_FG:
        fg_score = 1
    else:
        fg_score = fg_pct/MAX_FG

    off_factor =  pts_score * 0.5 + ast_score * 0.2 + reb_score * 0.2 + fg_score * 0.1
    off_rating = off_factor * 100
    off_rating = round(off_rating)

    return off_rating

def defensive_rating_calc(stl, blk):
    #Calculated as an overall sum of both catigories to make fair
    MAX_SUM = 3.4

    tot = stl + blk
    # stl and blk worth 100 of rating%
    if tot >= MAX_SUM:
        def_factor = 1
    else:
        def_factor = tot/MAX_SUM
    
    def_rating = def_factor * 100
    def_rating = round(def_rating)
    return def_rating

    



a = player_info('LeBron James')
b = gen_player_score()
print(b)