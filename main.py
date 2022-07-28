from tkinter import *
from GUI.SourceChoice import SourceChoice
from GUI.SizeChoice import SizeChoice
from GUI.FileChoice import FileChoice
from GUI.PassData import PassData
from GUI.Field import Field


class Controler:
    def __init__(self):
        self.root = Tk()
        self.sourceChoice()
        self.root.mainloop()

    def sourceChoice(self):
        self.root.title("Źródło")
        SourceChoice(self.root, self.readFromFile, self.sizeChoice)

    def sizeChoice(self):
        self.root.title("Rozmiar")
        SizeChoice(self.root, self.sourceChoice, self.passData)

    def passData(self, n, m, rows=None, columns=None):
        self.root.title("Wpisywanie danych")
        PassData(self.root, n, m, self.sourceChoice, self.field, rows, columns)

    def readFromFile(self):
        self.root.title("Czytanie z pliku")
        FileChoice(self.root, self.sourceChoice, self.passData)

    def field(self, n, m, rows, columns):
        self.root.title("Plansza")
        Field(self.root, n, m, rows, columns, self.sourceChoice, self.passData)

Controler()
