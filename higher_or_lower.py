from random import randrange

def guess() :
    guess = int(input("Please enter a number between 0 and 10: "))
    return guess


def rando_num() :
    rando = randrange(0,11)
    return rando
    

user_guess = guess()
rando_mando = rando_num()

while user_guess != rando_mando :
    
    if user_guess > rando_mando :
        print("Too High!")
        user_guess = guess()
    
    elif user_guess < rando_mando :
        print("Too Low!")
        user_guess = guess()
      
    if user_guess == rando_mando :
        print("Correct! You win!")