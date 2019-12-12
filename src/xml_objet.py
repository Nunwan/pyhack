#!/usr/bin/env python3
"""
Module gérant les liaisons entre XML et le jeu
"""

import xml.etree.ElementTree as ET


class XML_File:
    """
    Classe gérant toutes mes opérations utiles
    pour parse un fichier xml
    """
    def __init__(self, path):
        """
        Constructeur prend le chemin et stock la racine
        """
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()

    def recherche_objet(self, type_objet, name):
        """
        Renvoie l'élément dont le tag est type_objet et le nom est name
        """
        return next(element for element in self.root.iter(type_objet) if element.attrib['name'] == name)

    def iter_attribut(self, type_objet, name):
        """
        Renvoie un itérateur sur les enfants de l'élément cherché
        """
        objet = self.recherche_objet(type_objet, name)
        for child in objet:
            yield child.tag, child.text



if __name__ == "__main__":
    file = XML_File('../data/objet.xml')
    for a,b in file.iter_attribut('potion', "Potion de soin"):
        print(a,b)
