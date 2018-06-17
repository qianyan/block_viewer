from block_viewer import read
from block_viewer import Block

def test_block_parser():
    binary_data = read('tests/fixtures/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.bin')
    bitcoin_block = Block().parse_from_binary(binary_data)

    assert bitcoin_block.magic_number == 3652501241 
    assert bitcoin_block.tx_counter == 1031 

def test_block_header_parser():
    binary_data = read('tests/fixtures/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.bin')
    bitcoin_block = Block().parse_from_binary(binary_data)
    block_header = bitcoin_block.block_header

    assert block_header.version == 2
    assert block_header.hash_previous_block == '00000000000000000a3ed9a4e25407518aa854f09fa1981adaae9455a91d1966'
    assert block_header.hash_merkle_root == '9b7d5896398581a7ff26be4b3684ddd95a7c1dc1aab1df37cbb2127379ae8584'
    assert block_header.time == 1432723472
    assert block_header.bits == 404129525
    assert block_header.nonce == 226994584
    
def test_block_transactions_parser():
    binary_data = read('tests/fixtures/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.bin')
    bitcoin_block = Block().parse_from_binary(binary_data)

    coinbase = bitcoin_block.txs[0]

    assert coinbase.version_no == 1
    assert coinbase.in_counter == 1
    assert coinbase.out_counter == 1
    assert coinbase.inputs[0].previous_tx_hash == '0000000000000000000000000000000000000000000000000000000000000000' #coinbase
 

def test_block_transaction_inputs_and_outputs():
    binary_data = read('tests/fixtures/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.bin')
    bitcoin_block = Block().parse_from_binary(binary_data)

    tx = bitcoin_block.txs[1]
    inputs = tx.inputs
    outputs = tx.outputs

    assert inputs[0].previous_tx_hash == 'a59238577c596d2caa367c0855a76a75efcde6953186507fa51ee2dff3eb8b41'
    assert inputs[0].index == 1

    assert outputs[0].value == 10000000000
    assert outputs[1].value == 10000000000

