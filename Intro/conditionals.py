key_press = 'rö'
if key_press == 'r':
    print("Move right")
elif key_press == 'l':
    print('Move left')
else:
    print("Inv")

command = 'Move right' if key_press == 'r' else 'Move left'
print(command)

num_lives = 3
health = 2
if health <= 0:
    print("you died!")
elif health <= 10:
    print("warning")
elif health <= 50:
    print("half health")
else:
    print("fully healthy")
