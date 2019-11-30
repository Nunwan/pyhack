#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gérant les données du jeu.
Autant l'affichage que la donnée du personnage chose peut être
à séparer
"""

import datetime
import curses
import os
from niveau import Niveau, CAR
from generate import generate_dumb, delaunay

ROWS, COLUMNS = os.popen('stty size', 'r').read().split()


class Jeu:
    """
    Classe gérant le jeu dans sa généralité
    """
    def __init__(self, log=False):
        """
        Initialise le plateau de jeu en générant des salles/couloirs aléatoirement
        et un personnage en (0,0)
        """
        self.log = log
        self.taille = 100
        # Initialisation des attributs
        self.perso = [7, 8]  # Coordonnée du personnage
        self.niveau_en_cours = 0  # Le niveau dans lequel on se trouve
        self.stop = 0  # Variable pour finir le jeu

        ###
        # Fenetre
        ###
        # Création de la fenêtre
        self.window = curses.initscr()
        # Création du pad affichant le jeu
        self.pad = curses.newpad(self.taille, self.taille)
        # Création du pad affichant les infos
        self.pad_info = curses.newpad(200, 200)
        # Configuration de la fenetre
        curses.noecho()  # N'affiche pas les choses tapées
        curses.cbreak()  # laisse le buffer vide
        curses.curs_set(0)  # N'affiche pas le curseur
        #  Initialisation des niveaux du jeu
        self.niveaux = [Niveau()]

        ####
        # Bindings
        ####
        self.bindings = dict()
        self.bindings["j"] = self.descend
        self.bindings["k"] = self.monte
        self.bindings["l"] = self.droite
        self.bindings["h"] = self.gauche
        self.bindings["q"] = self.fin

        ####
        # possibilité de log
        ####
        if log:
            date = datetime.datetime.now()
            self.logfile = open("log_" + str(date) + ".txt", 'w')
            self.logfile.write("######  Logfile generate by pyhack")

    def generate_niveau(self):
        """
        Méthode générant un niveau entier pour le niveau en cours :
        Salles, couloirs, portes
        """
        generate_dumb(self, 20)
        delaunay(self)
        self.niveaux[self.niveau_en_cours].genere_dico()
        self.niveaux[self.niveau_en_cours].place_all_porte()


    def affiche(self):
        """
        Permet d'afficher le niveau en cours.
        Obsolete.
        """
        self.niveaux[self.niveau_en_cours].affiche(self)

    def affiche_perso(self):
        """
        Genere dico doit avoir été appelé peut etre ajouté une clause
        Méthode affichant le personnage là où il est
        """
        if (self.perso[0], self.perso[1]) in self.niveaux[self.niveau_en_cours].reminder:
            self.niveaux[self.niveau_en_cours].reminder[(self.perso[0], self.perso[1])].affiche(self, self.perso[0], self.perso[1], 0)
        self.pad.addstr(self.perso[1], self.perso[0], CAR["PERSO"])
        self.refresh()

    def reset_perso(self):
        """
        Méthode affichant la case sur laquelle était le personnage avant qu'il bouge
        """
        self.pad.addstr(self.perso[1], self.perso[0], self.niveaux[self.niveau_en_cours].reminder[(self.perso[0], self.perso[1])].CAR)
        self.refresh()

    def refresh(self):
        """
        Fait un refresh du pad.
        Ceci crée un système de caméra puisque cela n'affiche qu'une fenetre de 50*25
        suivant le personnage.
        """
        raw = min(int(ROWS), 25)
        column = min(int(COLUMNS), 50)
        cam_haut_y = min(max(self.perso[1] - 18, 0), self.taille - raw)
        cam_haut_x = min(max(self.perso[0] - 15, 0), self.taille - column)
        if raw < 25:
            cam_haut_y = max(self.perso[1] - 4, 0)
        if column < 50:
            cam_haut_x = max(self.perso[0] - 4, 0)
        # Log : self.pad.addstr(cam_haut_y, cam_haut_x, str(self.perso))
        self.pad.refresh(cam_haut_y, cam_haut_x, 0, 0, raw - 1, column - 1)
        self.pad_info.refresh(0, 0, 0, 60, 20, 60 + 40)

    def info(self, chaine):
        """
        Méthode basique affichant une chaine de caractère
        sur le pad d'info : à droite du jeu
        """
        self.pad_info.addstr(0, 0, chaine)

    def fin(self):
        """
        'Destructeur' fermant la fenêtre curses
        """
        self.stop = 1
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        if self.log:
            self.logfile.close()

    def in_log(self, chaine):
        """
        Methode écrivant la chaine
        dans le fichier de log si les logs
        sont activés.
        """
        if self.log:
            self.logfile.write(chaine)

    def step(self):
        """
        Fonction appelé par la boucle de jeu pour lire le clavier
        """
        key = self.window.getkey()
        if key in self.bindings:
            self.bindings[key]()


    # Fonction de déplacement
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
