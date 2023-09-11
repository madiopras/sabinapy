from flask import Flask, render_template, request, session, url_for, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls
app.jinja_env.filters["zip"] = zip
app.config["SECRET_KEY"] = "iniscretskuy2023"


@app.route("/", methods=["POST", "GET"])
def login():          
    return render_template("auth-login-basic.html")
    
@app.route('/home')
def home():
    return render_template("layouts-container.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=int("3000"))
# end main

# end main
#setup resource nya
#api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

