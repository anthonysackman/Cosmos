import random
import string

live = True
specadd = str("")
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
            specadd = ""
            spec = user_input1 - (user_input2 + user_input3)
            charlist = "!/\"#$%&\'()*+,-./:;?@[\\]^_{|}~"
            speclist = list(charlist)
            while spec > 0:
                specadd = specadd + random.choice(speclist)
                spec = spec - 1
                continue
        if user_input1 == user_input2 + user_input3 + len(specadd):
            finalpw = str("")
            numrange = str("")
            while user_input2 > 0:
                user_input2 = user_input2 - 1
                finalpw = finalpw + random.choice(string.ascii_lowercase)
            while user_input3 > 0:
                user_input3 = user_input3 - 1
                numrange = str(numrange) + str(random.randrange(0, 9))
            finalpw = str(finalpw) + str(numrange) + str(specadd)
            finalpw = list(finalpw)
            finalpw = random.sample(finalpw, len(finalpw))
            finalpw = ''.join(finalpw)
            print(finalpw)
            live = False
    elif user_input1 == user_input2:
        finalpw = "Password: "
        while user_input2 > 0:
            user_input2 = user_input2 - 1
            finalpw = finalpw + random.choice(string.ascii_lowercase)
        print(finalpw)
        live = False
