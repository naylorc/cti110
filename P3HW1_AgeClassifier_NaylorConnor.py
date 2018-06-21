# CTI-110
# P3HW1 - Age Classifier
# 6/19/18
# Connor Naylor

#Request age
choice="y"
while choice=="y":
    age=float(input("How old are you? "))

#Calculate age classification
    if age < 0:
        print("Invalid Number")
    elif 0<= age <= 1:
        print("You are an infant.")
    elif 1 < age < 13:
        print("You are a child.")
    elif 13 <= age < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")
    choice=input("Would you like to run the program again? Y or N ")
print ("Goodbye")
#End program
