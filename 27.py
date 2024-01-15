# Author: rishabhxchoudhary
# Created: 15.01.2024 12:22:43 (GMT+5:30)

# n^2 + an + b 
# |a| < 1000 and |b| < 1000

# for n=0: b is prime
# b  = [2,3,5,7,11...] all primes till 1000
# a = [-999, 999]

check = [True for i in range(1001)]
p = set()
for i in range(2,1001):
    if check[i]:
        p.add(i)
        for j in range(2*i,1001,i):
            check[j] = False

max_n = 0
max_a = 0
max_b = 0
for b in p:
    for a in range(-999,1000):
        n = 0
        while True:
            if (n*n + a*n + b) not in p:
                break
            n+=1
        if n>max_n:
            max_n = n
            max_a = a
            max_b = b
print(max_a*max_b)