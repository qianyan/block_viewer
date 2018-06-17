Bitcoin block viewer
===

## Installing
```bash
python setup.py install
```

## Run tests
```bash
python setup.py test
```

## Run command line
```
python setup.py install
block_viewer 000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9
```
or
```
python src/block_viewer/cli.py 000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9
```

## References
### block 
| Field       | Description |  Size  | 
| --------    | :-----:  | :----:  |
| Magic no    |  value always 0xD9B4BEF9 |  4 bytes  | 
| Blocksize   | number of bytes following up to end of block |  4 bytes  | 
| Blockheader | consists of 6 items |  80 bytes  | 
| Transaction counter   | positive integer VI = VarInt |  1-9 bytes  | 
| transactions | the (non empty) list of transactions | \<Transaction counter>-many transactions  | 

https://en.bitcoin.it/wiki/Block

### block header
| Field       | Description |  Updated when...  |  Size |
| --------    | :-----:  | :----:  | :---: |
|  Version    | Block version number | You upgrade the software and it specifies a new version | 4 bytes |
| hashPrevBlock  | 256-bit hash of the previous block header	| A new block comes in | 32 bytes |
| hashMerkleRoot  | 256-bit hash based on all of the transactions in the block\<Paste> | A transaction is accepted  | 32 bytes |
| Time  | Current timestamp as seconds since 1970-01-01T00:00 UTC | Every few seconds | 4 bytes |
| Bits  | Current target in compact format | The difficulty is adjusted | 4 bytes |
| Nonce | 32-bit number (starts at 0) | A hash is tried (increments)    | 4 bytes |

https://en.bitcoin.it/wiki/Block_hashing_algorithm

### transaction
| Field       | Description |  Size  | 
| --------    | :-----:  | :----:  |
| Version no    |  currently 1 |  4 bytes  | 
| In-counter |  positive integer VI = VarInt |  1 - 9 bytes | 
| list of inputs | the first input of the first transaction is also called "coinbase" (its content was ignored in earlier versions)	 |  \<in-counter>-many inputs | 
| Out-counter |  positive integer VI = VarInt |  1 - 9 bytes | 
| list of outputs |  the outputs of the first transaction spend the mined bitcoins for the block | \<out-counter>-many outputs | 
| lock_time | if non-zero and sequence numbers are < 0xFFFFFFFF: block height or timestamp when transaction is final | 4 bytes|

https://en.bitcoin.it/wiki/Transaction

### inputs
| Field       | Description |  Size  | 
| --------    | :-----:  | :----:  |
| Previous Transaction hash | doubled SHA256-hashed of a (previous) to-be-used transaction |  32 bytes  | 
| Previous Txout-index | non negative integer indexing an output of the to-be-used transaction |  4 bytes  | 
| Txin-script length | non negative integer VI = VarInt |  1-9 bytes  | 
| Txin-script / scriptSig | Script |  \<in-script length>-many bytes | 
| sequence_no | normally 0xFFFFFFFF; irrelevant unless transaction's lock_time is > 0 |  4 bytes | 

https://en.bitcoin.it/wiki/Transaction#general_format_.28inside_a_block.29_of_each_input_of_a_transaction_-_Txin

### outputs
| Field       | Description |  Size  | 
| --------    | :-----:  | :----:  |
| value       | non negative integer giving the number of Satoshis(BTC/10^8) to be transfered | 8 bytes | 
| Txout-script length | non negative integer | 1 - 9 bytes VI = VarInt | 
| Txout-script / scriptPubKey | Script | \<out-script length>-many bytes | 

https://en.bitcoin.it/wiki/Transaction#general_format_.28inside_a_block.29_of_each_output_of_a_transaction_-_Txout

## webbtc api
### block 
https://webbtc.com/api/block
### fixtures (bin | json)
https://webbtc.com/block/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.bin
https://webbtc.com/block/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.json
