#inheritance in python

class person: 
    def __init__(self,name,age):
        self.name =  name
        self.age =  age

p1 = person("John",35)
print(p1.name)
print(p1.age)

p1.name="Amit"
print(p1.name)
        
