"""
Her lager jeg først en tom liste og setter svaret lik en tilfeldig verdi, annet enn 0. Så defineres en
while-løkke som kjører så lenge variabelen svar ikke er lik 0. Vi tar imot brukerinput i form av tall og løkken
kjører altså helt til brukeren skriver inn tallet 0. Alle verdiene bruker skriver inn legges til i lista.
"""
liste = []
svar = 1

while svar != 0:
    svar = int(input("Skriv inn et tall"))
    liste.append(svar)

""" Her bruker vi en for-løkke til å printe ut alle verdiene i lista """
for x in liste:
    print(x)

""" Her definerer jeg en variabel minSum som summerer sammen alle tallene i lista tidligere definert. Vi kjører
gjennom lista med en for-løkke som summerer tallene og printer ut summen av lista """
minSum = 0
for x in liste:
    minSum += x
print("Din sum:", minSum)

""" Her definerer vi en variabel max som skal fortelle oss hva det høyeste tallet i lista er. Vi kjører igjen
gjennom lista med en for-løkke som sjekker tallene og bytter ut variabelen max med den høyeste verdien i
lista og printer dette ut."""
max = 0
for x in liste:
    if x > max:
        max = x
print("Din høyeste sum er", max)

""" Her definerer vi en variabel min som skal fortelle oss hva det laveste tallet i lista er. Vi kjører igjen
gjennom lista med en for-løkke som sjekker tallene og bytter ut variabelen min med den laveste verdien i 
lista og printer dette ut."""
max = 0
min = max
for x in liste:
    if x < min:
        min = x
print("Din laveste sum er", min)
