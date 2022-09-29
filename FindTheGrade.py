math=int(input("Enter math mark : "))
phy=int(input("Enter Physics mark : "))
com=int(input("Enter computer mark : "))
che=int(input("Enter chemistry mark : "))
eng=int(input("Enter English sub mark : "))
avg=(math+phy+com+che+eng)//5
if(avg>=90):
    print("Grade Outstanding ")   
elif(avg>=60) and (avg<90):
    print("Grade first ")
elif(avg>=50)and (avg<60):
    print("Grade second ")
elif(avg>=35)and (avg<50):
    print("Grade third ")
else:
    print("Grade Fail")
