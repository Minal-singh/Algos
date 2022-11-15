def fact(n):
    ans = 1
    for h in range(1, n + 1):
        ans *= h
    return ans


t = input()
a = t[::]
a = list(a)
a = set(a)
a = list(a)
a.sort()
d = {}
j = 1
for i in a:
    d[i] = j
    j = j + 1
a = [d[i] for i in t]
print("a", a)
z = []
for i in a:
    c = 0
    for l in a[a.index(i) + 1 : :]:
        if i > l:
            c += 1
    z.append(c)
print("z", z)
d = []
b = []
for i in range(len(t) - 1, -1, -1):
    b.append(fact(i))
print("b", b)
for g in range(len(t)):
    s = b[g] * z[g]
    d.append(s)
print("d", d)
v = []
for i in range(len(a)):
    p = a[i::]
    c = []
    w = 1
    for k in p:
        e = p.count(k)
        p.remove(k)
        w = w * fact(e)
    v.append(w)
    a.insert(a.index(a[i]), "x")
    a.remove(a[i + 1])
print("v", v)
for i in range(len(v)):
    v[i] = d[i] / v[i]
print(sum(v) + 1)
