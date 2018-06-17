from block_viewer import read
from block_viewer import BlockHeader
    
def test_block_header_parser():
    binary_data = read('tests/fixtures/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.bin')
    block_header = BlockHeader().parse_from_binary(binary_data[:80])

    assert block_header.version == 2
    assert block_header.hash_previous_block == '00000000000000000a3ed9a4e25407518aa854f09fa1981adaae9455a91d1966'
    assert block_header.hash_merkle_root == '9b7d5896398581a7ff26be4b3684ddd95a7c1dc1aab1df37cbb2127379ae8584'
    assert block_header.time == 1432723472
    assert block_header.bits == 404129525
    assert block_header.nonce == 226994584
    
