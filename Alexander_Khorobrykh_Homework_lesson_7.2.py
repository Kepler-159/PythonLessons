'''
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации,
библиотеки использовать нельзя.
'''


import os
import pathlib
from pathlib import Path


print(os.getcwd())
# Файл с расширением yaml не читается - не могу понять почему?
with open('Lesson_7_2_config.txt','r') as f:
    my_list = f.readlines()
    # определяю название папок и файлов
    for i in my_list:
        my_a_rf = i.rfind('-')+1
        if i.count(' ') == 0:
            my_project_name = i[my_a_rf:]
            # .rstrip() удаляет любой пробел в конце строки
            my_project_name = my_project_name.rstrip()
            my_path_project_name = os.path.join(os.getcwd(), my_project_name)
            if not os.path.exists(my_path_project_name):
                os.mkdir(my_path_project_name)

        elif i.count(' ') == 3:
            my_project_folder = i[my_a_rf:]
            my_project_folder=my_project_folder.rstrip()
            j=os.path.join(my_path_project_name, my_project_folder)
            if not os.path.exists(j):
                # if not Path(j).is_dir:
                #     os.mkdir(j)
                # else:
                if not os.path.isfile(j):
                    os.mkdir(j)
                else:
                    with open(j,'w') as f:
                        pass

        elif i.count(' ') == 5:
            my_project_folder_f = i[my_a_rf:]
            my_project_folder_f = my_project_folder_f.rstrip()
            j_f = os.path.join(j, my_project_folder_f)
            if not os.path.exists(j_f):
                if not os.path.isfile(j_f):
                    os.mkdir(j_f)
                else:
                    with open(j_f, 'w') as f:
                        pass

        elif i.count(' ') == 8:
            my_project_folder_f_f = i[my_a_rf:]
            my_project_folder_f_f = my_project_folder_f_f.rstrip()
            j_f_f=os.path.join(j_f, my_project_folder_f_f)
            if not os.path.exists(j_f_f):
                if not os.path.isfile(j_f_f):
                    os.mkdir(j_f_f)
                else:
                    with open(j_f_f, 'w') as f:
                        pass

        elif i.count(' ') == 11:
            my_project_folder_f_f_f = i[my_a_rf:]
            my_project_folder_f_f_f = my_project_folder_f_f_f.rstrip()
            j_f_f_f = os.path.join(j_f_f, my_project_folder_f_f_f)
            if not os.path.exists(j_f_f_f):
                if not os.path.isfile(j_f_f_f):
                    os.mkdir(j_f_f_f)
                else:
                    with open(j_f_f_f, 'w') as f:
                        pass


    # dir_path = [os.makedirs(os.path.join(, i)) for i in my_list if
    #             not os.path.exists(os.path.join( i))]

    pass

"""
вместо файлов создаются папки!! 
оптимизировать!!

"""




















