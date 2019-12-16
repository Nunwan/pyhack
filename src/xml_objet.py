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

    def recherche_objet(self, name):
        """
        Renvoie l'élément dont le tag est type_objet et le nom est name
        """
        return next(element for element in self.root if element.attrib['name'] == name)

    def def_objet(self, name):
        """
        Renvoie les attributs direct de l'objet ici le dict avec nom et car
        """
        return self.recherche_objet(name).attrib


    def iter_attribut(self, name):
        """
        Renvoie un itérateur sur les enfants de l'élément cherché
        """
        objet = self.recherche_objet(name)
        for child in objet:
            yield child.tag, child.text

    def __iter__(self):
        return self.root


def iter_attribut_element(element):
    """
    Itère sur les attributs d'un élément XML donné
    """
    for child in element:
        yield child.tag, child.text

def def_element(element):
    """
    Retourne la définition de notre élément
    """
    return element.attrib


