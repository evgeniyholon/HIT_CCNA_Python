shirts_count = int(input('Enter the count of shirts (units): '))
shirts_cost = float(input('Enter the cost of shirt (ILS): '))
pants_count = int(input('Enter the count of pants (units): '))
pants_cost = float(input('Enter the cost ot pants (ILS): '))
discount = int(input('Enter discount (%): '))

pay = (shirts_count*shirts_cost+pants_count*pants_cost)*(100-discount)/100

print('-'*30)
print(f'To pay: {pay:.2f} ILS')
