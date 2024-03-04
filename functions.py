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


"""











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











