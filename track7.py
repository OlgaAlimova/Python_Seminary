# Создайте словарь со списком вещей для похода в качестве ключа и
# их массой в качестве значения. Определите какие вещи влезут в
# рюкзак передав его максимальную грузоподъёмность. Достаточно
# вернуть один допустимый вариант. *Верните все возможные варианты
# комплектации рюкзака.

def find_possible_combinations(items, max_weight, current_combination=None, current_weight=0, index=0):
    if current_combination is None:
        current_combination = []

    # Если достигли конца списка предметов, возвращаем текущий набор
    if index == len(items):
        return [current_combination]

    # Рекурсивно ищем возможные комбинации с текущим предметом
    combination_with_current = []
    if current_weight + items[index][1] <= max_weight:
        combination_with_current = find_possible_combinations(
            items, max_weight, current_combination + [items[index]], current_weight + items[index][1], index + 1
        )

    # Рекурсивно ищем возможные комбинации без текущего предмета
    combination_without_current = find_possible_combinations(
        items, max_weight, current_combination, current_weight, index + 1
    )

    # Объединяем оба набора предметов
    return combination_with_current + combination_without_current

def main():
    items = {
        "Спальник": 2,
        "Термос": 1,
        "Палатка": 3,
        "Еда": 4,
        "Кружка": 1,
        "Фонарик": 2
    }
    max_weight = 6

    items_list = list(items.items())
    combinations = find_possible_combinations(items_list, max_weight)

    print("Возможные варианты комплектации рюкзака:")
    for combination in combinations:
        print(", ".join(item[0] for item in combination))

if __name__ == "__main__":
    main()
