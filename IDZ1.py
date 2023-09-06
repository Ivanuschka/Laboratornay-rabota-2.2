n = int(input("Введите натуральное число: "))

last_digit = n % 10

second_last_digit = n % 100 // 10

if second_last_digit != 1 and last_digit == 1:
    word = "год"
elif 2 <= last_digit <= 4 and (second_last_digit != 1 or second_last_digit is None):
    word = "года"
else:
    word = "лет"

print(f"Мне {n} {word}.")
