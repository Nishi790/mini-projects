import random

def assessGuess(user,answer):
    try:
        user=int(user)
        if user<answer:
            print("Your guess was too low")
            print("Guess again.")
            user=input()
            return assessGuess(user, answer)
        elif user>answer:
            print("Your guess was too high")
            print("Guess again.")
            user=input()
            return assessGuess(user, answer)
        elif user==answer:
            print("You guessed correctly! Congratulations!")
            return True
    except:
        print("You must guess a whole number")
        assessGuess(input(), answer)
    

def playGame():
    answer=random.randrange(0,100)
    print("Guess the number.")
    user=input()
    win=bool(assessGuess(user, answer))
    if win:
        print("Do you want to play again?")
        again=input()
        return again

def main():
    playagain=playGame()   
    while "y" in playagain:
        playagain=playGame()
    print("Thanks for playing.")

if __name__=="__main__":
    main()
