from components import quizVars
from PIL import Image

iron = Image.open("iron_man.jpg")
groot = Image.open("groot.jpg")
odin = Image.open("odin.jpg")
captainmarvel = Image.open("captain_marvel.jpg")

def total(value):

    if value == 4:
        quizVars.character = quizVars.characters[0]
        iron.show()
        print("It's " + quizVars.character)
    elif value == 8:
        quizVars.character = quizVars.characters[1]
        groot.show()
        print("It's " + quizVars.character)
    elif value == 10:
        quizVars.character = quizVars.characters[3]
        captainmarvel.show()
        print("It's " + quizVars.character)
    elif value == 14:
        quizVars.character = quizVars.characters[2]
        odin.show()
        print("It's " + quizVars.character)
    else:
        print("Couldn't guess your character :(")