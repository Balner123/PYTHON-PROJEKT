'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení (m/s)
MOON_GRAVITY =  1.7#? měsíční gravitace (m/s)
SPEED_OF_LIGHT = 300000 #? rychlost světla ve vakuu (km/s)
SPEED_OF_SOUND = 330 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu (m/s)

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
'''

def tiha_predmetu_na_mesici(hmotnost):
    print(f"{hmotnost*MOON_GRAVITY}\n")
    
def tiha_predmetu_na_zemi(hmotnost):
    print(f"{hmotnost*EARTH_GRAVITY}\n")    
    

def procent_rychlosti_svetla(rychlost):
    print(f"{rychlost/SPEED_OF_LIGHT*100}%")

def procent_rychlosti_svetla(rychlost):
    print(f"{rychlost/SPEED_OF_SOUND} Mach")


'''
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
