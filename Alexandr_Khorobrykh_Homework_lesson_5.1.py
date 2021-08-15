'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
1
#>>> next(odd_to_15)
3
...
#>>> next(odd_to_15)
15
#>>> next(odd_to_15)
#...StopIteration...
'''

n = int(input("Введите число n:" ))

def numbers_generator (num):
    for i in range(num+1):
        if i%2 !=0:
            yield i

nums_gen = numbers_generator(n)
i=0
while i!=n:
    print('next(n): ',next(nums_gen))
    i+=1

#-------------------------------------------------------------------------------------------------------------------
'''
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''

n = int(input("Введите число n:" ))
nums_gen = (x for x in range(n+1) if x%2 !=0)
i=0
while i!=n:                                
    print('next(n): ',next(nums_gen))
    i+=1

