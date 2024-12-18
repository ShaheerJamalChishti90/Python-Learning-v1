# Learning Match Case Statements:

num = int(input("Enter any number here: "))

match num:
    case 0:
        print("The number is zero")
    case 5:
        print("The number is five")
    case _ if num != 10:
        print("the num is not 10")
    case _ if num != 20:
        print("num is not 20")
    case _:
        print("num is", num)


# Program: number checker, if the number is in between 1 and 100 or not 


a = int(input("Enter any number here, 100 > num > 0: "))

if a > 100 or a <= 0:
    if a == 0:
        print("The number is zero and its invalid!")
    print(f"Invalid Entry! {a} is not between 100 and 1")
else:
    match a:
        case _ if a <= 25:
            print(f"The number is {a} and it's <= 25")
        case _ if a <= 50:
            print(f"The number is {a} and it's <= 50")
        case _ if a <= 75:
            print(f"The number is {a} and it's <= 75")
        case _ if a <= 100:
            print(f"The number is {a} and it's <= 100")