def personal_sum(numbers): # зададим ф-ю
    result = 0  # для хранения суммы чисел
    incorrect_data = 0  # счётчик для некорр. данных

    for number in numbers:  # перебир. эл. numbers
        try: # код с возможной ошибкой
            result += number  # увел. result на тек. эл.
        except TypeError:   # блок кода в случ. ошибки
            incorrect_data += 1  # увелич. счётчик некорр. данных на 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')  # вывод сообщ. об ошибке
    return result, incorrect_data  # возвращаем кортеж из суммы чисел и количества некорр. данных

def calculate_average(numbers): # зададим ф-ю
    try: # код с возможной ошибкой
        if isinstance(numbers, str):  # строка ли numbers
            numbers = list(numbers)  # преобр. строку в список символов

        if not isinstance(numbers, (list, tuple, set)):  # проверяем, является ли numbers коллекцией
            print('В numbers записан некорректный тип данных')  # выводим сообщение об ошибке
            return None  # возвращ. None, если numbers не коллекциея

        total_sum, incorrect_data = personal_sum(numbers)  # для подсчёта суммы
        valid_count = len(numbers) - incorrect_data  # вычисл. кол-во корр. чисел

        if valid_count == 0:  # если нет корр. чисел - возвращ. 0
            return 0
        average = total_sum / valid_count  # вычисл. ср. арифм.
        return average  # возвращаем ср. арифм.

    except ZeroDivisionError:  # обр-ем исключение деления на ноль
        return 0  # возвр. 0, если случилось деление на ноль

# Примеры
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать