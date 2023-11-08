#Python program to print a inverse pyramid with numbers

row = int(input("Enter the number of rows: "))

for i in range(row, 0,-1):
    for j in range(row-i):
        print(" ",end=" ")
    
    count = 0
    while count < (2 * i - 1):
        if count < i:
            print(i - count, end=" ")
        else:
            print(i - 2 * i + 2 + count, end=" ")
        count += 1
    
    print("\r")

