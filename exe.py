# import des librairies et fonctions
from tkinter import *
import PIL.Image
from mouvement import *


# création de la fenêtre dans laquelle on ajoute un canvas avec des marges extérieures de 45px

fen = Tk()
fen.geometry('600x650')
fen.config(background="#49667A")

can = Canvas(fen,width=500,height=500)
can.pack(padx=45,pady=45)

img = PIL.Image.open("pont.png")
largeur , hauteur = img.size

fen.title("Jeu pousse-pousse")
fen.iconbitmap("Pont.ico")

#################################################

# fonction qui découpe l'image en 16 cases qui sont sauvegardées dans le dossier du programme 
def decoupe():
    cases=[]
    
    for row in range(0,4):
        for col in range(0,4):
            box = (col*largeur/4,row*hauteur/4,(col+1)*largeur/4,(row+1)*hauteur/4)
            area = img.crop(box)
            area.save(f"image{row}{col}.png")
            cases.append(f"image{row}{col}.png")
            
    return cases

#################################################

# création d'une grille représentant la répartition des cases de l'image
matrice = [[0,1,2,3],
           [4,5,6,7],
           [8,9,10,11],
           [12,13,14,15]
           ]

matrice_origine = [[0,1,2,3],
                   [4,5,6,7],
                   [8,9,10,11],
                   [12,13,14,15]
                   ]

liste_cases=decoupe()

liste_images=[]
for etiquette in liste_cases:
    img = PhotoImage(file=etiquette)
    liste_images.append(img)

# fonction qui affiche les cases en fonction de leur répartition dans la matrice
def affichage(grid):
    for row in range(0,4):
        for col in range(0,4):
            can.create_image(col*largeur/4, row*hauteur/4, image=liste_images[grid[row][col]], anchor=NW)

affichage(matrice)

#################################################

# fonction qui divise le canvas en ligne et colonne correspondant aux cases de la matrice 
def coligne(position):
    if position >= 0 and position <= 125:
        position=0
    if position > 125 and position <= 250:
        position=1
    if position > 250 and position <= 375:
        position=2
    if position > 375 and position <= 500:
        position=3
    return position
        
#################################################         

# fonction permettant d'échanger les cases cliquer qui sont adjacentes
def pos_click(event):
    global matrice
    pos_x=event.x
    pos_y=event.y
    
    x=coligne(pos_y)
    y=coligne(pos_x)
    
    direction_blanc=direction(matrice,x,y,pos_empty(matrice)[0],pos_empty(matrice)[1])
    if direction_blanc != "NON ADJACENTE":
        matrice=echange(matrice,x,y,pos_empty(matrice)[0],pos_empty(matrice)[1])
        can.delete('all')
        affichage(matrice)
        victoire()
    else:
        print(direction_blanc)

can.bind("<Button-1>", pos_click)

#################################################

# fonction lancé suite à la pression du bouton mélanger, elle déclenche la fonction "melange" et se charge d'afficher le résultat final et de désactiver le bouton "Mélange"
def mel():
    global matrice
    matrice = melange(matrice)
    can.delete('all')
    affichage(matrice)
    bouton_melange.config(state='disabled')
    
    
#################################################

# fonction lancé suite à la pression du bouton abandonner, elle permet de réinitialiser l'image
def abandon():
    global matrice
    can.delete('all')
    matrice=[[0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,15]
            ]
    affichage(matrice)
    bouton_melange.config(state='active')
   
#################################################

# fonction détectant si la grille obtenue est celle d'origine, ce qui déclare une réussite si c'est le cas
def victoire():
    global matrice
    global matrice_origine
    if matrice == matrice_origine:
        gagne=Label(fen,text='Bravo, vous avez gagné !').pack()
        print("Bravo, vous avez gagné !")
        bouton_melange.config(state='active')
    
#################################################    

# bouton déclenchant la fonction "mel"
bouton_melange=Button(fen,text="Mélanger",command=mel)    
bouton_melange.place(x="150",y="580")    

# bouton fermant la fenêtre
bouton_fermer=Button(fen,text="Quitter",command=fen.destroy)
bouton_fermer.place(x="400",y="580")     
    
# bouton permettant d'abandonner et de remettre l'image vierge
bouton_abandon=Button(fen,text='Abandonner',command=abandon)
bouton_abandon.place(x="266",y="580")
    
fen.mainloop()

#################################################