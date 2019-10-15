#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gérant la génération et les opérations sur les
niveaux du jeu
"""

from affichage import Jeu, CAR

class Salle:
    """
    essai
    """
    def __init__(self, coin_hgauche, coin_bdroite):
        # self.deja = 0   Peut-être inutile
        self.coin_bdroite = coin_bdroite 
        self.coin_hgauche = coin_hgauche 
        self.portes = []  # Les portes sont de bases vides.
    
    def affiche(self, jeu):
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0] +1):
            for y in range(self.coin_hgauche[1], self.coin_bdroite[1] +1):
                jeu.window.addstr(y, x, CAR["SOL"])

