def xor(string: str, number: int) -> int:
    int_list = [ord(s) for s in string]
    xord_list_converted = [chr(i ^ 13) for i in int_list]
    # transform it back to string
    return "".join(xord_list_converted)


msg = "label"
print(f'crypto{{{xor(msg, 13)}}}')
