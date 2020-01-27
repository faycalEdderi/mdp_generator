import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("@logo.xbm")
window.config(background='#545A59')

# frame principale
frame = Frame(window, bg='#545A59')

#creation d'image
width = 300
height = 300
image = PhotoImage(file="password.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="#545A59", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creation d'une sous boite
right_frame = Frame(frame, bg='#545A59')

#creation d'un titre
label_title=Label(
    right_frame,
    text="Mot de passe",
    font=("Helvetica", 20),
    bg='#545A59',
    fg='white'
)
label_title.pack()

#creation d'un input
password_entry=Entry(
    right_frame,
    font=("Helvetica", 20),
    bg='#545A59',
    fg='white'
)
password_entry.pack()

#creation du bouton

button_generator=Button(
    right_frame,
    text="Générer",
    font=("Courrier", 15),
    bg='white',
    fg='black',
    command=generate_password
)
button_generator.pack(pady=25, fill = X)

# on place la sous boite a rite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)
# afficher frame
frame.pack(expand=YES)

# barre de menu
menu_bar = Menu(window)
# creation du menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer fenetre menu
window.config(menu=menu_bar)


window.mainloop()