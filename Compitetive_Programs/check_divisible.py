######################################################################
#
# Function Name:    Divisible
# Input:            Integer Number
# Description:      Checks Whether the Number is Divisible by 5 and 3
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################

def Divisible(Value):
    if(Value % 5 == 0 and Value % 3 == 0):
        return True
    else:
        return False

######################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Divisble Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################
def main():
    No = int(input("Enter Number:-"))

    Ans = Divisible(No)

    if(Ans == True):
        print("Number is Divisible By 5 & 3")
    else:
        print("Number is Not Divisible By 5 & 3")

######################################################################
#
# Starter of the Main Function
#
######################################################################

if __name__ == "__main__":
    main()