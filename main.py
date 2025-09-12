'''
print('Hello World')
#функция принт нужна для вывода данных в окно консоли#
name = input("Скажи своё имя:")
#переменная которая хранит в себе строку#
age = int(input("Введите свой возраст"))
#переменная которая хранит в себе целочисленное число#
print(type(age), type(name))
water = 4.5
#переменная которая хранит в себе дробь#
print('Привет,' , name, 'тебе', age, 'лет')
print('Я пью ', water, 'литров воды')
'''
'''
answer = int(input("Сколько будет 5*8:10:"))
print('Правильный Ответ 4, ваш ответ: ', answer)
'''
'''
Пользователь вводит с клавиатуры 3 числа необходимо найти сумму чисел найти произведение чисел найти разность чисел найти разделения
результат вычислений операций вывести на экран
'''
'''
num1 = int(input("Введите 1 число"))
num2 = int(input("Введите 2 число"))
num3 = int(input("Введите 3 число"))
print("Сумма ", num1 + num2 + num3, "Умножение ", num1 * num2 * num3)
'''

'''
print("Сегодня 5 сентября , " 'Я Измученный пришел на первую пару', 'к 8:15' , sep='\t', end=' ')

#\t - текствоя тагуляция ( 3 пробела) \n - перенос на новую строку  sep - отступы между параметрами print  end - завершение строки#

print('Желаю \'всем\'  продуктивного дня!')
'''
'''
name = input('Введите имя:')
s_name = input('Фамилия:')
age = int(input("Введите ваш возраст"))
date = int(input("Введите ваш год рождения:"))
print(f"Ваше имя: {name} \n"  f"Ваша фамилия: {s_name} \n"  f"Ваша дата рождения: {date} \n"  f"Ваш возраст: {age}")
# Обращение f" или f' и f~ нужно для форматирования текста и вставки переменных в строку 
'''
'''
Арифметические опперации python
 +-/* ( )
**  оператор возведения в степень
print(2+2) #4
// - целочисленное деление 
print(6,31 // 3) #2
% - деление по остатку
print(6%2) #0
Что делать не надо: 
1.делить на 0 нельзя 
2.делить целое число на 0
3.находить остаток от деления на 0
функция суммы - sum(123)#6
функция минимума - min(1,2,3)#1
функция максимума - max(1,2,3)#3
'''

'''
num1 = int(input("Введите зп: "))
num2 = int(input("Введите сумму месячного платежа:"))
num3 = int(input("Введите задолженность:"))
print("Сумма ", num1 - num2 - num3)
'''
'''
d1 = int(input("Длина 1 диагонали:"))
d2 = int(input("Длина 2 диагонали:"))
print("Длина 2 диагоналей", d1 * d2 /2)
'''
'''
print("To be", '\n' "or not" '\n' "to be")
'''

'''
#условные конструкции
age = int(input("Введите ваш возраст: "))
#if (Условие == true:
# функция действие
if age < 10 :
    print("тЫ ЕЩЕ МАЛЫШ")
else:
    print("Вы уже взрослый")
'''
'''
age = int(input("Введите ваш возраст: "))
if 0 < age < 10 :
        print("Ты еще малыш")
    if age < 20 and age < 10 :
        print("Ты еще подросток")
    if 20 < age < 45 :
        print("Ты молодеж")
    if 45 < age < 100 :
        print("Ты уже пенсионер")
    else:
        print("Некорректный возраст")
'''
'''
#ДЗ ЗАДАНИЕ 1
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

operation = input("Выберите операцию (сумма/произведение): ").lower()

if operation == "сумма":
    result = num1 + num2 + num3
elif operation == "произведение":
    result = num1 * num2 * num3
else:
    print("Некорректный выбор операции.")
    exit()

print("Результат:", result)

#ДЗ ЗАДАНИЕ 2

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

operation = input("Выберите операцию (максимум/минимум/среднее): ").lower()

if operation == "максимум":
    result = max(num1, num2, num3)
elif operation == "минимум":
    result = min(num1, num2, num3)
elif operation == "среднее":
    result = (num1 + num2 + num3) / 3
else:
    print("Некорректный выбор операции.")
    exit()

print("Результат:", result)

#ДЗ ЗАДАНИЕ 3

meters = float(input("Введите количество метров: "))

unit = input("Выберите единицу измерения для перевода (мили/дюймы/ярды): ").lower()

if unit == "мили":
    result = meters * 0.000621371
elif unit == "дюймы":
    result = meters * 39.3701
elif unit == "ярды":
    result = meters * 1.09361
else:
    print("Некорректный выбор единицы измерения.")
    exit()

print("Результат:", result, unit)

'''
'''
#ДЗ ЗАДАНИЕ 1
number = int(input("Введите число от 1 до 100: "))

if 1 <= number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("Ошибка: число должно быть в диапазоне от 1 до 100.")
    '''
'''
#ДЗ ЗАДАНИЕ 2
    base = float(input("Введите число: "))
exponent = int(input("Введите степень (от 0 до 7): "))

if 0 <= exponent <= 7:
    result = base ** exponent
    print(f"{base} в степени {exponent} равно {result}")
else:
    print("Ошибка: степень должна быть в диапазоне от 0 до 7.")
    '''
    '''
    #ДЗ ЗАДАНИЕ 3
cost_per_minute = float(input("Введите стоимость разговора за минуту: "))
operator_from = input("Выберите оператора, с которого звоните: ")
operator_to = input("Выберите оператора, на который звоните: ")

# Пример тарифов
tariffs = {
    ("OperatorA", "OperatorB"): 1.0,
    ("OperatorA", "OperatorC"): 1.2,
    ("OperatorB", "OperatorA"): 0.9,
    ("OperatorB", "OperatorC"): 1.1,
    ("OperatorC", "OperatorA"): 1.3,
    ("OperatorC", "OperatorB"): 0.8,
}

if (operator_from, operator_to) in tariffs:
    tariff = tariffs[(operator_from, operator_to)]
    total_cost = cost_per_minute * tariff
    print(f"Стоимость разговора: {total_cost:.2f}")
else:
    print("Ошибка: тариф не найден.")
'''
'''
#ДЗ ЗАДАНИЕ 4
def calculate_salary(sales):
    base_salary = 200
    if sales < 500:
        commission = sales * 0.03
    elif 500 <= sales <= 1000:
        commission = sales * 0.05
    else:
        commission = sales * 0.08
    return base_salary + commission

sales_manager1 = float(input("Введите уровень продаж для менеджера 1: "))
sales_manager2 = float(input("Введите уровень продаж для менеджера 2: "))
sales_manager3 = float(input("Введите уровень продаж для менеджера 3: "))

salary_manager1 = calculate_salary(sales_manager1)
salary_manager2 = calculate_salary(sales_manager2)
salary_manager3 = calculate_salary(sales_manager3)

max_salary = max(salary_manager1, salary_manager2, salary_manager3)
if max_salary == salary_manager1:
    salary_manager1 += 200  # Премия
elif max_salary == salary_manager2:
    salary_manager2 += 200  # Премия
else:
    salary_manager3 += 200  # Премия

print(f"Зарплата менеджера 1: {salary_manager1}")
print(f"Зарплата менеджера 2: {salary_manager2}")
print(f"Зарплата менеджера 3: {salary_manager3}")
'''

