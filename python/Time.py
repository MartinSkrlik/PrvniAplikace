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



