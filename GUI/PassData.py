from tkinter import *
from tkinter import messagebox


def check_and_get_blacks(text, max_space):
    data = text.split()
    sum_black = 0
    blacks = []
    for x in data:
        if x.isdigit() and x[0] != '0':
            number = int(x)
            blacks.append(number)
            sum_black += number
        else:
            return -1, []
    if sum_black + len(blacks) - 1 > max_space:
        return -2, []
    return sum_black, blacks


class PassData:
    def __init__(self, master, n, m, back, toField, rows, columns):
        self.back = back;
        self.toField = toField

        self.frame = Frame(master)
        self.frame.pack()

        self.rows_number = n
        self.columns_number = m
        self.rows_given = rows
        self.columns_given = columns

        self.info = Label(self.frame, text="Podaj dane wierszy i kolumn\n"
                                           "(ciąg liczb całkowitych dodatnich oddzielonych spacją)", height=2)
        self.info.grid(row=0, column=1, columnspan=3)

        self.rows = []
        self.rows_labels = []
        self.columns = []
        self.columns_labels = []

        self.columns_info = Label(self.frame, text="Kolumny", height=2)
        self.columns_info.grid(row=1, column=2, columnspan=2)

        self.rows_info = Label(self.frame, text="Wiersze", height=2)
        self.rows_info.grid(row=1, column=0, columnspan=2)

        self.frame_canvas = Frame(self.frame)
        self.frame_canvas.grid(row=2, column=0, sticky='N', columnspan=4)
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        self.frame_canvas.grid_propagate(False)

        self.canvas = Canvas(self.frame_canvas)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.frame_in = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_in, anchor=N)

        self.vsb = Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)

        for i in range(self.columns_number):
            self.columns_labels.append(Label(self.frame_in, text=f"\tkolumna {str(i + 1)}    "))
            if self.columns_given is None:
                self.columns.append(Entry(self.frame_in, width=30))
            else:
                entry = Entry(self.frame_in, width=30)
                entry.insert(0, self.columns_given[i])
                self.columns.append(entry)
            self.columns_labels[i].grid(row=i, column=2)
            self.columns[i].grid(row=i, column=3)

        for i in range(self.rows_number):
            self.rows_labels.append(Label(self.frame_in, text=f"wiersz {str(i + 1)}    "))
            if self.rows_given is None:
                self.rows.append(Entry(self.frame_in, width=30))
            else:
                entry = Entry(self.frame_in, width=30)
                entry.insert(0, self.rows_given[i])
                self.rows.append(entry)
            self.rows_labels[i].grid(row=i, column=0)
            self.rows[i].grid(row=i, column=1)

        self.frame_in.update_idletasks()

        height = (self.rows[0].winfo_height() + 2) * min(max(self.rows_number, self.columns_number), 20)
        width = 15 + self.rows[0].winfo_width() + self.rows_labels[0].winfo_width() + \
                self.columns_labels[0].winfo_width() + self.columns[0].winfo_width() + self.vsb.winfo_width()
        self.frame_canvas.config(height=height, width=width)

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.compute = Button(self.frame, text="Rozpocznij", command=self.check_and_compute, height=2, width=25,
                              cursor="heart", background="light blue", relief=RAISED)
        self.compute.grid(row=3, column=0, columnspan=4)

        self.back_button = Button(self.frame, text="Powrót", command=self.back_to_source_choice, height=2,
                                  relief=RAISED, background="light gray")
        self.back_button.grid(row=0, column=0, sticky=W)

    def check_and_compute(self):
        columns = []
        rows = []
        blacks_in_raws = 0
        blacks_in_columns = 0

        for i in range(self.columns_number):
            blacks, column = check_and_get_blacks(self.columns[i].get(), self.rows_number)
            if blacks == -1:
                messagebox.showerror("Błąd", f"Podano błędną ciąg w kolumnie {i + 1}\n(wpisz ciąg liczb całkowitych "
                                             f"dodatnich oddzielonych spacją)")
                return
            elif blacks == -2:
                messagebox.showerror("Błąd", f"Podany ciąg nie zmieści się w kolumnie {i + 1}")
                return
            else:
                blacks_in_columns += blacks
                columns.append(column)

        for i in range(self.rows_number):
            blacks, row = check_and_get_blacks(self.rows[i].get(), self.columns_number)
            if blacks == -1:
                messagebox.showerror("Błąd", f"Podano błędną ciąg w wierszu {i + 1}\n(wpisz ciąg liczb całkowitych "
                                             f"dodatnich oddzielonych spacją)")
                return
            elif blacks == -2:
                messagebox.showerror("Błąd", f"Podany ciąg nie zmieści się w wierszu {i + 1}")
                return
            else:
                blacks_in_raws += blacks
                rows.append(row)

        if blacks_in_raws != blacks_in_columns:
            messagebox.showerror("Błąd", f"Liczba czarnych pól w wierszach i kolumnach nie zgadza się\n"
                                         f"W wierszach jest: {blacks_in_raws}\nW kolumnach jest: {blacks_in_columns}")
        else:
            self.frame.destroy()
            self.toField(self.rows_number, self.columns_number, rows, columns)

    def back_to_source_choice(self):
        self.frame.destroy()
        self.back()