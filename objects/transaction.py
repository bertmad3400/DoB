from Crypto.Hash import SHA256


class transaction():
    def __init__(self, username, cpr, politicalParty, signature=None):
        self.username = username
        self.cpr = cpr
        self.politicalParty = politicalParty
        self.signature = signature

    def calculateTransactionHash(self):
        transaction = self.username + self.cpr + self.politicalParty
        return SHA256.new(transaction.encode())
