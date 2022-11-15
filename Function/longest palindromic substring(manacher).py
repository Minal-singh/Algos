s = input()
# as manacher algoritm only covers odd length pallindromes
# convert the string by inserting special character that didn't appeared in string ('$' in this case)
# to cover both even and odd length palindromes
# for example:- 'aba' = '$a$b$a$' palindrome at center b
# radius of palindrome:- 0103010  => longest length = 3
# and for even:- 'abba' = '$a$b$b$a$' palindrome at center $
# radius of palindrome:-   010141010  => longest length = 4
s = "$" + "$".join(s) + "$"
n = len(s)
# array to store radius at every index of string
p = [0] * n
p[0] = 0
# as first character of string is always palindrome of length 1
p[1] = 1
# center,left boundary and right boundary respectively of palindrome till last character checked
# currently center is 1 beacuse only first character checked till now
# left and right boundary are 0 and 2 respectively because neighbours are always special characters and same
c, l, r = 1, 0, 2
for i in range(2, n):
    # Case 1:- when the character is outside the right boundary of checked palindromes
    if i > r:
        # make new character center and it's neighbours left and right boundary
        c = i
        r = c + 1
        l = c - 1
        # check for palindrome around center c
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
            p[i] += 1
        # undo last increment/decrement which fails while loop condition
        r -= 1
        l += 1
    else:
        # m is mirror index
        # for example:- 'abcbad'
        #               ^ | ^
        # index 0 is mirror index of index 4 when center is at index 2
        # while i is 0 m is 4 and viceversa
        m = 2 * c - i  # c-(i-c)  ->  2-(4-2)  ->  2*2-4  ->  0
        # Case 2:- if mirror palindrome(p[m]) is inside left boundary(l) then palindrome at i(p[i]) will be same
        if m - p[m] > l:
            p[i] = p[m]
        # Case 3:- if mirror palindrome(p[m]) touches left boundary(l) then palindrome at i(p[i]) will be
        # minimum p[m] and extend can further
        elif m - p[m] == l:
            # tr,tc and tl are temporary right,center and left respectively to check if palindrome at i crosses right boundary
            tr = r + 1
            tc = i
            tl = 2 * tc - tr
            p[i] = p[m]  # minimum of p[i] is p[m] as we already checked till right boundary
            while tl >= 0 and tr < n and s[tl] == s[tr]:
                tl -= 1
                tr += 1
                p[i] += 1
            # if palindrome crosses right boundary we update center,right and left boundary
            if tr > r + 1:
                c = tc
                r = tr - 1  # to undo last increment which fails while condition
                l = tl + 1  # to undo last decrement which fails while condition
        else:
            # Case 4:- if mirror palindrome(p[m]) crosses left boundary(l) then palindome at i(p[i])
            # will only be till right boundary(r) oterwise center palindrome would have been extended further
            p[i] = r - i
    # if any palindrome reaches last element of the string, no need to check further as all palindrome after
    # will be of smaller length
    if r == n - 1:
        break
# extracting answer from p array
x = 0
y = 0
for i in range(r + 1):
    if p[i] > x:
        x = p[i]
        y = i
# for max palindrome length
print(x)
# for max palindrome
print(s[y - x + 1: y + x: 2])

"""Time complexity -> O(n)
   Space complexity -> O(n)"""
