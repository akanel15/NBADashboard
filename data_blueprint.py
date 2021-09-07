from flask import Blueprint, Flask, render_template, request, jsonify, make_response
from playerStats import player_info

data = Blueprint('data', __name__, template_folder='templates')


@data.route("/getdata", methods=["POST", "GET"])
def test():
    #put the data into the array which you want to render on the page
    array = request.get_json()
    data = player_info(array[0])
    print(data)

    res = make_response(jsonify(data), 200)

    return res


#get input from the homepage
#save the input in local storage

#redirect to the player page
#on load of player page use fecth to request data
#pass the variables from the local storage
#get the response

#graph or use the data