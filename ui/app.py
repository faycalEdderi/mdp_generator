from tkinter import *
import webbrowser


def open_my_site():
    webbrowser.open_new("http://fayc.fr/")

#création d'une fenetre
window = Tk()


#modification fenetre
window.title("Application")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("@logo.xbm")
window.config(background='#71D6C9')

#creation de frame
frame = Frame(window, bg='#71D6C9')

#ajout de texte
label_title = Label(
    frame,
    text ="Bienvenue sur mon application",
    font=("Courrier", 35),
    bg='#71D6C9',
    fg="white"
)
#ajouter un second texte
label_subtitle = Label(
    frame,
    text ="Developpé par Fayçal",
    font=("Courrier", 20),
    bg='#71D6C9',
    fg="white"
)
#ajout des textes
label_title.pack()
label_subtitle.pack()

# ajout d'un bouton
yt_button = Button(
    frame,
    text="Visiter fayc.fr",
    font=("Courrier", 20),
    bg='white',
    fg="#71D6C9",
    command = open_my_site
)
yt_button.pack(pady=25, fill=X)

#ajouter frame
frame.pack(expand=YES)

#afficher une fenetre
window.mainloop()