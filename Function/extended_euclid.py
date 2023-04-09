#extended euclid algorithm
def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x, y) = extended_euclid(b, a % b)
        return (d, y, x - (a // b) * y)

#main
a, b = map(int, input().split())
d, x, y = extended_euclid(a, b)
print(d, x, y)
