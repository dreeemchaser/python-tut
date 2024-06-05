# def add_one(num):
    
#     if (num >= 9):
#         return num + 1
    
#     total = num + 1
#     print(total)
    
#     return add_one(total)

# tot = add_one(0)
# print(tot)


def loop_add_one(num):
    for x in range(0,11):
        if (x >= 9):
            return num + 1
        
    total = num + 1
    print(total)
    
loop_add_one(1)