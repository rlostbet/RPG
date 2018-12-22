from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from myTool import Line

from chatbot_cmds import GetWords, CheckForCmd
from chatbot_interact import respondSequence


bot = ChatBot('Bot')
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.gossip"
    "chatterbot.corpus.englsih.humor"
    "chatterbot.corpus.englsih.botprofile"
)

# for multi lingual
# bot.train("chatterbot.corpus.korean")

while True:
    words = GetWords()

    if words[0].capitalize() == "Quit":
        break

    if CheckForCmd(words):
        pass

    else:
        message = " ".join(words)
        print(f"BOT: {bot.get_response(message)}")

bot.trainer.export_for_training('./export.yml')
