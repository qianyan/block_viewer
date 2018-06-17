import mmap

def read(binary_file):
     with open(binary_file, 'rb') as block_binary:
         return mmap.mmap(block_binary.fileno(), 0, prot=mmap.PROT_READ)

    
