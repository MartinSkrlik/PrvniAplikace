class Uzivatel:

    def __init__(self, jmeno, heslo, vek, pohlavie):
        self._jmeno = jmeno
        self._heslo = heslo
        self._vek = vek
        self._pohlavie = pohlavie

    def prihlasit(self, heslo):
        ...

    def odhlasit(self):
        ...

    def nastav_vahu(self, zvire):
        ...

        ...


class Administrator:

    def __init__(self, jmeno, heslo, vek, telefonni_cislo):
        self.__jmeno = jmeno
        self.__heslo = heslo
        self.__vek = vek
        self.__telefonni_cislo = telefonni_cislo

    def prihlasit(self, heslo):
        ...

    def odhlasit(self):
        ...

    def nastav_vahu(self, zvire):
        ...

    def pridej_zvire(self, zvire):
        ...

    def vymaz_zvire(self, zvire):
        ...


class Administrator(Uzivatel):

    def __init__(self, jmeno, heslo, vek, telefonni_cislo):
        super().__init__(jmeno, heslo, vek)
        self.__telefonni_cislo = telefonni_cislo

    def pridej_zvire(self, zvire):
        ...

    def vymaz_zvire(self, zvire):
        ...


x = [5, 6]

if type(x) == list:
    print("x je seznam")

y = "sdfsdf"

if type(y) == str:
    print("y je řetězec")   # funkcia type na zistovanie typu objektu

class Rodic:
    pass

class Potomek(Rodic):
    pass

karel = Potomek()

print(type(karel) == Potomek) # Type zistuje akeho objektu je instancia karel
print(isinstance(karel, Rodic)) # Isinstance zistuje ci je instancia dedena z inej triedy, alebo ci je instanciou specifickej triedy

