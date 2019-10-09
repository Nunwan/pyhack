#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of pyhack project : easy fork of nethack on python.


Institution : Grenoble INP - ENSIMAG
Author : BERTIN Robin & Genisson Maxime
"""

import keyboard
from affichage import Jeu


def main():
    """
    Main function of the project Pyhack
    """
    jeu = Jeu()
    while not jeu.stop:
        keyboard.getkey(jeu)



if __name__ == "__main__":
    main()
