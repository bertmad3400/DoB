from base64 import b64encode, b64decode
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

    def verify(self, publicKey):
        transactionHash = self.calculateTransactionHash()
        try:
            pkcs1_15.new(RSA.import_key(publicKey)).verify(transactionHash, b64decode(self.signature))
            return True
        except:
            return False
