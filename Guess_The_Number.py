from random import randint
g_Live = True
rNum = randint(0, 20)
while g_Live:
    user_Input = int(input("Choose a random number"))
    if user_Input == rNum:
        print("Correct!")
        g_Live = False
    elif user_Input > rNum:
        print("Lower!")
        continue
    else:
        print("Higher!")
        continue
        
    