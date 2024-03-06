class Kavovar:
    umisteni = "nezname misto"
    mnozstvy_vody = 0

    def dopln_vodu(self, mnozstvi):
        self.mnozstvy_vody += mnozstvi
        print(f"Do kavovaru {self.umisteni} bylo doplneno {mnozstvi} ml vody "
              f"Celkem je v nem {self.mnozstvy_vody} ml vody ")

    def uver_kavu(self):
        if self.mnozstvy_vody > 100:
            self.mnozstvy_vody -= 100
            print(f"Kavovar {self.umisteni} uvaril kavu, Zvyva {self.mnozstvy_vody}")
        else:
            print(f"V kavovaru {self.umisteni} neni dostatek vody")

# Vytvoříme dvě instance kávovaru
kavovar_doma = Kavovar()
kavovar_v_kancli = Kavovar()

# Umistneni pro kavovary
kavovar_doma.umisteni = "doma"
kavovar_v_kancli.umisteni = "v kancli"

# Uvar kavu v kancli
kavovar_v_kancli.dopln_vodu(150)

# Uvar kavu doma
kavovar_v_kancli.uver_kavu()
