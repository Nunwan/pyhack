#!/usr/bin/env python3

from random import randint

from scipy.spatial import Delaunay

def point_aleatoire(maxi):
    return [randint(0,maxi), randint(0, maxi)]

def vertices_aleatoire(nb):
    L = []
    for _ in range(nb):
        L.append(point_aleatoire(990))
    return L

L = vertices_aleatoire(50)
print(Delaunay(L).simplices)
