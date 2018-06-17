from utils import decode_varint
from block_header import BlockHeader
from transaction import Transaction

class Block(object):
    def __init__(self, magic_number=0xD9B4BEF9, block_size=None, block_header=None, tx_counter=None, txs=None):
        self.magic_number = magic_number
        self.block_size = block_size
        self.block_header = block_header
        self.tx_counter = tx_counter
        self.txs = txs or []

    def parse_from_binary(self, block_data):
        block_header_size = 80
        offset = block_header_size
        self.block_header = BlockHeader().parse_from_binary(block_data[:offset])

        self.tx_counter, varint_size = decode_varint(block_data[offset:])
        offset += varint_size

        for i in range(1):
            tx = Transaction().parse_from_binary(block_data[offset:])
            self.txs.append(tx)
            offset += tx.size

        return self
