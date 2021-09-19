from nba_api.stats.endpoints import playercareerstats, teamplayerdashboard
from nba_api.stats.static import players
from nba_api.stats.static import teams

from predict import player_predictor


def players_in_the_team(teamName):
    player_name = []
    nba_teams = teams.get_teams()

    selected_team = [team for team in nba_teams
                     if team['full_name'] == teamName][0]

    info = teamplayerdashboard.TeamPlayerDashboard(team_id=selected_team.get('id'))

    for player in info.get_data_frames()[1]['PLAYER_NAME']:
        player_name.append(player)

    return player_name


def gen_player_score(stats):
    scores = stats[7][len(stats[7]) - 1]
    assits = stats[9][len(stats[9]) - 1]
    steals = stats[10][len(stats[10]) - 1]
    blocks = stats[11][len(stats[11]) - 1]
    rebounds = stats[8][len(stats[8]) - 1]

    offensive = (0.8 * scores) + (0.4 * assits) + (0.4 * rebounds)
    defensive = (0.8 * blocks) + (0.8 * steals)

    return [offensive, defensive]


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

    last_activeyear = array[0][-1][0] + array[0][-1][1] + array[0][-1][2] + array[0][-1][3]
    next_season1_beforedash = int(last_activeyear) + 1
    next_season1_afterdash = int(last_activeyear[2] + last_activeyear[3]) + 2
    next_season2_beforedash = int(last_activeyear) + 2
    next_season2_afterdash = int(last_activeyear[2] + last_activeyear[3]) + 3
    next_2_season = [str(next_season1_beforedash) + '-' + str(next_season1_afterdash), str(next_season2_beforedash) +
                     '-' + str(next_season2_afterdash)]
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


b = player_info('Anthony Davis')
