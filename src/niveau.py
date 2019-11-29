#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gérant la génération et les opérations sur les
niveaux du jeu
"""

from random import randint, random

# Dictionnaire de l'affichage
CAR = dict()
CAR[0] = " "
CAR["SOL"] = "."
CAR["MURV"] = "|"
CAR["MURH"] = "-"
CAR["PERSO"] = "@"
CAR["COULOIR"] = "#"
CAR["PORTE"] = "/"

MAX_TAILLE = 25
MIN_TAILLE = 4

CHAMP_DE_VISION = 2

class Salle:
    """
    Classe représentant une salle du jeu
    """
    def __init__(self, coin_hgauche, coin_bdroite):
        """
        Constructeur créant une salle à partir des deux points extrêmes
        """
        # self.deja = 0   Peut-être inutile
        self.coin_bdroite = coin_bdroite
        self.coin_hgauche = coin_hgauche
        self.portes = []  # Les portes sont de bases vides.
        self.CAR = "."  # caractère du sol d'une salle

    def affiche_sol(self, jeu):
        """
        Méthode affichant le sol de la salle
        """
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0] +1):
            for y in range(self.coin_hgauche[1], self.coin_bdroite[1] +1):
                jeu.pad.addstr(y, x, CAR["SOL"])

    def affiche_murv(self, jeu):
        """
        Méthode affichant les murs verticaux de la salle
        """
        for y in range(self.coin_hgauche[1], self.coin_bdroite[1]+1):
            jeu.pad.addstr(y, self.coin_hgauche[0] - 1, CAR["MURV"])
            jeu.pad.addstr(y, self.coin_bdroite[0] + 1, CAR["MURV"])

    def affiche_murh(self, jeu):
        """
        Méthode affichant les murs verticaux de la salle
        """
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0]+1):
            jeu.pad.addstr(self.coin_hgauche[1] - 1, x, CAR["MURH"])
            jeu.pad.addstr(self.coin_bdroite[1] + 1, x, CAR["MURH"])

    def affiche(self, jeu, x, y, passe):
        """
        Méthode regroupant les méthodes précédentes et affichant toute la salle
        avec une champ de vision de 2 cases adjacentes.
        """
        reminder = jeu.niveaux[jeu.niveau_en_cours].reminder
        if passe < CHAMP_DE_VISION:
            self.affiche_sol(jeu)
            self.affiche_murh(jeu)
            self.affiche_murv(jeu)
            jeu.refresh()
            #if (x + 1, y) in reminder:
            #    reminder[(x + 1, y)].affiche(jeu, x + 1, y, passe + 1)
            #if (x - 1, y) in reminder:
            #    reminder[(x - 1, y)].affiche(jeu, x - 1, y, passe + 1)
            #if (x, y + 1) in reminder:
            #    reminder[(x, y + 1)].affiche(jeu, x, y + 1, passe + 1)
            #if (x, y - 1) in reminder:
            #    reminder[(x, y - 1)].affiche(jeu, x, y - 1, passe + 1)
            for porte in self.portes:
                porte.affiche(jeu, porte.x, porte.y, CHAMP_DE_VISION)
            jeu.refresh()

    def milieu(self):
        """
        Renvoie le milieu de la salle
        """
        x_milieu = (self.coin_bdroite[0] + self.coin_hgauche[0])//2
        y_milieu = (self.coin_bdroite[1] + self.coin_hgauche[1])//2
        return (x_milieu, y_milieu)

    def genere_dico(self, dico):
        """
        Génère le dico appelé par la méthode Niveau.genere_dico.
        Met la salle en tous les points la composant.
        """
        for x in range(self.coin_hgauche[0], self.coin_bdroite[0] + 1):
            for y in range(self.coin_hgauche[1], self.coin_bdroite[1] + 1):
                dico[(x, y)] = self

    def place_porte(self, dico):
        """
        Fonction additionelle mettant dans le dico de rappel
        toutes les portes de toutes les salles.
        """
        for porte in self.portes:
            dico[(porte.x, porte.y)] = porte

def plus_haute_basse(salle1, salle2):
    """
    Renvoie la ssalle la plus haute et la plus basse
    """
    if salle1.milieu()[1] <= salle2.milieu()[1]:
        return salle1, salle2
    else:
        return salle2, salle1


def plus_gauche_droite(salle1, salle2):
    """
    Renvoie la salle la plus à gauche puis la plus à droite
    """
    if salle1.milieu()[0] <= salle2.milieu()[0]:
        return salle1, salle2
    else:
        return salle2, salle1


class Couloir:
    """
    Classe représentant les couloirs
    """
    def __init__(self, salle1, salle2):
        """
        La classe a comme attributs principaux : les salles qu'elle joint
        """
        self.salle1 = salle1
        self.salle2 = salle2
        self.CAR = "#"

    def affiche(self, jeu, x, y, passe):
        """
        Prend le jeu en argument et affiche dans le jeu le couloir
        en x,y et regarde ce qu'il y a autour dans un champ de vision de
        2
        """
        jeu.pad.addstr(y, x, CAR["COULOIR"])
        reminder = jeu.niveaux[jeu.niveau_en_cours].reminder
        if passe < CHAMP_DE_VISION:
            if (x + 1, y) in reminder:
                reminder[(x + 1, y)].affiche(jeu, x + 1, y, passe + 1)
            if (x - 1, y) in reminder:
                reminder[(x - 1, y)].affiche(jeu, x - 1, y, passe + 1)
            if (x, y + 1) in reminder:
                reminder[(x, y + 1)].affiche(jeu, x, y + 1, passe + 1)
            if (x, y - 1) in reminder:
                reminder[(x, y - 1)].affiche(jeu, x, y - 1, passe + 1)
        jeu.refresh()


    def genere_ligne_droite(self, dico, horizontal, coordonee_fixe, debut, fin, direct = False):
        """
        Méthode générant une ligne droite dans le sens de horizontal (ou l'autre) entre
        les points (debut, coordonee_fixe) et (fin-1, coordonee_fixe) (ou inverse si vertical)
        Est utilisé dans genere_dico (utile seulement pour alleger la fonction
        """
        if horizontal:  # Si on fait un chemin horizontal
            for x in range(debut, fin):

                est_salle_1 = (x, coordonee_fixe - 1) in dico and isinstance(dico[(x, coordonee_fixe - 1)], Salle)
                est_salle_2 = (x, coordonee_fixe + 1) in dico and isinstance(dico[(x, coordonee_fixe + 1)], Salle)
                if (x, coordonee_fixe) not in dico and (x+1, coordonee_fixe) in dico and isinstance(dico[(x+1, coordonee_fixe)], Salle):  # Vérifie s'il faut mettre une porte en entrant dans une salle
                    porte = Porte(x, coordonee_fixe)
                    dico[(x, coordonee_fixe)] = porte
                    dico[(x+1, coordonee_fixe)].portes.append(porte)
                # A CHANGER !!!
                elif (x, coordonee_fixe) not in dico and (est_salle_1 or est_salle_2):
                    break
                elif (x, coordonee_fixe) not in dico:
                    dico[(x, coordonee_fixe)] = self  # Crée le couloir s'il n'est pas créé
                else:  # Gère la porte à créer si on est dans une salle et qu'on y sort
                    if isinstance(dico[(x, coordonee_fixe)], Salle) and  (x+1, coordonee_fixe) not in dico:
                        porte = Porte(x+1, coordonee_fixe)
                        dico[(x+1, coordonee_fixe)] = porte
                        dico[(x, coordonee_fixe)].portes.append(porte)
        else:  # Si on fait un chemin vertical, pour comprendre les if /else voir ci dessus
            for y in range(debut, fin):

                est_salle_1 = (coordonee_fixe - 1, y) in dico and isinstance(dico[(coordonee_fixe - 1, y)], Salle)
                est_salle_2 = (coordonee_fixe + 1, y) in dico and isinstance(dico[(coordonee_fixe + 1, y)], Salle)
                if (coordonee_fixe, y) not in dico and (coordonee_fixe, y+1) in dico and isinstance(dico[(coordonee_fixe, y+1)], Salle):
                    porte = Porte(coordonee_fixe, y)
                    dico[(coordonee_fixe, y)] = porte
                    dico[(coordonee_fixe, y+1)].portes.append(porte)
                elif (coordonee_fixe, y) not in dico and (est_salle_1 or est_salle_2):
                    break
                elif (coordonee_fixe, y) not in dico:
                    dico[(coordonee_fixe, y)] = self
                else:
                    if isinstance(dico[(coordonee_fixe, y)], Salle) and  (coordonee_fixe, y+1) not in dico:
                        porte = Porte(coordonee_fixe, y+1)
                        dico[(coordonee_fixe, y+1)] = porte
                        dico[(coordonee_fixe, y)].portes.append(porte)

    def genere_dico(self, dico):
        """
        Genere le dico pour un couloir :
        Il génere le couloir + toutes les portes utiles au parcours du couloir.
        """
        if len(dico) == 0:
            self.salle1.genere_dico(dico)
            self.salle2.genere_dico(dico)
        haute, basse = plus_haute_basse(self.salle1, self.salle2)  # Donne la plus haute/basse salle
        gauche, droite = plus_gauche_droite(self.salle1, self.salle2)  # Donne la plus à gauche, droite salle
        if self.salle1.coin_hgauche[1] < self.salle2.milieu()[1] < self.salle1.coin_bdroite[1]:
            porte1 = Porte(gauche.coin_bdroite[0] + 1, gauche.milieu()[1])
            porte2 = Porte(droite.coin_hgauche[0] - 1, gauche.milieu()[1])
            dico[(gauche.coin_bdroite[0] + 1, gauche.milieu()[1])] = porte1
            dico[(droite.coin_hgauche[0] - 1, gauche.milieu()[1])] = porte2
            gauche.portes.append(porte1)
            droite.portes.append(porte2)
            self.genere_ligne_droite(dico, True, gauche.milieu()[1], gauche.coin_bdroite[0] + 2, droite.coin_hgauche[0] - 1)
        elif self.salle1.coin_hgauche[0] < self.salle2.milieu()[0] < self.salle1.coin_bdroite[0]:
            porte1 = Porte(basse.milieu()[0], basse.coin_hgauche[1] - 1)
            porte2 = Porte(basse.milieu()[0], haute.coin_bdroite[1] + 1)
            dico[(basse.milieu()[0], basse.coin_hgauche[1] - 1)] = porte1
            dico[(basse.milieu()[0], haute.coin_bdroite[1] + 1)] = porte2
            basse.portes.append(porte1)
            haute.portes.append(porte2)
            self.genere_ligne_droite(dico, False, basse.milieu()[0], haute.coin_bdroite[1] + 2, basse.coin_hgauche[1] - 1)
        else:
            porte1 = Porte(gauche.coin_bdroite[0] + 1, gauche.milieu()[1])
            if gauche is basse:
                porte2 = Porte(droite.milieu()[0], droite.coin_bdroite[1] + 1)
            else:
                porte2 = Porte(droite.milieu()[0], droite.coin_hgauche[1] - 1)

            dico[(gauche.coin_bdroite[0] + 1, gauche.milieu()[1])] = porte1
            dico[(droite.milieu()[0], droite.coin_bdroite[1] + 1)] = porte2
            gauche.portes.append(porte1)
            droite.portes.append(porte2)
            self.genere_ligne_droite(dico, True, gauche.milieu()[1], gauche.coin_bdroite[0] + 2, droite.milieu()[0] + 1)
            if gauche is basse:
                self.genere_ligne_droite(dico, False, droite.milieu()[0], droite.coin_bdroite[1] + 2, gauche.milieu()[1] + 1)
            else:
                self.genere_ligne_droite(dico, False, droite.milieu()[0], gauche.milieu()[1], droite.coin_hgauche[1] - 1)

class Porte:
    """
    Classe représentant une porte
    """
    def __init__(self, x, y, lock = False):
        """
        Les attributs sont les coordonées de la porte et son caractère d'affichage
        """
        self.x = x
        self.y = y
        self.CAR = "/"
        self.lock = lock
        if not lock:
            if random() <= 0.2:
                self.lock = True

    def affiche(self, jeu, x, y, passe):
        """
        Méthode affichant la porte
        """
        jeu.pad.addstr(self.y, self.x, CAR["PORTE"])
        if not self.lock:
            reminder = jeu.niveaux[jeu.niveau_en_cours].reminder
            if passe < CHAMP_DE_VISION:
                if (x + 1, y) in reminder:
                    reminder[(x + 1, y)].affiche(jeu, x + 1, y, passe + 1)
                if (x - 1, y) in reminder:
                    reminder[(x - 1, y)].affiche(jeu, x - 1, y, passe + 1)
                if (x, y + 1) in reminder:
                    reminder[(x, y + 1)].affiche(jeu, x, y + 1, passe + 1)
                if (x, y - 1) in reminder:
                    reminder[(x, y - 1)].affiche(jeu, x, y - 1, passe + 1)
        else:
            pass
        jeu.refresh()




class Niveau:
    """
    Classe représentant un niveau du jeu
    """
    #import generate
    def __init__(self):
        """
        Le constructeur construit un niveau vide de salles et de couloir
        """
        self.couloirs = dict()
        self.salles = dict()
        self.genere_dico()

    def genere_dico(self):
        """
        Genere un dico tel que dico[(i,j)] = l'objet voulu : salle couloir etc ... en le point i,j
        """
        self.reminder = dict()
        for salle in self.salles.values():
            salle.genere_dico(self.reminder)
        file = open("log.txt", 'w')
        for c in self.couloirs.values():
            c.genere_dico(self.reminder)
            file.write("{}, {} -> {}, {} \n".format(*c.salle1.milieu(), *c.salle2.milieu()))
        file.write(str(self.reminder))
        file.close()

    def place_all_porte(self):
        """
        S'assure que toutes les portes sont placées. Doit reboucler sur les salles...
        Le dico doit avoir été générer
        """
        for salle in self.salles.values():
            salle.place_porte(self.reminder)


    def affiche(self, jeu):
        """
        Affiche un niveau.
        Obsolete
        """
        for salle in self.salles:
            salle.affiche(jeu)
