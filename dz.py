# '''
# # задание 1
#
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# for number in range(start, end + 1):
#     if number % 7 == 0:
#         print(number)
#
# #задание 2
#
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# for number in range(start, end + 1):
#     print(number, end=" ")
# print()
#
# for number in range(end, start - 1, -1):
#     print(number, end=" ")
# print()
#
# for number in range(start, end + 1):
#     if number % 7 == 0:
#         print(number, end=" ")
# print()
#
# count = 0
# for number in range(start, end + 1):
#     if number % 5 == 0:
#         count += 1
# print("Количество чисел, кратных 5:", count)
#
# #задание 3
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# for number in range(start, end + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# '''
#
# #дз Модуль 3. Циклы. Часть
# #1
# '''
# number = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")
# '''
# #2
# '''
# def currency_converter():
#     rates = {
#         'USD': 75.0,  # Пример курса рубля к доллару
#         'EUR': 85.0,  # Пример курса рубля к евро
#         'RUB': 1.0
#     }
#     while True:
#         print("\nМеню конвертера:")
#         print("1. Рубли в доллары")
#         print("2. Доллары в рубли")
#         print("3. Рубли в евро")
#         print("4. Евро в рубли")
#         print("0. Выход")
#         choice = input("Выберите действие: ")
#
#         if choice == '0':
#             break
#         elif choice == '1':
#             sum_rub = float(input("Введите сумму в рублях: "))
#             print(f"{sum_rub} RUB = {sum_rub / rates['USD']:.2f} USD")
#         elif choice == '2':
#             sum_usd = float(input("Введите сумму в долларах: "))
#             print(f"{sum_usd} USD = {sum_usd * rates['USD']:.2f} RUB")
#         elif choice == '3':
#             sum_rub = float(input("Введите сумму в рублях: "))
#             print(f"{sum_rub} RUB = {sum_rub / rates['EUR']:.2f} EUR")
#         elif choice == '4':
#             sum_eur = float(input("Введите сумму в евро: "))
#             print(f"{sum_eur} EUR = {sum_eur * rates['EUR']:.2f} RUB")
#         else:
#             print("Некорректный выбор. Попробуйте снова.")
#
# currency_converter()
# '''
# '''
# #3
# lower = int(input("Введите нижнюю границу диапазона: "))
# upper = int(input("Введите верхнюю границу диапазона: "))
#
# while True:
#     num = int(input("Введите число: "))
#     if lower <= num <= upper:
#         break
#     else:
#         print("Число вне диапазона, попробуйте снова.")
#
# for i in range(lower, upper + 1):
#     if i == num:
#         print(f"!{i}!", end=' ')
#     else:
#         print(i, end=' ')
# print()
# '''
# '''
# #4
# import random
# import time
#
# print("Игра 'Угадай число' от 1 до 500. Введите 0, чтобы выйти.")
#
# target = random.randint(1, 500)
# attempts = 0
# start_time = time.time()
#
# while True:
#     guess = int(input("Ваш вариант: "))
#     if guess == 0:
#         print("Игра завершена.")
#         break
#     attempts += 1
#     if guess == target:
#         elapsed = time.time() - start_time
#         print(f"Поздравляем! Вы угадали число за {attempts} попыток и {elapsed:.2f} секунд.")
#         break
#     elif guess < target:
#         print("Больше.")
#     else:
#         print("Меньше.")
# '''
#
#
# #9.25
#
# #2
# '''
# def find_minimum(numbers):
#
#     if not numbers:
#         return None, numbers  # Возвращаем None если список пуст
#
#
#     minimum = numbers[0]
#
#
#     for num in numbers:
#         # Если нашли число меньше текущего минимума
#         if num < minimum:
#             minimum = num  # Обновляем минимум
#
#
#     return minimum, numbers
#
#
# numbers_list = [5, 3, 8, 1, 9, 2]
# min_value, original_list = find_minimum(numbers_list)
# print(f"Минимальный элемент: {min_value}")
# print(f"Исходный список: {original_list}")
# '''
# #3
# '''
# def is_prime(n):
#
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# def count_primes(numbers):
#
#     prime_count = 0
#     for num in numbers:
#         if is_prime(num):
#             prime_count += 1
#     return prime_count, numbers
#
#
# numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# count, original_list = count_primes(numbers_list)
# print(f"Количество простых чисел: {count}")
# print(f"Исходный список: {original_list}")
# '''
# #4
# '''
# def remove_number(numbers, target):
#     removed_count = 0
#     for number in numbers:
#         if number == target:
#             removed_count += 1
#             numbers.remove(number)
#     return removed_count
# '''
# #5
# '''
# def merge_lists(list1, list2):
#     result = []
#
#     for item in list1:
#         result.append(item)
#
#     for item in list2:
#         result.append(item)
#
#     return result
#
# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
#
# merged = merge_lists(list_a, list_b)
# print(merged)
# '''
# #6
# '''
# numbers = [4, 5, 6, 3, 9] [4]
# def pow(numbers, k):
#     return [x ** k for x in numbers] [4]
# '''
#дз 2.10
#1
# import random
#
# my_list = [random.randint(-10, 10) for _ in range(20)]
# print("Начальный список:", my_list)
#
# mid_point = len(my_list) // 2
# left_half = my_list[:mid_point]
# right_half = my_list[mid_point:]
#
# left_half.sort()
#
# right_half.sort(reverse=True)
#
# sorted_list = left_half + right_half
# print("Отсортированный список:", sorted_list)
#
#2
# import random
#
# my_list_2 = [random.randint(-20, 20) for _ in range(45)]
# print("Начальный список :", my_list_2)
#
# third_size = len(my_list_2) // 3
#
#
# even_elements = sorted([x for x in my_list_2 if x % 2 == 0])
#
#
# unique_min = min(my_list_2)
# unique_max = max(my_list_2)
#
#
# max_min_alternating = []
# count = 0
# while count < third_size:
#     if count % 2 == 0:
#         max_min_alternating.append(unique_max)
#     else:
#         max_min_alternating.append(unique_min)
#     count += 1
#     if count < third_size and unique_max == unique_min:
#         break
#
#
# remaining_for_max_min = third_size - len(max_min_alternating)
# if remaining_for_max_min > 0:
#     max_min_alternating.extend([unique_max] * remaining_for_max_min)
#
#
# odd_elements = sorted([x for x in my_list_2 if x % 2 != 0])
#
#
# final_list_2 = []
#
# final_list_2.extend(even_elements)
#
# final_list_2.extend(max_min_alternating)
#
# final_list_2.extend(odd_elements)
#
#
# even_count = len(even_elements)
# odd_count = len(odd_elements)
# max_min_count = len(max_min_alternating)
#
# all_elements_sorted = sorted(my_list_2)
# even_from_original = [x for x in all_elements_sorted if x % 2 == 0]
# odd_from_original = [x for x in all_elements_sorted if x % 2 != 0]
#
# result_list_2 = []
# result_list_2.extend(even_from_original)
# result_list_2.extend(max_min_alternating)
# result_list_2.extend(odd_from_original)
#
# result_list_2 = result_list_2[:45]
#
# print("Отсортированный список :", result_list_2)

#10/6
#3
#import random
#
# def insertion_sort_desc(arr):
#     iterations = 0
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key > arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#             iterations += 1
#         arr[j + 1] = key
#         iterations += 1
#     return iterations
#

# numbers = random.sample(range(1, 101), 15)
#

# iterations = insertion_sort_desc(numbers)
#

# print("Отсортированный список:", numbers)
# print("Количество итераций:", iterations)

# 4
# words = ["apple", "banana", "cherry", "date", "apricot"]
#

# words.sort()
#

# print("Отсортированный список:", words)

#5
# def sort_excluding_index(arr, k):
#     left_part = arr[:k]
#     right_part = arr[k + 1:]
#
#     left_part.sort()
#     right_part.sort()
#
#     sorted_arr = left_part + [arr[k]] + right_part
#     return sorted_arr
#
# array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# k = 4
#
# sorted_array = sort_excluding_index(array, k)
#
# print("Отсортированный массив:", sorted_array)
#


#dz 10/23
#1
# def print_formatted_text():
#   """
#   Отображает на экране форматированный текст.
#   """
#   quote = "Don't compare yourself with anyone in this world...if you do so, you are insulting yourself."
#   author = "Bill Gates"
#   print(f'"{quote}"')
#   print(f"\n{author}")
#
# print_formatted_text()
#2
# def print_even_numbers_between(num1, num2):
#   """
#   Принимает два числа и отображает все четные числа между ними.
#
#   Args:
#     num1: Первое число.
#     num2: Второе число.
#   """
#   start = min(num1, num2)
#   end = max(num1, num2)
#
#   print(f"Четные числа между {start} и {end}:")
#   for number in range(start, end + 1):
#     if number % 2 == 0:
#       print(number)
#
# print_even_numbers_between(10, 25)
# print("-" * 20)
# print_even_numbers_between(30, 15)
#3
# def draw_square(side_length, symbol, is_filled):
#   """
#   Отображает пустой или заполненный квадрат.
#
#   Args:
#     side_length: Длина стороны квадрата.
#     symbol: Символ для рисования квадрата.
#     is_filled: Логическое значение, определяющее, заполнен ли квадрат.
#   """
#   if side_length <= 0:
#     print("Длина стороны должна быть положительным числом.")
#     return
#
#   if is_filled:
#     for _ in range(side_length):
#       print(symbol * side_length)
#   else:
#
#     print(symbol * side_length)
#     for _ in range(side_length - 2):
#       print(symbol + " " * (side_length - 2) + symbol)
#     if side_length > 1: # Если сторона больше 1, печатаем нижнюю строку
#       print(symbol * side_length)
#
#
# # Примеры вызова функции
# print("Заполненный квадрат (сторона 4, символ '*'):")
# draw_square(4, '*', True)
# print("\n" + "=" * 20 + "\n")
#
# print("Пустой квадрат (сторона 5, символ '#'):")
# draw_square(5, '#', False)
# print("\n" + "=" * 20 + "\n")
#
# print("Пустой квадрат (сторона 1, символ '@'):")
# draw_square(1, '@', False)
# print("\n" + "=" * 20 + "\n")
#
# print("Пустой квадрат (сторона 2, символ '+'):")
# draw_square(2, '+', False)




#dz 13.11


# identification_codes = [123, 456, 789, 234]
# phone_numbers = ['+79101112233', '+79223334455', '+79334445566', '+79445556677']
#
#
# def display_users():
#     for code, phone in zip(identification_codes, phone_numbers):
#         print(f"ID: {code}, Phone: {phone}")
#
#
# def sort_by_id():
#     sorted_data = sorted(zip(identification_codes, phone_numbers), key=lambda x: x[0])
#     for code, phone in sorted_data:
#         print(f"ID: {code}, Phone: {phone}")
#
#
# def sort_by_phone():
#     sorted_data = sorted(zip(identification_codes, phone_numbers), key=lambda x: x[1])
#     for code, phone in sorted_data:
#         print(f"ID: {code}, Phone: {phone}")
#
#
# def menu():
#     while True:
#         print("\nМеню:")
#         print("1. Отсортировать по идентификационным кодам")
#         print("2. Отсортировать по номерам телефона")
#         print("3. Вывести список пользователей")
#         print("4. Выход")
#
#         choice = input("Выберите действие: ")
#
#         if choice == '1':
#             sort_by_id()
#         elif choice == '2':
#             sort_by_phone()
#         elif choice == '3':
#             display_users()
#         elif choice == '4':
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
#
# menu()



# 2
# Списки данных
# book_titles = ["Гарри Поттер", "Война и мир", "1984", "Мастер и Маргарита"]
# release_years = [1997, 1869, 1949, 1967]
#
# def display_books():
#     for title, year in zip(book_titles, release_years):
#         print(f"Название: {title}, Год выпуска: {year}")
#
# def sort_by_title():
#     sorted_data = sorted(zip(book_titles, release_years), key=lambda x: x[0])
#     for title, year in sorted_data:
#         print(f"Название: {title}, Год выпуска: {year}")
#
# def sort_by_year():
#     sorted_data = sorted(zip(book_titles, release_years), key=lambda x: x[1])
#     for title, year in sorted_data:
#         print(f"Название: {title}, Год выпуска: {year}")
#
# def menu():
#     while True:
#         print("\nМеню:")
#         print("1. Отсортировать по названию книг")
#         print("2. Отсортировать по годам выпуска")
#         print("3. Вывести список книг")
#         print("4. Выход")
#
#         choice = input("Выберите действие: ")
#
#         if choice == '1':
#             sort_by_title()
#         elif choice == '2':
#             sort_by_year()
#         elif choice == '3':
#             display_books()
#         elif choice == '4':
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
# menu()