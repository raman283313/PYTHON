# write multiple inheritance program in python
class Parent:
    #def __init__(self, name ,age):
    def __init__(self):
        self.name=print("enter your name: ")
        self.age=int(print("Enter ur age: "))
    def display(self):
        print(self.name, self.age)
        
class child(Parent):
    def __init__(self,contact):
        self.contact=contact
        super.__init__()
    def show(self):
        print(self.contact)
        
obj=child(7545821890)
obj.display()
ohb.show()


