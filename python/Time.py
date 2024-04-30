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

# for i in range(1, 8, 2):
#     print(i)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:   # nested loop
#   for y in fruits:
#     print(x, y)

# meno = ["martin", "Ivan", "Peter", "Simon"]
# priezviesko = ["Petrovicky", "Novak", "Bajza", "Skrlik"]
# status = ["slobodny", "zenaty", "mastny", "nechcecny"]
#
# for x in meno:
#     for y in priezviesko:
#         for z in status:
#             print(x,y,z)

# def funkcia(parameter1, parameter2):    # two arguments
#     print(parameter1 + " sfsdf" + parameter2)
#
# funkcia("peto", "mato")

# def function2(*param):  # non defined count of parameters
#     print(param[2])
#
# function2("ako", "mako", "pako", "tak")


# def my_function(child3, child2, child1):    # kwargs arguments using as "key = value" duo
#     print("The youngest child is " + child3)
#
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(**kid): # kwargs** using as key=value duo with not knowing how meny arguments has function
#   print("His last name is " + kid["lname"])
#
# my_function(fname = "Tobias", lname = "Refsnes", mname = "Jebo")

# def my_function(country = "Norway"):    # default value in function, it is printed if function has no argument
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):  #  list as argument in python fuction can be used
#   for x in food:
#     print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# def function4(food):
#     for x in food:
#         print(x)
# food = ["jabko", "pomaranc", "citron"]
# function4(food)

# def my_function(x): # function can return value, not argument
#   return 5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def function6():    # empty function with no return value or parameter
#     pass

# def my_function(x): # '/' is using to reject using keyword argument
#   print(x)
#
# my_function(x = 3)
#
# def my_function(x, /): # '/' is using to reject using keyword argument
#   print(x)
#
# my_function(x = 3)


# def my_function(a, b, /, *, c, d):  #  you can add together '/' or '*' to set which parameters shoud be positioned or keywords
#   print(a + b + c + d)
#
# my_function(5, 6, c = 7, d = 8)

# def tri_recursion(k):   # recursion (function calling itself)
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
#
# tri_recursion(2)

# d = lambda x : x + 10   # lambda is small anonymous function with any numbers of parameters but inly one expression
# print(d(5))
# x = lambda a, b : a * b
# print(x(5, 6))
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))
# print(myfunc(5))

# def myfunc(n):    # anonymous function is called also lambda function ()
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(11))
# print(mytripler(11))

import array

# importing "array" for array creations
# import array as arr
#
# # creating an array with integer type
# a = arr.array('i', [1, 2, 3])   # array in python
# print(type(a))
# for i in a:
#     print(i, end=" ")


# class MyClass:      # create class
#     x = 5
# p1 = MyClass    # create object
# print(p1.x)

# class Person:   # class/object/example/init function
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         ako = 7
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)
#
# class Person:   #  class/method/init function
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name}({self.age})"
# p1 = Person("John", 36)
# print(p1)
# p1.name = "Mathiew"     # change object properties
# print(p1)
# del p1.name     # delete object properties
# print(p1)
# del p1  # delete object itself

class Person:   #  parent class to be inherit from
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def printName(self):
    print(self.firstname, self.lastname)

ako = Person("martin", "skrlik")
ako.printName()

class Student(Person):  #  child class, inherited from parent (Person) class
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)   #  add 'super().' causing inheritence from parent (Person) class
    self.graduationyear = year    #   adding property graduationyear and set to 34

  def welcome(self):
    print("Welcome"+ self.firstname, self.lastname + "to the class of" + self.graduationyear)

object = Student("mike", "bowel", "1970")
print(object.graduationyear)
object.printName()
object.welcome()
