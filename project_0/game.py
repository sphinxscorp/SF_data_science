"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def optimal_predict(number: int = 1) -> int:
    """Угадываем число меньше чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min = 1
    max = 101

    number = np.random.randint(min, max)

    count = 0

    while True:
        count+=1
        mid = round((min+max) / 2)
    
        if mid > number:
            max = mid
    
        elif mid < number:
            min = mid

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    return count


def score_game(optimal_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        optimal_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(optimal_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(optimal_predict)