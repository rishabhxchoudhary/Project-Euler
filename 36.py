def check(n):
    x = str(n)
    y = bin(n)[2:]
    if x[::-1]=='0':
        return False
    if y[-1]=='0': return False
    if (x)==x[::-1] and (y)==(y[::-1]):
        return True
    return False
c = 0
for i in range(1,1000000):
    if check(i):
        c+=i
print(c)