from flask import *
from nba_api.stats.static import teams
from teamStats import get_team_info, get_team_info_using_teamid


views = Blueprint('views', __name__, template_folder='templates')


@views.route("/")
@views.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@views.route("/player")
def player():
    return render_template('player.html')


@views.route("/team/<teamRequest>")
def team(teamRequest):
    teamName = teamRequest.replace("%20", " ")
    teamData = get_team_info(teamName)
    teamInfo = teams.find_teams_by_full_name(teamName)[0]
    return render_template('team.html', teamInfo=teamInfo, teamData=teamData)
