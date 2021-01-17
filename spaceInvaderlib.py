#Header
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
import random

class Partie:
    """
    cette classe est notre classe principale c'est elle qui vient gerer tous le jeu.
    comme le deplacement du joueur les deplacement des monstres etc.
    """
    def __init__(self, canvas,fenetre ,var_score,var_vie):
        #creation des liens avec la fenetre du programme principal
        self.canvas=canvas
        self.fenetre=fenetre
        self.var_score=var_score
        self.var_vie=var_vie

        # creation des objets du jeu 
        self.joueur=Joueur(self.canvas)
        self.mur1=Protection(self.canvas,50)
        self.mur2=Protection(self.canvas,280)
        self.mur3=Protection(self.canvas,500)
        self.monstre=[Monstres(self.canvas,10,0),Monstres(self.canvas,50,0)]
        self.dicoAmis={2:self.joueur, 3:self.mur1,4:self.mur1,5:self.mur1,6:self.mur1,7:self.mur1,8:self.mur1,9:self.mur2,10:self.mur2,11:self.mur2,12:self.mur2,13:self.mur2,14:self.mur3,15:self.mur3,16:self.mur3,17:self.mur3,18:self.mur3,19:self.mur3,20:self.mur3}
        self.dicoEnnemis={21:self.monstre[0],22:self.monstre[1]}

        self.var_vie.set("vie"+str(self.joueur.vie))
        self.var_score.set("score: "+ str(self.joueur.score))
        self.fenetre.update()
        self.TirMonstre()
        self.deplacementMonstre()
        self.canvas.bind('<Key>',self.deplacementJoueur)
        self.canvas.focus_set()

    def deplacementJoueur(self,event):
        """
        Gestion de l'événement Appui sur une touche du clavier
        et vient deplacer notre joueur en fonction de la touche ou lui permettre de tirer
        """
        touche = event.keysym
       
        #déplacement vers la gauche
        if touche == 'Left' :
            if self.joueur.positionX - self.joueur.move > 0:
                self.joueur.positionX-=self.joueur.move

        #déplacement vers la droite 
        if touche == 'Right':
            if self.joueur.positionX+25 + self.joueur.move <= self.canvas.winfo_width():
                self.joueur.positionX+=self.joueur.move

        #tir
        if touche == 'space' and self.joueur.shoot: 
            self.joueur.shoot=False       
            laz=Laserrr(self.joueur.positionX,self.joueur.positionY,self.canvas,"green",-10)
            self.Tirjoueur(laz)                   
            
            
        self.canvas.coords(self.joueur.joueur,self.joueur.positionX,self.joueur.positionY,self.joueur.positionX+25,self.joueur.positionY+25)

    def Tirjoueur(self,laz):
        # gestion du tir du joueur
        laz.Tir()
        toucher=laz.couler()
        self.testeAmis(toucher,laz)
        self.fenetre.after(20,lambda: self.Tirjoueur(laz) )


    def TirMonstre2(self,laz):
        #gere le deplaczement du tir du monstre
        laz.Tir()
        toucher=laz.couler()
        self.testeEnnemie(toucher,laz)
        self.fenetre.after(20,lambda:self.TirMonstre2(laz))
    
    def TirMonstre(self):
        # choisi un monstre au hasard et le fais tirer
        choix=random.choice(list(self.dicoEnnemis.values()))
        laz=Laserrr(choix.positionX,choix.positionY,self.canvas,"orange",10)
        self.TirMonstre2(laz)
        self.fenetre.after(5000, self.TirMonstre)    
    
    def testeEnnemie(self,listeTouche,laser):
        #fonction qui teste si un allie du joueur est touche par un tir ennemi
        for touche in listeTouche:
            if touche in self.dicoAmis:
                if touche ==2:
                    print(self.joueur.vie)
                    self.joueur.vie-=1
                    self.var_vie.set("vie:"+str(self.joueur.vie))
                    self.fenetre.update()
                    print(self.joueur.vie)
                    laser.supprimer()
                    print(laser)
                    
                    
                    self.perdu()
                else:
                    del(self.dicoAmis[touche])
                    self.canvas.delete(touche)
                    laser.supprimer()
    
    def testeAmis(self,listeTouche, laser):
        #fonction qui teste si un alien est touche par un tir du joueur
        for touche in listeTouche:
            if touche in self.dicoEnnemis.keys():
                del(self.dicoEnnemis[touche])
                self.canvas.delete(touche)
                laser.supprimer()
                self.gagner()

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

        self.fenetre.after(75,self.deplacementMonstre)

    def perdu(self):
        #teste la fin de partie si perdue
        if self.monstre[0].positionY>280 or self.joueur.vie<=0:
            for monster in self.monstre:
                monster.vitesse=0
            self.canvas.delete(2)
            self.canvas.delete("all")
            fin=tkinter.Label(self.fenetre, text="vous avez perdu", bg="#d348d0")
            fin.grid(column=0, row=1, ipadx=5, pady=5)

    def gagner(self):
        #test la fin de partie si gagnée
        if len(self.dicoEnnemis)==0:
            fin=tkinter.Label(self.fenetre, text="vous avez gagner", bg="#d348d0")
            fin.grid(column=0, row=1, ipadx=5, pady=5)

    

class Monstres:
    #classe qui nous cree les monstre avec leurs attributs
    def __init__(self,pcanvas,px,py):
        self.vie=1
        self.positionX=px
        self.positionY=py
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.canvas=pcanvas
        self.monst=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="blue")
        self.vitesse=5
    
    def deplacement(self):
    
        self.positionX+=self.vitesse
        self.canvas.coords(self.monst,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        

class Protection:
    #creation des murs de protection
     def __init__(self,canvas,px):
         self.canvas=canvas
         self.mur=[self.canvas.create_rectangle(px,300,px+20,320,fill="white"),self.canvas.create_rectangle(px+25,300,px+45,320,fill="white"),self.canvas.create_rectangle(px+50,300,px+70,320,fill="white"),self.canvas.create_rectangle(px,320,px+20,340,fill="white"),self.canvas.create_rectangle(px+25,320,px+45,340,fill="white"),self.canvas.create_rectangle(px+50,320,px+70,340,fill="white")]           
        
class Joueur:
    # creation du joueur
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



    
        

        
        
class Laserrr:
    #creation du laser
    def __init__(self,posX,posY, canevas,couleur,vitesse):
        self.Long=20
        self.Larg=5
        self.xlaser=posX
        self.ylaser=posY
        self.canevas=canevas
        self.couleur=couleur
        self.vitesse=vitesse
        self.laser=self.canevas.create_rectangle(self.xlaser+self.Larg+9.5, self.ylaser-self.Long, self.xlaser+9.5, self.ylaser, fill=self.couleur)
        
    def supprimer(self):

        self.canevas.delete(self.laser)


            
    def Tir(self):
        #fais bouger le laser sur le canvas
        if self.ylaser<500 and self.ylaser>0:
            self.ylaser+=self.vitesse
            self.canevas.coords(self.laser, self.xlaser+self.Larg+9.5, self.ylaser-self.Long, self.xlaser+9.5,self.ylaser )
           
        
            
    def couler(self):
        # permet de donner tous les elements du canvas qui se supperposent avec le laser
        x1l,y1l,x2l,y2l=self.canevas.coords(self.canevas.find_all()[-1])
        toucher=self.canevas.find_overlapping(x1l,y1l,x2l,y2l)
        return toucher
  


    


