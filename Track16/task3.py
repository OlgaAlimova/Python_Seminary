# Перемножение пар чисел и сохранение результатов

def multiply_numbers(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            int_num, float_num = map(float, line.strip().split('|'))
            product = int_num * float_num
            if product < 0:
                result_line = f"{line.strip().lower()}|{abs(product):.2f}\n"
            else:
                result_line = f"{line.strip().upper()}|{round(product)}\n"
            output_f.write(result_line)

__all__ = ["multiply_numbers"]

# Пример использования
if __name__ == "__main__":
    input_file = "random_numbers.txt"
    output_file = "results.txt"
    multiply_numbers(input_file, output_file)
    print(f"Результаты перемножения сохранены в файл '{output_file}'.")
