#!/usr/bin/env python
# -*- coding: utf-8 -*-
from affichage import Jeu
import pyxhook

def on_press(event, jeu):
    if event.Ascii == 106:
        jeu.descend()
    elif event.Ascii == 107:
        jeu.monte()
    elif event.Ascii == 108:
        jeu.droite()
    elif event.Ascii == 104:
        jeu.gauche()
    elif event.Ascii == 27:
        jeu.stop = 1

def init_key(jeu):
    hookman = pyxhook.HookManager(parameters=True)
    hookman.KeyDown = on_press
    hookman.KeyDownParameters = jeu
    return hookman
