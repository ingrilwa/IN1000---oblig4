""" Her lager jeg funskjoner med en parameter. Den første retunerer lengden på ordet, antall bokstaver.
Den andre funksjonen legger antall ord i setningen inn i en ordbok. Vi bruker split() for å splitte setningen
ved mellomrom slik at hvert ord kommer for seg. Vi bruker en for-løkke til å øke antallord for hvert ord.
Dette returneres også."""
def antallBokstaver(ord):
    return len(ord)
def antallOrd(setning):
    ord = setning.split()
    antallOrd = {}
    for x in ord:
        if x in antallOrd:
            antallOrd[x] += 1
        else:
            antallOrd[x] = 1
    return antallOrd
""" Her tar jeg in brukerinput, en setning, og dette legges inn i variabelen setning. Variabelen totalAntallOrd
blir lik lengden av setningen, antall ord. Dette printes ut.  """
setning = input("Skriv en setning")
totalAntallOrd = len(setning.split())
print("Setningen din bestod av", totalAntallOrd, "ord")
antallOrd = antallOrd(setning)
""" Til slutt kjøres en for-løkke som kjører gjennom setningen og ordene og printer ut hvor mange ganger de
forskjellige ordene forekom i setningen og hvor mange bokstaver de forskjellige ordene består av. Her kaller
vi samtidig på funksjonene fra starten, antallOrd og antallBokstaver. """
for x in antallOrd:
    print("Ordet", x, "forekom", antallOrd[x], "ganger, og består av", antallBokstaver(x), "bokstaver")
