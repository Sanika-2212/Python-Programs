#####################################################################################
#
# Function Name:    Table
# Input:            Integer Number
# Description:      Accepts one number and prints multiplication table of that number
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Table(Value):
    i = 0
    for i in range(1,11):
        print(f"{Value} * {i} = {Value * i}")

######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the Table Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    Ans = Table(No)

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()