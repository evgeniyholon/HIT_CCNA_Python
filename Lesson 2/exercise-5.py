age = int(input('Enter your age: '))

if age < 0:
    print('You are not born.')
elif age <= 3:
    print('You are Baby.')
elif age <= 12:
    print('You are Child.')
elif age <= 18:
    print('You are Teenager.')
elif age <= 60:
    print('You are Adult.')
elif age <= 120:
    print('You are Old.')
else:
    print('You are Dead.')
