from flask import Flask, render_template, request, jsonify, make_response
from data_blueprint import data
from views_blueprint import views

app = Flask(__name__)

app.register_blueprint(data)
app.register_blueprint(views)


if __name__ == "__main__":
    app.run(debug=True)