from utils import decode_uint64
from utils import decode_varint

class Output(object):
    def __init__(self, value=None, txout_script_length=None, script_pubkey=None):
        self.value = value
        self.txout_script_length = txout_script_length
        self.script_pubkey = script_pubkey

    def parse_from_binary(self, output_data):
        offset = 8
        self.value = decode_uint64(output_data[:offset])
        self.txout_script_length, varint_size = decode_varint(output_data[8:])
        offset += varint_size
        self.script_pubkey = "TODO"

        offset += self.txout_script_length
        self.size = offset
        return self
