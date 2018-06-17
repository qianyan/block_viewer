import sys
import requests
from binary_reader import read
from block import Block

def main():
    if len(sys.argv) < 2:
        print "Usage: python block_viewer.py <block_hash>"
    else:
        url = 'https://webbtc.com/block/{block_hash}.bin'.format(block_hash=sys.argv[1])
        target_file = '{block_hash}.bin'.format(block_hash=sys.argv[1])
        response = requests.get(url, stream=True)
        handle = open(target_file, "wb")
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)
            
        bitcoin_block = Block().parse_from_binary(read(target_file))
        print bitcoin_block
      
if __name__ == "__main__":
    main()
