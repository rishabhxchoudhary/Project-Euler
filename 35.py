N = 999999
check = [True for i in range(N+1)]
p = set()
for i in range(2,N+1):
    if check[i]:
        p.add(i)
        for j in range(i,N+1,i):
            check[j] = False

def check2(x):
    y = str(x)
    for _ in range(len(y)):
        y = y[1:] + y[0]
        if int(y) not in p:
            return False
    return True

count = 0
for i in p:
    if i>1000000: continue
    if check2(i):
        count+=1
print(count)
