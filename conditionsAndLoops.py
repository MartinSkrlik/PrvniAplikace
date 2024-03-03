"""
a = int(input("Zadaj nejake cislo"))
if (a > 10):
    print("Vacsie ako 10")
print("Mensie ako 10")

a = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (a > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit!")
    odmocnina = a ** (1 / 2)
    print(f"Odmocnina z čísla {a} je {odmocnina}")
print("Děkuji za zadání")

cislo = 1 # deklarace proměnné s hodnotou 0

if (cislo == 0): # pokud je hodnota proměnné 0, změníme hodnotu na 1
    cislo = 1
else: # pokud je hodnota proměnné 1, změníme hodnotu na 0
    cislo = 0

print(cislo)

a = int(input("uloz daco\n"))
if ( a > 10 and a > 20):
    print("Nieco je proste vacsie ako nieco ine")
else:
    print("Zadal si blbo")

a = int(input("Zadejte číslo v rozmezí 10-20 nebo 30-40: "))
if (a >= 10 and a <= 20) or (a >= 30 and a <= 40):
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně")

print("vitajte v kalkulacke")
a = float(input("zadaj cislo"))
b = float(input("zadaj druhe cislo"))
print("zavolaj si operacio")
print("1 - scitanie")
print("2 - odcitanie")
print("3 - nasobenie")
print("4 - delenie")
volba = int(input())
vysledok = 0.0
match volba:
    case 1:
        vysledok = a * b
    case 2:
        vysledok = a - b
    case 3:
        vysledok = a * b
    case 4:
        vysledok = a / b
        if b != 0:
            vysledok = a / b
        else:
            print("Nulou nelze delit")
            vysledok = "N/A"

if volba > 0 and volba < 5:
    print(f"Vysledok  {vysledok}")
else:
    print("Neplatna volba")
print("Uz daj pokoj")

x = int(input())

match x:
    case 1:
        print("sdfafd")
        print("sdfsfsdffd")
        print("sfsfdssfs")
    case 2:
        print("ssssssssssss")
        print("aaaaaaaaaaaa")
        print("dddddddd")
    case _:
        print("sdsffsdfsddddddddddddddddd")

#cycles

for i in range(3):
    print("Knock")
print("Penny!")

for i in range(1, 11, 2):
    print(i , end=" ")

slovo = "Znak"  # string in for interation
for znak in slovo:
    print(znak)

for i in range(1,10):
    print(i, end=" ")
print()
for i in range(1,10):
    print(i * 2, end=" ")
print()
for i in range(1,10):
    print(i * 3, end=" ")
print()
for i in range(1,10):
    print(i * 4, end=" ")
print()
for i in range(1,10):
    print(i * 5, end=" ")
print()
for i in range(1,10):
    print(i * 6, end=" ")
print()
for i in range(1,10):
    print(i * 7, end=" ")
print()
for i in range(1,10):
    print(i * 8, end=" ")
print()
for i in range(1,10):
    print(i * 9, end=" ")
print()
for i in range(1,10):
    print(i * 10, end=" ")
print()

for i in range(1,11):
    for j in range(1,11):
        print(i * j, end=" ")
    print()

print("Mocninátor")
print("==========")
a = int(input("Zadejte základ mocniny: "))
n = int(input("Zadejte exponent: "))
result = a
for i in range(n - 1):
    result = result * a

print(f"Výsledek: {result}")
print("Děkuji za použití mocninátoru")

for i in range(1, 10, 3):
    print("vypis pocet opakovani ")
    print(i)

# while loop

i = 1
while i <= 10:
    print(i, end=" " "\n")
    i += 1

print("Vítejte v kalkulačce")
a = float(input("Zadejte první číslo:"))
b = float(input("Zadejte druhé číslo:"))
print("Zvolte si operaci:")
print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")
volba = int(input())
vysledek = 0.0
match volba:
    case 1:
        vysledek = a + b
    case 2:
        vysledek = a - b
    case 3:
        vysledek = a * b
    case 4:
        if b != 0:
            vysledek = a / b
        else:
            print("Nulou nelze dělit!")
            vysledek = "N/A"

if volba > 0 and volba < 5:
    print(f"Výsledek: {vysledek}")
else:
    print("Neplatná volba")
print("Děkuji za použití kalkulačky, aplikaci ukončíte libovolnou klávesou.")

print("No pod")
pokracovat = "ano"
while (pokracovat == "ano"):
    a = float(input("zadaj prve cislo"))
    b = float(input("zadaj druhe cislo"))
    print("Zvolte si operaci:")
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    vysledok = 0.0
    volba = int(input())
    match volba:
        case 1:
            vysledok = a + b
        case 2:
            vysledok = a - b
        case 3:
            vysledok = a * b
        case 4:
            if b != 0:
                vysledok = a / b
            else:
                print("Nemozes delit 0")
                vysledok = "N/A"

    if volba > 0 and volba < 5:
        print(f"vysledok {vysledok}")
    else:
        print("Zadal si cislo out of enumeration")
    pokracovat = input("Chces pokracovat [ano/nie]")
print("Děkuji za použití kalkulačky, aplikaci ukončíte libovolnou klávesou.")


# Lists

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # manually created list
print(cisla[3])
cisla[5] = 60
print(cisla[5])

cisla= list(range(1, 11))
for cislo in cisla:
    cislo += 1
print(cisla)

for i in range(len(cisla)):
    cisla[i] /= 0.5
    print(cisla[i])
print()
print(f"cisla {cisla}, \n")

# enumerate




for index, value in enumerate(simpsons):
    print(f"index and list of values {index} and {value}")
print("gadzo")

zoznam = ["martin", "ivan", "alojz", "simon"]
cisla= [1,3,6,9,]

for i in range(len(cisla)):
    i = i+4
    print(i)
    print(cisla)

simpsons = ["mam", "dad", "son", "daugther"]

cisla = range(5)

print(list(cisla))
print(list(cisla[0:5]))
print(list(cisla[2:8]))
print(list(cisla[1:7:2]))
print(list(cisla[::2]))
print(list(cisla[6:]))

for i in cisla:
    print(cisla[i])

# string methods

cisla = range(10)
cisla2 = [1, 2, 3, 4]
cisla2.append(14)   # append method
print(cisla2)
print(cisla2[1])
print(cisla2[4])

cisla2.insert(-2, 34)   # insert method
print(cisla2)

cisla2.extend(cisla)    # extend method
print(cisla2)

cisla2.clear()  # clear method
print(cisla2)

del cisla2[:]   # clear command
print(cisla2)

cisla2 = [1, 2, 3, 4]
cisla2.remove(2)    # remove method
print(cisla2)

cisla2 = [23, 4545, 46675, 0.8778787, 23]
cisla2.reverse()    # reverse method
print(cisla2)

pocet = cisla2.count(23)    # count method
print(pocet)

simpsons = ["mam", "dad", "son", "daugther"]

for i in simpsons:
    simpsons.sort()     # sort method
print(simpsons)

simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
simpson = input("Ahoj, zadej svého oblíbeného Simpsona (z rodiny Simpsonů): ")
if simpson in simpsons:
    pozice = simpsons.index(simpson)    # index method
    print(f"Muj nejoblibenejsi simpson {pozice+1}")
else:
    print("Pozice nenalezena")

"""

smes = [1, "Ahoj", 3.14, [1, 2, 3]] # different data types
print(smes)


