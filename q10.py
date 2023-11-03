#List Operations(length, append, insert)
list=[]
print(type(list))
print("The initial list: ",list)
list.append(1)
list.append(2)
list.append(3)
print("List after adding elements using append operation: ", list)
list2=[23,"Apple",4.5,"Banana"]
print("Intial list: ", list2)
list2.insert(2,90)
print("List after adding new element after using insert function", list2)
print(len(list))
print(len(list2))