from tkinter import *
from random import randint


fenster = Tk()
fenster.title("Würfel")
fenster.geometry("90x180+800+350")
fenster.minsize(190, 160)
fenster.resizable(True, True)


def Zufall():
    zufallszahl = randint(text.get(), text2.get())
    lab.config(text=zufallszahl)


text = IntVar()
text2 = IntVar()

lab = Label(fenster, font=("Arial", 50), text="?", width=3)
lab.grid(row=0, column=1)


von = Entry(fenster, textvariable=text)
von.grid(row=1, column=1)

bis = Entry(fenster, textvariable=text2)
bis.grid(row=2, column=1)

Label(fenster, text="von").grid(row=1)
Label(fenster, text="bis").grid(row=2)


knopf = Button(fenster, text="Drück mich!", command=Zufall)
knopf.grid(row=3, column=1)

fenster.mainloop()
