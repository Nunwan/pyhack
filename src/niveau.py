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
CAR["COULOIR"] = "#"

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


def milieu_deux(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x1 + x2) // 2, (y1 + y2)//2


def plus_haute_basse(salle1, salle2):
    if salle1.milieu()[1] <= salle2.milieu()[1]:
        return salle1, salle2
    else:
        return salle2, salle1


def plus_gauche_droite(salle1, salle2):
    if salle1.milieu()[0] <= salle2.milieu()[0]:
        return salle1, salle2
    else:
        return salle2, salle1


class Couloir:
    """
    Classe représentant les couloirs
    """
    def __init__(self, salle1, salle2):
        self.salle1 = salle1
        self.salle2 = salle2


    # Méthode d'affichage surement nul, à faire
    def affiche(self, jeu):
        if (jeu.perso[0] + 1, jeu.perso[1]) in jeu.reminder:
            jeu.addstr(jeu.perso[1], jeu.perso[0] + 1, CAR["COULOIR"])
        if (jeu.perso[0] - 1, jeu.perso[1]) in jeu.reminder:
            jeu.addstr(jeu.perso[1], jeu.perso[0] - 1, CAR["COULOIR"])
        if (jeu.perso[0], jeu.perso[1] + 1) in jeu.reminder:
            jeu.addstr(jeu.perso[1] + 1, jeu.perso[0], CAR["COULOIR"])
        if (jeu.perso[0], jeu.perso[1] - 1) in jeu.reminder:
            jeu.addstr(jeu.perso[1] - 1, jeu.perso[0], CAR["COULOIR"])


    def genere_dico(self, dico):
        if len(dico) == 0:
            self.salle1.genere_dico(dico)
            self.salle2.genere_dico(dico)
        mid_x, mid_y = milieu_deux(self.salle1.milieu(), self.salle2.milieu())
        haute, basse = plus_haute_basse(self.salle1, self.salle2)
        gauche, droite = plus_gauche_droite(self.salle1, self.salle2)
        if self.salle1.coin_hgauche[0] <= mid_x <= self.salle1.coin_bdroite[0]:
            for y in range(haute.coin_bdroite[1] + 1, basse.coin_hgauche[1]):
                dico[(mid_x, y)] = self
        if self.salle1.coin_hgauche[1] <= mid_y <= self.salle1.coin_bdroite[1]:
            for x in range(gauche.coin_bdroite[0] + 1, droite.coin_hgauche[0]):
                dico[(x, mid_y)] = self
        else:
            for x in range(gauche.coin_bdroite[0] + 1, mid_x + 1):
                dico[(x, mid_y)] = self
            for y in range(haute.coin_bdroite[1] + 1, mid_y):
                dico[(mid_x, mid_y)] = self


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


