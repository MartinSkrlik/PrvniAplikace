import copy as cp

# class Kostka:
#     """
#     Třída reprezentuje hrací kostku.
#     """
#
#     def __init__(self, pocetSten=6):
#         self.__pocet_sten = pocetSten     # jedno podtržítko dává najevo, že nechceme, aby se k atributu přistupovalo přímo
#
#     def vrat_pocet_sten(self):
#         """
#         Vrátí počet stěn kostky.
#         """
#         return self.__pocet_sten
#
#     def hod(self):
#         """
#         Vykoná hod kostkou a vrátí číslo od 1 do
#         počtu stěn.
#         """
#         import random as _random
#         return _random.randint(1, self.__pocet_sten)
#
#     def __str__(self):
#         """
#         Vrací textovou reprezentaci kostky.
#         """
#         return str(f"Kostka s {self.__pocet_sten} stenami.")
#
# sestStranovaKostka = Kostka()
# desatStranovaKostka = Kostka(10)
#
#
# desatStranovaKostka.__pocet_sten = 34 # you cannot chagge private attribute set with "__"
# desatStranovaKostka._Kostka__pocet_sten = 34 # you can change private attribute with "__" using the whole name of variable with Kostka
#
# print(sestStranovaKostka.vrat_pocet_sten())
# print(desatStranovaKostka.vrat_pocet_sten())
#
# # hod sesti stranovou kostkou
# print(sestStranovaKostka)
# for i in range(6):
#     print(sestStranovaKostka.hod(), end=" ")
#
# print()
# print(desatStranovaKostka, sep=" ")
# # hod deset stranovou kostkou
# for i in range(10):
#     print(desatStranovaKostka.hod(), end=" ")
#
# print()
#
# class Auto:
#     __slots__ = ['znacka', 'model']     # __slots__ deklaruje nemoznost puzitia inych atrubutov ako zvolenych
#
#     def __init__(self, znacka="Superb", model="Skoda"):
#         self.model = model
#         self.znacka = znacka
#
#     def vypisUdaje(self):
#         return str(f"{self.znacka} and {self.model}")
#
# auto = Auto()
# print(auto.vypisUdaje())
#
# # Vytvori instanciu kostky kopirovanim z inej instancie
# moje_kostka = Kostka()
# print(moje_kostka)
#
# print()
#
# # Vytvoříme kopii instance moje_kostka pomocí konstruktoru
# kopie_kostky = Kostka(moje_kostka.vrat_pocet_sten())
# print(kopie_kostky)
#

#
# # Vytvorime instanciu kostky s 6 stenami
# puvodni_kostka = Kostka(6)
# print(puvodni_kostka)
#
# # vytvorime melkou kopii pomocou "copy"
# melka_kopie_kostky = cp.copy(puvodni_kostka)
# print(melka_kopie_kostky)

# class Kostka:
#
#     def __init__(self, pocetSten=6):
#         self.pocetSten = pocetSten
#
#     def __str__(self):
#         return str(f"Pocet sten je {self.pocetSten}")
#
# class Hrac:
#
#     def __init__(self, jemno, kostka):
#         self.jmeno = jemno
#         self.kostka = kostka
#
#     def __str__(self):
#         return f"{self.jmeno} : {self.kostka}"
#
# kostka = Kostka()
# hrac = Hrac("Martin", kostka)
#
# print(hrac)
#
# kopie_hrace = cp.copy(hrac)
#
# kostka.pocetSten = 8
#
# print(kopie_hrace)
# print(hrac)

# class Kostka:
#
#     def __init__(self, pocet_sten=6):
#         self.pocet_sten = pocet_sten
#
#     def __str__(self):
#         return str(f"Nasa kocka ma {self.pocet_sten}")
#
#     def vrat_pocet_sten(self):
#         return self.pocet_sten
#
#     def hod(self):
#         import random
#         return random.randint(1, self.pocet_sten)

# kostka = Kostka(8)
#
# kopiruj_kostku = Kostka(kostka.vrat_pocet_sten())
#
# print(kostka)
# print(kopiruj_kostku)

# kopirovanie pomocou "copy"

# kostka = Kostka()
# print(kostka)
#
# kopiruj_kostku = cp.copy(kostka)
# print(kopiruj_kostku)

# kopiruj kostku s vnorenymi objektami

# class Hrac:
#     def __init__(self, jmeno, kostka):
#         self.jmeno = jmeno
#         self.kostka = kostka
#
#     def __str__(self):
#         return f"{self.jmeno} and {self.kostka}"

# kostka = Kostka(6)
# hrac = Hrac("Martin", kostka)
# # print(hrac)
#
# kopie_hrace = cp.copy(hrac)
#
# kostka.pocet_sten = 8
#
# print(hrac)
# print(kopie_hrace)

# kopie s "deepcopy"

# kostka = Kostka(6)
# hrac = Hrac("Martin", kostka)
# # print(hrac)
#
# kopie_hrace = cp.deepcopy(hrac)
#
# kostka.pocet_sten = 8
#
# print(hrac)
# print(kopie_hrace)

# kopie s __repr__ and __eval__

# class Kostka:
#     def __init__(self, pocet_sten=6):
#         self._pocet_sten = pocet_sten
#
#     def __str__(self):
#         return f"Kostka s {self._pocet_sten} stěnami."
#
#     def __repr__(self):
#         return f"Kostka({self._pocet_sten})"
#
#
#
#
# puvodni_kostka = Kostka(8)  # 8-stěnná kostka
# kopie_kostky = eval(repr(puvodni_kostka))
#
# print(puvodni_kostka)
# print(kopie_kostky)

# class Kostka:
#     def __init__(self, pocet_sten=6):
#         self._pocet_sten = pocet_sten
#
#     def __str__(self):
#         return f"Kostka s {self._pocet_sten} stěnami."
#
#     def __repr__(self):
#         return f"Kostka({self._pocet_sten})"
#
#
# puvodni_kostka = Kostka(8)  # 8-stěnná kostka
# kopie_kostky = eval(repr(puvodni_kostka))
#
# print(puvodni_kostka)
# print(kopie_kostky)


