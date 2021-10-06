import random
computer_points=0
human_points=0
count=5
print("Welcome to Snake, Water and Gun Game")
print(" Type s to chosse Snake\n","Type w to chosse Water\n","Type g to chosse Gun")
for i in range(count):
    human1=str(input("Make your choice:"))

    lst=["s","w","g"]
    comp1=random.choice(lst)
    print("Computer choice",comp1)
    if (human1==comp1):
        print("Tie!None of you win\n")
    elif(human1=="s" and comp1=="w"):
        human_points=human_points+1
        print("You wins, Your point: ",human_points)
        print("\n")
    elif(human1=="s" and comp1=="g"):
        computer_points+=1
        print("Computer wins, Computer point: ",computer_points)
        print("\n")
    elif (human1 == "w" and comp1 == "s"):
        computer_points += 1
        print("Computer wins, Computer point: ", computer_points)
        print("\n")
    elif (human1 == "w" and comp1 == "g"):
        human_points = human_points + 1
        print("You wins, Your point: ", human_points)
        print("\n")
    elif (human1 == "g" and comp1 == "s"):
            human_points = human_points + 1
            print("You wins, Your point: ", human_points)
            print("\n")
    elif (human1 == "g" and comp1 == "w"):
        computer_points += 1
        print("Computer wins, Computer point: ", computer_points)
        print("\n")
    else:
        print("Invalid input")

if(computer_points>human_points):
    print("You losse!, You are noob Ha! Ha! Ha! Ha!\nTumse na ho payega Ha ah ah aha ha XD")
elif(computer_points==human_points):
    print("Koi nhi jeeta :(\nAb nikal yaha se\nPehli Fursat mai nikal XD")
else:
    print("You won!\nAree bete moz kardi :)")
