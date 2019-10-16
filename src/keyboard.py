#!/usr/bin/env python
# -*- coding: utf-8 -*-
from affichage import Jeu

def step(jeu):
    """
    Fonction lisant le clavier et lançant la bonne
    méthode.
    """
    key = jeu.window.getkey()
    if key == "q":
        jeu.fin()
    if key == "j":
        jeu.descend()
    if key == "k":
        jeu.monte()
    if key == "h":
        jeu.gauche()
    if key == "l":
        jeu.droite()
