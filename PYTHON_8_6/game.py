"""Игра 'Угадай число'"""

import numpy as np

# Загадываем число
number = np.random.randint(1,101) 

# Количество, необходимое для угадывания числа
count = 0

while True:
    count += 1
    predict_number = int(input('Введите число от 1 до 100: '))
    
    if predict_number > number:
        print('Введенное число больше загаданного!')
    
    elif predict_number < number:
        print('Введенное число меньше загаданного!')
        
    # Условие выигрыша
    else:
        print('Вы угадали! Загаданное число {0}. Вам понадобилось {1} попыток'.format(number, count))
        break
            
        
    


