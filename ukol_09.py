import pandas

# UKOL 9 - ADOPCE ZVÍŘAT
# Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.
zvirata = pandas.read_csv("adopce-zvirat.csv", sep=";")

# Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?
zvirata.info()
# odpověď: tabulka má 513 řádků záznamů a 6 sloupců (vč. číselného id)

# Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině.
print(zvirata.iloc[34, [1, 2]])
# odpověď: CZ Ibis bílý, EN White ibis


print("-"*30)
# ------------- BONUS --------------

# Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině. Všimni si, že sloupec teď povýší na index a už se nenachází mezi "běžnými" sloupci.
zvirata2 = pandas.read_csv("adopce-zvirat.csv", sep=";", index_col="nazev_cz")
print(zvirata2.head())

# Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.
print(zvirata2.index.is_unique)
# odpověď: ano, index "nazev_cz" je unikátní

# Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index(). Bacha, metoda vrátí novou tabulku se seřazeným indexem. Budeš tedy chtít přepsat původní tabulku.
zvirata2 = zvirata2.sort_index()
print(zvirata2.head())

# Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.
print(zvirata2.loc["Outloň váhavý"])

# Rozsahy fungují podobně jako u číselných indexů. Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá".
print(zvirata2.loc["Želva Smithova":"Želva žlutočelá"])
# DOTAZ: proč nejsou výsledky seřazeny abecedně i v přídavcích? tedy želva annámská před želvou Smithovou?