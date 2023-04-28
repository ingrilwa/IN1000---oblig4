"""
I denne oppgaven lager jeg funksjon med parametere. Under her returnerer jeg summen av tallene og printer
dette ut gjennom funksjonen.
"""
def adder(tall1,tall2):
    return tall1 + tall2

print("Summen av 5 og 8 er" , adder(5,8))
print("Summen av 4 og 3 er" , adder(4,3))

"""
Under her lager jeg en til funksjon tellForekomst, med to paramtere minTekst og minBokstav. Funksjonen skal
telle antall forekomster av en viss bokstav i en tekststreng som kommer via brukerinput. Dette returneres og
printes ut på slutten. Vi må gjøre teksten om til en liste for å sjekke antall forekomster av en bokstav.
"""
def tellForekomst(minTekst, minBokstav):
    forekomst = 0
    for e in list(minTekst):
        if e == minBokstav:
            forekomst += 1
    return forekomst

tekststreng = input("Skriv inn en tekststreng: ")
bokstav = input("skriv inn en bokstav: ")
liste = list(tekststreng)
forekomst = tellForekomst(tekststreng,bokstav)
print("Bokstaven forekommer ", forekomst, "ganger i tekststrengen")
