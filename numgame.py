import random 

print("Let's play a number guessing game! :)")
num_one = int(input("Enter your first number: "))
num_two = int(input("Enter your second number: "))
number = random.randint(num_one, num_two)
count = 0

while True:
    count += 1
    answer = int(input("Enter your guess: "))
    if answer < number:
        print("Too low!! Try again.")
    elif answer > number:
        print("Too high!! Try again.")
    else:
        print("Correct!!! :) You guessed the number in", count ,"tries.")
        break
