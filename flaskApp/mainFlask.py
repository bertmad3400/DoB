#!/usr/bin/python3
from flask import Flask, render_template, Response
import json
import sqlite3

from Crypto.Hash import SHA256

from base64 import b64decode

from objects.transaction import transaction
from objects.blocks import block
from objects.chain import chain


app = Flask(__name__)
app.static_folder = "./static"
app.template_folder = "./templates"

def requestSingleDBEntry(fieldName, identifierFields, identifierValues):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    identifierFieldsString = ' and '.join([f"{fieldName} = ?" for fieldName in identifierFields])
    cur.execute(f"select {fieldName} from users where {identifierFieldsString}", tuple(value for value in identifierValues))

    DBEntry = cur.fetchone()

    conn.close()

    return DBEntry[0] if isinstance(DBEntry, tuple) else DBEntry

@app.route("/api/publicKey/<string:cpr>")
def returnPublicKey(cpr):

    publicKey = requestSingleDBEntry("publicKey", ["cpr"], [cpr])

    return Response(json.dumps({"publicKey" : publicKey}), mimetype='application/json')

@app.route("/api/privateKey/<string:cpr>/<string:password>")
def returnPrivateKey(cpr, password):

    privateKey = requestSingleDBEntry("privateKey", ["cpr", "password"], [cpr, password])

    return Response(json.dumps({"privateKey" : privateKey}), mimetype='application/json')



if __name__ == '__main__':
    firstBlock = block(SHA256.new("0".encode("utf-8")), [])
    firstBlock.calculatePoW()
    currentChain = chain(firstBlock)
    currentBlock = block(firstBlock.getBlockHash(), [])
    app.run(debug=True)
