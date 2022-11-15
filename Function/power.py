def power(a, b):
    t = 1
    while b > 0:
        if b & 1:
            t *= a
        b = b >> 1
        a *= a
    return t


print(power(2, 10))
