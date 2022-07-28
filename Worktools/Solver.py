from Worktools.MyQueue import MyQueue


def fit_left(line, data, line_size, data_size):
    start_indexes = []
    data_index = 0
    line_index = 0

    while data_index <= data_size:
        if data_index == data_size:
            if data_size == 0:
                if check_blacks(line, 0, line_size) == -1:
                    correct(line, data, line_size, data_size, start_indexes)
                    return True
                else:
                    return False
            else:
                black_index = check_blacks(line, line_index, line_size)
                if black_index == -1:
                    correct(line, data, line_size, data_size, start_indexes)
                    return True
                else:
                    data_index -= 1
                    start_indexes.pop()
                    line_index = black_index - data[data_index] + 1

        line_index = fit_this_left(line, line_size, line_index, data[data_index])
        if line_index == -1:
            return False
        elif data_index == 0:
            if check_blacks(line, 0, line_index) == -1:
                start_indexes.append(line_index)
                line_index += data[data_index] + 1
                data_index = 1
            else:
                return False
        else:
            black_index = check_blacks(line, start_indexes[data_index - 1] + data[data_index - 1], line_index)
            if black_index == -1:
                start_indexes.append(line_index)
                line_index += data[data_index] + 1
                data_index += 1
            else:
                start_indexes.pop()
                data_index -= 1
                line_index = black_index - data[data_index] + 1
    return False


def fit_right(line, data, line_size, data_size):
    line.reverse()
    data.reverse()
    answer = fit_left(line, data, line_size, data_size)
    line.reverse()
    data.reverse()
    return answer


def correct(line, data, line_size, data_size, start_indexes):
    prev = 0
    for i in range(data_size):
        for j in range(prev, start_indexes[i]):
            if line[j] == "pos_b":
                line[j] = "none"
            elif line[j] == "":
                line[j] = "pos_w"
        for j in range(start_indexes[i], start_indexes[i] + data[i]):
            if line[j] == "pos_w":
                line[j] = "none"
            elif line[j] == "":
                line[j] = "pos_b"
        prev = start_indexes[i] + data[i]
    for j in range(prev, line_size):
        if line[j] == "pos_b":
            line[j] = "none"
        elif line[j] == "":
            line[j] = "pos_w"


def check_blacks(line, start, end):
    for i in range(end - 1, start - 1, -1):
        if line[i] in ["old_b", "new_b"]:
            return i
    return -1


def fit_this_left(line, line_size, start, length):
    end = start + length
    if end > line_size:
        return -1
    for i in range(start, end):
        if line[i] in ["old_w", "new_w"]:
            return fit_this_left(line, line_size, i + 1, length)
    while end < line_size and line[end] in ["old_b", "new_b"]:
        end += 1
    return end - length


class Solver:
    def __init__(self, n, m, rows, columns):

        self.rows_number = n
        self.columns_number = m
        self.rows_data = rows
        self.columns_data = columns

        self.field = []
        for i in range(n):
            self.field.append([])
            for j in range(m):
                self.field[i].append(0)
        self.layer = 1
        self.guessed = []

        self.rows = []
        self.columns = []
        for i in range(n):
            self.rows.append([""] * m)
        for i in range(m):
            self.columns.append([""] * n)

        self.queue = MyQueue(n, m, full=True)

    def is_queue_empty(self):
        return self.queue.empty()

    def analize_one(self, new_w, new_b, new_g):
        if self.queue.empty():
            if self.is_finished():
                return 1
            else:
                self.guess(new_b)
                return 0
        else:
            x = self.queue.get()
            if self.analize(x, new_w, new_b, new_g):
                return 0
            else:
                return -1

    def guess(self, new_b):
        for i in range(self.rows_number):
            for j in range(self.columns_number):
                if self.field[i][j] == 0:
                    self.layer += 1
                    self.guessed.append((i, j))
                    self.queue.put(('r', i))
                    self.queue.put(('c', j))
                    self.update(i, j, new_b)
                    return True
        return False

    def fix_guessing(self, new_w, new_g):
        if self.layer == 1:
            return False
        x = self.guessed.pop()
        for i in range(self.rows_number):
            for j in range(self.columns_number):
                if abs(self.field[i][j]) == self.layer and not (i, j) == x:
                    self.update(i, j, new_g, color="gray")
        self.layer -= 1
        self.update(x[0], x[1], new_w, color="white")
        self.queue.clear()
        self.queue.put(('r', x[0]))
        self.queue.put(('c', x[1]))
        return True

    def is_finished(self):
        for i in range(self.rows_number):
            for j in range(self.columns_number):
                if self.field[i][j] == 0:
                    return False
        return True

    def update(self, row, column, new_tab, color="black"):
        if color == "black":
            self.field[row][column] = self.layer
            self.rows[row][column] = "old_b"
            self.columns[column][row] = "old_b"
        elif color == "white":
            self.field[row][column] = -self.layer
            self.rows[row][column] = "old_w"
            self.columns[column][row] = "old_w"
        else:
            self.field[row][column] = 0
            self.rows[row][column] = ""
            self.columns[column][row] = ""
        new_tab.append((row, column))

    def analize(self, x, new_w, new_b, new_g):
        if x[0] == 'r':
            line = self.rows[x[1]]
            data = self.rows_data[x[1]]
        else:
            line = self.columns[x[1]]
            data = self.columns_data[x[1]]

        line_size = len(line)
        data_size = len(data)

        if not fit_left(line, data, line_size, data_size):
            return self.fix_guessing(new_w, new_g)
        fit_right(line, data, line_size, data_size)

        for i in range(line_size):
            if line[i] == "pos_b":
                line[i] = "old_w"
                if fit_left(line, data, line_size, data_size):
                    line[i] = "none"
                else:
                    line[i] = "new_b"

        for i in range(line_size):
            if line[i] == "pos_w":
                line[i] = "old_b"
                if fit_left(line, data, line_size, data_size):
                    line[i] = "none"
                else:
                    line[i] = "new_w"

        for i in range(line_size):
            if line[i] == "none":
                line[i] = ""
            elif line[i] == "new_b":
                if x[0] == 'r':
                    self.update(x[1], i, new_b)
                    self.queue.put(('c', i))
                else:
                    self.update(i, x[1], new_b)
                    self.queue.put(('r', i))
            elif line[i] == "new_w":
                if x[0] == 'r':
                    self.update(x[1], i, new_w, "white")
                    self.queue.put(('c', i))
                else:
                    self.update(i, x[1], new_w, "white")
                    self.queue.put(('r', i))
        return True