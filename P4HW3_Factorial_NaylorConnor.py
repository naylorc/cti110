#CTI-110
#P4HW3 - Factorial
#Connor Naylor
#7/1/18

#import required libraries
import math

#While loop
answer="y"
while answer=="y":

    #request input
    number=int(input("Enter a nonnegative interger: "))

    print("The factorial of",number,"is",math.factorial(number))
    
    answer=input("Would you like to run this again? Y or N ")
    
print("Goodbye")
