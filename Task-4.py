'''
Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
'''

print('Программа найдет сумму чётных чисел, расположенных между числами от 1 до N включительно')

while True:
    lim = int(input('Введите число: '))

    sum = 0
    for i in range(2, lim + 1, 2):
        sum += i
    print(f'Сумма четных чисел от 1 до {lim} составляет {sum}')

    if lim <= 0:
        print('Вы ввели что-то не то... Try again')