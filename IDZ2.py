animal_cycle = {
    0: "мыши", 1: "коровы", 2: "тигра", 3: "зайца",
    4: "дракона", 5: "змеи", 6: "лошади", 7: "овцы",
    8: "обезьяны", 9: "курицы", 10: "собаки", 11: "свиньи"
}

color_cycle = {
    0: "зеленый", 1: "красный", 2: "желтый", 3: "белый", 4: "черный"
}

year = int(input("Введите год: "))

cycle_year = (year - 1984) % 60

animal_index = cycle_year % 12

color_index = cycle_year % 5

animal_name = animal_cycle[animal_index]
color_name = color_cycle[color_index]

# Выводим результат
print(f"{year} - год {color_name} {animal_name}.")
