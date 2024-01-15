def check(n):
    res = 0
    for x in str(n):
        res+= pow(int(x),5)
    return res==n

ans = 0
for i in range(2,1000000):
    if check(i):
        print(i)
        ans+=i
print(ans)