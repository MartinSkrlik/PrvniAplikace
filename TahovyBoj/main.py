from bojovnik import Bojovnik
from kostka import Kostka

kostka = Kostka()
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)

print(f"Bojovnik {bojovnik}")
print(f"Nazivu {bojovnik.jeNazivu()}")
print(f"Zivot {bojovnik.grafickyZivot()}")
