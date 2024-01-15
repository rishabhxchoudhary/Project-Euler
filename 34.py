memo = {}
def f(n):
    if n == 1 or n==0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n*f(n-1)
    return memo[n]

def check(n):
    s = 0
    for x in str(n):
        s+=f(int(x))
    return s == n

ans = 0
for i in range(3,1000000):
    if check(i):
        print(i)
        ans += i
print(ans)
