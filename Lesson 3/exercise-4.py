greate = 0
for i in range(1, 4):
    num = int(input(f"Enter number {i}: "))
    if num > greate:
        greate = num

print(f'{"-" * 30}\nYou greater number is: {greate}')
