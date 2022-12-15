#4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна.

import random

mas = []
sum = 0
mas = [random.randint(1,100) for i in range(1,10)]

print('Список случайных чисел: %s' % mas)

for i in mas: 

    if (i%2) == 0:

        sum += i

print('Сумма четных элементов = %s' % sum)