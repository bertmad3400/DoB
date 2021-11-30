
class transaction():
    def __init__(self, username, cpr, politicalParty, fee, signature=None):
        self.username = username
        self.cpr = cpr
        self.fee = fee
        self.politicalParty = politicalParty
        self.signature = signature
