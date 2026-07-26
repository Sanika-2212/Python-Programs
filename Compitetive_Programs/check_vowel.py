#####################################################################################
#
# Function Name:    CheckVowel
# Input:            Character Value
# Description:      Accepts one character and checks whether it is a vowel or not
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def CheckVowel(Alph):
    if(Alph == "a" or Alph =="e" or Alph =="i" or Alph =="o" or Alph =="u"):
        return True
    else:
        return False

######################################################################################
#
# Function Name:    Main
# Input:            Character Value
# Description:      Takes User Input & Calls the CheckVowel Function
# Date:             19/07/2026
# Author:           Sanika Ashok Misal
#
######################################################################################

def main():
    Char = input("Enter The alphabet:-")

    if(len(Char) != 1):
        print("Please Enter Only Single Character")
        return

    Ans = CheckVowel(Char)

    if(Ans == True):
        print("Character is an Vowel")
    else:
        print("Character is a Constant")

######################################################################################
#
# Starter of the Main Function
#
######################################################################################

if __name__ == "__main__":
    main()