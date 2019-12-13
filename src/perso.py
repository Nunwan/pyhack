"""
Module gérant tout ce qui compose un personnage
"""

from niveau import CAR, Porte
from objet import *
from tools import get_n_dict

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
        """
        Affiche l'inventaire aka :
        identifiant. Nom objet x nb_objet
        """
        debut = "Your inventory is : \n ############ \n Consommables \n ############ \n"
        dico_obj = self.jeu.dico_objet
        inventaire = "\n".join(chr(97 + ind) +  ". " + dico_obj[nom].name + "  x " + str(nb) for ind, (nom, nb) in enumerate(self.bag_objet.items()))
        self.jeu.info(debut + inventaire)

    def utilisation(self):
        """
        Demande quel objet veut être utiliser et l'utilise.
        Il faut préciser l'identifiant de l'objet dans le sac.
        """
        n = len(self.bag_objet)
        liste_ind = [chr(97+i) for i in range(n)]
        if n > 7:
            liste_ind = [chr(97+i) for i in range(7)] + [chr(97+i+1) for i in range(7, n)]
        self.jeu.msg("Que voulez vous utilisez ?  (" + "".join(liste_ind) + ") ou i (inventaire)")
        key = self.jeu.pad.getkey()
        if key == "i":
            self.affiche_inventaire()
        elif key in liste_ind:
            cle_obj = get_n_dict(self.bag_objet, ord(key) - 97)
            if ord(key) - 97 > 7:
                cle_obj = get_n_dict(self.bag_objet, ord(key) - 97 - 1)
            nb_objet = self.bag_objet[cle_obj]
            if nb_objet > 0:
                self.jeu.dico_objet[cle_obj].utilisation(self)
                if nb_objet == 1:
                    del self.bag_objet[cle_obj]
                    del self.jeu.dico_objet[cle_obj]
                else:
                    self.bag_objet[cle_obj] -= 1
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
