"""
Module gérant tout ce qui compose un personnage
"""

from niveau import CAR, Porte
from objet import Objet

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
            self.jeu.niveaux[self.niveau_en_cours].reminder[(self.position[0], self.position[1])].affiche(self.position[0], self.position[1], 0)
            #self.jeu.msg(str(self.jeu.niveaux[self.niveau_en_cours].reminder[(self.position[0], self.position[1])]))
        self.jeu.pad.addstr(self.position[1], self.position[0], CAR["PERSO"])
        self.jeu.refresh()

    def reset_perso(self):
        """
        Méthode affichant la case sur laquelle était le personnage avant qu'il bouge
        """
        self.jeu.pad.addstr(self.position[1], self.position[0], self.jeu.niveaux[self.niveau_en_cours].reminder[(self.position[0], self.position[1])].CAR)
        self.jeu.refresh()

    def __str__(self):
        return("Personnage :  {} PV | {} Mana | {} niveau".format(self.pv, self.mana, self.niveau_en_cours))

    # Fonction de déplacement
    def mouvement(self, vers_x, vers_y):
        """
        Fonction gérant le déplacement général
        """
        self.reset_perso()
        if (vers_x, vers_y) in self.jeu.niveaux[self.niveau_en_cours].reminder:
            # Gère la porte bloqué
            reminder = self.jeu.niveaux[self.niveau_en_cours].reminder
            prochain = reminder[(vers_x, vers_y)]
            if isinstance(prochain, Porte) and prochain.lock:
                self.jeu.msg("La porte est bloqué")
            else:  # sinon fais le mouvement
                self.jeu.msg(" ")
                if isinstance(prochain, Objet):
                    prochain.action(self)
                self.position = [vers_x, vers_y]
        self.affiche_perso()

    def monte(self):
        """
        Fonction montant le personnage
        """
        self.mouvement(self.position[0], self.position[1] - 1)

    def descend(self):
        """
        Méthode faisant descendre le perso
        """
        self.mouvement(self.position[0], self.position[1] + 1)

    def gauche(self):
        """
        Methode déplacant le perso à gauche
        """
        self.mouvement(self.position[0] - 1, self.position[1])

    def droite(self):
        """
        Méthode déplacant le perso à droite
        """
        self.mouvement(self.position[0] + 1, self.position[1])
