class WorldError(Exception):
    """Errors That Occur While Creating Wolrd Objects"""


class EnemyCreationError(WorldError):
    def __init__(self, msg=None, *args):
        super().__init__(*args)
        self.msg = "An Error Occured Creating Enemy" if msg is None else msg


class World:    # phisical features.
    archive = {}

    def __init__(self, name):
        self._lvUnSet = True
        self._name = name
        World.archive[name] = self

    @property
    def lvUnSet(self):
        return self._lvUnSet

    @property
    def name(self):
        return self._name

# Livings #
class Life(World):
    archive = {}
    titles = ("Common", "Uncommon", "Rare", "Epic", "Legendary", "God-like", "Mid-god", "God")
    relationships = ("Stranger", "friend", "familly", "Lover")
    healthRatio = 10

    def __init__(self, name, *args):
        super().__init__(name, *args)
        self._lv = 1  # setter > 0
        self._ATK = self.lv * 5
        self._maxHealth = self.lv * self.__class__.healthRatio
        self.health = self._maxHealth
        self.gender = None
        self.weaponATK = 0  # weapon dmg * weapon skill * weapon Familiarity
        self.possesion = {}
        self.job = None
        self.title = None
        Life.archive[name] = self

    @property
    def lv(self):
        return self._lv

    @property
    def maxHealth(self):
        return self._maxHealth

    @property
    def health(self):
        return self._health

    @property
    def ATK(self):
        return self._ATK

    @health.setter
    def health(self, value):
        if value > 0:
            self._health = value
        else:
            self._health = 0

    @lv.setter
    def lv(self, value=1):
        if self.lvUnSet:
            if value > 0:
                self._lv = value
                self._lvUnSet = False
        else:
            self._lv += 1
            # exp limmit or something..

        self._maxHealth = self._lv * self.__class__.healthRatio
        self.health = self._maxHealth
        self._ATK = self._lv * 5

    def GetStatus(self):
        return (
            "------------------------------\n"
            f"{self.name}\n"
            "------------------------------\n"
            f"Level   : {self.lv}\n"
            f"Health  : {self.health} / {self.maxHealth}\n" # health bar
            f"ATK     : {self.ATK}\n"
            f"Title   : {self.title}\n"
            f"Job     : {self.job}\n"
            f"Gender  : {self.gender}\n"
            "------------------------------")


class Animal(Life):
    archive = {}
    def __init__(self, name, gender=0, *args):
        super().__init__(name, *args)
        Animal.archive[name] = self
        self.gender = "Male" if gender == 0 else "Female"


class Plant(Life):
    healthRatio = 1000
    def __init__(self, *args):
        super().__init__(*args)


class Humanoid(Animal):  # those who can speak & walk.
    healthRatio = 100
    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        self.title = ""  # <-- Rarity, setter in titles.
        self.job = "No Job"
        Humanoid.archive[name] = self


class Human(Humanoid):  # engel, ancient being.
    healthRatio = 150
    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        Human.archive[name] = self


class Elf(Humanoid):
    healthRatio = 80
    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        Elf.archive[name] = self


class Fairy(Humanoid):
    healthRatio = 30
    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        Fairy.archive[name] = self


class Dwarf(Humanoid):
    healthRatio = 125
    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        Dwarf.archive[name] = self


class Beast(Animal):
    healthRatio = 200
    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        Beast.archive[name] = self


# Non Livings #
class Map(World):
    pass


class Nation(Map):
    # capital =
    pass


class Town(Nation):
    pass


class HuntingGround(Map):
    archive = {}

    def __init__(self, name):
        super().__init__(name)
        self.collectables = {}
        self.enemies = []     # 1 type of enemy 1 hunting Ground for now
        HuntingGround.archive[name] = self

    def CreateEnemy(self, enemyClass, enemyNames, enemyNumber):
        import random
        enemyNames = list(enemyNames)

        if enemyNames == []:
            raise EnemyCreationError("Enemy Name is Empty")

        length = len(enemyNames)

        if length != enemyNumber:
            diff = (enemyNumber - length)

            if diff > 0:
                for i in range(diff):
                    rNum = random.randint(0, length-1)
                    enemyNames.append(enemyNames[rNum])
            else:
                for i in range(abs(diff)):
                    rNum = random.randint(0, len(enemyNames)-1)
                    enemyNames.remove(enemyNames[rNum])

            del i
            del rNum
            del diff
            del length

        for i in range(enemyNumber):
            enemy = eval(f"{enemyClass}(\"{enemyNames[i]}\")")
            self.enemies.append(enemy)

        del i


class Item(World):
    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        Item.archive[name] = self


def main():
    pass


if __name__ == '__main__':
    main()
