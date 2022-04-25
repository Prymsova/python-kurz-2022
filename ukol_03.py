cislo_prijemce = input("Vložte telefonní číslo: ")

def overeni_platnosti_cisla(tel_cislo):
    tel_cislo = tel_cislo.replace(" ", "")
    if len(tel_cislo) == 9 or (len(tel_cislo) == 13 and tel_cislo[0:4] == "+420" in tel_cislo):
        return True
    else:
        return False

def vypocet_ceny_zpravy(text_zpravy:str, delka_sms:int=180, cena_sms:int=3):
    pocet_sms = len(text_zpravy) // delka_sms + 1
    cena_zpravy = pocet_sms * cena_sms
    return cena_zpravy


if overeni_platnosti_cisla(cislo_prijemce):
    print("číslo je platné")
    text_zpravy = input("Vložte zprávu, kterou chcete poslat: ")
    print(f"Cena Vaší zprávy je {vypocet_ceny_zpravy(text_zpravy)} Kč.")
else:
    print("vložené číslo je neplatné")