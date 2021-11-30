from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


class transaction():
    def __init__(self, username, cpr, politicalParty, signature=None):
        self.username = username
        self.cpr = cpr
        self.politicalParty = politicalParty
        self.signature = signature

    def calculateTransactionHash(self):
        transaction = self.username + self.cpr + self.politicalParty
        return SHA256.new(transaction.encode())

    def sign(self, privateKey):
        transactionHash = self.calculateTransactionHash()
        self.signature = b64encode(pkcs1_15.new(RSA.import_key(privateKey)).sign(transactionHash))
