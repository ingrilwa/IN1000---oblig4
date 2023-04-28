""" Oppgavetekst:
Lag et program som lar deg fylle inn hva du har i kjøleskapet og hva du skal ha i middagen din. Varene du ikke har i kjøleskapet skal legges til i en annen liste, kalt handleliste. Til slutt skal du skrive ut en setning til bruker som forteller de hva handellisten tilslutt består av utenom det de hadde av matvarer fra før. Programmet skal bestå av lister og løkker """

"""Først definerer jeg en tom liste kjøleskap. Deretter spør jeg bruker om hvor mange varer de har i kjøleskapet fra før av. Jeg lager en while-løkke som kjører så lenge lengden på lista kjøleskap ikke er lengre enn antall matvarer bruker skrev inn de hadde i kjøleskapet. Inni while-løkka skriver bruker inn alle varene de har i kjøleskapet og dette legges til i lista kjøleskap med append. """
kjoleskap = []
varer = int(input("Hvor mange varer har du i kjøleskapet?"))
while varer > len(kjoleskap):
    kjoleskap.append(input("Skriv inn hva du har i kjøleskapet."))

""" Her definerer jeg to tomme lister til. Her bruker jeg en for-løkke for å legge til matvarene man trenger til middagen  """
matvarer = []
handleliste = []
for x in range(7):
    matvarer.append(input("Skriv matvarene du trenger til middag"))

""" Her bruker jeg en til for-løkke som sjekker om matvarene skrevet inn allerede finnes i kjøleskapet. Hvis de ikke gjør dette, skal varene legges til i en handleliste. """
for x in matvarer:
    if x in kjoleskap:
         0
    else:
        handleliste.append(x)

print("Matvarene du trenger til middag er", matvarer, " og du må handle det du ikke har i kjøleskapet, altså:", handleliste)

""" På slutten her skriver jeg ut alle varene som brukes og hva som må handles inn. """
