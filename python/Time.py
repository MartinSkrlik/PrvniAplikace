import time

# start_time = time.time()
# je_tik = True
# print(je_tik)
#
# while (time.time() - start_time) <= 1:
#     if je_tik:
#         print("tik", end=" ")
#     else:
#         print("tak", end=" ")
#     je_tik = not je_tik
#
# print(time.localtime())
# local = time.localtime()
# print(f"Dnes je {local[2]}.{local[1]}.{local[0]}") # localtime
#
# print(f"Datum a cas {time.asctime(local)}")  # asctime

# print("start")
# time.sleep(3)
# print("end")

# local = time.localtime()
# formatovany_cas = time.strftime("%d.%m.%S",local) # self formated datetime (z datoveho fromatu prevedie na string)
# print(formatovany_cas)

# cas_text = "20.10.2023 15:30:00"
# cas_objekt = time.strptime(cas_text, "%d.%m.%Y %H:%M:%S") # string to time object
# print(f"Převedeno na struct_time: {cas_objekt}")

# uct_cas = time.gmtime()
# print(uct_cas)
# formatovany_cas = time.strftime("%d.%m.%Y %H:%M:%S" ,uct_cas) # aktualiny cas UTC coordinated universl time without any time movement
# print(formatovany_cas)

from fractions import Fraction

# print(Fraction(11, 35))
# # returns Fraction(11, 35)
#
# print(Fraction(10, 18))
# # returns Fraction(5, 9)
#
# print(Fraction())
# # returns Fraction(0, 1)

import calendar

# mnesic = calendar.month(2024, 6, 6)
# print(mnesic)

# hlavicka = calendar.weekheader(6)
# print(hlavicka)
# mnesic = calendar.month(2024, 6, 6)
# print(mnesic)

# rok = 2023
# mesic = 11
# month_range = calendar.monthrange(rok, mesic)
# seznam_month_range = list(month_range)       # nám zatím neznámý typ tuple převedeme na seznam
# print(seznam_month_range)
#
# dny = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
# #  Funkce monthrange() indexuje dny od 0 a měsíce od 1. Proto je níže v seznamu jako první prázdný řetězec
# mesice = ["", "leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]
#
# den = dny[seznam_month_range[0]]
# mesic_slovem = mesice[mesic]
# pocet_dni = seznam_month_range[1]
#
# print(f"Prvním dnem v měsíci {mesic_slovem} je v roce 2023 {den} a {mesic_slovem} má {pocet_dni} dní.")

# dny = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
# den = calendar.weekday(2024,4,15)
# print(f"5. října 2023 byl {dny[den]}.")

# je_prestupny = calendar.isleap(2025) # zisti ci je prestunpy
# print(je_prestupny)

# je_prestupny = calendar.leapdays(2000,2025) # zisti kolko prestypnych rokov bolo medzi dvoma rokmi
# print(je_prestupny)

from datetime import datetime

# datum = datetime(2023, 12, 12) # funkce datetime
# print(datum) # 2023-12-12 00:00:00
#
# cas = datetime.now() # funkce now
# print(cas)
# print(f"{cas.hour}")
# print(f"{cas.minute}")
# print(f"{cas.day}")

# dnes = datetime.now()
# dny_v_tydnu = ["pondelok", "utorok", "streda", "strvrtok", "piatok", "sobota", "nedela"]
# den = dny_v_tydnu[dnes.weekday()] # funkcia weekday
# print(den)
# print(dnes.weekday()) # vrati den v tyzdni ako cislo

# dnes = datetime.now()
# vtedy = datetime(2023, 12, 12) # zistit cas medzi obdobim
# cas = dnes - vtedy
# print(cas)

# dnes = datetime.now()
#
# zmena_roku = dnes.replace(year = dnes.year + 1)
# zmena_dne = dnes.replace(day =  dnes.day + 1)
#
# print(f"Přidáme rok navíc a budeme mít rok {zmena_roku.year}.")
# print(f"Přidáme den navíc a budeme mí {zmena_dne.day}.{dnes.month}.")

# def pridat_casove_razitko(func):
#     # Dekorátor, který přidává časové razítko k výstupu funkce
#     def zaznamenat_zpravu(zprava):
#         cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         return func(f"[{cas}] {zprava}")
#     return zaznamenat_zpravu
#
# @pridat_casove_razitko
# def zapsat_do_deniku(zprava):
#     # Zapisuje zprávu do deníku s časovým razítkem
#     print(zprava)
#
# # Použití dekorované funkce
# zapsat_do_deniku("Přihlásit se na školení ITnetwork")

# def zapis_data():
#     return "Zapisuji data do databáze."
#
# def povol_zapis():
#     return zapis_data      # vrací funkci zapis_data, ne její výsledek
#
# vysledek = povol_zapis()    # do proměnné výsledek vkládáme obsah funkce povol_zapis(), což je reference na funkci zapis_data()
# print(vysledek)         # dostaneme pouze referenci na funkci zapis_data
# print(vysledek())

# import time
#
# def vypocet_objemu_krychle(func):
#     def vypocet_objemu_a_obsahu(*args, **kwargs):
#         obsah = func(*args, **kwargs)
#         objem = obsah * args[0]
#         print(f"Obsah čtverce se stranou {args[0]} je: {obsah}")
#         print(f"Objem krychle se stranou {args[0]} je: {objem}")
#         return obsah
#     return vypocet_objemu_a_obsahu
#
# def validuj_vstup(func):
#     def over_data(*args, **kwargs):
#         if any(arg <= 0 for arg in args):
#             print("Varování: Všechny argumenty musí být kladné a nenulové.")
#         return func(*args, **kwargs)
#     return over_data
#
# def zmer_cas(func):
#     def zmer_a_vypis_cas(*args, **kwargs):
#         zacatek = time.time()
#         vysledek = func(*args, **kwargs)
#         konec = time.time()
#         print(f"Čas běhu funkce obsah_ctverce(): {konec - zacatek:.5f} sekund.")
#         return vysledek
#     return zmer_a_vypis_cas
#
# @validuj_vstup
# @zmer_cas
# @vypocet_objemu_krychle
# def obsah_ctverce(a):
#     time.sleep(1)  # na sekundu zdržíme běh programu, jinak je tak rychlý, že bychom dostali čas běhu nulový.
#     return a**2
#
# obsah_ctverce(3)

# built-in data types for collection data

# list = ["a","a", 2, 2, 5] # list
# for i in list:
#     print(i)
#     print(list[0])
#
# thistuple = ("apple", "banana", "cherry", "apple", "cherry") # tuple, the same like list but can have duplicates and itmes cannot be added or deleted.
# for i in thistuple:
#     print(i)
#
# thisset = {"apple", "banana", "cherry", "cherry","cherry"} # set is urordered, ignore duplicates,
# print(thisset)
# for i in thisset:
#     print(i)
#
# thisdict = {    # dictionaries using key value pairs
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])
# print(len(thisdict))

# i = 1 # loop with while
# while i < 6:
#   print(i)
#   i += 1

# i = 1 # loop with while and break
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
#
#
# ako = 1 # loop with while and break
# while ako < 6:
#     print(ako)
#     if ako == 3:
#         break
#     ako += 1

# i = 1 # loop with while and break
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# fruits = ["banana", "grape" , "apple" , "orange"]   # for loop with continue
# for i in fruits:
#   print(i)
#   if i == "banana":
#     continue

# fruits = ["banana", "grape" , "apple" , "orange"]   # for loop with break
# for i in fruits:
#   print(i)
#   if i == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]  # for with break, before print
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# for x in range(6): # range using in loop
#   print(x)

for i in range(1, 8, 2):
    print(i)