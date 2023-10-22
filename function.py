import os
import sys

from random import choice

sign_hor = '═'
sign_vert = '║'
LINE_LEN = 70

about = '''Представь, что перед тобой две двери, ведущие в отдельные комнаты. Известно, что в каждой из этих комнат находится милая кошка или страшный паук.

Может быть так, что в обеих комнатах находятся кошки или в обеих комнатах находятся пауки. При этом в каждой из комнат всегда находится кто-то один. На каждой двери есть табличка с надписью.
'''.split('\n')

answers = '''Выбери правильный вариант ответа.

1. За обоими дверьми находятся пауки.
2. За первой дверью находится паук, а за второй кошка.
3. За первой дверью находится кошка, а за второй паук.
4. За обеими дверьми находятся кошки.'''.split('\n')

# Два варианта
verity = f'''Известно, что на обеих дверях написана, либо чистейшая истина, либо абсолютная ложь.
Известно, что одна дверь говорит чистую правду, а другая подло лжет.'''.split('\n')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path = resource_path('door_close.txt')
with open(path, 'r', encoding='utf-8') as f:
    door_close = f.read().split('\n')

path = resource_path('door_cat.txt')
with open(path, 'r', encoding='utf-8') as f:
    door_cat = f.read().split('\n')

path = resource_path('door_spider.txt')
with open(path, 'r', encoding='utf-8') as f:
    door_spider = f.read().split('\n')

path = resource_path('12345.txt')
with open(path, 'r', encoding='utf-8') as f:
    score = f.read().split('\n')

step = 6
k = 0

dict_score = {i: [] for i in range(1, 6)}
for i in range(1, 6):
    dict_score[i] = score[k:k + step]
    k += step

dict_score[0] = dict_score[1]


def print_text(text, len_string):
    new_s = [f" {(len_string - 2) * sign_hor} ", f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}"]

    for line in text:
        if len(line) + 4 < len_string:
            new_s.append(f"{sign_vert} {line}{(len_string - len(line) - 4) * ' '} {sign_vert}")
        else:
            new_s += cut_string(line, len_string)
    new_s.append(f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}")
    new_s.append(f" {(len_string - 2) * sign_hor} ")

    return new_s


def cut_string(text, len_string):
    s = []

    text = text.split(' ')
    lines = []
    now_string = ''
    for i in text:
        if len(now_string + ' ' + i) < len_string - 4:
            now_string += ' ' + i
        else:
            lines.append(now_string)
            now_string = i
    lines.append(now_string)

    for line in lines:
        s.append(f"{sign_vert} {line}{(len_string - 4 - len(line)) * ' '} {sign_vert}")

    return s


def what_door(num):
    match num:
        case 3:
            return door_close
        case 1:
            return door_cat
        case 0:
            return door_spider


def print_door(door1, door2):
    s = ['', '', f"{17 * ' '}1{34 * ' '}2"]

    for i, j in zip(door1.door, door2.door):
        s.append(i + j)
    s.append('')
    s.append('')
    s.append('')
    s.append('')
    s.append('')
    return s


class Door:
    def __init__(self, door_now, sentence):
        # дверь
        self.door = what_door(door_now)
        # высказывание
        self.sentence = sentence


door_3 = Door(3, '')


def clear_var():
    # выбор размещения
    var_choice = choice(range(len(options)))

    ant: int = 0

    # Двери
    door_choice = options[var_choice][0]

    # Вариант ответа
    match door_choice:
        case [0, 0]:
            ant = 1
        case [0, 1]:
            ant = 2
        case [1, 0]:
            ant = 3
        case [1, 1]:
            ant = 4

    # Дополнительное условие
    if options[var_choice][1][0] == options[var_choice][1][1]:
        true_full = verity[0]
    else:
        true_full = verity[1]

    # Высказывания
    sentence = choice(var_sent[var_choice])
    door1 = Door(door_choice[0], sentence[0])
    door2 = Door(door_choice[1], sentence[1])

    return door1, door2, true_full, ant


# все варианты размещения
# 0 - паук
# 1 - кошка
doors = [[0, 0], [0, 1], [1, 0], [1, 1]]

options = [
    [[0, 0], [0, 0]],
    [[0, 0], [0, 1]],
    [[0, 0], [1, 0]],
    [[0, 0], [1, 1]],
    [[0, 1], [0, 0]],
    [[0, 1], [0, 1]],
    [[0, 1], [1, 0]],
    [[0, 1], [1, 1]],
    [[1, 0], [0, 0]],
    [[1, 0], [0, 1]],
    [[1, 0], [1, 0]],
    [[1, 0], [1, 1]],
    [[1, 1], [0, 0]],
    [[1, 1], [0, 1]],
    [[1, 1], [1, 0]],
    [[1, 1], [1, 1]],
]

# возможные высказывания
statements = '''Кошки сидят в обеих комнатах.
Ни в одной из этих комнат нет кошки.
В другой комнате сидит кошка.
Кошка сидит в этой комнате.
По крайне мере в одной из этих комнат сидит кошка.
Пауки сидят в обеих комнатах.
Ни в одной из этих комнат нет паука.
В другой комнате сидит паук.
Паук сидит в этой комнате.
По крайне мере в одной из этих комнат сидит паук.
Кошка сидит только в этой комнате.
Паук сидит только в этой комнате.'''.split('\n')

# Размещения по высказываниям
cases = [
    [[3], [3]],
    [[0], [0]],
    [[1, 3], [2, 3]],
    [[2, 3], [1, 3]],
    [[1, 2, 3], [1, 2, 3]],
    [[0], [0]],
    [[3], [3]],
    [[0, 2], [0, 1]],
    [[0, 1], [0, 2]],
    [[0, 1, 2], [0, 1, 2]],
    [[2], [1]],
    [[1], [2]],
]

# Соединим высказывания с размещением
x = [(i, j) for i, j in zip(statements, cases)]


class Statement:
    def __init__(self, statement, door1, door2):
        self.statement = statement
        self.door1 = door1
        self.door2 = door2


door = []

for i, j in enumerate(x):
    door_1 = [doors[i] for i in j[1][0]]
    door_1 = [''.join([str(k) for k in i]) for i in door_1]

    door_1_not = {0, 1, 2, 3} - set(j[1][0])
    door_1_not = [doors[i] for i in door_1_not]
    door_1_not = [''.join([str(k) for k in i]) for i in door_1_not]

    door_2 = [doors[i] for i in j[1][1]]
    door_2 = [''.join([str(k) for k in i]) for i in door_2]

    door_2_not = {0, 1, 2, 3} - set(j[1][1])
    door_2_not = [doors[i] for i in door_2_not]
    door_2_not = [''.join([str(k) for k in i]) for i in door_2_not]

    door.append([j[0], [door_1_not, door_1], [door_2_not, door_2]])

sent = []

for i in options:
    var = ''.join([str(k) for k in i[0]])
    door_1 = []
    door_2 = []
    for dr in door:
        dr_1 = dr[1]
        if var in dr_1[i[1][0]]:
            door_1.append(dr)

        dr_2 = dr[2]
        if var in dr_2[i[1][1]]:
            door_2.append(dr)

    sent.append([door_1, door_2])

var_sent = []

for k in range(len(sent)):

    door_1 = sent[k][0]
    door_2 = sent[k][1]
    dr_tr = options[k][1]

    now = []

    for i in door_1:
        for j in door_2:
            if i != j:
                a = set(i[1][dr_tr[0]])
                b = set(j[2][dr_tr[1]])
                cond_1 = len(a.intersection(b)) == 1

                a = set(i[1][int(str(dr_tr[0]).translate(str.maketrans({'0': '1', '1': '0'})))])
                b = set(j[2][int(str(dr_tr[1]).translate(str.maketrans({'0': '1', '1': '0'})))])

                cond_2 = len(a.intersection(b)) != 1

                if cond_1 and cond_2:
                    now.append([i[0], j[0]])

    var_sent.append(now)
