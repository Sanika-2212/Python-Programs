#####################################################################################
#
# Function Name:    Odd
# Input:            Integer Number
# Description:      Accepts one number and prints all Odd numbers till that number
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Odd(Value):
    i = 0
    for i in range(1,Value+1):
        if(i % 2 != 0):
            print(i)
            i = i+1

    return i

######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Odd Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    print("Odd Numbers till the Given Number is:-")

    Ans = Odd(No)

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()