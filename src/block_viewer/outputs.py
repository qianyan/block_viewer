from block_viewer.utils import decode_uint64
from block_viewer.utils import decode_varint
from block_viewer.script import Script
from binascii import b2a_hex


class Output(object):
    def __init__(self,
                 value=None,
                 txout_script_length=None,
                 script_pubkey=None):

        self.value = value
        self.txout_script_length = txout_script_length
        self.script_pubkey = script_pubkey

    def parse_from_binary(self, output_data):
        offset = 8
        self.value = decode_uint64(output_data[:offset])
        self.txout_script_length, varint_size = decode_varint(output_data[8:])
        offset += varint_size
        script = Script().parse_from_binary(output_data[offset:offset+self.txout_script_length])
        operations = list(script)
        parts = []
        for operation in operations:
            if isinstance(operation, bytes):
                parts.append(b2a_hex(operation).decode("ascii"))
            else:
                parts.append(str(operation))

        self.script_pubkey = " ".join(parts)

        offset += self.txout_script_length
        self.size = offset
        return self

    def __repr__(self):
        return '<value: {value}, \n' \
            'txout_script_length: {txout_script_length}, \n' \
            'script_pubkey: {script_pubkey}>'.format(value=self.value,
                                                     txout_script_length=self.txout_script_length,
                                                     script_pubkey=self.script_pubkey)
