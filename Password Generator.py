import random
import string
live = True
while live:
    user_input1 = int(input("How Long Do You Want Your Password?"))
    user_input2 = int(input("How Many Letters?"))
    while user_input2 > user_input1:
        error_input1 = int(input("Number Higher Than Total Password Legnth, Please Try Again."))
        user_input2 = error_input1
        continue
    if user_input1 != user_input2:
        user_input3 = int(input("How Many Numbers?"))
        while user_input1 < user_input2 + user_input3:
            error_input3 = int(input("Combined Number Higher Than Total Password Legnth, Please Try Again."))
            user_input3 = error_input2
            continue
        if user_input1 != user_input2 + user_input3:
            spec = user_input1 - (user_input2 + user_input3)
            speclist = ["!", "@", "#", "$"]
            while spec > 0:
                specadd = "specadd" + random.choice(speclist)
                spec = spec - 1
                continue
    elif user_input1 == user_input2:
        while user_input2 > 0:
            user_input2 = user_input2 - 1
            passw = passw + random.choice(string.ascii_lowercase)
            print(passw)

        

    
    req = "user_input1" + "user_input2" + "user_input3"
