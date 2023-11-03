#Set - collection of numerical data. { }, unordered, mutable, doesn't allow duplicates, heterogenous

set = {70, 12, 40, 23}
print(set)

#access elements

print(12 in set)
 
#add elements

set.add(100)
print(set)

#remove elements

set.remove(100)
print(set)

#update set

s1={40,87,98}
s2={76,51,89}
s1.update(s2)
print(s1)