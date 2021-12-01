from Crypto.Hash import SHA256
import json

class block():
    def __init__(self, lastBlockHash, transactionList):
        self.lastBlockHash = lastBlockHash
        self.transactionList = transactionList
        self.proofOfWork = 0

    def toString(self):
        transactionString = [transaction.toString() for transaction in self.transactionList]
        return json.dumps({ "lastBlock" : self.lastBlockHash, "transactions" : transactionString, "PoW" : self.proofOfWork })

    def getBlockHash(self):
        return SHA256.new(self.toString().encode("utf-8"))
