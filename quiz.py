from quizComponents import quizVars

def calculate(answers, charVal, questionVal):
    score = 0
    for i in range(0,len(answers)):
        if answers[i] == 'Yes':
            score = score + questionVal['Points'][i]
    checker = 0
    for i in range(0, len(charVal['Scores'])):
        if charVal['Scores'][i] == score:
            checker = 1 
            return(charVal['Characters'][i])
    if checker == 0:
        return("No character found")
