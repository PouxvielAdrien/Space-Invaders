"""
Cette page contient les fonctions nécessaires pour jouer 
Auteurs : Adrien Pouxviel, Farès Zaghouane
Il a été réalisé le 17/01/2021 mise a jour le 24/01/21
To Do : -ajouter plus d'aliens   
        -ajouter alien bonus    
        -mettre des images pour les aliens et le joueur
        - petit proble lorque le joueur et le monstre tir en meme temps, le monstre se supprime tous seul
        - ajouter des niveau
        -enrgistrer le meilleur score

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
    var_score=tkinter.StringVar()
    var_vie=tkinter.StringVar()
    

    canvas=tkinter.Canvas(fenetre, width = longeur,height = largeur,bg = "#47484b")
    images=tkinter.PhotoImage(file = "fond.gif" )
    canvas.create_image(0,0,anchor = 'nw' , image=images)
    canvas.grid(column=0, row=1, ipadx=5, pady=5)

    partie=spaceInvaderlib.Partie(canvas, fenetre,var_score,var_vie)

    score=tkinter.Label(fenetre, textvariable=var_score, bg="#d348d0")
    score.grid(column=0, row=0, ipadx=5, pady=5 , sticky="w" )

    

    vie=tkinter.Label(fenetre, textvariable=var_vie, bg="#d348d0")
    vie.grid(column=0, row=0, ipadx=5, pady=5 ,sticky="e")


    btnQuit=tkinter.Button(fenetre,text="quitter",command=fenetre.destroy)
    btnQuit.grid(column=0, row=2, ipadx=5, pady=5, sticky="w")

    btnPause=tkinter.Button(fenetre,text="Pause" ,command=partie.pause)
    btnPause.grid(column=0, row=2, ipadx=5, pady=5, sticky="n")
    

    btnNew=tkinter.Button(fenetre,text="nouveau", command= lambda: [fenetre.destroy(),jeu()])
    btnNew.grid(column=0, row=2, ipadx=5, pady=5,sticky="e")


    fenetre.mainloop()

jeu()
