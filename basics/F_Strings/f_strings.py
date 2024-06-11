person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coints left.")

message = "\n%s has %s coins left" % (person, coins)
print(message)


#Format method approach. 
message = "\n {} has {} coins left".format(person, coins)
print(message)

#Format method approach. 
message = "\n {1} has {0} coins left".format(coins, person)
print(message)


#Format method approach. 
message = "\n {person} has {coins} coins left".format(coins = 10, person = "Alexander")
print(message)

player = {
    'person' : 'King Shack', 
    'coins' : 21
}

#Format method approach. 
message = "\n {person} has {coins} coins left".format(**player)
print(message)

# F-Strings

message = f"\n{person} has {coins} coins left."
print(message) 

message = f"\n{person} has {31 * 20} coins left."
print(message) 


message = f"\n{person.lower()} has {(31 * 20)} coins left."
print(message) 

message = f"\n{player['person']} has {player['coins']} coins left."
print(message) 

# You can pass formatting options: 
num =100
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1,10):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
    
for num in range(1,10):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")