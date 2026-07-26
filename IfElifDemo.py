print("-------------------------------------------")
print("----------Ticket prizing Software----------")
print("-------------------------------------------")

print("Please Enter Your Age:-")
Age = int(input())

if(Age <= 5):
    print("Free Entry")

elif(Age > 5 and Age<=18):
    print("Ticket Prize:-900")

elif(Age > 18 and Age <= 40):
    print("Ticket Prize:-1200")

else:
    print("Ticket Prize:-500")

