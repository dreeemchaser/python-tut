# # <--- Dictionaires --->
# # ! Key Value Pairs 
# # Curly Braces
# band = {
#     "vocals" : "Plant",
#     "guitar" : "page"
# }
# band_two = dict(make = "VW", year = "2024")


# # print(band_two)
# # print(len(band_two))
# # print(band)

# # # Access Items: 
# # print(band_two.get("vocals"))
# # print(band_two.get("make"))

# # List all keys: 
# print(band.keys())

# # List all values: 
# print(band.values())

# # List key/value pairs as tuples. 
# print(band.items())

# # Verify if the key exits: 
# print("make" in band_two)
# print("make" in band)


# # How to change values: 

# band["vocals"] = "Coverdale"
# band.update({"bass" : "KingRock"}) # Can create a new one too.. 

# print(band)

# # Remove Items: 
 
# print(band.pop("bass")) # POP returns the value that was removed 
# print(band)

# # Add new value: 

# band["drums"] = "Bonham"
# print(band.popitem()) # reutrns tuple -> Removed last key-value pair that was added.
# print(band)

# # Delete an Item: 

# band["drums"] = "Bonham"
# del band["drums"]
# print(band)

# band_two.clear()
# print(band_two)

# # Copying Dictionaires: 

# band2 = band # this wont copy it - it just gives reference to the other dictionary. 
# print(band2)

# band2["dums"] = "Dave"

# # dict() constructor function: 

# band3 = dict(band)
# print("Good Copy")
# print(band3)

# Nested Dictionaries: 

users = {
    "name": "Alexander",
    "Subjects": ["Math", "CAT", "IT"]
}

teachers = {
    "name": "Stander",
    "subjectCode": "0213",
}
school = {
    1: users,
    2: teachers
}

# print(school)

print(school[2])