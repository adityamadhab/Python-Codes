#Use of logical operators

a, b = 10, 20
print(a>b and a>=b) # T T -> T, F F -> F, T F -> F, F T -> F
print(a<=b or a>b) # T T -> T, F F -> F, T F -> T, F T -> T
print(not a<b) # T -> F, F -> T