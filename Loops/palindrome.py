#####################################################################################
#
# Function Name:    Palindrome
# Input:            Integer Number
# Description:      Accepts one number and checks whether that number is palindrome or not
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Palindrome(Value):
    Original = Value
    Reverse = 0
    while (Value > 0):
        Digit = Value % 10
        Reverse = Reverse * 10 + Digit
        Value = Value // 10

    if(Original == Reverse):
        return True
    else:
        return False

######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Palindrome Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))
    Ans = 0

    Ans = Palindrome(No)

    if(Ans == True):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()