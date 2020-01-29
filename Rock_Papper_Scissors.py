import random
moves = ["Rock", "Papper", "Scissors"]
glive = True
while glive:
    uinput = input("Rock, Papper, or Scissors?")
    cpu = random.choice(moves)
    if uinput == "Rock" and cpu == "Scissors":
        print("CPU uses Scissors!")
        print("You Win!")
        glive = False
    elif uinput == "Papper" and cpu == "Rock":
        print("CPU uses Rock!")
        print("You Win!")
        glive = False
    elif uinput == "Scissors" and cpu == "Papper":
        print("CPU uses Papper!")
        print("You Win!")
        glive = False
    elif uinput == cpu:
        print("Tie!")
        continue
    else:
        print("CPU uses " + cpu + "!")
        print("You Lose!")
        glive = False
        
        