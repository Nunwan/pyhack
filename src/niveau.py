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
    
    def affiche_sol(self, jeu):
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0] +1):
            for y in range(self.coin_hgauche[1], self.coin_bdroite[1] +1):
                jeu.window.addstr(y, x, CAR["SOL"])
    
    def affiche_murv(self,jeu):
        for y in range(self.coin_hgauche[1], self.coin_bdroite[1]+1): 
            jeu.window.addstr(y, self.coin_hgauche[0] - 1, CAR["MURV"])
            jeu.window.addstr(y, self.coin_bdroite[0] + 1, CAR["MURV"]) 
    
    def affiche_murh(self,jeu):
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0]+1): 
            jeu.window.addstr(self.coin_hgauche[1] - 1, x, CAR["MURH"])
            jeu.window.addstr(self.coin_bdroite[1] + 1, x, CAR["MURH"]) 

    def affiche(self,jeu):
        self.affiche_sol(jeu)
        self.affiche_murh(jeu)
        self.affiche_murv(jeu)
        jeu.window.refresh()
        
