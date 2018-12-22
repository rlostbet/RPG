import World
import Game
import World_Objs
import NPC_Objs

from random import randint
from time import sleep
p1 = Game.Avatar("me")
p1._ATK = p1.ATK * 999
"""
skill:
    - Scattering Spark
    - Sparky, Windy, and Rainy.
    - Gorgeous Yellow Storm.

Events:
    Event1
    - when LV <20 if enter "Gorgeous Forest".
    - She Stuns Him(10% of chance dying).
    - She Decorates Him as a doll.
      (with Honey From "the World Tree")
      (20% of chance dying, 1% of chance soul being taken))
    - Beauty, pls don't harrass me?
    - GoodBye Kiss of A stunning elf.
"""
class Event:  # fate
    sequence = ["Sparky_Lia"]
    # Time Stuff
    #  - Morning, Night.
    #  - Playtime
    #
    def Sparky_Lia(avatar):
        # if CurrentLocation in World.Map.
        # Move.Walk()
        def Walk():
            forest = World_Objs.gorgeous_Forest
            fairy = NPC_Objs.Lia
            print("You are walking " + forest.name +"...")
            if randint(1, 3) == 1:
                enemies = forest.enemies
                rNum = randint(0, len(enemies) - 1)
                enemy = enemies[rNum]
                sleep(1)
                print(f"You Have Encountered A {enemy.__class__.__name__}!!!")
                Game.Commands.ShowStatus(enemy.name)

            if randint(1, 3) == 2:
                sleep(1)
                print("You Have Encountered " + fairy.name)
                Game.Commands.ShowStatus(fairy.name)
        Cmds = {
            "Walk": Walk
        }
        # Cmds.update(Game.basicCmds)
        while True:
            avatar.CmdInterface(Cmds, False)


class Move(Event):
    def walk():     #current Location
        # find a collectable
        # find a foe
        # find a town
        pass

    def Roam():
        pass

    def Stay():
        pass

    def Chase():
        pass

    def Fallow():
        pass
    # (etc)


class Fight(Event):
    pass


class Talk(Event):
    pass


class Dialogue:
    pass

def main():
    Event.Sparky_Lia(p1)

if __name__ == '__main__':
    main()