from random import randint

def guess() :
    guess = int(input("Please enter a number between 0 and 10: "))
    return guess


def rando_num() :
    rando = randint(0,11)
    return rando
    

user_guess = guess()
rando_mando = rando_num()
count = 0

while count < 1 :
    
    if user_guess > rando_mando :
        user_guess = int(input("Too High! Please enter a number between 0 and 10: "))
        
    elif user_guess < rando_mando :
        user_guess = int(input("Too Low! Please enter a number between 0 and 10: "))
    
    if user_guess == rando_mando :
        print("Correct! You win!")
        count = count + 1