#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module of pyhack project : easy fork of nethack on python.


Institution : Grenoble INP - ENSIMAG
Author : BERTIN Robin & Genisson Maxime
"""

import keyboard
from jeu import Jeu
from niveau import Niveau

def main():
    """
    Main function of the project Pyhack
    """
    jeu = Jeu()
    niveau1 = Niveau() 
    #niveau1.affiche(jeu)
    jeu.affiche_perso() 
    
    while not jeu.stop:
        keyboard.step(jeu) 
    

if __name__ == "__main__":
    main()
