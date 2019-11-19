#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of pyhack project : easy fork of nethack on python.


Institution : Grenoble INP - ENSIMAG
Author : BERTIN Robin & GENISSON Maxime
"""

from jeu import Jeu
from generate import generate_dumb, delaunay


def main():
    """
    Main function of the project Pyhack
    """
    jeu = Jeu()  # Crée le jeu
    generate_dumb(jeu, 20)  # Genere les salles
    delaunay(jeu)  #Genere les couloirs 
    jeu.niveaux[jeu.niveau_en_cours].genere_dico()  # Genere le dico rappel du niveau en cours
    jeu.niveaux[jeu.niveau_en_cours].place_all_porte()
    #for salle in jeu.niveaux[jeu.niveau_en_cours].salles.values():
    #    salle.affiche(jeu, salle.coin_bdroite[0], salle.coin_bdroite[1], 0)
    jeu.monte()  # Effectue une action mais ne fonction pas jsp pq
    jeu.refresh()  # affiche le jeu
    while not jeu.stop:  # Tant que le jeu ne doit pas s'arreter attend un appel clavier
        jeu.step()


if __name__ == "__main__":
    main()
