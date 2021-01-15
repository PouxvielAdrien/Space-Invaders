"""
a faire laser allier ennemis, fin de partie gagner et perdu, score , protection
idee pour laser et collision on garde dans une liste les valeurs de ennemie en fonctions de qui tire et on verrifie
juste si c'est un ennemi
ex collision(listeEnnemie)
    for i in tocuher 
        if i in liste ennemie 
            on supprime
"""

import tkinter
import random

class Partie:
    def __init__(self, canvas):
        self.canvas=canvas
<<<<<<< HEAD
        self.joueur=Joueur(self.canvas)
        self.mur1=Protection(self.canvas,50)
        self.mur2=Protection(self.canvas,280)
        self.mur3=Protection(self.canvas,500)
        self.monstre=[Monstres(self.canvas,10,0),Monstres(self.canvas,50,0)]
        self.listeAmis{2:self.joueur; [3,4,5,6,7,8,9];self.mur1; }
        var_vie.set("vie"+str(self.joueur.vie))
        var_score.set("score: "+ str(self.joueur.score))
        self.TirMonstre()
        self.deplacementMonstre()
    
=======
        self.restart()

    def restart(self):
            print('partie recommencee')
            
            self.canvas.delete("all")
            self.joueur=Joueur(self.canvas)

            self.mur1=Protection(self.canvas,50)
            self.mur2=Protection(self.canvas,280)
            self.mur3=Protection(self.canvas,500)
            self.monstre=[Monstres(self.canvas,10,0),Monstres(self.canvas,50,0)]
            var_vie.set("vie"+str(self.joueur.vie))
            var_score.set("score: "+ str(self.joueur.score))
            self.TirMonstre()
            self.deplacementMonstre()
            
>>>>>>> d9b99acaa01ba352d2957831c3c6db789528a323

    def TirMonstre(self):
        #choix=random.choice(self.monstre)
        choix=self.monstre[0]
        laz=Laserrr(choix.positionX,choix.positionY,self.canvas,"orange",10)
        laz.TirEnnemis([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        self.perdu()
        fenetre.after(1000, self.TirMonstre)    
    """
    def teste(self):

        listeTouche=[]
        for touche in listeTouche:
            if touche in dicoAmis:
                self.joueur.vie-=1
                self.perdu()
            elif touche in dicoEnnemis:
                del(self.dicoEnnemis[touche])
                self.canvas.delete(touche)
                gagner()
                """
    def deplacementMonstre(self):
        
        #rebond droite
        if self.monstre[-1].positionX+25>=self.canvas.winfo_width():
            
            for monster in self.monstre:
                monster.vitesse=-monster.vitesse
                monster.positionY+=10
                monster.deplacement()   
            self.perdu()

        # rebond gauche
        elif self.monstre[0].positionX<=0:
            
            for monster in self.monstre:
                monster.vitesse=-monster.vitesse
                monster.positionY+=10
                monster.deplacement()
            self.perdu()    
        
        else:
            for monster in self.monstre:
                monster.deplacement()

        fenetre.after(75,self.deplacementMonstre)

    def perdu(self):
        if self.monstre[0].positionY>280 or self.joueur.vie==0:
            for monster in self.monstre:
                monster.vitesse=0
            self.canvas.delete(2)
            fin=tkinter.Label(fenetre, text="vous avez perdu", bg="#d348d0")
            fin.grid(column=0, row=1, ipadx=5, pady=5)

    def gagner(self):
        if len(self.monstre)==0:
            fin=tkinter.Label(fenetre, text="vous avez gagner", bg="#d348d0")
            fin.grid(column=0, row=1, ipadx=5, pady=5)

    

class Monstres:
    def __init__(self,pcanvas,px,py):
        self.vie=1
        self.positionX=px
        self.positionY=py
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.canvas=pcanvas
        self.monst=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="blue")
        self.vitesse=(5)

    def deplacement(self):
    
        self.positionX+=self.vitesse
        self.canvas.coords(self.monst,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        

class Protection:
     def __init__(self,canvas,px):
         self.canvas=canvas
         self.mur=[self.canvas.create_rectangle(px,300,px+20,320,fill="white"),self.canvas.create_rectangle(px+25,300,px+45,320,fill="white"),self.canvas.create_rectangle(px+50,300,px+70,320,fill="white"),self.canvas.create_rectangle(px,320,px+20,340,fill="white"),self.canvas.create_rectangle(px+25,320,px+45,340,fill="white"),self.canvas.create_rectangle(px+50,320,px+70,340,fill="white")]           
        
class Joueur:
    def __init__(self,pcanvas):
        self.vie=3
        self.score=0
        
        self.positionX=305
        self.positionY=390
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.canvas= pcanvas
        self.joueur=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="red")
        
        self.move=25
        self.shoot=True
        self.vitesse = 5

        self.canvas.bind('<Key>',self.deplacement)
        self.canvas.focus_set()
      
    def deplacement (self,event):
        #Gestion de l'événement Appui sur une touche du clavier
    
        touche = event.keysym
       
        #déplacement vers la gauche
        if touche == 'Left' :
            if self.positionX - self.move > 0:
                self.positionX-=self.move

        #déplacement vers la droite 
        if touche == 'Right':
             if self.positionX+25 + self.move <= self.canvas.winfo_width():
                self.positionX+=self.move

        #tir
        if touche == 'space' and self.shoot:                      
            laz=Laserrr(self.positionX,self.positionY,self.canvas,"green",-10)
            laz.TirAllier()
            
        self.canvas.coords(self.joueur,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        var_vie.set("vie:"+str(self.vie))
        fenetre.update()

    
        

        
        
class Laserrr:
    def __init__(self,posX,posY, canevas,couleur,vitesse):
        self.Long=20
        self.Larg=5
        self.xlaser=posX
        self.ylaser=posY
        self.canevas=canevas
        self.couleur=couleur
        self.vitesse=vitesse
        self.laser=self.canevas.create_rectangle(self.xlaser+self.Larg+9.5, self.ylaser-self.Long, self.xlaser+9.5, self.ylaser, fill=self.couleur)
        

    def TirAllier(self):
        if self.ylaser>0:
            self.ylaser+=self.vitesse
            self.canevas.coords(self.laser, self.xlaser+self.Larg+9.5, self.ylaser-self.Long, self.xlaser+9.5,self.ylaser )
            self.Collision()
            fenetre.after(10, self.TirAllier)
        else:
           
            self.canevas.delete(self.laser)
            
        
            
    def TirEnnemis(self,plisteEnnemie):
        if self.ylaser<500:
            self.ylaser+=self.vitesse
            self.canevas.coords(self.laser, self.xlaser+self.Larg+9.5, self.ylaser-self.Long, self.xlaser+9.5,self.ylaser )
            self.couler(plisteEnnemie)
            fenetre.after(10, lambda:self.TirEnnemis(plisteEnnemie))
        else:
<<<<<<< HEAD
            
=======
            #print("sup2")
>>>>>>> d9b99acaa01ba352d2957831c3c6db789528a323
            self.canevas.delete(self.laser)
            
    def couler(self,listeEnnemie):
        x1l,y1l,x2l,y2l=self.canevas.coords(self.canevas.find_all()[-1])
        toucher=self.canevas.find_overlapping(x1l,y1l,x2l,y2l)
<<<<<<< HEAD
        
=======
        #print(toucher) 
>>>>>>> d9b99acaa01ba352d2957831c3c6db789528a323
        for obj in toucher:
            if obj in listeEnnemie:
                mort=self.canevas.find_withtag(obj)
                self.canevas.delete(mort)
                self.canevas.delete(self.laser)
<<<<<<< HEAD
               
=======
                #print("toucher: " ,mort)
>>>>>>> d9b99acaa01ba352d2957831c3c6db789528a323

    def Collision(self):
        x1l,y1l,x2l,y2l=self.canevas.coords(self.canevas.find_all()[-1])
        toucher=self.canevas.find_overlapping(x1l,y1l,x2l,y2l)
        #print(toucher)
        for i in toucher[1:-1]:
            mort=self.canevas.find_withtag(i)
            self.canevas.delete(self.laser)
            self.canevas.delete(mort)
<<<<<<< HEAD
            
=======
            #print("toucher: " ,mort)
>>>>>>> d9b99acaa01ba352d2957831c3c6db789528a323
            



    





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


partie=Partie(canvas)
<<<<<<< HEAD


btnNew=tkinter.Button(fenetre,text="nouveau", command=fenetre.destroy)
=======

btnNew=tkinter.Button(fenetre,text="nouveau", command= partie.restart)
>>>>>>> d9b99acaa01ba352d2957831c3c6db789528a323
btnNew.grid(column=0, row=2, ipadx=5, pady=5,sticky="e")


fenetre.mainloop()






