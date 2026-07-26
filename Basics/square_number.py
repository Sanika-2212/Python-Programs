######################################################################
#
# Function Name:    Square
# Input:            Integer Number
# Description:      Return the Square value of number 
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################

def Square(Value):
    FValue = Value * Value
    return FValue

######################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes user Input and Calls the Square Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################

def main():
    No = int(input("Enter the Number:-"))

    Ans = Square(No)

    print("Square of the given Number is:-",Ans)

######################################################################
#
# Starter of the Main Function
#
######################################################################

if __name__ == "__main__":
    main()