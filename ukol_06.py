#půjčovna aut
zdroj = input("Zadejte název vstupního souboru:")

with open(zdroj, encoding='utf-8') as vstup:
    vykaz = vstup.readlines()

zaznamy = [item.split() for item in vykaz]

zaznamyDot = [[item[0], item[1].replace(",", ".")] for item in zaznamy]

zaznamyFloat = [[item[0], float(item[1])] for item in zaznamyDot]

zaznamyKm = [item[1] for item in zaznamyFloat]
sumKm = sum(zaznamyKm)

print(sumKm)
