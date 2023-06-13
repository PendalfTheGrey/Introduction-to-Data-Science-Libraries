x_pos = 0
end_pos = 5
y_pos = 1
enemy_pos = 3
while x_pos <= end_pos:
    if y_pos > 1:
        continue
    x_pos += 1
    if x_pos == enemy_pos:
        break
print(x_pos)

#FOR loops
for  i in reversed(range(5)):
    print(i*2)
inventory = ['A','B','C','S']
for item in reversed(inventory):
    print(item)