#dynamic lists -> no size
inventory = ['Alice','Fedor','Fira']
print(inventory[1])
inventory[2] = 'Krasa'
print(inventory)

print(len(inventory))
print(max(inventory))

inventory.append('Fira')
print(inventory)
inventory.insert(0,'Papa')
print(inventory)
inventory.pop()
inventory.remove('Papa')
print(inventory)

#two dimensional
universe = [[1,2,3,4],
            [1,2],
            [1,2,3,4],
            [1,2,3,4,5,6]]
print(universe[1][1])
print(universe)