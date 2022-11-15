"""
suffix array for string => a b a a b a b a a b
                     is => 0 0 1 1 2 3 2 3 4 5
"""
txt = input()
n = len(txt)
pattern = input()
m = len(pattern)
sa = [0] * m  # suffix array
j, i = 0, 1  # two pointers for comparisons
while i < m:  # for traversing pattern
    if pattern[i] == pattern[j]:
        j += 1  # increment j
        sa[i] = j  # at index i we store the number of characters matches
        # here we use incremented j because index start at 0
        i += 1  # increment i
    else:
        if j == 0:  # if the character at index i didn't matches with the first index of pattern
            # then there is no prefix for that character in the pattern
            sa[i] = 0  # so we store 0 at index i of suffix array
            i += 1  # increment i and keep j = 0
        else:
            j = sa[j - 1]
flag = 1
p, q = 0, 0
while p < n:
    if txt[p] == pattern[q]:
        p += 1
        q += 1
    else:
        if q == 0:
            p += 1
        else:
            q = sa[q - 1]
    if q == m:
        print("Pattern found at index:", p - q)
        flag = 0
        q = sa[q - 1]
if flag:
    print("Pattern not found")
