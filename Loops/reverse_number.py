#####################################################################################
#
# Function Name:    Reverse
# Input:            Integer Number
# Description:      Accepts one number and reverses that number
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Reverse(Value):
    Reverse = 0
    while (Value > 0):
        Digit = Value % 10
        Reverse = Reverse * 10 + Digit
        Value = Value // 10

    return Reverse

######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Reverse Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    Ans = Reverse(No)

    print("Reverse of the number is:-",Ans)

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()