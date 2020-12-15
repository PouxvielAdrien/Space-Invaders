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
            
        # rebond gauche
        if self.positionX+self.vitesse <= 0:
           self.vitesse=-self.vitesse

        self.positionX+=self.vitesse
        self.canvas.coords(self.monst,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        fenetre.after(100,self.deplacement)
        
       
      

fenetre=tkinter.Tk()
fenetre.title("Space Invaders")
fenetre.configure(bg="black")

longeur=610
largeur=417

canvas=tkinter.Canvas(fenetre, width = longeur,height = largeur,bg = "#47484b")
images=tkinter.PhotoImage(file = "fond.gif" )
fond=canvas.create_image(0,0,anchor = 'nw' , image=images)
mont=Monstres(canvas)
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
fenetre.mainloop()


class Monstres:
    def __init__(self,pcanvas):
        self.vie=1
        self.positionX=0
        self.positionY=0
        self.canvas=pcanvas
        self.monst=self.canvas.create_rectangle(self.positionX,self.positionY,self.positionX+25,self.positionY+25, fill="blue")
        self.vitesse=50
 
    def deplacement(self):
        self.positionX+=self.vitesse
        self.canvas.coords(self.monst,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        
        




