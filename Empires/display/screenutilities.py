from os import system, name
from time import sleep

def ClearScreen():
    system('cls' if name == 'nt' else 'clear')
    #TODO: The above needs to be tested on linux. Works great on Windows

def PrintTitle():
    ClearScreen()   
    print('                   E M P I R E')
    print('\n\n\n\n\n\n\n\n(Always hit <enter> to continue)')
    sleep(4)

_weatherSwitcher = {
    0: "Poor weather. No rain. Locusts migrate.",
    1: "Early frosts. Arid conditions.",
    2: "Flash floods. Too much rain.",
    3: "Average weather. Good year.",
    4: "Fine weather. Long summer.",
    5: "Fantastic weather! Great year!"
}

def PrintYear(year, weather):
    print("Year {}\n".format(year))
    print(_weatherSwitcher.get(weather, "nothing"))

def PrintPlague(serfs, merchants, soldiers, nobles):
    print("                      P L A G U E  ! ! !");
    print("Black death has struck your nation.");
    print("{0} serfs died.".format(serfs));
    print("{0} merchants died.".format(merchants));
    print("{0} soldiers died.".format(soldiers));
    print("{0} nobles died.".format(soldiers));
