from nba_api.stats.endpoints import teamyearbyyearstats, teamplayerdashboard, teamdashboardbylastngames, \
    teamdashboardbyshootingsplits
from nba_api.stats.static import teams


def get_team_id(teamName):
    nba_teams = teams.get_teams()

    selected_team = [team for team in nba_teams
                     if team['full_name'] == teamName][0]

    teamInfo = teamyearbyyearstats.TeamYearByYearStats(team_id=str(selected_team.get('id')))

    return teamInfo.get_data_frames()[0].TEAM_ID[0]


def get_team_info(teamName):
    team_id = get_team_id(teamName)

    team_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id).get_data_frames()[0]

    season_played = []
    for season in team_stats['YEAR']:
        season_played.append(season)

    game_played = []
    for gp in team_stats['GP']:
        game_played.append(gp)

    wins = []
    for win in team_stats['WINS']:
        wins.append(win)

    losses = []
    for loss in team_stats['LOSSES']:
        losses.append(loss)

    win_percentage = []
    for win_pct in team_stats['WIN_PCT']:
        win_percentage.append(win_pct)

    conf_rank = []
    for _ in team_stats['CONF_RANK']:
        conf_rank.append(_)

    po_wins = []
    for powins in team_stats['PO_WINS']:
        po_wins.append(powins)

    po_losses = []
    for polosses in team_stats['PO_LOSSES']:
        po_losses.append(polosses)

    # N/A - not in final, FINALS APPEARANCE - lost in final, LEAGUE CHAMPION - won in final.
    final_appearance = []
    for _ in team_stats['NBA_FINALS_APPEARANCE']:
        final_appearance.append(_)

    po_gp = [[] for _ in po_wins]
    for i in range(len(po_gp)):
        po_gp[i] = po_wins[i] + po_losses[i]

    latest_season = season_played[-1]
    team_dashboard = teamplayerdashboard.TeamPlayerDashboard(team_id=team_id, season=latest_season).get_data_frames()[1]

    player_name = []
    for player in team_dashboard['PLAYER_NAME']:
        player_name.append(player)

    team_lastgame = teamdashboardbylastngames.TeamDashboardByLastNGames(
        team_id=team_id, season=latest_season).get_data_frames()[1]

    last_5_games = ['Last 5 games']
    w = []
    for win in team_lastgame['W']:
        w.append(win)

    l = []
    for lose in team_lastgame['L']:
        l.append(lose)

    w_pct = []
    for win_pct in team_lastgame['W_PCT']:
        w_pct.append(win_pct)

    # field goal attempt
    fga = []
    for FGA in team_lastgame['FGA']:
        fga.append(FGA)
    # field goal made
    fgm = []
    for FGM in team_lastgame['FGM']:
        fgm.append(FGM)

    fg_pct = []
    for FG_pct in team_lastgame['FG_PCT']:
        fg_pct.append(FG_pct)

    reb = []
    for rebound in team_lastgame['REB']:
        reb.append(rebound)

    ast = []
    for assist in team_lastgame['AST']:
        ast.append(assist)
    # turnovers
    tov = []
    for turnover in team_lastgame['TOV']:
        tov.append(turnover)

    stl = []
    for steal in team_lastgame['STL']:
        stl.append(steal)

    blk = []
    for block in team_lastgame['BLK']:
        blk.append(block)

    pts = []
    for point in team_lastgame['PTS']:
        pts.append(point)
    # team efficiency
    plus_minus = []
    for plusandminus in team_lastgame['PLUS_MINUS']:
        plus_minus.append(plusandminus)

    team_shooting = teamdashboardbyshootingsplits.TeamDashboardByShootingSplits(
        team_id=team_id, season=latest_season).get_data_frames()[3]

    shot_area = []
    for values in team_shooting['GROUP_VALUE']:
        shot_area.append(values)

    # field goal attempt
    fga_area = []
    for FGA in team_shooting['FGA']:
        fga_area.append(FGA)
    # field goal made
    fgm_area = []
    for FGM in team_shooting['FGM']:
        fgm_area.append(FGM)

    fg_pct_area = []
    for FG_pct in team_shooting['FG_PCT']:
        fg_pct_area.append(FG_pct)

    return [season_played, game_played, wins, losses, win_percentage, conf_rank, po_gp, po_wins, po_losses,
        final_appearance], \
        [player_name], \
        [last_5_games, w, l, w_pct, fga, fgm, fg_pct, pts, ast, reb, stl, blk, tov, plus_minus], \
        [shot_area, fga_area, fgm_area, fg_pct_area]


def get_team_info_using_teamid(teamID):
    team_stats = teamyearbyyearstats.TeamYearByYearStats(teamID).get_data_frames()[0]

    season_played = []
    for season in team_stats['YEAR']:
        season_played.append(season)

    game_played = []
    for gp in team_stats['GP']:
        game_played.append(gp)

    wins = []
    for win in team_stats['WINS']:
        wins.append(win)

    losses = []
    for loss in team_stats['LOSSES']:
        losses.append(loss)

    win_percentage = []
    for win_pct in team_stats['WIN_PCT']:
        win_percentage.append(win_pct)

    conf_rank = []
    for _ in team_stats['CONF_RANK']:
        conf_rank.append(_)

    po_wins = []
    for powins in team_stats['PO_WINS']:
        po_wins.append(powins)

    po_losses = []
    for polosses in team_stats['PO_LOSSES']:
        po_losses.append(polosses)

    # N/A - not in final, FINALS APPEARANCE - lost in final, LEAGUE CHAMPION - won in final.
    final_appearance = []
    for _ in team_stats['NBA_FINALS_APPEARANCE']:
        final_appearance.append(_)

    po_gp = [[] for _ in po_wins]
    for i in range(len(po_gp)):
        po_gp[i] = po_wins[i] + po_losses[i]

    return [season_played, game_played, wins, losses, win_percentage, conf_rank, po_gp, po_wins, po_losses,
            final_appearance]
