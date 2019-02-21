from tkinter import *

def deplacement():
    canvas.move(robot,10,0) # (valeurs en pixels) ex: robot avance de 10 pixels en direction 1:0
    #On repete cette fonctionn
    fenetre.after(40,deplacement) #valeur en millisecondes (40 pour avoir un mouvement assez fluide: ~25images/seconde)
    # exemple: vitesse en direction 1:0 ~~> 10/0.04 = 250 pixels/seconde

# initialisation de la fenetre
fenetre = Tk()

# ouvre un espace de dessin
canvas = Canvas(fenetre, width=800, height=600, background='white')

#affiche les dessins "canvas"	
canvas.pack()

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(fenetre, text ='Quitter', command = fenetre.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

# initialise le robot (représenté par un triangle indiquant sa direction et dont la pointe marque sa position)

robot = canvas.create_polygon(60,20,20,10,20,30)
#robot = canvas.create_polygon(20,60,30,20,10,20)

o_rectangle = canvas.create_rectangle(300,300,350,370,fill = "black")
o_circle = canvas.create_oval(600,150,650,200,fill = "black")

#supprimer un élément
canvas.delete(élément)
#tout supprimer (dessins canvas)
canvas.delete(ALL)

#met a jour le canvas sert enormément pour le deplacement
canvas.update()

deplacement()

# affiche la fenetre jusqu'à fermeture par l'utilisateur		
fenetre.mainloop()
