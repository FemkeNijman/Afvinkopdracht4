def product(getal):
    """
input: een gekozen getal

output:het getal vermenigvuldigd met hetzelfde getal en elk getal daar onder
"""
    totaalaantal = 1
    for i in range(getal):
        totaalaantal*=i+1
    print(totaalaantal)

def main():
    product(int(input("Kies een getal")))
main()
