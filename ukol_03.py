tel_cislo = input("Zadejte telefonní číslo, na které chcete zaslat SMS zprávu:")

def kontrola_cisla():
    delka_cisla = len(tel_cislo)

    if delka_cisla == 9 or (delka_cisla == 13 and "+420" in tel_cislo):
        text_zpravy = input("Napište text SMS zprávy, kterou chcete odeslat:")
        pocet_zprav = len(text_zpravy) // 180 + 1

        def vypocet_ceny(pocet_zprav, cena_SMS=3):
            cena_zpravy = pocet_zprav * cena_SMS
            print(f"Vaše zpráva byla odeslána. Cena Vaší zprávy je {cena_zpravy} Kč.")

        vypocet_ceny(pocet_zprav)

    else:
        print(f"Chyba formátu čísla - prosím, ověřte si správnost telefonního čísla.")

kontrola_cisla()