from random import randint
dice = randint(1,6)
#print(dice)
while dice > 0:
    user_Input = input("Roll Dice?")
    if user_Input == "Yes":
        print(randint(1,6));
        continue
    else:
        print("Thank you!")
        break