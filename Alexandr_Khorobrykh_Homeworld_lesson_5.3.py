'''
Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести
последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''
print("вариант_1 ________________________________________________________________________________________________")
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Eka', 'ASD', 'Flor'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
def plus_gen(a,b):
    x = tuple(map(plus, a, b))
    for i in x:
        yield i

def plus(a,b):
    return a,b


while len(tutors) > len(klasses):
    klasses.append('None')
x = plus_gen (tutors, klasses)
i = 0
while i != len(tutors):
    print(f'next({i+1}): ', next(x))
    i += 1
#print(f'next({i+1}): ', next(x)) # StopIteration


#_____var2_____________________________________________________________________________
print("вариант_2 __________________________________________________________________________________________________")
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Eka', 'ASD', 'Flor'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def plus_gen(a,b):
    x = zip(a, b)
    for i in x:
        yield i


def plus(a,b):
    return a,b


while len(tutors) > len(klasses):
    klasses.append('None')
x = plus_gen (tutors, klasses)
i = 0
while i != len(tutors):
    print(f'next({i+1}): ', next(x))
    i += 1

######var3___________________________############_________________________________________________________
print("вариант_3 __________________________________________________________________________________________________")
a_b_test= (zip(tutors,klasses))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
print('***',list(next(a_b_test)))
