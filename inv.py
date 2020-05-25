# 返回三元组(d,x,y)
# 其中d是gcd（a,b)
# 并且返回一组解使得 ax + by = d
def egcd(a,b):
    if b==0:
        return a,1,0
    [d,y,x] = egcd(b,a%b)
    return d,x,y-x*(a//b)

def inv(a,n):
    [d,x,_] = egcd(a,n)
    if d!=1: return -1
    return x % n

n = 10004
print(43 * inv(43,n) % n)