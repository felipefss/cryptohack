import base64

encodedHex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

hexToBytes = bytes.fromhex(encodedHex)
b64 = base64.b64encode(hexToBytes)

print(b64)
