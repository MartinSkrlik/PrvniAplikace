from decimal import Decimal
from fractions import Fraction
import math



"""
print("Pí:", math.pi)
print("e:", math.e)
print(math.sin(math.pi/2))  # Vrací sinus 90°
print(math.degrees(math.pi))   # Vrací 180.0
print(math.radians(180))  
print(math.degrees(math.pi))   # Vrací 180.0
print(math.radians(180)) 
print(math.ceil(656.787878)) # ceil fuunction, rounded towards up
print(math.floor(4545.898989))  # floor function, rounded towards down
print(round(3434.4545454))  
print(math.floor(3434.4545454)) # floor is build-in function
print(math.fabs(-3434.34343))  # fabs return absolute value (negative is transformed to positive number)
print(math.factorial(34)) # return factorial number
print(math.pow(4,4))  # return pow
print(math.sqrt(16))    # return root of number
print(math.log(16, 4))
print(math.log10(1000))
print(math.log2(32))

"""

def selection_sort(array):
    for i in range(len(array) - 1):  # 0 - 3
        index_minima = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_minima]:
                index_minima = j

        array[i], array[index_minima] = array[index_minima], array[i]
    return array





pole = [3,1,5,4]
print(pole)
print(len(pole))
print(selection_sort(pole))


pole = [1,2,3,4,5,6]
cisla = list(range(1,11))

for cislo in range(len(pole)):
    print(cislo, end=" ")

print()

for cislo in pole:
    print(cislo, end=" ")