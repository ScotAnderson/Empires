from display.screenutilities import *
from random import randint
from time import sleep

currentYear = 0
numberOfHumanPlayers = 0
players = [
    ['Montaigne', 'Auveyron', 'Chevalier', 'Prince', 'Roi', 'Empereur', 'francs'],
    ['Arthur', 'Brittany', 'Sir', 'Prince', 'King', 'Emperor', 'francs'],
    ['Munster', 'Bavaria', 'Ritter', 'Prinz', 'Konig', 'Kaiser', 'marks'],
    ['Khotan', 'Quatara', 'Hasid', 'Caliph', 'Sheik', 'Shah', 'dinars'],
    ['Ferdinand', 'Barcelona', 'Caballero', 'Principe', 'Rey', 'Emperadore', 'peseta'],
    ['Hjodolf', 'Svealand', 'Riddare', 'Prins', 'Kung', 'Kejsare', 'krona']
]

#Pretty sure this stores various data about the players (ie, think 2 is amount of grain in storage, etc.)
# 0 is if the country/player is still alive. I *think* only AI players can die in random events...
# 1 is the amount of land the country currently has
# 2 is the amount of grain in the reserve
# 3 I think is the amount of serfs
# 4 is the amount of money in the treasury
# 7 is number of merchants
# 15 is number of soldiers
# 16 is how much of a palace has been built
# 17 is the index of the current title in the player array
# 18 is number of noobles
variableA = [
    #[0,     1,                         2,    3,    4, 5, 6,  7,  8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [0, 10000, 15000 + randint(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + randint(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + randint(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + randint(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + randint(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + randint(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15]
]

variableO = 0
#This seems to be the catch variable for when they use input for a pause (ie, show the summary and wait for enter to continue...)
variableZ = ""

#Suspect this is how much land the barbarians have...
variableBA = 6000

#This is the variable to determine if the game is over (someone has won)
variableKK = 0


def DoAITurn(playerNumber):
    pass

def DoHumanTurn(playerNumber):
    pass

def PrintYearSummary():
    ClearScreen();
    print("Summary")
    print("Nobles   Soldiers   Merchants   Serfs   Land    Palace\n")
    for i in range(0, 6):
        print("{0} {1} of {2}".format(players[i][variableA[i][17]], players[i][0], players[i][1]))
        print(" {0:3d}      {1:6,d}      {2:6,d}   {3:7,d}  {4:6,d}  {5:3d}%".format(variableA[i][18], variableA[i][15], variableA[i][7], variableA[i][3], variableA[i][1], variableA[i][16] * 10))
    pass

def MainLoop():
    global currentYear
    currentYear += 1
    ClearScreen()
    weather = randint(0, 5)
    PrintYear(currentYear, weather)
    sleep(4)

    # Do player turns (Human and AI)
    for playerNumber in range(0, 6):
        variableQF = 0
        if playerNumber >= numberOfHumanPlayers:
            DoAITurn(playerNumber)
        else:
            DoHumanTurn(playerNumber)

    PrintYearSummary()
    #Add wait for enter

def InitQuestions():
    global numberOfHumanPlayers
    ClearScreen()
    while numberOfHumanPlayers < 1 or numberOfHumanPlayers > 6:
        numPlayers = input('How many people are playing? ')
        try:
            numberOfHumanPlayers = int(numPlayers)
        except ValueError:
            print('Answer must be an integer 1-6')

    for i in range(0, numberOfHumanPlayers):
        players[i][0] = input('Who is the ruler of {}? '.format(players[i][1]));

PrintTitle()
InitQuestions()
MainLoop()


