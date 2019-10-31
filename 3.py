def tijden(aantallaps):
    """
input: Vraagt hoe snel er is gerend

output: print het gemiddelde, de snelste tijd, de langzaamste tijd en de tijd zelf
"""
    #als de tijd minder is dan snelste wordt snelste erin verandert.
    #hetzelfde gebeurt bij langzamer, maar dan met hoger dan.
    #zo word gekeken welke tijden het snelst en het langzaamst zijn
    snelste = 1000000
    langzaamste = 0
    gemiddelde = 0
    for i in range(aantallaps):
        tijd = (int(input("Hoe snel heb je gerend?")))
        if tijd < snelste:
            snelste = tijd
        if tijd > langzaamste:
            langzaamste = tijd
        gemiddelde += tijd
    gemiddelde = gemiddelde/aantallaps
    print("Het gemiddelde is",gemiddelde)
    print("De snelste tijd is", snelste)
    print("De langzaamste tijd is", langzaamste)
        

def main():
    aantallaps = (int(input("Hoeveel laps heb je gerend?")))
    tijden(aantallaps)
    
main()
