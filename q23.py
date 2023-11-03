#Loop: Loop are used to repeat the iteration of the elements present in list, tuples, set etc. and perform the same action for each entry
#For Loop: It is used for iterative over a squence(list, tuple, set, dictionary). This is an iterative method using for as a keyword used to execute a set of statements once for each item in it.

fruit=["apple","mango","orange"]

for x in fruit:
    print(x)

for y in "apple":
    print(y)

for x in range(2,30,2): # 2 is start, 30 is end, 2 is skip
    print(x)

#Nested for loop

color=["red","yellow","orange"]
fruits=["apple","mango","orange"]
for a in color:
    for b in fruits:
        print(a,b)


