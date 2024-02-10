
from random import randint


class JeuDeDes:
    def __init__(self):
        self.resultat = None

    def lancer_from(self):
        self.resultat = randint(1, 6)


jeu = JeuDeDes()


jeu.lancer_from()


print(f"Le résultat du lancer de dé est : {jeu.resultat}")


for _ in range(3):
    jeu.lancer_from()
    print(f"Nouveau résultat : {jeu.resultat}")


if jeu.resultat % 2 == 0:
    print("Le résultat est pair.")
else:
    print("Le résultat est impair.")
