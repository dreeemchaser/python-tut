users = ["Tia","Kevin","Myrah"]

# Similar to lists BUT
# The content (data inside) WONT change 
# The ORDER will not change. 

myTup = tuple(("Alexander", "Tia")) 

anothertuple = (1,42,41,31,31,2,2)

newList = list(myTup) # New List of tuples. 
newList.append("Jackson")
newTup = tuple(newList)

# print(type(myTup))
# print(type(my_tup))
# print((myTup))
# print((newTup))


(one, two, *hey) = anothertuple

print(one)
print(two)
print(hey)

# .count() - needs a parameter - counts the no. of accurances in of(2) in the tuple.
print(anothertuple.count(2))