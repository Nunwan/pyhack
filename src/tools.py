"""
Module contenant des outils pour le code
"""

def get_n_dict(dico, n=0):
    if n < 0:
        n += len(dico)
    for i, key in enumerate(dico):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def total_nb_objet(dico_objet):
    somme = 0
    for value in dico_objet.values():
        if  isinstance(value, int):
            somme += value
        else:
            raise TypeError("Le type devrait être int")
    return somme
