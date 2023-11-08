#Program to print inverted right angle triangle with numbers

r = int(input("Enter the no. of rows: "))

for i in range(r+1,0,-1) :
    for j in range(1,i+1):
        print(j, end=" ")
    print("\r")
