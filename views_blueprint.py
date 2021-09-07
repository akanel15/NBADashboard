from flask import Blueprint, Flask, render_template, request, jsonify, make_response

views = Blueprint('views', __name__, template_folder='templates')


@views.route("/")
def home():
    return render_template('home.html')

@views.route("/player")
def player():
    return render_template('player.html')

@views.route("/team")
def team():
    return render_template('team.html')

@views.route("/temp")
def main():
    return render_template('main.html')