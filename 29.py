
def binpow(a,b):
    res = 1
    while b:
        if b&1:
            res*=a
        a*=a
        b>>=1
    return res

s = set()
for a in range(2,101):
    for b in range(2,101):
        s.add(binpow(a,b))
print(len(s))