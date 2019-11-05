def product(getal):
    """Vermenigvuldigd het getal met zichzelf en elk getal wat daarvoor komt.
    input: getal - int

    output: print totaalaantal - int
    """
    totaalaantal = 1
    for i in range(getal):
        totaalaantal*=i+1
    print(totaalaantal)

def main():
    product(int(input("Kies een getal")))
main()
