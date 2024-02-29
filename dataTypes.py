from decimal import Decimal

"""
print("Please input your name")
print("Your name")

vstup = input()
vystup = vstup + ", " + vstup
print(vystup)
"""

"""
print("Zadajte cislo")
a = input()
a = a * 2
print(a)

print("Zadejte číslo k zdvojnásobení:")
s = input()  # Držme se našeho čísla 12
a = int(s)
a = a * 2
print(a)
"""

print("Welcome to calculator")
print("Please input your numbers and behold the magic")
a = Decimal(input())
print("Input your second number")
b = Decimal(input())
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
print(f"scitanie {addition}")
print(f"odcitanie {subtraction}")
print(f"nasobenie {multiplication}")
print(f"division {division}")   # first way to print string+float
print("text" + str(division))   # second way to print string+float

zaokruhlit = round(a - b, 3)    # round to desired decimal number
print(zaokruhlit)
