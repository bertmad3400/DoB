import requests
from base64 import b64decode
from Crypto.Hash import SHA256
import json

PoWNDigits = 2

maxNTransactions = 3

class block():
    def __init__(self, lastBlockHash, transactionList):
        self.lastBlockHash = lastBlockHash
        self.transactionList = transactionList
        self.proofOfWork = 0

    def toString(self):
        transactionString = [transaction.toString() for transaction in self.transactionList]
        return json.dumps({ "lastBlock" : self.lastBlockHash.hexdigest(), "transactions" : transactionString, "PoW" : self.proofOfWork })

    def getBlockHash(self):
        return SHA256.new(self.toString().encode("utf-8"))

    def verifyTransactions(self):
        for transaction in self.transactionList:
            if not transaction.verify():
                return self.transactionList.index(transaction)

        return -1

    def calculatePoW(self):
        for i in range(1, 100000000):
            self.proofOfWork = i
            if self.verifyPoW():
                return True

        return False

    def verifyPoW(self):
        if self.getBlockHash().hexdigest()[:PoWNDigits] == "0" * PoWNDigits:
            return True
        else:
            return False

    def appendTransaction(self, transaction):
        if len(self.transactionList) > maxNTransactions:
            return 1
        if transaction.verify():
            self.transactionList.append(transaction)
            if len(self.transactionList) < maxNTransactions:
                return 0
            else:
                return 1
        else:
            return 2
