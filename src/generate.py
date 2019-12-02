"""
Module gérant la génération des niveaux
"""


from random import randint, choice, seed
from niveau import Salle, Couloir
from scipy.spatial import Delaunay
#from jeu import Jeu

MAX_TAILLE = 15
MIN_TAILLE = 4
# A décommenter ssi on debug
seed(1234567890)

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
        while j <= pas and (r is None or a_une_intersection(r, jeu.niveaux[jeu.perso.niveau_en_cours])):
            height = randint(MIN_TAILLE, MAX_TAILLE)
            width = randint(MIN_TAILLE, MAX_TAILLE)
            coin_hgauche = [randint(1, jeu.taille - width-2), randint(1, jeu.taille - height-2)]
            coin_bdroite = [coin_hgauche[0] + width, coin_hgauche[1] + height]
            if coin_bdroite[0] == jeu.taille or coin_bdroite[1] == jeu.taille:
                r = None
            r = Salle(jeu, coin_hgauche, coin_bdroite)
        x_mid, y_mid = r.milieu()
        jeu.niveaux[jeu.perso.niveau_en_cours].salles[(x_mid, y_mid)] = r
        if j > pas:
            continue
    # Placement du joueur initialement
    salle = choice(list(jeu.niveaux[jeu.perso.niveau_en_cours].salles.values()))
    x_init, y_init = salle.milieu()
    jeu.perso.position = [x_init + 2, y_init + 2]
    return 1


def a_une_intersection(salle, niveau):
    """
    Renvoie le boléen la salle a une intersection avec une des
    salles présentes dans le niveau
    """
    for salle1 in niveau.salles.values():
        if intersection(salle1, salle) or intersection(salle, salle1):
            return True
    return False


def liste_milieu(jeu):
    """
    Renvoie la liste des milieux de toutes les salles.
    """
    return  [milieu for milieu in jeu.niveaux[jeu.perso.niveau_en_cours].salles.keys()]

def delaunay(jeu):
    """
    Applique l'algorithme de Delaunay aux milieux des salles pour avoir une triangulation
    optimale.
    Rentre ensuite les couloirs dans le dico prévu dans la classe niveau
    """
    milieux = liste_milieu(jeu)
    triangles = Delaunay(milieux).simplices
    couloirs = jeu.niveaux[jeu.perso.niveau_en_cours].couloirs
    salles = jeu.niveaux[jeu.perso.niveau_en_cours].salles
    for p1, p2, p3 in triangles:
        if (p1, p2) not in couloirs and (p2, p1) not in couloirs:
            couloirs[(p1, p2)] = Couloir(jeu, salles[milieux[p1]], salles[milieux[p2]])
        if (p3, p2) not in couloirs and (p2, p3) not in couloirs:
            couloirs[(p2, p3)] = Couloir(jeu, salles[milieux[p2]], salles[milieux[p3]])
        if (p1, p3) not in couloirs and (p3, p1) not in couloirs:
            couloirs[(p1, p3)] = Couloir(jeu, salles[milieux[p1]], salles[milieux[p3]])
