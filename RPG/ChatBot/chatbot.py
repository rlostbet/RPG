import logging

from myTool import Line

from chatbot_cmds import GetWords, CheckForCmd
from chatbot_interact import respondSequence

# crtDir = os.getcwd()  # current directory
# sys.path.append(crtDir)

# 미연시?
# Basic interaction
# - greeting
# - cmd descs
# - guides.


def Main():

    while True:
        words = GetWords()

        if words[0].capitalize() == "Quit":
            break

        if CheckForCmd(words):
            pass

        else:
            for respond in respondSequence:
                respond(words)


if __name__ == '__main__':
    Main()
