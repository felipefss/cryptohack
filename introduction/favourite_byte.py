from Crypto.Util.number import *

# flag = byte ^ data
data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data_b = bytes.fromhex(data)
data_int = bytes_to_long(data_b)


def xor(toBeXord, secret):
    data_xord = [chr(b ^ secret) for b in toBeXord]
    return "".join(data_xord)


s = b"crypto{0x10_15_my_f4v0ur173_by7e}"

match = b'crypto{'

# Find secret byte
x = [(data_b[i] ^ match[i]) for i in range(len(match))]
print(x)

# print(xor(data_b, 0x10))
