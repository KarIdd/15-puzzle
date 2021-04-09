from random import *

#################################################

# fonction pour connaître la direction de la case blanche par rapport à une autre case
def direction(grid,ligne,colonne,ligne_vide,colonne_vide):
    if ligne==ligne_vide-1 and colonne==colonne_vide:
        return "SUD"
    elif ligne==ligne_vide+1 and colonne==colonne_vide:
        return "NORD"
    elif ligne==ligne_vide and colonne==colonne_vide-1:
        return "EST"
    elif ligne==ligne_vide and colonne==colonne_vide+1:
        return "OUEST"
    else:
        return "NON ADJACENTE"

#################################################

# fonction échangeant deux cases
def echange(grid,ligne,colonne,ligne_vide,colonne_vide):
    grid[ligne][colonne], grid[ligne_vide][colonne_vide] = grid[ligne_vide][colonne_vide], grid[ligne][colonne]
    return grid

#################################################

# fonction retournant les coordonnées de la case blanche
def pos_empty(grid):
    for x_blanc in range (4):
        for y_blanc in range (4):
            if grid[x_blanc][y_blanc] == 3:
                return (x_blanc,y_blanc)

#################################################

# fonction qui donne les directions que peux prendre la case blanche
def motions_empty(grid):
    liste_direction=[]
    for x in range (0,4):
        for y in range (0,4):
            direction_blanc=direction(grid,x,y,pos_empty(grid)[0],pos_empty(grid)[1])
            if direction_blanc == ("SUD"):
                liste_direction.append("NORD")
            elif direction_blanc == ("NORD"):
                liste_direction.append("SUD")
            elif direction_blanc == ("EST"):
                liste_direction.append("OUEST")
            elif direction_blanc == ("OUEST"):
                liste_direction.append("EST")
    return liste_direction

#################################################

# fonction qui mélange automatiquement les cases du pousse-pousse
def melange(grid):
    global matrice
    direction_trou=[]
    for i in range (0,2):
        #les positions de la case blanche
        ligne_blanc=pos_empty(grid)[0]
        colonne_blanc=pos_empty(grid)[1]
        choix=False
        direction_possible=motions_empty(grid)
        while choix==False:
            la_direction=choice(direction_possible)
            direction_possible.remove(la_direction)
            
            if la_direction == "NORD" and (len(direction_trou)==0 or direction_trou[-1] != "SUD"):
                choix=True
                #échange de la case blanche et de la case située dans la direction choisi aléatoirement
                grid=echange(grid,ligne_blanc-1,colonne_blanc,ligne_blanc,colonne_blanc)
                direction_trou.append(la_direction)
                
            elif la_direction == "SUD" and (len(direction_trou)==0 or direction_trou[-1] != "NORD"):
                choix=True
                #échange de la case blanche et de la case située dans la direction choisi aléatoirement
                grid=echange(grid,ligne_blanc+1,colonne_blanc,ligne_blanc,colonne_blanc)
                direction_trou.append(la_direction)
                
            elif la_direction == "OUEST" and (len(direction_trou)==0 or direction_trou[-1] != "EST"):
                choix=True
                #échange de la case blanche et de la case située dans la direction choisi aléatoirement
                grid=echange(grid,ligne_blanc,colonne_blanc-1,ligne_blanc,colonne_blanc)
                direction_trou.append(la_direction)
                
            elif la_direction == "EST" and (len(direction_trou)==0 or direction_trou[-1] != "OUEST"):
                choix=True
                #échange de la case blanche et de la case située dans la direction choisi aléatoirement
                grid=echange(grid,ligne_blanc,colonne_blanc+1,ligne_blanc,colonne_blanc)
                direction_trou.append(la_direction)

    return grid

#################################################