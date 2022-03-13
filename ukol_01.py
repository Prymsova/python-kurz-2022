baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}


c_baliku = input("Jaké je Vaše číslo balíku?")

if c_baliku in baliky:
    if baliky[c_baliku] == True:
        print(f"Balík byl předán kurýrovi.")
    else:
        print(f"Balík zatím nebyl předán kurýrovi.")

else:
    print("Chybně zadané číslo balíku.")