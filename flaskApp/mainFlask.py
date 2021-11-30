#!/usr/bin/python3
from flask import Flask, render_template, Response
import json
import sqlite3


app = Flask(__name__)
app.static_folder = "./static"
app.template_folder = "./templates"

@app.route("/publicKey/<string:cpr>")
def returnPublicKey(cpr):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("select publicKey from users where cpr=?", (cpr,))

    publicKey = cur.fetchone()[0]

    conn.close()

    return Response(json.dumps({"publicKey" : publicKey}), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
