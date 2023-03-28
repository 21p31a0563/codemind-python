n=int(input())
for i in range(n,0,-1):
    a=""
    for j in range(1,i+1):
        a=a+str(j)
    print(a)