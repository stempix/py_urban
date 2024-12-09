from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed = 0, _cords = None):
        if _cords is None:
            _cords = [0, 0, 0]
        self.speed = speed
        self._cords = _cords

    def move(self, dx, dy, dz):
        if self._cords[2] < 0:
            print("It's so deep, I can't move :(")
        else:
            move_cords = (self.speed * cord for cord in [dx, dy, dz])
            self._cords = [sum(values) for values in zip(*(self._cords, move_cords))]

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    @staticmethod
    def lay_eggs():
        num = randint(1, 4)
        to_be = "is" if num == 1 else "are"
        print("Here", to_be, num, "egg" + ("" if num == 1 else "s"), "for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.speed /= 2
        super().move(0, 0, -(abs(dz)))
        self.speed *= 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()