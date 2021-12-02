from flask import Flask, render_template, request, flash

from account import checkAcc
from account import balance, accounts, writeAcc, readAcc

app = Flask(__name__)
app.secret_key = 'development key'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard", methods=['POST', 'GET'])
def dash():
    usname = (request.form['name'])
    pss = str(request.form['pass'])
    writeAcc(usname)
    return render_template("dashboard.html", name=checkAcc(usname, pss), b=balance(usname, pss), id=usname)


@app.route("/deposit")
def depo():
    return render_template("deposit.html")


@app.route("/final", methods=['POST', 'GET'])
def dep():
    amount = request.form['amount']
    iden = readAcc()
    f = open('notes.txt', 'r+')
    f.truncate(0)
    balance = int(accounts[iden]["Balance"]) + int(amount)
    writeAcc(str(balance))
    fin = int(readAcc())
    return render_template("final.html", b=fin, name=accounts[iden]["name"], id=iden, t=accounts[iden]["Type"])


if __name__ == '__main__':
    app.run(debug=True)
