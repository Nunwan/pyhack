"""
Module gérant la création de Perso
"""

def choix_race(jeu):
    msg = open('../data/msg_create.txt', 'r')
    contenu = msg.read()
    msg_race = contenu.splitlines()[0:14]
    chaine = "\n".join(msg_race)
    jeu.info(chaine)
