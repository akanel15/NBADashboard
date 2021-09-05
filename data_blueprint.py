from flask import Blueprint, Flask, render_template, request, jsonify, make_response

data = Blueprint('data', __name__, template_folder='templates')


@data.route("/getdata")
def test():
    #put the data into the array which you want to render on the page
    
    array = []

    res = make_response(jsonify(array), 200)

    return res