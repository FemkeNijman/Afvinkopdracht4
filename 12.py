def product(getal):
    """vermenigvuldigd het getal met zichzelf en elk getal wat daarvoor komt.
    
    input: 
    getal - int
    output: 
    """
    totaalaantal = 1
    for i in range(getal):
        totaalaantal*=i+1
    print(totaalaantal)

def main():
    product(int(input("Kies een getal")))
main()
