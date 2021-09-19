from nba_api.stats.endpoints import teamyearbyyearstats
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

    return [season_played, game_played, wins, losses, win_percentage, conf_rank, po_gp, po_wins, po_losses,
            final_appearance]


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

