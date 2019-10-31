def aantalbugs(aantaldagen):
    """
    input: Vraagt hoeveel bugs er zijn gezien

    output: het totale aantal bugs
"""
    totaalaantal = 0
    for i in range(aantaldagen):
        totaalaantal += int(input("Hoeveel bugs zijn er vandaag gezien? "))
    return totaalaantal

def main():
    aantaldagen = 5
    #print het aantal dagen en het aantal gevonden bugs
    print("Er zijn in deze 5 dagen", aantalbugs(aantaldagen), "bugs gevonden")

main()
