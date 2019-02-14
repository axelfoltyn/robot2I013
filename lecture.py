#symbole de robot =R
#symbole obstacle=O
#utiliser with open
#retourne larene
from Arene import *
from Obstacle import *
from Robot import *

def lecture(fichier):
  Fichier=open(fichier,"r")
   
  txt=Fichier.readline()
  x=int(txt)
  
  txt=Fichier.readline()
  y=int(txt)
  
  txt=Fichier.readline()
  z=int(txt)
  
  a= Arene(x,y,z)  #creation de arene
  
  n=0
  for elt in Fichier.readlines() :    #parcour le fichier pour cree des obstacles ou robots
    arg=elt.split(" ")
    if 'O'==arg[0] : 
      a.ajout_Obstacle(Obstacle(int(arg[1]),int(arg[2]),int(arg[3]),arg[0],float(arg[4])))
                            
    if 'R'==arg[0] : 
      a.ajout_Robot(Robot([int(arg[1]),int(arg[2]),int(arg[3])],float(arg[4]),float(arg[5]),[float(arg[6]),float(arg[7]),float(arg[8])]))
                      
    if 'C'==arg[0] :
      a.ajout_Obstacle(Obstacle(int(arg[1]),int(arg[2]),int(arg[3]),arg[0],lo=float(arg[4]),la=float(arg[5])))
                                                   
      
  Fichier.close()    
  
  return a
