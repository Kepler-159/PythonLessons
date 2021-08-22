'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

'''

import os
import yaml


my_values = ['settings','mainapp','adminapp','authapp']
my_keys = 'my_project'
my_dict = {my_keys : my_values}

##_____________________________________________________________________________________
# Создаем папку my_project и вложенные папки settings, mainapp, adminapp, authapp
dir_path = [os.makedirs(os.path.join(my_keys,i)) for i in my_values if not os.path.exists(os.path.join(my_keys,i))]

##--------------------------------------------------------------------------------------

print(os.path.join(os.path.abspath(os.getcwd()), my_keys))
my_path=os.path.join(os.path.abspath(os.getcwd()), my_keys)
for i in my_values:
    print(os.path.join(my_path,i))

# #__________________создаем файл

with open ('Lesson_7_1_config.yaml','w') as f:
    yaml.dump(my_path, f)
    for i in my_values:
        yaml.dump(os.path.join(my_path, i),f)
    pass













#
# folder = r'C:\Users\kukkr\PycharmProjects\Helloworld\my_project'
# # py_files=[item for item in os.listdir(r'C:\Users\kukkr\PycharmProjects\Helloworld\my_project')]
# django_dirs=[item
#              for item in os.listdir(folder)
#              if os.path.isdir(os.path.join(folder,item))]
# django_dirs_yaml = print('*',django_dirs)
#
# with open('Lesson_7_1_config.yaml','w') as f:
#     print('*')
#     document = yaml.dump(django_dirs_yaml, f)
#     print('**',document)
#     pass
#
# with open('Lesson_7_1_config.yaml','r') as f:
#     document = yaml.full_load(f)
#     print(document)
#     # for item, doc in document.items():
#     #     print(item, ":", doc)
#     pass
#



