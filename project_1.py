import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1,0,-1])
youstr  = input("Enter your choice: ")
youDict = {"s": 1, "g": 0, "w":-1}
reverseDict = {1: "snake", 0: "gun", -1: "water"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 or you == 1):
        print("You win!")

    elif(computer == -1 or you == 0):
        print("You lose!")
    
    elif(computer == 1 or you == -1):
        print("You lose!")
    
    elif(computer == 1 or you == 0):
        print("You win!")
    
    elif(computer == 0 or you == -1):
        print("You win!")
    
    elif(computer == 0 or you == 1):
        print("You lose!")
    else:
        print("Something went wrong!")    