from utils import format_hash
from utils import decode_varint
from utils import decode_uint32

class Input(object):
    def __init__(self, previous_tx_hash=None, index=None, txin_script_length=None, script_sig=None, sequence_no=None):
        self.previous_tx_hash = previous_tx_hash
        self.index = index
        self.txin_script_length = txin_script_length
        self.script_sig = script_sig
        self.sequence_no = sequence_no
        self.size = 0

    def parse_from_binary(self, input_data):
        offset = 32
        self.previous_tx_hash = format_hash(input_data[:offset])
        self.index = decode_uint32(input_data[offset:offset + 4])
        offset += 4
        self.txin_script_length, varint_size = decode_varint(input_data[offset:])
        offset += varint_size
        self.script_sig = "TODO"

        offset += self.txin_script_length

        self.sequence_no = decode_uint32(input_data[offset:offset + 4])
        offset += 4
        self.size = offset
        return self