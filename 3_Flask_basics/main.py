from flask import Flask, render_template # import Flask class from flask module

myapp = Flask(__name__)

@myapp.route("/<job>")                   # End-point of our web-app
def FlaskTut(job):                       # function to be run when any user visits the end-point of my web-app
    name = "Sundas"
    return render_template("index.html", name1 = name, profession = str(job))

myapp.run(debug=True)                    # run on local host # auto Update

                                         # Running on http://127.0.0.1:5000/student
