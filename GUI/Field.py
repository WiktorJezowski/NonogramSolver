from tkinter import *
from tkinter import messagebox
from Worktools.Solver import Solver


def listToString(row, separator):
    text = ""
    for x in row:
        text += separator + str(x)
    return text

def get_label_text(list):
    if list == []:
        return ""
    text = str(list[0])
    for i in range(1, len(list)):
        text += " " + str(list[i])
    return text

class Field:
    def __init__(self, master, n, m, rows, columns, back, toDataPassing):
        self.back = back
        self.toDataPassing = toDataPassing

        self.frame = Frame(master)
        self.frame.pack()
        self.frame.grid_propagate(False)
        self.solver = Solver(n, m, rows, columns)

        self.rows_number = n
        self.columns_number = m

        self.rows_data = rows
        self.columns_data = columns
        self.rows = []
        self.columns = []

        self.rows_labels = []
        for i in range(n):
            label = Label(self.frame, text=listToString(rows[i], "     "))
            self.rows_labels.append(label)
            label.grid(row=2 + i, column=0, sticky=E, columnspan=2)

        self.columns_labels = []
        for i in range(m):
            label = Label(self.frame, text=listToString(columns[i], "\n"))
            self.columns_labels.append(label)
            label.grid(row=0, column=2 + i, sticky=S, rowspan=2)

        self.field = []
        for i in range(n):
            self.field.append([])
            for j in range(m):
                lev = Label(self.frame, border=1, relief="groove", background="light grey", width=2)
                lev.grid(row=2 + i, column=2 + j)
                self.field[i].append(lev)

        self.back_button = Button(self.frame, text="Powrót", command=self.back_to_source_choice, width=10,
                                  background="light gray", relief=RAISED)
        self.back_button.grid(row=0, column=0, sticky=S)
        self.toDataPassing_button = Button(self.frame, text="Popraw dane", command=self.to_data_passing, width=10,
                                           background="light gray", relief=RAISED)
        self.toDataPassing_button.grid(row=0, column=1, sticky=S)
        self.solve_button = Button(self.frame, text="Rozwiąż", command=self.solve, width=21, background="light blue",
                                   relief=RAISED, cursor="heart")
        self.solve_button.grid(row=1, column=0, columnspan=2, sticky=N)

        self.frame.grid_propagate(True)

    def solve(self):
        code = 0
        while code == 0:
            code = self.step()
        if code == 1:
            return True
        else:
            messagebox.showerror("Błędna plansza", "Podana plansza nie ma rozwiązania!\n"
                                                   "Możesz sprawdzić dane wracając do poprzedniego okna "
                                                   "za pomocą opcji Popraw dane.")
            return False

    def step(self):
        new_w = []
        new_b = []
        new_g = []
        code = self.solver.analize_one(new_w, new_b, new_g)
        for x in new_b:
            self.mark(x[0], x[1], "black")
        for x in new_w:
            self.mark(x[0], x[1], "white")
        for x in new_g:
            self.mark(x[0], x[1], "light grey")
        return code

    def mark(self, i, j, color):
        self.field[i][j].config(background=color)

    def back_to_source_choice(self):
        self.frame.destroy()
        self.back()

    def to_data_passing(self):
        self.frame.destroy()
        rows = []
        for x in self.rows_data:
            rows.append(get_label_text(x))
        columns = []
        for x in self.columns_data:
            columns.append(get_label_text(x))
        self.toDataPassing(self.rows_number, self.columns_number, rows, columns)