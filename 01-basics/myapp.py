"""
Cvičení 3:

Vytvořte originální aplikaci v Pythonu, v níž požádáte uživatele o různé vstupní údaje a
využijete na maximum možností výstupů do konzole. Může to být vtipný dotazník, jednoduchý znalostní test (např.
z matematiky...), průvodce fiktivní instalací atd. Fantazii se meze nekladou a vtipnější vyhrává :-)
Aplikaci uložte do samostatného souboru myapp.py.
"""
import re
import camelcase
c = camelcase.CamelCase() 

print("___Dotaznik___")

jmeno = c.hump(input("Zadejte své jméno: "))
prijmeni = c.hump(input("Zadejte své příjmení: "))

while True:
    datum_narozeni = input("Zadejte své datum narození (DD.MM.RRRR): ")
    if re.match(r"^\d{2}\.\d{2}\.\d{4}$", datum_narozeni):
        break
    else:
        print("!!! Datum ve formátu DD.MM.RRRR.")

print(f"-----------------------------------\n"
      f" |         INFORMACE         \n"
      f" ----------------------------------\n"
      f" | Jméno: {jmeno}                   \n"
      f" | Příjmení: {prijmeni}             \n"
      f" | Datum narození: {datum_narozeni} ")

print(f"\nA víte, že vaše celé jméno má {len(jmeno) + len(prijmeni)} znaků?")
