import tkinter
import random


class Monstres:
    def __init__(self,pcanvas):
        self.vie=1
        self.positionX=0
        self.positionY=0
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.canvas=pcanvas
        self.monst=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="blue")
        self.vitesse=5
 
    def deplacement(self): 
        # rebond droite
        if self.positionX+25+self.vitesse >=self.canvas.winfo_width():
            self.vitesse=-self.vitesse
            self.positionY+=10
            
        # rebond gauche
        if self.positionX+self.vitesse <= 0:
           self.vitesse=-self.vitesse
           self.positionY+=10

        self.positionX+=self.vitesse
        self.canvas.coords(self.monst,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        fenetre.after(75,self.deplacement)
        
class Joueur:
    def __init__(self,pcanvas):
        self.vie=1
        self.positionX=305
        self.positionY=390
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.canvas= pcanvas
        self.joueur=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="red")
        self.move=25
        
        self.vitesse = 5
        self.canvas.bind('<Key>',self.deplacement)
        self.canvas.focus_set()
      
    def deplacement (self,event):
        #Gestion de l'événement Appui sur une touche du clavier
    
        touche = event.keysym
        print(touche)
        

        #déplacement vers la gauche
        if touche == 'Left' :
            if self.positionX - self.move > 0:
                self.positionX-=self.move

        #déplacement vers la droite 
        if touche == 'Right':
             if self.positionX+25 + self.move <= self.canvas.winfo_width():
                self.positionX+=self.move

        #tir
        if touche == 'space':
            self.Laser()

        self.canvas.coords(self.joueur,self.positionX,self.positionY,self.positionX+25,self.positionY+25)

    def Laser(self):
        Long=20
        Larg=5
        xlaser=self.positionX
        ylaser=self.positionY

        self.laser=canvas.create_rectangle(xlaser+Larg+9.5,ylaser-Long,xlaser+9.5,ylaser,fill='green')
        self.Tir(xlaser,ylaser,Long,Larg)
        
    def Tir(self,xlaser,ylaser,Long,Larg):
        if ylaser>0 :
            ylaser-=8
            self.canvas.coords(self.laser,xlaser+Larg+9.5,ylaser-Long,xlaser+9.5,ylaser)
            self.Collision()
            fenetre.after(10,lambda : self.Tir(xlaser,ylaser,Long,Larg))
            
        else:
            self.canvas.delete(self.laser)

    def Collision(self):
        x1monstre=self.canvas.coords(mont)
        print(x1monstre)




        






fenetre=tkinter.Tk()
fenetre.title("Space Invaders")
fenetre.configure(bg="black")

longeur=610
largeur=417

canvas=tkinter.Canvas(fenetre, width = longeur,height = largeur,bg = "#47484b")
images=tkinter.PhotoImage(file = "fond.gif" )
fond=canvas.create_image(0,0,anchor = 'nw' , image=images)
mont=Monstres(canvas)
joueur=Joueur(canvas)

canvas.grid(column=0, row=1, ipadx=5, pady=5)

score=tkinter.Label(fenetre, text="score", bg="#d348d0")
score.grid(column=0, row=0, ipadx=5, pady=5 , sticky="w" )

vie=tkinter.Label(fenetre, text="vie", bg="#d348d0")
vie.grid(column=0, row=0, ipadx=5, pady=5 ,sticky="e")


btnQuit=tkinter.Button(fenetre,text="quitter",command=fenetre.destroy)
btnQuit.grid(column=0, row=2, ipadx=5, pady=5, sticky="w")

btnNew=tkinter.Button(fenetre,text="nouveau")
btnNew.grid(column=0, row=2, ipadx=5, pady=5,sticky="e")
mont.deplacement()

PosMonstre=[mont.positionX,mont.positionY,mont.tailleX,mont.tailleY]

fenetre.mainloop()





