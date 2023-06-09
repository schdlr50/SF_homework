"""Итоговое задание"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def game_core_v3(numberZ: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    max = 101 # добавил границу, которую буду в последствие уменьшать для сокращения количества неверных ответов
    count = 0 # установил счетчик
    my_predict=np.random.randint(1,101)
    while numberZ != my_predict: # добавил основную функцию
        count += 1 # теперь при каждой новой попытке счетчик будет увеличиваться на 1
        if my_predict > numberZ: # добавил условие, если предполагаемое число больше загаданного 
            max = my_predict # если выполняется предыдущее условие то сужаем границы поиска
            my_predict = round(my_predict/2) # а так же присваемваем предполагаемому числу значение в два раза меньше предыдущего, и обязательно округляем его
        elif my_predict < numberZ: # добавил условие, если предполагаемое число меньше загаданного
            my_predict = round((my_predict+max)/2) # присваеваем предполагаемому числу среднеарифметическое значение его суммы и установленного максимума
    
    return count # возвращаем счетчик

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for random_predict: ', end='')
score_game(random_predict)

print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v2)

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)