'''
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.

'''


from utils import *

'''
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

'''

if cod_currency.islower()==True:
        cod_currency=cod_currency.upper() # преобразованными в верхний регистр

currency_rates(cod_currency)
print (currency_rates(cod_currency))
