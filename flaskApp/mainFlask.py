#!/usr/bin/python3
from flask import Flask, render_template, Response, request, abort
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

firstBlock = block(SHA256.new("0".encode("utf-8")), [])
firstBlock.calculatePoW()
currentChain = chain(firstBlock)
currentBlock = block(firstBlock.getBlockHash(), [])

def handleNewTransaction(transaction):
    global currentBlock
    blockResponse = currentBlock.appendTransaction(transaction)
    print(blockResponse)
    print(len(currentBlock.transactionList))

    verifyFeedback = currentBlock.verifyTransactions()
    while verifyFeedback != -1:
        currentBlock.pop(verifyFeedback)
        verifyFeedback = currentBlock.verifyTransactions()

    if blockResponse == 1:
        currentBlock.calculatePoW()
        if not currentChain.appendBlock(currentBlock):
            abort(500)
        currentBlock = block(currentChain.blockchain[-1].getBlockHash(), [])
    elif blockResponse == 2:
        abort(422)
    elif blockResponse == 3:
        abort(500)


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

@app.route("/api/submitTransaction", methods=["POST"])
def submitTransaction():
    try:
        details = {}
        for element in ["username", "cpr", "politicalParty", "signature"]:
            currentElement = element
            details[element] = request.get_json(force=True)[element]
    except:
        return Response(response=json.dumps({"error" : f'The needed paramter "{currentElement}" was not sent.'}), mimetype="application/json", status=422)

    details["signature"] = b64decode(details["signature"])

    details["publicKey"] = b64decode(requestSingleDBEntry("publicKey", ["cpr"], [details["cpr"]]))

    currentTransaction = transaction(details["username"], details["cpr"], details["politicalParty"], signature=details["signature"], publicKey=details["publicKey"])

    if currentTransaction.verify():
        handleNewTransaction(currentTransaction)
        print(currentChain.blockchain)
        return Response(response=json.dumps({"msg" : "Transaction successfully submitted"}), mimetype="application/json", status=200)
    else:
        return Response(response=json.dumps({"error" : "Transaction is not valid"}), mimetype="application/json", status=422)

@app.route("/api/countVotes")
def countVotes():
    partyList = ["Test1", "Test2", "Test3"]
    currentBlock.calculatePoW()
    currentChain.appendBlock(currentBlock)
    print(currentChain.blockchain)
    return Response(json.dumps(currentChain.countVotes(partyList)), mimetype='application/json')





if __name__ == '__main__':
    app.run(debug=True)
