#!/usr/bin/python3
from flask import Flask, render_template, Response
import json
import sqlite3


app = Flask(__name__)
app.static_folder = "./static"
app.template_folder = "./templates"

@app.route("/api/publicKey/<string:cpr>")
def returnPublicKey(cpr):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("select publicKey from users where cpr=?", (cpr,))

    publicKey = cur.fetchone()[0]

    conn.close()

    return Response(json.dumps({"publicKey" : publicKey}), mimetype='application/json')

@app.route("/api/privateKey/<string:cpr>/<string:password>")
def returnPublicKey(cpr, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("select privateKey from users where cpr=? and password=?", (cpr,password))

    privateKey = cur.fetchone()[0]

    conn.close()

    return Response(json.dumps({"privateKey" : privateKey}), mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
