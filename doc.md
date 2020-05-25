# CINTA作业二，编程（求乘法逆元）、找规律

## 1、写Python（或Sage程序）的求乘法逆元的函数，输入a和n，求a'，使得a a' = 1 (mod n)。要求：如果无解，请给出无解提示；输出必须是正数。

有且当且仅当$gcd(a,m)=1$

求逆元可以借助扩展欧几里得算法。输入a和m之后,利用扩展欧几里得算法，可以求得一组（x,y)，满足：
$$ ax + yn = 1 $$

这样， ax在模m下面等于1， 于是，x就是a的逆元。 

注意，扩展欧几里得算法求得的x有可能是负数，要将x取模.

代码如下：

```python
def egcd(a,b):
    if b==0:
        return a,1,0
    [d,y,x] = egcd(b,a%b)
    return d,x,y-x*(a//b)

def inv(a,n):
    [d,x,_] = egcd(a,n)
    if d!=1: return -1
    return x % n
```

另外，当n是素数是，也可以考虑使用费马小定理和快速幂次运算，求得：

$$ a^{n-2} \mod n $$

## 2、编写C语言程序完成模指数运算，即给定整数x，y和m为输入，计算并返回值x^y mod m。


有递归与非递归两种方法。

非递归的方法基于将y拆分成2的幂次之和。

他们的时间复杂度均为$O(log y)$

代码如下：
```c
int mod_pow(int x,int y,int m) {
    if(y==0) return 1;
    int a = mod_pow(x,y>>1,m);
    int res = 1ll * a * a % m;
    if(y&1) res = res * x % m;
    return res;
}

int mod_pow2(int x,int y,int m) {
    int res = 1;
    while(y) {
        if(y&1) res = 1ll * res * x % m;
        x = 1ll * x * x % m;
        y>>=1;
    }
    return res;
}
```

## 3、编写一个Python程序求解以下同余方程： a x = b (mod m)，即给定整数a，b和m作为输入，返回所有满足方程的解x，或者给出无解告警。

要求解方程
$$ a x = b (mod m) $$
既要求得一个x，满足
$$ ax + my = b $$
设$gcd(a,m) = d$，可以看出，有解当且仅当
$$ d | b  $$
所以不妨先解
$$ ax + my = d $$
最后再将方程两边同时乘上$\frac{b}{d}$，就能得到
$$ ax + my = b $$
的一组解。

而右手边是b时，恰好是扩展欧几里得问题。

问题转化成了，求不定方程：
$$ ax + my = b  $$
的所有解。

不过不用担心会有无数个解，因为解必须在$[0,m-1]$的范围内。

扩展欧几里得算法只能求出一组解，不过不用担心，根据《A friend Introduction to Number Theory》第6章定理6.1，求出一组解$(x_1,y_1)$之后，所有解都能表示成
$$ (  x_1 + k \frac{m}{b}, y_1 - k \frac{a}{b} ) $$

这样，做法就是：

1. 判断是否$d | b$，是继续，否则无解
2. $ax + my = b$的一组解$(x_1,y_1)$
3. 利用上述定理求出所有解（出现当前解已经在答案的集合中时，终止）
4. 对求出来的所有解在模m下乘上$\frac{b}{d}$

```python
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
```


## 4、设p是素数，计算(p-1)! (mod p），找出规律，写成定理，并给出证明。设n是合数，计算(n-1)! (mod n），找出规律，写成定理，并给出证明。提示：可以编程找规律。

先写程序来找规律：

```python
for i in range(1,100):
    f = 1
    for j in range(1,i):
        f = f*j % i
    print(i,f)
```
不难发现，在模素数下，
$$ (p-1)! \equiv -1  (\bmod p)$$

而模合数下，除了$3! \equiv 2  ( \bmod 4)$外，其余有:

$$ (m-1)! \equiv 0  (\bmod m)$$

下面给出证明：

先证明模数是素数p时：这其实是著名的威尔逊定理

p = 2,3时显然，下面考虑$p\geq 5$

考虑平方剩余问题：
$$ x^2 \equiv 1 （\bmod p) $$
由模p多项式根定理，解的个数为至多为2。

并且我们恰好找到了两个解1和p-1.

所以，对于$2 \cdots p-2$，必然有偶数个数,因为$p\geq 5$的素数是奇数

于是，$1 \cdot 2 \cdot 3 \cdots p-1$中，从$2 \cdots p-2$的每个数i，必然有唯一一个逆元j使得$ij \equiv 1 (mod p)$，并且$i \neq j$，否则违反模p多项式根定理。

这样，这些数可以两两配对都等于1，最后剩下1和p-1.

故
$$ (p-1)! \equiv 1 \cdot (p-1) \equiv -1  (\bmod p)$$


下证模数是合数时的情况：

m = 4时，$3! \equiv 2  ( \bmod 4)$显然。

下证$m\geq 6$时，

$$ (m-1)! \equiv 0  (\bmod m)$$

这里，我们再分两种情况：

情况1，m是某个素数的平方：

那么这时，$(m-1)!$包含p和2p，这里$2p \leq m-1$，是因为如若不然，有$2p \geq m$,推导出$p \geq \frac{m}{2}$,于是$\sqrt{m} \geq  \frac{m}{2}$，由函数关系知道$m\geq 6$时，这是不可能的。

于是，$m | (m-1)!$

情况2，m不是某个素数的平方：

这种情况更为简单，m必然可以写成两个不相同的大于1的数的乘积，$m = ab$，a和b都是小于m的，这样,必有 $m | (m-1)!$.

所以，两种情况都有
$$ (m-1)! \equiv 0  (\bmod m)$$
QED.