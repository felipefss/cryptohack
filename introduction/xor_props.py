from Crypto.Util.number import *

k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
c = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
d = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1_int = bytes_to_long(bytes.fromhex(k1))
c_int = bytes_to_long(bytes.fromhex(c))
d_int = bytes_to_long(bytes.fromhex(d))

k1_xor_c = k1_int ^ c_int
flag = k1_xor_c ^ d_int

print(long_to_bytes(flag))
