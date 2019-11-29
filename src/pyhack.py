#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of pyhack project : easy fork of nethack on python.


Institution : Grenoble INP - ENSIMAG
Author : BERTIN Robin & GENISSON Maxime
"""

from jeu import Jeu

def main():
    """
    Main function of the project Pyhack
    """
    jeu = Jeu()  # Crée le jeu
    jeu.generate_niveau()
    for salle in jeu.niveaux[jeu.niveau_en_cours].salles.values():
        salle.affiche(jeu, salle.milieu()[0], salle.milieu()[1], 0)
    jeu.monte()  # Effectue une action mais ne fonction pas jsp pq
    jeu.refresh()
    while not jeu.stop:  # Tant que le jeu ne doit pas s'arreter attend un appel clavier
        jeu.step()


if __name__ == "__main__":
    main()
