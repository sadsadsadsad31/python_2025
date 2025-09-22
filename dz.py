'''
# задание 1

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)

#задание 2

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for number in range(start, end + 1):
    print(number, end=" ")
print()

for number in range(end, start - 1, -1):
    print(number, end=" ")
print()

for number in range(start, end + 1):
    if number % 7 == 0:
        print(number, end=" ")
print()

count = 0
for number in range(start, end + 1):
    if number % 5 == 0:
        count += 1
print("Количество чисел, кратных 5:", count)

#задание 3
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
'''

#дз Модуль 3. Циклы. Часть
#1
'''
number = int(input("Введите число: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
'''
#2
'''
def currency_converter():
    rates = {
        'USD': 75.0,  # Пример курса рубля к доллару
        'EUR': 85.0,  # Пример курса рубля к евро
        'RUB': 1.0
    }
    while True:
        print("\nМеню конвертера:")
        print("1. Рубли в доллары")
        print("2. Доллары в рубли")
        print("3. Рубли в евро")
        print("4. Евро в рубли")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '0':
            break
        elif choice == '1':
            sum_rub = float(input("Введите сумму в рублях: "))
            print(f"{sum_rub} RUB = {sum_rub / rates['USD']:.2f} USD")
        elif choice == '2':
            sum_usd = float(input("Введите сумму в долларах: "))
            print(f"{sum_usd} USD = {sum_usd * rates['USD']:.2f} RUB")
        elif choice == '3':
            sum_rub = float(input("Введите сумму в рублях: "))
            print(f"{sum_rub} RUB = {sum_rub / rates['EUR']:.2f} EUR")
        elif choice == '4':
            sum_eur = float(input("Введите сумму в евро: "))
            print(f"{sum_eur} EUR = {sum_eur * rates['EUR']:.2f} RUB")
        else:
            print("Некорректный выбор. Попробуйте снова.")

currency_converter()
'''
'''
#3
lower = int(input("Введите нижнюю границу диапазона: "))
upper = int(input("Введите верхнюю границу диапазона: "))

while True:
    num = int(input("Введите число: "))
    if lower <= num <= upper:
        break
    else:
        print("Число вне диапазона, попробуйте снова.")

for i in range(lower, upper + 1):
    if i == num:
        print(f"!{i}!", end=' ')
    else:
        print(i, end=' ')
print()
'''
'''
#4
import random
import time

print("Игра 'Угадай число' от 1 до 500. Введите 0, чтобы выйти.")

target = random.randint(1, 500)
attempts = 0
start_time = time.time()

while True:
    guess = int(input("Ваш вариант: "))
    if guess == 0:
        print("Игра завершена.")
        break
    attempts += 1
    if guess == target:
        elapsed = time.time() - start_time
        print(f"Поздравляем! Вы угадали число за {attempts} попыток и {elapsed:.2f} секунд.")
        break
    elif guess < target:
        print("Больше.")
    else:
        print("Меньше.")
'''