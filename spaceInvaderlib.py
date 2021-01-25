#Header
"""
Cette page contient les fonctions nécessaires pour jouer 
Auteurs : Adrien Pouxviel, Farès Zaghouane
Il a été réalisé le 17/01/2021 grosse mise a jour le 24/01/21
To Do : - probleme lorsque joueur et un alien tirent en meme temps.
        -ajouter plus d'aliens   
        -ajouter alien bonus    
        -mettre des images pour les aliens et le joueur

Lien du git : https://github.com/PouxvielAdrien/Space-Invaders
"""



import tkinter
import random

class Partie:
    """
    cette classe est notre classe principale c'est elle qui vient gerer les parties du jeux
    qui sont en communes entres les differents personnages comme la victoire de la partie. 
    """
    def __init__(self, canvas,fenetre ,var_score,var_vie):
        #creation des liens avec la fenetre du programme principal
        self.canvas=canvas
        self.fenetre=fenetre
        self.var_score=var_score
        self.var_vie=var_vie

        # variable qui gere si le jeu est en pause ou non 
        self.continuer=True
        
        # creation des objets du jeu
        self.joueur=Joueur(self.fenetre,self.canvas)
        self.mur1=Protection(self.canvas,50)
        self.mur2=Protection(self.canvas,280)
        self.mur3=Protection(self.canvas,500)
        self.monstre=[Monstres(self.fenetre,self.canvas,10,0),Monstres(self.fenetre,self.canvas,50,0),Monstres(self.fenetre,self.canvas,90,0),Monstres(self.fenetre,self.canvas,130,0),Monstres(self.fenetre,self.canvas,170,0),Monstres(self.fenetre,self.canvas,210,0),Monstres(self.fenetre,self.canvas,250,0),Monstres(self.fenetre,self.canvas,290,0),Monstres(self.fenetre,self.canvas,330,0)]

        # on initialise le deplacement et les tirs des monstres
        self.TirMonstre() 
        self.deplacementMonstre()

        # on initalise les diffrentes parties raccrocher au lables dans le jeu
        self.var_vie.set("vie"+str(self.joueur.vie))
        self.var_score.set("score: "+ str(self.joueur.score))
        self.fenetre.update()
        self.miseAJour()

        # on intialise les actions du joueur
        self.canvas.bind('<Right>',self.joueur.deplacement)
        self.canvas.bind('<Left>', self.joueur.deplacement)
        self.canvas.bind('<space>',self.joueur.Tir)
        self.canvas.focus_set()


    def miseAJour(self):
        # cette fonction tourne en boucle et sert a mettre a jour l'affichage du score et de la vie 
        if self.continuer:
            self.var_score.set("score: "+ str(self.joueur.score))
            self.var_vie.set("vie"+str(self.joueur.vie))
            self.fenetre.update()
            self.gagner()
            self.perdu()
        self.fenetre.after(10,self.miseAJour)

    def pause(self):
        # fonction qui met le jeu en pause mais ne le fais pas repartir
        
        
        if self.continuer==True:
            self.continuer=False
            pause=tkinter.Label(self.fenetre, text="Pause", bg="#d348d0")
            pause.grid(column=0, row=1, ipadx=5, pady=5)
        else:
            self.continuer=True
            if pause.winfo_exists():
                pause.destroy()
            
            
 
    
    def TirMonstre(self):
        # choisi un monstre au hasard et le fais tirer
        global dicoEnnemis
        if len (dicoEnnemis)!=0 and self.continuer:
            choix=random.choice(list(dicoEnnemis.values()))
            Laserrr(self.fenetre,choix.positionX,choix.positionY,self.canvas,"orange",10,False)
        self.fenetre.after(5000, self.TirMonstre)    

    def deplacementMonstre(self):
        # on regarde si le monstre le plus a droite le mur droit si oui on les change tous de direction et descendre
        # on fais de meme avec le monstre le plus a gauche
        # sinon on les deplacent simplement sur le cote 
        # une fois qu'ils sont descendu on regarde si ils ont atteint la limite basse pour voir si on a perdu

        if self.continuer:

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
        #teste si on a perdu si le joueur a plus de vie ou si les monstres sont en bas de l'ecran
        # dans ce cas on stop les monstres et on affiche un petit label
        global dicoEnnemis
        if self.monstre[0].positionY>250 or self.joueur.vie<=0:
            
            self.canvas.delete(2)
            self.continuer=False
            fin=tkinter.Label(self.fenetre, text="vous avez perdu", bg="#d348d0")
            fin.grid(column=0, row=1, ipadx=5, pady=5)

    def gagner(self):
        #test si on a gagner c'est a dire s'il n'y a plus de monstre 
        global dicoEnnemis
        if len(dicoEnnemis)==0:
            
            self.continuer=False
            fin=tkinter.Label(self.fenetre, text="vous avez gagner", bg="#d348d0")
            fin.grid(column=0, row=1, ipadx=5, pady=5)

    

class Monstres:
    #classe qui nous cree les monstres avec leurs attributs
    def __init__(self, fenetre,pcanvas,px,py):

        global dicoEnnemis
        # on vient ajouter des liens dans la classe monstre pour faire tourner le jeu
        self.fenetre=fenetre
        self.canvas=pcanvas
        
        # on declare les caracteristiques des monstres
        self.positionX=px
        self.positionY=py
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.vitesse=0
        self.monst=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="blue")
        
        # on ajoute le monstre dans le dictionnaire Ennemies avec son Id sur le canvas
        dicoEnnemis[self.canvas.find_all()[-1]]=self
        self.dificulter()

    def deplacement(self):
        # fonction qui permet le deplacr le monstre
        self.positionX+=self.vitesse
        self.canvas.coords(self.monst,self.positionX,self.positionY,self.positionX+25,self.positionY+25)
        
    def dificulter(self):
        # petite fonction qui augmente la difficulter en augmentant la vitesse des monstres
        self.vitesse+=5
        self.fenetre.after(10000,self.dificulter)


class Protection:
    #creation des murs de protection
    def __init__(self,canvas,px):
        global dicoAmis
        self.canvas=canvas
        self.mur=[self.canvas.create_rectangle(px,300,px+20,320,fill="white"),self.canvas.create_rectangle(px+25,300,px+45,320,fill="white"),self.canvas.create_rectangle(px+50,300,px+70,320,fill="white"),self.canvas.create_rectangle(px,320,px+20,340,fill="white"),self.canvas.create_rectangle(px+25,320,px+45,340,fill="white"),self.canvas.create_rectangle(px+50,320,px+70,340,fill="white")]           
        # on vient a jouter chaque partie du mur dans le dictionnnaire Amis avec son Id sur le canvas
        for i in range(1,len(self.mur)+1):
            dicoAmis[self.canvas.find_all()[-i]]=self
            


class Joueur:
    # creation du joueur
    def __init__(self,fenetre,pcanvas):
        global dicoAmis  
        # on vient ajouter des liens dans la classe joueur pour faire tourner le jeu
        self.canvas= pcanvas
        self.fenetre=fenetre 

        # on declare les caracteristiques du joueur
        self.vie=3
        self.score=0
        self.positionX=305
        self.positionY=390
        self.tailleX=self.positionX+25
        self.tailleY=self.positionY+25
        self.move=25
        self.shoot=True
        self.vitesse = 5
        self.joueur=self.canvas.create_rectangle(self.positionX,self.positionY,self.tailleX,self.tailleY, fill="red")
        
        # on ajoute le joueur dans le dictionnaire Amis avec son Id sur le canvas
        dicoAmis[self.canvas.find_all()[-1]]=self


    def deplacement(self,event):
        """
        Gestion de l'événement Appui sur une touche du clavier
        et vient deplacer notre joueur en fonction de la touche ou lui permettre de tirer
        """
        touche = event.keysym
       
        #déplacement vers la gauche
        if touche == 'Left' :
            if self.positionX - self.move > 0:
                self.positionX-=self.move

        #déplacement vers la droite 
        if touche == 'Right':
            if self.positionX+25 + self.move <= self.canvas.winfo_width():
                self.positionX+=self.move
          
        self.canvas.coords(self.joueur,self.positionX,self.positionY,self.positionX+25,self.positionY+25)    


    def Tir(self, event):
        # losque l'on appuis sur Espace on vient cree un Objet laser 
            if self.shoot:
                self.shoot=False
                Laserrr(self.fenetre,self.positionX,self.positionY,self.canvas,"green",-10,True)
                self.shoot=True
        # on voulais limmiter le tir avec la variable shoot pour empecher de tirer plusieurs lasers en meme temps,
        # mais on a un procble a cause des fenetre.after car elle sont pas bloquante donc on revient dans cette fonction avant la fin du laser

class Laserrr:
    #creation du laser
    def __init__(self,fenetre,posX,posY, canevas,couleur,vitesse, ami):
         # on vient ajouter des liens dans la classe laser pour pouvoir l'ajouter dans la partie graphique du jeu
        self.canevas=canevas
        self.fenetre=fenetre

        #caracteristiques du laser
        self.Long=20
        self.Larg=5
        self.xlaser=posX
        self.ylaser=posY
        self.couleur=couleur  # depend de si c'est le joueur ou un mosntre qui tir
        self.vitesse=vitesse
        self.ami=ami   # depend de si c'est le joueur ou un mosntre qui tir pour la fonction couler
        self.laser=self.canevas.create_rectangle(self.xlaser+self.Larg+9.5, self.ylaser-self.Long, self.xlaser+9.5, self.ylaser, fill=self.couleur)

        self.Tir()
    


            
    def Tir(self):
        #fais bouger le laser sur le canvas ou le supprime s'il est sortir du canvas
        if self.ylaser<500 and self.ylaser>0:
            self.ylaser+=self.vitesse
            self.canevas.coords(self.laser, self.xlaser+self.Larg+9.5, self.ylaser-self.Long, self.xlaser+9.5,self.ylaser )
            self.couler()
            self.fenetre.after(5,self.Tir)
        else:
            self.canevas.delete(self.laser)
              
        
            
    def couler(self):
        global dicoAmis ,dicoEnnemis
        # permet de donner tous les elements du canvas qui se supperposent avec le laser overlapping
        x1l,y1l,x2l,y2l=self.canevas.coords(self.canevas.find_all()[-1])
        toucher=self.canevas.find_overlapping(x1l,y1l,x2l,y2l)

        # verification pour savoir dans quel dictionnaire on vas chercher  True si c est le joueur qui tir False si c'est un monstre
        if self.ami==True:  
            for i in dicoEnnemis.keys():
                if i in toucher:
                    self.canevas.delete(i)
                    self.canevas.delete(self.laser)
                    del(dicoEnnemis[i])
                    dicoAmis[2].score+=50   # change le score du joueur s'il a toucher une monstre on peux mettre la cle en dur car le joueur a toujours l'indice 2 dans le canvas
                    
        # si un monstre tir on cherche a supprimer dans le dictionnaire des amis( murs + joueur)            
        else: 
            for i in toucher :
                # disjonction de cas, car si le joueur est toucher on lui enleve une vie, si c'est une mur on le supprime simplement
                if i in dicoAmis.keys():
                    if i==2:
                        dicoAmis[2].vie-=1
                        self.canevas.delete(self.laser)
                        
                    else:
                        self.canevas.delete(i)
                        self.canevas.delete(self.laser)
                        del(dicoAmis[i])
                        
        # dans les 2 cas on a un dictionnaire qui change de taille durant la boucle, mais on ne peux pas faire autrement car si on boucle sur le tuple Toucher on a un bug a niveau des monstres
        # car avec 1 tir du joueurs plusieurs monstres peuvent se supprimer en meme temps. Nous n'avons pas trouver de solution a cela.



# declaration de nous 2 seules variables globales nous avons ete force de les utiliser,
# car on les utilises dans plusieurs classes differentes, on a essayer sans ces variables mais le jeux ne tournais pas correctement,$
# ou on devais faire des appel de foncitions avec parametre simplement pour passer ce paramettre a une sous fonction ex: Tir qui appelle couler         
dicoAmis={}
dicoEnnemis={}    
    
  


    


