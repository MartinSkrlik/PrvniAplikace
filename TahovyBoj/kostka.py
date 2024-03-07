class Kostka:
    """
    Třída reprezentuje hrací kostku.
    """

    def __init__(self, pocetSten=6):
        self.__pocet_sten = pocetSten     # jedno podtržítko dává najevo, že nechceme, aby se k atributu přistupovalo přímo

    def vrat_pocet_sten(self):
        """
        Vrátí počet stěn kostky.
        """
        return self.__pocet_sten

    def hod(self):
        """
        Vykoná hod kostkou a vrátí číslo od 1 do
        počtu stěn.
        """
        import random as _random
        return _random.randint(1, self.__pocet_sten)

    def __str__(self):
        """
        Vrací textovou reprezentaci kostky.
        """
        return str(f"Kostka s {self.__pocet_sten} stenami.")


sestStranovaKostka = Kostka()
desatStranovaKostka = Kostka(10)


desatStranovaKostka.__pocet_sten = 3434 # private attribute set with "__"

print(sestStranovaKostka.vrat_pocet_sten())
print(desatStranovaKostka.vrat_pocet_sten())

# hod sesti stranovou kostkou
print(sestStranovaKostka)
for i in range(6):
    print(sestStranovaKostka.hod(), end=" ")

print()
print(desatStranovaKostka, sep=" ")
# hod deset stranovou kostkou
for i in range(10):
    print(desatStranovaKostka.hod(), end=" ")








