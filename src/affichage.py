#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import curses


CAR = dict()
CAR[0] = " "
CAR["SOL"] = "."
CAR[2] = "|"
CAR[3] = "-"
CAR[4] = "#"


class Jeu:
    """
    Classe gérant le jeu dans sa généralité
    """
    def __init__(self):
        """
        Initialise le plateau de jeu en générant des salles/couloirs aléatoirement
        et un personnage en (0,0)
        """
        # Initialisation des attributs
        self.perso = [0, 0]
        self.stop = 0
        # Création de la fenêtre
        self.window = curses.initscr()
        curses.noecho()
        curses.cbreak()

    def __del__(self):
        """
        Destructeur fermant la fenêtre curses
        """
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def monte(self):
        """
        Fonction d'essai pour monter le personnage
        """
        print("monte")
