import random

class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycistiObrazovku()
        print("-------------- Aréna -------------- \n")
        print("Zdraví bojovníků: \n")
        print(f"{self._bojovnik_1} {self._bojovnik_1.graficky_zivot()}")
        print(f"{self._bojovnik_2} {self._bojovnik_2.graficky_zivot()}")

    def _vycistiObrazovku(self):
        import os as _os
        _os.system('cls' if _os.name == 'nt' else 'clear')

    def _vypis_zpravu(self, zprava):
        import time as _time
        print(zprava)
        _time.sleep(0.75)

    def zapas(self):
        print("Vitejte v arene")
        print(f"Dnes se utkaji {self._bojovnik_1} a {self._bojovnik_2}")
        print("Zapas muze zacit", end=" ")
        input()
        # cyklus s bojem
        # prohození bojovníků
        if random.randint(0,1):
            (self._bojovnik_1, self._bojovnik_2) = (self._bojovnik_2, self._bojovnik_1)

        while self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu():
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
            self._bojovnik_2.utoc(self._bojovnik_1)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
            self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())


