from .block import Block
from .transaction import Transaction

from datetime import datetime


class Blockchain:
    '''
    A chain of blocks
    '''
    def __init__(self):
        self.genesis_block = self.create_genesis_block()
        self.chain = [self.genesis_block]

    # genesis block
    def create_genesis_block(self):
        '''
        Blockchain is a chain.
        So it must have started from the element in index 0. Hence, genesis block.
        Modern versions of cryptocurrency number it block 0, 
        but very early versions numbered it block1.
        '''
        raw_tx_list = []
        hashed_tx_list = []
        for each_tx in range(7):
            new_tx = Transaction(each_tx,
                                 '0217',
                                 datetime.now(),
                                 'tx ' + str(each_tx))
            raw_tx_list.append(new_tx)
            hashed_tx_list.append(new_tx.hash_tx())
        block = Block(hashed_tx_list, raw_tx_list)
        block.attaching_markle_root_to_tx()
        return block

    def add_block(self, block):
        self.chain.append(block)

    def __repr__(self):
        return ("\nThis blockchain has the genesis block with markle root of: \n" +
                str(self.genesis_block))
