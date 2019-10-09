#!/usr/bin/env python
# -*- coding: utf-8 -*-
import niveau
import numpy as np
car = dict()
car[0] = " "
car[1] = "."
car[2] = "|"
car[3] = "-"
car[4] = "#"


class Jeu:
    """
    Classe gérant le jeu dans sa généralité
    """
    def __init__(self):
        """
        Initialise le plateau de jeu en générant des salles/couloirs aléatoirement
        et un personnage en (0,0)
        """
        self.perso = [0,0]
        self.plateau = np.zeros((20,30))
        self.stop = 0
    def refresh(self):
        """
        Affiche le plateau de jeu
        """
        n,m = self.plateau.shape
        for i in range(n):
            for j in range(m):
                print(car[self.plateau[i][j]])

    def monte(self):
        print("monte")
