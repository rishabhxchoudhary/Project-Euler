N = 999999
check = [True for i in range(N+1)]
p = set()
for i in range(2,N+1):
    if check[i]:
        p.add(i)
        for j in range(i,N+1,i):
            check[j] = False

def check2(n:int)->bool:
    s = str(n)
    for i in range(len(s)):
        if int(s[i:]) not in p:
            return False
    for i in range(1,len(s)):
        if int(s[:i]) not in p:
            return False
    return True

x = []

for i in p:
    if i not in [2,3,5,7]:
        if check2(i):
            x.append(i)
print(sum(x))
