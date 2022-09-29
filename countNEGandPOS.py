'''write a code to count total +ve and -ve enteries from a
    a)List
    b)tuple
'''

ls=[12,-34,65,52,-86]
l=len(ls)
tuple=(12,34,65,52,56)
pos=0
neg=0
p=0
n=0
for i in range(l):
    if(ls[i]<0):
        neg=neg+1
    else:
        pos=pos+1      
print("Total +ve number  in list is",pos," and negative is ",neg)

for j in range(len(tuple)):
     if(tuple[j]<0):
        n=n+1
     else:
        p=p+1
print("Total +ve number in tuple is",p," and negative is ",n)

''' write a program to asked value from user without for loop'''
'''write a code to check weather a string is palindrome or not '''

'''write a code to check weather a string is palindrome or not '''
