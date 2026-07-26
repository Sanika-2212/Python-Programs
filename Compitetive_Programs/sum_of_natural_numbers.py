#####################################################################################
#
# Function Name:    Sum
# Input:            Integer Number
# Description:      Accepts one number and prints Sum of first N natural numbers
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Sum(Value):
    total = 0
    for i in range(1,Value+1):
        total = total + i

    return total

######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Sum Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    Ans = Sum(No)

    print("Sum of first",No,"natural Numbers is:-",Ans)

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()