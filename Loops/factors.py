#####################################################################################
#
# Function Name:    Factors
# Input:            Integer Value
# Description:      Accepts one integer and find its factors
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def Factors(Value):
    Count = 0
    i = 0
    for i in range(1,Value +1):
        if(Value % i == 0):
            print(i)
            Count = Count + 1
    return Count 
######################################################################################
#
# Function Name:    Main
# Input:            Integer Value
# Description:      Takes User Input & Calls the Factors Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter The Number:-"))

    Ans = Factors(No)

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()