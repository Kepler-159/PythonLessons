'''
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#>>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
'''

def num_translate(key):
    print(numerals_dict.get(key))

'''Доработать предыдущую функцию в num_translate_adv()'''
def num_translate_adv(key):
    if (my_num[:1].isupper()) == True:
        for i in numerals_eng:
            numerals_eng[numerals_eng.index(i)] = numerals_eng[numerals_eng.index(i)].capitalize()
        for i in numerals_rus:
            numerals_rus[numerals_rus.index(i)] = numerals_rus[numerals_rus.index(i)].capitalize()

#-----------------------------------------------------------------------------
print('-----------------------------------------------------------------------------')

my_num = input('Print numeric in 0  fo 10: ')
#my_num = 'Three'
numerals_eng = ['one','two','three','four','five','six','seven','eight','nine','ten']
numerals_rus = ['один','два','три','четыре','пять','шесть','семь','восемь','девять','десять']
''' 
# Вариант 2: def num_translate_adv(key)
if (my_num[:1].isupper()) == True:
    print(my_num[:1].isupper())
    numerals_eng = list(map(str.capitalize, numerals_eng))
    numerals_rus = list(map(str.capitalize, numerals_rus))

'''
num_translate_adv(my_num)
numerals_dict = dict(zip(numerals_eng,numerals_rus))
num_translate(my_num)
