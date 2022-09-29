'''write a program which accepts a sequence of comma-seperated numbers from user and generate a list and a tuple with those numbers
sample data: 3,5,7,23
output:
list:['3','5','7','23']
tuple:('3','5','7','23')
'''
values=input("Input some comma seperated numbers : ")
list=values.split(",")
tuple=tuple(list)
print('List :',list)
print('Tuple :',tuple)

