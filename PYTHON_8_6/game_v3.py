from game_v2 import score_game

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0   # счетчик попыток
    predict_number_min = 1  # нижняя граница поиска числа
    predict_number_max = 101  # верхняя граница поиска числа
    
    while True:
        count+=1
        
        predict_number = (predict_number_max + predict_number_min)//2

        if number > predict_number:
            predict_number_min = predict_number  # смещение нижней границы поиска числа

        elif number < predict_number:
            predict_number_max = predict_number  # смещение верхней границы поиска числа

        else:
            break

    return count


score_game(game_core_v3)