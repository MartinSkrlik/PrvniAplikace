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

class Trida:
    pass

Trida.novy_tridni_atribut = "toto je novy atribut"

class Clovek:
    vek = 30

print(f"Puvodni vek {Clovek.vek} (typ {type(Clovek.vek).__name__})" )

Clovek.vek = "Tricet let"

print(f"Po pretypovani: {Clovek.vek} (typ {type(Clovek.vek).__name__})")