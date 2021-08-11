'''
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно
запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str,
решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

import requests

#   код провеки состояния
from requests.exceptions import HTTPError
for url in ['http://www.cbr.ru/scripts/XML_daily.asp']:
        try:
                response = requests.get(url)
                # если ответ успешен, исключения задействованы не будут
                response.raise_for_status()
        except HTTPError as http_err:
                print (f'HTTP error occurred: {http_err}')
        except Exception as err:
                print(f'Other error occurred: {err}')
        else:
                print('Success')

def currency_rates (cod_currency):
        if len(cod_currency) == 3 and cod_currency.isalpha() == True:
                char_code = response.text.find(cod_currency)
                char_code_str = response.text[char_code:char_code + 92]  # сокращаю текст
                nominal_code = char_code_str[0:3]
                char_code_str = char_code_str.split('>' '<')
                nominal_code_value = int(char_code_str[1][8:-9])
                value_code_value = char_code_str[3][6:-7]
                value_code_value_N1,value_code_value_N2=value_code_value.split(',')
                value_code_value_N3 = (float(value_code_value_N1+"."+value_code_value_N2))
                name_code = char_code_str[2][5:-6]
                #print(f'{nominal_code_value} {name_code} = {value_code_value_N3}')
                return nominal_code_value, name_code, value_code_value_N3
        else:
                return #None

response=requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
#print(response)
#print(response.status_code)
#print(response.content) #доступ к чистым байтам ответного пейлоада, то есть к любым данным в теле запроса.
#print(response.text) #конвертировать полученную информацию в строку в кодировке UTF-8. response делает это при помощи .text.
#Декодирование байтов в строку требует наличия определенной модели кодировки.
#умолчанию requests попытается узнать текущую кодировку, ориентируясь по заголовкам HTTP.
#Указать необходимую кодировку можно при помощи добавления .encoding перед .text.
#response.encoding = 'utf8' ####
#print(response.text) ##########
#response.json()
# print(response.headers) # .headers возвращает словарь, что позволяет получить доступ к значению заголовка HTTP по ключу.
# print(response.headers['Pragma'])

cod_currency = input('Введите код валюты (например, USD, EUR, GBP, ...): ')
if cod_currency.islower()==True:
        cod_currency=cod_currency.upper() # преобразованными в верхний регистр
currency_rates(cod_currency)
print (currency_rates(cod_currency))

#НЕ РАБОТАЕТ:
#nominal_code_value=[int(i) for i in char_code_str.split() if i.isdigit()]
#print(nominal_code_value)


