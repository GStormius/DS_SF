"""
Игра 'Угадай число'
Компьютер сам угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Предплагаемое число
        
        if number == predict_number:
            break # Условие победы (выход из цикла)
        
    return count


def score_game(func: random_predict) -> int:
    """Среднее количество попыток, необходимое для определения загаданного числа. 1000 подходов

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали 1000 чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print('Алгоритм угадывает число в среднем за {0} попыток'.format(score))
    return score


if __name__ == "__main__":
    # Запускаем
    score_game(random_predict)