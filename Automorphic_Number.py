n=int(input())
s=n**2
dc=0
t=n
while n>0:
    n=n//10
    dc+=1
x=s%10**dc
if x==t: 
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")