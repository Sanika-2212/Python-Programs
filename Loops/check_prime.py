#####################################################################################
#
# Function Name:    CheckPrime
# Input:            Integer Number
# Description:      Accepts one number and checks whether it is prime or not
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def CheckPrime(Value):
    count = 0
    for i in range(1,Value+1):
        if(Value % i == 0):
            count = count+1

    if (count == 2):
        return True
    else:
        return False
    
######################################################################################
#
# Function Name:    Main
# Input:            Integer Number
# Description:      Takes User Input & Calls the CheckPrime Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    No = int(input("Enter Number:-"))

    Ans = CheckPrime(No)

    if(Ans == True):
        print("The Given Number is prime")
    else:
        
        print("The Given Number is not prime")


######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()