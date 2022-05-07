# PRODEJ VSTUPENEK
# ceny vstupenek 1. 7. 2021 - 10. 8. 2021: 250 Kč, 11. 8. 2021 - 31. 8. 2021: 180 Kč, jinak zavřeno
# dotaz na uživatele na datum (ve středoevropském formátu - převeď řetězec na datum pomocí fce datetime.strptime() ) a dotaz na počet vstupenek
# datum kdy zavřeno - vypiš info, pokud otevřeno - spočítej a vypiš cenu vstupenky

from datetime import datetime

kino_otevreno = datetime(2021, 7, 1)
kino_prelom_ceny = datetime(2021, 8, 10)
kino_zavreno = datetime(2021, 8, 31)
cervenec_cena = 250
srpen_cena = 180

def vypocti_cenu(cena, listky_pocet):
    return cena * listky_pocet
    
listky_datum = input("Zadejte datum, na kdy chcete lístky (prosím, uveďte ve formátu 11. 7. 2022):")
listky_datum = datetime.strptime(listky_datum, "%d. %m. %Y")

listky_pocet = input("Kolik chcete lístků (uveďte číslicí):")
listky_pocet = int(listky_pocet)

if listky_datum < kino_otevreno or listky_datum > kino_zavreno:
    print("V tomto termínu máme zavřeno.")
elif listky_datum <= kino_prelom_ceny:
    print(f"Cena vstupenek: {vypocti_cenu(cervenec_cena, listky_pocet)}.")
elif listky_datum > kino_prelom_ceny:
    print(f"Cena vstupenek: {vypocti_cenu(srpen_cena, listky_pocet)}.")
else:
    print("Někde se stala chyba.")