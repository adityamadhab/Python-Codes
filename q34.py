#Python program to find the summation of first 10 numbers in a list

list=[1,2,3,4,5,6,7,8,9,10,11,12,1,3,14,15]
sum=0
for i in range(10):
    sum += list[i]
print(sum)