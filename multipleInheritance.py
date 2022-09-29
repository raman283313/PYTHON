
class General:
    def __init__(self,name,roll_no,adhar_no,mob_no):
        self.name=name
        self.roll=roll_no
        self.adhar=adhar_no
        self.mob=mob_no
    def display1(self):
        print(self.name,self.roll,self.adhar,self.mob)
       # print("Name is"+self.name,"Roll is " +self.roll,"Adhar no is "+self.adhar,"Mobile no "+self.mob)
class Academic(General):
    def __init__(self,cgpa1,cgpa2,cgpa3):
        super().__init__(self,name,roll_no,adhar_no,mob_no):
            self.Mcgpa=cgpa1
            self.Icgpa=cgpa2
            self.Hcgpa=cgpa3   
    def display2(self):
        print(self.Mcgpa,self.Icgpa,self.Hcgpa)
class Store(General):
    def __init__(self,Total_book,issueDate,returnDate,fine):
        self.tb=Total_book
        self.issueD=issueDate
        self.ret_Date=returnDate
        self.Tot_fine=fine
        
    def display3(self):
        print(self.tb,self.issueD,self.ret_Date,self.Tot_fine)
//gen=General('raman','b46',787938465873,7363984344)
//gen.display1()
//obj=General('Raman','b57','8584758895754',7654478674)
obj=Academic('6','6.5','8')
obj1=Academic()
obj1.General('Raman','b57','8584758895754',7654478674)
obj.display2()
obj.display1()






#ob=Academic('Raman','B12',225545467519,7545821890)
#ob.display1()

'''
class General:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
        print(f('name='{fname})


obj=General('raman','Hrishi')
obj.display()
'''
















        
    
