from Crypto.Util.number import *

enc = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
enc_b = bytes.fromhex(enc)


def xor(toBeXord, secret):
    data_xord = [chr(b ^ secret) for b in toBeXord]
    return "".join(data_xord)


match = b'crypto{1'

# Find secret byte
x = [(enc_b[i] ^ match[i]) for i in range(len(match))]
k = bytes("".join([chr(s) for s in x]), 'utf8')

j = 0
i = 0
f = ''

while j < len(enc_b):
    x1 = enc_b[j] ^ k[i]
    f = f + chr(x1)

    j = j + 1
    i = j % len(k)


print(f)
