#Todo List pour pyhack.

- Un système d'affichage de la carte qui de base met tout en étoile puis rajoute les salles et couloirs
- Un système de construction de salle aléatoire cohérentes avec la taille de l'écran
- Puis les couloirs reliant les salles à une entrée aléatoire
- Le système qui lit l'entrée clavier
- Un système de mouvement et donc de MAJ de la carte. ATTENTION aux murs qui doivent être imperméables
- Réfléchir à comment stocker la carte et la position du joueur.
- Réflechir à n'afficher qu'une partie de la map dès le début dans le but de continuer le projet ensuite


## Gestion du clavier et de l'interaction.

Pynput ne marchait pas.
pyxhook a l'air de fonctionner (voir sur branche dev).
On va essayer curses qui est sensé nous faciliter la vie pour beaucoup de choses

## Gestion de l'affichage.

Le plus simple semble être une matrice de la taile du jeu.
On peut :

- associer un nombre à un état dans la matrice 0 pas découvert, 1 sol, 2 mur, 3 porte, 4 couloir et *-1* le personnage.
- On crée un dictionnaire qui a chaque nombre associe sa chaine préféré : " ", ".", "|" ou "-" (à gérer), "#", "@"
- On affiche en parcourant le dico d'indice la matrice
