"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def optimal_predict_random(number: int = 1) -> int:
    """Компьютер загадывает и угадывает число меньше чем за 20 попыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    number = np.random.randint(1, 101) #рандомайзер для загадывания чисел компьютером
           
    min = 1
    max = 101
    count = 0
    
    mid = (min + max) // 2
    while number != mid:
        count += 1
        if number > mid:
            min = mid
        else:
            max = mid
        mid = (min + max) // 2
    print(f'Загаданное число {number} угадано за {count} попыток') #вывод результата для самостоятельной работы функции
    return count


def optimal_predict(number: int = 1) -> int:
    """Угадываем число меньше чем за 20 попыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
           
    min = 1
    max = 101
    count = 0
    
    mid = (min + max) // 2
    while number != mid:
        count += 1
        if number > mid:
            min = mid
        else:
            max = mid
        mid = (min + max) // 2
    return count


def score_game(optimal_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        optimal_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(optimal_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == '__main__':
    score_game(optimal_predict)