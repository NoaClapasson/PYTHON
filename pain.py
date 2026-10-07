class personnage:
    def __init__(self, nom: str, age: int):
        self.hp:int = 100
        self.mana:int = 50
        self.nom:str = nom
        self.atq:int = 10
        self.defense:int = 5
        self.fireball:int = 40
        self.defense.fireball:int = 30
        self.afficher_stats()
perso_1: Personnage =Personnage("Alex", 17)
perso_2: Personnage =Personnage("Sarah", 21)

print(perso_1.nom)
print(perso_2.nom)


def attack(attaque: Personnage, defense: Personnage):
    damage: int = attaque.atq - defense.defense
    if defense.hp <= 0:
        print(f"{defense.nom} est déjà vaincu.")
        return
    if damage > 0:
        defense.hp -= damage
        print(f"{attaque.nom} attaque {defense.nom} et inflige {damage} points de dégâts.")
        print(f"{defense.nom} a maintenant {defense.hp} points de vie.")
    else:
        attaque.hp -= damage
        defense.hp -= damage
        print(f"{attaque.nom} attaque {defense.nom} et inflige {damage} points de dégâts.")
        print(f"{defense.nom} a maintenant {defense.hp} points de vie.")
        print(f"{fireball.nom} a maintenant {fireball.hp} points de vie.")


def fireball(attaque: Personnage, defense: Personnage):
    damage: int = attaque.fireball - defense.defense.fireball
    if defense.hp <= 0:
        print(f"{defense.nom} est déjà vaincu.")
        return
    if damage > 0:
        defense.hp -= damage
        print(f"{attaque.nom} lance une boule de feu sur {defense.nom} et inflige {damage} points de dégâts.")
        print(f"{defense.nom} a maintenant {defense.hp} points de vie.")
    else:
        attaque.hp -= damage
        defense.hp -= damage
        print(f"{attaque.nom} lance une boule de feu sur {defense.nom} et inflige {damage} points de dégâts.")
        print(f"{defense.nom} a maintenant {defense.hp} points de vie.")
        print(f"{fireball.nom} a maintenant {fireball.hp} points de vie.")


def afficher_stats(self) -> None:
    print(f"Nom: {self.nom}, HP: {self.hp}, Mana: {self.mana}, ATQ: {self.atq}, DEF: {self.defense}, Fireball: {self.fireball}, DEF Fireball: {self.defense.fireball}")
