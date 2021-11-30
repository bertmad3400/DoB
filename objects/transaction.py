from base64 import b64encode, b64decode
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

import json

class transaction():
    def __init__(self, username, cpr, politicalParty, signature=None):
        self.username = username
        self.cpr = cpr
        self.politicalParty = politicalParty
        self.signature = signature

    def toString(self):
        return json.dumps({ "username" : self.username, "cpr" : self.cpr, "politicalParty" : self.politicalParty })

    def calculateTransactionHash(self):
        return SHA256.new(self.toString().encode("utf-8"))

    def sign(self, privateKey):
        transactionHash = self.calculateTransactionHash()
        self.signature = b64encode(pkcs1_15.new(RSA.import_key(privateKey)).sign(transactionHash))

    def verify(self, publicKey):
        transactionHash = self.calculateTransactionHash()
        try:
            pkcs1_15.new(RSA.import_key(publicKey)).verify(transactionHash, b64decode(self.signature))
            return True
        except:
            return False
