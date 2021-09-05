from flask import Blueprint, Flask, render_template, request, jsonify, make_response

data = Blueprint('data', __name__, template_folder='templates')


@data.route("/getdata")
def test():
    #put the data into the array which you want to render on the page
    array = getdata(Name, Team)

    res = make_response(jsonify(array), 200)

    return res


#get input from the homepage
#save the input in local storage

#redirect to the player page
#on load of player page use fecth to request data
#pass the variables from the local storage
#get the response

#graph or use the data