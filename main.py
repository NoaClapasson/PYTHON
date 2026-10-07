prenom: str = "Alex"
age: int = 17   
taille: float = 1.72
est_majeur: bool = False

if age >= 18:
    est_majeur = True
if est_majeur == True:
    print(f"Nom: {prenom} a {age} ans, mesure {taille} m et est majeur.")
else:  
    print(f"Nom: {prenom} a {age} ans, mesure {taille} m et est mineur.")

notes: list[int] = [12, 8, 15, 19, 6, 14]
print(len(notes))
print(max(notes))
print(min(notes))
moyenne: float = sum(notes) / len(notes)
print(f"La moyenne des notes est: {moyenne}")
notes.append(17)
print(notes)

etudiant: dict = {
    "prenom": "sarah",
    "age": 21,
    "notes": [14, 16, 12]
}
moyenne_etudiant: float = sum(etudiant["notes"]) / len(etudiant["notes"])
print(moyenne_etudiant)


contact: list[dict] = []
input: int = int(input("Combien de contacts voulez-vous ajouter ? "))
for i in range(input):
    nom: str = input(f"Entrez le nom du contact {i + 1}: ")
    numero: str = input(f"Entrez le numéro du contact {i + 1}: ")
    contact.append({"nom": nom, "numero": numero})
for contact in contact:
    print(f"Nom: {contact['nom']}, Numéro: {contact['numero']}")
print(f"nbre de contacts: {len(contact)}")

