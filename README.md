Bitcoin block viewer
===

## Installing
```python
python setup install
```

* https://webbtc.com/api/block

## block header
Version	Block version number	You upgrade the software and it specifies a new version	4
hashPrevBlock	256-bit hash of the previous block header	A new block comes in	32
hashMerkleRoot	256-bit hash based on all of the transactions in the block	A transaction is accepted	32
Time	Current timestamp as seconds since 1970-01-01T00:00 UTC	Every few seconds	4
Bits	Current target in compact format	The difficulty is adjusted	4
Nonce	32-bit number (starts at 0)	A hash is tried (increments)	4

https://webbtc.com/block/000000000000000001f942eb4bfa0aeccb6a14c268f4c72d5fff17270da771b9.json

https://webbtc.com/api/tx

https://en.bitcoin.it/wiki/Block
https://en.bitcoin.it/wiki/Transaction
https://en.bitcoin.it/wiki/Script#Constants
https://github.com/alecalve/python-bitcoin-blockchain-parser/blob/a2c7b50ec0e83bd5460e994272df3d9a283d3f08/blockchain_parser/utils.py
