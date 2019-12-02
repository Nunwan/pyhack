"""
Module gérant les objets et leur interaction
"""


class Objet:
    """
    Classe gérant les objets
    """

    def __init__(self, jeu, x, y, salle):
        self.salle = salle
        self.x = x
        self.y = y
        self.car = "o"
        self.jeu = jeu

    def affiche(self, x, y, jeu):
        self.salle.affiche(self.salle.milieu()[0], self.salle.milieu()[1], 0)
    

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
        niveau = self.jeu.niveaux[self.jeu.perso.niveau_en_cours]
        reminder = niveau.reminder
        niveau.reminder[(self.x, self.y)] = self.salle
        del self.salle.objets[(self.x, self.y)] 
