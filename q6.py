#Use of membership operator
# in , not in 

list1=[1,2,3,4]
list2=[2,6,7,8]
for item in list1:
    if item in list2:
        print("The item is in the both the list")
    else:
        print("The item is not in the list")