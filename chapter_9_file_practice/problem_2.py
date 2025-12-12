#  the game() function in a program lets a user play a game  and return the score as an integer
# . you need to read a file "hi-score.tex" which is either blank or contain the pervious hi-score.
# you need to write a program to update the high score whenever  the game () function  breaks 
# the high-score


# i have doubt 

import random


def game():

    score = random.randint(1,500)
    print("you are playing the game")


    with open("highscore.txt") as f:
        highscore = f.read()


        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

        print(score)
    if score> highscore:
        with open("highscore.txt","w") as f:
            f.write(str(score))
    return score

game()