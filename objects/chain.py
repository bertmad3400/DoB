class chain():
    def __init__(self, firstBlock):
        if firstBlock.verifyTransactions() == -1 and firstBlock.verifyPoW():
            self.blockchain = [firstBlock]
            return None
        else:
            return False
