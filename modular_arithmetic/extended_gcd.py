q = []
p = [0, 1]
steps = 0


def gcd(a, b):
    steps = steps + 1
    # print(steps)

    if b == 0:
        return a
    q.append(int(a/b))

    return gcd(b, a % b)


def ext_gcd(n, x):
    gcd(n, x)

    for i in range(2, steps + 2):
        newP = p[i - 2] - p[i - 1] * (q[i - 2] % x)
        p.append(newP)


ext_gcd(15, 26)
print(p)
