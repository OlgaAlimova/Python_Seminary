# задание с каникул, но нужно добавить логирование несортированых
# сообщения и запуск из терминала

import csv
import re
import logging
import argparse

# Настройка логирования
logging.basicConfig(filename='email_categorization.log', level=logging.INFO)

# Создаем словарь с ключевыми словами для каждой категории
categories = {
    "Security": ["security", "threat", "breach"],
    "Refunds": ["refund", "return", "chargeback"],
    "Troubleshooting": ["problem", "issue", "error"],

}

# Функция для категоризации письма
def categorize_email(email_text):
    email_text = email_text.lower()  # Переводим текст в нижний регистр для регистронезависимого сравнения

    categorized = []  # Список для хранения категорий, к которым относится письмо

    # Проходим по каждой категории и проверяем наличие ключевых слов
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(rf'\b{keyword}\b', email_text):  # Ищем ключевое слово в тексте
                categorized.append(category)  # Если найдено, добавляем категорию

    if not categorized:
        categorized.append("Uncategorized")  # Если письмо не отнеслось ни к одной категории

    return categorized

# Функция для чтения и категоризации писем из CSV-файла
def categorize_emails(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)  # Считываем заголовок

            # Определяем индекс столбца с текстом письма (предположим, это второй столбец)
            text_column_index = header.index("EmailText")

            categorized_emails = []

            for row in reader:
                email_text = row[text_column_index]  # Получаем текст письма
                categories = categorize_email(email_text)  # Категоризируем письмо
                categorized_emails.append([row[0], email_text, ', '.join(categories)])  # Сохраняем результат

                # Логируем несортированные сообщения
                if "Uncategorized" in categories:
                    logging.info(f"Uncategorized email: {email_text}")

        # Записываем результаты в новый CSV-файл
        with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(["EmailID", "EmailText", "Categories"])  # Записываем заголовок
            writer.writerows(categorized_emails)  # Записываем категоризированные письма

        print("Categorization complete. Results saved to", output_file)
    except FileNotFoundError:
        print("File not found. Please provide a valid input file.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Email Categorization")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    args = parser.parse_args()

    categorize_emails(args.input, args.output)

