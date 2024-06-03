nums_ = {1,2,3,4}
nums = set((1,2,3,4,5,6))

print(nums)
print(nums_)
print(type(nums_))

# No duplicates are allowed: 
# It will remove them for you...
numbers = {1,2,4,5,3,3,4}
print(numbers)

# True is a dupe of 1,  False is a dup of zero
nums_tf = {1,True,2,False,3,4,0}
print(nums_tf)


# Check if the value is in a set: 

print(2 in nums_tf)

# You cannot refer to an element in a set with an index position !

# Add Element: 
nums_tf.add(8)
print(nums_tf)

# Add Elements from one set to another: 

set_one = {10, 1,2,3,4}
set_two = {5,6,7}

set_one.update(set_two) # -> this can be a dict, tuple or list. 

# print(set_one)

# You can use update with lists, tuples and dictionaries ! 

# Merge two to one: 
# set_one = {"A","B","C"}
# set_two = {"D","E","F"}
# set_three = set_one.union(set_two)

# print(set_three)

# Keep ONLY DUPLICATES: 
set_one = {2,3,4,3}
set_two = {3,4,5,2}
set_one.intersection_update(set_two)
print(set_one)