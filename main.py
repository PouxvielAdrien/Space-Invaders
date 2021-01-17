"""
Cette page contient les fonctions nécessaires pour jouer 
Auteurs : Adrien Pouxviel, Farès Zaghouane
Il a été réalisé le 17/01/2021
To Do : - probleme lors du tir joueur.
        -ajouter plus d'aliens   
        -ajouter alien bonus    
        -mettre des images pour les aliens et le joueur

Lien du git : https://github.com/PouxvielAdrien/Space-Invaders
"""

import tkinter
import spaceInvaderlib

def jeu():
    #fonction qui cree la partie 
    fenetre=tkinter.Tk()
    fenetre.title("Space Invaders")
    fenetre.configure(bg="black")

    longeur=610
    largeur=417

    canvas=tkinter.Canvas(fenetre, width = longeur,height = largeur,bg = "#47484b")
    images=tkinter.PhotoImage(file = "fond.gif" )
    fond=canvas.create_image(0,0,anchor = 'nw' , image=images)


    canvas.grid(column=0, row=1, ipadx=5, pady=5)

    var_score=tkinter.StringVar()

    score=tkinter.Label(fenetre, textvariable=var_score, bg="#d348d0")
    score.grid(column=0, row=0, ipadx=5, pady=5 , sticky="w" )

    var_vie=tkinter.StringVar()

    vie=tkinter.Label(fenetre, textvariable=var_vie, bg="#d348d0")
    vie.grid(column=0, row=0, ipadx=5, pady=5 ,sticky="e")


    btnQuit=tkinter.Button(fenetre,text="quitter",command=fenetre.destroy)
    btnQuit.grid(column=0, row=2, ipadx=5, pady=5, sticky="w")


    partie=spaceInvaderlib.Partie(canvas, fenetre,var_score,var_vie)

    btnNew=tkinter.Button(fenetre,text="nouveau", command= lambda: [fenetre.destroy(),jeu()])
    btnNew.grid(column=0, row=2, ipadx=5, pady=5,sticky="e")


    fenetre.mainloop()

jeu()
