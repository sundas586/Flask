# A minimal Flask application looks something like this:

from flask import Flask # import Flask class from flask module

app = Flask(__name__)

@app.route("/")     # End-point of our web-app
def firstpage():      # function to be run when any user visits the end-point of my web-app
    return "<p>Hello, Welcome to Home Page!</p>"
@app.route("/FlaskWebApp")
def secondpage():
    return "<p>Hello, This is second page!</p>"
app.run(debug=True)     # # run on local host # auto Update
