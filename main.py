# '''i
# print('Hello World')
# #функция принт нужна для вывода данных в окно консоли#
# name = input("Скажи своё имя:")
# #переменная которая хранит в себе строку#
# age = int(input("Введите свой возраст"))
# #переменная которая хранит в себе целочисленное число#
# print(type(age), type(name))
# water = 4.5
# #переменная которая хранит в себе дробь#
# print('Привет,' , name, 'тебе', age, 'лет')
# print('Я пью ', water, 'литров воды')
# '''
# '''
# answer = int(input("Сколько будет 5*8:10:"))
# print('Правильный Ответ 4, ваш ответ: ', answer)
# '''
# '''
# Пользователь вводит с клавиатуры 3 числа необходимо найти сумму чисел найти произведение чисел найти разность чисел найти разделения
# результат вычислений операций вывести на экран
# '''
# '''
# num1 = int(input("Введите 1 число"))
# num2 = int(input("Введите 2 число"))
# num3 = int(input("Введите 3 число"))
# print("Сумма ", num1 + num2 + num3, "Умножение ", num1 * num2 * num3)
# '''
#
# '''
# print("Сегодня 5 сентября , " 'Я Измученный пришел на первую пару', 'к 8:15' , sep='\t', end=' ')
#
# #\t - текствоя тагуляция ( 3 пробела) \n - перенос на новую строку  sep - отступы между параметрами print  end - завершение строки#
#
# print('Желаю \'всем\'  продуктивного дня!')
# '''
# '''
# name = input('Введите имя:')
# s_name = input('Фамилия:')
# age = int(input("Введите ваш возраст"))
# date = int(input("Введите ваш год рождения:"))
# print(f"Ваше имя: {name} \n"  f"Ваша фамилия: {s_name} \n"  f"Ваша дата рождения: {date} \n"  f"Ваш возраст: {age}")
# # Обращение f" или f' и f~ нужно для форматирования текста и вставки переменных в строку
# '''
# '''
# Арифметические опперации python
#  +-/* ( )
# **  оператор возведения в степень
# print(2+2) #4
# // - целочисленное деление
# print(6,31 // 3) #2
# % - деление по остатку
# print(6%2) #0
# Что делать не надо:
# 1.делить на 0 нельзя
# 2.делить целое число на 0
# 3.находить остаток от деления на 0
# функция суммы - sum(123)#6
# функция минимума - min(1,2,3)#1
# функция максимума - max(1,2,3)#3
# '''
#
# '''
# num1 = int(input("Введите зп: "))
# num2 = int(input("Введите сумму месячного платежа:"))
# num3 = int(input("Введите задолженность:"))
# print("Сумма ", num1 - num2 - num3)
# '''
# '''
# d1 = int(input("Длина 1 диагонали:"))
# d2 = int(input("Длина 2 диагонали:"))
# print("Длина 2 диагоналей", d1 * d2 /2)
# '''
# '''
# print("To be", '\n' "or not" '\n' "to be")
# '''
#
# '''
# #условные конструкции
# age = int(input("Введите ваш возраст: "))
# #if (Условие == true:
# # функция действие
# if age < 10 :
#     print("тЫ ЕЩЕ МАЛЫШ")
# else:
#     print("Вы уже взрослый")
# '''
# '''
# age = int(input("Введите ваш возраст: "))
# if 0 < age < 10 :
#         print("Ты еще малыш")
#     if age < 20 and age < 10 :
#         print("Ты еще подросток")
#     if 20 < age < 45 :
#         print("Ты молодеж")
#     if 45 < age < 100 :
#         print("Ты уже пенсионер")
#     else:
#         print("Некорректный возраст")
# '''
# '''
# #ДЗ ЗАДАНИЕ 1
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))
#
# operation = input("Выберите операцию (сумма/произведение): ").lower()
#
# if operation == "сумма":
#     result = num1 + num2 + num3
# elif operation == "произведение":
#     result = num1 * num2 * num3
# else:
#     print("Некорректный выбор операции.")
#     exit()
#
# print("Результат:", result)
#
# #ДЗ ЗАДАНИЕ 2
#
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))
#
# operation = input("Выберите операцию (максимум/минимум/среднее): ").lower()
#
# if operation == "максимум":
#     result = max(num1, num2, num3)
# elif operation == "минимум":
#     result = min(num1, num2, num3)
# elif operation == "среднее":
#     result = (num1 + num2 + num3) / 3
# else:
#     print("Некорректный выбор операции.")
#     exit()
#
# print("Результат:", result)
#
# #ДЗ ЗАДАНИЕ 3
#
# meters = float(input("Введите количество метров: "))
#
# unit = input("Выберите единицу измерения для перевода (мили/дюймы/ярды): ").lower()
#
# if unit == "мили":
#     result = meters * 0.000621371
# elif unit == "дюймы":
#     result = meters * 39.3701
# elif unit == "ярды":
#     result = meters * 1.09361
# else:
#     print("Некорректный выбор единицы измерения.")
#     exit()
#
# print("Результат:", result, unit)
#
# '''
# '''
# #ДЗ ЗАДАНИЕ 1
# number = int(input("Введите число от 1 до 100: "))
#
# if 1 <= number <= 100:
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# else:
#     print("Ошибка: число должно быть в диапазоне от 1 до 100.")
#     '''
# '''
# #ДЗ ЗАДАНИЕ 2
#     base = float(input("Введите число: "))
# exponent = int(input("Введите степень (от 0 до 7): "))
#
# if 0 <= exponent <= 7:
#     result = base ** exponent
#     print(f"{base} в степени {exponent} равно {result}")
# else:
#     print("Ошибка: степень должна быть в диапазоне от 0 до 7.")
#     '''
#
#     #ДЗ ЗАДАНИЕ 3
# cost_per_minute = float(input("Введите стоимость разговора за минуту: "))
# operator_from = input("Выберите оператора, с которого звоните: ")
# operator_to = input("Выберите оператора, на который звоните: ")
#
# # Пример тарифов
# tariffs = {
#     ("OperatorA", "OperatorB"): 1.0,
#     ("OperatorA", "OperatorC"): 1.2,
#     ("OperatorB", "OperatorA"): 0.9,
#     ("OperatorB", "OperatorC"): 1.1,
#     ("OperatorC", "OperatorA"): 1.3,
#     ("OperatorC", "OperatorB"): 0.8,
# }
#
# if (operator_from, operator_to) in tariffs:
#     tariff = tariffs[(operator_from, operator_to)]
#     total_cost = cost_per_minute * tariff
#     print(f"Стоимость разговора: {total_cost:.2f}")
# else:
#     print("Ошибка: тариф не найден.")
# '''
# '''
# #ДЗ ЗАДАНИЕ 4
# def calculate_salary(sales):
#     base_salary = 200
#     if sales < 500:
#         commission = sales * 0.03
#     elif 500 <= sales <= 1000:
#         commission = sales * 0.05
#     else:
#         commission = sales * 0.08
#     return base_salary + commission
#
# sales_manager1 = float(input("Введите уровень продаж для менеджера 1: "))
# sales_manager2 = float(input("Введите уровень продаж для менеджера 2: "))
# sales_manager3 = float(input("Введите уровень продаж для менеджера 3: "))
#
# salary_manager1 = calculate_salary(sales_manager1)
# salary_manager2 = calculate_salary(sales_manager2)
# salary_manager3 = calculate_salary(sales_manager3)
#
# max_salary = max(salary_manager1, salary_manager2, salary_manager3)
# if max_salary == salary_manager1:
#     salary_manager1 += 200  # Премия
# elif max_salary == salary_manager2:
#     salary_manager2 += 200  # Премия
# else:
#     salary_manager3 += 200  # Премия
#
# print(f"Зарплата менеджера 1: {salary_manager1}")
# print(f"Зарплата менеджера 2: {salary_manager2}")
# print(f"Зарплата менеджера 3: {salary_manager3}")
# '''
# '''
# import random
# N = 10
# list_sort_buble = []
# for i in range(10) :
#     list_sort_buble.append(random.randint(0,100))
# print(f'Начальный список: ' "{list_sort_buble}")
# for i in range(N) :
#     for j in range (N - 1 - i):
#         if list_sort_buble[j] > list_sort_buble[j+1] :
#             list_sort_buble[j], list_sort_buble[j+1]
# print(f"Отсортированный список: {list_sort_buble}")
#
# '''
# '''
# def circle(r):
#     are = 3.14 * r * r
#     return area
# print(circle(10))
#
# def max3(a, b, c):
#
# if a >= b and a >= circle
#     return a
# if b >= a and b >= c
#     return b
# if c >= a and c >= b
#     return c
#
# def perimeter(l, w):
#     p = l + l + w + w
#     return p
#
# print(perimeter(5, 7))
#
# def n(number):
#     if number % 2 == 0:
#         return number - 1
#     else:
#         return number
# print(f"Обработка числа 10:{n(10)}")
# print(f"Обработка числа 7:{n(7)}")

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n * f(n-1)
# print(f(5))

# def num(a, b, c):
#     return (a + b + c) / 3

# def median(a, b, c):
#     num = sorted([a, b, c])
#     return num[1]

# from random import randint
#
# N = 10
# mylist = []
# for i in range(N):
#     mylist.append(randint(1,99))
# print(f"Неотсортированный список: {mylist}")
# i = 0
# while i < N - 1:
#     m = i
#     j = i + 1
#     while j < N:
#         if mylist[j] < mylist[m]:
#             m = j
#         j += 1
#     mylist[i], mylist[m] = mylist[m], mylist[i]
#     i += 1
# print(f"Отсортированный список: {mylist}")

#3



#4
# words = ["apple", "banana", "cherry", "date", "apricot"]
# print(f"Неотсортированный список: {words}")
# words.sort()
# print(f"Отсортированный список: {words}")


# # import re
# #
# # def isCyrillic(text):
# #     """Проверяет, содержит ли текст кириллические символы."""
# #     return bool(re.search('[а-яА-Я]', text))
# #
# # def create_letter_points_dict(point_map):
# #     """Создает словарь для быстрого поиска очков по букве."""
# #     letter_points = {}
# #     for points, letters in point_map.items():
# #         for letter in letters:
# #             letter_points[letter] = points
# #     return letter_points
# #
# # point_en_map = {1:'AEIOULNSTR',
# #                 2:'DG',
# #                 3:'BCMP',
# #                 4:'FHVWY',
# #                 5:'K',
# #                 8:'JX',
# #                 10:'QZ'}
# #
# # point_ru_map = {1:'АВЕИНОСТ',
# #                 2:'ДКЛМПУ',
# #                 3:'БГЁЬЯ',
# #                 4:'ЙЫ',
# #                 5:'ЖЗЧЦ',
# #                 8:'ШЭЮ',
# #                 10:'ФЩЪ'}
# #
# # en_letter_points = create_letter_points_dict(point_en_map)
# # ru_letter_points = create_letter_points_dict(point_ru_map)
# #
# # def calculate_scrabble_score(word, letter_points_dict):
# #     """Подсчитывает очки за слово, используя предоставленный словарь букв."""
# #     score = 0
# #     for letter in word:
# #         score += letter_points_dict.get(letter, 0)
# #     return score
# #
# # def play_scrabble_multiplayer(num_players=2, num_rounds=3):
# #     """
# #     Реализует многопользовательский режим игры Скрабл.
# #
# #     Args:
# #         num_players (int): Количество игроков.
# #         num_rounds (int): Количество раундов.
# #     """
# #     if num_players > 10:
# #         print("Максимальное количество игроков - 10.")
# #         num_players = 10
# #     if num_rounds > 10:
# #         print("Максимальное количество раундов - 10.")
# #         num_rounds = 10
# #
# #     players = {}
#
#     print("--- Добро пожаловать в Скрабл! ---")
#
#
#     for i in range(num_players):
#         player_name = input(f"Введите имя игрока {i+1}: ").strip()
#         players[player_name] = {'total_score': 0, 'rounds': []}
#
#
#     for round_num in range(1, num_rounds + 1):
#         print(f"\n--- Раунд {round_num} ---")
#         for player_name in players:
#             while True:
#                 word = input(f"{player_name}, введите ваше слово: ").strip().upper()
#                 if not word:
#                     print("Слово не может быть пустым. Попробуйте снова.")
#                     continue
#
#
#                 if isCyrillic(word):
#                     letter_points = ru_letter_points
#                 else:
#                     letter_points = en_letter_points
#
#
#                 valid_word = True
#                 for char in word:
#                     if char not in letter_points:
#                         valid_word = False
#                         print(f"Слово '{word}' содержит недопустимые буквы ({char}). Попробуйте снова.")
#                         break
#
#                 if valid_word:
#                     round_score = calculate_scrabble_score(word, letter_points)
#                     players[player_name]['total_score'] += round_score
#                     players[player_name]['rounds'].append(round_score)
#                     print(f"Ваши очки за этот раунд: {round_score}")
#                     break
#
#
#     print("\n--- Итоговые результаты ---")
#     sorted_players = sorted(players.items(), key=lambda item: item[1]['total_score'], reverse=True)
#
#     for i, (player_name, data) in enumerate(sorted_players):
#         print(f"{i+1}. {player_name}: Общий счет - {data['total_score']} (Раунды: {', '.join(map(str, data['rounds']))})")
#
# if __name__ == "__main__":
#     try:
#         num_players_input = int(input("Введите количество игроков (до 10): "))
#         num_rounds_input = int(input("Введите количество раундов (до 10): "))
#         play_scrabble_multiplayer(num_players=num_players_input, num_rounds=num_rounds_input)
#     except ValueError:
#         print("Некорректный ввод. Пожалуйста, вводите числа.")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")

# backpack_items = {
#     'Зажигалка': {'weight': 20, 'value': 5},
#     'Компас': {'weight': 100, 'value': 10},
#     'Фрукты': {'weight': 500, 'value': 30},
#     'Рубашка': {'weight': 300, 'value': 20},
#     'Термос': {'weight': 1000, 'value': 50},
#     'аптечка': {'weight': 200, 'value': 40},
#     'Куртка': {'weight': 600, 'value': 35},
#     'Бинокль': {'weight': 400, 'value': 25},
#     'Удочка': {'weight': 1300, 'value': 15},
#     'Салфетки': {'weight': 40, 'value': 10},
#     'Бутерброды': {'weight': 800, 'value': 45},
#     'Палатка': {'weight': 5500, 'value': 100},
#     'Спальный мешок': {'weight': 2500, 'value': 80},
#     'Изолента': {'weight': 250, 'value': 15},
#     'Котел': {'weight': 3000, 'value': 70}
# }
#
# max_weight_kg = float(input("Введите допустимый вес рюкзака (кг): "))
# max_weight_grams = max_weight_kg * 1000
#
# print(f"\n--- Анализ рюкзака (макс. вес: {max_weight_kg:.2f} кг) ---")
#
# items_can_take = []
# items_cannot_take = []
# current_weight = 0
# total_value = 0
#
# sorted_items = sorted(backpack_items.items(),
#                       key=lambda item: item[1]['value'] / item[1]['weight'] if item[1]['weight'] > 0 else float('inf'),
#                       reverse=True)
#
# print("\nВещи, которые могут поместиться (выбраны жадным методом по ценности/вес):")
# for item_name, details in sorted_items:
#     item_weight = details['weight']
#     item_value = details['value']
#
#     if current_weight + item_weight <= max_weight_grams:
#         current_weight += item_weight
#         total_value += item_value
#         items_can_take.append((item_name, item_weight, item_value))
#         print(f"- {item_name} (вес: {item_weight/1000:.2f} кг, ценность: {item_value})")
#     else:
#         items_cannot_take.append((item_name, item_weight, item_value))
#
# print(f"\nИтого помещено: {len(items_can_take)} вещей.")
# print(f"Общий вес: {current_weight/1000:.2f} кг / {max_weight_kg:.2f} кг.")
# print(f"Общая ценность: {total_value}")
#
# print("\n--- Все вещи, которые легче максимального веса ---")
# all_lighter_items = []
# for item_name, details in backpack_items.items():
#     if details['weight'] < max_weight_grams:
#         all_lighter_items.append((item_name, details['weight']))
#         print(f"- {item_name} (вес: {details['weight']/1000:.2f} кг)")
#
# print("\n--- Все вещи, которые тяжелее максимального веса ---")
# all_heavier_items = []
# for item_name, details in backpack_items.items():
#     if details['weight'] > max_weight_grams:
#         all_heavier_items.append((item_name, details['weight']))
#         print(f"- {item_name} (вес: {details['weight']/1000:.2f} кг)")

# def create_phone_book_entry(tel, vk=None, youtube=None, telegram=None):
#     """Создает запись для телефонной книги."""
#     entry = {'tel': tel}
#     if vk:
#         entry['vk'] = vk
#     if youtube:
#         entry['youtube'] = youtube
#     if telegram:
#         entry['telegram'] = telegram
#     return entry
#
# phone_book = {
#     "Маша": create_phone_book_entry('+7922123561', vk='vk.com/masha321', youtube='youtube.com/masha321', telegram='t.me/masha321'),
#     "Петр": create_phone_book_entry('+7911987654', vk='vk.com/petr_ivanov'),
#     "Анна": create_phone_book_entry('+79035551212', telegram='t.me/anna_s'),
#     "Сергей": create_phone_book_entry('+79500001122', youtube='youtube.com/sergey_vlog'),
#     "Иван": create_phone_book_entry('+79601112233') # Только телефон
# }
#
# def search_contact(book, name):
#     """Ищет контакт в телефонной книге."""
#     name_capitalized = name.strip().capitalize() # Приводим к единому виду
#     if name_capitalized in book:
#         return book[name_capitalized]
#     else:
#         return None
#
# def display_contact_info(contact_data):
#     """Красиво выводит информацию о контакте."""
#     if contact_data:
#         print("\n--- Информация о контакте ---")
#         for key, value in contact_data.items():
#             print(f"{key.capitalize()}: {value}")
#         print("---------------------------")
#     else:
#         print("Контакт не найден.")
#
# if __name__ == "__main__":
#     while True:
#         user_search = input("Введите имя контакта для поиска (или 'выход' для завершения): ")
#         if user_search.lower() == 'выход':
#             break
#
#         contact_info = search_contact(phone_book, user_search)
#         display_contact_info(contact_info)
#
#     print("Программа завершена.")



# import random
# class MSDice:
#     def _init_(self, sides):
#         self.sides = sides
#         self.current_value = 1
#         def roll(self):
#             self.current_value = random.randint(1, self.sides)
#             return self.current_value
#         def_str_(self):
#         return f"MSDice({self.sides}-sided): Current Value = {self.current_value}"
#     class D4(MSDice):
#         def_init_(self):
#         super()._init_(4)
#     class D6(MSDice):
#         def_init_(self):
#         super()._init_(6)
#
#         class D10(MSDice):
#             def_init_(self):
#             super()._init_(10)
#
#             class D20(MSDice):
#                 def_init_(self):
#                 super()._init_(20)
#                 if_name_=="_main_":
#                 dice = D20()
#                 print(dice)
#                 print("Rolling dice...")
#                 print("Result", dice.roll())




