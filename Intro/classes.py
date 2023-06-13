class GameCharacter:
    #static var
    speed = 1.0

    def __init__(self,name,x_pos,health):
        self.name = name
        self.x_pos = x_pos
        self.health = health

    def move(self, by_amount):
        self.x_pos += by_amount

    def teke_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
    def chack_is_dead(self):
        return self.health <= 0

    #static func
    def change_speed(to_speed):
        GameCharacter.speed = to_speed

#subclass
class PlayerCharacter(GameCharacter):
    def __init__(self,name,x_pos,health, number_lives):
        # super(GameCharacter)
        super().__init__(name,x_pos,health)
        self.max_health = health
        self.num_lives = number_lives

    def teke_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.num_lives -= 1
            self.health = self.max_health

    def chack_is_dead(self):
        return self.health <= 0 and self.num_lives <=0

    def get_health(self):
        return self.health

player_charecter = GameCharacter("Fedor",5,100)
# print(type(player_charecter))
player_charecter.move(20)
print(player_charecter.x_pos)
player_charecter.teke_damage(150)
print(player_charecter.chack_is_dead())

pc = PlayerCharacter("Alis", 0, 100, 3)
gc = GameCharacter("Wolf", 0, 100)

print(pc.max_health)
pc.teke_damage(20)
print(pc.get_health())

gc_1 = GameCharacter("Lion", 0, 100)
gc_2 = GameCharacter("Dino", 2, 150)



print(GameCharacter.speed)
GameCharacter.speed = 2.0
GameCharacter.change_speed(4.0)
print(gc_1.speed)
print(gc_2.speed)