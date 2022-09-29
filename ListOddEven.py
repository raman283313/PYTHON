'''list=[0,2,32,5,351,35,36]
even=0
odd=0
for i in list:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Total number of even is ",even,"and Odd is",odd)
'''


list=[1,2,32,5,351,35,36]
even=0
odd=0
evenLs=[]
oddLs=[]
for i in list:
    if(i%2==0):
        evenLs.append(i)
       # print("Even number is ",i)
        even=even+1
    else:
        #print("Odd Number is ",i)
        oddLs.append(i)
        odd=odd+1
print("These are the even number present in list",evenLs)
print("These are the odd number present in list",oddLs)

print("Total number of even is ",even,"and Odd is",odd)

'''list=[1,2,32,5,351,35,36]
even=0
odd=0
#evenLs=[]
#oddLs=[]
for i in list:
    if(i%2==0):
        #evenLs.append(i)
        print("Even number is ",i)
        even=even+1
    else:
        print("Odd Number is ",i)
        #oddLs.append(i)
        odd=odd+1
#print("These are the even number present in list",evenLs)
#print("These are the odd number present in list",oddLs)

print("Total number of even is ",even,"and Odd is",odd)'''












