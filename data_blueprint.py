from flask import Blueprint, Flask, render_template, request, jsonify, make_response

data = Blueprint('data', __name__, template_folder='templates')


@data.route("/meme")
def test():
    print("h")