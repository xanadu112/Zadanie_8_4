from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/mypage/me", methods=['GET'])
def mypage_me():
    return render_template("site_1.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def mypage_contact():
    contacts = ["email: michal_zatorski@o2.pl", "telefon: 604 836 715"]
    if request.method == 'GET':
        return render_template("site_2.html", contacts=contacts)  
    elif request.method == 'POST':
        print(request.form)
        return redirect("/mypage/contact")