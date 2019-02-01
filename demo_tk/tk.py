from tkinter import *

def deplacement():
    canvas.move(robot,10,0) ### exemple: vitesse en direction 1:0 ~~> 10/0.04 = 250 pixels/seconde
    #On repete cette fonction
    fenetre.after(40,deplacement)
    ### 40 pour avoir un mouvement assez fluide: ~25images/seconde

# initialisation de la fenetre
fenetre = Tk()

# ouvre un espace de dessin
canvas = Canvas(fenetre, width=800, height=600, background='grey')

#affiche les dessins "canvas"	
canvas.pack()

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(fenetre, text ='Quitter', command = fenetre.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

# initialise le robot (représenté par un triangle indiquant sa direction et dont la pointe marque sa position)

robot = canvas.create_polygon(100,100,60,90,60,110)


deplacement()

# affiche la fenetre jusqu'à fermeture par l'utilisateur		
fenetre.mainloop()