# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть
# дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def find_duplicates(input_list):
    # Создаем словарь для подсчета количества повторений элементов
    element_counts = {}

    # Подсчитываем количество повторений каждого элемента в списке
    for element in input_list:
        element_counts[element] = element_counts.get(element, 0) + 1

    # Выводим только те элементы, у которых количество повторений больше 1
    duplicates = [element for element, count in element_counts.items() if count > 1]

    return duplicates


def main():
    try:
        input_list = input("Введите список повторяющихся элементов через запятую: ").split(',')
        input_list = [element.strip() for element in input_list]

        duplicates = find_duplicates(input_list)

        if duplicates:
            print("Повторяющиеся элементы:", ", ".join(map(str, duplicates)))
        else:
            print("Нет повторяющихся элементов.")

    except ValueError:
        print("Ошибка: Введите список элементов в правильном формате.")


if __name__ == "__main__":
    main()
