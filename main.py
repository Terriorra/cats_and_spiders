import os

from function import print_text
from function import clear_var
from function import print_door

from function import about
from function import LINE_LEN
from function import door_3
from function import answers
from function import dict_score

# Количество попыток
count = 10

# Количество попыток
right = 0


def set_text():
    text_head = ['Для прохождения требуется правильно ответить десять раз', f'Осталось решить {10 - quest_i} задач.']
    return text_head


def set_about():
    text_about_pr = about.copy()

    door1, door2, door_true, answer = clear_var()

    text_about_pr.append(door_true)

    text_about_pr.append('')

    text_about_pr.append('Вот эти надписи:')
    text_about_pr.append(f'1. {door1.sentence}')
    text_about_pr.append(f'2. {door2.sentence}')

    return text_about_pr, door1, door2, answer


for quest_i in range(count):

    os.system("CLS")

    text = print_text(set_text(), LINE_LEN)

    text_about, door_1, door_2, ans = set_about()

    text += print_text(text_about, LINE_LEN)

    text += print_text(answers, LINE_LEN)

    for i in zip(text, print_door(door_3, door_3)):
        print(i[0], i[1])

    gamer_ans = input('Введите ответ: ')

    if str(ans) == gamer_ans:
        a = 'Правильно!'
        right += 1
    else:
        a = 'Не правильно.'

    os.system("CLS")

    text = print_text(set_text(), LINE_LEN)
    text += print_text(text_about, LINE_LEN)
    text += print_text(answers, LINE_LEN)

    for i in zip(text, print_door(door_1, door_2)):
        print(i[0], i[1])

    print('\n' + a)
    print('\n' + 'Введите ответ: ' + gamer_ans)

    gamer_ans = input('Нажми enter для продолжения...')

print('')

print('Тренировка пройдена')

print(f'Решено {right} из 10 правильно. Твоя оценка.')

print()

for i in dict_score[round(right * 5 / count)]:
    print(i)

print()

gamer_ans = input('Нажми enter для продолжения...')
