from sympy import *
print("Enter value: ")
inp=tuple(map(int,input().split()))
c=0
for i in range(len(inp)):
    if(isprime(inp[i])):
       c=c+1
    if(c==2):
       break
if(c==2):
    print("index for second prime is: ",i)
