#Learning typecasting
#there are two types of typecasting

# 01- explicit typecasting (iss mein hm py ko bataty hain ke kia typecast karna hai)

# 02- implicit typecasting

a = "1"
b = "2"

# a = "shaheer"
# b = " bhai"

# print(a + b)     #widout clarifying it ke ye int hai str nahi

print(int(a) + int(b))  #this time clarifying py that ke ye str nahi hai blky int hai taakay wo a aurr b ko plus kary aurr phir ans de



a = "15"
b = 30

print("The sum of both the numbers is: ", int(a) + b)


# now learning that the type casting will only type cast the str into and int function if its possile to typecast it.

a = "shaheer"
b = 10

print(int(a) + b ) # iss ko run karne pe error dega kyunke "shaheer" ek string hai aurr ye integer mein convert nahi ho sakta 


# implicit typecasting mein py khud type cast karta hai jaisay float aurr int ko add karwaye tou py khud int ko pehly float mein convert karta hai aurr phir uska answer deta hai (basically converts lower data type into higher data type to prevent data loss) 