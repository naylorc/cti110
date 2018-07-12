#CTI - 110
#P5HW1 - Test Average and Grades
#Connor Naylor
#7/5/18


def main():
    g1=int(input("What is the first grade? "))
    g2=int(input("What is the second grade? "))
    g3=int(input("What is the third grade? "))
    g4=int(input("What is the fourth grade? "))
    g5=int(input("What is the fifth grade? "))
    ave=calcAverage(g1,g2,g3,g4,g5)   
    displayLetterGrade(ave)
    
def calcAverage(g1,g2,g3,g4,g5):
    total=g1+g2+g3+g4+g5
    ave=total/5
    return ave

def displayLetterGrade(ave):
    if ave > 89 and ave < 101:
        print("Your numeric grade of",ave,"is an A!")
    elif ave > 79 and ave < 90:
        print("Your numeric grade of",ave,"is an B!")
    elif ave > 69 and ave < 80:
        print("Your numeric grade of",ave,"is an C.")
    elif ave > 59 and ave < 70:
        print("Your numeric grade of",ave,"is an D.")
    elif ave >= 0 and ave < 60:
        print("Your numeric grade of",ave,"is an F...")
    else:
        print("Invalid input. Try again")

main()
