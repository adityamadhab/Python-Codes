#Converting the tuple to list and updating the elements

x = ("apple",80,70,"mango",21.8)
y = list(x)
y[1]=90
y[-2]="orange"
x = tuple(y)
print(type(x))
print(x)

