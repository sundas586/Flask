
# A minimal Flask application looks something like this:

from flask import Flask    # import Flask class from flask module

app = Flask(__name__)      # Define App

@app.route("/myFlaskWebApp")            # End-point of our web-app
def hello_world():         # function to be run when any user visits the end-point of my web-app
    return "<p>Hello, World!</p>
  
app.run(debug= True)                  # run on local host # auto Update
  
