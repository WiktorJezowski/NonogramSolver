from tkinter import *
from tkinter import messagebox

class SizeChoice:
    def __init__(self, master, back, toPassData):
        self.back = back
        self.toPassData = toPassData

        self.frame = Frame(master)
        self.frame.pack()

        self.info = Label(self.frame, text="Podaj liczbę wierszy i kolumn", height=2)
        self.info.grid(row=0, column=1, columnspan=3, sticky=E)

        self.size_x_label = Label(self.frame, text="Liczba wierszy: ", height=2)
        self.size_y_label = Label(self.frame, text="Liczba kolumn: ", height=2)
        self.size_x_label.grid(row=1, column=0, columnspan=2)
        self.size_y_label.grid(row=2, column=0, columnspan=2)

        self.size_x_entry = Entry(self.frame)
        self.size_y_entry = Entry(self.frame)
        self.size_x_entry.grid(row=1, column=2, columnspan=2)
        self.size_y_entry.grid(row=2, column=2, columnspan=2)

        self.check = Button(self.frame, text="Zatwierdź", command=self.check_size, height=2,
                            background="light gray", relief=RAISED)
        self.check.grid(row=3, column=0, columnspan=4)

        self.back_buttom = Button(self.frame, text="Powrót", command=self.back_to_source_choice, height=2,
                                  background="light gray", relief=RAISED)
        self.back_buttom.grid(row=0, column=0, sticky=W)

    def check_size(self):
        x_size = self.size_x_entry.get()
        y_size = self.size_y_entry.get()
        if x_size.isdigit() and x_size[0] != '0':
            if y_size.isdigit() and y_size[0] != '0':
                self.frame.destroy()
                self.toPassData(int(x_size), int(y_size))
            else:
                messagebox.showerror("Błąd", "Podano błędną liczbę kolumn!\n(liczba kolumn musi być liczbą całkowitą "
                                             "dodatnią)")
        else:
            messagebox.showerror("Błąd", "Podano błędną liczbę wierszy!\n(liczba wierszy musi być liczbą całkowitą "
                                         "dodatnią)")

    def back_to_source_choice(self):
        self.frame.destroy()
        self.back()