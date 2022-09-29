#It will execute TypeError only
a=[11,12,13,14,"HELLO",33,66]
try:
    for i in range(10):
        print("Value : ",a[i]/2)
except TypeError:
    print("Not a valid value.")
except IndexError:
    print("Not in valid range.")
print("Bye..")

'''
#It will execute all the Exception
a=[11,12,13,14,"HELLO",33,66]
for i in range(10):
    try:
        print("Value : ",a[i]/2)
    except TypeError:
        print("Not a valid value.")
    except IndexError:
        print("Not in valid range.")
print("Bye..")
'''
