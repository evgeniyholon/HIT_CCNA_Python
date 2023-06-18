count = total = min_num = max_num = 0

while True:
    number = int(input("Enter nuber (0 for stop): "))
    if number == 0:
        break
    else:
        count += 1
        total += number
        if number > max_num:
            max_num = number
        if min_num == 0 or number < min_num:
            min_num = number

print('-' * 25)
if count == 0:
    print('You not entered numbers!')
else:
    print(f'Count numbers - {count}\nTotal - {total}\n'
          f'Average - {total / count:.2f}\n'
          f'Minimum number - {min_num}\nMaximum number - {max_num}')
