# Задача 1
# def circle_stats(radius):
#     # Простая проверка: радиус должен быть числом и неотрицательным
#     if not isinstance(radius, (int, float)) or radius < 0:
#         return (0, 0)
#     pi = 3.14159
#     circumference = 2 * pi * radius
#     area = pi * radius * radius
#     return (circumference, area)
#Пример использования:
# radius = 5
# length, square = circle_stats(radius)
# print(f"Радиус: {radius}")
# print(f"Длина окружности: {length}")
# print(f"Площадь круга: {square}")
#
# # Задача 2
# def count_vowels(text):
#     # Проверка: text должен быть строкой
#     if not isinstance(text, str):
#         return {}
#     vowels = 'аеиоуыэюя'
#     text = text.lower()
#     result = {}
#     for v in vowels:
#         result[v] = 0  # инициализируем все гласные нулём
#     for char in text:
#         if char in vowels:
#             result[char] += 1
#     return result
# Пример использования:
# text = "Привет, мир! Как дела?"
# counts = count_vowels(text)
# print(f"Строка: '{text}'")
# print(f"Статистика гласных: {counts}")
#
#
# # Задача 3
# def fizzbuzz_sum(n):
#     # Проверка: n должно быть целым и >= 1
#     if not isinstance(n, int) or n < 1:
#         return 0
#     total = 0
#     for i in range(1, n + 1):
#         if i % 3 != 0 and i % 5 != 0:
#             total += i
#     return total
# Пример использования:
# n = 20
# result_sum = fizzbuzz_sum(n)
# print(f"Сумма чисел от 1 до {n} (исключая кратные 3 и 5): {result_sum}")
#
#
# # Задача 4
# def remove_duplicates_sorted(lst):
#     # Проверка: lst должен быть списком
#     if not isinstance(lst, list):
#         return []
#     unique = []
#     for item in lst:
#         if item not in unique:
#             unique.append(item)
#     # Простая сортировка пузырьком (без sorted() и set())
#     n = len(unique)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if unique[i] > unique[j]:
#                 unique[i], unique[j] = unique[j], unique[i]
#     return unique
# Пример использования:
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# unique_sorted_numbers = remove_duplicates_sorted(numbers)
# print(f"Исходный список: {numbers}")
# print(f"Отсортированный список без дубликатов: {unique_sorted_numbers}")
#
# # Задача 5
# def merge_dicts(dict1, dict2):
#     # Проверка: оба аргумента должны быть словарями
#     if not isinstance(dict1, dict) or not isinstance(dict2, dict):
#         return {}
#     result = {}
#     all_keys = set(dict1.keys()) | set(dict2.keys())
#     for key in all_keys:
#         val1 = dict1.get(key, 0)
#         val2 = dict2.get(key, 0)
#         # Очень простая проверка: значения должны быть числами
#         if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
#             result[key] = val1 + val2
#         else:
#             result[key] = 0  # если не число — считаем как 0
#     return result
#
# Пример использования:
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 5, 'c': 15, 'd': 40}
# combined = merge_dicts(d1, d2)
# print(f"Словарь 1: {d1}")
# print(f"Словарь 2: {d2}")
# print(f"Объединенный словарь: {combined}")
#
# # Задача 6
# def process_numbers_file():
#     try:
#         with open('numbers.txt', 'r', encoding='utf-8') as f_in:
#             lines = f_in.readlines()
#         filtered = []
#         for line in lines:
#             line = line.strip()
#             if line.isdigit() or (line.startswith('-') and line[1:].isdigit()):
#                 num = int(line)
#                 if num > 0 and num % 2 == 0:
#                     filtered.append(str(num))
#         with open('filtered.txt', 'w', encoding='utf-8') as f_out:
#             f_out.write('\n'.join(filtered))
#     except:
#         # Если файл не найден или ошибка — просто ничего не делаем (защита от "дурочка")
#         pass
#
# Для тестирования создайте файл numbers.txt с содержимым:
# -5
# 10
# 7
# 12
# 0
# 22
# -8
# 15
#
#Затем вызовите функцию:
# process_numbers_file()
#
# После выполнения, в файле filtered.txt должны быть:
# 10
# 12
# 22
#
# # Задача 7
# def apply_to_list(func, lst):
#     # Проверка: lst должен быть списком, func — функцией
#     if not isinstance(lst, list) or not callable(func):
#         return []
#     result = []
#     for item in lst:
#         try:
#             result.append(func(item))
#         except:
#             result.append(None)  # если ошибка — ставим None
#     return result
#
# Пример использования:
# def square(x):
#     return x * x
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = apply_to_list(square, numbers)
# print(f"Исходный список: {numbers}")
# print(f"Список квадратов: {squared_numbers}")
#
# def to_uppercase(s):
#     return s.upper()
#
# words = ["hello", "world"]
# upper_words = apply_to_list(to_uppercase, words)
# print(f"Исходный список слов: {words}")
# print(f"Список слов в верхнем регистре: {upper_words}")
#
# # Задача 8
# def safe_divide(a, b):
#     # Простая проверка: оба должны быть числами, и b ≠ 0
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         return "Ошибка"
#     if b == 0:
#         return "Ошибка"
#     return a / b
#
# Примеры использования:
# print(safe_divide(10, 2))       # Вывод: 5.0
# print(safe_divide(10, 0))       # Вывод: Ошибка
# print(safe_divide("abc", 2))    # Вывод: Ошибка
# print(safe_divide(10, "def"))   # Вывод: Ошибка
# print(safe_divide(15, 3))       # Вывод: 5.0
#
# # Задача 10
# def text_analyzer(text):
#     # Проверка: text должен быть строкой
#     if not isinstance(text, str):
#         return {
#             'char_count': 0,
#             'word_count': 0,
#             'sentence_count': 0,
#             'most_common_word': ''
#         }
#
#     char_count = len(text)
#
#     # Удалим знаки препинания для подсчёта слов
#     clean_text = ''
#     for ch in text:
#         if ch.isalpha() or ch == ' ':
#             clean_text += ch.lower()
#         else:
#             clean_text += ' '
#
#     words = clean_text.split()
#     word_count = len(words)
#
#     # Подсчёт предложений
#     sentence_count = 0
#     for ch in text:
#         if ch in '.!?':
#             sentence_count += 1
#
#     # Самое частое слово
#     most_common_word = ''
#     if words:
#         freq = {}
#         for word in words:
#             freq[word] = freq.get(word, 0) + 1
#         max_count = 0
#         for word, count in freq.items():
#             if count > max_count:
#                 max_count = count
#                 most_common_word = word
#
#     return {
#         'char_count': char_count,
#         'word_count': word_count,
#         'sentence_count': sentence_count,
#         'most_common_word': most_common_word
#     }
# # Пример использования:
# text = "Это пример текста. Он имеет несколько слов, и он довольно прост! Как дела?"
# analysis = text_analyzer(text)
# print(f"Анализ текста:\n'{text}'")
# print(f"Статистика: {analysis}")
#
# text_empty = ""
# analysis_empty = text_analyzer(text_empty)
# print(f"\nАнализ пустого текста: {analysis_empty}")
#
# text_no_punctuation = "Одно слово"
# analysis_np = text_analyzer(text_no_punctuation)
# print(f"\nАнализ текста без знаков препинания:\n'{text_no_punctuation}': {analysis_np}")
