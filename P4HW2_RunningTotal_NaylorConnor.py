# P4HW2 - Running Total
# CTI - 110
# Connor Naylor
# 6/26/18

#accumulator variables
count=0
runningtotal=0

answer="y"
#loop
while answer=="y":
    count=count+1
    number=int(input("What is your grade? "))
    runningtotal=runningtotal+number
    
    answer=input("Would you like to add more grades? Y or N ")
#end loop
average=runningtotal/count
print("You ran this program",count,"times, adding",count,"grades.")
print("Your average between these grades is",average)
