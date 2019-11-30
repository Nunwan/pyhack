"""
Module gérant tout ce qui compose un personnage
"""

from niveau import CAR

class Personnage:
    """
    Classe gérant un personnage
    """
    def __init__(self, jeu):
        self.position = [0, 0]
        self.pv = 100
        self.mana = 100
        self.jeu = jeu
        self.niveau_en_cours = 0

    def affiche_perso(self):
        """
        Genere dico doit avoir été appelé peut etre ajouté une clause
        Méthode affichant le personnage là où il est
        """
        if (self.position[0], self.position[1]) in self.jeu.niveaux[self.niveau_en_cours].reminder:
            self.jeu.niveaux[self.niveau_en_cours].reminder[(self.position[0], self.position[1])].affiche(self.jeu, self.position[0], self.position[1], 0)
        self.jeu.pad.addstr(self.position[1], self.position[0], CAR["PERSO"])
        self.jeu.refresh()

    def reset_perso(self):
        """
        Méthode affichant la case sur laquelle était le personnage avant qu'il bouge
        """
        self.jeu.pad.addstr(self.position[1], self.position[0], self.jeu.niveaux[self.niveau_en_cours].reminder[(self.position[0], self.position[1])].CAR)
        self.jeu.refresh()

    # Fonction de déplacement
    def monte(self):
        """
        Fonction montant le personnage
        """
        self.reset_perso()
        if (self.position[0], self.position[1] - 1) in self.jeu.niveaux[self.niveau_en_cours].reminder:
            self.position[1] -= 1
        self.affiche_perso()

    def descend(self):
        """
        Méthode faisant descendre le perso
        """
        self.reset_perso()
        if (self.position[0], self.position[1] + 1) in self.jeu.niveaux[self.niveau_en_cours].reminder:
            self.position[1] += 1
        self.affiche_perso()

    def gauche(self):
        """
        Methode déplacant le perso à gauche
        """
        self.reset_perso()
        if (self.position[0] - 1, self.position[1]) in self.jeu.niveaux[self.niveau_en_cours].reminder:
            self.position[0] -= 1
        self.affiche_perso()


    def droite(self):
        """
        Méthode déplacant le perso à droite
        """
        self.reset_perso()
        if (self.position[0] + 1, self.position[1]) in self.jeu.niveaux[self.niveau_en_cours].reminder:
            self.position[0] += 1
        self.affiche_perso()
