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

def trouverLettre (tableau_mot,mot_joueur):
    for i in range (0,6):
        if (tableau_mot [i] == mot_joueur [i]):
            print(Back.RED + mot_joueur[i], end = " ")
        else :
            print (Back.BLUE + mot_joueur[i], end = " ")
    return i 
    
    
mot_joueur= input("Veuiller entrer un mot")