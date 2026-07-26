#####################################################################################
#
# Function Name:    Count
# Input:            Integer Number
# Description:      Accepts one number and counts the digit in that number
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Count(Value):
    count = 0
    while (Value > 0):
        Value = Value // 10
        count = count + 1

    return count
######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Count Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    Ans = Count(No)

    print("The Count of Digits in the number is:-",Ans)


######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()