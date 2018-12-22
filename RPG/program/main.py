# import World, Event, Game
import Game
import NPC_Objs

"""
소설 세계관을 정리한다고 생각하자.
World, Event, Game.
- Phisical Features of the World I'm Creating
- Giving Fate to those Phisical Features. giving Chronological
  -sense to object creating.
- Game. Things that enables Users to Interact with the Wolrd and things
  that enables them to Cause Event.

  Data is Charicteristics or a part of World.
  Then, Event Let Data Recogninsed.

!this is gonna be text adventure game.
I can make
  + take
  + inventory

+ Select a race for each entity
+ Figth With NPC
+ I think Charicter are enuff.
+ search what obj is; if the object is map or not, blah blah
+ Travel Thru
+ have a story line.
- 그 이전에는, 작가들이 여러 이야기들을 감당할 수 있는 등장인물을 만들려 했지만,
 지금은 여러 등장인물들과 이야기들을 감당할 수 있는 세계를 만들고 있다.
- inside out
- outside in
"""


def main():
    p1 = Game.Avatar("me")

    for i in range(999):
        p1.lv = 1000
    del i

    p1._ATK = p1.ATK * 999

    Game.Commands.ShowCmds()
    while True:
        p1.CmdInterface(Game.basicCmds)


# only when directly script is open it executes.
if __name__ == "__main__":
    main()