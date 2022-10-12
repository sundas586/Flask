# A minimal Flask application looks something like this:

from flask import Flask , jsonify# import Flask class from flask module

app = Flask(__name__)

@app.route("/CheckOddNuber/<int:a>")      # End-point of our web-app
def CheckOddNuber(a): # function to be run when any user visits the end-point of my web-app
    if a%2 != 0 :
        print("Not an odd number")
        result = {                   # python dictionary
            "Your Number" : a,
            "Your Result": False
        }
    else :
        print("An odd number")       # python dictionary
        result = {
            "Your Number": a,
            "Your Result": True
        }
    return jsonify(result)           # converts python to JSON

app.run(debug=True)# # run on local host # auto Update

# Check Results --> http://127.0.0.1:5000/CheckOddNuber/55
