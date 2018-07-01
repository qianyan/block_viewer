"""a viewer for bitcoin block structure including blockheaer, transactions etc.
  Usage:
    block_viewer <block_hash>
    block_viewer -h | --help | --version
"""
import requests
from block_viewer.binary_reader import read
from block_viewer.block import Block
from block_viewer.__version__ import __version__


def main():
    from docopt import docopt
    arguments = docopt(__doc__, version=__version__)
    block_hash = arguments['<block_hash>']
    if block_hash is not None:
        url = 'https://webbtc.com/block/{}.bin'.format(block_hash)
        target_file = '{}.bin'.format(block_hash)
        response = requests.get(url, stream=True)
        handle = open(target_file, "wb")
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)

        handle.close()

        bitcoin_block = Block().parse_from_binary(read(target_file))
        print(bitcoin_block)


if __name__ == "__main__":
    main()
