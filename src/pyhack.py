#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of pyhack project : easy fork of nethack on python.


Institution : Grenoble INP - ENSIMAG
Author : BERTIN Robin & GENISSON Maxime
"""
from os import remove
from jeu import Jeu
from generate import generate_dumb, delaunay


def main():
    """
    Main function of the project Pyhack
    """
    jeu = Jeu()
    generate_dumb(jeu, 20)
    delaunay(jeu) 
    jeu.niveaux[jeu.niveau_en_cours].genere_dico()
    #for salle in jeu.niveaux[jeu.niveau_en_cours].salles.values():
    #    salle.affiche(jeu, salle.coin_bdroite[0], salle.coin_bdroite[1], 0)
    jeu.monte()
    jeu.refresh()
    jeu.refresh()
    while not jeu.stop:
        jeu.step() 
    


if __name__ == "__main__":
    main()
