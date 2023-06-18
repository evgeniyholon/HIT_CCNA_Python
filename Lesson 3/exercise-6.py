import random

count = 7
total = 0
numbers_str = ''
for i in range(count):
    num = random.randint(1, 100)
    numbers_str += str(num)
    if i+1 != count:
        numbers_str += ' + '
    total = total + num

print(f'\n{numbers_str} = {total}')
if total % count == 0:
    print('BOOM')
