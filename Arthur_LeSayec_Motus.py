from colorama import init
init()
from colorama import Fore, Back, Style
import random


premierMot=["A","C","C","R","O","C"]
secondMot= ["A","V","A","L","E","R"]
troisiemeMot= ["B","A","M","B","O","U"]
quatriemeMot= ["B","A","N","C","A","L"]
cinquiemeMot= ["B","I","E","R","E","S"]
siziemeMot= ["C","A","S","T","O","R"]
septiemeMot= ["D","I","L","U","E","R"]
huitiemeMot= ["M","E","D","U","S","E"]
neuviemeMot= ["F","I","L","M","E","R"]
dixiemeMot= ["Z","A","P","P","E","R"]

def trouverLettre (premierMot,mot_joueur):
    for i in range (0,6):
        if (premierMot [i] == mot_joueur [j]):
            print(Back.RED + mot_joueur[j], end = " ")
        else :
            print (Back.BLUE + mot_joueur[j], end = " ")
    return i 
    
    
for i in range (0,9)
    mot_joueur = input ("Veuillez saisir un mot")
    trouverLettre (mot_joueur)
