from math import sqrt


def prime(n):
    seive = [int(i) for i in range(n + 1)]
    seive[0] = False
    seive[1] = False
    for i in range(4, n + 1, 2):
        seive[i] = False
    for i in range(3, int(sqrt(n)), 2):
        j = i * i
        while j < n + 1:
            seive[j] = False
            j += i
    for k in seive:
        if k:
            print(k)
        else:
            pass


prime(100)
