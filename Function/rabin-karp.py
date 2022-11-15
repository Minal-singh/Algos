txt = input()
t = len(txt)
pattern = input()
l = len(pattern)
# If pattern length is greater than string
if l > t or l == 0 or t == 0:
    print("Not found")
# if pattern length is equal to string length
# don't need to build hash function just check letter by letter and raise error where letters don't match
elif l == t:
    i = 0
    while i < l:
        if txt[i] == pattern[i]:
            i += 1
        else:
            print("Not found")
            break
    # If all characters match
    if i == l:
        print("Pattern found at index: 0")
else:
    prime = 1000000007  # for mod answers so that they don't become too big
    domain = 256
    power = pow(domain, l - 1) % prime
    flag = 1  # If pattern not found in string
    n = 0  # hash value of pattern
    m = 0  # hash value of substring of length equal to pattern length
    for i in range(l):  # for calculating hash values
        n = (domain * n + ord(pattern[i])) % prime
        m = (domain * m + ord(txt[i])) % prime
    for i in range(t - l + 1):
        if n == m:  # if hash values matches
            c = 0
            for k in range(l):
                if pattern[k] == txt[i + k]:
                    c += 1
                else:
                    break
            if c == l:
                print("Pattern found at index:", i)
                flag = 0
        if i < (t - l):  # slide string window
            m = (m - (ord(txt[i]) * power)) % prime
            m = (domain * m + ord(txt[i + l])) % prime
    if flag:
        print("Not found")
