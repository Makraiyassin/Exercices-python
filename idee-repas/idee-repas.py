from  tkinter import *
import string
from random import choice
import os

def generate_meals():
    if os.path.exists("meals.txt"):
        with open("meals.txt","r+") as file:
            meals_list= file.readlines()
            meals_entry.delete(0,END)
            meals_entry.insert(0,choice(meals_list))

            file.close()
    else:
        with open("meals.txt","w+") as file:
            meals_list = ["Poivron farci\n","Spagheti bolognese\n","Nouilles sautees\n","Burger frite\n","Pizza\n","Lasagne\n"]
            file.write(meals_list)
            file.close()

        with open("meals.txt","r+") as file:
            meals_list= file.readlines()
            meals_entry.delete(0,END)
            meals_entry.insert(0,choice(meals_list))

            file.close()


#créer une fenetre

window = Tk()
window.title("Idées repas")
window.iconbitmap("logo.ico")
window.geometry("730x480")
window.minsize(730,360)
window.config(background="#bdd8ef")

#variables:
width = 300
height = 300
background="#bdd8ef"

#créer le frame principal
frame = Frame(window, bg=background)

#créer une image

image = PhotoImage(file="bar.png").zoom(15).subsample(32)

canvas = Canvas(frame, width=width, height=height, bg=background, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite
right_frame = Frame(frame,bg=background)


#titre:
label_title = Label(right_frame, text = "Pas d'idée repas pour aujourd'hui?", font=("Helvetica", 20), bg=background, fg="#13334f")
label_title.pack()

#input:
meals_entry= Entry(right_frame, font=("Helvetica", 20), bg=background, fg="#13334f")
meals_entry.pack(fill=X)

#bouton:
generate = Button(right_frame, text = "Clique ici ! ;)", font=("Helvetica", 20), bg=background, fg="#13334f", command=generate_meals)
generate.pack(fill=X)

#on place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

#afficher frame
frame.pack(expand=YES)

#créer navbar
menu_bar = Menu(window)

# créer un premier menu
file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label="Nouveau",command=generate_meals)
file_menu.add_command(label="Quitter",command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configurer la fenetre pour ajouter cette navbar
window.config(menu=menu_bar)

#ouvrir la fenetre
window.mainloop()




