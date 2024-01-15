def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def check(a,b):
    if a%10 == 0 or b%10 == 0:
        return False
    if a%11 == 0 or b%11 == 0:
        return False
    a = str(a)
    b = str(b)
    if a[0] == b[0]:
        return int(a[1])/int(b[1]) == int(a)/int(b)
    elif a[0] == b[1]:
        return int(a[1])/int(b[0]) == int(a)/int(b)
    elif a[1] == b[0]:
        return int(a[0])/int(b[1]) == int(a)/int(b)
    elif a[1] == b[1]:
        return int(a[0])/int(b[0]) == int(a)/int(b)
    else:
        return False

x = 1
y = 1
for num in range(10,100):
    for den in range(num+1,100):
        if check(num,den):
            print(num,den)
            x*=num
            y*=den

g = gcd(x,y)
print(y//g)