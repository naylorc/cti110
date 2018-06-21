# CTI-110
# P3HW2 - Software Sales
# Connor Naylor
# 6/21/18

# Pre-defined Variables
package = 99

# Main and While functions
def main():
    choice="y"
    while choice=="y":
        
# Request input from user    
        quantity=int(input("How many packages are you buying? "))
        volume=quantity*package
# If, elif, else categories for discount

        if 1<= quantity < 10:
            print ("Your packages will cost you $", package * quantity)
        elif 10<=quantity<=19:
            print ("You will have a 10% discount. Your packages will cost you $", volume * .9,". That saves you $", volume * .1)
        elif 20<=quantity<=49:
            print ("You will have a 20% discount. Your packages will cost you $", volume * .8,". That saves you $", volume * .2)
        elif 50<=quantity<=99:
            print ("You will have a 30% discount. Your packages will cost you $", volume * .7,". That saves you $", volume * .3)
        else:
            print ("You will have a 40% discount. Your packages will cost you $", volume * .6,". That saves you $", volume * .4)
        choice=input("Would you like to run the program again? Y or N ")
    print ("Thank you for your purchase!")
main()
