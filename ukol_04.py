# EVIDENCE AUT
# Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily (vlastnosti registrační značka, značka a typ vozidla, počet najetých km).
# Vytvoř třídu Auto s atributy viz výše plus info o tom, zda je vozidlo aktuálně volné (bool).
# Vytvoř metodu init, parametry do této fce jsou atributy třídy viz výše.
# Vytvoř objekty pro dvě auta.
# Třídě Auto přidej metodu pujc_auto(), která zkontroluje, zda je auto volné. True > změnit na False a return textu "Potvrzuji zapůjčení vozidla", False > return textu "Vozidlo není k dispozici".
# Třídě přidej funkci get_info() s return info o vozidle (reg_znacka a znacka_typ) jako řetězec.
# Mimo třídu napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Lze zadat Peugeot nebo Škoda. Jakmile vybere značku, vypíše se info o vozidle pomocí fce get_info() a následně se použije fce pujc_auto().
# Otestuj, že program nedovolí půjčit stejné auto dvakrát.

class Auto:
    def __init__(self, reg_znacka, znacka_typ, ujete_km):
        self.reg_znacka = reg_znacka
        self.znacka_typ = znacka_typ
        self.ujete_km = ujete_km
        self.volne = True
    def pujc_auto(self):
        if self.volne:
            self.volne = False
            return f"Potvrzuji zapůjčení vozidla."
        else:
            return f"Vozidlo není k dispozici."
    def get_info(self):
        return f"Registrační značka: {self.reg_znacka}, značka a typ vozidla: {self.znacka_typ}."

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

chce_znacku = input("Jakou značku auta chcete zapůjčit? Zadejte Peugeot nebo Škoda:")

def lze_pujcit_auto():
    if chce_znacku == "Peugeot" or chce_znacku == "Škoda":
        if chce_znacku in auto1.znacka_typ:
            print(auto1.get_info())
            print(auto1.pujc_auto())
        else:
            print(auto2.get_info())
            print(auto2.pujc_auto())
    else:
        print("Nezadal jste správně značku auta, která lze zapůjčit - Peugeot nebo Škoda.")

lze_pujcit_auto()

chce_znacku = input("Jakou značku auta chcete zapůjčit? Zadejte Peugeot nebo Škoda:")
lze_pujcit_auto()

chce_znacku = input("Jakou značku auta chcete zapůjčit? Zadejte Peugeot nebo Škoda:")
lze_pujcit_auto()

chce_znacku = input("Jakou značku auta chcete zapůjčit? Zadejte Peugeot nebo Škoda:")
lze_pujcit_auto()