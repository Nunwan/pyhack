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

from niveau import Niveau

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
        self.perso = [7, 8]  # Coordonnée du personnage
        self.niveau_en_cours = 0  # Le niveau dans lequel on se trouve
        self.stop = 0  # Variable pour finir le jeu 
        # Création de la fenêtre
        self.window = curses.initscr()
        curses.noecho()  # N'affiche pas les choses tapées
        curses.cbreak()  # laisse le buffer vide
        #  Initialisation des niveaux du jeu
        self.niveaux = [Niveau()]

    def affiche_perso(self):
        """
        Méthode affichant le personnage là où il est
        """
        if (self.perso[0], self.perso[1]) in self.niveaux[self.niveau_en_cours].reminder:
            self.niveaux[self.niveau_en_cours].reminder[(self.perso[0], self.perso[1])].affiche(self)
        self.window.addstr(self.perso[1], self.perso[0], CAR["PERSO"])
        self.window.refresh()

    def reset_perso(self):
        """
        Méthode affichant la case sur laquelle était le personnage avant qu'il bouge
        """
        self.window.addstr(self.perso[1], self.perso[0], CAR["SOL"])
        self.window.refresh()

    def fin(self):
        """
        'Destructeur' fermant la fenêtre curses
        """
        self.stop = 1
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def monte(self):
        """
        Fonction montant le personnage
        """
        self.reset_perso()
        if (self.perso[0], self.perso[1] - 1) in self.niveaux[self.niveau_en_cours].reminder:
            self.perso[1] -= 1
        self.affiche_perso()

    def descend(self):
        """
        Méthode faisant descendre le perso
        """
        self.reset_perso()
        if (self.perso[0], self.perso[1] + 1) in self.niveaux[self.niveau_en_cours].reminder:
            self.perso[1] += 1
        self.affiche_perso()

    def gauche(self):
        """
        Methode déplacant le perso à gauche
        """
        self.reset_perso()
        if (self.perso[0] - 1, self.perso[1]) in self.niveaux[self.niveau_en_cours].reminder:
            self.perso[0] -= 1
        self.affiche_perso()

    def droite(self):
        """
        Méthode déplacant le perso à droite
        """
        self.reset_perso()
        if (self.perso[0] + 1, self.perso[1]) in self.niveaux[self.niveau_en_cours].reminder:
            self.perso[0] += 1
        self.affiche_perso()
