#4 "Do not worry about your difficulties in Mathematics. I can assure you mine are still greater."
vokaler = "aeiouy"
mening="Do not worry about your difficulties in Mathematics. I can assure you mine are still greater."
vokalerna = []

for ord in mening: #Varje ord gås igenom mening
    for vokal in vokaler: #Varje ord i vokaler
        if ord == vokal:#Går igenom varje ord och om det finns en vokal i det, ifall det ger till vokaler
            vokalerna.append(ord)

print(f"Antalet vokaler är {len(vokalerna)}")
print("\n")
print(f"Vokalerna är: {vokalerna}")
