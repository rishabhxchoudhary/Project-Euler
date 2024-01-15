M = pow(10,10)
def binpow(a,b):
    res = 1
    while b:
        if b&1:
            res*=a
            res%=M
        a*=a
        a%=M
        b>>=1
    return res

ans = 0
for i in range(1,1001):
    ans = (ans + binpow(i,i))%M
print(ans)