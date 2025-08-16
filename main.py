'''
Задание
Программа на вход принимает строку и количество совпадений (N), подсчитать какие из них встречаются (N). 
Результат вывести на экран.
'''
repeat = True
while repeat:
    try:
        import os
        os.system('clear')  # Очистка консоли для Linux/Mac
    except ImportError:
        import platform
        if platform.system() == 'Windows':
            os.system('cls')  # Очистка консоли для Windows

    print("Программа подсчитывает количество совпадений символов в строке.")
    print("Введите строку и количество совпадений, которые нужно найти.")
    print("Результат будет выведен на экран.\n")

    # Получаем на вход строку
    input_string = input("Введите строку: ").lower()

    # Получаем на вход количство совпадений
    n = input("Введите количество совпадений: ")

    try:
        int(n)
    except ValueError:
        print("Ошибка: количество совпадений должно быть числом.")
        exit(1)

    # Подсчет подстрок
    list_of_subs = []
    for _ in input_string:
        num_of_subs = input_string.count(_)
        if num_of_subs == int(n):
            list_of_subs.append(_)
    list_of_subs = list(dict.fromkeys(list_of_subs))  # Удаляем дубликаты, сохраняя порядок

    for _ in list_of_subs:
        print(f"подстрока '{_}' встречается {n} раз(а).")
    if len(list_of_subs) > 0:
        print(f"Весь лист совпавщих {n} раз(а) подстрок: ", list_of_subs)
    else:
        print(f"Нет подстрок, которые встречаются {n} раз(а).")
        
    # Предложение повторить или выйти
    print("Нажмите Enter для повтора или 0 для выхода.")

    if input() == '0': 
        repeat = False
        print("Вы вышли из программы.")
        