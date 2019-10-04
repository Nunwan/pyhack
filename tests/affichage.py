#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

L = np.zeros((5,5))

affichage = dict()
affichage[0] = " "
affichage[1] = "."
affichage[2] = "|"
L[2,1] = 2
L[2,2] = 1
L[2,3] = 1
L[2,4] = 2
for i in range(len(L)):
    for j in range(len(L)):
        print(affichage[L[i][j]], end="")
    print("")

