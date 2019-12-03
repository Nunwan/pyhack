"""
Module gérant les objets et leur interaction
"""
from inspect import getmembers, isclass
import sys
current_module = sys.modules[__name__]


def liste_objet():
    """
    Renvoie la liste des sous_objets présents dans le module
    """
    L = []
    for name, obj in getmembers(sys.modules[__name__]):
        if isclass(obj) and name != "Objet":
            L.append(obj)
    return L

def genere_dico_objet():
    dico = dict()
    for objet in liste_objet():
        dico[objet.__name__] = str(objet.__str__(objet))
    return dico

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

    def __str__(self):
        return "o"

    def affiche(self, x, y, jeu):
        self.salle.affiche(self.salle.milieu()[0], self.salle.milieu()[1], 0)

    def pick(self, perso):
        niveau = self.jeu.niveaux[self.jeu.perso.niveau_en_cours]
        reminder = niveau.reminder
        niveau.reminder[(self.x, self.y)] = self.salle
        del self.salle.objets[(self.x, self.y)]
        inv = perso.bag_objet
        if self in inv:
            inv[self] += 1
        else:
            inv[self] = 1

class Potion(Objet):
    """
    Classe décrivant les potions du jeu
    """
    def __init__(self, x, y, jeu, salle):
        Objet.__init__(self, x, y, jeu, salle)
        self.car = "p"

    def __str__(self):
        return "p"

    def action(self, perso):
        perso.pv += 10
        self.jeu.msg("Vous gagnez 10 PV")

