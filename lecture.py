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
  
  txt=Fichier.readline()
  n=0
  while txt :    #parcour le fichier pour cree des obstacles ou robots
    arg=txt.split(" ")
    if 'O'==arg[0] : 
      ajout_Obstacle(Obstacle(int(arg[1]),int(arg[2]),int(arg[3]),arg[0],flot(arg[4])))
                            
    if 'R'==arg[0] : 
      ajout_Robot(Robot(int(arg[1]),int(arg[2]),int(arg[3]),float(arg[4]),float(arg[5]),float(arg[6]),float(arg[7]),float(arg[8])))
                      
    if 'C'==arg[0] : 
      ajout_Obstacle(Obstacle(int(arg[1]),int(arg[2]),int(arg[3]),float(arg[0]),float(arg[4]),float(arg[5]),float(arg[6])))
                                                   
    txt=Fichier.readline()
  
  Fichier.close()    
  
  return a
