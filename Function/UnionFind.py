UF = {}


def find(x):
    if x != UF.setdefault(x, x):
        UF[x] = find(UF[x])
    return UF[x]


def union(x, y):
    UF[find(x)] = find(y)


union(1, 2)
union(2, 3)
union(4, 5)
union(6, 7)
union(5, 6)
print(find(3), find(7))
union(3, 7)
print(find(3), find(7))
