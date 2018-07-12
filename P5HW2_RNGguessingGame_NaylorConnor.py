#CTI - 110
#RNG Guessing Game
#Connor Naylor
#7/5/18

#The one time my linux class has paid off
#Import Libraries
import random

def main():
    answer="y"
    while answer=="y":
        guessesTaken = 0
        number=random.randint(0,101)
        
        while guessesTaken < 9:
            guess=int(input("Guess my number! It's between 1 and 100."))
            guessesTaken = guessesTaken + 1
            
            if guess < number:
                print("Too low. Try again!")
                
            if guess > number:
                print("Too high. Try again!")
                
            if guess == number:
                break
            
        if guess == number:
            print("Good job! You guessed my number",number,"in",guessesTaken,"guesses!")

        if guess != number:
            print("Game Over! Better luck next time!")
            print("My number was",number)
        answer=input("Would you like to play again? ")   
main()
