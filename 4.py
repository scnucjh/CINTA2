for i in range(1,100):
    f = 1
    for j in range(1,i):
        f = f*j % i
    print(i,f)