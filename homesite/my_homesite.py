from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/mypage/me", methods=['GET'])
def display_about_me():
    return render_template("about_me.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def display_contact():
    contact_details = ["email: michal_zatorski@o2.pl", "telefon: 604 836 715"]
    
    if request.method == 'GET':
        return render_template("contact.html", contact_details=contact_details)  
    
    elif request.method == 'POST':
        print(request.form["element"])
        return redirect("/mypage/contact")