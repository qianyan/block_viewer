from utils import decode_uint32
from utils import format_hash

class BlockHeader(object):
    def __init__(self, version=None, hash_previous_block=None, hash_merkle_root=None, time=None, bits=None, nonce=None):
        self.version = version
        self.hash_previous_block = hash_previous_block
        self.hash_merkle_root = hash_merkle_root
        self.time = time
        self.bits = bits
        self.nonce = nonce

    def parse_from_binary(self, binary_data):
        assert(len(binary_data) == 80)
        self.version = decode_uint32(binary_data[:4])
        self.hash_previous_block = format_hash(binary_data[4:36])
        self.hash_merkle_root = format_hash(binary_data[36:68])
        self.time = decode_uint32(binary_data[68:72])
        self.bits = decode_uint32(binary_data[72:76])
        self.nonce = decode_uint32(binary_data[76:80])
        return self
