hours = int(input('Enter Hours: '))
rate = int(input('Enter Rate: '))
delta_hours = 0

if hours > 40:
    delta_hours = hours - 40
    hours = 40

print(f'{"-"*30}\nPay: {hours*rate+delta_hours*rate*1.5} $')
