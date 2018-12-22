from World import World, Humanoid, Life
from myTool import rLine, Line, Cap


# Exceptions
class GameError(Exception):
    """Exceptions Occured In game"""


class SaveError(GameError):
    """When Error occurs while saving game object"""

    def __init__(self, msg=None, *args):
        super().__init__(*args)
        self.msg = "An Error Occurred Saving Game" if msg is None else msg


class Game:

    @staticmethod
    def CreateAvatar():
        print("Name Your Character")
        name = input(">").capitalize()
        print("Chose Gender Of Your Character")

        gender = input(">").capitalize()

        # validate gender
        while(gender not in ("Male", "M", "F", "Female")):
            print("Again?")
            gender = input(">").capitalize()

        # Store Number for gender
        gender = 0 if gender in ("Male", "M") else 1
        return Avatar(name, gender)

    @staticmethod
    def SaveObj(load_name, save_name, mode="w"):
        try:
            path = "C:/Users/Seungwon/Documents/CS for Cool Stuff/OOL GAME/"
            start_i = None
            end_i = None

            modes = ("w", "w+", "a", "a+")
            if mode not in modes:
                raise SaveError("Wrong Mode")

            with open(path + load_name + ".py", "r") as f1:
                i = 0  # because f can't be index()-ed..
                lines = f1.readlines()
                for line in lines:
                    # find start point
                    if f"# +# {load_name.upper()} #+ #" in line:
                        start_i = i

                    # find end point
                    if f"# -# {load_name.upper()} #- #" in line:
                        end_i = i
                    i += 1
                del i

            if start_i is None:
                raise SaveError(f"Failed finding starting point of {load_name}")

            if end_i is None:
                raise SaveError(f"Failed finding ending point of {load_name}")

            lines = lines[start_i: end_i + 1]
            contents = "".join(lines)

            del lines

            with open(path + save_name + ".py", mode) as f2:
                f2.write("\n" + contents)

        except SaveError as err:
            print("SaveError: " + err.msg)

    def MovementCtrl():
        pass


class Commands(Game):

    def Say(noun="nothing"):
        print(f'You said {noun}')

    def Examine(objName=""):  # a bit to wide isn't it
        if objName in World.archive:
            # description
            pass

    def ShowCmds():
        string = ("Command Description\n" + rLine() + "\n")
        for key in cmdDescs:
            indentation = " " * (15 - len(key))
            string += (f"{key + indentation}: {cmdDescs[key]} \n")
        string += rLine()
        print(string)

    def ShowStatus(objName=""):     # by name..
        if objName in World.archive:
            print(World.archive[objName].GetStatus())
        else:
            print("Object Not Found")

    def Show(ObjName):
        if ObjName.capitalize == "Cmds":
            Commands.ShowCmds()

        else:
            Commands.ShowStatus(ObjName)

# class Interface(Game):
cmdDescs = {
    "Say [text]": "Say something([text]) to the world",
    "Examine [obj]": "Examine, roughly describe a Object",
    "Show [obj]": "Show detailed Status the object",
    "Show_cmds": "Show Descriptions of Basic Commands",
    "Attack [obj]": "Avatar Dammages Living Object"  # also some non-living?
}

basicCmds = {
    "Say": Commands.Say,
    "Examine": Commands.Examine,
    "Show": Commands.Show,
    "Attack": "avatar.Attack",  # hmmm
    "Show_cmds": Commands.ShowCmds
}


class Avatar(Game, Humanoid):
    # normal Wolrd Features
    # Game Features:
    #   - Controlable
    #   - Reviving
    #   - Going Back The Events.

    archive = {}

    def __init__(self, name, *args):
        super().__init__(name, *args)
        Avatar.archive[name] = self
        self.lv = 1

    def Attack(self, objName):
        if objName in Life.archive:
            foe = World.archive[objName]
            foe.health = foe.health - self.ATK
            print(f"{self.name} Attacks {foe.name}.\n {self.ATK} Dammage!")
        else:
            print("Target not Found")

    def CmdInterface(avatar, cmds=Commands.basicCmds):
        # need ? ava = Avatar.archive[Avatar_name]

        userInput = input(">").split()

        # no empty input
        while userInput == []:
            userInput = input(">").split()

        # upper only 1st char
        cmdName = Cap(userInput[0])

        if cmdName not in cmds:
            print(f"- Unknown command {cmdName}")

        else:
            Cmd = cmds[cmdName]

            if isinstance(Cmd, str):
                Cmd = eval(Cmd)

            # single Parameter.
            if len(userInput) == 1:
                Cmd()

            else:
                parameter = " ".join(userInput[1:])
                Cmd(parameter)
