#Program to print right angled triangle with numbers

r = int(input("Enter the no. of rows: "))

for i in range(1,r+1) :
    for j in range(1,i+1):
        print(j, end=" ")
    print("\r")