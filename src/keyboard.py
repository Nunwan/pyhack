#!/usr/bin/env python
# -*- coding: utf-8 -*-
from affichage import Jeu

def getkey(jeu):
    """
    Fonction lisant le clavier et lançant la bonne
    méthode.
    """
    key = jeu.window.getkey()
    # A lot of things with if 
    jeu.window.refresh()
