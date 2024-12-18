# Learning string methods

# strings are immutable (matlab ye ke original string apni jaggha change nahi hoga lekin haan mein uski new copy xaroor bana sakta hoon)

# jaisa "name = shaheer" ab name ke andar "shaheer" ko "SHAHEER" mein convert tou karsakta hoon lekin "shaheer" ko kisi doosry cheez mein convert nahi karsakta

# .upper()
# .lower()
# .rstrip()
# .replace()
# .split()
# .capitalize()
# .center()
# .count()
# .endswith()
# .find()
# .index()
# .isalnum()
# .isalpha()
# .islower()
# .isprintable()
# .isspace()
# .istitle()
# .isupper()
# .startswith()
# .swapcase()

# SOME EXAMPLES:

a = "ShAhEEr JaMaL"
b = "shaheer jamal"
c = "SHAHEER JAMAL"
d = "shaheer jamalshaheer chishtishaheer"
my_str = "Quick #25 Chars String !!"
abc = "Hello World"

# print(a.upper()) # yahan par ye meri existing string "a" ko change nahi karega lekin ye new string bana dega

# print(c.lower())
# print(b.rstrip("jamal"))
# print(d.replace("shaheer", ""))
# print(a.split(" "))
# print(a.capitalize())


# print(len(abc))
# print(abc.center(50,"_"))
# print(d.count("shaheer"))

# print(abc.endswith("World", 4, 11))     
# jaisa ke humein pata hai ke 4th index pe "hello" ka "o" hai aurr 11th index pe kuch bhi nahi hai, lekin in dono index ke ddarmiyaan world aaraha hai, issliye ye mujhe "True" return karega! 

pr = 'Muhammad shaheer jamal chishti shabbar ahmad latif khan chishti 932006'
# print(pr.find("chishti"))
# find method srif first occourance ko hii detect karega aurr detect karne ke baad wo index number deta hai jaisay "chishti" first occourance ka index number 23 hai"

# print(pr.index("ishh"))
# index method dekhyga agar given string hai tou batadega warna error dekr program execute kardega


pr = "ShaheerJamal90"
# print(pr.isalnum())
# isalnum method ki boht basic shit, dekhyga ke apki str mein alphanumeric hain ya nahi, agar alphanumeric hai tou "True" return karega warna "False", pr mein spaces hain tou wahan false return kar raha hai, agar spaces hata diye jayen tou true return karega


# print(pr.isalpha())
# isalpha method dekhyga ke apki str mein srif alphabets hain ya nahi, agar alphabets ke ilawa kuch bhii hua tou error dedega


# print(pr.islower())
# islower ki boht basic shit, ye dekhega ke saary characters lower case hain ya nahi, agar lower case hain tou "True" return karega warna "False"

# print(pr.isprintable())
# isprintable method dekhyga ke apki str mein printable hain ya nahi, agar printable hai tou "True" return karega warna "False", 



spaces1 = "      "
spaces2 = "Shaheer        Jamal"
spaces3 = "  Shaheer  Jamal"

# print(spaces1.isspace())
# isspace mein ye check karega ke str mein whitespaces hain ya nahi, ab white spaces kia hai?? kuch bhi nahi bas "        " ye jo gap hai ye kehlaty hain whitespaces, ab chahay ye gap tab daba kar diyejayen ya phirr spacebar se, aurr mazay kii baat ye true srif jab return karega jab str mein srif aurr srif space hoga, agar kisi cheez ke beech mein ya pehly space hua tou ye false return karega


name = "Shaheer Jamal Chishti"
# print(name.istitle())

# same shit boht basic function, true return karega jab str mein saary words ke initials capital hoengy, agar ek initial bhi capital nahi hua tou false return karega 

name = "SHAHEER JAMAL"
# print(name.isupper())

# same shit boht basic function, true return karega jab str mein saary characters  capital hoengy, agar ek character bhi capital nahi hua tou false return karega 

# print(name.swapcase())
# boht hii gandu method hai ye, ye cases ko change kardeta hai, matlab lower ko upper case mein convert kardeta hai aurr upper ko lower case mein convert kardeta


myself = "Shaheer is a good boy. he lives in karachi"
# print(myself.title())
# bhai ye method apki str ke har word ke initial ko capital banadega thats it 