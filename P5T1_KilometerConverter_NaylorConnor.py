#CTI - 110
#P5T1 - Kilometer Converter
#Connor Naylor
#7/17/18

#miles=kilometers*0.6214
def main():
    kilometers=int(input("How many kilometers were traveled? "))
    miles=kilometers*0.6214
    show_miles(miles)
def show_miles(miles):
    print(miles,"miles were traveled.")
main()
