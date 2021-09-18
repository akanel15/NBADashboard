from flask import *
from nba_api.stats.static import teams
from teamStats import get_team_info_using_teamid


views = Blueprint('views', __name__, template_folder='templates')


@views.route("/")
@views.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@views.route("/player")
def player():
    return render_template('player.html')


@views.route("/team/<teamID>")
def team(teamID):
    teamData = get_team_info_using_teamid(teamID)
    teamInfo = teams.find_team_name_by_id(teamID)
    return render_template('team.html', teamInfo=teamInfo, teamData=teamData)
