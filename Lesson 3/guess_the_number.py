import random

name = input('Hello! What is your name?\n')
num = random.randint(1, 20)
guess = int(
    input(f'Well, {name}, I am thinking of a number between 1 and 20.\n'
          f'Take a guess.\n'))
count = 1

while guess != num and count < 5:
    if guess > num:
        guess = int(input('Your guess is too high.\nTake a guess.\n'))
    else:
        guess = int(input('Your guess is too low.\nTake a guess.\n'))
    count += 1

if guess == num:
    print(f'Good job, {name}! You guessed my number in {count} guesses!')
else:
    print(f'{name}, you loss :-(')
