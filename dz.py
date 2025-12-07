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


#dz 14.11
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# list3 = [7, 8, 9]
# list4 = [0, 10, 11]
#
#
# combined_list = list1 + list2 + list3 + list4
#
# sort_order = input("Выберите порядок сортировки (возрастание/убывание): ").strip().lower()
#
# if sort_order == "возрастание":
#     combined_list.sort()
# elif sort_order == "убывание":
#     combined_list.sort(reverse=True)
# else:
#     print("Некорректный ввод.")
#
# print("Отсортированный список:", combined_list)
#
# user_value = int(input("Введите значение для поиска: "))
#
# found = False
# for i in combined_list:
#     if i == user_value:
#         found = True
#         break
#
# if found:
#     print(f"Значение {user_value} найдено.")
# else:
#     print(f"Значение {user_value} не найдено.")

#2
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# list3 = [7, 8, 9]
# list4 = [0, 10, 11]
#
# unique_elements = set(list1) ^ set(list2) ^ set(list3) ^ set(list4)
# unique_list = list(unique_elements)
#
# sort_order = input("Выберите порядок сортировки (возрастание/убывание): ").strip().lower()
#
# if sort_order == "возрастание":
#     unique_list.sort()
# elif sort_order == "убывание":
#     unique_list.sort(reverse=True)
# else:
#     print("Некорректный ввод.")
#
# print("Отсортированный список:", unique_list)
#
# def binary_search(lst, value):
#     low, high = 0, len(lst) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if lst[mid] == value:
#             return True
#         elif lst[mid] < value:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False
#
# user_value = int(input("Введите значение для поиска: "))
#
# if binary_search(unique_list, user_value):
#     print(f"Значение {user_value} найдено.")
# else:
#     print(f"Значение {user_value} не найдено.")


# Задание
# 1
# import random
#
#
# class Number:
#     def __init__(self):
#         self.numbers = [random.randint(1, 100) for _ in range(15)]
#
#     def process_numbers(self):
#         first_third = self.numbers[:len(self.numbers) // 3]
#         average = sum(self.numbers) / len(self.numbers)
#
#         if average > len(self.numbers) // 3:
#             first_third.sort()
#         else:
#             first_third.sort(reverse=True)
#
#         remaining = self.numbers[len(self.numbers) // 3:]
#         remaining.sort(reverse=True)
#
#         self.numbers = first_third + remaining
#
#     def display(self):
#         print(self.numbers)
#
#
# number = Number()
# print("Исходный список:", number.numbers)
# number.process_numbers()
# print("Обработанный список:", number.numbers)
#
# ### Задание 2
#
#
# def main():
#     marks = [random.randint(1, 12) for _ in range(10)]
#
#     def display_marks():
#         print("Оценки студентов:", marks)
#
#     def change_mark():
#         index = int(input("Введите номер студента (0-9): "))
#         new_mark = int(input("Введите новую оценку (1-12): "))
#         marks[index] = new_mark
#
#     def display_average():
#         average = sum(marks) / len(marks)
#         print(f"Средний балл: {average:.2f}")
#
#     def sort_marks():
#         marks.sort()
#         print("Оценки отсортированы:", marks)
#
#     while True:
#         print("\nМеню:")
#         print("1. Вывод оценок")
#         print("2. Пересмотр экзамена (изменение оценки)")
#         print("3. Вывод среднего балла")
#         print("4. Сортировка списка оценок")
#         print("5. Выход")
#
#         choice = input("Выберите действие: ")
#         if choice == '1':
#             display_marks()
#         elif choice == '2':
#             change_mark()
#         elif choice == '3':
#             display_average()
#         elif choice == '4':
#             sort_marks()
#         elif choice == '5':
#             break
#         else:
#             print("Неверный ввод, попробуйте снова.")
#
#
# main()
#
# ### Задание 3
#
#
# def bubble_sort_optimized(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
#
#
# numbers = [random.randint(1, 100) for _ in range(10)]
# print("Исходный список:", numbers)
# sorted_numbers = bubble_sort_optimized(numbers)
# print("Отсортированный список:", sorted_numbers)







#DZ


# def добавить_баскетболиста(фио, рост):
#     """Добавляет баскетболиста в словарь."""
#     if фио in баскетболисты:
#         print(f"Баскетболист с ФИО '{фио}' уже существует.")
#     else:
#         баскетболисты[фио] = {'рост': рост}
#         print(f"Баскетболист '{фио}' успешно добавлен.")
#
# def удалить_баскетболиста(фио):
#     """Удаляет баскетболиста из словаря."""
#     if фио in баскетболисты:
#         del баскетболисты[фио]
#         print(f"Баскетболист '{фио}' успешно удален.")
#     else:
#         print(f"Баскетболист с ФИО '{фио}' не найден.")
#
# def поиск_баскетболиста(фио):
#     """Ищет баскетболиста по ФИО и выводит его информацию."""
#     if фио in баскетболисты:
#         info = баскетболисты[фио]
#         print(f"Найдено:\n  ФИО: {фио}\n  Рост: {info['рост']} см")
#     else:
#         print(f"Баскетболист с ФИО '{фио}' не найден.")
#
# def заменить_данные_баскетболиста(фио, новый_рост):
#     """Заменяет рост баскетболиста."""
#     if фио in баскетболисты:
#         баскетболисты[фио]['рост'] = новый_рост
#         print(f"Рост баскетболиста '{фио}' успешно изменен на {новый_рост} см.")
#     else:
#         print(f"Баскетболист с ФИО '{фио}' не найден.")
#
# def вывести_всех_баскетболистов():
#     """Выводит информацию обо всех баскетболистах."""
#     if not баскетболисты:
#         print("Список баскетболистов пуст.")
#         return
#     print("Список баскетболистов:")
#     for фио, info in баскетболисты.items():
#         print(f"- ФИО: {фио}, Рост: {info['рост']} см")
#
# # Пример использования:
# добавить_баскетболиста("Леброн Джеймс", 206)
# добавить_баскетболиста("Майкл Джордан", 198)
# добавить_баскетболиста("Леброн Джеймс", 207) # Попытка добавить существующего
#
# print("\n--- Поиск ---")
# поиск_баскетболиста("Майкл Джордан")
# поиск_баскетболиста("Стефен Карри")
#
# print("\n--- Замена ---")
# заменить_данные_баскетболиста("Леброн Джеймс", 207)
# заменить_данные_баскетболиста("Майклордан", 199) # Опечатка
#
# print("\n--- Вывод всех ---")
# вывести_всех_баскетболистов()
#
# print("\n--- Удаление ---")
# удалить_баскетболиста("Майкл Джордан")
# удалить_баскетболиста("Коби Брайант") # Несуществующий
#
# print("\n--- Вывод всех после удаления ---")
# вывести_всех_баскетболистов()
#
# Задание 2: Англо-французский словарь
# Описание: Программа для хранения пар "английское слово - перевод на французский" с возможностью добавления, удаления, поиска и замены данных.
#
#
#
# англо_французский_словарь = {}
#
# def добавить_перевод(английское_слово, французское_слово):
#     """Добавляет перевод в словарь."""
#     if английское_слово in англо_французский_словарь:
#         print(f"Слово '{английское_слово}' уже существует. Перевод не изменен.")
#     else:
#         англо_французский_словарь[английское_слово] = {'перевод': французское_слово}
#         print(f"'{английское_слово}' -> '{французское_слово}' добавлено.")
#
# def удалить_перевод(английское_слово):
#     """Удаляет перевод из словаря."""
#     if английское_слово in англо_французский_словарь:
#         del англо_французский_словарь[английское_слово]
#         print(f"Перевод для '{английское_слово}' удален.")
#     else:
#         print(f"Слово '{английское_слово}' не найдено в словаре.")
#
# def поиск_перевода(английское_слово):
#     """Ищет перевод английского слова."""
#     if английское_слово in англо_французский_словарь:
#         перевод = англо_французский_словарь[английское_слово]['перевод']
#         print(f"Перевод '{английское_слово}': {перевод}")
#     else:
#         print(f"Слово '{английское_слово}' не найдено в словаре.")
#
# def заменить_перевод(английское_слово, новый_французский_перевод):
#     """Заменяет перевод английского слова."""
#     if английское_слово in англо_французский_словарь:
#         англо_французский_словарь[английское_слово]['перевод'] = новый_французский_перевод
#         print(f"Перевод для '{английское_слово}' изменен на '{новый_французский_перевод}'.")
#     else:
#         print(f"Слово '{английское_слово}' не найдено в словаре.")
#
# def вывести_весь_словарь():
#     """Выводит все записи из словаря."""
#     if not англо_французский_словарь:
#         print("Словарь пуст.")
#         return
#     print("Англо-французский словарь:")
#     for англ_слово, данные in англо_французский_словарь.items():
#         print(f"- {англ_слово}: {данные['перевод']}")
#
# # Пример использования:
# добавить_перевод("hello", "bonjour")
# добавить_перевод("goodbye", "au revoir")
# добавить_перевод("hello", "salut") # Попытка добавить существующее
#
# print("\n--- Поиск ---")
# поиск_перевода("hello")
# поиск_перевода("thank you")
#
# print("\n--- Замена ---")
# заменить_перевод("goodbye", "adieu")
# заменить_перевод("please", "s'il vous plaît") # Несуществующее
#
# print("\n--- Вывод всего ---")
# вывести_весь_словарь()
#
# print("\n--- Удаление ---")
# удалить_перевод("hello")
# удалить_перевод("ciao") # Несуществующее
#
# print("\n--- Вывод всего после удаления ---")
# вывести_весь_словарь()
#
# Задание 3: Программа "Фирма"
# Описание: Программа для хранения информации о человеке (ФИО, телефон, email, должность, кабинет, Skype) с возможностью добавления, удаления, поиска и замены данных.
#
#
#
# def добавить_сотрудника(фио, телефон, email, должность, кабинет, skype):
#     """Добавляет сотрудника в словарь."""
#     if фио in сотрудники_фирмы:
#         print(f"Сотрудник с ФИО '{фио}' уже существует.")
#     else:
#         сотрудники_фирмы[фио] = {
#             'телефон': телефон,
#             'email': email,
#             'должность': должность,
#             'кабинет': кабинет,
#             'skype': skype
#         }
#         print(f"Сотрудник '{фио}' успешно добавлен.")
#
# def удалить_сотрудника(фио):
#     """Удаляет сотрудника из словаря."""
#     if фио in сотрудники_фирмы:
#         del сотрудники_фирмы[фио]
#         print(f"Сотрудник '{фио}' успешно удален.")
#     else:
#         print(f"Сотрудник с ФИО '{фио}' не найден.")
#
# def поиск_сотрудника(фио):
#     """Ищет сотрудника по ФИО и выводит его информацию."""
#     if фио in сотрудники_фирмы:
#         info = сотрудники_фирмы[фио]
#         print(f"---- Информация о сотруднике: {фио} ----")
#         print(f"  Телефон: {info['телефон']}")
#         print(f"  Email: {info['email']}")
#         print(f"  Должность: {info['должность']}")
#         print(f"  Кабинет: {info['кабинет']}")
#         print(f"  Skype: {info['skype']}")
#         print("---------------------------------------")
#     else:
#         print(f"Сотрудник с ФИО '{фио}' не найден.")
#
# def заменить_данные_сотрудника(фио, телефон=None, email=None, должность=None, кабинет=None, skype=None):
#     """Заменяет указанные данные сотрудника."""
#     if фио in сотрудники_фирмы:
#         if телефон is not None:
#             сотрудники_фирмы[фио]['телефон'] = телефон
#         if email is not None:
#             сотрудники_фирмы[фио]['email'] = email
#         if должность is not None:
#             сотрудники_фирмы[фио]['должность'] = должность
#         if кабинет is not None:
#             сотрудники_фирмы[фио]['кабинет'] = кабинет
#         if skype is not None:
#             сотрудники_фирмы[фио]['skype'] = skype
#         print(f"Данные сотрудника '{фио}' успешно обновлены.")
#     else:
#         print(f"Сотрудник с ФИО '{фио}' не найден.")
#
# def вывести_всех_сотрудников():
#     """Выводит информацию обо всех сотрудниках."""
#     if not сотрудники_фирмы:
#         print("Список сотрудников фирмы пуст.")
#         return
#     print("\n--- Список сотрудников фирмы ---")
#     for фио, info in сотрудники_фирмы.items():
#         print(f"ФИО: {фио}")
#         print(f"  Телефон: {info['телефон']}")
#         print(f"  Email: {info['email']}")
#         print(f"  Должность: {info['должность']}")
#         print(f"  Кабинет: {info['кабинет']}")
#         print(f"  Skype: {info['skype']}")
#         print("-" * 20)
#     print("------------------------------")
#
# # Пример использования:
# добавить_сотрудника("Иванов Иван Иванович", "+7 (123) 456-78-90", "ivanov@firm.com", "Разработчик", "№101", "ivan_skype")
# добавить_сотрудника("Петрова Анна Сергеевна", "+7 (987) 654-32-10", "petrova@firm.com", "Менеджер", "№205", "anna_petrova")
# добавить_сотрудника("Иванов Иван Иванович", "+7 (111) 222-33-44", "ivanov.i@firm.com", "Старший Разработчик", "№102", "ivan_skype_pro") # Попытка добавить существующего
#
# print("\n--- Поиск ---")
# поиск_сотрудника("Петрова Анна Сергеевна")
# поиск_сотрудника("Сидоров Петр Николаевич")
#
# print("\n--- Замена ---")
# заменить_данные_сотрудника("Иванов Иван Иванович", кабинет="№105", skype="ivan_i_ivanov")
# заменить_данные_сотрудника("Смирнова Елена", телефон="+7 (555) 555-55-55") # Несуществующий
#
# print("\n--- Вывод всех ---")
# вывести_всех_сотрудников()
#
# print("\n--- Удаление ---")
# удалить_сотрудника("Петрова Анна Сергеевна")
# удалить_сотрудника("Васильев Юрий") # Несуществующий
#
# print("\n--- Вывод всех после удаления ---")
# вывести_всех_сотрудников()
# Задание 4: Программа "Книжная коллекция"
# Описание: Программа для хранения информации о книгах (автор, название, жанр, год выпуска, количество страниц, издательство) с возможностью добавления, удаления, поиска и замены данных.
#
#
#
#
# def добавить_книгу(название, автор, жанр, год_выпуска, количество_страниц, издательство):
#     """Добавляет книгу в коллекцию."""
#     if название in книжная_коллекция:
#         print(f"Книга с названием '{название}' уже существует.")
#     else:
#         книжная_коллекция[название] = {
#             'автор': автор,
#             'жанр': жанр,
#             'год_выпуска': год_выпуска,
#             'количество_страниц': количество_страниц,
#             'издательство': издательство
#         }
#         print(f"Книга '{название}' успешно добавлена.")
#
# def удалить_книгу(название):
#     """Удаляет книгу из коллекции."""
#     if название in книжная_коллекция:
#         del книжная_коллекция[название]
#         print(f"Книга '{название}' успешно удалена.")
#     else:
#         print(f"Книга с названием '{название}' не найдена.")
#
# def поиск_по_названию_книги(название):
#     """Ищет книгу по названию и выводит ее информацию."""
#     if название in книжная_коллекция:
#         info = книжная_коллекция[название]
#         print(f"---- Информация о книге: {название} ----")
#         print(f"  Автор: {info['автор']}")
#         print(f"  Жанр: {info['жанр']}")
#         print(f"  Год выпуска: {info['год_выпуска']}")
#         print(f"  Количество страниц: {info['количество_страниц']}")
#         print(f"  Издательство: {info['издательство']}")
#         print("------------------------------------")
#     else:
#         print(f"Книга с названием '{название}' не найдена.")
#
# def поиск_книг_по_автору(автор):
#     """Ищет книги по автору и выводит их информацию."""
#     найденные_книги = []
#     for название, info in книжная_коллекция.items():
#         if info['автор'].lower() == автор.lower(): # Поиск без учета регистра
#             найденные_книги.append((название, info))
#
#     if not найденные_книги:
#         print(f"Книги автора '{автор}' не найдены.")
#         return
#
#     print(f"---- Книги автора: {автор} ----")
#     for название, info in найденные_книги:
#         print(f"  Название: {название}")
#         print(f"    Жанр: {info['жанр']}, Год: {info['год_выпуска']}, Страниц: {info['количество_страниц']}, Издательство: {info['издательство']}")
#     print("-------------------------------")
#
#
# def заменить_данные_книги(название, автор=None, жанр=None, год_выпуска=None, количество_страниц=None, издательство=None):
#     """Заменяет указанные данные книги."""
#     if название in книжная_коллекция:
#         if автор is not None:
#             книжная_коллекция[название]['автор'] = автор
#         if жанр is not None:
#             книжная_коллекция[название]['жанр'] = жанр
#         if год_выпуска is not None:
#             книжная_коллекция[название]['год_выпуска'] = год_выпуска
#         if количество_страниц is not None:
#             книжная_коллекция[название]['количество_страниц'] = количество_страниц
#         if издательство is not None:
#             книжная_коллекция[название]['издательство'] = издательство
#         print(f"Данные книги '{название}' успешно обновлены.")
#     else:
#         print(f"Книга с названием '{название}' не найдена.")
#
# def вывести_всю_коллекцию():
#     """Выводит информацию обо всех книгах в коллекции."""
#     if not книжная_коллекция:
#         print("Книжная коллекция пуста.")
#         return
#     print("\n--- Ваша Книжная Коллекция ---")
#     for название, info in книжная_коллекция.items():
#         print(f"Название: {название}")
#         print(f"  Автор: {info['автор']}")
#         print(f"  Жанр: {info['жанр']}")
#         print(f"  Год выпуска: {info['год_выпуска']}")
#         print(f"  Количество страниц: {info['количество_страниц']}")
#         print(f"  Издательство: {info['издательство']}")
#         print("-" * 20)
#     print("----------------------------")
#
# # Пример использования:
# добавить_книгу("Мастер и Маргарита", "Михаил Булгаков", "Роман", 1967, 384, "Высшая школа")
# добавить_книгу("1984", "Джордж Оруэлл", "Антиутопия", 1949, 328, "Secker & Warburg")
# добавить_книгу("Мастер и Маргарита", "М. Булгаков", "Фантастика", 1968, 380, "АСТ") # Попытка добавить существующее
#
# print("\n--- Поиск по названию ---")
# поиск_по_названию_книги("1984")
# поиск_по_названию_книги("Война и мир")
#
# print("\n--- Поиск по автору ---")
# поиск_книг_по_автору("Михаил Булгаков")
# поиск_книг_по_автору("Лев Толстой")
#
# print("\n--- Замена ---")
# заменить_данные_книги("1984", жанр="Дистопия", количество_страниц=330)
# заменить_данные_книги("Преступление и наказание", автор="Ф. Достоевский") # Несуществующее
#
# print("\n--- Вывод всей коллекции ---")
# вывести_всю_коллекцию()
#
# print("\n--- Удаление ---")
# удалить_книгу("1984")
# удалить_книгу("Евгений Онегин") # Несуществующее
#
# print("\n--- Вывод всей коллекции после удаления ---")
# вывести_всю_коллекцию()