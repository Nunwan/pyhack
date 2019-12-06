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
        niveau.reminder[(self.x, self.y)] = self.salle
        del self.salle.objets[(self.x, self.y)]
        inv = perso.bag_objet
        nom = type(self).__name__
        if nom in inv:
            inv[nom] =  inv[nom] + 1
        else:
            inv[nom] = 1

class Potion_Heal(Objet):
    """
    Classe décrivant les potions du jeu
    """
    name = "Potion de soin"
    def __init__(self, x, y, jeu, salle):
        Objet.__init__(self, x, y, jeu, salle)
        self.car = "h"

    def __str__(self):
        return "h"

    @staticmethod
    def action(jeu, perso):
        perso.pv += 10
        jeu.msg("Vous gagnez 10 PV")


class Potion_Mana(Objet):
    """
    Classe décrivant les potions du jeu
    """
    name = "Potion de Mana"
    def __init__(self, x, y, jeu, salle):
        Objet.__init__(self, x, y, jeu, salle)
        self.car = "m"

    def __str__(self):
        return "m"

    @staticmethod
    def action(jeu, perso):
        perso.mana += 10
        jeu.msg("Vous gagnez 10 Mana")

