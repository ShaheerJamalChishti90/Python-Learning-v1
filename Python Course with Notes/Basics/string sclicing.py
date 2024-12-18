#doing string slicing [0,1,2,3] <== these are called index

# name = "Shaheer"
# print(name[0:-4])  # yahan ye -4 karne se name kii length mein 4 se minus karke answer dega


# print(name, " :The total alphabets in this name if we minus 5 are:", len(name[:-5]))

f = "hariea" 
print(f [-4:-2])



# end wala index number neglect hojata hai
# jaisay "mango" ismein total [0:4] hain ab agar mein isko print karwaounga tou  "mang" print hoga kyun ke end wala index number count nahi hota ignore hojata hai

# negative slicing
# neg slicing mein ye hota hai ki string ki length mein se apke index ka number minus hojata hai jaisy "mango" hai iski len 5 hai, ab agar [-4:-2] karounga ismein tou 5-4=1 aurr 5-2=3 tou 1:3 print hoga matlab index 1 pe jo alphabet hoga wo,LEKIN index 3 pe jo alphabet hoga wo print nahi hoga wo neglect hojayega aurr uski jaggha index 2 wala print hoga "an"

a = "mango"
print(a[-4:-2])


print(a[0:-4]) # 5 - 4 = 1 "a[0:1]" and as we know that last wali value neglect hojati hai aurr ussay pehly wali aati hai so the ans will be "m"