# value = 0
# while value < 10:
#     print(value)
#     if value == 120:
#         break
#     else:
#         value += 1

value = 0.5
while value <= 10:
    print(value)
    value += 0.8
    if value == 5:
        continue
else:
    print("The loop has completed, Thank you. 😊 \n The final value is: " + str(value))