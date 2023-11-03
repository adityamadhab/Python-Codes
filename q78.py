#Overloading: When two or methods are with the same name but assign with different types of parameters or different number of parameters. This method are called method overloading.
#Example

#Overriding : It is a feature of OOP where a sub class can provide the program or information already defined at parent class.
#It occurs when the classes are named similarly with different parametres remaining the same signature

def add(a,b) : 
    return (a+b)

def add(a,b,c) :
    return (a+b+c)

print(add(4,5))