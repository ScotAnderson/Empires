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
    '{0} has been assassinated by an ambitious\nnoble',
    '{0} has been killed from a fall during\nthe annual fox-hunt.',
    '{0} died of acute food poisoning.\nThe royal cook was summarily executed.',
    '{0} passed away this winter from a weak heart.'
]

def safeRandInt(lower, upper):
    if lower >= upper:
        return upper
    return randint(lower, int(upper))

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

barbarianLands = 6000

def GetFullPlayerName(playerNumber):
    return "{0} of {1}".format(GetTitleName(playerNumber), players[playerNumber][1])

def GetTitleName(playerNumber):
    return '{0} {1}'.format(players[playerNumber][playerData[playerNumber][17]], players[playerNumber][0])


# Original code 395- - 409
def CheckForPlague(playerNumber):
    if random() <= 0.02:
        serfs = safeRandInt(1, int(playerData[playerNumber][3] / 2))
        playerData[playerNumber][3] -= serfs
        
        merchants = safeRandInt(1, int(playerData[playerNumber][7] / 3))
        playerData[playerNumber][7] -= merchants
        
        soldiers = safeRandInt(1, int(playerData[playerNumber][15] / 3))
        playerData[playerNumber][15] -= soldiers
                
        nobles = safeRandInt(1, int(playerData[playerNumber][18] / 3))
        playerData[playerNumber][18] -= nobles
        
        ClearScreen();
        PrintPlague(serfs, merchants, soldiers, nobles)
        sleep(8)


def DoAITurn(playerNumber, weather):
    # It is very unclear what this line is doing
    # 413 FOR Q = 1 TO NP : If A(Q, 0) <> 0 Next Q : PRINT : End

    if playerData[playerNumber][0] != 0:
        return

    ClearScreen()
    print("One moment -- {0}'s turn . . .".format(GetTitleName(playerNumber)))
    sleep(.25)

    CheckForRandomDeath(playerNumber)

    if playerData[playerNumber][0] != 0:
        return

    serfs        = 0
    grainMarket  = 0
    priceMarket  = 0
    money        = 0
    merchants    = 0
    marketplaces = 0
    mills        = 0
    foundries    = 0
    shipyards    = 0
    palace       = 0
    nobles       = 0
    armyEffectiveness = 0
    howManyHumanPlayersAreAlive = 0

    for q in range(0, numberOfHumanPlayers):
        if playerData[q][0] == 0:
            howManyHumanPlayersAreAlive = howManyHumanPlayersAreAlive + 1
            serfs        = playerData[q][3] + serfs
            grainMarket  = playerData[q][5] + grainMarket
            priceMarket  = playerData[q][6] + priceMarket
            money        = playerData[q][4] + money
            merchants    = playerData[q][7] + merchants
            marketplaces = playerData[q][11] + marketplaces
            mills        = playerData[q][12] + mills
            foundries    = playerData[q][13] + foundries
            shipyards    = playerData[q][14] + shipyards
            palace       = playerData[q][16] + palace
            nobles       = playerData[q][18] + nobles
            armyEffectiveness = playerData[q][19] + armyEffectiveness

    serfs        = serfs / howManyHumanPlayersAreAlive
    grainMarket  = grainMarket / howManyHumanPlayersAreAlive
    priceMarket  = priceMarket / howManyHumanPlayersAreAlive
    money        = money / howManyHumanPlayersAreAlive
    merchants    = merchants / howManyHumanPlayersAreAlive
    marketplaces = marketplaces / howManyHumanPlayersAreAlive
    mills        = mills / howManyHumanPlayersAreAlive
    foundries    = foundries / howManyHumanPlayersAreAlive
    shipyards    = shipyards / howManyHumanPlayersAreAlive
    palace       = palace / howManyHumanPlayersAreAlive
    nobles       = nobles / howManyHumanPlayersAreAlive
    armyEffectiveness = armyEffectiveness / howManyHumanPlayersAreAlive

    while True:
        serfs = int(serfs + safeRandInt(1, 200) - safeRandInt(1, 200))
        grainMarket = int(grainMarket + safeRandInt(1, 1000) - safeRandInt(1, 1000))
        priceMarket = priceMarket + random() - random()
        money = int(money + safeRandInt(1, 1500) - safeRandInt(1, 1500))
        merchants = int(merchants + safeRandInt(1, 25) - safeRandInt(1, 25))
        if priceMarket < 0:
            priceMarket = 0
        else:
            break

    marketplaces = int(marketplaces + safeRandInt(1, 4) - safeRandInt(1, 4))
    mills = int(mills + safeRandInt(1, 2) - safeRandInt(1, 2))
    if random() <= 0.3:
        foundries = int(foundries + safeRandInt(1, 2) - safeRandInt(1, 2))
        shipyards = int(shipyards + safeRandInt(1, 2) - safeRandInt(1, 2))
        if random() <= 0.5:
            palace = int(palace + safeRandInt(1, 2) - safeRandInt(1, 2))
            nobles = int(nobles + safeRandInt(1, 2) - safeRandInt(1, 2))

    playerData[playerNumber][3] = serfs
    if grainMarket > playerData[playerNumber][5] and safeRandInt(1, 9) > 6:
        playerData[playerNumber][5] = grainMarket
        playerData[playerNumber][6] = priceMarket
        if weather < 3:
            playerData[playerNumber][6] = playerData[playerNumber][6] + random() / 1.5


    playerData[playerNumber][4] = money
    if merchants > playerData[playerNumber][7]:
        playerData[playerNumber][7] = merchants

    if marketplaces > playerData[playerNumber][11]:
        playerData[playerNumber][11] = marketplaces

    if mills > playerData[playerNumber][12]:
        playerData[playerNumber][12] = mills

    if foundries > playerData[playerNumber][13]:
        playerData[playerNumber][13] = foundries

    if shipyards > playerData[playerNumber][14]:
        playerData[playerNumber][14] = shipyards

    if palace > playerData[playerNumber][16]:
        playerData[playerNumber][16] = palace

    if nobles > playerData[playerNumber][18]:
        playerData[playerNumber][18] = nobles

    playerData[playerNumber][15] = 10 * playerData[playerNumber][18] + safeRandInt(1, 10 * playerData[playerNumber][18])

    while (playerData[playerNumber][15] / serfs > playerData[playerNumber][13] * .01 + .05):
        playerData[playerNumber][15] = playerData[playerNumber][15] / 2

    playerData[playerNumber][19] = armyEffectiveness
    CheckForTitles(playerNumber)

    marketHumanPlayer = safeRandInt(1, numberOfHumanPlayers) - 1
    while playerData[marketHumanPlayer][0] != 0:
        marketHumanPlayer = safeRandInt(1, numberOfHumanPlayers)

    if playerData[marketHumanPlayer][5] > 0:
        while True:
            amountOfGrainToBuy = int(random() * playerData[marketHumanPlayer][5])
            if amountOfGrainToBuy * playerData[marketHumanPlayer][6] < playerData[playerNumber][4]:
                playerData[marketHumanPlayer][4] = playerData[marketHumanPlayer][4] + int(amountOfGrainToBuy * playerData[marketHumanPlayer][6] * 90) / 100
                playerData[marketHumanPlayer][5] = playerData[marketHumanPlayer][5] - amountOfGrainToBuy
                break

            if safeRandInt(1, 9) <= 3:
                break

    attacksSoFar = 0
    defender = -1

    while True:
        if safeRandInt(1, 9) < 2:
            return

        if currentYear < 3:
            if barbarianLands <= 0:
                return
            defender = -1            
        else:
            defender = playerNumber
            while defender == playerNumber or playerData[defender][0] != 0:
                defender = safeRandInt(0, 5)


        Attack(playerNumber, defender, safeRandInt(1, playerData[playerNumber][15]), True)
        attacksSoFar = attacksSoFar + 1
        
        if playerData[playerNumber][15] <= 30 or attacksSoFar >= playerData[playerNumber][18] / 4:
            return


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


def DoHumanTurn(playerNumber, weather):
    CheckForPlague(playerNumber)
    starvationDeaths = 0

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

    if playerData[playerNumber][0] != 0:
        return

    DoTaxesAndInvestments(playerNumber, grainHarvest, immigrations, weather)
    DoAttacks(playerNumber)



def PrintAttacks():
    print('Land holdings:\n')
    print('1)  Barbarians\t{0}'.format(barbarianLands))

    for i in range(0, 6):
        if playerData[i][0] == 0:
            print('{0})  {1}\t{2}'.format(i + 2, players[i][1], playerData[i][1]))

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
            

def PrintAttackInternal(aggressor, defender, aggressorSoldiers, defenderSoldiers, serfsDefending):
    print('\n\n                                        Soldiers remaining:')
    print('\n  {0:>36}:           {1:3}'.format(GetFullPlayerName(aggressor), aggressorSoldiers))

    if defender < 0:
        print('                        Pagan barbarians:           {0:3}'.format(defenderSoldiers))
    else:
        print('  {0:>36}:           {1:3}'.format(GetFullPlayerName(defender), int(defenderSoldiers)))
        if serfsDefending == True:
            print('\n{0}\'s serfs are forced to defend their country!'.format(players[defender][1]))


def Attack(attacker, defender, attackingSoldiers, aiTurn):
    attackingSoldierStrength = playerData[attacker][19]
    playerData[attacker][15] = playerData[attacker][15] - attackingSoldiers
    defendingSoldiers = 0
    defendingSoldierStrength = 0
    defenderLands = 0
    serfsDefending = False
    landsSeized = 0

    if defender < 0:
        defendingSoldiers = safeRandInt(1, safeRandInt(1, attackingSoldiers * 3)) + safeRandInt(1, safeRandInt(1, attackingSoldiers * 1.5))
        defendingSoldierStrength = 9
        defenderLands = barbarianLands
    else:
        defendingSoldiers = playerData[defender][15]
        defendingSoldierStrength = playerData[defender][19]
        defenderLands = playerData[defender][1]

        if playerData[defender][15] < 1:
            defendingSoldiers = playerData[defender][3]
            defendingSoldierStrength = 5
            serfsDefending = True

    while True:
        ClearScreen()
        PrintAttackInternal(attacker, defender, attackingSoldiers, defendingSoldiers, serfsDefending)
        sleep(.15)

        troopUnit = int(attackingSoldiers / 15) + 1
        if safeRandInt(1, attackingSoldierStrength) < safeRandInt(1, defendingSoldierStrength):
            attackingSoldiers -= troopUnit
        else:
            landsSeized = landsSeized + safeRandInt(1, troopUnit * 26) - safeRandInt(1, troopUnit + 5)
            defendingSoldiers -= troopUnit
            if landsSeized < 0:
                landsSeized = 0

        if defenderLands - landsSeized < 0:
            CountryOverrun(attacker, defender, landsSeized, attackingSoldiers, defendingSoldiers, serfsDefending, aiTurn)
            return    

        if attackingSoldiers > 0 and defendingSoldiers > 0:
            continue

        if attackingSoldiers < 0:
            attackingSoldiers = 0

        if defendingSoldiers < 0:
            defendingSoldiers = 0

        if serfsDefending == True and attackingSoldiers > 0:
            CountryOverrun(attacker, defender, landsSeized, attackingSoldiers, defendingSoldiers, serfsDefending, aiTurn)
            return

        BattleOver1(attacker, defender, landsSeized, attackingSoldiers, defendingSoldiers, serfsDefending, aiTurn)
        return



def PauseOrWait(aiTurn):
    if aiTurn == True:
        sleep(4)
    else:
        input('<Enter>?')


def BattleOver1(playerNumber, defender, landsSeized, remainingSoldiers, remainingDefenders, serfsDefending, aiTurn):
    global barbarianLands

    ClearScreen()
    print('\n                       Battle over\n')

    if remainingSoldiers > 0:
        print('The forces of {0} were victorious.'.format(GetTitleName(playerNumber)))
        print('{0} acres were seized'.format(landsSeized))
    else:
        print('{0} was defeated.'.format(GetTitleName(playerNumber)))
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
    else:
        playerData[playerNumber][15] = playerData[playerNumber][15] + remainingSoldiers
        playerData[playerNumber][1] = playerData[playerNumber][1] + landsSeized
        playerData[defender][1] = playerData[defender][1] - landsSeized
        
        if serfsDefending == True:
            playerData[defender][15] = 0
            playerData[defender][3] = remainingDefenders
        else:
            playerData[defender][15] = remainingDefenders

        if landsSeized > playerData[defender][1] / 3:
            if playerData[defender][3] > 0:
                serfs = safeRandInt(1, playerData[defender][3])
                print('{0} enemy serfs were beaten and murdered by your troops!'.format(serfs))
                playerData[defender][3] = playerData[defender][3] - serfs

            if playerData[defender][11] > 0:
                markets = safeRandInt(1, playerData[defender][11])
                print('{0} enemy marketplaces were destroyed'.format(markets))
                playerData[defender][11] = playerData[defender][11] - markets

            if playerData[defender][2] > 0:
                grain = safeRandInt(1, playerData[defender][2])
                print('{0} bushels of enemy grain were burned'.format(grain))
                playerData[defender][2] = playerData[defender][2] - grain

            if playerData[defender][12] > 0:
                mills = safeRandInt(1, playerData[defender][12])
                print('{0} enemy grain mills were sabotaged'.format(mills))
                playerData[defender][12] = playerData[defender][12] - mills
            
            if playerData[defender][13] > 0:
                foundries = safeRandInt(1, playerData[defender][13])
                print('{0} enemy foundries were leveled'.format(foundries))
                playerData[defender][13] = playerData[defender][13] - foundries

            if playerData[defender][14] > 0:
                shipyards = safeRandInt(1, playerData[defender][14])
                print('{0} enemy shipyards were over-run'.format(shipyards))
                playerData[defender][14] = playerData[defender][14] - shipyards

            if playerData[defender][18] > 2:
                nobles = safeRandInt(1, playerData[defender][18] / 2)
                print('{0} enemy nobles were summarily executed'.format(nobles))
                playerData[defender][18] = playerData[defender][18] - nobles
    
    PauseOrWait(aiTurn)


def CountryOverrun(attacker, defender, landsSeized, remainingAttackers, remainingDefenders, serfsDefending, aiTurn):
    global barbarianLands

    ClearScreen()
    print('\n                       Battle over')
    if defender < 0:
        print('All barbarian lands have been seized\nThe remaining barbarians fled')
        playerData[attacker][1] = playerData[attacker][1] + landsSeized
        playerData[attacker][15] = playerData[attacker][15] + remainingAttackers
        barbarianLands = 0

    else:
        print('The country of {0} was overrun!'.format(players[defender][1]))
        print('All enemy nobles were summarily executed!\n\n')
        print('The remaining enemy soldiers were imprisoned. All enemy serfs')
        print('have pledged oaths of fealty to you, And should now be consid-')
        print('ered to be your people too. All enemy merchants fled the coun-')
        print('try. Unfortunately, all enemy assets were sacked and destroyed')
        print('by your revengeful army in a drunken riot following the victory')
        print('celebration.')

        playerData[attacker][15] = playerData[attacker][15] + remainingAttackers
        playerData[attacker][1] = playerData[attacker][1] + playerData[defender][1]

        if serfsDefending == True:
            playerData[defender][3] = remainingDefenders

        playerData[defender][1] = 0
        playerData[defender][0] = 1
        playerData[attacker][3] = playerData[attacker][3] + playerData[defender][3]

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
    neededMerchants = 0
    neededNobles = 0    

    cost = investmentType[taxIndex - 1][0]
    if taxIndex == 1:
        neededMerchants = safeRandInt(1, 7)
    if taxIndex == 6:
        neededNobles = safeRandInt(1, 4)

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

            if amount + (amount - 1) * (neededMerchants + neededNobles) > playerData[playerNumber][3]:
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
                playerData[playerNumber][7] = playerData[playerNumber][7] + neededMerchants * amount
                playerData[playerNumber][18] = playerData[playerNumber][18] + neededNobles * amount
                playerData[playerNumber][3] = playerData[playerNumber][3] - (neededMerchants + neededNobles) * amount

            playerData[playerNumber][4] = playerData[playerNumber][4] - amount * cost
            playerData[playerNumber][10 + taxIndex] = playerData[playerNumber][10 + taxIndex] + amount
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
    print('State revenues:    Treasury={0:10,.2f} {1}'.format(int(playerData[playerNumber][4]), players[playerNumber][6]))
    print('Customs duty    Sales tax       Income tax')
    print(' {0} %            {1} %              {2} %'.format(int(playerData[playerNumber][8]), int(playerData[playerNumber][9]), int(playerData[playerNumber][10])))
    print(' {0}             {1}             {2}'.format(int(customsCollected + .5), int(salesCollected + .5), int(incomeCollected + .5)))
    print('')
    print('Investments     Number          Profits           Cost')
    print('1) Marketplaces  {0:<5d}           {1:<5d}            1000'.format(playerData[playerNumber][11], int(marketProfit)))
    print('2) Grain mills   {0:<5d}           {1:<5d}            2000'.format(playerData[playerNumber][12], int(millProfit)))
    print('3) Foundries     {0:<5d}           {1:<5d}            7000'.format(playerData[playerNumber][13], int(foundryProfit)))
    print('4) Shipyards     {0:<5d}           {1:<5d}            8000'.format(playerData[playerNumber][14], int(shipyardProfit)))
    print('5) Soldiers      {0:<5d}          {1:< 6d}            8'.format(playerData[playerNumber][15], soldierCost))
    print('6) Palace        {0:<16}                 5000\n\n'.format('{0}% Completed'.format(playerData[playerNumber][16] * 10)))


def BuyGrain(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    while True:
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        try:
            country = int(input('From which country  (give #)? '))
            if country == 0:
                return

            if country < 1 or country > 6:
                continue

            country = country - 1

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
                try:
                    price = float(input('What will be the price per bushel? '))
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
        try:
            acres = int(input('How many acres will you sell them? '))
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
    print("                Country         Bushels         Price")

    grainForSale = False

    for i in range(0, 6):
        if (playerData[i][0] == 0 and playerData[i][5] > 0):
            grainForSale = True
            print("{0}\t\t{1:9}\t {2}\t\t{3:5.2f}".format(i + 1, players[i][1], int(playerData[i][5]), playerData[i][6]))

    if grainForSale == False:
        print("\n\n\nNo grain for sale . . .\n")

    print('\n\n')


def MarketInternal(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    exitMarket = False
    menuItemSelected = 0
    while (menuItemSelected < 1 or menuItemSelected > 4) and exitMarket == False:
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        try:
            menuItemSelected = int(input('1) Buy Grain 2) Sell Grain 3) Sell Land? '))
        except ValueError:
            exitMarket = True

    return exitMarket, menuItemSelected



def DoArmyGrainShare(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands):
    armyShare = -1
    while (armyShare < 0 or armyShare > playerData[playerNumber][2]):
        ClearScreen()
        PrintMarket(playerNumber, grainHarvest, ratsAte, peopleGrainDemands, armyGrainDemands)
        try:
            armyShare = int(input('How many bushels will you give to your army of {0} men? '.format(playerData[playerNumber][15])))
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
        try:
            peopleShare = int(input('How many bushels will you give to your {0} people? '.format(people)))
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
        immigrantBase = (sqrt(peopleShare - peopleGrainDemands) - safeRandInt(1, int(playerData[playerNumber][8] * 1.5)))
        if immigrantBase >= 0:
            immigrations = safeRandInt(1, int(2 * immigrantBase + 1))

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
    armyStarvation2 = 0
    if armyShare * 2 < armyDemands:
        armyStarvation2 = safeRandInt(1, int(playerData[playerNumber][15] / 5))
        playerData[playerNumber][15] = playerData[playerNumber][15] - armyStarvation2

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
        playerData[playerNumber][0] = 1
        print('\n\nThe other nation-states have sent representatives to the\nfuneral')
        sleep(8)

def PrintVerySadNews():
    ClearScreen()
    print("Very sad news ...\n")

def PrintYearSummary():
    print("Summary")
    print("Nobles   Soldiers   Merchants   Serfs   Land    Palace\n")
    for i in range(0, 6):
        if playerData[i][0] == 0:
            print(GetFullPlayerName(i))
            print(" {0:3d}      {1:6,d}      {2:6,d}   {3:7,d}  {4:6,d}  {5:3d}%".format(int(playerData[i][18]), int(playerData[i][15]), int(playerData[i][7]), int(playerData[i][3]), playerData[i][1], int(playerData[i][16] * 10)))




def MainLoop():
    global currentYear
    currentYear += 1
    ClearScreen()
    weather = safeRandInt(0, 5)
    PrintYear(currentYear, weather)
    sleep(4)

    # Do player turns (Human and AI)
    for playerNumber in range(0, 6):
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
        try:
            numberOfHumanPlayers = int(input('How many people are playing? '))
        except ValueError:
            print('Answer must be an integer 1-6')

    for i in range(0, numberOfHumanPlayers):
        players[i][0] = input('Who is the ruler of {}? '.format(players[i][1]));

PrintTitle()
InitQuestions()

while True:
    MainLoop()


