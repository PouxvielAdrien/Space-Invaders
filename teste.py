import tkinter
import random

class Partie:
    def __init__(self, canvas):
        self.canvas=canvas
        self.joueur=Joueur(self.canvas)
        self.monstre=[Monstres(self.canvas,0,0),Monstres(self.canvas,50,0)]
        
        
    def initialisation(self):
        for monster in self.monstre:
            if monster.deplacement()==False:
                monster.vitesse=-monster.vitesse


                
        


        
class Monstres:
    def __init__(self,pcanvas,px,py):
        self.vie=1
        self.positionX=px
        self.positionY=py
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.canvas=pcanvas
        self.monst=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="blue")
        self.vitesse=10
        
 
    def deplacement(self): 
        valren=True
        # rebond droite
        if self.positionX+25+self.vitesse >=self.canvas.winfo_width():
            self.vitesse=-self.vitesse
            self.positionY+=10
            valren=False
            
        # rebond gauche
        if self.positionX+self.vitesse <= 0:
           self.vitesse=-self.vitesse
           self.positionY+=10
           valren=False
        return valren
        self.positionX+=self.vitesse
        self.canvas.coords(self.monst,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        self.gagner()
        fenetre.after(75,self.deplacement)
        
    def gagner(self):
        if self.positionY+self.tailleY>300:
            self.vitesse=0
            print('vous avez perdu')
            
        
class Joueur:
    def __init__(self,pcanvas):
        self.vie=5
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
            Laserrr(self.positionX,self.positionY,self.canvas)
            
            #self.Laser()
            

        self.canvas.coords(self.joueur,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        var_vie.set("vie:"+str(self.vie))
        fenetre.update()

    def Laser(self):
        self.shoot=False
        Long=20
        Larg=5
        xlaser=self.positionX
        ylaser=self.positionY

        self.laser=self.canvas.create_rectangle(xlaser+Larg+9.5,ylaser-Long,xlaser+9.5,ylaser, fill='green')
        self.Tir(xlaser,ylaser,Long,Larg)
        
    def Tir(self,xlaser,ylaser,Long,Larg):
        if ylaser>0 :
            ylaser-=8
            self.canvas.coords(self.laser,xlaser+Larg+9.5,ylaser-Long,xlaser+9.5,ylaser)
            self.Collision()
            fenetre.after(10,lambda : self.Tir(xlaser,ylaser,Long,Larg))
            
        else:
            self.canvas.delete(self.laser)
            self.shoot=True

    def Collision(self):
        x1l,y1l,x2l,y2l=self.canvas.coords(self.canvas.find_all()[-1])
        toucher=self.canvas.find_overlapping(x1l,y1l,x2l,y2l)
        for i in toucher[1:-1]:
            mort=self.canvas.find_withtag(i)
            self.canvas.delete(mort)
            self.score+=50
            var_score.set("score:" +str(self.score))
            print("toucher: " ,mort)
        

        
        
class Laserrr:
    def __init__(self,posX,posY, canevas):
        self.Long=20
        self.Larg=5
        self.xlaser=posX
        self.ylaser=posY
        self.canevas=canevas
        self.laser=self.canevas.create_rectangle(self.xlaser+self.Larg+9.5,self.ylaser-self.Long,self.xlaser+9.5,self.ylaser, fill='orange')
        
        #self.Tir()
        

    def Tir(self):
        
        if self.ylaser>0 :
            self.ylaser-=8
            self.canevas.coords(self.laser,self.xlaser+self.Larg+9.5,self.ylaser-self.Long,self.xlaser+9.5,self.ylaser)
            self.Collision()
            fenetre.after(10,self.Tir())
            
        else:
            self.canevas.delete(self.laser)
            

    def Collision(self):
        x1l,y1l,x2l,y2l=self.canevas.coords(self.canevas.find_all()[-1])
        toucher=self.canevas.find_overlapping(x1l,y1l,x2l,y2l)
        
        for i in toucher[1:-1]:
            mort=self.canevas.find_withtag(i)
            self.canevas.delete(mort)
            print("toucher: " ,mort)


    



        






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

btnNew=tkinter.Button(fenetre,text="nouveau")
btnNew.grid(column=0, row=2, ipadx=5, pady=5,sticky="e")

new=Partie(canvas)

new.initialisation()

fenetre.mainloop()





