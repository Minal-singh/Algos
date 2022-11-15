def mod_power(a, b, m):
    t = 1
    while b > 0:
        if b & 1:
            t = (t * a) % m
        b = b >> 1
        a = (a * a) % m
    return t % m


m = 1000000007
print(mod_power(218, 10, m))
