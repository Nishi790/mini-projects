import random

def rollDie(sides):
    out=random.randrange(1,int(sides)+1)
    print("Your roll is "+str(out))
    print("Would you like to roll again")
    answer=input()
    while "y" in answer:
        boundary=int(sides)+1
        out=random.randrange(1,boundary)
        print("Your roll is "+str(out))
        print("Would you like to roll again")
        answer=input()

def main():
    print("How many sides does your die have?")
    sides=input()
    rollDie(sides)
    while True:
        print("Would you like to roll a different die?")
        response=input()
        if "y" in response:
            print("How many sides does your die have?")
            sides=input()
            rollDie(sides)
        else: break
if __name__=="__main__":
        main()
