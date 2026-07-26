######################################################################
#
# Function Name:    Cube
# Input:            Integer Number
# Description:      Return the cube value of number 
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################

def Cube(Value):
    FValue = Value ** 3

    return FValue

######################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes user Input and Calls the Cube Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################

def main():
    No = int(input("Enter the Number:-"))

    Ans = Cube(No)

    print("Cube of the given Number is:-",Ans)

######################################################################
#
# Starter of the Main Function
#
######################################################################

if __name__ == "__main__":
    main()
