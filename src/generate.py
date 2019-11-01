"""
Module gérant la génération des niveaux
"""


from random import randint
from niveau import Salle
#from jeu import Jeu

MAX_TAILLE = 25
MIN_TAILLE = 4

def intersection(salle1, salle2):
    """
    Fonction renvoyant si les deux salles s'intersectent.
    """
    if salle1.coin_hgauche[0] <= salle2.coin_hgauche[0] <= salle1.coin_bdroite[0] and salle1.coin_bdroite[1] <= salle2.coin_hgauche[1] <= salle1.coin_bdroite[1]:
        return True
    if salle2.coin_hgauche[0] <= salle1.coin_hgauche[0] <= salle2.coin_bdroite[0] and salle2.coin_bdroite[1] <= salle1.coin_hgauche[1] <= salle2.coin_bdroite[1]:
        return True
    return False

def generate_dumb(jeu, number):
    """
    Fonction générant une liste de number salles aléatoires dans le jeu
    """
    rooms = []
    for _ in range(number):
        height = randint(MIN_TAILLE, MAX_TAILLE)
        width = randint(MIN_TAILLE, MAX_TAILLE)
        coin_hgauche = [randint(0, jeu.taille - width), randint(0, jeu.taille - height)]
        coin_bdroite = [coin_hgauche[0] + width, coin_hgauche[1] + height]
        rooms.append(Salle(coin_hgauche, coin_bdroite))
    return rooms

def a_une_intersection(indice_salle, niveau):
    for indice, salle in enumerate(niveau.salles):
        if indice_salle != indice and intersection(niveau.salles[indice_salle], salle):
            return True
    return False



def deplace(niveau):
    for indice, salle in enumerate(niveau.salles):
        i = 0
        x = randint(-1, 1)
        y = randint(-1, 1)
        while i < 100 and a_une_intersection(indice, niveau):
            salle.coin_bdroite[0] += x
            salle.coin_hgauche[0] += x
            salle.coin_bdroite[1] += y
            salle.coin_hgauche[1] += y
        if i == 100:
            return 0
    return 1
