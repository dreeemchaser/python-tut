# CLOSURE is a function having access to the scope of its parent function
# after the parent function has returned. 
# ! -- Nested function - will have access to its scope of the parent function

def parent_function(person, coins):
    # coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.") 
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        else:
             print("\n" + person + " is out of coins.") 
    
    return play_game


Alexander = parent_function("Alexander", 3)
Tia = parent_function("Tia", 5)

Alexander()
Alexander()

Tia()
Alexander()