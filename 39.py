import time
m = 0
ans = 0
t1 = time.time()
for p in range(1,1001):
    count = 0
    for a in range(1,p):
        for b in range(a+1,p):
            c = p - (a+b)
            if c<0: break
            if c*c == a*a + b*b:
                # print(a,b,c)
                count+=1
    if count>m:
        m = count
        ans = p
print(ans)
print("Executed in :", time.time()-t1," seconds")

# 840
# Executed in : 25.78894591331482 seconds