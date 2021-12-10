from components import quizVars
from PIL import Image


def total(value):

    if value == 4:
        quizVars.character = quizVars.characters[0]
        print("It's " + quizVars.character)
    elif value == 8:
        quizVars.character = quizVars.characters[1]
        print("It's " + quizVars.character)
    elif value == 10:
        quizVars.character = quizVars.characters[3]
        print("It's " + quizVars.character)
    else value == 14:
        quizVars.character = quizVars.characters[2]
        print("It's " + quizVars.character)