
class Uzivatel:

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return str(self.jmeno)

# založení proměnných
u = Uzivatel("Jan Novák", 28)
v = Uzivatel("Josef Nový", 32)
print(f"u: {u}\nv: {v}")
print(f"u: {id(u)}\nv: {id(v)}\n")

# přiřazování
u = v
print(f"u: {u}\nv: {v}")
print(f"u: {id(u)}\nv: {id(v)}\n")

# změna jména
v.jmeno = "John Doe"
print(f"u: {u}\nv: {v}")
print(f"u: {id(u)}\nv: {id(v)}\n")


# druhá změna
v.jmeno = "John Doe"
v = None # zrusi odkaz na referenciu
print(f"u: {u}\nv: {v}")
print(f"u: {id(u)}\nv: {id(v)}\n")