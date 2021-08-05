'''
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

'''

#price_list_products = input('Введите цены на 10 товаров, например [57.8, 46.51, 97, ...]: ')
price_list_products = [57.8, 46.51, 97, 7, 58.4, 34, 5, 1, 34.4, 89, 5.19, 69]
print(id(price_list_products))
price_list_products_format=[]
#Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).

for i in price_list_products:

    if type(price_list_products[price_list_products.index(i)]) == float:
        meaning = str(price_list_products[price_list_products.index(i)])
        r, kk=meaning.split('.')
        r=int(r)
        kk=int(kk)
        if r <=9:
            if kk <= 9:
                price_list_products_format.append(f'«0{r} руб 0{kk} коп»')
            else:
                price_list_products_format.append(f'«0{r} руб {kk} коп»')
        else:
            if kk<=9:

                price_list_products_format.append(f'«{r} руб 0{kk} коп»')

            else:
                price_list_products_format.append (f'«{r} руб {kk} коп»')

    elif type(price_list_products[price_list_products.index(i)]) == int:
        r = price_list_products[price_list_products.index(i)]
        kk = 00
        if r <= 9:

            price_list_products_format.append(f'«0{r} руб 0{kk} коп»')
        else:

            price_list_products_format.append(f'«{r} руб 0{kk} коп»')




price_list_products = [57.8, 46.51, 97, 7]
print(price_list_products_format)
print(id(price_list_products))
#Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
price_list_products_format.sort()
print(price_list_products_format)
print(id(price_list_products))

#Создать новый список, содержащий те же цены, но отсортированные по убыванию.

price_list_products_format = price_list_products_format[::-1]
print(price_list_products_format)
print(id(price_list_products_format))

#Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print('Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?')
print(price_list_products_format[:5])