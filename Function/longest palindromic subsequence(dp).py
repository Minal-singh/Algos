s = input()
n = len(s)
dp = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    # for palindromes of length 1
    dp[i][i] = 1

# traversing only upper part of diagonal
for i in range(1, n):
    for j in range(n - i):
        if i == 1:
            if s[j] == s[j + i]:
                # for palindromes of length 2
                dp[j][j + i] = 2
        else:
            if s[j] == s[j + i]:
                # if characters are same max palindrome length between characters + 2(the current characters)
                dp[j][j + i] = dp[j + 1][j + i - 1] + 2
            else:
                # if characters are not same then take maximum of max palindrome length achieved by including only one of either characters
                dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1])
# the final maximum palindrome length in complete string(dp[0][n-1])
# if you want max palindrome length in string s[i:j](i included,j excluded)
# then print(dp[i][j])
print(dp[0][n - 1])

"""Time Complexity = O(n^2)
   Space Complexity = O(n^2)"""
