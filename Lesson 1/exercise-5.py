bus = int(input('Enter the cost of renting a bus: '))
park = int(input('Enter the park entrance fee for the class: '))
students = int(input('Enter the number of students in the class: '))

print(f'Each student must pay: {(bus+park)/students:.2f} ILS')
