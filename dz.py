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
