from block_viewer.utils import decode_varint
from block_viewer.block_header import BlockHeader
from block_viewer.transaction import Transaction

class Block(object):
    def __init__(self, magic_number=0xD9B4BEF9, block_size=None, block_header=None, tx_counter=None, txs=None):
        self.magic_number = magic_number
        self.block_size = block_size
        self.block_header = block_header
        self.tx_counter = tx_counter
        self.txs = txs or []

    def parse_from_binary(self, block_data, top=5):
        block_header_size = 80
        offset = block_header_size
        self.block_header = BlockHeader().parse_from_binary(block_data[:offset])

        self.tx_counter, varint_size = decode_varint(block_data[offset:])
        offset += varint_size

        if(top >= self.tx_counter): 
            top = self.tx_counter

        for i in range(top):
            tx = Transaction().parse_from_binary(block_data[offset:])
            self.txs.append(tx)
            offset += tx.size

        return self

    def __repr__(self):
        return '<magic_number: {magic_number}, \n' \
            'block_size: {block_size}, \n' \
            'block_header: {block_header}, \n' \
            'tx_counter: {tx_counter}, \n' \
            'txs: {txs}>'.format(magic_number=self.magic_number,
                                 block_size = self.block_size,
                                 block_header = self.block_header,
                                 tx_counter = self.tx_counter,
                                 txs = self.txs)
