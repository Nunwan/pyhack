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
Pyxhook était trop compliqué.
curses est meilleur et permet deux choses : la gestion des events au clavier + une gestion de l'affichage bien plus simple


## Gestion de l'affichage.

Mieux qu'une matrice :

- On crée des salles qui sont décrites par une taille et le point du coin haut gauche
- On définit une méthode qui affiche une salle qqc avec sol + mur grâce à addstr
- On génère alors les salles aléatoires et on les affiche avec la méthode. On peut ainsi plus facilement gérer un affichage pas à pas ( c'est le cas de le dire)

Pour la génération des salles : 
https://github.com/adnzzzzZ/blog/issues/7