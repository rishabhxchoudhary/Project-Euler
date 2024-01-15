# p should be coprime to 10
# length of repeating decimal expansion of 1/p is order of 10 % p
# read: https://en.wikipedia.org/wiki/Cyclic_number

def order(b,p):
    b = b%p
    r = b
    o = 1
    while (r!=1):
        r = (r*b)%p
        o+=1
    return o

N = 1000
max_O = 0
max_i = 0
for i in range(2,1000):
    if i%2==0 or i%5==0: continue
    o = order(10,i)
    if (o>max_O):
        max_O = o
        max_i = i
print(max_i)