#symbole de robot =R
#symbole obstacle=O
#utiliser with open

def lecture(fichier):
  Fichier=open(fichier,"r")
  
  txt=Fichier.readline()
  x=int(txt)
  
  txt=Fichier.readline()
  y=int(txt)
  
  txt=Fichier.readline()
  z=int(txt)
  
  txt=Fichier.readline()
  n=0
  while txt :
    arg=txt.split("")
    switch (arg[0]) {
      case 'O' : ajout_Obstacle(Obstacle(int(arg[1]),int(arg[2]),int(arg[3]),float(arg[4])))
                 break      
      
      case 'R' : ajout_Robot(Robot(int(arg[1]),int(arg[2]),int(arg[3]),float(arg[4]),float(arg[5]),float(arg[6]),float(arg[7]),float(arg[8]),float(arg[9]),float(arg[10]),float(arg[11]),float(arg[12])))
                 break
      case 'C' :  ajout_Obstacle(Obstacle(int(arg[1]),int(arg[2]),int(arg[3]),float(arg[4]),float(arg[5]),float(arg[6])))
                 break                           
    }  
    txt=Fichier.readline()
  Fichier.close()    
  
