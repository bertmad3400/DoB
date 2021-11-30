from Crypto.PublicKey import RSA
import requests
import json
from base64 import b64decode
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
