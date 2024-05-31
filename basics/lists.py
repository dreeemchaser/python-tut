
users = ["Tia","Kevin","Myrah"]

empytyList = []
empytyList.append("Alexander Draai")
users += empytyList

empytyList.append("Jake")
users += empytyList


empytyList.extend(["Kitty"]) # This wont remove... hmm

# # ADD at specific spot: 
users.insert(0,"Akumbo")

users[1:4] = ["GOONZ", "ELLY"]

users.remove('GOONZ')


# del users[0:len(users) - 1]
users[1:2] = "ABCD"
users.sort(key=str.upper)

print(users)
# print(empytyList)

nums = [1,2,3,4,5]
nums.reverse()
print(nums)

nums.sort(reverse=False)
nums[1] = 21

# Using List constructor: 
myList = list([1, "Niel", True])

print(sorted(nums, reverse =True))
print(nums)
print(myList)
print(type(nums))