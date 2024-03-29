from mag import Mag


class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti_obrazovku()
        print("  __    ____  ____  _  _    __   ")
        print("  /__\\  (  _ \\( ___)( \\( )  /__\\  ")
        print(" /(__)\\  )   / )__)  )  (  /(__)\\ ")
        print("(__)(__)(_)\\_)(____)(_)\\_)(__)(__)\n")

        print("Bojovníci: \n")
        self._vypis_bojovnika(self._bojovnik_1)
        self._vypis_bojovnika(self._bojovnik_2)

    def _vycisti_obrazovku(self):
        import os as _os
        _os.system('cls' if _os.name == 'nt' else 'clear')

    def _vypis_zpravu(self, zprava):
        import time as _time
        print(zprava)
        _time.sleep(.75)

    def zapas(self):
        import random as _random
        print("Vítejte v aréně!")
        print(f"Dnes se utkají {self._bojovnik_1} a {self._bojovnik_2}!")
        print("Zápas může začít...", end=" ")
        input()
        # prohození bojovníků
        if _random.randint(0, 1):
            (self._bojovnik_1, self._bojovnik_2) = (self._bojovnik_2,
                                                    self._bojovnik_1)
        # cyklus s bojem
        while self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu():
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
            if self._bojovnik_2.je_nazivu():
                self._bojovnik_2.utoc(self._bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
                self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())

    def _vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f"Život: {bojovnik.graficky_zivot()}")
        if isinstance(bojovnik, Mag):
            print(f"Mana: {bojovnik.graficka_mana()}")