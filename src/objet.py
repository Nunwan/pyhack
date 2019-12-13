"""
Module gérant les objets et leur interaction
"""


class Objet:
    """
    Classe gérant les objets
    """
    def __init__(self, jeu, x, y, salle):
        """
        Construit un objet faisant parti de jeu en position
        (x,y) dans la salle salle.
        Les caracteristique de l'objet sont dans son dico
        """
        self.salle = salle
        self.x = x
        self.y = y
        self.car = "o"
        self.name = "objet"
        self.jeu = jeu
        self.caracteristique = dict()

    def __str__(self):
        return "o"

    def affiche(self, x, y, jeu):
        """
        Affiche la salle autour de l'objet
        """
        self.salle.affiche(self.salle.milieu()[0], self.salle.milieu()[1], 0)

    def pick(self, perso):
        """
        Prend un objet et le met dans l'inventaire de perso.
        L'enlève de l'affichage
        """
        niveau = self.jeu.niveaux[self.jeu.perso.niveau_en_cours]
        niveau.reminder[(self.x, self.y)] = self.salle
        total_obj = len(perso.bag_objet)
        if total_obj > 25:
            self.jeu.msg("Votre inventaire est plein")
        else:
            del self.salle.objets[(self.x, self.y)]
            inv = perso.bag_objet
            nom = self.name
            if nom in inv:
                inv[nom] =  inv[nom] + 1
            else:
                inv[nom] = 1
            if nom not in self.jeu.dico_objet:
                self.jeu.dico_objet[nom] = self
            self.jeu.msg("Vous avez recupéré : " + nom)

    def utilisation(self, perso):
        """
        Utilse l'objet en rajoutant les attributs de celui-ci
        à perso
        """
        for name, value in self.caracteristique.items():
            if name in perso.__dict__ and isinstance(value, type(perso.__dict__[name])):
                perso.__dict__[name] += value  # Obligé d'appeler __dict__ pour changer les attributs de perso


class Consommable(Objet):
    """
    Classe décrivant les consommables du jeu
    """
    def __init__(self, jeu, x, y, salle, name, car, iterable_caracteristique=None):
        Objet.__init__(self, jeu, x, y, salle)
        self.name = name
        self.car = car
        if iterable_caracteristique:
            for nom, value in iterable_caracteristique:
                self.caracteristique[nom] = int(value)
