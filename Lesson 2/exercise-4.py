students = int(input('Enter nuber of students: '))
seats = int(input('Enter nuber of seats on bus: '))
price = int(input('Enter price of rent one bus: '))

if students % seats > 0:
    buses = (students // seats)+1
else:
    buses = students // seats

print(f'{"-" * 40}\nNeed {buses} buses by total price {buses*price:.2f} $')
