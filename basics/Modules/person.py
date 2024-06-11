from random import choice 

favourite_car = "e46 BMW M3"
favourite_place = "Cape Town"
favourite_color = "Black"
favourite_song = "1942 Flows"

def randomFunFact():
    funfacts = [
        "I was born in Port Elizabeth.",
        "I love cricket.",
        "I a forex trader.",
        "I am a developer",
    ]
    
    index = choice("0123")
    
    print(funfacts[int(index)])
    
# if __name__ == "__main__":
randomFunFact()