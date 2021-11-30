from Crypto.PublicKey import RSA

class wallet():
    def __init__(self):
        privateKey = RSA.generate(2048)
        self.privateKey = privateKey.export_key('PEM')
        self.publicKey = privateKey.public_key().export_key('PEM')
