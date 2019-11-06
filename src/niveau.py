#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gérant la génération et les opérations sur les
niveaux du jeu
"""

from random import randint

# Dictionnaire de l'affichage
CAR = dict()
CAR[0] = " "
CAR["SOL"] = "."
CAR["MURV"] = "|"
CAR["MURH"] = "-"
CAR["PERSO"] = "@"

MAX_TAILLE = 25
MIN_TAILLE = 4

class Salle:
    """
    Classe représentant une salle du jeu
    """
    def __init__(self, coin_hgauche, coin_bdroite):
        """
        Constructeur créant une salle à partir des deux points extrêmes
        """
        # self.deja = 0   Peut-être inutile
        self.coin_bdroite = coin_bdroite
        self.coin_hgauche = coin_hgauche
        self.portes = []  # Les portes sont de bases vides.

    def affiche_sol(self, jeu):
        """
        Méthode affichant le sol de la salle
        """
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0] +1):
            for y in range(self.coin_hgauche[1], self.coin_bdroite[1] +1):
                jeu.pad.addstr(y, x, CAR["SOL"])

    def affiche_murv(self, jeu):
        """
        Méthode affichant les murs verticaux de la salle
        """
        for y in range(self.coin_hgauche[1], self.coin_bdroite[1]+1):
            jeu.pad.addstr(y, self.coin_hgauche[0] - 1, CAR["MURV"])
            jeu.pad.addstr(y, self.coin_bdroite[0] + 1, CAR["MURV"])

    def affiche_murh(self, jeu):
        """
        Méthode affichant les murs verticaux de la salle
        """
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0]+1):
            jeu.pad.addstr(self.coin_hgauche[1] - 1, x, CAR["MURH"])
            jeu.pad.addstr(self.coin_bdroite[1] + 1, x, CAR["MURH"])

    def affiche(self, jeu):
        """
        Méthode regroupant les méthodes précédentes et affichant toute la salle
        """
        self.affiche_sol(jeu)
        self.affiche_murh(jeu)
        self.affiche_murv(jeu)
        jeu.refresh()

    def milieu(self):
        """
        Renvoie le milieu de la salle
        """
        x_milieu = (self.coin_bdroite[0] - self.coin_hgauche[0])//2
        y_milieu = (self.coin_bdroite[1] - self.coin_hgauche[1])//2
        return (x_milieu, y_milieu)

    def genere_dico(self, dico, salle):
        """
        Génère le dico appelé par la méthode Niveau.genere_dico.
        Met la salle en tous les points la composant.
        """
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0] + 1):
            for y in range(self.coin_hgauche[1], self.coin_bdroite[1] + 1):
                dico[(x, y)] = salle



class Couloir:
    """
    Classe représentant les couloirs
    """
    def __init__(self, points):
        self.points = points


    # Méthode d'affichage surement nul, à faire
    def affiche(self):
        for _ in range(len(self.points) -1):
            pass

    def genere_dico(self, dico, salle):
        pass


class Niveau:
    """
    Classe représentant un niveau du jeu
    """
    import generate
    def __init__(self):
        """
        Le constructeur construit un niveau vide de salles et de couloir
        """
        self.couloirs = []
        self.salles = dict()
        self.genere_dico()

    def genere_dico(self):
        """
        Genere un dico tel que dico[(i,j)] = l'objet voulu : salle couloir etc ... en le point i,j
        """
        self.reminder = dict()
        for salle in self.salles:
            salle.genere_dico(self.reminder, salle)
        #for c in self.couloirs:
        #    c.genere_dico(self.niveau, c)

    def affiche(self, jeu):
        for salle in self.salles:
            salle.affiche(jeu)


