import tkinter
import random


        self.fenetre=tkinter.Tk()
        self.fenetre.title("Space Invaders")
        self.fenetre.configure(bg="black")

        self.canvas=tkinter.Canvas(self.fenetre, width = "610",height = "417",bg = "#47484b")
        self.images=tkinter.PhotoImage(file = "fond.gif" )
        self.fond=self.canvas.create_image(0,0,anchor = 'nw' , image=self.images)
        self.mont=Monstres(self.canvas)
        self.canvas.grid(column=0, row=1, ipadx=5, pady=5)

        self.score=tkinter.Label(self.fenetre, text="score", bg="#d348d0")
        self.score.grid(column=0, row=0, ipadx=5, pady=5 , sticky="w" )

        self.vie=tkinter.Label(self.fenetre, text="vie", bg="#d348d0")
        self.vie.grid(column=0, row=0, ipadx=5, pady=5 ,sticky="e")


        self.btnQuit=tkinter.Button(self.fenetre,text="quitter",command=self.fenetre.destroy)
        self.btnQuit.grid(column=0, row=2, ipadx=5, pady=5, sticky="w")

        self.btnNew=tkinter.Button(self.fenetre,text="nouveau")
        self.btnNew.grid(column=0, row=2, ipadx=5, pady=5,sticky="e")
        self.mont.deplacement()
        

    

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
        
        


jeux= Jeux()
jeux.Jouer()

