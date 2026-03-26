class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(self.name)

class MarioCharacter(Character):
    def __init__(self, name, lives):
        super().__init__(name)
        self.lives = lives

    def jump(self):
        print('Wahoo!')

class FireMario(MarioCharacter):
    def throw_fireball(self):
        print('Fireball!!')


mario = MarioCharacter('Mario', 4)
fire_mario = FireMario('Fire Mario', 5)

mario.introduce()
mario.jump()

print()

fire_mario.introduce()
fire_mario.jump()
fire_mario.throw_fireball()


print()
# Part 2
class SuperMario(MarioCharacter):
    def yell(self):
        print('Mamma Mia!')

class SuperFireMario(SuperMario, FireMario):
    pass

super_mario = SuperMario('Super Mario', 6)

super_mario.introduce()
super_mario.yell()
super_mario.jump()

print()

super_fire_mario = SuperFireMario('Super Fire Mario', 9)
super_fire_mario.introduce()
super_fire_mario.jump()
super_fire_mario.yell()
super_fire_mario.throw_fireball()

