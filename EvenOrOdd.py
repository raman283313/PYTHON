#write a program to check wheather given number is even or odd.
num=int(input("Enter a Number : "))
if(num%2==0 and num>=0):
    print(num," is +ve  Even")
elif(num%2==0 and num<0):
    print(num," is -ve Even")
elif(num%2!=0 and num>=0 ):
    print(num," is +ve odd")
else:     # elif(num%2!=0 and num<0 ):
    print(num," is -ve odd")



'''
if(num%2==0):
    if(n>=0):
        print("Even and +ve")
    else:
        print("Even and -ve")
else:
    if(n>=0)
        print("odd and +ve")
    else:
        print("Odd and -ve")'''


        
