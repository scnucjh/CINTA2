import random
def egcd(a,b):
    if b==0:
        return a,1,0
    [d,y,x] = egcd(b,a%b)
    return d,x,y-x*(a//b)

def inv(a,n):
    [d,x,_] = egcd(a,n)
    if d!=1: return -1
    return x % n

def solve(a,b,m):
    if a==b==0:
        print('任意解')
    if a==0 and b!=0:
        print('无解')
    if b==0:
        return [0]

    [d,x,_] = egcd(a,m)
    if b%d!=0:
        return '无解'

    t = b//d
    x = x % m
    res = [x]

    while True:
        x = x+m//d
        x_ = x % m
        if x_==res[0]: 
            for i in range(len(res)):
                res[i] = res[i] * t % m
            res = list(set(res))
            return res
        res.append(x_)

for k in range(100):
    m = random.randint(1,1000)
    a = random.randint(0,m-1)
    b = random.randint(0,m-1)

    
    print('(a,b,m) = ',a,b,m)
    x = solve(a,b,m)
    print('x = ',solve(a,b,m))

    # if x!='无解' and x!='任意解':
    #     for e in x:
    #         print(e*a%m==b)
