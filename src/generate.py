"""
Module gérant la génération des niveaux
"""


from random import randint
from niveau import Salle
#from jeu import Jeu

MAX_TAILLE = 15
MIN_TAILLE = 4

def intersection(salle1, salle2):
    """
    Fonction renvoyant si les deux salles s'intersectent.
    """
    a = salle1.coin_hgauche[0] - 1 > salle2.coin_bdroite[0] + 1
    b = salle1.coin_bdroite[0] + 1 < salle2.coin_hgauche[0] - 1
    c = salle1.coin_bdroite[1] + 1 < salle2.coin_hgauche[1] - 1
    d = salle1.coin_hgauche[1] - 1 > salle2.coin_bdroite[1] + 1
    if not(a or b or c or d):
        return True
    return False

def generate_dumb(jeu, number):
    """
    Fonction générant une liste de number salles aléatoires dans le jeu
    """
    pas = 150
    for i in range(number):
        r = None
        j = 0
        while j <= pas and (r is None or a_une_intersection(r, jeu.niveaux[jeu.niveau_en_cours])):
            height = randint(MIN_TAILLE, MAX_TAILLE)
            width = randint(MIN_TAILLE, MAX_TAILLE)
            coin_hgauche = [randint(1, jeu.taille - width-2), randint(1, jeu.taille - height-2)]
            coin_bdroite = [coin_hgauche[0] + width, coin_hgauche[1] + height]
            if coin_bdroite[0] == jeu.taille or coin_bdroite[1] == jeu.taille:
                r = None
            r = Salle(coin_hgauche, coin_bdroite)
        jeu.niveaux[jeu.niveau_en_cours].salles.append(r)
        if j > pas:
            return 0
    # Placement du joueur initialement
    x_init = jeu.niveaux[jeu.niveau_en_cours].salles[0].coin_hgauche[0] + 2
    y_init = jeu.niveaux[jeu.niveau_en_cours].salles[0].coin_hgauche[1] + 3
    jeu.perso = [x_init, y_init]
    return 1


def a_une_intersection(salle, niveau):
    for salle1 in niveau.salles:
        if intersection(salle1, salle) or intersection(salle, salle1):
            return True
    return False
