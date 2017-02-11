from display.screenutilities import *
from random import randint, random
from time import sleep
from math import sqrt

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
randDeathStrings = [
    '{0} has been assassinated by an ambitions\noble',
    '{0} has been killed from a fall during\nthe annual fox-hunt.',
    '{0} died of acute food poisoning.\nThe royal cook was summarily executed.',
    '{0} passed away this winter from a weak heart.'
]

def safeRandInt(lower, upper):
    if lower >= upper:
        return upper
    return randint(lower, upper)

#Pretty sure this stores various data about the players (ie, think 2 is amount of grain in storage, etc.)
# 0 is if the country/player is still alive. (0 is alive, 1 is dead)
# 1 is the amount of land the country currently has
# 2 is the amount of grain in the reserve
# 3 s the amount of serfs
# 4 is the amount of money in the treasury
# 5 is the number of bushels on the grain market
# 6 is the price of the bushels on the grain market
# 7 is number of merchants
# 8 is the customs tax
# 9 is the sales tax
# 10 is the income tax
# 11 is the number of marketplaces
# 12 is the number of grain mills
# 13 is the number of foundries
# 14 is number of shipyards?
# 15 is number of soldiers
# 16 is how much of a palace has been built
# 17 is the index of the current title in the player array
# 18 is number of nobles
# 19 is how well the army fights between 5 (at 50%) and 15 (at 150%)
playerData = [
    #[0,    1,                             2,    3,    4, 5, 6,  7,  8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [0, 10000, 15000 + safeRandInt(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + safeRandInt(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + safeRandInt(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + safeRandInt(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + safeRandInt(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15],
    [0, 10000, 15000 + safeRandInt(1, 10000), 2000, 1000, 0, 0, 25, 20, 5, 35,  0,  0,  0,  0, 20,  0,  2,  1, 15]
]

variableO = 0

#This seems to be the catch variable for when they use input for a pause (ie, show the summary and wait for enter to continue...)
variableZ = ""

#Suspect this is how much land the barbarians have...
barbarianLands = 6000

def GetFullPlayerName(playerNumber):
    return "{0} {1} of {2}".format(players[playerNumber][playerData[playerNumber][17]], players[playerNumber][0], players[playerNumber][1])


# Original code 395- - 409
def CheckForPlague(playerNumber):
    if random() <= 0.02:
        ClearScreen();
        print("                      P L A G U E  ! ! !");
        print("Black death has struck your nation.");
        
        serfs = safeRandInt(1, int(playerData[playerNumber][3] / 2))
        playerData[playerNumber][3] = playerData[playerNumber][3] - serfs
        print("{0} serfs died.".format(serfs));

        merchants = safeRandInt(1, int(playerData[playerNumber][7] / 3))
        playerData[playerNumber][7] = playerData[playerNumber][7] - merchants
        print("{0} merchants died.".format(merchants));

        soldiers = safeRandInt(1, int(playerData[playerNumber][15] / 3))
        playerData[playerNumber][15] = playerData[playerNumber][15] - soldiers
        print("{0} soldiers died.".format(soldiers));
        
        nobles = safeRandInt(1, int(playerData[playerNumber][18] / 3))
        playerData[playerNumber][18] = playerData[playerNumber][18] - nobles
        print("{0} nobles died.".format(soldiers));

        sleep(8)


def DoAITurn(playerNumber, weather):
    # It is very unclear what this line is doing
    # 413 FOR Q = 1 TO NP : If A(Q, 0) <> 0 Next Q : PRINT : End

    if playerData[playerNumber][0] != 0:
        return

    variableDS = 0;
    ClearScreen()
    print("One moment -- {0} {1}'s turn . . .".format(players[playerNumber][playerData[playerNumber][17]], players[playerNumber][0]))
    sleep(1)

    CheckForRandomDeath(playerNumber)

    if playerData[playerNumber][0] != 0:
        return

    variableQ2 = 0
    variableQ3 = 0
    variableQ4 = 0
    variableQ5 = 0
    variableQ6 = 0
    variableQ7 = 0
    variableQ8 = 0
    variableQ9 = 0
    variableQ0 = 0
    variableQB = 0
    variableQC = 0
    variableQD = 0
    variableQP = 0

    for q in range(0, numberOfHumanPlayers):
        if playerData[q][0] == 0:
            variableQP = variableQP + 1
            variableQ2 = playerData[q][3] + variableQ2
            variableQ3 = playerData[q][5] + variableQ3
            variableQ4 = playerData[q][6] + variableQ4
            variableQ5 = playerData[q][4] + variableQ5
            variableQ6 = playerData[q][7] + variableQ6
            variableQ7 = playerData[q][11] + variableQ7
            variableQ8 = playerData[q][12] + variableQ8
            variableQ9 = playerData[q][13] + variableQ9
            variableQ0 = playerData[q][14] + variableQ0
            variableQB = playerData[q][16] + variableQB
            variableQC = playerData[q][18] + variableQC
            variableQD = playerData[q][19] + variableQD

    variableQ2 = variableQ2 / variableQP
    variableQ3 = variableQ3 / variableQP
    variableQ4 = variableQ4 / variableQP
    variableQ5 = variableQ5 / variableQP
    variableQ6 = variableQ6 / variableQP
    variableQ7 = variableQ7 / variableQP
    variableQ8 = variableQ8 / variableQP
    variableQ9 = variableQ9 / variableQP
    variableQ0 = variableQ0 / variableQP
    variableQB = variableQB / variableQP
    variableQC = variableQC / variableQP
    variableQD = variableQD / variableQP

    while True:
        variableQ2 = int(variableQ2 + safeRandInt(1, 200) - safeRandInt(1, 200))
        variableQ3 = int(variableQ3 + safeRandInt(1, 1000) - safeRandInt(1, 1000))
        variableQ4 = variableQ4 + random() - random()
        variableQ5 = int(variableQ5 + safeRandInt(1, 1500) - safeRandInt(1, 1500))
        variableQ6 = int(variableQ6 + safeRandInt(1, 25) - safeRandInt(1, 25))
        if variableQ4 < 0:
            variableQ4 = 0
        else:
            break

    variableQ7 = int(variableQ7 + safeRandInt(1, 4) - safeRandInt(1, 4))
    variableQ8 = int(variableQ8 + safeRandInt(1, 2) - safeRandInt(1, 2))
    if random() <= 0.3:
        variableQ9 = int(variableQ9 + safeRandInt(1, 2) - safeRandInt(1, 2))
        variableQ0 = int(variableQ0 + safeRandInt(1, 2) - safeRandInt(1, 2))
        if random() <= 0.5:
            variableQB = int(variableQB + safeRandInt(1, 2) - safeRandInt(1, 2))
            variableQC = int(variableQC + safeRandInt(1, 2) - safeRandInt(1, 2))

    playerData[playerNumber][3] = variableQ2
    if variableQ3 > playerData[playerNumber][5] and safeRandInt(1, 9) > 6:
        playerData[playerNumber][5] = variableQ3
        playerData[playerNumber][6] = variableQ4
        if weather < 3:
            playerData[playerNumber][6] = playerData[playerNumber][6] + random() / 1.5


    playerData[playerNumber][4] = variableQ5
    if variableQ6 > playerData[playerNumber][7]:
        playerData[playerNumber][7] = variableQ6

    if variableQ7 > playerData[playerNumber][11]:
        playerData[playerNumber][11] = variableQ7

    if variableQ8 > playerData[playerNumber][12]:
        playerData[playerNumber][12] = variableQ8

    if variableQ9 > playerData[playerNumber][13]:
        playerData[playerNumber][13] = variableQ9

    if variableQ0 > playerData[playerNumber][14]:
        playerData[playerNumber][14] = variableQ0

    if variableQB > playerData[playerNumber][16]:
        playerData[playerNumber][16] = variableQB

    if variableQC > playerData[playerNumber][18]:
        playerData[playerNumber][18] = variableQC

    playerData[playerNumber][15] = 10 * playerData[playerNumber][18] + safeRandInt(1, 10 * playerData[playerNumber][18])
    variableIQ = 0

    while (playerData[playerNumber][15] / variableQ2 > playerData[playerNumber][13] * .01 + .05):
        playerData[playerNumber][15] = playerData[playerNumber][15] / 2

    playerData[playerNumber][19] = variableQD
    CheckForTitles(playerNumber)
    sleep(4)


    variableQ = safeRandInt(1, numberOfHumanPlayers)
    while playerData[variableQ][0] != 0:
        variableQ = safeRandInt(1, numberOfHumanPlayers)

    if playerData[playerNumber][5] < 1:
        doAIAttack(playerNumber)


    while True:
        variableQR = random() * playerData[variableQ][5]
        if variableQR * playerData[variableQ][6] < playerData[playerNumber][4]:
            playerData[variableQ][4] = playerData[variableQ][4] + int(variableQR * playerData[variableQ][6] * 90) / 100
            playerData[variableQ][5] = playerData[variableQ][5] - variableQR
            doAIAttack(playerNumber)
            break
        else:
            if safeRandInt(1, 9) <= 3:
                doAIAttack(playerNumber)
                break

def doAIAttack(playerNumber):
    if safeRandInt(1, 9) < 2:
        return

    if currentYear < 3:
        variableI = 0

        if barbarianLands < 0:
            return
        else:
            variableQF = 1
            variableI1 = safeRandInt(1, playerData[playerNumber][15])
            #TODO: Jump into attack here
            variableQF = 0
            #variableIQ = variableIQ + 1

            if playerData[playerNumber][15] > 30 and variableIQ < playerData[playerNumber][18] / 4:
                doAIAttack(playerNumber)

                                     





# Original code 359 - 369
def CheckForTitles(playerNumber):
    # Check for the "prince" title
    if playerData[playerNumber][11] > 7 and \
       playerData[playerNumber][12] > 3 and \
       playerData[playerNumber][16] > 1 and \
       (playerData[playerNumber][1] / playerData[playerNumber][3]) > 4.8 and \
       playerData[playerNumber][3] > 2300 and \
       playerData[playerNumber][18] > 10:
        playerData[playerNumber][17] = 3

    # Check for the "king" title
    if playerData[playerNumber][11] > 13 and \
       playerData[playerNumber][12] > 5 and \
       playerData[playerNumber][13] > 0 and \
       playerData[playerNumber][16] > 5 and \
       (playerData[playerNumber][1] / playerData[playerNumber][3]) > 5.0 and \
       playerData[playerNumber][3] > 2600 and \
       playerData[playerNumber][18] > 25:
        playerData[playerNumber][17] = 4

    # Check for the "Emperor" title
    if playerData[playerNumber][17] > 3 and \
       playerData[playerNumber][16] > 9 and \
       playerData[playerNumber][4] > 3100 and \
       playerData[playerNumber][18] > 40:
        ClearScreen()
        playerData[playerNumber][17] = 5
        print("Game over . . .")
        print("{0} Wins !\n\n".format(GetFullPlayerName(playerNumber)))
        PrintYearSummary()
        exit()

    # In the original code, there is a check here for QF = 1, which either results in a sleep, or a full return (which ends the players turn)
    # QF = 1 is set for the AI turns, so humans have a change to see it most likely.

def DoHumanTurn(playerNumber, weather):
    CheckForPlague(playerNumber)
    starvationDeaths = 0
    variableIQ = 1

    #usableLand = allLand                    - numberSerfs                 - (numberNobles * 2)                 - howMuchOfPalaceWasBuilt      - numberOfMerchants           - (numberSoldiers * 2)
    usableLand = playerData[playerNumber][1] - playerData[playerNumber][3] - (playerData[playerNumber][18] * 2) - playerData[playerNumber][16] - playerData[playerNumber][7] - (playerData[playerNumber][15] * 2)

    #peopleGrainDemands = (numberSerfs                 + numberMerchants             + (numberNobles *))                  * 5
    peopleGrainDemands = (playerData[playerNumber][3] + playerData[playerNumber][7] + (playerData[playerNumber][18] * 3)) * 5
   
    armyGrainDemands = playerData[playerNumber][15] * 8


    playerData[playerNumber][19] = 15

    if playerData[playerNumber][0] != 0:
        return

    CheckForTitles(playerNumber)

    if playerData[playerNumber][2] * 3 < usableLand:
        usableLand = playerData[playerNumber][2] * 3

    if playerData[playerNumber][3] * 5 < usableLand:
        usableLand = playerData[playerNumber][3] * 5

    playerData[playerNumber][2] = playerData[playerNumber][2] - usableLand / 3
    grainHarvest = usableLand * weather * 0.72 + safeRandInt(1, 501) - playerData[playerNumber][13] * 500
    ratsAte = safeRandInt(1, 31)
    playerData[playerNumber][2] = playerData[playerNumber][2] - playerData[playerNumber][2] * ratsAte / 100
    if grainHarvest < 0:
        grainHarvest = 0
    
    playerData[playerNumber][2] = playerData[playerNumber][2] + grainHarvest

    starvationDeaths, immigrations = DoMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
    CheckForHumanPlayerRandomDeath(playerNumber, starvationDeaths)

    DoTaxesAndInvestments(playerNumber, grainHarvest, immigrations, weather)
    # TODO: Continue turn with Taxes and Investments! (line 189 from the original code)

    DoAttacks(playerNumber)

def PrintAttacks():
    print('Land holdings:\n')
    print('1)  Barbarians\t{0}'.format(barbarianLands))

    for i in range(1, 6):
        if playerData[i][0] == 0:
            print('{0})  {1}\t{2}'.format(i + 1, players[i][1], playerData[i][1]))

    print('\n\n\n')


def DoAttacks(playerNumber):
    global barbarianLands

    attacksSoFar = 0
    attacksPerTurn = int(playerData[playerNumber][18] / 4 + 1)

    while True:
        ClearScreen()
        PrintAttacks()

        attackInput = input('Who do you wish to attack (give #)? ')
        try:
            attack = int(attackInput)
            if attack < 0 or attack > 7:
                continue

            if attack == 0:
                return

            if attack == playerNumber + 2:
                print('{0}, Please think again.  You are #{1}!'.format(players[playerNumber][playerData[playerNumber][17]], attack))
                sleep(4)
                continue

            if attack > 1 and currentYear < 3:
                print('Due to international treaty, you cannot attack other\nnations until the third year.')
                sleep(4)
                continue

            if attack == 1 and barbarianLands < 1:
                print('All barbarian lands have been seized')
                sleep(4)
                continue

            if attack > 1 and playerData[attack - 2][0] != 0:
                print('That player is no longer in the game')
                sleep(4)
                continue

            if attacksSoFar >= attacksPerTurn:
                print('Due to a shortage of nobles , you are limited to only\n{0} attacks per year'.format(attacksPerTurn))
                sleep(4)
                continue

            while True:
                ClearScreen()
                PrintAttacks()
    
                soldiersInput = input('How many soldiers do you wish to send? ')

                try:
                    soldiers = int(soldiersInput)

                    if soldiers < 1:
                        break

                    if soldiers > playerData[playerNumber][15]:
                        print('Think again... You have only {0} soldiers'.format(playerData[playerNumber][15]))
                        sleep(4)
                        continue

                    Attack(playerNumber, attack - 2, soldiers, False)
                    attacksSoFar += 1
                    break

                except ValueError:
                    continue


        except ValueError:
            break
            

def PrintAttackInternal(aggressor, defender, aggressorSoldiers, defenderSoldiers):
    print('\n\n                                        Soldiers remaining:')
    print('\n             {0}:\t{1}'.format(GetFullPlayerName(aggressor), aggressorSoldiers))

    if defender < 0:
        print('                       Pagan barbarians:\t{0}'.format(defenderSoldiers))
    else:
        print('             {0}:\t{1}'.format(GetFullPlayerName(defender), defenderSoldiers))


    #     PRINT@269,Z(K,A(K,17));" ";Z(K,0);" of ";Z(K,1);":"
    #     PRINT@169,"Soldiers remaining:";
    #     PRINT@333,Z(I,A(I,17));" ";Z(I,0);" of ";Z(I,1);":"
    #     PRINT@512,Z(I,1);"'s serfs are forced to defend their country!"
    #     PRINT@306,CHR$(30);:PRINT@306,INT(I1);:PRINT@370,CHR$(30);:PRINT@370,INT(I2);:



# I0 == defenders available land
# I1 == attacking soldiers
# I2 == defending soldiers
# I3 == defending soldier strength
# I4 == attackers soldier strength
# I5 == lands seized
# IH == flag for if serfs are defending?
# O1 == how long to take per tick, to keep combat from being too fast for low numbers of soldiers?
# I7 == how many soldiers to lose per tick?
    

def Attack(aggressor, defender, aggressorSoldiers, aiTurn):
    aggressorSoldierStrength = playerData[aggressor][19]
    landsSeized = 0
    defenderSoldiers = playerData[defender][15]
    defenderLands = playerData[defender][1]
    variableO1 = 75 - aggressorSoldiers - defenderSoldiers
    playerData[aggressor][15] = playerData[aggressor][15] - aggressorSoldiers
    variableIH = 0

    if defender < 0:
        defenderSoldiers = safeRandInt(1, safeRandInt(1, aggressorSoldiers * 3)) + safeRandInt(1, safeRandInt(1, aggressorSoldiers * 1.5))
        defenderSoldierStrength = 9
        defenderLands = barbarianLands
        variableO1 = 75 - aggressorSoldiers - defenderSoldiers
    else:
        defenderSoldierStrength = playerData[defender][19]

        if playerData[defender][15] < 1:
            defenderSoldiers = playerData[defender][3]
            defenderSoldierStrength = 5
            variableIH = 1
            variableO1 = -1

    while True:
        ClearScreen()
        PrintAttackInternal(aggressor, defender, aggressorSoldiers, defenderSoldiers)
        sleep(.5)

        variableI7 = int(aggressorSoldiers / 15) + 1
        if safeRandInt(1, aggressorSoldierStrength) < safeRandInt(1, defenderSoldierStrength):
            aggressorSoldiers = aggressorSoldiers - variableI7
        else:
            landsSeized = landsSeized + safeRandInt(1, variableI7 * 26) - safeRandInt(1, variableI7 + 5)
            defenderSoldiers = defenderSoldiers - variableI7
            if landsSeized < 0:
                landsSeized = 0

        if defenderLands - landsSeized < 0:
            BattleOver2(aggressor, defender, landsSeized, aggressorSoldiers, aiTurn)
            return    

        if aggressorSoldiers > 0 and defenderSoldiers > 0:
            continue

        if aggressorSoldiers < 0:
            aggressorSoldiers = 0

        if defenderSoldiers < 0:
            defenderSoliders = 0

        if variableIH == 1 and aggressorSoldiers > 0:
            BattleOver2(aggressor, defender, landsSeized, aggressorSoldiers, aiTurn)
            return

        BattleOver1(aggressor, defender, landsSeized, aggressorSoldiers, aiTurn)
        return



def PauseOrWait(aiTurn):
    if aiTurn == True:
        sleep(4)
    else:
        input('<Enter>?')


def BattleOver1(playerNumber, defender, landsSeized, remainingSoldiers, aiTurn):
    global barbarianLands

    ClearScreen()
    print('\n                       Battle over\n')

    if remainingSoldiers > 0:
        print('The forces of {0} {1} were victorious.'.format(players[playerNumber][playerData[playerNumber][17]], players[playerNumber][0]))
        print('{0} acres were seized'.format(landsSeized))
    else:
        print('{0} {1} was defeated.'.format(players[playerNumber][playerData[playerNumber][17]], players[playerNumber][0]))
        if landsSeized < 2:
            landsSeized = 0
            print('{0} acres were seized'.format(landsSeized))
        else:
            landsSeized = int(landsSeized / safeRandInt(1, 3))
            print('In your defeat you nevertheless managed to capture {0} acres.'.format(landsSeized))

    if defender < 0:
        playerData[playerNumber][15] = playerData[playerNumber][15] + remainingSoldiers
        playerData[playerNumber][1] = playerData[playerNumber][1] + landsSeized
        barbarianLands = barbarianLands - landsSeized
        PauseOrWait(aiTurn)
    else:
        if landsSeized > playerData[defender][5] / 3:
            if playerData[defender][3] > 0:
                variableI6 = safeRandInt(1, playerData[defender][3])
                print('{0} enemy serfs were beaten and murdered by your troops!'.format(variableI6))
                playerData[defender][3] = playerData[defender][3] - variableI6

            if playerData[defender][11] > 0:
                variableI6 = safeRandInt(1, playerData[defender][11])
                print('{0} enemy marketplaces were destroyed'.format(variableI6))
                playerData[defender][11] = playerData[defender][11] - variableI6

            if playerData[defender][2] > 0:
                variableI6 = safeRandInt(1, playerData[defender][2])
                print('{0} bushels of enemy grain were burned'.format(variableI6))
                playerData[defender][2] = playerData[defender][2] - variableI6

            if playerData[defender][12] > 0:
                variableI6 = safeRandInt(1, playerData[defender][12])
                print('{0} enemy grain mills were sabotaged'.format(variableI6))
                playerData[defender][12] = playerData[defender][12] - variableI6
            
            if playerData[defender][13] > 0:
                variableI6 = safeRandInt(1, playerData[defender][13])
                print('{0} enemy foundries were leveled'.format(variableI6))
                playerData[defender][13] = playerData[defender][13] - variableI6

            if playerData[defender][14] > 0:
                variableI6 = safeRandInt(1, playerData[defender][14])
                print('{0} enemy shipyards were over-run'.format(variableI6))
                playerData[defender][14] = playerData[defender][14] - variableI6

            if playerData[defender][18] > 2:
                variableI6 = safeRandInt(1, playerData[defender][18] / 2)
                print('{0} enemy nobles were summarily executed'.format(variableI6))
                playerData[defender][18] = playerData[defender][18] - variableI6

            playerData[playerNumber][1] = playerData[playerNumber][1] + landsSeized
            playerData[defender][1] = playerData[defender][1] - landsSeized

            PauseOrWait(aiTurn)
        else:
            playerData[playerNumber][15] = playerData[playerNumber][15] + remainingSoldiers
            playerData[playerNumber][1] = playerData[playerNumber][1] + landsSeized

            if variableIH == 1:
                variableIH = 0
                playerNumber[defender][15] = 0
                playerNumber[defender][3] = variableI2
                playerNumber[defender][1] = playerNumber[defender][1] - landsSeized
                PauseOrWait(aiTurn)

            playerData[defender][15] = varaibleI2
            playerData[defender][1] = playerData[defender][1] - landsSeized
            PauseOrWait(aiTurn)



def BattleOver2(playerNumber, defender, landsSeized, remainingSoldiers, aiTurn):
    global barbarianLands

    ClearScreen()
    print('\n                       Battle over')
    if defender < 0:
        print('All barbarian lands have been seized\nThe remaining barbarians fled')
        playerData[playerNumber][1] = playerData[playerNumber][1] + landsSeized
        playerData[playerNumber][15] = playerData[playerNumber][15] + remainingSoldiers
        barbarianLands = 0

    else:
        print('The country of {0} was overrun!'.format(players[defender - 1][1]))
        print('All enemy nobles were summarily executed!\n\n')
        print('The remaining enemy soldiers were imprisoned. All enemy serfs')
        print('have pledged oaths of fealty to you, And should now be consid-')
        print('ered to be your people too. All enemy merchants fled the coun-')
        print('try. Unfortunately, all enemy assets were sacked and destroyed')
        print('by your revengeful army in a drunken riot following the victory')
        print('celebration.')

        if variableIH == 1:
            variableIH = 0
            playerData[defender][3] = variableI2

        playerData[playerNumber][15] = playerData[playerNumber][15] + remainingSoldiers
        playerData[playerNumber][1] = playerData[playerNumber][1] + playerData[defender][1]
        playerData[defender][1] = 0
        playerData[defender][0] = 1
        playerData[playerNumber][3] = playerData[playerNumber][3] + playerData[defender][3]

    PauseOrWait(aiTurn)



def DoTaxesAndInvestments(playerNumber, grainHarvest, immigrations, weather):
    # [ is apparently the power operator in TRS80 basic X[.9 means x to the power of .9
 
    # marketProfit = (numMarkets * ((numMerchants + RND(35) + RND(35)) / (salesTax + 1) * 12 + 5)) [ .9
    marketProfit = (playerData[playerNumber][11] * ((playerData[playerNumber][7] + safeRandInt(1, 35) + safeRandInt(1, 35)) / (playerData[playerNumber][9] + 1) * 12 + 5)) ** .9
    
    # millProfit = (numMills * (5.8 * (harvest + RND(250)) / (incomeTax * 20 + salesTax * 40 + 10) + 150)) [ .9
    millProfit = (playerData[playerNumber][12] * (5.8 * (grainHarvest + safeRandInt(1, 250)) / (playerData[playerNumber][10] * 20 + playerData[playerNumber][9] * 40 + 10) + 150)) ** .9

    # foundryProfit = (numFoundry * (numSoldiers + RND(150) + 400)) [ .9
    foundryProfit = (playerData[playerNumber][13] * (playerData[playerNumber][15] + safeRandInt(1, 150) + 400)) ** .9

    # shipyardProfit = (numShipyard * (numMerchants * 4 + numMarkets * 9 + numFoundry * 15) * weather) [ .9
    shipyardProfit = (playerData[playerNumber][14] * (playerData[playerNumber][7] * 4 + playerData[playerNumber][11] * 9 + playerData[playerNumber][13] * 15) * weather) ** .9

    # soldierCost = numSoldiers * (-8)
    soldierCost = playerData[playerNumber][15] * -8

    # customsCollected = immigrations * (RND(40) + RND(40)) / 100 * customsTax
    customsCollected = immigrations * (safeRandInt(1, 40) + safeRandInt(1, 40)) / 100 * playerData[playerNumber][8]

    # salesCollected = salesTax / 100 * ((numMerchants * 1.8 + marketProfit * 33 + millProfit * 17 + foundryProfit * 50 + shipyardProfit * 70) [ .85 + numMobles * 5 + numSerfs)
    salesCollected = playerData[playerNumber][9] / 100 * ((playerData[playerNumber][7] * 1.8 + marketProfit * 33 + millProfit * 17 + foundryProfit * 50 + shipyardProfit * 70) ** .85 + playerData[playerNumber][18] * 5 + playerData[playerNumber][3])

    # incomeCollected = (incomeTax / 100 * (numSerfs * 1.3 + numNobles * 145 + numMerchants * 39 + numMarkets * 99 + numMills * 99 + numFoundry * 425 + numShipyards * 965)) [ .97
    incomeCollected = (playerData[playerNumber][10] / 100 * (playerData[playerNumber][3] * 1.3 + playerData[playerNumber][18] * 145 + playerData[playerNumber][7] * 39 + playerData[playerNumber][11] * 99 + playerData[playerNumber][12] * 99 + playerData[playerNumber][13] * 425 + playerData[playerNumber][14] * 965)) ** .97
    
    # treasury = treasury + marketProfit + millProfit + foundryProfit + shipyardProfit + soldierCost + customsCollected + salesCollected + incomeCollected
    playerData[playerNumber][4] = playerData[playerNumber][4] + marketProfit + millProfit + foundryProfit + shipyardProfit + soldierCost + customsCollected + salesCollected + incomeCollected
    playerData[playerNumber][18] = int(playerData[playerNumber][18])

    exitTaxes = False
    while True:
        exitTaxes, menuItemSelected = TaxesInternal(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        if exitTaxes == True:
            break
        SetTax(menuItemSelected, playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        del menuItemSelected

    exitInvestments = False
    while  True:
        exitInvestments, menuItemSelected = InvestmentsInternal(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        if exitInvestments == True:
            break
        SetInvestment(menuItemSelected, playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        del menuItemSelected


investmentType = [
    [1000],
    [2000],
    [7000],
    [8000],
    [8],
    [5000]
]

def SetInvestment(taxIndex, playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost):
    variableJ = 0
    variableH = 0    

    cost = investmentType[taxIndex - 1][0]
    if taxIndex == 1:
        variableJ = safeRandInt(1, 7)
    if taxIndex == 6:
        variableH = safeRandInt(1, 4)

    while True:
        ClearScreen()
        PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        amountInput = input('How many? ')
        try:
            amount = int(amountInput)
            if amount < 0:
                continue

            if amount == 0:
                return

            if playerData[playerNumber][4] < cost * amount:
                ClearScreen()
                PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
                print('Think again . . .You only have {0} {1}'.format(playerData[playerNumber][4], players[playerNumber][6]))
                sleep(4)
                continue

            if amount + (amount - 1) * (variableJ + variableH) > playerData[playerNumber][3]:
                ClearScreen()
                PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
                print('You don\'t have enough serfs to train')
                sleep(4)
                continue

            if cost == 8:
                people = playerData[playerNumber][3] + playerData[playerNumber][7] + playerData[playerNumber][18]
                if (amount + playerData[playerNumber][15]) / people > .05 + playerData[playerNumber][13] * .015:
                    ClearScreen()
                    PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
                    print('You cannot equip and maintain so many troops, {0}.'.format(players[playerNumber][playerData[playerNumber][17]]))
                    sleep(4)
                    continue

            playerData[playerNumber][15] = int(playerData[playerNumber][15])

            if cost == 8 and amount + playerData[playerNumber][15] > playerData[playerNumber][18] * 20:
                ClearScreen()
                PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
                print('Please think again . . . You only have {0} nobles\nto lead your troops.'.format(int(playerData[playerNumber][18] + .5)))
                sleep(4)
                continue

            if cost == 8:
                playerData[playerNumber][3] = playerData[playerNumber][3] - amount
            else:
                playerData[playerNumber][7] = playerData[playerNumber][7] + variableJ * amount
                playerData[playerNumber][18] = playerData[playerNumber][18] + variableH * amount
                playerData[playerNumber][3] = playerData[playerNumber][3] - (variableJ + variableH) * amount

            playerData[playerNumber][4] = playerData[playerNumber][4] - amount * cost
            playerData[playerNumber][10 + taxIndex] = playerData[playerNumber][10 + taxIndex] + amount
            variableKL = 1
            return

        except ValueError:
            continue


taxType = [
    ['Give new customs tax (max=50%)? ', 50],
    ['Give new sales tax (max=20%)? ', 20],
    ['Give new income tax (max=35%)? ', 35]
]

def SetTax(taxIndex, playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost):
    while True:
        ClearScreen()
        PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        taxInput = input(taxType[taxIndex - 1][0])

        try:
            tax = float(taxInput)
            if tax < 0 or tax > taxType[taxIndex - 1][1]:
                continue
            playerData[playerNumber][taxIndex + 7] = tax
            break
        except ValueError:
            pass        

def TaxesInternal(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost):
    exitTaxes = False
    menuItemSelected = 0
    while (menuItemSelected < 1 or menuItemSelected > 3) and exitTaxes == False:
        ClearScreen()
        PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        menuItem = input('1) Customs duty  2) Sales tax  3) Income tax? ')
        try:
            menuItemSelected = int(menuItem)
        except ValueError:
            exitTaxes = True

    return exitTaxes, menuItemSelected

def InvestmentsInternal(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost):
    exitInvestments = False
    menuItemSelected = 0
    while (menuItemSelected < 1 or menuItemSelected > 6) and exitInvestments == False:
        ClearScreen()
        PrintTaxesAndInvestments(playerNumber, customsCollected, salesCollected, incomeCollected, marketProfit, millProfit, foundryProfit, shipyardProfit, soldierCost)
        menuItem = input('Any new investments (give #)? ')
        try:
            menuItemSelected = int(menuItem)
        except ValueError:
            exitInvestments = True

    return exitInvestments, menuItemSelected




def PrintTaxesAndInvestments(playerNumber,
                             customsCollected,
                             salesCollected,
                             incomeCollected,
                             marketProfit,
                             millProfit,
                             foundryProfit,
                             shipyardProfit,
                             soldierCost):
    print('State revenues:    Treasury={0:7,d} {1}'.format(int(playerData[playerNumber][4]), players[playerNumber][6]))
    print('Customs duty    Sales tax       Income tax')
    print(' {0} %            {1} %              {2} %'.format(int(playerData[playerNumber][8]), int(playerData[playerNumber][9]), int(playerData[playerNumber][10])))
    print(' {0}             {1}             {2}'.format(int(customsCollected + .5), int(salesCollected + .5), int(incomeCollected + .5)))
    print('\nInvestments     Number           Profits           Cost')
    print('1) Marketplaces  {0}                {1}                1000'.format(playerData[playerNumber][11], int(marketProfit)))
    print('2) Grain mills   {0}                {1}                2000'.format(playerData[playerNumber][12], int(millProfit)))
    print('3) Foundries     {0}                {1}                7000'.format(playerData[playerNumber][13], int(foundryProfit)))
    print('4) Shipyards     {0}                {1}                8000'.format(playerData[playerNumber][14], int(shipyardProfit)))
    print('5) Soldiers      {0}              {1}              8'.format(playerData[playerNumber][15], soldierCost))
    print('6) Palace        {0}% Completed                      5000\n\n'.format(playerData[playerNumber][16] * 10))
    #TODO: Fix the number padding on the above table so it looks right with various values

    #TODO Figure out what this KL variable eval code is for?
    #if variableKL == 1:
    #    variableKL = 0
    #    return


def BuyGrain(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    while True:
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        countryInput = input('From which country  (give #)? ')
        try:
            country = int(countryInput)
            if country == 0:
                return

            if country < 1 or country > 6:
                continue

            if playerData[country][0] == 1 or playerData[country][5] == 0:
                ClearScreen()
                PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
                print('That country has none for sale!')
                sleep(4)
                return

            if country == playerNumber:
                ClearScreen()
                PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
                print('You cannot buy grain that you have put onto the market!')
                sleep(4)
                continue

            while True:
                ClearScreen()
                PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
                bushelsInput = input('How many bushels? ')
                try:
                    bushels = int(bushelsInput)
                    if bushels > playerData[country][5]:
                        ClearScreen()
                        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
                        print('You can\'t buy more grain then they are selling!')
                        sleep(4)
                        continue

                    if bushels < 0:
                        break

                    cost = bushels * playerData[country][6] / .9
                    if cost > playerData[playerNumber][4]:
                        ClearScreen()
                        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
                        print('{0} {1} please reconsider -'.format(players[playerNumber][playerData[playerNumber][17]], playerData[playerNumber][0]))
                        print('You can only afford to buy {0} bushels'.format(playerData[playerNumber][4] * .9 / playerData[country][6]))
                        sleep(4)
                        continue

                    playerData[playerNumber][2] = playerData[playerNumber][2] + bushels
                    playerData[playerNumber][4] = playerData[playerNumber][4] - cost
                    playerData[country][4] = playerData[country][4] + cost * 0.9
                    playerData[country][5] = playerData[country][5] - bushels
                    return

                except ValueError:
                    pass

        except ValueError:
            pass


def SellGrain(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    while True:
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        bushelsInput = input('How many bushels do you wish to sell? ')
        try:
            bushels = int(bushelsInput)

            if bushels > playerData[playerNumber][2]:
                ClearScreen()
                PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
                print('{0} {1}, please think again'.format(players[playerNumber][playerData[playerNumber][17]], playerData[playerNumber][0]))
                print('You only have {0} bushels.'.format(playerData[playerNumber][2]))
                sleep(4)
                continue

            if bushels < 0:
                continue

            while True:
                ClearScreen()
                PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
                priceInput = input('What will be the price per bushel? ')
                try:
                    price = int(priceInput)
                    if price <= 0:
                        continue
                    if price > 15:
                        print('Be reasonable . . .even gold costs less than that!')
                        sleep(4)
                        continue

                    playerData[playerNumber][6] = (playerData[playerNumber][6] * playerData[playerNumber][5] + bushels * price) / (playerData[playerNumber][5] + bushels)
                    playerData[playerNumber][5] = playerData[playerNumber][5] + bushels
                    playerData[playerNumber][2] = playerData[playerNumber][2] - bushels
                    break
                except ValueError:
                    break
            break
        except ValueError:
            pass


def SellLand(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    global barbarianLands

    while True:
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        print('The barbarians will give you 2 {0} per acre'.format(players[playerNumber][6]))
        sleep(4)
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        acresInput = input('How many acres will you sell them? ')
        try:
            acres = int(acresInput)
            if acres > playerData[playerNumber][1] * .95:
                print('You must keep some land for the royal palace!')
                sleep(4)
                continue
            if acres < 0:
                continue

            playerData[playerNumber][4] = playerData[playerNumber][4] + (acres * 2)
            playerData[playerNumber][1] = playerData[playerNumber][1] - acres
            barbarianLands = barbarianLands + acres
            break
        except ValueError:
            pass

marketMenu = {1 : BuyGrain,
              2 : SellGrain,
              3 : SellLand}

def DoMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    exitMarket = False
    while True:
        exitMarket, menuItemSelected = MarketInternal(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        if exitMarket == True:
            break

        marketMenu[menuItemSelected](playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        menuItemSelected = 0
    
    armyShare = DoArmyGrainShare(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
    peopleShare = DoPeopleGrainShare(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands, armyShare)

    playerData[playerNumber][2] = playerData[playerNumber][2] - armyShare - peopleShare

    # Calculate the effectiveness of the soldiers
    playerData[playerNumber][19] = armyShare / (armyGrainDemands + 0.001) * 10
    if playerData[playerNumber][19] < 5:
        playerData[playerNumber][19] = 5
    if playerData[playerNumber][19] > 15:
        playerData[playerNumber][19] = 15

    return DoEndOfYear(playerNumber, peopleShare, peopleGrainDemands, armyShare, armyGrainDemands)


def PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    print(GetFullPlayerName(playerNumber))
    print("Rats ate {0}% of the grain reserve".format(ratsAte))
    print("Grain     Grain     People     Army       Royal")
    print("harvest   reserve   require    requires   treasury")
    print("{0:7,d}   {1:7,d}   {2:7,d}    {3:7,d}    {4:7,d}".format(int(grainHarvest), int(playerData[playerNumber][2]), int(peopleGrainDemands), int(armyGrainDemands), int(playerData[playerNumber][4])))
    print("bushels   bushels   bushels    bushels    {0}".format(players[playerNumber][6]))
    print("------Grain for sale:")
    print("\t\tCountry\t\tBushels\t\tPrice")

    grainForSale = False

    for i in range(0, 6):
        if (playerData[i][0] == 0 and playerData[i][5] > 0):
            grainForSale = True
            print("{0}\t\t{1}\t{2}\t\t{3}".format(i + 1, players[i][1], playerData[i][5], playerData[i][6]))

    if grainForSale == False:
        print("\n\n\nNo grain for sale . . .\n")


def MarketInternal(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    exitMarket = False
    menuItemSelected = 0
    while (menuItemSelected < 1 or menuItemSelected > 4) and exitMarket == False:
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        menuItem = input('1) Buy Grain 2) Sell Grain 3) Sell Land? ')
        try:
            menuItemSelected = int(menuItem)
        except ValueError:
            exitMarket = True

    return exitMarket, menuItemSelected



def DoArmyGrainShare(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    armyShare = -1
    while (armyShare < 0 or armyShare > playerData[playerNumber][2]):
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        shareInput = input('How many bushels will you give to your army of {0} men? '.format(playerData[playerNumber][15]))
        try:
            armyShare = int(shareInput)
            if armyShare > playerData[playerNumber][2]:
                print('You cannot give your army more grain than you have!')
                sleep(4)
        except ValueError:
            print('Answer must be an integer between 0 and the Grain Reserve Max.')
            sleep(4)
    return armyShare
  


def DoPeopleGrainShare(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands, armyShare):
    people = playerData[playerNumber][3] + playerData[playerNumber][7] + playerData[playerNumber][18]
    grainReserve = playerData[playerNumber][2] - armyShare
    peopleShare = -1
    while (peopleShare < (playerData[playerNumber][2] * 0.1) or peopleShare > playerData[playerNumber][2]):
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        shareInput = input('How many bushels will you give to your {0} people? '.format(people))
        try:
            peopleShare = int(shareInput)
            if peopleShare > playerData[playerNumber][2]:
                print('But you only have {0} bushels of grain!'.format(int(playerData[playerNumber][2])))
                sleep(4)
            elif peopleShare < (playerData[playerNumber][2] * 0.1):
                print('You must release at least 10% of the stored grain')
                sleep(4)
        except ValueError:
            print('Answer must be an integer betwen 10% and MAX of the Grain Reserve.')
            sleep(4)

    return peopleShare





def DoEndOfYear(playerNumber, peopleShare, peopleGrainDemands, armyShare, armyDemands):
    people = playerData[playerNumber][3] + playerData[playerNumber][7] + playerData[playerNumber][18]
    births = safeRandInt(1, int(people / 9.5))
    deaths = safeRandInt(1, int(people / 22))

    immigrations = 0

    if peopleShare > (peopleGrainDemands * 1.5):
        variableD = (sqrt(peopleShare - peopleGrainDemands) - safeRandInt(1, int(playerData[playerNumber][8] * 1.5)))
        if variableD >= 0:
            immigrations = safeRandInt(1, int(2 * variableD + 1))

    malnutritionDeaths = 0
    starvationDeaths = 0
    if peopleGrainDemands > (peopleShare * 2):
        starvationDeaths = safeRandInt(1, int(people / 16 + 1))
        malnutritionDeaths = safeRandInt(1, int(people / 12 + 1))
    elif peopleGrainDemands > peopleShare:
        malnutritionDeaths = safeRandInt(1, int(people / 15 + 1))

    populationChange = births - starvationDeaths - malnutritionDeaths - deaths + immigrations
    newMerchants = safeRandInt(1, int(immigrations / 5))
    newNobles = safeRandInt(1, int(immigrations / 25))
    playerData[playerNumber][7] = playerData[playerNumber][7] + newMerchants
    playerData[playerNumber][18] = playerData[playerNumber][18] + newNobles
    playerData[playerNumber][3] = playerData[playerNumber][3] + populationChange - newMerchants - newNobles

    armyStarvation = 0
    if armyDemands > (armyShare * 2):
        armyStarvation = safeRandInt(1, int(playerData[playerNumber][15] / 2 + 1))
        playerData[playerNumber][15] = playerData[playerNumber][15] - armyStarvation

    #This just seems to be the same army starvation code duplicated?
    variablePA = 0
    if armyShare * 2 < armyDemands:
        variablePA = safeRandInt(1, int(playerData[playerNumber][15] / 5))
        playerData[playerNumber][15] = playerData[playerNumber][15] - variablePA

    PrintMarketSummary(playerNumber, births, deaths, immigrations, malnutritionDeaths, starvationDeaths, armyStarvation, populationChange)
    return starvationDeaths, immigrations
            
def PrintMarketSummary(playerNumber, births, deaths, immigrations, malnutritionDeaths, starvationDeaths, armyStarvation, populationChange):
    ClearScreen()
    print('{0}:'.format(GetFullPlayerName(playerNumber)))
    print('In Year {0},'.format(currentYear))
    print('\n{0} babies were born'.format(births))
    print('{0} people died of disease'.format(deaths))

    if immigrations > 0:
        print('{0} people immigrated into your country.'.format(immigrations))

    if malnutritionDeaths > 0:
        print('{0} people died of malnutrition.'.format(malnutritionDeaths))

    if starvationDeaths > 0:
        print('{0} people starved to death.'.format(starvationDeaths))

    if armyStarvation > 0:
        print('{0} soldiers starved to death.'.format(armyStarvation))

    print('Your army will fight at {0}% effeciency.'.format(int(playerData[playerNumber][19] * 10 + .5)))
    direction = 'gained'
    if populationChange < 0:
        direction = 'lost'
    print('Your population {0} {1} citizens\n\n'.format(direction, abs(populationChange)))
    input('<Enter>?')


def CheckForHumanPlayerRandomDeath(playerNumber, starvationDeaths):
    if safeRandInt(1, starvationDeaths) > safeRandInt(1, 110):
        PrintVerySadNews()
        print('{0} has been assassinated\nby a crazed mother whose child had starved to death . . .'.format(GetFullPlayerName(playerNumber)))
        playerData[playerNumber, 0] = 1
        print('\n\nThe other nation-states have sent representatives to the\nfuneral')
        sleep(8)
    else:
        CheckForRandomDeath(playerNumber)

def CheckForRandomDeath(playerNumber):
    if random() <= 0.01:
        PrintVerySadNews()
        death = safeRandInt(0, 3)
        print(randDeathStrings[death].format(GetFullPlayerName(playerNumber)))
        playerData[playerNumber, 0] = 1
        print('\n\nThe other nation-states have sent representatives to the\nfuneral')
        sleep(8)

def PrintVerySadNews():
    ClearScreen()
    print("Very sad news ...\n")

def PrintYearSummary():
    print("Summary")
    print("Nobles   Soldiers   Merchants   Serfs   Land    Palace\n")
    for i in range(0, 6):
        print(GetFullPlayerName(i))
        print(" {0:3d}      {1:6,d}      {2:6,d}   {3:7,d}  {4:6,d}  {5:3d}%".format(playerData[i][18], playerData[i][15], playerData[i][7], playerData[i][3], playerData[i][1], playerData[i][16] * 10))




def MainLoop():
    global currentYear
    currentYear += 1
    ClearScreen()
    weather = safeRandInt(0, 5)
    PrintYear(currentYear, weather)
    sleep(4)

    # Do player turns (Human and AI)
    for playerNumber in range(0, 6):
        variableQF = 0
        if playerNumber >= numberOfHumanPlayers:
            DoAITurn(playerNumber, weather)
        else:
            DoHumanTurn(playerNumber, weather)

    ClearScreen()
    PrintYearSummary()
    input('<Enter>?')

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


