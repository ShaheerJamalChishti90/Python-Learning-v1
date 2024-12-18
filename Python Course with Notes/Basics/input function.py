#learning input functions

# we use it like input()

# we can also typecast init like i did below:

# a = int(float(input("Enter your marks out of 550: ")))
# print("Your total percentage is: ", a/550*100)

# making an eligiblity checker for the driving license (using if else on my previous experience)

a = int(input("Enter your age: "))
if(a < 18):
    print("Sorry Sir/Mam you are not eligible to apply for this driving license application, pls try when you are 18, tyvm!")
else:
    print("Congragulations you are eligile to apply for this license application!")