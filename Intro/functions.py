def my_func():
    print("heello")

x_pos = 0
def move(x_pos,by_amount):
    x_pos += by_amount
    return x_pos

#
# for i in range(5):
#     move()
print(move(x_pos,10))

