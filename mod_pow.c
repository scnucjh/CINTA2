#include <stdio.h>
#include <time.h>
#include <stdlib.h>

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

int main() {
    srand(time(NULL));
    for(int i=0;i<200;i++) {
        int a = rand() % 10000, b = rand() % 10000;
        int m = rand() % 10000;
        printf("%d %d\n",mod_pow(a,b,m),mod_pow2(a,b,m));
    }
}