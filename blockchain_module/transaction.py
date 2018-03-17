# import sha256 as the whitepaper also uses sha256
from hashlib import sha256
from datetime import datetime


class Transaction:
    '''
    A transaction consists of the following:
    - index: index of a tx within the block
    - previous hash: previous tx that has been hashed
    - timestamp: when the tx was instantiated
    - data: any data regarding the tx
    '''
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        # store hash that will be used for creating next block
        self.hash = self.hash_tx()

    def concatenated_info(self):
        '''
        concatenating information to feed to hash function
        '''
        return (str(self.index) + str(self.previous_hash) +
                str(self.timestamp) + str(self.data)).encode('utf8')

    def hash_tx(self):
        # create a hash object
        hashed_info = sha256()
        # Update the hash object by feeding it
        hashed_info.update(self.concatenated_info())
        return hashed_info.hexdigest()

    def add_merkle_root(self, merkle_root):
        self.merkle_root = merkle_root

    def __repr__(self):
        return ('Transaction ' + str(self.index) + ': ' +
                '\n' + "Timestamp: " + str(self.timestamp) + '\n' + 
                "id: " + str(self.hash) + '\n')
