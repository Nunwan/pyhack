#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of pyhack project : easy fork of nethack on python.


Institution : Grenoble INP - ENSIMAG
Author : BERTIN Robin & GENISSON Maxime
"""

import keyboard
from jeu import Jeu

def main():
    """
    Main function of the project Pyhack
    """
    jeu = Jeu()
    #niveau1 = Niveau()
    #niveau1.affiche(jeu)

    jeu.monte()
    while not jeu.stop:
        keyboard.step(jeu)


if __name__ == "__main__":
    main()
