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
from niveau import Niveau
from perso import Personnage
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
        self.perso = Personnage(self)
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
        self.niveaux = [Niveau(self)]
        self.dico_objet = dict()

        ####
        # Bindings
        ####
        self.bindings = dict()
        self.bindings["j"] = self.perso.descend
        self.bindings["k"] = self.perso.monte
        self.bindings["l"] = self.perso.droite
        self.bindings["h"] = self.perso.gauche
        self.bindings["i"] = self.perso.affiche_inventaire
        self.bindings["q"] = self.fin
        self.bindings["u"] = self.perso.utilisation

        ####
        # possibilité de log
        ####
        if log:
            date = datetime.datetime.now()
            self.logfile = open("log_" + str(date) + ".txt", 'w')
            self.logfile.write("######  Logfile generate by pyhack")



    def accueil(self):
        """
        Méthode gérant l'accueil du jeu.
        """
        confirmation = self.oui_non("Bienvenue sur le pyhack de BERTIN Robin \n \
Voulez vous commencer une partie ? (o/n)")
        if confirmation:
            self.window.clear()
            self.window.refresh()
            self.perso.monte()
        else:
            self.fin(True)

    def generate_niveau(self):
        """
        Méthode générant un niveau entier pour le niveau en cours :
        Salles, couloirs, portes
        """
        generate_dumb(self, 20)
        delaunay(self)
        self.niveaux[self.perso.niveau_en_cours].genere_dico()
        #self.niveaux[self.perso.niveau_en_cours].place_all_porte()

    def refresh(self):
        """
        Fait un refresh du pad.
        Ceci crée un système de caméra puisque cela n'affiche qu'une fenetre de 50*25
        suivant le personnage.
        """
        raw = min(int(ROWS), 25)
        column = min(int(COLUMNS), 50)
        cam_haut_y = min(max(self.perso.position[1] - 18, 0), self.taille - raw)
        cam_haut_x = min(max(self.perso.position[0] - 15, 0), self.taille - column)
        if raw < 25:
            cam_haut_y = max(self.perso.position[1] - 4, 0)
        if column < 50:
            cam_haut_x = max(self.perso.position[0] - 4, 0)
        # Log : self.pad.addstr(cam_haut_y, cam_haut_x, str(self.perso))
        self.pad.refresh(cam_haut_y, cam_haut_x, 1, 0, raw - 1, column - 1)
        self.pad_info.refresh(0, 0, 2, 60, 20, 60 + 40)
        self.window.refresh()

    def msg(self, chaine, override_limit=False):
        """
        Affiche la chaine donnée sur la première ligne du jeu
        """
        if len(chaine) <=  100 or override_limit:
            self.window.addstr(0, 0, " " * 50)
            self.refresh()
            self.window.addstr(0, 0, chaine)
            self.refresh()

    def info(self, chaine):
        """
        Méthode basique affichant une chaine de caractère
        sur le pad d'info : à droite du jeu
        """
        self.pad_info.clear()
        self.pad_info.addstr(0, 0, chaine)
        self.refresh()

    def oui_non(self, msg):
        """
        Demande une confirmation
        """
        self.msg(msg, True)
        key = self.window.getkey()
        while key != "o" and key != "n":
            key = self.window.getkey()
        if key == "o":
            return True
        else:
            return False

    def fin(self, override=False):
        """
        'Destructeur' fermant la fenêtre curses
        """
        confirmation = self.oui_non("Voulez-vous vraiment quitter ? (o/n)")
        if confirmation or override:
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
        self.window.addstr(26, 0, str(self.perso))
        if key in self.bindings:
            self.pad_info.clear()
            self.refresh()
            self.bindings[key]()
