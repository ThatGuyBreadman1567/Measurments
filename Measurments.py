def main():
    fun = int(input("Please enter the number assigned to the task you would like to complete: \n1. Feet to Inches" +
    "\n2. Miles to Feet\n3.Yards to Meters\n4. Pounds to Kilograms"))
    if fun == 1:
        f = float(input("You chose the function, Feet to Inches, please enter the number of feet: "))
        feetToInches(f)
    elif fun == 2:
        m = float(input("You chose the function, Miles to Feet, please enter the number of miles: "))
        milesToFeet(m)
    elif fun == 3:
        y = float(input("You chose the function, Yards to Meters, please enter the number of yards: "))
        yardsToMeters(y)
    elif fun == 4:
        p = float(input("You chose the function, Pounds to Kilograms, please enter the number of pounds: "))
        poundsToKilograms(p)

def feetToInches(ft):
    print("HI")
def milesToFeet(miles):
    print("HI")
def yardsToMeters(yds):
    print("HI")
def poundsToKilograms(lbs):