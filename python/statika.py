# class Uzivatel:
#
#     minimalniDelkaHesla = 6
#     dalsi_id = 1
#
#     def __init__(self, jmeno, heslo):
#         self._jmeno = jmeno
#         self._heslo = heslo
#         self._prihlaseny = False
#         self._id = Uzivatel.dalsi_id
#         Uzivatel.dalsi_id += 1
#
#     def prihlasSa(self, zadane_heslo, zadane_jmeno):
#         if self._jmeno == zadane_jmeno and self._heslo == zadane_heslo:
#             self.prihlaseny = True
#             return True
#         else:
#             self._prihlaseny = False
#             return False
#
#     def __str__(self):
#         return str(f"{self._jmeno} a {self._heslo}")
#
# uzivatel_admin = Uzivatel("Tomáš Správce", "adminheslo")
# uzivatel_obycejny = Uzivatel("Tomáš Uživatel", "heslouzivatele")
#
# print(f"ID uživatele {uzivatel_admin._jmeno} je {uzivatel_admin._id}")
# print(f"ID uživatele {uzivatel_obycejny._jmeno} je {uzivatel_obycejny._id}")
#
# print(Uzivatel.dalsi_id)
#
#
# class Trida:
#     tridni_atrigut = "ako"
#
# instance = Trida()
#
# print(instance.tridni_atrigut)
#
# instance.tridni_atrigut = "nato"
# #
# print(instance.tridni_atrigut)
# print(Trida.tridni_atrigut)

# class Trida:
#     pass
#
# Trida.novy_tridni_atribut = "toto je novy atribut"
#
# class Clovek:
#     vek = 30
#
# print(f"Puvodni vek {Clovek.vek} (typ {type(Clovek.vek).__name__})" )
#
# Clovek.vek = "Tricet let"
#
# print(f"Po pretypovani: {Clovek.vek} (typ {type(Clovek.vek).__name__})")

# class Uzivatel:
#
#     minimalniDelkaHesla = 6
#     dalsi_id = 1
#
#     def __init__(self, jmeno, heslo):
#         self._jmeno = jmeno
#         self._heslo = heslo
#         self._prihlaseny = False
#         self.fddddf = False
#
#     @staticmethod
#     def zvalidujHeslo(heslo):
#         if len(heslo) >= Uzivatel.minimalniDelkaHesla:
#             return True
#         else:
#             return False
#
# instance = Uzivatel("sdfsd", "sdfsdf")
# print(Uzivatel.zvalidujHeslo("sdfsfdsfsdfs"))

import math

# class Geometrie:
#
#     @staticmethod
#     def obvodKruhu(polomer):
#         return round((2 * math.pi * polomer),2)
#
#     @staticmethod
#     def obvodObdelniku(delka, sirka):
#         return 2 * (delka, sirka)
#
#     @staticmethod
#     def je_Ctverec(delka, sirka):
#         return delka == sirka

# print(Geometrie.obvodKruhu(23))
# print(Geometrie.obvodObdelniku(12,15))
# print(Geometrie.je_Ctverec(12,12))
#
# g = Geometrie()
#
# print(g.obvodKruhu(23))

# print(Geometrie.obvodKruhu(5)) # Funguje správně - i když metoda nemá dekorátor, volání přímo na třídě je možné
# g = Geometrie()
# print(g.obvodKruhu(5))

# class Geometrie:
#
#     @staticmethod
#     def obvod_kruhu(polomer):  # metoda BEZ dekorátoru
#         return 2 * math.pi * polomer
#
# print(Geometrie.obvod_kruhu(5)) # Funguje správně - i když metoda nemá dekorátor, volání přímo na třídě je možné
# g = Geometrie()
# print(g.obvod_kruhu(5))

# class GeometrieUtilities:
#
#     def obvod_kruhu(polomer):
#         return round((2 * math.pi * polomer), 2)
#
#     def obvod_delka(delka, sirka):
#         return 2 * (delka + sirka)
#
#     def je_ctverec(delka, sirka):
#         return delka == sirka
#
# print(GeometrieUtilities.obvod_kruhu(5))

# class Ridic:
#     hodnota = "rodic"
#
#     @classmethod
#     def vrat_hodnotu(cls):
#         return cls.hodnota
#
#     def statickametoda(self):
#         return self.hodnota
#
# class Potomek(Ridic):
#     hodnota = "Jsem potomek, ne rodič."
#
#
# print(Potomek.vrat_hodnotu())
# print(Potomek.statickametoda)


# class Uzivatel:
#     minimalni_delka = 6
#
#     def __init__(self, jmeno, heslo):
#         self._jmeno = jmeno
#         self._heslo = heslo
#
#     @staticmethod
#     def zvaliduj_heslo(heslo):
#         return len(heslo) >= Uzivatel.minimalni_delka
#
#     @classmethod
#     def nastav_minimalni_delka_hesla(cls, nova_delka):
#         cls.minimalni_delka = nova_delka
#
#     def je_heslo_validni(self):
#         return self.zvaliduj_heslo(self._heslo)
#
# class VIPuzivatel(Uzivatel):
#     minimalni_delka = 10
#
#     @staticmethod
#     def zvaliduj_heslo(heslo):
#         return len(heslo) >= VIPuzivatel.minimalni_delka
#     @classmethod
#     def informace_o_hesle(cls):
#         return f"Minimální délka hesla pro {cls.__name__} je {cls.minimalni_delka} znaků."
#
# tomas = Uzivatel('Tomas', 'motyka')
# petr = VIPuzivatel('Peter', 'veslo12')
#
# print(tomas.zvaliduj_heslo('test'))
# print(petr.informace_o_hesle())
#
# print(tomas.je_heslo_validni())
# print(petr.je_heslo_validni())