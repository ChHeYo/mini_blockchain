from hashlib import sha256


class Block:
    '''
    A block is made up of txs.
    A block in bitcoin blockchain can have as many txs as a miner wishes.
    '''
    def __init__(self, txlist, raw_txlist):
        self.markle_root = self.find_merkle_root(txlist)
        self.raw_txlist = raw_txlist

    def find_merkle_root(self, txlist):
        '''
        recursively hash nodes in order to
        return merkle root of a block
        '''
        if len(txlist) == 1:
            return txlist[0]
        combinedHash = []
        for i in range(0, len(txlist)-1, 2):
            # get two nodes, combine and hash the two together
            combinedHash.append(combine_two_nodes(txlist[i], txlist[i+1]))
        if len(txlist) % 2 != 0:
            combinedHash.append(combine_two_nodes(txlist[-1], txlist[-1]))
        return self.find_merkle_root(combinedHash)

    def attaching_markle_root_to_tx(self):
        for each_tx in self.raw_txlist:
            each_tx.add_markle_root(self.markle_root)

    def __repr__(self):
        return self.markle_root


def combine_two_nodes(node_a, node_b):
    hash_two = sha256()
    concat_two = (str(node_a) + str(node_b)).encode('utf8')
    hash_two.update(concat_two)
    return hash_two.hexdigest()
    