class Zdravic:
    text = "nezadanyStale"
    opis = "celkomVpoho"
    def pozdrav(self, jmeno):
        return f"Hello object world {jmeno} a {self.text} a {self.opis}"

zdravic = Zdravic()
zdravic.pozdrav("Igor")
zdravic = Zdravic()
zdravic.text = "Ahoj uživateli"
zdravic.pozdrav("Karel")
zdravic.pozdrav("Petr")
zdravic.text = "Vítám tě tu programátore"
zdravic.pozdrav("Richard")
zdravic.opis = "trochuMimo"
zdravic.pozdrav("Martin")

print(zdravic.pozdrav("Martin"))

