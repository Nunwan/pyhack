#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gérant le clavier et les intéractions avec celui-ci
"""
def step(jeu):
    """
    Fonction lisant le clavier et lançant la bonne
    méthode.

    q : ferme le jeu
    j : le joueur descend
    k : il monte
    h : il va à gauche
    l : il va à droite
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
