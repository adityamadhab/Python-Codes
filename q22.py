#Dictioanry: It stores key value ordered pair
#ordered, mutable, does allow duplicates

dic = {
    "name":"Aditya Madhab",
    "rollno":17,
    "age":19
}
print(dic)

#length

print(len(dic))

#accessing the elements

print(dic["name"])

#get()

x=dic.get("name")
print(x)

#Changing the elements

dic["age"]=20
print(dic)

#update the elements

dic.update({"name":"Aditya Madhab Borah"})
print(dic)

#remove the elements

dic.pop("age")
print(dic)