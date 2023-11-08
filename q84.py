#Program to print inverted right angle triangle with stars

r = int(input("Enter the no. of rows: "))

for i in range(r+1,0,-1) :
    for j in range(1,i+1):
        print("*", end=" ")
    print("\r")

