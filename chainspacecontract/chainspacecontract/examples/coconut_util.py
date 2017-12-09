from bplib.bp import G2Elem, G1Elem
from petlib.pack import encode, decode
from binascii import hexlify, unhexlify

def bn_pack(x):
    return hexlify(encode(x))

def bn_unpack(x):
    return decode(unhexlify(x))

def pack(elem):
	return hexlify(elem.export()).decode()

def unpackG1(params, elem):
	G = params[0]
	return G1Elem.from_bytes(unhexlify(elem.encode()), G)

def unpackG2(params, elem):
	G = params[0]
	return G2Elem.from_bytes(unhexlify(elem.encode()), G)

