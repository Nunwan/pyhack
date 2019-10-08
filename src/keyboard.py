#!/usr/bin/env python
# -*- coding: utf-8 -*-
from affichage import Jeu
from pynput import keyboard

def on_press(key):
    try:
        if key.char == j:
            jeu2.descend()
        elif key.char == 'k':
            jeu.monte()
        elif key.char == 'l':
            jeu.droite()
        elif key.char == 'l':
            jeu.gauche()
    except:
        if key == "key.esc":
            jeu.quit()


def init_key(jeu):
    global jeu2
    jeu2 = jeu
    with keyboard.Listener(
            on_press = on_press) as listener:

        listener.join()


