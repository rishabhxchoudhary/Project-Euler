coins = [1,2,5,10,20,50,100,200]
# let dp[i][j] = number of ways to make i using first j coins
# dp[i][j] = dp[i][j-1] + dp[i-coins[j]][j]

memo = {}
def dp(i,j):
    if (i,j) in memo: return memo[(i,j)]
    if i==len(coins):
        if j==0: return 1
        else: return 0
    if j<0: return 0
    memo[(i,j)] = dp(i+1,j) + dp(i,j-coins[i])
    return memo[(i,j)]

print(dp(0,200))
