#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gérant la génération et les opérations sur les
niveaux du jeu
"""

class Salle:
    """
    essai
    """
    def __init__(self, position, taille):
        self.deja = 0
        self.pos =  position
        self.taille = taille
        self.portes = []  # Les portes sont de bases vides.

def generation(jeu):
    """
    """
    salles = []  # A generer aléatoirement
    for salle in salles:
        salle.introduit(jeu.plateau)
