# Learning IF/Else Conditional Statements:
# These are actual conditional statments:
# >, <, ==, >=, <=, !=

# a = int(input("Enter your age: "))
# print("Your age is:", a)

# if(a>18):
#   print("Yes")
#   print("You can drive")
#   print("Congragulations!!")
# else:
#   print('No')
#   print("You cannot drive")
#   print("Jaldi bara ho Madarchod!")



# # Using >= and <= conditions:


# budentry = int(float(input("Enter your budget: ")))
# iphone = 200


# if(budentry >= iphone):
#   print("You can buy this iphone")

# else:
#   print("You cannot buy this iphone")



# # Making an driving lisence eligiblity checker:

# username = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# height = int(float(input("Enter your height: ")))
# print ("\n eg: 5.5, 5.6, 5.7, 5.8, 5.9, 6.0"  ) 


# if(age >= 18 and height >= 5.10):
#   print("Congratulations", username, "you are eligible to apply for this driving license!")

# else:
#   print("Sorry", username, "you are not eligible to apply for this driving license!")


# # Using Elif in Program:

# money =  int(input("Enter money to recharge your card balance: "))
# cardbalance = money
# print("\n Your card balance is",cardbalance)

# if(cardbalance < 50):
#   print("\n Insuficient balance, balance must be more than 50 Rps")

# elif(cardbalance == 50):
#   print("\n 50 Rps conducted successfully, Your card remaining balance is", cardbalance - 50)

# else:
#   print("\n 50 Rps conducted successfully, Your card remaining balance is", cardbalance - 50)



# # Elif statment 02:

# num =  int(input("Enter any number which is less than 50: "))


  
# if(num <= 50 and num >= 40 ):
#   print("The number is in between 40 and 50") 

# elif(num <= 40 and num >= 30):
#   print("The number is in between 30 and 40")

# elif(num <= 30 and num >= 20):
#   print("The number is in between 20 and 30")

# elif(num <= 20 and num >= 10):
#   print("The number is in between 10 and 20")

# elif(num <= 10 and num >= 0):
#   print("The number is in between 0 and 10")

# else:
#   print("The number is not a Valid Number")





# # Learning Nested IF:
# # working!


# age = int(input("Enter your age: "))
# carowner = int(input("Do you own a car? (1/0): "))
# co = 1 == True and 0 == False


# if(age >= 18):
#   if(carowner == 1):
#     print("has car, can drive")
#     # if (carowner == 02):
#     #   print("hasnt a car, drive")
#   elif(carowner == 0):
#     print("hasnt a car cannot drive")
# else:
#   print("Try next year")
  



# Using Def function for the first time on my own:

# name = input("Enter your name here: ")

# def get_name(name):
#   if name == "shaheer":
#       return "My name is shaheer"
#   else:
#      return "Re-enter"
  
# print(get_name(name))







# # Nested IF:

# age = int(input("Wots your age: "))
# partypass = input("Do you have a pass?: ")
# gender = input("Whats your gender?: ")

# if(age > 18):
#   if(partypass == "yes"):
#     if(gender == "male"):
#       print("Can enter in party")
#     else:
#       print("Sorry, cannot enter in party, only males are allowed")
#   else:
#     print("Sorry, cannot enter in party, pass is required")
# else:
#   print("Sorry, cannot enter in party, you must be older tan 18")



# import time 

# timebatao = time.strftime( '%c' )
# print("Today is", timebatao)



# QUICK CODE:

age = int(input("Enter your age: "))

if age >= 25:
    print("You can get a degree")
else:
    match age:
        case _ if age>=20:
            print("do internships")
        case _ if age <20:
            print("study more")

    