inventory = {'Knife':1, 'Healthkit':3,
             'Wood':10}

print(inventory['Knife'])

inventory['Knife'] = 2
print(inventory)
inventory['Gold'] = 50
print(inventory)

print(inventory['Gold'])
print(inventory.get('Cool'))

print(inventory.keys())
print(inventory.values())

inventory.pop('Knife')
print(len(inventory))
inventory['Apple'] = 10
print(inventory)