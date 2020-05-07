# Avalam ECAM
Réalisé par Victor Janssens (18322) et Sarah Liettefti Lens (18253) pour le projet d'informatique de Bac 2 de l'ECAM.
Mai 2020
Voir règles du projet : https://github.com/ECAM-Brussels/AIGameRunner/blob/master/avalam.md
## Bibliothèque utilisé
- json : pour envoyer l'inscription
- socket : pour communiquer avec le server
- sys : pour utiliser le terminal
- cherypy, cherrypy.lib.static
- random : pour choisir un coup dans une liste


## Lancement de l'ia contre une autre ia:

### Inscription au server et démarrage du jeu


#### Fonctionnement : 
Le fichier simple.py permet l'inscription, il envoie un message TCP en JSON au porte 3001 sous cette forme :

```json
{
	"matricules": ["18253", "18322"],
	"port": port ,
	"name": "Sartor"
}
```
Utiliser la commande:
```
python simple.py port
```
Où `port` doit être remplacé par le numéro de port utilisé par l'ia, sinon il prendra le port 8001 par défaut. 

### Démarrer le jeu

Pour lancer l'ia assurez-vous que le fichier `jeu1.py` est bien téléchargé et se trouve dans le même dossier. 
Écrivez dans un terminal la commande:
```
python Sartor.py port
```
Remplacez `port` par le numéro de port utilisé par l'ia, sinon il prendra le port 8001 par défaut. 

## Explication jeu.1

Via la route `casejouables`, l'ia va d'abord créer une liste `casesoccupes` de toutes les cases de l'état du jeu sur lesquels il est possible de se déplacé (c'est à dire les cases occupées par au moins un pion et au plus 4 pions, puisque lorsqu'une tour a 5 pions elle est dite figée). Chaque case du jeu est identifiée par une liste avec en premier son numéro de ligne et en deuxième son numéro de colonne ([ligne,colonne])

La route `coup` va regarder pour chaque case dans `casesoccupes` si un déplacement est possible (si des cases voisines se trouvent aussi dans la liste `casesoccupes` et si la sommes de leurs pions n'est pas supérieur à 5). Si c'est le cas, la case d'origine, appelé `de` et la case de destination, appelé `to`, sont envoyé vers la fonction `findallcoup` qui va trier les déplacements qu'elle reçoit dans des listes en fonction de leur objectif.

### Listes de stratégie: 
Classé de la moins avantageuse à la plus avantageuse :

| Listes | Objectif | Commentaire |
|----------|:-------------:|------:|
| `coups` | liste de tous les déplacements possibles | elle est utilisée si toutes les autres listes sont vide, elle permet de ne pas renvoyer un déplacement libre si il ne trouve pas de bon coup |
| `ajout` | empile deux tours de notre couleurs | stratégiquement ce n'est pas un coup prioritaire car si une tour adverse peut nous attaquer au coup suivant, c'est qu'on peut également l'attaquer et dans ce cas le coup sera joué par `ecrase` |
| `embete` | déplace une tour de l'adversaire sur ses couleurs | réduit son nombre de tour |
| `complettheybythey` | déplace une tour de l'adversaire sur ses couleurs et créer une tour de 5 | les pions ne sont donc plus jouables et ne valent que pour un point |
| `ecrase` | déplace une de nos tours sur l'adversaire|remplacé par dans l'ordre: `ecrase4`, `ecrase3` et `ecrase2`|
| `ecrase4`, `ecrase3` et `ecrase2` | dérivé de la liste `ecrase`, le chiffre correspond à la hauteur de la tour final créé sur la tour adverse| il est plus avantageux de d'abord créer plein de petites tours de 2 avant des tours de 4 |
| `complettheybyus` | déplace une de nos tours sur l'adversaire et créons une tour de 5 | nous sécurise un point |
| `ensembleseul` | liste de déplacements dont le pion d'origine nous appartient et le pion destination non dont les deux n'ont pas d'autres choix de déplacement | nous sécurise un point | 


Une fois toutes les cases parcourues, ces listes sont renvoyées  vers `Choosestrat` qui renvoie la liste la plus avantageuse non vide dans laquelle un déplacement sera choisi aléatoirement, mis en forme de dictionnaire comme ci-dessous avant d'être renvoyé sous forme de json par le server `Sarator` : 

```json
{
	"move": {
		"from": [0, 3],
		"to": [1, 4]
}
```

## Jouer avec random:
Vous pouvez jouer en aléatoire grâce au server `randomplayer.py`. 