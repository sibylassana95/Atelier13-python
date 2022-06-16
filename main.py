from tkinter import *
    
root = Tk()
root.geometry("300x150")
root.title("Bouton Quitter en Tkinter")

# création du bouton quitter
btn_quit = Button(root , text = "Fermer la fenêtre !" , command = quit)
btn_quit.place(x = 100 , y = 50)

root.mainloop()
