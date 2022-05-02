class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def __str__(self):
        return f"Název: {self.nazev}, žánr: {self.zanr}."

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def __str__(self):
        return super().__str__() + f" Délka zvoleného filmu je {self.delka} minut."
    def get_celkova_delka(self):
        celkova_delka = self.delka
        return celkova_delka

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
    def __str__(self):
        return super().__str__() + f" Zvolený seriál má {self.pocet_epizod} epizod a jedna epizoda trvá přibližně {self.delka_epizody} minut."
    def get_celkova_delka(self):
        celkova_delka = self.pocet_epizod * self.delka_epizody
        return celkova_delka


class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
    def pripocti_zhlednuti(self, celkova_delka):
        self.delka_sledovani = self.delka_sledovani + celkova_delka
        return self.delka_sledovani
    def __str__(self):
        return f"Uživatel {self.uzivatelske_jmeno} má celkem zhlédnuto: {self.delka_sledovani} minut."

film1 = Film("Vrchní prchni", "komedie", 90)
serial1 = Serial("HIMYM", "komedie", 24, 20)
serial2 = Serial("Red Dwarf", "komedie", 8, 30)

uzivatel1 = Uzivatel("Karel")

uzivatel1.pripocti_zhlednuti(film1.get_celkova_delka())
uzivatel1.pripocti_zhlednuti(serial1.get_celkova_delka())
uzivatel1.pripocti_zhlednuti(serial2.get_celkova_delka())

print(uzivatel1)