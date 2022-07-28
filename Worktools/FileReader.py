from tkinter import messagebox

def read(path):
    try:
        f = open(path, "r")

        rows = []
        columns = []

        line = f.readline()[:-1]
        if line:
            if line.isdigit() and line[0] != '0':
                n = int(line)
            else:
                messagebox.showerror("Błędne dane", "Podana w pliku liczba wierszy jest niepoprawna")
                return -1, -1, [], []
        else:
            messagebox.showerror("Błędne dane", "Wskazany plik nie posiada informacji o liczbie wierszy")
            return -1, -1, [], []
        line = f.readline()[:-1]
        if line:
            if line.isdigit() and line[0] != '0':
                m = int(line)
            else:
                messagebox.showerror("Błędne dane", "Podana w pliku liczba kolumn jest niepoprawna")
                return -1, -1, [], []
        else:
            messagebox.showerror("Błędne dane", "Wskazany plik nie posiada informacji o liczbie kolumn")
            return -1, -1, [], []

        for i in range(n):
            next = f.readline()
            if next:
                rows.append(next)
            else:
                messagebox.showerror("Błędne dane", "Wskazany plik ma za mało linii na wskazaną długość")
                return -1, -1, [], []
        for i in range(m):
            next = f.readline()
            if next:
                columns.append(next)
            else:
                messagebox.showerror("Błędne dane", "Wskazany plik ma za mało linii na wskazaną długość")
                return -1, -1, [], []

        f.close()
        return n, m, rows, columns

    except IOError:
        messagebox.showerror("Brak pliku", "Podana ścieżka jest błędna")
        return -1, -1, [], []