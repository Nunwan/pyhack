#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of pyhack project : easy fork of nethack on python.


Institution : Grenoble INP - ENSIMAG
Author : BERTIN Robin & GENISSON Maxime
"""

from jeu import Jeu
from generate import generate_dumb


def main():
    """
    Main function of the project Pyhack
    """
    jeu = Jeu()
    generate_dumb(jeu, 20)
    jeu.niveaux[jeu.niveau_en_cours].genere_dico()
    for salle in jeu.niveaux[jeu.niveau_en_cours].salles:
        salle.affiche(jeu)
    jeu.monte()
    jeu.refresh()
    while not jeu.stop:
        jeu.step()

if __name__ == "__main__":
    main()
