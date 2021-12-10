class chain():
    def __init__(self, firstBlock):
        if firstBlock.verifyTransactions() == -1 and firstBlock.verifyPoW():
            self.blockchain = [firstBlock]
            return None
        else:
            return False

    def appendBlock(self, blockToAppend):
        print(blockToAppend.verifyTransactions() == -1, blockToAppend.verifyPoW(), blockToAppend.lastBlockHash.digest() == self.blockchain[-1].getBlockHash().digest())
        if blockToAppend.verifyTransactions() == -1 and blockToAppend.verifyPoW() and blockToAppend.lastBlockHash.digest() == self.blockchain[-1].getBlockHash().digest():
            self.blockchain.append(blockToAppend)
            return True
        else:
            return False

    def verifyChain(self):
        for blockNumber, block in enumerate(self.blockchain):
            if not (block.verifyTransactions() or block.verifyPoW()):
                return False
            if not blockNumber == 0:
                if not block.lastBlockHash.digest() == self.blockchain[blockNumber - 1].getBlockHash().digest():
                    return False

        return True

    def countVotes(self, partyList):
        votes = {}
        if self.verifyChain():
            for block in self.blockchain:
                for transaction in block.transactionList:
                    if transaction.politicalParty in partyList:
                        votes[transaction.cpr] = transaction.politicalParty

        return votes
