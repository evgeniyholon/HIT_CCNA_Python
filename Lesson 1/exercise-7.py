ice_count = int(input('Enter number of ice (units): '))
ice_cost = 0.80
choco_count = int(input('Enter number of choco (units): '))
choco_cost = 2.40
vat = 1.17

pay = (ice_count*ice_cost+choco_count*choco_cost)*vat

print('-'*40)
print(f'To pay: {pay:.2f} ILS')
