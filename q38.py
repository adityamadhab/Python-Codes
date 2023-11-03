#inheritance part 2

class person: 
    def __init__(self,name,age):
        self.name =  name
        self.age =  age
    def printname(self): 
        print(self.name,self.age)

class child(person) :
    pass

x = child("John",37)
x.printname()