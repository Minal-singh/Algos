UF = {}


def find(x):
    if x != UF[x]:
        UF[x] = find(UF[x])
    return UF[x]


def union(x, y):
    UF.setdefault(x, x)
    UF.setdefault(y, y)
    UF[find(x)] = find(y)


"""
# shorter version
def ffind(x):
    if x != UF.setdefault(x, x):
        UF[x] = ffind(UF[x])
    return UF[x]


# union function
UF[ffind(1)] = ffind(2)
"""


union(1, 2)
union(2, 3)
union(4, 5)
union(6, 7)
union(5, 6)
print(find(3), find(7))
union(3, 7)
print(find(3), find(7))
