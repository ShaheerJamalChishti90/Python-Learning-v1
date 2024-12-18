import time


name = input('Enter your name: ')
recenttime = time.strftime('%I:%M:%S')
Recenttime = int(time.strftime('%I'))
c = name.capitalize()
if(4<=Recenttime<12):
    print("Good Morning, ",c, "Welcome to the party! Let's make this Morning unforgettable. Enjoy yourselves and have a fantastic time!," "its,", recenttime,"in the Morning.")
elif(12>=Recenttime<4):
    print("Good Afternoon, ",c, "Welcome to the party! Let's make this Afternoon unforgettable. Enjoy yourselves and have a fantastic time!,"'its',recenttime,"in the Afternoon.")
elif(4>=Recenttime<7):
    print("Good Evening, ",c, "Welcome to the party! Let's make this Evening unforgettable. Enjoy yourselves and have a fantastic time!",c,'its',recenttime,"in the Evening.")
else:
    print("Enjoye your late night, ",c, "Welcome to the party! Let's make this Morning unforgettable. Enjoy yourselves and have a fantastic time!",c,'its',recenttime,"in the late night.")



# print('Hii',name,'its',recenttime)
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59