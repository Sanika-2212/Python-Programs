#####################################################################################
#
# Function Name:    Factorial
# Input:            Integer Number
# Description:      Accepts one number and prints Factorial of that number
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Factorial(Value):
    total = 1
    for i in range(1,Value+1):
        total = total * i

    return total

######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Factorial Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    Ans = Factorial(No)

    print("Factorial of the Given Number is:-",Ans)

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()