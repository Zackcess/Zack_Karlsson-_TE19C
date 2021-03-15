person=dict(
    namn="Kokchun",
    ålder = "15",
    yrke="lärare",
    arbetsplats="NTI"
)
#åtkomsoperatorn [] för att hitta värdena i key:value par
print(person["arbetsplats"])

glosor ={
    "tilldela":"ge ett värde till en variabel",
    "datastruktur": "strukturering av data",
    "sträng": "sekvens av tecken"
}
#lägga till ett element
glosor["dictionary"] = "datastruktur för att spara data i key:value par"

print("Ord vi behöver lära oss: ")
#Ett sätt att loopa igenom en dict
for key in glosor:
    print(f"{key} \t {glosor[key]} ")

for key, value in glosor.items():
    print(f"{key} \t {value}")

husdjur={
    "djur": "fisk",
    "ålder": 5,
    "ätbar": False,
    "actions":["simma fram", "simma bak", "äta"]
}