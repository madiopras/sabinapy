from flask import Flask, render_template, request, session, url_for, redirect
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls
app.jinja_env.filters["zip"] = zip
app.config["SECRET_KEY"] = "iniscretskuy2023"





@app.route("/", methods=["POST", "GET"])
def index():
    title = "Home"
    if "email" in session:
        return redirect(url_for('sukses_login'))
    else: 
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            #check Debugging
            print("Email :", email)
            print("Password :", password)
            if email == 'sabina@gmail.com' and password == 'dio':
                session['email'] = email
                return redirect(url_for('sukses_login'))
            else:
                return redirect(url_for('index'))
            
        return render_template("index.html", judul=title)
    

@app.route('/sukses')
def sukses_login():
    title = "Home"
    nilai = "Hallo selamat datang, Sabina!"
    return render_template("sukses.html", nilai=nilai, judul=title)

@app.route("/about")
def about():
    title = "About"
    if "email" in session:
        return render_template("about.html", judul=title)
    else:
        return redirect(url_for('index'))

@app.route("/contact")
def contact():
    title = "Contact"
    if "email" in session:
        return render_template("contact.html", judul=title)
    else:
        return redirect(url_for('index'))


@app.route("/redirect-about")
def skuy_redirect():
    return redirect(url_for('about'))
    
@app.route("/logout")
def logout_akun():
    if "email" not in session:
        return redirect(url_for('index'))
    else:
        session.pop("email")
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=int("80"))

# end main

# end main
#setup resource nya
#api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

