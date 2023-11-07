#Python program to print a pyramid with numbers

row = int(input("Enter the number of rows: "))

for i in range(0, row):
    for j in range(1, row - i):
        print(" ",end=" ")
    
    count = 0
    while count < (2 * i - 1):
        if count < i:
            print(i + count, end=" ")
        else:
            print(i + 2 * i - 2 - count, end=" ")
        count += 1
    
    print("\r")
