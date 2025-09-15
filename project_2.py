import random
n  = random.randint(1, 100)
a = -1
guesses = 1

while(a !=n):
    a = int(input("Enter your guess: "))
    if( a > n):
        print("lower number please")
        guesses += 1
    elif(a < n):
        print("Higher number please")
        guesses += 1

print(f"Finally you guessed the number in {guesses} attempts")       

