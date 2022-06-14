# Conversion Website calculator

import time
import sys
import os

msg = "Good-bye"
conv = ""

os.system("cls" if os.name == "nt" else "clear")


def choiceMenu():
    print("Choose from the following")
    print("[1] Inchs to Centimeters")
    print("[2] Centimeters to inches")
    print("[0] To exit")


def clearScreen():
    print(msg)
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    sys.exit()


# Convert Centimeters to Inchs


def CentimeterToInch(cm):
    global conv
    conv = str(cm)
    return float(cm) / float(2.54)


# Convert inches to centimeters


def convInchToCentimeters(inch):
    global conv
    conv = str(inch)
    return float(inch) * float(2.54)


print("Hello...Welcome to the conversion program")

time.sleep(2)
choiceMenu()
option = int(input("Enter your option: "))

while option != 0:

    if option == 1:

        inch = int(input("How many inches to convert? "))
        ans = convInchToCentimeters(inch)
        print(f"{conv} inch's equals {ans} Centimeters")
        choice = input("Try again? (y/n)")
        if choice == "y":
            os.system("cls" if os.name == "nt" else "clear")
            choiceMenu()
            option = int(input("Enter your option: "))

        else:
            clearScreen()

    elif option == 2:
        ans = CentimeterToInch(int(input("How may centimeters to convert? ")))
        print(f"{conv} centimeters equals {ans} inch\s")
        choice = input("Try again? (y/n)")
        if choice == "y":
            os.system("cls" if os.name == "nt" else "clear")
            choiceMenu()
            option = int(input("Enter your option: "))

        else:
            clearScreen()
    else:
        print("Nothing matched your selection")
        choiceMenu()
        option = int(input("Enter your option: "))
        if option == 0:
            clearScreen()
        else:
            continue


# #Convert mm to inches
# mm  = inch / 25.4

# #Convert inches to mm
# inch = inch * 25.4

# #Convert inches to meters
# inch = inch / 0.0254

# #Convert meter to feet
# meter = meter * 3.28084
