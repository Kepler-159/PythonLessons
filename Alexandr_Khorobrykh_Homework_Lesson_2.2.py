'''
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
'''


announced_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(announced_list))
'''
message = ''
for i in announced_list:
    message += i
    message += ' '
    print(type(i))
print (message)
'''

announced_list =announced_list[::-1]

for i in announced_list:
    #Проверяем состоит ли строка из цифр и состоит ли строка из цифр или букв
    if announced_list[announced_list.index(i)].isdigit() == True and announced_list[announced_list.index(i)].startswith('"') == False:
        #announced_list.insert(announced_list.index(i), '"')     # Вопрос: не пойму почему программа уходит бесконечный цикл?
        announced_list.insert(announced_list.index(i)+1, '"')
    elif announced_list[announced_list.index(i)].isdigit() == False and announced_list[announced_list.index(i)].startswith('+') == True:
        announced_list.insert(announced_list.index(i) + 1, '"')

announced_list =announced_list[::-1]

for i in announced_list:
    #Проверяем состоит ли строка из цифр и состоит ли строка из цифр или букв
    if announced_list[announced_list.index(i)].isdigit() == True and announced_list[announced_list.index(i)].startswith('"') == False:
        #announced_list.insert(announced_list.index(i), '"')
        announced_list.insert(announced_list.index(i)+1, '"')
        #дополняем нулём до двух целочисленных разрядов
        if len(i) == 1:
            announced_list[announced_list.index(i)] = '0'+i

    elif announced_list[announced_list.index(i)].isdigit() == False and announced_list[announced_list.index(i)].startswith('+') == True:
        announced_list.insert(announced_list.index(i) + 1, '"')

# Сформировать из обработанного списка строку:

message= ' '.join(announced_list)
print(message)



