
class transaction():
    def __init__(self, username, cpr, politicalParty, signature=None):
        self.username = username
        self.cpr = cpr
        self.politicalParty = politicalParty
        self.signature = signature
