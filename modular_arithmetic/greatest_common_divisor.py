def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(66528, 52920))
print(gcd(15, 26))
