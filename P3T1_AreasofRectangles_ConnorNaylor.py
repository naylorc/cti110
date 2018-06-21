# CTI-110
# Area of Rectangles
# Connor Naylor
# 6/19/18

#Get the dimenstions of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

#Dimensions of rectangle 2
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#Calculate areas
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area
if area1 > area2:
    print("Rectangle 1 has the greatest area.")
elif area2 > area1:
    print("Rectangle 2 has the greatest area.")
else:
    print("Both rectangles have the same area.")
