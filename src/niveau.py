#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gérant la génération et les opérations sur les
niveaux du jeu
"""

from random import randint

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
        self.CAR = "."

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
        """
        reminder = jeu.niveaux[jeu.niveau_en_cours].reminder
        if passe < 2:
            self.affiche_sol(jeu)
            self.affiche_murh(jeu)
            self.affiche_murv(jeu)
            jeu.refresh()
            if (x + 1, y) in reminder:
                reminder[(x + 1, y)].affiche(jeu, x + 1, y, passe + 1)
            if (x - 1, y) in reminder:
                reminder[(x - 1, y)].affiche(jeu, x - 1, y, passe + 1)
            if (x, y + 1) in reminder:
                reminder[(x, y + 1)].affiche(jeu, x, y + 1, passe + 1)
            if (x, y - 1) in reminder:
                reminder[(x, y - 1)].affiche(jeu, x, y - 1, passe + 1)
        for porte in self.portes:
            porte.affiche(jeu, porte.x, porte.y, passe + 1)
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
        for porte in self.portes:
            dico[(porte.x, porte.y)] = porte

def milieu_deux(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x1 + x2) // 2, (y1 + y2)//2


def plus_haute_basse(salle1, salle2):
    if salle1.milieu()[1] <= salle2.milieu()[1]:
        return salle1, salle2
    else:
        return salle2, salle1


def plus_gauche_droite(salle1, salle2):
    if salle1.milieu()[0] <= salle2.milieu()[0]:
        return salle1, salle2
    else:
        return salle2, salle1


class Couloir:
    """
    Classe représentant les couloirs
    """
    def __init__(self, salle1, salle2):
        self.salle1 = salle1
        self.salle2 = salle2
        self.CAR = "#"

    # Méthode d'affichage surement nul, à faire
    def affiche(self, jeu, x, y, passe):
        jeu.pad.addstr(y, x, CAR["COULOIR"])
        reminder = jeu.niveaux[jeu.niveau_en_cours].reminder
        if passe < 2:
            if (x + 1, y) in reminder:
                reminder[(x + 1, y)].affiche(jeu, x + 1, y, passe + 1)
            if (x - 1, y) in reminder:
                reminder[(x - 1, y)].affiche(jeu, x - 1, y, passe + 1)
            if (x, y + 1) in reminder:
                reminder[(x, y + 1)].affiche(jeu, x, y + 1, passe + 1)
            if (x, y - 1) in reminder:
                reminder[(x, y - 1)].affiche(jeu, x, y - 1, passe + 1)
        jeu.refresh()

    def genere_dico(self, dico):
        if len(dico) == 0:
            self.salle1.genere_dico(dico)
            self.salle2.genere_dico(dico)
        mid_x, mid_y = milieu_deux(self.salle1.milieu(), self.salle2.milieu())
        haute, basse = plus_haute_basse(self.salle1, self.salle2)
        gauche, droite = plus_gauche_droite(self.salle1, self.salle2)
        if self.salle1.coin_hgauche[0] < mid_x < self.salle1.coin_bdroite[0] and self.salle2.coin_hgauche[0] < mid_x < self.salle2.coin_bdroite[0]:
            porte1 = Porte(mid_x, haute.coin_bdroite[1] + 1)
            porte2 = Porte(mid_x, basse.coin_hgauche[1] - 1)
            dico[(mid_x, haute.coin_bdroite[1] + 1)] = porte1
            dico[(mid_x, haute.coin_bdroite[1] + 1)] = porte2
            haute.portes.append(porte1)
            basse.portes.append(porte2)
            for y in range(haute.coin_bdroite[1] + 2, basse.coin_hgauche[1] - 1):
                if (mid_x, y) not in dico and (mid_x, y+1) in dico and isinstance(dico[(mid_x, y+1)], Salle):
                    porte = Porte(mid_x, y)
                    dico[(mid_x, y)] = porte
                    dico[(mid_x, y+1)].portes.append(porte)
                if (mid_x, y) not in dico:
                    dico[(mid_x, y)] = self
                else:
                    if isinstance(dico[(mid_x, y)], Salle) and  (mid_x, y+1) not in dico:
                        porte = Porte(mid_x, y + 1)
                        dico[(mid_x, y+1)] = porte
                        dico[(mid_x, y)].portes.append(porte)
        if self.salle1.coin_hgauche[1] < mid_y < self.salle1.coin_bdroite[1] and self.salle2.coin_hgauche[1] < mid_y < self.salle2.coin_bdroite[1]:
            porte1 = Porte(gauche.coin_bdroite[0] + 1, mid_y)
            porte2 = Porte(droite.coin_hgauche[0] - 1, mid_y)
            dico[(gauche.coin_bdroite[0] + 1, mid_y)] = porte1
            dico[(droite.coin_hgauche[0] - 1, mid_y)] = porte2
            gauche.portes.append(porte1)
            droite.portes.append(porte2)
            for x in range(gauche.coin_bdroite[0] + 2, droite.coin_hgauche[0] - 1):
                if (x, mid_y) not in dico and (x, mid_y+1) in dico and isinstance(dico[(x, mid_y+1)], Salle):
                    porte = Porte(x, mid_y)
                    dico[(x, mid_y)] = porte
                    dico[(x, mid_y+1)].portes.append(porte)
                if (x, mid_y) not in dico:
                    dico[(x, mid_y)] = self
                else:
                    if isinstance(dico[(x, mid_y)], Salle) and  (x+1, mid_y) not in dico:
                        porte = Porte(x+1, mid_y )
                        dico[(x+1, mid_y)] = porte
                        dico[(x, mid_y)].portes.append(porte)
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
            for x in range(gauche.coin_bdroite[0] + 2, droite.milieu()[0] + 1):
                if (x, gauche.milieu()[1]) not in dico and (x+1, gauche.milieu()[1]) in dico and isinstance(dico[(x+1, gauche.milieu()[1])], Salle):
                    porte = Porte(x, gauche.milieu()[1])
                    dico[(x, gauche.milieu()[1])] = porte
                    dico[(x+1, gauche.milieu()[1])].portes.append(porte)
                if (x, gauche.milieu()[1]) not in dico:
                    dico[(x, gauche.milieu()[1])] = self
                else:
                    if isinstance(dico[(x, gauche.milieu()[1])], Salle) and (x + 1 , gauche.milieu()[1]) not in dico:
                        porte = Porte(x+1, gauche.milieu()[1])
                        dico[(x+1, gauche.milieu()[1])] = porte
                        dico[(x, gauche.milieu()[1])].portes.append(porte)
            if gauche is basse:
                for y in range(droite.coin_bdroite[1] + 2, gauche.milieu()[1] + 1):
                    if (droite.milieu()[0], y) not in dico and (droite.milieu()[0], y+1) in dico and isinstance(dico[(droite.milieu()[0], y+1)], Salle):
                        porte = Porte(droite.milieu()[0], y)
                        dico[(droite.milieu()[0], y)] = porte
                        dico[(droite.milieu()[0], y+1)].portes.append(porte)
                    if (droite.milieu()[0], y) not in dico:
                        dico[(droite.milieu()[0], y)] = self
                    else:
                        if isinstance(dico[(droite.milieu()[0], y)], Salle) and (droite.milieu()[0], y+1) not in dico:
                            porte = Porte(droite.milieu()[0], y+1)
                            dico[(droite.milieu()[0], y+1)] = porte
                            dico[(droite.milieu()[0], y)].portes.append(porte)
            else:
                for y in range(gauche.milieu()[1], droite.coin_bdroite[1] - 1):
                    if (droite.milieu()[0], y) not in dico and (droite.milieu()[0], y+1) in dico and isinstance(dico[(droite.milieu()[0], y+1)], Salle):
                        porte = Porte(droite.milieu()[0], y)
                        dico[(droite.milieu()[0], y)] = porte
                        dico[(droite.milieu()[0], y+1)].portes.append(porte)
                    if (droite.milieu()[0], y) not in dico:
                        dico[(droite.milieu()[0], y)] = self
                    else:
                        if isinstance(dico[(droite.milieu()[0], y)], Salle) and (droite.milieu()[0], y+1) not in dico:
                            porte = Porte(droite.milieu()[0], y+1)
                            dico[(droite.milieu()[0], y+1)] = porte
                            dico[(droite.milieu()[0], y)].portes.append(porte)


class Porte:
    """
    Classe représentant une porte
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.CAR = "/"

    def affiche(self, jeu, x, y, passe):
        jeu.pad.addstr(self.y, self.x, CAR["PORTE"])
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
        for salle in self.salles:
            salle.affiche(jeu)


