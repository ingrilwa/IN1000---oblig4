""" Her definerer vi en tom liste kalt steder. Vi lager en for-løkke som legger til reisemål som brukerne
skriver inn i lista. Vi gjør akkurat det samme med to lister til, klesplagg og avreisedatoer."""
steder = []
for x in range(5):
    steder.append(input("Skriv inn et reisemål"))
klesplagg = []
for x in range(5):
    klesplagg.append(input("Skriv inn et klesplagg"))
avreisedatoer = []
for x in range(5):
    avreisedatoer.append(input("Skriv inn en avreisedato"))

""" Her lager jeg en ny liste, reiseplan og legger listene fra istad inn i denne. Vi kjører gjennom lista
med en for-løkke og skriver ut alle elementene i listene. """
reiseplan = [steder,klesplagg,avreisedatoer]
for x in reiseplan:
    print(x)

""" Her definerer vi to nye variabler og spør om brukerinput til disse. Vi sikrer oss at det blir en tallverdi
med int foran input. Etter vi har fått brukerinput kjører jeg en if-test som sjekker om vi har fått gyldige
verdier, altså det vi spurte om. Hvis vi har fått dette, finner vi frem og printer ut verdien som står på
nettopp denne plassen i lista. Hvis vi har fått ugyldig brukerinput, går det til else, og vi printer ut at det
er ugyldig input."""
liste_indeks1 = int(input("Oppgi første indeks(0-2)"))
liste_indeks2 = int(input("Oppgi andre indeks(0-4)"))
if (liste_indeks1 >= 0 and liste_indeks1 <= 2) and (liste_indeks2 >= 0 and liste_indeks2 <= 4):
    print(reiseplan[liste_indeks1][liste_indeks2])
else:
    print("Ugyldig input!")
