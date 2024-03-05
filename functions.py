"""
def mocnina (cislo):
    cislo = cislo ** 7  # 3 * 3 * 3 * 3 * 3 * 3
    return cislo

print(mocnina(3))

def soucin(prvni_cislo, druhe_cislo, treti_cislo):
    cislo = prvni_cislo * druhe_cislo * treti_cislo
    return cislo

priklad = soucin(2, 3, 4)
print(priklad)

# types of arguments
def mocnina(cislo, exponent=2):    # Cislo je poziční argument, exponent je klíčový argument
    cislo = cislo ** exponent
    return cislo

print(mocnina(2))

def mocnina(cislo, exponent=2):
    cislo = cislo ** exponent
    return cislo

print(mocnina(3))

def nejaka_funkce(*pozicni_argumenty):
    pass

def moje_funkce(*, prvni_klicovy_arg, druhy_klicovy_arg=1):
    print(prvni_klicovy_arg, druhy_klicovy_arg)

# recursion

def faktorial(cislo):
    if cislo > 0:
        return (cislo - 1) * cislo
    else:
        return 1

print(faktorial(5))

# data type definition in function
def faktorial(martin: str) -> str:
    return "Ahoj " + martin + " !"
print(faktorial("Martin"))

print(1, 2, 3, "a", end=" ")
print("Žádná nová řádka", end=" ")
print("nebude.", end=" ")

# delenie, kalkulacka
while True:
    try:
        delenec = float(input("Vloz cislo ktore bude delene"))
        delitel = float(input("Vloz cislo ktore bude delit"))

        vysledok = delenec / delitel
    except  ZeroDivisionError:
        print("Delenie dulou")
    except ValueError:
        print("Zle datove typy")
    else:
        print(f"vysledok je {vysledok}")
    finally:
        opustit = input("Chces opustit kaluklacku [ano/nie]").lower()
        if  opustit == "ano":
            break

print("Vitajte v kalkulacke")
pokracovat = "ano"
while pokracovat == "ano":
    a = float(input("Vloz prve cislo"))
    b = float(input("Vloz druhe cislo"))
    print("Zvolte si operaci:")
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    volba = int(input())
    vysledok = 0.0
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
                print("Nulou nelze dělit!")
                vysledok = "N/A"

    if 0 < volba < 5:
        print(f"Výsledek: {vysledok}")
    else:
        print("Neplatná volba")
    nezadano = True
    while nezadano:
        odpoved = input("\nPřejete si zadat další příklad? ano / ne: ").lower()
        if odpoved == "ano":
            nezadano = False
        elif odpoved == "ne":
            nezadano = False
            pokracovat = False
        else:
            pass
print("Děkuji za použití kalkulačky, aplikaci ukončíte libovolnou klávesou.")

# 3 functions together

def nactiCislo(textZadani, textChyba):
    spatne = True
    while spatne:
        try:
            cislo = int(input(textZadani))
            spatne = False
        except ValueError:
            print(textChyba)
        else:
            return cislo

def dalsiPriklad():
    while True:
        odpoved = input("Chcete pokracovat [ano/ne] ").lower()
        if odpoved == "ano":
            return True
        elif odpoved == "ne":
            return False
        else:
            print("Zadaj iba ano alebo ne")

def provedOperaci(a, b):
    while True:
        print("Scitani: 1")
        print("Odcitani: 2")
        print("Nasobeni: 3")
        print("Deleni 4")

        try:
            vstup = int(input("Zadejte cislo pro danou operaci"))

            match vstup:
                case 1:
                    return a + b
                case 2:
                    return a - b
                case 3:
                    return a * b
                case 4:
                    if b != 0:
                        return a / b
                    else:
                        print("Nulou nelze delit")
                        continue
                case _:
                    print("Neplatna volba, zadejte ine cislo")
                    continue

        except ValueError:
            print("Neplatni vstup, zadejte prosim cislo")
            continue



print("KALKULACKA \n")
pokracovat = True

while pokracovat:
    prvni_cislo = nactiCislo("Nacti prve cislo", "Neplatne cislo")
    druhe_cislo = nactiCislo("Nacti druhe cislo", "Nespravne cislo")
    vysledek_vypoctu = provedOperaci(prvni_cislo, druhe_cislo)
    print(f"Vysledek vypoctu {vysledek_vypoctu}")
    pokracovat = dalsiPriklad()

print("Dakujem ze nefajcis, koniec")
print()

"""
































