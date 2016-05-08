# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:01:00 2016

@author: Ethan

"""
#importation des bibliothèques
from Tkinter import *
import random
import tkFont

#intialisation de la variable L
L=0


#Défintion des fonctions
def generateur(L):
    ''' 
    Fonction qui génère 5 entiers au hasard entre 1 et 10 et avec 50 et 100 également. Il affecte ses entiers dans une liste L. Elle s'éxecute lorsqu'on appuie sur le bouton 'Chiffres' (b1).  '''
    global a,b,c,d,e
    L=random.sample(range(1,11)+[50,100],5)
    a=L[0]
    b=L[1]
    c=L[2]
    d=L[3]
    e=L[4]
    return L


def carres():
    '''
    Créé 5 label avec les éléments de la liste L, fonctionne avec une boucle while et des conditions if, elif. Elle s'éxecute lorsqu'on appuie sur le bouton 'Chiffres' (b1). Elle détruit tout le contenu du canevas 'can' à chaque exécution. Affectation de la valeur de a,b,c,d,e générée par 'generateur' au compteur de telle sorte que chaque label affiche une variable. La variable Tkinter : Chiffres prend la valeur du compteur (convertie en type string).
    ''' 
    global x,i,compteur
    compteur=0
    i=0
    x=100
    for widget in can.winfo_children(): #détruit tout ce qui est dans le canevas 'can'
        widget.destroy()
    while x<701:
        
       #Affectation de la valeur (a,b,c,d,e) générée par 'generateur' à compteur de telle sorte que chaque rectangle en affiche une
        if compteur==0:
            compteur=a
        elif compteur==1:
            compteur=b
        elif compteur==2:
            compteur=c
        elif compteur==3:
            compteur=d
        elif compteur==4:
            compteur=e
       
        #La variable Tkinter :Chiffres prend la valeur de compteur (convertie en type string)
        Chiffres=StringVar()
        Chiffres.set(str(compteur))
        
        # Création d'un widget Label (texte: un chiffre parmi les cinq)
        LabelResultat = Label(can,textvariable = Chiffres, fg ='black', bg='white', relief='solid')
        LabelResultat.place(x=x,y=50)
        LabelResultat.config(font='bold 55')
        #incrémentation des abscisses(x), du compteur i, et affectation à la variable compteur de la n-ième fois que la boucle tourne (compté par i)
        x=x+150 
        i=i+1
        compteur=i
    '''else:
         i=0
         compteur=0
         x=100'''
         
         
         
         
         
def sol():
    '''
    La fonction sol() choisi au hasard une suite d'opératoins à faire pour définir le résultat à trouver 's'. Elle affiche ce résultat avec écrit : 'à trouver:'. Elle s'éxecute lorsqu'on appuie sur le bouton 'Chiffres' (b1). Elle associe aussi à S1 une chaine de caractères qui sera celle affichée lors de l'appui sur le bouton 'solution' par la fonction so().
    '''
    global a,b,c,d,e,s,S1
    h=random.randint(1,4)
    if h==1:
        if ((b+e)%a)==0:
            s=((b+e)/a)+c
            S1="Une solution\npossible:\n \n"+str(b)+"+"+str(e)+"="+str(b+e)+"\n"+str(b+e)+"/"+str(a)+"="+str((b+e)/a)+"\n"+str((b+e)/a)+"+"+str(c)+"="+str(s)
        else:
            s=((b+e)*a)+c
            S1="Une solution\npossible:\n \n"+str(b)+"+"+str(e)+"="+str(b+e)+"\n"+str(b+e)+"x"+str(a)+"="+str((b+e)*a)+"\n"+str((b+e)*a)+"+"+str(c)+"="+str(s)
    
    
    if h==2:
        if a>b:
            s=((a-b)*e)+c
            S1="Une solution\npossible:\n \n"+str(a)+"-"+str(b)+"="+str(a-b)+"\n"+str(a-b)+"x"+str(e)+"="+str((a-b)*e)+"\n"+str((a-b)*e)+"+"+str(c)+"="+str(s)
        else:
            s=((b-a)*e)+c
            S1="Une solution\npossible:\n \n"+str(b)+"-"+str(a)+"="+str(b-a)+"\n"+str(b-a)+"x"+str(e)+"="+str((b-a)*e)+"\n"+str((b-a)*e)+"+"+str(c)+"="+str(s)
   
   
    if h==3:
        if b>a:
            s=(((c+e)*(b-a))+d)
            S1="Une solution\npossible:\n \n"+str(c)+"+"+str(e)+"="+str(c+e)+"\n"+str(b)+"-"+str(a)+"="+str(b-a)+"\n"+str(b-a)+"x"+str(c+e)+"="+str((c+e)*(b-a))+"\n"+str((c+e)*(b-a))+"+"+str(d)+"="+str(s)
        else:
            s=(((c+e)*(a-b))+d)
            S1="Une solution\npossible:\n \n"+str(c)+"+"+str(e)+"="+str(c+e)+"\n"+str(a)+"-"+str(b)+"="+str(a-b)+"\n"+str(a-b)+"x"+str(c+e)+"="+str((c+e)*(a-b))+"\n"+str((c+e)*(a-b))+"+"+str(d)+"="+str(s)
            
    if h==4:
        if ((b*c)%e)==0:
            s=((b*c)/e)+a
            S1="Une solution\npossible:\n \n"+str(b)+"x"+str(c)+"="+str(b*c)+"\n"+str(b*c)+"/"+str(e)+"="+str((b*c)/e)+"\n"+str((b*c)/e)+"+"+str(a)+"="+str(s)
        else:
            s=((b*c)+e)+a
            S1="Une solution\npossible:\n \n"+str(b)+"x"+str(c)+"="+str(b*c)+"\n"+str(b*c)+"+"+str(e)+"="+str((b*c)+e)+"\n"+str((b*c)+e)+"+"+str(a)+"="+str(s)
      


    #Affichage de :'A trouver : s', avec s le resultat à trouver 
    at=StringVar()
    at.set('à trouver : ')
    labat = Label(can,textvariable = at, fg ='black', bg ='white')
    labat.place(x=130,y=250)
    labat.config(font='bold 30')
    
    resultat=StringVar()
    resultat.set(str(s))
    solat = Label(can,textvariable = resultat, fg ='black', bg ='white')
    solat.place(x=320,y=235)
    solat.config(font='bold 47')
    

def c1():
    '''.
    La fonction c1() est celle éxecutée lors de l'appui sur le bouton 'Chiffres' (b1). Elle regroupe 3 fonctions: generateur(L), carres(), et sol().
    '''
    print generateur(L)
    print carres()
    print sol()

def so():
   '''
   La fonction so() affiche la variable S1 -générée auparavant par la fonction sol()- lors de l'appui sur le bouton 'solution' (b2).
   '''
   Solution=StringVar()
   Solution.set(S1)
   LabelResultat = Label(can,textvariable = Solution, fg ='black',bg='white')
   LabelResultat.place(x=600,y=200)
   LabelResultat.config(font='bold 25')
   
        

    
#Creation du graphisme
fen = Tk()
fen.title('Le compte est bon')


can=Canvas(fen,width=850, height=500, bg='white') #création du canevas : can
can.pack( padx=5, pady=5)

txt = can.create_text(400, 30, text="Le compte est bon", font=tkFont.Font(size=30, weight='bold'))

b1=Button(fen, text ='Chiffres', command=c1, overrelief='ridge', bd='10',height='2', font=tkFont.Font(size=15, weight='bold'))
b1.place(relx=0.33, rely=0.85, anchor="c") #création et placement du bouton b1 qui effectue la fonction c1()


b2=Button(fen, text ='Solution', command=so, overrelief='groove', bd='10',height='2', font=tkFont.Font(size=15, weight='bold'))
b2.place(relx=0.45, rely=0.85, anchor="c")  #création et placement du bouton b2 qui effectue la fonction so()


fen.mainloop()