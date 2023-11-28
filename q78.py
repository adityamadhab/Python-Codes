#Overloading: When two or methods are with the same name but assign with different types of parameters or different number of 
#parameters. This method are called method overloading.
#Example

#Overriding : It is a feature of OOP where a sub class can provide the program or information already defined at parent class.
#It occurs when the classes are named similarly with different parametres remaining the same signature

class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Calculating area in the base class")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    # Method overriding
    def area(self):
        result = self.length * self.width
        print(f"Area of Rectangle: {result}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    # Method overriding
    def area(self):
        result = 3.14 * self.radius * self.radius
        print(f"Area of Circle: {result}")

# Method overloading (using default values)
def add_numbers(a, b=0, c=0):
    return a + b + c

if __name__ == "__main__":
    # Method overriding example
    rectangle = Rectangle(5, 10)
    rectangle.area()  # Calls overridden method in Rectangle class

    circle = Circle(7)
    circle.area()  # Calls overridden method in Circle class

    # Method overloading example
    result1 = add_numbers(1)
    result2 = add_numbers(1, 2)
    result3 = add_numbers(1, 2, 3)

    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print(f"Result 3: {result3}")
