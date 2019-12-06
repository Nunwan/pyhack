"""
Module gérant tout ce qui compose un personnage
"""

from niveau import CAR, Porte
from objet import *

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
        self.bag_objet = dict()   # entrée : obj -> nb

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
        self.jeu.pad.addstr(self.position[1], self.position[0], self.jeu.niveaux[self.niveau_en_cours].reminder[(self.position[0], self.position[1])].car)
        self.jeu.refresh()

    def affiche_inventaire(self):
        debut = "Your inventory is : \n ############ \n Consommables \n ############ \n" 
        dico_obj = self.jeu.dico_objet
        inventaire = "\n".join(dico_obj[name] +  ". " + globals()[name].name + "  x " + str(nb) for name, nb in self.bag_objet.items())
        self.jeu.info(debut + inventaire)

    def utilisation(self):
        different = "".join(self.jeu.dico_objet[name] for name in self.bag_objet.keys())
        self.jeu.msg("Que voulez vous utilisez ?  (" + different + ") ou i (inventaire)")
        dico_objet_inv = {v: k for k, v in self.jeu.dico_objet.items()}
        key = self.jeu.pad.getkey()
        if key == "i":
            self.affiche_inventaire()
        elif key in dico_objet_inv:
            name = dico_objet_inv[key]
            if name in self.bag_objet and self.bag_objet[name] > 0:
                globals()[name].action(self.jeu, self)
                if self.bag_objet[name] == 1:
                    del self.bag_objet[name]
                else:
                    self.bag_objet[name] -= 1
        else:
            self.jeu.msg("Cette objet n'est pas dans votre sac")

    def __str__(self):
        return("Vous :  {} PV | {} Mana | {} niveau".format(self.pv, self.mana, self.niveau_en_cours))

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
                    prochain.pick(self)
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
