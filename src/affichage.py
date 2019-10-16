#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import curses


CAR = dict()
CAR[0] = " "
CAR["SOL"] = "."
CAR["MURV"] = "|"
CAR["MURH"] = "-"
CAR["PERSO"] = "@"


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
        self.perso = [7, 8]
        self.stop = 0
        # Création de la fenêtre
        self.window = curses.initscr()
        curses.noecho()
        curses.cbreak()
    

    def affiche_perso(self):
        self.window.addstr(self.perso[1], self.perso[0], CAR["PERSO"])
        self.window.refresh()

    def reset_perso(self):
        self.window.addstr(self.perso[1], self.perso[0], CAR["SOL"])
        self.window.refresh()   

    def fin(self):

        """
        Destructeur fermant la fenêtre curses
        """
        self.stop = 1
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def monte(self):
        """
        Fonction d'essai pour monter le personnage
        """
        self.reset_perso() 
        self.perso[1] -= 1
        self.affiche_perso()

    def descend(self):
        """
        Fonction d'essai pour monter le personnage
        """
        self.reset_perso() 
        self.perso[1] += 1
        self.affiche_perso()

    def gauche(self):
        """
        Fonction d'essai pour monter le personnage
        """
        self.reset_perso() 
        self.perso[0] -= 1
        self.affiche_perso()

    def droite(self):
        """
        Fonction d'essai pour monter le personnage
        """
        self.reset_perso() 
        self.perso[0] += 1
        self.affiche_perso()
