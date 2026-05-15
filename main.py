#%%%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import os
dirPath = os.path.dirname(os.path.realpath(__file__))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]

def Charge_fichier(nom):
    """Chargement des données d'un fichier et conversion des 
    valeurs en floatant ou entier.

    Parameters
    ----------
    nom [str] : nom du fichier à charger (chemain complet)

    Returns
    -------
    matrice : données du fichier
    """
    matrice = []
    try:
        with open(nom, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                matrice.append(ligne) 
    except FileNotFoundError:
        print(f"Erreur : le fichier {nom} n'a pas été trouvé.")
    except IOError:
        print(f"Erreur : problème d'ouverture du fichier {nom}.")

    return matrice

filename = dirPath + os.sep + "_store" + os.sep + "reponses.csv"

brut = Charge_fichier(filename)

tab = []

for i, ligne in enumerate(brut) : 
    ligne = ligne.replace("\n","")
    if i != 0 :
        ligne = ligne.replace(" h","")
        ligne = ligne.replace("h","")
        ligne = ligne.replace("3 +","4")
        ligne = ligne.replace("7 ou +","7")
    tab.append(ligne.split(","))

X1 = []
X2 = []
X3 = []
for i, ligne in enumerate(tab):
    del ligne[0]
    
    if i!=0:
        for j in range (len(ligne)) : 
            ligne[j] = int(ligne[j])
        
        X1.append(ligne[0])
        X2.append(ligne[1])
        X3.append(ligne[2])