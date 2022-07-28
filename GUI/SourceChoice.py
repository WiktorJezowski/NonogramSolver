from tkinter import *

class SourceChoice:
    def __init__(self, master, toFileReader, toPassByUser):
        self.toFileReader = toFileReader
        self.toPassByUser = toPassByUser

        self.frame = Frame(master)
        self.frame.pack()

        self.info = Label(self.frame, text="Wybierz sposób wprowadzania danych", height=4)
        self.info.grid(row=0, column=0)

        self.button1 = Button(self.frame, text="Dane z pliku", command=self.fromFile, width=30, height=4,
                              relief=RAISED, background="light gray")
        self.button1.grid(row=1, column=0)

        self.button2 = Button(self.frame, text="Wprowaź dane ręcznie", command=self.byUser, width=30, height=4,
                              relief=RAISED, background="light gray")
        self.button2.grid(row=2, column=0)

    def fromFile(self):
        self.frame.destroy()
        self.toFileReader()

    def byUser(self):
        self.frame.destroy()
        self.toPassByUser()