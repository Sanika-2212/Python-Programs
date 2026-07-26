#####################################################################################
#
# Function Name:    SumofDigits
# Input:            Integer Number
# Description:      Accepts one number and adds all the digits in that number
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def SumofDigits(Value):
    Sum = 0
    while (Value > 0):
        Digit = Value % 10
        Sum = Sum + Digit
        Value = Value // 10

    return Sum
######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the SumofDigits Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    Ans = SumofDigits(No)

    print("The Sum of Digits in the number is:-",Ans)


######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()