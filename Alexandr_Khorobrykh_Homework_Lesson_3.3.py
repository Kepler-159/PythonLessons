'''
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

Подумайте: полезен ли будет вам оператор распаковки? Как поступить,
если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

'''
name_staff = "Иван", "Мария", "Петр", "Илья", "Сергей"
name_staff_letter=[]
same_capital_letters={}


def thesaurus(name_staff):
    def same_capital_letters_sch(name_staff):
        return name_staff.startswith(my_names)
    for i in name_staff:
        name_staff_letter.append(name_staff[name_staff.index(i)][:1])
        my_names=name_staff[name_staff.index(i)][:1]
        name_staff_test = list(filter(same_capital_letters_sch, name_staff))
        same_capital_letters[my_names] = name_staff_test
    return same_capital_letters


print('***', thesaurus(name_staff))



'''
*(вместо задачи 3) Написать функцию thesaurus_adv(), 
принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, 
в котором ключи — первые буквы фамилий, а значения — словари, 
реализованные по схеме предыдущего задания и содержащие записи, 
в которых фамилия начинается с соответствующей буквы. 

'''

