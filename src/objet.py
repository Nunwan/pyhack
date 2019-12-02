"""
Module gérant les objets et leur interaction
"""


class Objet:
    """
    Classe gérant les objets
    """

    def __init__(self, x, y, jeu, salle):
        self.salle = salle
        self.x = x
        self.y = y
        self.car = "o"
        self.jeu = jeu

    def affiche(self, x, y, jeu):
        self.salle.affiche(jeu, self.salle.milieu()[0], self.salle.milieu()[1], 0)
    
    def action(self):
        pass

class Potion(Objet):
    """
    Classe décrivant les potions du jeu
    """

    def __init__(self, x, y, jeu, salle):
        Objet.__init__(self, x, y, jeu, salle)
        self.car = "p"

    def action(self, perso):
        perso.pv += 10
        self.jeu.msg("Vous gagnez 10 PV")
