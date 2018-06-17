from block_viewer import read
from block_viewer import Block

def test_block_parser():
    binary_data = read('tests/fixtures/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.bin')
    bitcoin_block = Block().parse_from_binary(binary_data)

    assert bitcoin_block.magic_number == 3652501241 
    assert bitcoin_block.tx_counter == 1031 
