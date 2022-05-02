import re
regularniVyraz = re.compile(r"\d{3} \d{2} \w+ ?\w+ ?\w+")

with open("posta.html", encoding='utf-8') as vstup:
    data = vstup.read()

data = data.replace("\n", " ")
data = re.sub(" {2,}", " ", data)

ukazkova_mesta = regularniVyraz.findall(data)

print(ukazkova_mesta)
print(len(ukazkova_mesta))