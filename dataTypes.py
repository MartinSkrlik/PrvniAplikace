from decimal import Decimal
from fractions import Fraction


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

print("Zadaj cislo")
a = int(input())
a = a * a
print(a)

print("Zadaj cislo")
a = float(input())
b = (2 * 3.14 * a)
c = (3.14 * (a * a))
print(f"obvod je {b}")
print(f"obsah je {c}")

s1 = "Python"
s2 = s1
print(s1)
print(s2)

print("Zadaj cislo")
a = float(input())
b = (2 * 3.14 * a)
c = (3.14 * (a * a))
print(f"obvod je {b}")
print(f"obsah je {c}")

s1 = "Tohle je původní text"
s2 = s1
s1 = "Tohle je nový text"
print(s1)
print(s2)

b = float('2.71e-5')
print(b)

a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(Decimal(c))

b = False
vyraz = 6 > 5
print(b)
print(vyraz)

cislo = 3 + 4j # complex data types
cislo2 = complex(3, 4)  # complex data types

zlomok = Fraction(3, 4) # data type fraction
zlomok2 = Fraction(6, 8)
vysledok = zlomok + zlomok2
print(vysledok)
print(float(vysledok)) # fraction converted to float

# retazce
retazec = 'retazec'
retazec2 = "retazec"
zprava = 'Můj kamarád řekl: "Kdo používá Python, nikdy se nenudí!" A měl\" pravdu.'
print(retazec)
print(retazec2)
print(zprava)

python = "pthon"
jeNajlepsi = ' je Najlepsi'
print(len(python))
print(python + jeNajlepsi)

bum = "bum "
sprava = bum * 7
print(sprava)

vstup = "Krokonosohroch"
print(vstup.startswith("krok"))
print(vstup.endswith("hroch"))
print("nos" in vstup)
print("roh" in vstup)

nastaveni = 'Fullscreen shaDows autosave'
nastaveni = nastaveni.lower()

print("ful" in nastaveni)
print("Ful" in nastaveni)
print("shadows" in nastaveni)

veta = "C# je najlepsi"
veta2 = veta.replace("C#", "Python")
print(veta2)
