#!/usr/bin/env python
# -*- coding: utf-8 -*-
import niveau

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

    def refresh(self):
        """
        Affiche le plateau de jeu
        """
        pass
