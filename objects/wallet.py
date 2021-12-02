from Crypto.PublicKey import RSA
import requests
import json
from base64 import b64decode, b64encode
from objects.transaction import transaction

class newWallet():
    def __init__(self):
        privateKey = RSA.generate(2048)
        self.privateKey = privateKey.export_key('PEM')
        self.publicKey = privateKey.public_key().export_key('PEM')

class wallet():
    def __init__(self, cpr, password):
        self.cpr = cpr
        self.publicKey = b64decode(requests.get(f"http://localhost:5000/api/publicKey/{cpr}").json()["publicKey"])
        self.privateKey = b64decode(requests.get(f"http://localhost:5000/api/privateKey/{cpr}/{password}").json()["privateKey"])

    def vote(self, username, politicalParty):
        currentTransaction = transaction(username, self.cpr, politicalParty)
        currentTransaction.sign(self.publicKey, self.privateKey)

        return requests.post("http://localhost:5000/api/submitTransaction", data=json.dumps({"username" : username, "cpr": self.cpr, "politicalParty" : politicalParty, "signature" : b64encode(currentTransaction.signature).decode("utf-8")}))
