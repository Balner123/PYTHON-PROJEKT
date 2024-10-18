from physics import *

def main():
    while True:
        volba = input('''1 = Kolik kg vážíš na Měsíci
2 = Převod rychlosti na % rychlosti světla
3 = Převod rychlosti na Machy 

Co se chceš dozvědět?: 
''')
        
        if volba == '1':
            x = float(input("Zadej svou hmotnost (kg): "))
            print(f"Na měsíci bys vážil {tiha_predmetu_na_mesici(x)} kg (na Zemi {x} kg)\n")
        elif volba == '2':
            x = float(input("Zadej rychlost předmětu (km/h): "))
            print(f"Předmět svištící {x} km/h dosahuje rychlosti rovné {procent_rychlosti_svetla(x)} % C\n")
        elif volba == '3':
            x = float(input("Zadej rychlost předmětu (km/h): "))
            print(f"Předmět svištící {x} km/h dosahuje rychlosti rovné {prevod_na_machy(x)} Machů\n")
        else:
            print("Neplatná volba!\n")
        
        pokracovat = input("Chceš pokračovat? (ano/ne): ").lower()
        if pokracovat != 'ano':
            print("Program ukončen.")
            break

    main()
