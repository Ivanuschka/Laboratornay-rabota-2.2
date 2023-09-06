n = int(input("Введите натуральное число: "))

# Определяем последнюю цифру числа
last_digit = n % 10

# Определяем предпоследнюю цифру числа (если она есть)
second_last_digit = n % 100 // 10

# Проверяем условия для склонения слова "год"
if second_last_digit != 1 and last_digit == 1:
    word = "год"
elif 2 <= last_digit <= 4 and (second_last_digit != 1 or second_last_digit is None):
    word = "года"
else:
    word = "лет"

# Выводим фразу на экран
print(f"Мне {n} {word}.")
