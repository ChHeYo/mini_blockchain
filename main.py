from blockchain_module.block import Block
from blockchain_module.transaction import Transaction
from blockchain_module.blockchain import Blockchain

if __name__ == "__main__":
    # starting blockchain
    blockchain = Blockchain()
    # show the blockchain's initial status
    print(blockchain)
    
    for block in blockchain.chain:
        print("\n** Transactions in the block: ")
        for tx in block.raw_txlist:
            print(tx)