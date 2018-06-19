import struct
from binascii import hexlify

def decode_varint(data):
    assert(len(data) > 0)
    size = int(data[0])
    assert(size <= 255)

    if size < 253:
        return size, 1

    if size == 253:
        format_ = '<H'
    elif size == 254:
        format_ = '<I'
    elif size == 255:
        format_ = '<Q'
    else:
        assert 0, "unknown format_ for size : %s" % size

    size = struct.calcsize(format_)
    return struct.unpack(format_, data[1:size+1])[0], size + 1

def decode_uint32(data):
    assert(len(data) == 4)
    return struct.unpack("<I", data)[0]

def format_hash(data):
    return str(hexlify(data[::-1]).decode('utf-8'))

def decode_uint64(data):
    assert(len(data) == 8)
    return struct.unpack("<Q", data)[0]
