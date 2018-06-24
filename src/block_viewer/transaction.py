from block_viewer.utils import decode_uint32
from block_viewer.utils import decode_varint
from block_viewer.inputs import Input
from block_viewer.outputs import Output

class Transaction(object):
    def __init__(self,
                 version_no=None,
                 in_counter=None,
                 inputs=None,
                 out_counter=None,
                 outputs=None,
                 lock_time=None):

        self.version_no = version_no
        self.in_counter = in_counter
        self.inputs = inputs or []
        self.out_counter = out_counter
        self.outputs = outputs or []
        self.lock_time = lock_time
        self.size = 0

    def parse_from_binary(self, tx_data):
        offset = 4
        self.version_no = decode_uint32(tx_data[:offset])
        self.in_counter, varint_size = decode_varint(tx_data[offset:])
        offset += varint_size

        for i in range(self.in_counter):
            the_input = Input().parse_from_binary(tx_data[offset:])
            self.inputs.append(the_input)
            offset += the_input.size

        self.out_counter, varint_size = decode_varint(tx_data[offset:])
        offset += varint_size

        for i in range(self.out_counter):
            the_output = Output().parse_from_binary(tx_data[offset:])
            self.outputs.append(the_output)
            offset += the_output.size

        self.lock_time = decode_uint32(tx_data[offset:offset+4])
        self.size = offset + 4
        
        return self

    def __repr__(self):
        return '<version_no: {version_no}, \n' \
            'in_counter: {in_counter}, \n' \
            'inputs: {inputs}, \n' \
            'out_counter: {out_counter}, \n' \
            'outputs: {outputs}, \n' \
            'lock_time: {lock_time}>\n\n'.format(version_no=self.version_no,
                                               in_counter=self.in_counter,
                                               inputs=self.inputs,
                                               out_counter=self.out_counter,
                                               outputs=self.outputs,
                                               lock_time=self.lock_time)
