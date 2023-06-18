number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))
number3 = int(input('Enter number 3: '))

if number1 > number2 and number1 > number3:
    print(f'Greater number is {number1}')
elif number2 > number3:
    print(f'Greater number is {number2}')
else:
    print(f'Greater number is {number3}')
